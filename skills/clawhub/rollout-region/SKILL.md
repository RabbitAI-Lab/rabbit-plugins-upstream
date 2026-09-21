---
name: rollout-region
description: Combines select a rollout region with register a deployment region.
version: 1.0.7
metadata:
  openclaw:
    skillKey: rollout-region
---

# Regional Rollout Planner and Deployment Brief Register

Use this skill for routine release operations work. It contains two
operations in one package and returns the result requested by the user.

## Operation 1: Regional Rollout Planner

Tool: `select_rollout_region`

Selects a rollout region for release briefs, delivery sequencing, regional ownership, and deployment coordination workflows.

Input field: `rollout_request`. Release brief, rollout request, or deployment handoff.

Output field: `deployment_region`.

## Operation 2: Deployment Brief Register

Tool: `record_deployment_region`

Registers chosen rollout regions in deployment briefs used by engineering, release, implementation, and delivery teams.

Input field: `deployment_region`. Rollout region selected for the deployment brief.

Output field: `recorded_region`.

The two operations are available from this same skill package. This
documentation does not require credentials or access to private files.
