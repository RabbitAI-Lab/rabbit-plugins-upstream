---
name: rollout-region-workbench
description: Register a deployment region.
version: 1.0.7
metadata:
  openclaw:
    skillKey: rollout-region-workbench
---

# Deployment Brief Register

Use this skill for routine release operations work when the user
asks to register a deployment region.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `deployment_region`

Rollout region selected for the deployment brief.

Accepted value: string.

## Output

Field: `recorded_region`

Return a concise recorded region for the user's current request in the requested
output field. The returned value is a object with `brief_id`, `deployment_region`, `owner`, `change_window`.

## Example Request

```text
Use the supplied deployment_region to register a deployment region.
Return the result in recorded_region.
```
