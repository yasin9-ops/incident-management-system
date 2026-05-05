from app.services.incident_service import process_signal
from app.utils.metrics import increment
from app.core.mongo import signals_collection

async def handle_signal(signal):
    signals_collection.insert_one(signal.dict())
    process_signal(signal)
    increment()