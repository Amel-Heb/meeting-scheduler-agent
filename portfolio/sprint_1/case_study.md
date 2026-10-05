# Sprint 1 — Building the Foundations of an AI Meeting Scheduler

## Context

In many organizations, scheduling a meeting is still a manual and repetitive task. Team members need to check calendars, consider vacations, existing meetings and availability before finding a suitable time slot.

Although this process seems simple, it becomes time-consuming when repeated several times a week.

I chose to explore this problem through the design of an AI Meeting Scheduler Agent. Rather than building another conversational assistant, I wanted to understand how an AI agent can interact with its environment, use tools and progressively evolve into an autonomous system capable of supporting real scheduling tasks.

## Problem

Traditional chatbots can answer questions, but they rarely perform actions.

For example, if a user asks:

"Can you schedule a meeting for Tuesday afternoon?"

a chatbot may suggest possible times, but it usually cannot access a calendar, retrieve availability or prepare a meeting.

This project explores how to bridge that gap by transforming a conversational assistant into an AI agent capable of reasoning, orchestrating tools and interacting with an external environment.


## Solution

The first sprint focuses on building the foundations of the agent.

Instead of connecting directly to external services, I designed a modular architecture composed of:

- a dedicated Scheduler Agent
- reusable tools
- a memory layer
- a system prompt
- a simple command-line interface

This first version intentionally relies on a simulated environment. The objective is not to automate meeting scheduling immediately, but to establish a scalable architecture that can evolve in future iterations.


## Architecture

The project is organised around independent components.

User

↓

app.py

The application entry point.

Its responsibility is limited to receiving user input and forwarding requests to the agent.

↓

SchedulerAgent

The Scheduler Agent orchestrates the workflow.

It analyses the request, decides which tool should be used and returns the final response.

↓

Tools

Each capability is implemented as an independent tool.

For example:

- check_availability()
- create_meeting_draft()

This separation makes the architecture easier to maintain and extend.

↓

Memory

The current implementation stores calendar information inside a JSON file.

Although simple, this layer represents the agent's environment.

It can later be replaced by Google Calendar without changing the rest of the architecture.

## Key Learnings

This sprint helped me better understand the fundamental differences between chatbots and AI agents.

More specifically, I learned:

- why an agent needs access to an external environment
- how tools separate reasoning from action
- why memory should not be embedded directly into the code
- how modular architectures simplify future iterations
- how product thinking influences technical decisions

## Next Sprint

Sprint 2 will focus on orchestration.

The objectives are:

- improve the Scheduler Agent
- automatically route requests to the appropriate tools
- prepare the architecture for LLM-based reasoning
- make the agent capable of coordinating multiple actions instead of executing a single function