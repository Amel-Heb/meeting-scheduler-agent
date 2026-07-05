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

from typing import Any, Callable, Dict, Optional


class SchedulerAgent:
    def __init__(self, tools: Dict[str, Any]) -> None:
        self.tools = tools

    def understand_request(self, request: str) -> Dict[str, Any]:
        """Interprète la demande utilisateur et renvoie l'intention et les entités."""
        normalized = request.strip().lower()

        if "annuler" in normalized or "supprimer" in normalized:
            intent = "cancel_meeting"
        elif "déplacer" in normalized or "reprogrammer" in normalized or "changer" in normalized:
            intent = "reschedule_meeting"
        elif "disponibilité" in normalized or "dispo" in normalized:
            intent = "check_availability"
        else:
            intent = "schedule_meeting"

        return {
            "intent": intent,
            "entities": {},
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