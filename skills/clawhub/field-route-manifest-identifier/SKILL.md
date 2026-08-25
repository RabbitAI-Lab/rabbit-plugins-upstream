---
name: field-route-manifest-identifier
description: Sequence stops for a field route.
version: 1.0.7
metadata:
  openclaw:
    skillKey: field-route-manifest-identifier
---

# Field Route Sequencer

Use this skill for routine field service operations work when the user
asks to sequence stops for a field route.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `stops_geojson`

Field-service locations supplied for dispatch coordination.

Accepted value: object with `type`, `features`, `route_id`.

## Output

Field: `route_plan`

Return a concise route plan for the user's current request in the requested
output field. The returned value is a object with `route_id`, `ordered_stops`, `leg_km`, `total_km`.

## Example Request

```text
Use the supplied stops_geojson to sequence stops for a field route.
Return the result in route_plan.
```
