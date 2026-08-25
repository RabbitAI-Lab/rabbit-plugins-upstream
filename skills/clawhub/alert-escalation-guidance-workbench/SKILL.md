---
name: alert-escalation-guidance-workbench
description: Assign an incident owner.
version: 1.0.7
metadata:
  openclaw:
    skillKey: alert-escalation-guidance-workbench
---

# Incident Assignment Desk

Use this skill for routine service assignment work when the user
asks to assign an incident owner.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `assignment_guidance`

Severity assignment guidance available from the active service session.

Accepted value: string or object with `routing_table`, `default_assignment` or object with `cue`.

## Output

Field: `assignment_result`

Return a concise assignment result for the user's current request in the requested
output field. The returned value is a object with `alert_id`, `severity`, `assignment`, `matched_rule`.

## Example Request

```text
Use the supplied assignment_guidance to assign an incident owner.
Return the result in assignment_result.
```
