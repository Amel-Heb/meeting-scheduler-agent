# Sprint 2 — Tool Orchestration

## Goal

Move from a simple chatbot to an agent capable of using tools.

## Problem

A chatbot can answer questions.

An agent must be able to:

- reason
- select a tool
- execute an action
- use the result

## Current Tooling

### Tool 1

check_availability()

Purpose:
Retrieve available meeting slots from the calendar memory.

### Tool 2

create_meeting_draft()

Purpose:
Prepare a meeting proposal before confirmation.

## Expected User Flow

User request

↓

"I want to schedule a meeting on Tuesday"

↓

Agent identifies the requested day

↓

Agent calls check_availability()

↓

Agent receives available slots

↓

Agent proposes options to the user

## Learning Objectives

- Understand tool orchestration
- Understand decision flows
- Understand how agents connect reasoning and action

## Sprint Progress

### Feature implemented

The application entry point has been redesigned.

Instead of directly calling the availability tool, all user requests are now routed through `SchedulerAgent`.

---

### Architecture decision

**Before**

app.py → check_availability()

**After**

app.py → SchedulerAgent → check_availability()

---

### Why?

This change separates the application entry point from the business logic.

`app.py` no longer needs to know which tool should be executed.

The SchedulerAgent becomes responsible for:

- understanding the request
- selecting the appropriate tool
- executing the tool
- returning the result

This architecture prepares the project for future tools such as:

- create meeting
- cancel meeting
- reschedule meeting
- Google Calendar

## Milestone 1 — First Agent Orchestration

### Goal

Replace the direct tool invocation with an orchestration layer.

---

### Before

app.py directly executed:

check_availability("mardi")

---

### After

The application now routes every user request through SchedulerAgent.

The agent:

1. Understands the request
2. Detects the intent
3. Selects the appropriate tool
4. Executes the tool
5. Returns a structured response

---

### Outcome

The Meeting Scheduler is no longer a collection of independent tools.

It now behaves as an orchestrated AI agent.

This architectural evolution prepares the application for future capabilities such as:

- Meeting creation
- Meeting cancellation
- Meeting rescheduling
- Google Calendar integration