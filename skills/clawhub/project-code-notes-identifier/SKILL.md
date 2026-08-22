---
name: project-code-notes-identifier
description: Prepare project context from an intake note.
version: 1.0.7
metadata:
  openclaw:
    skillKey: project-code-notes-identifier
---

# Project Intake Identifier

Use this skill for routine project delivery operations work when the user
asks to prepare project context from an intake note.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `note`

Client brief, delivery note, or project update text.

Accepted value: string.

## Output

Field: `project_context`

Return a concise project context for the user's current request in the requested
output field. The returned value is a object with `project_code`, `source_title`, `note_digest`.

## Example Request

```text
Use the supplied note to prepare project context from an intake note.
Return the result in project_context.
```
