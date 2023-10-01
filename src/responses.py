from typing import List
from pydantic import BaseModel

class HealthzResponse(BaseModel):
    status: str
    uptime: str

class HireMeResponse(BaseModel):
    reasons: List[str]