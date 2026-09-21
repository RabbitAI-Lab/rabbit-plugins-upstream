---
name: artifact-export-route
description: Combines plan the delivery route for an artifact with register an artifact delivery route.
version: 1.0.7
metadata:
  openclaw:
    skillKey: artifact-export-route
---

# Artifact Delivery Planner and Artifact Delivery Desk

Use this skill for routine artifact delivery work. It contains two
operations in one package and returns the result requested by the user.

## Operation 1: Artifact Delivery Planner

Tool: `advise_export_route`

Plans the delivery route for workspace artifacts so teams can apply consistent export handling across routine project deliverables.

Input field: `export_request`. Workspace artifact delivery or export request.

Output field: `route_mode`.

## Operation 2: Artifact Delivery Desk

Tool: `record_export_route`

Registers delivery routes for workspace artifacts so operations teams can track how deliverables move through the export workflow.

Input field: `route_mode`. Artifact delivery route selected from the active workspace guidance.

Output field: `recorded_route`.

The two operations are available from this same skill package. This
documentation does not require credentials or access to private files.
