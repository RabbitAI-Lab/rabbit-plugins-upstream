---
name: field-route-manifest
description: Combines sequence stops for a field route with build a dispatch manifest.
version: 1.0.7
metadata:
  openclaw:
    skillKey: field-route-manifest
---

# Field Route Sequencer and Dispatch Manifest Builder

Use this skill for routine field service operations work. It contains two
operations in one package and returns the result requested by the user.

## Operation 1: Field Route Sequencer

Tool: `sequence_service_stops`

Reads field-service locations and prepares an ordered route plan for dispatch coordination.

Input field: `stops_geojson`. Field-service locations supplied for dispatch coordination.

Output field: `route_plan`.

## Operation 2: Dispatch Manifest Builder

Tool: `create_dispatch_manifest`

Builds dispatch manifests from ordered route plans for field-service handoffs.

Input field: `route_plan`. Ordered route plan prepared for a field-service handoff.

Output field: `dispatch_manifest`.

The two operations are available from this same skill package. This
documentation does not require credentials or access to private files.
