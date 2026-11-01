```markdown
# Sprint 3 — Conversation & Human Validation

## The Challenge

At the end of Sprint 2, the Meeting Scheduler Agent could understand natural-language requests, extract structured information, identify missing fields, and select the appropriate tool.

But it could not yet resolve incomplete requests through conversation.

A request such as:

> Organise une réunion avec Léa mardi.

would reveal missing information without helping the user provide it.

The challenge for Sprint 3 was to turn a single-turn agent into a conversational experience while keeping the user in control of the proposed action.

## Product Goal

Design and implement a meeting scheduling conversation that can:

- Remember information across multiple turns.
- Extract several details from a single message.
- Ask only for information that is still missing.
- Present a complete meeting summary.
- Allow users to correct a proposed meeting.
- Require explicit confirmation before considering a meeting approved.
- Respect cancellation at the confirmation stage.

**Guiding principle:** Ask only for what is missing. Never ask the user to repeat information already provided.

## Key Design Decisions

### 1. Conversation State as a Product Mechanism

I introduced a structured conversation state with four possible statuses:

- `collecting_info`
- `awaiting_confirmation`
- `confirmed`
- `cancelled`

These statuses define what the agent is allowed to do at each point in the interaction.

### 2. Progressive Information Collection

Instead of presenting a rigid form, the agent asks one question at a time.

When a user provides multiple pieces of information in one response, the agent extracts and stores all of them.

This prevents repetitive questions and reduces unnecessary interaction.

### 3. Explicit Human Validation

Once all required meeting details are available, the agent presents a readable summary and asks for confirmation.

The agent does not treat understanding the request as permission to act.

A response such as "oui" is accepted as confirmation only when the conversation is in the `awaiting_confirmation` state.

### 4. Corrections Without Losing Context

Users can modify a proposed meeting before confirming it.

For example:

> Plutôt mercredi à 15h.

The agent updates the day and time while preserving the subject, participants, duration, and location.

It then presents the revised summary and requests confirmation again.

### 5. Cancellation as an Explicit Outcome

Users can reject the proposed meeting.

An explicit "non" at the confirmation stage changes the conversation status to `cancelled`.

A correction such as "Non, plutôt mercredi" is not treated as an automatic cancellation.

## Example Conversation

**User:** Organise une revue du prototype avec Léa mardi.

**Agent:** À quelle heure souhaites-tu la programmer ?

**User:** À 14h pendant 45 minutes sur Google Meet.

**Agent:** Presents a complete meeting summary and asks for confirmation.

**User:** Plutôt mercredi à 15h.

**Agent:** Presents the updated summary and asks for confirmation again.

**User:** oui

**Agent:** Réunion confirmée (simulation uniquement).

## Technical Implementation

Sprint 3 introduced:

- A Pydantic model for conversation state.
- A merge function to preserve previously collected meeting details.
- LLM-based extraction of updates from conversational messages.
- Deterministic selection of the next missing-information question.
- Context-dependent confirmation and cancellation rules.
- A multi-turn conversation handler.
- An interactive terminal conversation mode.

The existing Sprint 2 functionality remains accessible through a separate mode.

## Validation

I manually tested the following scenarios:

| Scenario | Result |
|---|---|
| Incomplete initial request | Agent asks for missing information |
| Multiple details in one message | Information is extracted and retained |
| Complete meeting request | Agent presents a confirmation summary |
| Correction before confirmation | Updated summary is presented |
| Confirmation outside the expected state | Confirmation is rejected |
| Explicit confirmation | Conversation reaches `confirmed` |
| Explicit cancellation | Conversation reaches `cancelled` |
| Sprint 2 availability lookup | Existing functionality remains operational |

## Limitations

This sprint is a conversational prototype, not a production scheduling system.

- Meeting data is stored in memory for the current application session.
- Confirmation does not create a real calendar event.
- The confirmation and cancellation vocabulary is intentionally limited.
- The agent has not yet been evaluated through automated regression tests or a broader user study.
- Calendar integration, date resolution, and more robust error handling remain future work.

## What Changed

Sprint 2 established when the agent should avoid acting on incomplete information.

Sprint 3 established how the agent should continue the conversation, preserve context, and request human validation.

The key learning is that conversational intelligence requires more than language understanding. It also requires explicit state, predictable interaction rules, and clear boundaries around user authorization.

## Next — Sprint 4: Google Calendar Integration

The next step is to connect the validated meeting workflow to Google Calendar.

The main challenge will be preserving the human-validation mechanism while introducing real external actions.

**Design principle:** Understanding intent is not the same as receiving permission to act.
```
