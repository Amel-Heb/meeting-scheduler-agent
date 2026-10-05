from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

from pathlib import Path

from models.meeting import MeetingRequest

client = OpenAI()

def extract_meeting_request(user_request: str) -> MeetingRequest:
    """Extrait les informations structurées d'une demande de réunion."""

    prompt_path = Path("prompts/meeting_extraction_prompt.txt")
    extraction_prompt = prompt_path.read_text(encoding="utf-8")

    response = client.responses.parse(
        model="gpt-5.6",
        instructions=extraction_prompt,
        input=user_request,
        text_format=MeetingRequest,
    )

    return response.output_parsed