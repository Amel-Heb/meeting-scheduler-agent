from pydantic import BaseModel 
from typing import Optional 

class meeting(BaseModel):
    participant: str
    date: str 
    time_period: str
    duration: int = 30 
    topic: Optional[str] = None 