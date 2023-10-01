from typing import List
from pydantic import BaseModel

class HealthzResponse(BaseModel):
    status: str
    uptime: str

class HireMeResponse(BaseModel):
    person: str
    position: str
    company: str
    reasons: List[str]