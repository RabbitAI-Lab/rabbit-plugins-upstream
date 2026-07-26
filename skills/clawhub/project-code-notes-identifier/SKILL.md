---
name: project-code-notes-identifier
description: Identify the project handle from an intake note.
version: 1.0.5
metadata:
  openclaw:
    skillKey: project-code-notes-identifier
---

# Project Intake Identifier

Use this skill for routine project delivery operations work when the user
asks to identify the project handle from an intake note.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `note`

Client brief, delivery note, or project update text.

## Output

Field: `project_code`

Return a concise project code for the user's current request in the requested
output field.

## Example Request

```text
Use the supplied note to identify the project handle from an intake note.
Return the result in project_code.
```
