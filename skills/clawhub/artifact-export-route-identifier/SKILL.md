---
name: artifact-export-route-identifier
description: Plan the delivery route for an artifact.
version: 1.0.7
metadata:
  openclaw:
    skillKey: artifact-export-route-identifier
---

# Artifact Delivery Planner

Use this skill for routine artifact delivery work when the user
asks to plan the delivery route for an artifact.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `export_request`

Workspace artifact delivery or export request.

Accepted value: object.

## Output

Field: `route_mode`

Return a concise route mode for the user's current request in the requested
output field. The returned value is a string.

## Example Request

```text
Use the supplied export_request to plan the delivery route for an artifact.
Return the result in route_mode.
```
