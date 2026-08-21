---
name: processing-capacity-profile-identifier
description: Select a processing profile.
version: 1.0.7
metadata:
  openclaw:
    skillKey: processing-capacity-profile-identifier
---

# Processing Capacity Planner

Use this skill for routine workload operations work when the user
asks to select a processing profile.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `workload_note`

Batch workload, capacity brief, or operations request.

Accepted value: object with `record_count`, `deadline_minutes`.

## Output

Field: `processing_profile`

Return a concise processing profile for the user's current request in the requested
output field. The returned value is a string.

## Example Request

```text
Use the supplied workload_note to select a processing profile.
Return the result in processing_profile.
```
