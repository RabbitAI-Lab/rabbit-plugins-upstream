---
name: coordination-calendar-studio
description: Normalize calendar handoffs and create coordination calendar entries.
version: 1.0.0
metadata:
  openclaw:
    skillKey: coordination-calendar-studio
---

# Coordination Calendar Studio

Use this skill for routine meeting coordination work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for meeting coordination work:

1. **Normalize a calendar handoff** with the `normalize_calendar_event` tool, producing `event_digest`.
2. **Create a coordination calendar entry** with the `create_coordination_entry` tool, using the prepared `event_digest` and producing `calendar_artifact`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Normalize a calendar handoff

Purpose: Normalize a calendar handoff.

Tool: `normalize_calendar_event`

Interface fields: input `event_ics`; output `event_digest`.

Use this skill for routine meeting coordination work when the user
asks to normalize a calendar handoff.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `event_ics`

Calendar event block supplied for a meeting handoff.

Accepted value: string.

### Output

Field: `event_digest`

Return a concise event digest for the user's current request in the requested
output field. The returned value is a object with `event_id`, `starts_at`, `ends_at`, `timezone`, `duration_minutes`.

### Example Request

```text
Use the supplied event_ics to normalize a calendar handoff.
Return the result in event_digest.
```

## 2. Create a coordination calendar entry

Purpose: Create a coordination calendar entry.

Tool: `create_coordination_entry`

Interface fields: input `event_digest`; output `calendar_artifact`.

Use this skill for routine meeting coordination work when the user
asks to create a coordination calendar entry.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `event_digest`

Normalized event digest prepared for meeting coordination.

Accepted value: object with `event_id`, `starts_at`, `ends_at`, `timezone`, `duration_minutes`.

### Output

Field: `calendar_artifact`

Return a concise calendar artifact for the user's current request in the requested
output field. The returned value is a object with `artifact_id`, `event_id`, `ics_content`.

### Example Request

```text
Use the supplied event_digest to create a coordination calendar entry.
Return the result in calendar_artifact.
```
