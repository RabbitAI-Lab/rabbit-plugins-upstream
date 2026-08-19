---
name: project-code-notes-workbench
description: Build a delivery ledger entry.
version: 1.0.7
metadata:
  openclaw:
    skillKey: project-code-notes-workbench
---

# Delivery Update Ledger

Use this skill for routine project delivery operations work when the user
asks to build a delivery ledger entry.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `project_context`

Project context prepared from a delivery handoff.

Accepted value: object with `project_code`, `source_title`, `note_digest`.

## Output

Field: `delivery_entry`

Return a concise delivery entry for the user's current request in the requested
output field. The returned value is a object with `entry_id`, `project_code`, `summary`.

## Example Request

```text
Use the supplied project_context to build a delivery ledger entry.
Return the result in delivery_entry.
```
