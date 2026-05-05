from fastapi import APIRouter, BackgroundTasks, Request
from slowapi import Limiter
from slowapi.util import get_remote_address

from app.schemas.signal import Signal
from app.schemas.rca import RCA
from app.services.incident_service import get_all_incidents, update_status
from app.workers.signal_worker import handle_signal
from app.core.mongo import signals_collection

from typing import List
from pydantic import BaseModel

router = APIRouter()

limiter = Limiter(key_func=get_remote_address)

class IncidentResponse(BaseModel):
    component_id: str
    status: str
    severity: str

@router.post("/signals")
@limiter.limit("10/second")
async def ingest_signal(request: Request, signal: Signal, bg: BackgroundTasks):
    bg.add_task(handle_signal, signal)
    return {
        "status": "accepted",
        "component_id": signal.component_id
    }


@router.get("/incidents", response_model=List[IncidentResponse])
def get_incidents():
    return get_all_incidents()


@router.post("/incident/{component_id}/status")
def change_status(component_id: str, status: str, rca: RCA = None):
    return update_status(component_id, status, rca)


@router.get("/incident/{component_id}/signals")
def get_incident_signals(component_id: str):
    signals = list(signals_collection.find({"component_id": component_id}, {"_id": 0}))
    return signals