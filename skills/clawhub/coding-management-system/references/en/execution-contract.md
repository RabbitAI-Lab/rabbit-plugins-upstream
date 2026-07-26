# Execution Contract 2.0

`Docs/ACTIVE_PACKET.md` is the current authorization and handoff between governance and execution.

## Required Frontmatter

```yaml
---
contract_version: "2.0"
packet_id: "GOAL-001"
goal_readiness: "Ready for Execution"
project_state: "Active"
execution_state: "Ready"
alignment_state: "Aligned"
qa_required: true
qa_decision: "Not Reviewed"
size: "Medium"
governance: "Standard"
stage: 1
max_stages: 10
stage_minutes: 60
updated_at: "YYYY-MM-DDTHH:mm:ssZ"
---
```

## Required Sections

- Desired Outcome
- User And Situation
- Current Stage Outcome
- Scope
- Non-Goals
- Acceptance Criteria
- Allowed Changes
- Protected Boundaries
- Evidence Required
- Stop Conditions
- Assumptions And Decisions
- Current Evidence
- One Next Action

Use `{baseDir}/templates/en/ACTIVE_PACKET.md`.

## Ownership

| Field/content | Owner |
| --- | --- |
| Desired outcome, Core Target, Non-Goals | Owner / authorized Controller |
| Size, governance, stage plan, Work Order scope | Controller |
| Execution state, implementation notes, evidence links | Developer / execution agent |
| Alignment verdict | Controller or designated reviewer |
| QA decision | QA; self only when Lite explicitly permits |
| Project state | Controller after QA decision |

An agent must not edit fields outside its current role.

## State Transitions

```text
Ready
  -> In Progress
  -> Ready for Review
  -> QA Accepted / Accepted With Risk

In Progress
  -> Needs Fix
  -> In Progress

Any active state
  -> Blocked
  -> resume only after the named gate is cleared

Any contradiction
  -> Invalid State
```

QA `Failed` maps to `execution_state: Needs Fix` and `project_state: Needs Fix`. It does not create a new Milestone.

## Conflict Rules

For Standard or Full projects, the Active Packet is a current projection:

```text
Owner-approved TARGET / Non-Goals
  -> ACCEPTANCE
  -> active WORK_ORDER
  -> ACTIVE_PACKET
  -> logs and chat
```

If the packet conflicts with a higher authority file, stop as `Invalid State`.

For Lite projects, the Active Packet may be the sole authority file.

## Write Rules

- Update the packet atomically where possible.
- Keep one next action.
- Link to evidence; do not paste large logs.
- Do not store secrets, private data, full chat transcripts, or hidden reasoning.
- Use ISO 8601 timestamps.
- Append one concise JSON object per execution loop to `Docs/LOOP_RUNS.jsonl`.
