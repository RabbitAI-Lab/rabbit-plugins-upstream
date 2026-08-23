---
name: processing-capacity-profile-workbench
description: Register a queued processing profile.
version: 1.0.7
metadata:
  openclaw:
    skillKey: processing-capacity-profile-workbench
---

# Job Queue Register

Use this skill for routine workload operations work when the user
asks to register a queued processing profile.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `processing_profile`

Processing profile selected for the queued job.

Accepted value: string.

## Output

Field: `recorded_profile`

Return a concise recorded profile for the user's current request in the requested
output field. The returned value is a object with `queue_entry_id`, `processing_profile`, `queue_lane`, `chunk_count`.

## Example Request

```text
Use the supplied processing_profile to register a queued processing profile.
Return the result in recorded_profile.
```
