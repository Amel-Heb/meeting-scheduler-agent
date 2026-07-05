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
