from typing import Literal

from pydantic import BaseModel, Field
from models.meeting import Meeting


ConversationStatus = Literal[
	"collecting_info",
	"awaiting_confirmation",
	"confirmed",
	"cancelled",
]


class ConversationState(BaseModel):
	status: ConversationStatus = "collecting_info"
	meeting: Meeting = Field(default_factory=Meeting)

def merge_meeting(state: ConversationState, updates: Meeting) -> None:
    for field, value in updates.model_dump().items():
        if value is not None and value != []:
            setattr(state.meeting, field, value)

