# Sprint 3 — Conversation & Human Validation

## Sprint Goal

Transform the Meeting Scheduler from a single-request agent into a conversational agent capable of progressively completing a scheduling request and obtaining human confirmation.

## User Story

As a user, I want to organize a meeting through a natural conversation, without repeating information I have already provided, so that scheduling feels simple and intuitive.

## Problem

At the end of Sprint 2, the agent can detect missing information, but it cannot collect it through a multi-turn conversation.

For example, when the user says:

> Organise une réunion avec Léa mardi.

The agent identifies the missing fields but displays them all at once.

The next challenge is to turn this technical validation into a natural conversational experience.

## Acceptance Criteria

- The agent remembers information provided across multiple turns.
- The agent identifies which information is still missing.
- The agent asks one relevant question at a time.
- The agent does not ask users to repeat information already provided.
- The agent prepares a complete meeting draft.
- The agent presents a summary before confirmation.
- The agent requires explicit confirmation before finalizing the simulated workflow.
- The user can refuse or correct the proposed meeting.

## Out of Scope

- Google Calendar integration
- Sending real invitations
- Persistent conversation history across application restarts
- Graphical chat interface

## Product Principle

**Ask only for what is missing. Never ask the user to repeat information already provided.**

## Conversation Design Decision 1 — Contextual Questions

### Decision

The agent should ask contextual questions rather than follow a rigid questionnaire.

### Rationale

The conversation should adapt to the information already provided by the user.

The agent must avoid asking unnecessary questions or repeating information already known.

### Behavioral Rules

- Identify missing information before asking a question.
- Ask only one question at a time.
- Prioritize questions according to the available context.
- Use a predictable fallback order when no contextual priority applies.
- Preserve previously collected information across turns.
- Never invent missing information.

### Design Principle

A conversational agent should adapt to the user, rather than forcing the user to adapt to a form.

## Conversation Design Decision 2 — Multi-Entity Responses

### Decision

The agent must extract all relevant information from every user message, even when it asks for only one specific field.

### Example

Agent:
> Quel est l'objet de la réunion ?

User:
> Une revue du prototype, à 14h, pendant 45 minutes.

The agent should update:

- subject: revue du prototype
- time: 14:00
- duration: 45

It should preserve previously collected information:

- participants: Léa
- day: mardi

The next question should concern only the remaining missing information:

> Où souhaites-tu organiser la réunion ?

### Behavioral Rules

- Process the entire user message, not only the answer to the last question.
- Merge newly extracted information with the existing conversation state.
- Preserve previously provided information unless the user explicitly corrects it.
- Recalculate missing fields after every turn.
- Ask only about information that remains missing.

### Product Principle

The user should be free to communicate naturally, without having to follow the agent's internal questionnaire.

## Conversation Design Decision 3 — Human Confirmation

### Decision

The agent must present a complete meeting summary and obtain explicit user confirmation before finalizing the simulated scheduling workflow.

### Behavioral Rules

- Present a clear summary when all required information is available.
- Never interpret silence or missing information as confirmation.
- Allow the user to confirm, correct, or cancel the proposal.
- If the user corrects information, update the meeting state.
- Present the updated proposal for confirmation.
- Never treat a correction as authorization to proceed.
- Do not claim that a real calendar event has been created.

### Confirmation States

- **Collecting information** — Required information is still missing.
- **Awaiting confirmation** — The proposal is complete and ready for review.
- **Confirmed** — The user explicitly approves the proposal.
- **Cancelled** — The user decides not to proceed.

### Product Principle

**Understanding intent is not the same as receiving permission to act.**

The user must remain in control of the final decision.

## Conversation State Model

The agent must maintain a conversation state across multiple user turns.

### Meeting Data

- subject
- participants
- day
- time
- duration
- location

### Conversation Status

- collecting_info
- awaiting_confirmation
- confirmed
- cancelled

### State Transitions

1. A new meeting request starts in `collecting_info`.
2. Each user message updates the known meeting information.
3. When all required information is available, the agent moves to `awaiting_confirmation`.
4. An explicit confirmation moves the conversation to `confirmed`.
5. A cancellation moves the conversation to `cancelled`.
6. A correction updates the meeting data and requires a new confirmation.
7. A simple "oui" confirms the meeting only when the conversation is awaiting confirmation.

### Technical Scope

For Sprint 3, conversation state will be stored in memory during the running Python session.

Persistent storage and real calendar modifications remain out of scope.

