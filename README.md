# 📅 Meeting Scheduler Agent

> **Building an AI agent that evolves from conversation to action.**

An educational project documenting the design and implementation of an AI Meeting Scheduler through iterative product sprints.

---

# Why this project?

Scheduling meetings is a repetitive task that often requires checking calendars, considering vacations, existing meetings and participant availability.

Rather than simply building another chatbot, this project explores how an AI agent can progressively automate this workflow by combining reasoning, memory and tools.

The objective is to understand how an agent can evolve from answering questions to interacting with its environment and supporting real scheduling tasks.

---

## Overview

Meeting Scheduler Agent is an educational AI agent project designed to explore how Large Language Models interact with tools, memory, and environments.

The objective is not only to build a chatbot, but to understand the foundations of agentic systems.

---

## Project Goals

- Understand the difference between a chatbot and an agent
- Build a memory layer
- Build reusable tools
- Connect reasoning with actions
- Explore human-in-the-loop workflows
- Design an evolutive AI product

---

## Current Architecture

```text
User
  │
  ▼
app.py
  │
  ▼
SchedulerAgent
  │
  ├── Understand request
  │       │
  │       ▼
  │   LLM extraction
  │       │
  │       ▼
  │   Intent + entities
  │
  ├── Validate request
  │
  └── Select tool
          │
     ┌────┴───────────────┐
     ▼                    ▼
check_availability()   create_meeting_draft()
     │
     ▼
calendar.json

---

# Architecture Principles

This project follows a modular architecture inspired by modern AI agent systems.

Each layer has a single responsibility.

| Layer | Responsibility |
|--------|----------------|
| Application | Presents the interaction to the user |
| LLM | Translates natural language into structured data |
| SchedulerAgent | Validates requests and orchestrates actions |
| Tools | Execute specific operations |
| Memory | Represents the agent's environment |
| Models | Define structured data contracts |
| Prompts | Define extraction and behavioral instructions |

This separation makes the project easier to understand, maintain and extend.

---

## Features

### Sprint 1 — Foundations

Features delivered:

- Python project setup
- Virtual environment
- OpenAI API integration
- System prompt
- Calendar memory
- Meeting model
- Availability tool
- Project documentation

Status: Completed

---

### Sprint 2 — Understanding & Orchestration

Features delivered:

- Natural language request understanding
- LLM-based structured extraction
- Intent detection
- Structured meeting entities
- Time and duration normalization
- SchedulerAgent orchestration
- Tool routing
- Availability checking
- Meeting draft creation
- Missing information detection
- Request validation before tool execution
- Regression testing

Status: Completed

---

### Sprint 3 — Conversation & Human Validation

Objectives:

- Multi-turn conversation
- Progressive collection of missing information
- Conversation state
- Avoid asking for information already provided
- Meeting proposal
- Explicit user confirmation
- Human-in-the-loop workflow

Status: Planned

---

### Sprint 4 — Real Calendar Integration

Objectives:

- Google Calendar
- Real environment
- Calendar events

Status: Planned

---

### Sprint 5 — User Interface

Objectives:

- Chat interface
- Better user experience
- Error handling

Status: Planned

---

# What I Learned

During Sprint 1 I discovered that:

- an AI agent is more than a language model
- tools separate reasoning from execution
- memory represents the agent's environment
- modular architectures make future iterations easier
- product decisions influence technical architecture

During Sprint 2 I learned that:

- LLMs can translate natural language into structured system data
- structured outputs create a contract between language and application logic
- prompts can influence system behavior and data normalization
- agents need validation before executing tools
- missing information should remain explicit rather than being invented
- technically correct outputs do not automatically create good user experiences
- regression testing is essential when introducing new agent capabilities
- language design can influence both the user experience and the architecture of an agent

---

# Project Status

This repository documents the progressive evolution of an AI Meeting Scheduler.

Each sprint introduces new capabilities while preserving a modular architecture.

The project is intentionally developed in public to document:

- product decisions
- architectural choices
- technical trade-offs
- lessons learned

---

# Repository Structure

```text
meeting-scheduler-agent/

├── agent/
├── memory/
├── models/
├── notes/
├── portfolio/
├── prompts/
├── tools/

├── app.py
├── README.md
├── requirements.txt
└── .env
```

---

# Portfolio

This repository is part of a broader AI Product Design learning journey.

Each sprint is documented through:

- Product decisions
- Case studies
- Architecture diagrams
- Sprint reviews

---

# Roadmap

- ✅ Sprint 1 — Foundations
- ✅ Sprint 2 — Understanding & Orchestration
- ⏳ Sprint 3 — Conversation & Human Validation
- ⏳ Sprint 4 — Real Calendar Integration
- ⏳ Sprint 5 — User Interface

---

# Author

Built by **Amel** as part of an AI Product Design learning journey documenting the design of evolving agentic systems.