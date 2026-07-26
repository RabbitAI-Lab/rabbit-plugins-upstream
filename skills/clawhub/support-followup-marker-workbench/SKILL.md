---
name: support-followup-marker-workbench
description: Add a support case follow-up.
version: 1.0.5
metadata:
  openclaw:
    skillKey: support-followup-marker-workbench
---

# Support Case Workbench

Use this skill for routine support operations work when the user
asks to add a support case follow-up.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `comment`

Support case comment or escalation note to add.

## Output

Field: `ticket_comment`

Return a concise ticket comment for the user's current request in the requested
output field.

## Example Request

```text
Use the supplied comment to add a support case follow-up.
Return the result in ticket_comment.
```
