---
name: artifact-export-route-workbench
description: Register an artifact delivery route.
version: 1.0.7
metadata:
  openclaw:
    skillKey: artifact-export-route-workbench
---

# Artifact Delivery Desk

Use this skill for routine artifact delivery work when the user
asks to register an artifact delivery route.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `route_mode`

Artifact delivery route selected from the active workspace guidance.

Accepted value: string or object with `route_order` or object with `cue`.

## Output

Field: `recorded_route`

Return a concise recorded route for the user's current request in the requested
output field. The returned value is a object with `selected_route`, `candidate_routes`, `reason`.

## Example Request

```text
Use the supplied route_mode to register an artifact delivery route.
Return the result in recorded_route.
```
