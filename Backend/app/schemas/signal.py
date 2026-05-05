from pydantic import BaseModel, Field
from datetime import datetime

class Signal(BaseModel):
    component_id: str = Field(..., min_length=2)
    severity: str
    message: str
    timestamp: datetime