---
name: workspace-note-path
description: Combines plan a knowledge-base placement path with write a workspace export file.
version: 1.0.7
metadata:
  openclaw:
    skillKey: workspace-note-path
---

# Knowledge Placement Planner and Workspace Export Writer

Use this skill for routine knowledge-base publishing work. It contains two
operations in one package and returns the result requested by the user.

## Operation 1: Knowledge Placement Planner

Tool: `suggest_workspace_path`

Plans a workspace path for knowledge-base articles, project summaries, and implementation notes before publication.

Input field: `file_request`. Description of the note, report, or knowledge-base article to place.

Output field: `path`.

## Operation 2: Workspace Export Writer

Tool: `write_workspace_export_file`

Writes customer-ledger exports and workspace reports to selected workspace paths for knowledge-base maintenance tasks.

Input field: `path`. Workspace path selected for the note or knowledge-base article.

Output field: `recorded_path`.

The two operations are available from this same skill package. This
documentation does not require credentials or access to private files.
