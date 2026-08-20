---
name: workspace-note-path-workbench
description: Write a workspace export file.
version: 1.0.7
metadata:
  openclaw:
    skillKey: workspace-note-path-workbench
---

# Workspace Export Writer

Use this skill for routine knowledge-base publishing work when the user
asks to write a workspace export file.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `path`

Workspace path selected for the note or knowledge-base article.

Accepted value: string.

## Output

Field: `recorded_path`

Return a concise recorded path for the user's current request in the requested
output field. The returned value is a object with `relative_path`, `stem`, `extension`.

## Example Request

```text
Use the supplied path to write a workspace export file.
Return the result in recorded_path.
```
