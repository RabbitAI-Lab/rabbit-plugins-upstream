---
name: rollout-region-identifier
description: Select a rollout region.
version: 1.0.7
metadata:
  openclaw:
    skillKey: rollout-region-identifier
---

# Regional Rollout Planner

Use this skill for routine release operations work when the user
asks to select a rollout region.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `rollout_request`

Release brief, rollout request, or deployment handoff.

Accepted value: object with `residency`.

## Output

Field: `deployment_region`

Return a concise deployment region for the user's current request in the requested
output field. The returned value is a string.

## Example Request

```text
Use the supplied rollout_request to select a rollout region.
Return the result in deployment_region.
```
