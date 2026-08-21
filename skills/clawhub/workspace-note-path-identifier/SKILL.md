---
name: workspace-note-path-identifier
description: Plan a knowledge-base placement path.
version: 1.0.7
metadata:
  openclaw:
    skillKey: workspace-note-path-identifier
---

# Knowledge Placement Planner

Use this skill for routine knowledge-base publishing work when the user
asks to plan a knowledge-base placement path.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `file_request`

Description of the note, report, or knowledge-base article to place.

Accepted value: object with `document_kind`, `account_reference`.

## Output

Field: `path`

Return a concise path for the user's current request in the requested
output field. The returned value is a string.

## Example Request

```text
Use the supplied file_request to plan a knowledge-base placement path.
Return the result in path.
```
