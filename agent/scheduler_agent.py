"""
Scheduler Agent

Responsabilité :
Coordonner les outils afin de répondre à une demande de planification.

Ce fichier ne réalise aucune action lui-même.

Il décide :

1. Comprendre la demande utilisateur
2. Identifier l'action à effectuer
3. Choisir le bon tool
4. Exécuter le tool
5. Retourner le résultat
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from models.llm import extract_meeting_request, extract_meeting_update
from models.conversation import ConversationState, merge_meeting


class SchedulerAgent:
    def __init__(self, tools: Dict[str, Any]) -> None:
        self.tools = tools
        self.state = ConversationState()

    def update_conversation(self, user_message: str) -> None:
        """Update the meeting state with information from a user message."""

        updates = extract_meeting_update(user_message)
        merge_meeting(self.state, updates)

        if not self.get_missing_fields():
            self.state.status = "awaiting_confirmation"
        else:
            self.state.status = "collecting_info"

    def get_missing_fields(self) -> list[str]:
        """Return the meeting fields that still need information."""

        required_fields = [
            "subject",
            "participants",
            "day",
            "time",
            "duration",
            "location",
        ]

        meeting_data = self.state.meeting.model_dump()

        return [
            field
            for field in required_fields
            if not meeting_data.get(field)
        ]
    def get_next_question(self) -> str | None:
        """Return the next question based on missing meeting fields."""

        questions = {
            "subject": "Quel est l'objet de la réunion ?",
            "participants": "Qui participera à la réunion ?",
            "day": "Quel jour souhaites-tu organiser la réunion ?",
            "time": "À quelle heure souhaites-tu la programmer ?",
            "duration": "Combien de temps doit durer la réunion ?",
            "location": "Où souhaites-tu organiser la réunion ?",
        }

        missing_fields = self.get_missing_fields()

        if not missing_fields:
            return None

        return questions[missing_fields[0]]

    def get_confirmation_summary(self) -> str:
        """Build a readable summary before user confirmation."""

        meeting = self.state.meeting

        participants = ", ".join(meeting.participants)

        return (
            "Voici le récapitulatif de ta réunion :\n"
            f"- Objet : {meeting.subject}\n"
            f"- Avec : {participants}\n"
            f"- Jour : {meeting.day}\n"
            f"- Heure : {meeting.time}\n"
            f"- Durée : {meeting.duration} minutes\n"
            f"- Lieu : {meeting.location}\n\n"
            "Souhaites-tu confirmer cette réunion ?"
        )
    
    def confirm_meeting(self, user_message: str) -> bool:
        """Confirm a meeting only when confirmation is expected."""

        if self.state.status != "awaiting_confirmation":
            return False

        confirmation_words = [
            "oui",
            "je confirme",
            "confirmer",
            "c'est bon",
            "ok",
        ]

        response = user_message.strip().lower()

        if response in confirmation_words:
            self.state.status = "confirmed"
            return True

        return False

    def cancel_meeting(self, user_message: str) -> bool:
        """Cancel a meeting draft when cancellation is explicit."""

        if self.state.status != "awaiting_confirmation":
            return False

        cancellation_words = [
            "non",
            "annule",
            "annuler",
            "je préfère annuler",
            "laisse tomber",
        ]

        response = user_message.strip().lower()

        if response in cancellation_words:
            self.state.status = "cancelled"
            return True

        return False

    def correct_meeting(self, user_message: str) -> bool:
        """Update a meeting draft before confirmation."""

        if self.state.status != "awaiting_confirmation":
            return False

        updates = extract_meeting_update(user_message)

        if not updates.model_dump(exclude_none=True, exclude_defaults=True):
            return False

        merge_meeting(self.state, updates)

        self.state.status = (
            "awaiting_confirmation"
            if not self.get_missing_fields()
            else "collecting_info"
        )

        return True

    def handle_conversation(self, user_message: str) -> str:
        """Handle one turn of a meeting scheduling conversation."""

        if self.state.status == "confirmed":
            return "Cette réunion a déjà été confirmée."

        if self.state.status == "cancelled":
            return "Cette demande de réunion a été annulée."

        if self.state.status == "awaiting_confirmation":
            if self.confirm_meeting(user_message):
                return "Réunion confirmée (simulation uniquement)."

            if self.cancel_meeting(user_message):
                return "Demande de réunion annulée."

            if self.correct_meeting(user_message):
                if self.state.status == "awaiting_confirmation":
                    return self.get_confirmation_summary()
                return self.get_next_question()

            return (
                "Je n'ai pas compris ta réponse. "
                "Tu peux confirmer, annuler ou modifier la réunion."
            )

        self.update_conversation(user_message)

        if self.state.status == "awaiting_confirmation":
            return self.get_confirmation_summary()

        return self.get_next_question()
    
    def understand_request(self, request: str) -> Dict[str, Any]:
        """Interprète la demande utilisateur avec le LLM."""

        parsed = extract_meeting_request(request)

        return {
            "intent": parsed.intent,
            "entities": parsed.entities.model_dump(),
        }


    def select_tool(self, intent: str) -> Optional[Any]:
        """Choisit le tool approprié en fonction de l'intention détectée."""
        routing = {
            "schedule_meeting": "calendar",
            "reschedule_meeting": "calendar",
            "cancel_meeting": "calendar",
            "check_availability": "availability",
        }
        tool_name = routing.get(intent)
        if tool_name is None:
            return None
        return self.tools.get(tool_name)

    def execute_tool(self, tool: Any, payload: Dict[str, Any]) -> Any:
        """Exécute le tool choisi avec les données de la demande."""
        if tool is None:
            raise ValueError("Aucun outil disponible pour exécuter la requête")

        if callable(tool):
            return tool(payload)

        if hasattr(tool, "run") and callable(getattr(tool, "run")):
            return tool.run(payload)

        raise TypeError("Le tool sélectionné n'est pas exécutable")

    def handle(self, request: str) -> Dict[str, Any]:
        """Traite une demande et retourne le résultat du tool choisi."""
        parsed = self.understand_request(request)

        if parsed["intent"] == "schedule_meeting":
            required_fields = [
                "subject",
                "participants",
                "day",
                "time",
                "duration",
                "location",
            ]

            missing_fields = [
                field
                for field in required_fields
                if not parsed["entities"].get(field)
            ]

            if missing_fields:
                return {
                    "request": request,
                    "intent": parsed["intent"],
                    "missing_fields": missing_fields,
                    "result": None,
                }

        tool = self.select_tool(parsed["intent"])

        payload = {
            "request": request,
            "intent": parsed["intent"],
            "entities": parsed["entities"],
        }

        result = self.execute_tool(tool, payload)

        return {
            "request": request,
            "intent": parsed["intent"],
            "tool": tool.__class__.__name__ if tool is not None else None,
            "result": result,
        }


def create_scheduler_agent(tools: Dict[str, Any]) -> SchedulerAgent:
    return SchedulerAgent(tools)

# Étape 1
# Comprendre la demande

# Étape 2
# Identifier le jour demandé

# Étape 3
# Choisir le tool à utiliser

# Étape 4
# Exécuter le tool

# Étape 5
# Retourner la réponse
