---
name: operations-scheduling-desk
description: Derive service classes and build operations task schedules.
version: 1.0.0
metadata:
  openclaw:
    skillKey: operations-scheduling-desk
---

# Operations Scheduling Desk

Use this skill for routine operations scheduling work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for operations scheduling work:

1. **Set service-class guidance for a task** with the `derive_service_class` tool, producing `scheduling_guidance`.
2. **Build an operations task schedule** with the `build_task_schedule` tool, using the prepared `scheduling_guidance` and producing `task_schedule`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Set service-class guidance for a task

Purpose: Set service-class guidance for a task.

Tool: `derive_service_class`

Interface fields: input `task_profile`; output `scheduling_guidance`.

Use this skill for routine operations scheduling work when the user
asks to set service-class guidance for a task.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `task_profile`

Task urgency, due date, and staffing profile.

Accepted value: object.

### Output

Field: `scheduling_guidance`

Return a concise scheduling guidance for the user's current request in the requested
output field. The returned value is a string.

### Example Request

```text
Use the supplied task_profile to set service-class guidance for a task.
Return the result in scheduling_guidance.
```

## 2. Build an operations task schedule

Purpose: Build an operations task schedule.

Tool: `build_task_schedule`

Interface fields: input `scheduling_guidance`; output `task_schedule`.

Use this skill for routine operations scheduling work when the user
asks to build an operations task schedule.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `scheduling_guidance`

Scheduling guidance available from the active operations session.

Accepted value: string or object with `service_class` or object with `cue`.

### Output

Field: `task_schedule`

Return a concise task schedule for the user's current request in the requested
output field. The returned value is a object with `ordered_task_ids`, `scheduled_task_id`, `scheduled_start`.

### Example Request

```text
Use the supplied scheduling_guidance to build an operations task schedule.
Return the result in task_schedule.
```
