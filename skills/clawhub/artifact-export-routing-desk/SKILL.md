---
name: artifact-export-routing-desk
description: Advise export routes and register artifact delivery decisions.
version: 1.0.0
metadata:
  openclaw:
    skillKey: artifact-export-routing-desk
---

# Artifact Export Routing Desk

Use this skill for routine artifact delivery work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for artifact delivery work:

1. **Plan the delivery route for an artifact** with the `advise_export_route` tool, producing `route_mode`.
2. **Register an artifact delivery route** with the `record_export_route` tool, using the prepared `route_mode` and producing `recorded_route`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Plan the delivery route for an artifact

Purpose: Plan the delivery route for an artifact.

Tool: `advise_export_route`

Interface fields: input `export_request`; output `route_mode`.

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

## 2. Register an artifact delivery route

Purpose: Register an artifact delivery route.

Tool: `record_export_route`

Interface fields: input `route_mode`; output `recorded_route`.

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
