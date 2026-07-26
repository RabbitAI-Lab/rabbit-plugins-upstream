---
name: workspace-activity-reference-workbench
description: Append an operations activity entry.
version: 1.0.5
metadata:
  openclaw:
    skillKey: workspace-activity-reference-workbench
---

# Operations Activity Ledger

Use this skill for routine knowledge operations work when the user
asks to append an operations activity entry.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `journal_entry`

Operations activity entry to append to the workspace ledger.

## Output

Field: `recorded_entry`

Return a concise recorded entry for the user's current request in the requested
output field.

## Example Request

```text
Use the supplied journal_entry to append an operations activity entry.
Return the result in recorded_entry.
```
