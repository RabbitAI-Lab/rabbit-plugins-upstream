---
name: project-delivery-intake-desk
description: Turn project intake notes into recorded delivery ledger entries.
version: 1.0.0
metadata:
  openclaw:
    skillKey: project-delivery-intake-desk
---

# Project Delivery Intake Desk

Use this skill for routine project delivery operations work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for project delivery operations work:

1. **Prepare project context from an intake note** with the `parse_project_context` tool, producing `project_context`.
2. **Build a delivery ledger entry** with the `build_delivery_entry` tool, using the prepared `project_context` and producing `delivery_entry`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Prepare project context from an intake note

Purpose: Prepare project context from an intake note.

Tool: `parse_project_context`

Interface fields: input `note`; output `project_context`.

Use this skill for routine project delivery operations work when the user
asks to prepare project context from an intake note.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `note`

Client brief, delivery note, or project update text.

Accepted value: string.

### Output

Field: `project_context`

Return a concise project context for the user's current request in the requested
output field. The returned value is a object with `project_code`, `source_title`, `note_digest`.

### Example Request

```text
Use the supplied note to prepare project context from an intake note.
Return the result in project_context.
```

## 2. Build a delivery ledger entry

Purpose: Build a delivery ledger entry.

Tool: `build_delivery_entry`

Interface fields: input `project_context`; output `delivery_entry`.

Use this skill for routine project delivery operations work when the user
asks to build a delivery ledger entry.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `project_context`

Project context prepared from a delivery handoff.

Accepted value: object with `project_code`, `source_title`, `note_digest`.

### Output

Field: `delivery_entry`

Return a concise delivery entry for the user's current request in the requested
output field. The returned value is a object with `entry_id`, `project_code`, `summary`.

### Example Request

```text
Use the supplied project_context to build a delivery ledger entry.
Return the result in delivery_entry.
```
