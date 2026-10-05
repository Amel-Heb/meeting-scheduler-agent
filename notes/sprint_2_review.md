# Sprint 2 — Review

## Sprint Goal

Transform the Meeting Scheduler from a collection of tools into an orchestrated AI agent capable of understanding natural language requests and selecting the appropriate action.

## What We Built

During Sprint 2, the Meeting Scheduler evolved from a tool-based application into an orchestrated AI agent.

The agent can now:

- understand a scheduling request written in natural language
- extract structured meeting information using an LLM
- identify the user's intent
- route the request to the appropriate tool
- check calendar availability
- prepare a structured meeting draft
- detect when required information is missing
- avoid executing an action when the request is incomplete

## Validated User Flows

### 1. Check availability

**User**

> Je veux connaître mes disponibilités mardi.

**Agent**

Returns the available calendar slots for Tuesday.

### 2. Prepare a complete meeting

**User**

> Organise une revue du prototype avec Léa mardi à 14h pendant 45 minutes sur Google Meet.

**Agent**

Extracts the meeting information and prepares a structured meeting draft.

### 3. Handle an incomplete request

**User**

> Organise une réunion avec Léa mardi.

**Agent**

Recognizes the information already provided and identifies the missing information:

- subject
- time
- duration
- location

The meeting draft is not created until the required information is available.

## Architecture Evolution

### Sprint 1

The application directly connected the entry point to individual tools.

```text
User
  ↓
app.py
  ↓
Tool
  ↓
Result
```

The application needed to know which function to execute.

### Sprint 2

The application now routes user requests through an orchestration layer.

```text
User
  ↓
Natural language request
  ↓
SchedulerAgent
  ↓
LLM extraction
  ↓
Structured intent + entities
  ↓
Request validation
  ↓
Tool selection
  ↓
Tool execution
  ↓
Result
```

The `SchedulerAgent` is now responsible for deciding what should happen, while individual tools remain responsible for performing specific operations.

### Separation of Responsibilities

The architecture now separates four responsibilities:

- **LLM** — translates natural language into structured information
- **SchedulerAgent** — evaluates the request and decides what action should be taken
- **Tools** — perform specific operations
- **Application layer** — presents the result to the user

This separation keeps language understanding distinct from deterministic application behavior.

## Key Product & Design Decisions

### 1. The LLM interprets language but does not execute actions

The LLM is used to transform natural language into structured data.

Execution remains controlled by the application and its tools.

This prevents the language model from directly modifying the system and keeps agent behavior more predictable.

### 2. Missing information is not invented

If the user does not provide information such as the meeting duration, location, or time, the system returns a missing value instead of guessing.

For example:

`duration = None`

This makes uncertainty explicit and allows the agent to decide what information it still needs.

### 3. An incomplete request should not trigger an action

Before selecting and executing the meeting tool, the `SchedulerAgent` checks whether the required information is available.

If information is missing, execution stops and the missing fields are returned.

This introduces an important behavioral principle:

> The agent should know when it does not have enough information to act.

### 4. Internal system language and user-facing language are separated

Internally, the system works with structured fields such as:

`subject`, `participants`, `time`, `duration`, `location`

The application layer translates these concepts into user-facing language such as:

`l'objet`, `les participants`, `l'heure`, `la durée`, `le lieu`

This separation allows the technical representation to remain stable while the conversational experience can evolve independently.

## Challenges & Learnings

### 1. Keeping the data contract consistent

When `duration` was added to the meeting model, the meeting draft tool was not updated at the same time.

This caused:

`KeyError: 'duration'`

This highlighted an important architectural lesson: when structured data evolves, every component that consumes that data must remain aligned.

### 2. Prompt changes affect system behavior

The first LLM extraction returned the meeting time as:

`14h`

After refining the extraction instructions, the same request returned:

`14:00`

This demonstrated that prompt design can directly affect the data produced by the system.

Prompt wording is therefore not only conversational copy; it can become part of the product's behavioral contract.

### 3. Test existing capabilities after introducing a new one

After integrating LLM-based extraction, the availability flow was tested again to ensure that the new architecture had not broken an existing capability.

This regression test exposed an invalid `calendar.json` file containing two JSON documents.

The problem was unrelated to the LLM itself, but the test prevented the sprint from being considered complete while an existing user flow was broken.

### 4. Agent behavior requires more than successful extraction

The LLM correctly extracted missing values as `None`.

However, the application initially displayed:

`Heure : None`

`Durée : None minutes`

`Lieu : None`

Technically, the extraction was correct. From a user experience perspective, the behavior was not.

The solution was to introduce request validation before tool execution.

This distinction became an important learning from the sprint:

> Correct structured data does not automatically produce a good agent experience.

## Sprint 2 Outcome

Sprint 2 transformed the Meeting Scheduler from a collection of independent functions into an orchestrated AI agent.

The agent can now:

- interpret natural language
- convert it into structured data
- identify user intent
- validate whether enough information is available
- select and execute the appropriate tool
- avoid acting when required information is missing

The agent can understand and orchestrate, but it cannot yet conduct a multi-turn conversation to complete an incomplete request.

## Deferred to Sprint 3

Sprint 3 will focus on conversation and human control.

The next version of the agent should be able to:

- ask for one missing piece of information at a time
- remember information across multiple turns
- avoid asking users to repeat information already provided
- progressively build a complete meeting request
- present the proposed meeting before taking action
- ask for explicit user confirmation
- execute the final action only after confirmation

### Example target interaction

**User**

> Organise une réunion avec Léa mardi.

**Agent**

> Quel est l'objet de la réunion ?

**User**

> Revue du prototype.

**Agent**

> À quelle heure souhaites-tu la programmer ?

...

**Agent**

> Léa et toi êtes disponibles mardi à 14h. Veux-tu que je programme la réunion ?

**User**

> Oui.

**Agent**

> C'est fait. La réunion est programmée.

## Product Principle for Sprint 3

> Ask only for what is missing. Never ask the user to repeat information already provided.

Sprint 2 established the agent's decision layer.

Sprint 3 will turn that decision layer into a conversational experience.

