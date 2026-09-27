---
name: artifact-export-routing-desk
description: Plan the delivery route for an artifact. Register an artifact delivery route.
version: 2.1.0
metadata:
  openclaw:
    skillKey: artifact-export-routing-desk
---

# Artifact Export Routing Desk

## 1. Plan the delivery route for an artifact.

Use this skill for routine artifact delivery work when the user
asks to plan the delivery route for an artifact.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `export_request`

Workspace artifact delivery or export request.

Accepted value: object.

### Output

Field: `route_mode`

Return a concise route mode for the user's current request in the requested
output field. The returned value is a string.

### Example Request

```text
Use the supplied export_request to plan the delivery route for an artifact.
Return the result in route_mode.
```

## 2. Register an artifact delivery route.

Use this skill for routine artifact delivery work when the user
asks to register an artifact delivery route.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `route_mode`

Artifact delivery route selected from the active workspace guidance.

Accepted value: string or object with `route_order` or object with `cue`.

### Output

Field: `recorded_route`

Return a concise recorded route for the user's current request in the requested
output field. The returned value is a object with `selected_route`, `candidate_routes`, `reason`.

### Example Request

```text
Use the supplied route_mode to register an artifact delivery route.
Return the result in recorded_route.
```
