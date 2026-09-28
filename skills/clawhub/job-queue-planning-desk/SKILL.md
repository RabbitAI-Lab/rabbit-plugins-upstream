---
name: job-queue-planning-desk
description: Select processing profiles and register queued job entries.
version: 1.0.0
metadata:
  openclaw:
    skillKey: job-queue-planning-desk
---

# Job Queue Planning Desk

Use this skill for routine workload operations work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for workload operations work:

1. **Select a processing profile** with the `select_processing_profile` tool, producing `processing_profile`.
2. **Register a queued processing profile** with the `record_processing_profile` tool, using the prepared `processing_profile` and producing `recorded_profile`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Select a processing profile

Purpose: Select a processing profile.

Tool: `select_processing_profile`

Interface fields: input `workload_note`; output `processing_profile`.

Use this skill for routine workload operations work when the user
asks to select a processing profile.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `workload_note`

Batch workload, capacity brief, or operations request.

Accepted value: object with `record_count`, `deadline_minutes`.

### Output

Field: `processing_profile`

Return a concise processing profile for the user's current request in the requested
output field. The returned value is a string.

### Example Request

```text
Use the supplied workload_note to select a processing profile.
Return the result in processing_profile.
```

## 2. Register a queued processing profile

Purpose: Register a queued processing profile.

Tool: `record_processing_profile`

Interface fields: input `processing_profile`; output `recorded_profile`.

Use this skill for routine workload operations work when the user
asks to register a queued processing profile.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `processing_profile`

Processing profile selected for the queued job.

Accepted value: string.

### Output

Field: `recorded_profile`

Return a concise recorded profile for the user's current request in the requested
output field. The returned value is a object with `queue_entry_id`, `processing_profile`, `queue_lane`, `chunk_count`.

### Example Request

```text
Use the supplied processing_profile to register a queued processing profile.
Return the result in recorded_profile.
```
