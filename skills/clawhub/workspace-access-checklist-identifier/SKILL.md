---
name: workspace-access-checklist-identifier
description: Compare workspace access lists.
version: 1.0.7
metadata:
  openclaw:
    skillKey: workspace-access-checklist-identifier
---

# Workspace Access Comparator

Use this skill for routine collaboration operations work when the user
asks to compare workspace access lists.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `sharing_acl_json`

Current and approved workspace membership lists.

Accepted value: object with `workspace_id`, `current_members`, `approved_members`.

## Output

Field: `access_delta`

Return a concise access delta for the user's current request in the requested
output field. The returned value is a object with `workspace_id`, `added`, `removed`, `role_changed`, `external_entries`.

## Example Request

```text
Use the supplied sharing_acl_json to compare workspace access lists.
Return the result in access_delta.
```
