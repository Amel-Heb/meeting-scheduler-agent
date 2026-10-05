 # Sprint 2 — From Tools to an Agent

## The Starting Point

At the end of Sprint 1, the Meeting Scheduler had the foundations of an agentic system: a calendar memory, a meeting model, and a tool capable of checking availability.

But there was a fundamental limitation: the application still needed to know which function to call. The user could not simply express what they wanted in natural language and let the system decide what to do.

The product had tools, but it did not yet behave like an agent.

## The Product Question

Sprint 2 started with a simple question:

> How can the system understand what the user wants and decide what action to take?

This introduced a new responsibility between the user and the tools: orchestration.

Instead of connecting the interface directly to individual functions, I introduced a `SchedulerAgent` responsible for interpreting the request, validating it, and selecting the appropriate tool.

## The Evolution

### Before

```text
User
	↓
app.py
	↓
Tool
	↓
Result
```

The application called a tool directly. The user’s intent was not yet what determined which action to take.

### After

```text
User request
	↓
app.py
	↓
SchedulerAgent
	├─ Interpret intent
	├─ Validate request
	└─ Select appropriate tool
			 ↓
		 Result
```

The agent became the orchestration layer between the interface and the tools. The application could pass in a request, and the agent took responsibility for deciding what to do with it.

## The Agent’s Responsibility

`SchedulerAgent` separates decision-making from the interface and the individual tools:

1. **Interpret** the user’s request to determine the intended scheduling task.
2. **Validate** the request before acting on it.
3. **Select** an appropriate available tool.
4. **Return** the tool’s result to the application.

This creates a clear boundary: the interface handles interaction, the agent handles orchestration, and tools perform specific operations.

## Why This Matters

Adding more tools alone would not solve the original limitation; the application would still need to choose each function. The agent introduces a single place to connect user intent with tool execution. It also gives the system a natural point to validate requests before invoking a capability.

## Outcome

Sprint 2 moved the Meeting Scheduler from direct function calls toward an agent-driven workflow. The important change was the orchestration layer: users could express what they wanted, while `SchedulerAgent` was responsible for interpreting the request and choosing an appropriate action.

User
  ↓
Natural language
  ↓
LLM extraction
  ↓
Structured intent + entities
  ↓
SchedulerAgent
  ↓
Validation
  ↓
Tool
  ↓
Result

## When Technically Correct Is Not Enough

One of the most useful moments in the sprint came from testing an incomplete request:

> Organise une réunion avec Léa mardi.

The extraction layer worked correctly.

It understood that:

- the participant was Léa
- the day was Tuesday
- the subject was missing
- the time was missing
- the duration was missing
- the location was missing

The system represented these missing values as `None`.

Technically, this was correct.

But the interface produced:

> Objet : None  
> Participants : Léa  
> Jour : mardi  
> Heure : None  
> Durée : None minutes  
> Lieu : None

The data was correct.  
The experience was not.

## Turning a UX Problem into a System Behavior

The obvious solution could have been to hide the `None` values in the interface.

But that would only solve the presentation problem.

The deeper question was:

> Should the agent prepare an action when it knows that required information is missing?

I decided that it should not.

A validation step was therefore introduced inside the `SchedulerAgent`, before tool execution.

```text
Understand request
        ↓
Validate information
     ↙       ↘
Incomplete   Complete
    ↓           ↓
Do not act   Select tool
                ↓
             Execute


