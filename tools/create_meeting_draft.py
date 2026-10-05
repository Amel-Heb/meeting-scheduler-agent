def create_meeting_draft(payload):
	"""Crée un brouillon de réunion à partir des informations fournies."""

	entities = payload["entities"]

	meeting_draft = {
		"subject": entities.get("subject"),
		"participants": entities.get("participants", []),
		"day": entities.get("day"),
		"time": entities.get("time"),
		"duration": entities.get("duration"),
		"location": entities.get("location"),
	}

	return meeting_draft
