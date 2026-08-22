---
name: service-capacity-window-workbench
description: Record a capacity-window entry.
version: 1.0.7
metadata:
  openclaw:
    skillKey: service-capacity-window-workbench
---

# Capacity Ledger Desk

Use this skill for routine service capacity planning work when the user
asks to record a capacity-window entry.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `capacity_window`

Timezone-aware service window selected for the capacity ledger.

Accepted value: date-time.

## Output

Field: `capacity_ledger_entry`

Return a concise capacity ledger entry for the user's current request in the requested
output field. The returned value is a object with `capacity_entry_id`, `start_at`, `end_at`, `duration_minutes`, `total_slots`, `requested_slots`, `reserved_slots`, `available_slots`, `capacity_status`, `overlap_status`.

## Example Request

```text
Use the supplied capacity_window to record a capacity-window entry.
Return the result in capacity_ledger_entry.
```
