---
name: task-priority-guidance-workbench
description: Build an operations task schedule.
version: 1.0.7
metadata:
  openclaw:
    skillKey: task-priority-guidance-workbench
---

# Operations Schedule Builder

Use this skill for routine operations scheduling work when the user
asks to build an operations task schedule.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `scheduling_guidance`

Scheduling guidance available from the active operations session.

Accepted value: string or object with `service_class` or object with `cue`.

## Output

Field: `task_schedule`

Return a concise task schedule for the user's current request in the requested
output field. The returned value is a object with `ordered_task_ids`, `scheduled_task_id`, `scheduled_start`.

## Example Request

```text
Use the supplied scheduling_guidance to build an operations task schedule.
Return the result in task_schedule.
```
