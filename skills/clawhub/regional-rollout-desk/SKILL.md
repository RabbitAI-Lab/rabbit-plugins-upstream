---
name: regional-rollout-desk
description: Select rollout regions and register deployment brief records.
version: 1.0.0
metadata:
  openclaw:
    skillKey: regional-rollout-desk
---

# Regional Rollout Desk

Use this skill for routine release operations work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for release operations work:

1. **Select a rollout region** with the `select_rollout_region` tool, producing `deployment_region`.
2. **Register a deployment region** with the `record_deployment_region` tool, using the prepared `deployment_region` and producing `recorded_region`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Select a rollout region

Purpose: Select a rollout region.

Tool: `select_rollout_region`

Interface fields: input `rollout_request`; output `deployment_region`.

Use this skill for routine release operations work when the user
asks to select a rollout region.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `rollout_request`

Release brief, rollout request, or deployment handoff.

Accepted value: object with `residency`.

### Output

Field: `deployment_region`

Return a concise deployment region for the user's current request in the requested
output field. The returned value is a string.

### Example Request

```text
Use the supplied rollout_request to select a rollout region.
Return the result in deployment_region.
```

## 2. Register a deployment region

Purpose: Register a deployment region.

Tool: `record_deployment_region`

Interface fields: input `deployment_region`; output `recorded_region`.

Use this skill for routine release operations work when the user
asks to register a deployment region.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `deployment_region`

Rollout region selected for the deployment brief.

Accepted value: string.

### Output

Field: `recorded_region`

Return a concise recorded region for the user's current request in the requested
output field. The returned value is a object with `brief_id`, `deployment_region`, `owner`, `change_window`.

### Example Request

```text
Use the supplied deployment_region to register a deployment region.
Return the result in recorded_region.
```
