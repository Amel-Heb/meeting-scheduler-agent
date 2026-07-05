# Meeting Scheduler Agent — Product Decisions

## 1. Project goal

Build a simple AI agent that helps users schedule meetings.

The goal is not only to create a chatbot, but to understand how an AI agent can:
- understand a user request
- access an environment
- use tools
- retrieve availability
- support human validation

## 2. Problem

Scheduling a meeting often requires interpreting vague natural language requests such as:

"Can you schedule a meeting with Sarah next Tuesday afternoon?"

A simple chatbot can respond with suggestions, but an agent should be able to check real or simulated availability before answering.

## 3. Agent architecture

Current architecture:

User request
→ LLM
→ Tool
→ Calendar memory
→ Available slots
→ Response

## 4. What I built in Part 1

- Python project setup
- Virtual environment
- OpenAI API connection
- System prompt
- Meeting data model
- Simulated calendar memory
- First tool: `check_availability()`

## 5. Key product decision

I chose to start with a simulated calendar instead of connecting Google Calendar immediately.

Reason:
- reduce technical complexity
- focus on agent architecture
- understand the role of tools and environment
- avoid premature integration

## 6. AI UX principle

The agent should not create a meeting automatically without user confirmation.

Reason:
- scheduling affects other people
- user trust matters
- the agent should support decision-making before acting

## 7. What I learned

A chatbot responds.
An agent responds and acts through tools.

The LLM is the reasoning layer.
The tools are the action layer.
The calendar JSON file is the environment.
