from pydantic import BaseModel

class RCA(BaseModel):
    root_cause: str
    fix: str
    prevention: str