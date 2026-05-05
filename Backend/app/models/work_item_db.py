from sqlalchemy import Column, String, DateTime, Text
from datetime import datetime
from app.core.database import Base

class WorkItemDB(Base):
    __tablename__ = "work_items"

    component_id = Column(String, primary_key=True, index=True)
    status = Column(String, default="OPEN")
    start_time = Column(DateTime, default=datetime.utcnow)
    end_time = Column(DateTime, nullable=True)
    rca = Column(Text, nullable=True)
    severity = Column(String, default="P2")