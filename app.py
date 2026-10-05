from agent.scheduler_agent import create_scheduler_agent
from tools.check_availability import check_availability
from tools.create_meeting_draft import create_meeting_draft

def availability_tool(payload):
    request = payload["request"].lower()

    if "mardi" in request:
        return check_availability("mardi")

    if "mercredi" in request:
        return check_availability("mercredi")

    return []


tools = {
    "availability": availability_tool,
    "calendar": create_meeting_draft,
}

agent = create_scheduler_agent(tools)

user_request = input("Vous : ")

result = agent.handle(user_request)

if "missing_fields" in result:
    labels = {
        "subject": "l'objet",
        "participants": "les participants",
        "day": "le jour",
        "time": "l'heure",
        "duration": "la durée",
        "location": "le lieu",
    }

    print("\nAgent : Il me manque quelques informations pour préparer la réunion :")

    for field in result["missing_fields"]:
        print(f"- {labels[field]}")

elif result["intent"] == "check_availability":
    available_slots = result["result"]

    if available_slots:
        print("\nAgent : Voici les créneaux disponibles :")

        for slot in available_slots:
            print(f"- {slot}")
    else:
        print("\nAgent : Je n’ai trouvé aucun créneau disponible.")

elif result["intent"] == "schedule_meeting":
    meeting = result["result"]

    print("\nAgent : Voici le brouillon de la réunion :")
    print(f"- Objet : {meeting['subject']}")
    print(f"- Participants : {', '.join(meeting['participants'])}")
    print(f"- Jour : {meeting['day']}")
    print(f"- Heure : {meeting['time']}")
    print(f"- Durée : {meeting['duration']} minutes")
    print(f"- Lieu : {meeting['location']}")
    