---
name: agreement-renewal-schedule-workbench
description: Add entries to a renewal schedule.
version: 1.0.7
metadata:
  openclaw:
    skillKey: agreement-renewal-schedule-workbench
---

# Renewal Schedule Desk

Use this skill for routine agreement operations work when the user
asks to add entries to a renewal schedule.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `obligation_schedule`

Dated obligation entries prepared for a renewal handoff.

Accepted value: object with `agreement_id`, `obligations`.

## Output

Field: `schedule_receipt`

Return a concise schedule receipt for the user's current request in the requested
output field. The returned value is a object with `schedule_id`, `rows`.

## Example Request

```text
Use the supplied obligation_schedule to add entries to a renewal schedule.
Return the result in schedule_receipt.
```
