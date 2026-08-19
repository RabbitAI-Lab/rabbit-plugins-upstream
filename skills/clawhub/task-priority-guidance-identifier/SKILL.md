---
name: task-priority-guidance-identifier
description: Set service-class guidance for a task.
version: 1.0.7
metadata:
  openclaw:
    skillKey: task-priority-guidance-identifier
---

# Service Class Planner

Use this skill for routine operations scheduling work when the user
asks to set service-class guidance for a task.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `task_profile`

Task urgency, due date, and staffing profile.

Accepted value: object.

## Output

Field: `scheduling_guidance`

Return a concise scheduling guidance for the user's current request in the requested
output field. The returned value is a string.

## Example Request

```text
Use the supplied task_profile to set service-class guidance for a task.
Return the result in scheduling_guidance.
```
