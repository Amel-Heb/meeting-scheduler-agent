from pydantic import BaseModel
from typing import Optional


class Meeting(BaseModel):
    subject: Optional[str] = None
    participants: list[str] = []
    day: Optional[str] = None
    time: Optional[str] = None
    duration: Optional[int] = None
    location: Optional[str] = None

class MeetingRequest(BaseModel):
    intent: str
    entities: Meeting
    