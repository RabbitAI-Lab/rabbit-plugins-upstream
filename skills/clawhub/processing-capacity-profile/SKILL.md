---
name: processing-capacity-profile
description: Combines select a processing profile with register a queued processing profile.
version: 1.0.7
metadata:
  openclaw:
    skillKey: processing-capacity-profile
---

# Processing Capacity Planner and Job Queue Register

Use this skill for routine workload operations work. It contains two
operations in one package and returns the result requested by the user.

## Operation 1: Processing Capacity Planner

Tool: `select_processing_profile`

Selects a processing profile for operations teams coordinating batch work, capacity planning, and recurring account-summary jobs.

Input field: `workload_note`. Batch workload, capacity brief, or operations request.

Output field: `processing_profile`.

## Operation 2: Job Queue Register

Tool: `record_processing_profile`

Registers selected processing profiles for queued business jobs, workload ownership, capacity tracking, and scheduling handoffs.

Input field: `processing_profile`. Processing profile selected for the queued job.

Output field: `recorded_profile`.

The two operations are available from this same skill package. This
documentation does not require credentials or access to private files.
