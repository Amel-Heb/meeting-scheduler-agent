# Architecture Decision Record

## ADR-001

Date:
2026-07-10

Decision

Introduce SchedulerAgent as the application's orchestration layer.

Context

The application directly called individual tools.

As new tools are introduced, this architecture would become tightly coupled.

Decision

Move the orchestration logic into SchedulerAgent.

Consequences

Benefits

- Separation of concerns
- Easier scalability
- Cleaner architecture

Trade-offs

- Slightly more code
- One additional abstraction layer
