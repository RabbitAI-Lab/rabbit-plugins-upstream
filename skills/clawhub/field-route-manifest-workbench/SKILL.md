---
name: field-route-manifest-workbench
description: Build a dispatch manifest.
version: 1.0.7
metadata:
  openclaw:
    skillKey: field-route-manifest-workbench
---

# Dispatch Manifest Builder

Use this skill for routine field service operations work when the user
asks to build a dispatch manifest.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `route_plan`

Ordered route plan prepared for a field-service handoff.

Accepted value: object with `route_id`, `ordered_stops`, `leg_km`, `total_km`.

## Output

Field: `dispatch_manifest`

Return a concise dispatch manifest for the user's current request in the requested
output field. The returned value is a object with `manifest_id`, `route_id`, `stops`, `total_km`.

## Example Request

```text
Use the supplied route_plan to build a dispatch manifest.
Return the result in dispatch_manifest.
```
