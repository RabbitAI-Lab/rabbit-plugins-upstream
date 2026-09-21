---
name: project-code-notes
description: Combines prepare project context from an intake note with build a delivery ledger entry.
version: 1.0.7
metadata:
  openclaw:
    skillKey: project-code-notes
---

# Project Intake Identifier and Delivery Update Ledger

Use this skill for routine project delivery operations work. It contains two
operations in one package and returns the result requested by the user.

## Operation 1: Project Intake Identifier

Tool: `parse_project_context`

Reads project intake notes and prepares a project handle with source context for delivery handoffs.

Input field: `note`. Client brief, delivery note, or project update text.

Output field: `project_context`.

## Operation 2: Delivery Update Ledger

Tool: `build_delivery_entry`

Builds account-facing delivery entries from prepared project context for operations and implementation teams.

Input field: `project_context`. Project context prepared from a delivery handoff.

Output field: `delivery_entry`.

The two operations are available from this same skill package. This
documentation does not require credentials or access to private files.
