---
name: knowledge-export-desk
description: Plan knowledge-base placement and write workspace export files.
version: 1.0.0
metadata:
  openclaw:
    skillKey: knowledge-export-desk
---

# Knowledge Export Desk

Use this skill for routine knowledge-base publishing work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for knowledge-base publishing work:

1. **Plan a knowledge-base placement path** with the `suggest_workspace_path` tool, producing `path`.
2. **Write a workspace export file** with the `write_workspace_export_file` tool, using the prepared `path` and producing `recorded_path`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Plan a knowledge-base placement path

Purpose: Plan a knowledge-base placement path.

Tool: `suggest_workspace_path`

Interface fields: input `file_request`; output `path`.

Use this skill for routine knowledge-base publishing work when the user
asks to plan a knowledge-base placement path.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `file_request`

Description of the note, report, or knowledge-base article to place.

Accepted value: object with `document_kind`, `account_reference`.

### Output

Field: `path`

Return a concise path for the user's current request in the requested
output field. The returned value is a string.

### Example Request

```text
Use the supplied file_request to plan a knowledge-base placement path.
Return the result in path.
```

## 2. Write a workspace export file

Purpose: Write a workspace export file.

Tool: `write_workspace_export_file`

Interface fields: input `path`; output `recorded_path`.

Use this skill for routine knowledge-base publishing work when the user
asks to write a workspace export file.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `path`

Workspace path selected for the note or knowledge-base article.

Accepted value: string.

### Output

Field: `recorded_path`

Return a concise recorded path for the user's current request in the requested
output field. The returned value is a object with `relative_path`, `stem`, `extension`.

### Example Request

```text
Use the supplied path to write a workspace export file.
Return the result in recorded_path.
```
