from datetime import datetime
from app.core.database import SessionLocal
from app.models.work_item_db import WorkItemDB
from app.core.redis_client import redis_client
from app.services.state_manager import can_transition
from app.services.alert_strategy import get_strategy
import json

VALID_STATES = ["OPEN", "INVESTIGATING", "RESOLVED", "CLOSED"]
DEBOUNCE_WINDOW = 10  # seconds


def process_signal(signal):
    db = SessionLocal()
    try:
        item = db.query(WorkItemDB).filter_by(component_id=signal.component_id).first()

        if item:
            time_diff = (datetime.utcnow() - item.start_time).seconds

            if time_diff < DEBOUNCE_WINDOW:
                return item
            else:
                item.start_time = datetime.utcnow()
                item.severity = signal.severity
        else:
            item = WorkItemDB(
                component_id=signal.component_id,
                severity=signal.severity
            )
            db.add(item)

        # Strategy pattern
        strategy = get_strategy(signal.severity)
        strategy.send(signal.component_id)

        db.commit()
        redis_client.delete("incidents")

        return item
    finally:
        db.close()


def get_all_incidents():
    # Try cache first
    cached = redis_client.get("incidents")
    if cached:
        return json.loads(cached)

    db = SessionLocal()
    try:
        items = db.query(WorkItemDB).all()

        result = [
            {
                "component_id": i.component_id,
                "status": i.status,
                "severity": i.severity
            }
            for i in items
        ]

        # Store in cache
        redis_client.set("incidents", json.dumps(result))

        return result

    finally:
        db.close()


def update_status(component_id, new_status, rca=None):
    db = SessionLocal()
    try:
        item = db.query(WorkItemDB).filter_by(component_id=component_id).first()

        if not item:
            return {"error": "Not found"}

        # STATE PATTERN CHECK (exact place)
        if not can_transition(item.status, new_status):
            return {"error": f"Invalid transition from {item.status} to {new_status}"}

        if new_status == "CLOSED":
            if not rca or not rca.root_cause or not rca.fix:
                return {"error": "RCA required"}

            item.rca = rca.root_cause
            item.end_time = datetime.utcnow()

            mttr = (item.end_time - item.start_time).total_seconds()
        else:
            mttr = None

        item.status = new_status
        db.commit()

        redis_client.delete("incidents")

        return {
            "message": "Updated",
            "mttr_seconds": mttr
        }

    finally:
        db.close()