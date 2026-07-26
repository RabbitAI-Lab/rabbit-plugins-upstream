---
name: project-code-notes-workbench
description: Append a delivery update to the account ledger.
version: 1.0.5
metadata:
  openclaw:
    skillKey: project-code-notes-workbench
---

# Delivery Update Ledger

Use this skill for routine project delivery operations work when the user
asks to append a delivery update to the account ledger.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `status_update`

Delivery update text supplied by the user.

## Output

Field: `recorded_update`

Return a concise recorded update for the user's current request in the requested
output field.

## Example Request

```text
Use the supplied status_update to append a delivery update to the account ledger.
Return the result in recorded_update.
```
