---
name: workspace-access-checklist-workbench
description: Create an access review checklist.
version: 1.0.7
metadata:
  openclaw:
    skillKey: workspace-access-checklist-workbench
---

# Access Review Checklist

Use this skill for routine collaboration operations work when the user
asks to create an access review checklist.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `access_delta`

Workspace membership differences prepared for collaboration follow-up.

Accepted value: object with `workspace_id`, `added`, `removed`, `role_changed`, `external_entries`.

## Output

Field: `checklist_artifact`

Return a concise checklist artifact for the user's current request in the requested
output field. The returned value is a object with `checklist_id`, `workspace_id`, `items`.

## Example Request

```text
Use the supplied access_delta to create an access review checklist.
Return the result in checklist_artifact.
```
