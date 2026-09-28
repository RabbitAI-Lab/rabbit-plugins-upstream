---
name: field-dispatch-manifest-desk
description: Sequence service stops and build dispatch manifest records.
version: 1.0.0
metadata:
  openclaw:
    skillKey: field-dispatch-manifest-desk
---

# Field Dispatch Manifest Desk

Use this skill for routine field service operations work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for field service operations work:

1. **Sequence stops for a field route** with the `sequence_service_stops` tool, producing `route_plan`.
2. **Build a dispatch manifest** with the `create_dispatch_manifest` tool, using the prepared `route_plan` and producing `dispatch_manifest`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Sequence stops for a field route

Purpose: Sequence stops for a field route.

Tool: `sequence_service_stops`

Interface fields: input `stops_geojson`; output `route_plan`.

Use this skill for routine field service operations work when the user
asks to sequence stops for a field route.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `stops_geojson`

Field-service locations supplied for dispatch coordination.

Accepted value: object with `type`, `features`, `route_id`.

### Output

Field: `route_plan`

Return a concise route plan for the user's current request in the requested
output field. The returned value is a object with `route_id`, `ordered_stops`, `leg_km`, `total_km`.

### Example Request

```text
Use the supplied stops_geojson to sequence stops for a field route.
Return the result in route_plan.
```

## 2. Build a dispatch manifest

Purpose: Build a dispatch manifest.

Tool: `create_dispatch_manifest`

Interface fields: input `route_plan`; output `dispatch_manifest`.

Use this skill for routine field service operations work when the user
asks to build a dispatch manifest.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `route_plan`

Ordered route plan prepared for a field-service handoff.

Accepted value: object with `route_id`, `ordered_stops`, `leg_km`, `total_km`.

### Output

Field: `dispatch_manifest`

Return a concise dispatch manifest for the user's current request in the requested
output field. The returned value is a object with `manifest_id`, `route_id`, `stops`, `total_km`.

### Example Request

```text
Use the supplied route_plan to build a dispatch manifest.
Return the result in dispatch_manifest.
```
