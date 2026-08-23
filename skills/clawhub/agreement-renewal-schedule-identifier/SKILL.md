---
name: agreement-renewal-schedule-identifier
description: Prepare an agreement obligation schedule.
version: 1.0.7
metadata:
  openclaw:
    skillKey: agreement-renewal-schedule-identifier
---

# Agreement Obligation Reader

Use this skill for routine agreement operations work when the user
asks to prepare an agreement obligation schedule.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `agreement_markdown`

Agreement sections supplied for renewal planning.

Accepted value: string.

## Output

Field: `obligation_schedule`

Return a concise obligation schedule for the user's current request in the requested
output field. The returned value is a object with `agreement_id`, `obligations`.

## Example Request

```text
Use the supplied agreement_markdown to prepare an agreement obligation schedule.
Return the result in obligation_schedule.
```
