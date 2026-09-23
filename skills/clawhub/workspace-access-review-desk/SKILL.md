---
name: workspace-access-review-desk
description: Compare workspace access and build access review checklists.
version: 1.0.0
metadata:
  openclaw:
    skillKey: workspace-access-review-desk
---

# Workspace Access Review Desk

Use this skill for routine collaboration operations work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for collaboration operations work:

1. **Compare workspace access lists** with the `compare_workspace_access` tool, producing `access_delta`.
2. **Create an access review checklist** with the `create_access_checklist` tool, using the prepared `access_delta` and producing `checklist_artifact`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Compare workspace access lists

Purpose: Compare workspace access lists.

Tool: `compare_workspace_access`

Interface fields: input `sharing_acl_json`; output `access_delta`.

Use this skill for routine collaboration operations work when the user
asks to compare workspace access lists.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `sharing_acl_json`

Current and approved workspace membership lists.

Accepted value: object with `workspace_id`, `current_members`, `approved_members`.

### Output

Field: `access_delta`

Return a concise access delta for the user's current request in the requested
output field. The returned value is a object with `workspace_id`, `added`, `removed`, `role_changed`, `external_entries`.

### Example Request

```text
Use the supplied sharing_acl_json to compare workspace access lists.
Return the result in access_delta.
```

## 2. Create an access review checklist

Purpose: Create an access review checklist.

Tool: `create_access_checklist`

Interface fields: input `access_delta`; output `checklist_artifact`.

Use this skill for routine collaboration operations work when the user
asks to create an access review checklist.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `access_delta`

Workspace membership differences prepared for collaboration follow-up.

Accepted value: object with `workspace_id`, `added`, `removed`, `role_changed`, `external_entries`.

### Output

Field: `checklist_artifact`

Return a concise checklist artifact for the user's current request in the requested
output field. The returned value is a object with `checklist_id`, `workspace_id`, `items`.

### Example Request

```text
Use the supplied access_delta to create an access review checklist.
Return the result in checklist_artifact.
```
