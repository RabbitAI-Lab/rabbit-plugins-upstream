---
name: service-capacity-booking-desk
description: Select capacity windows and record capacity ledger entries.
version: 1.0.0
metadata:
  openclaw:
    skillKey: service-capacity-booking-desk
---

# Service Capacity Booking Desk

Use this skill for routine service capacity planning work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for service capacity planning work:

1. **Select a service capacity window** with the `select_capacity_window` tool, producing `capacity_window`.
2. **Record a capacity-window entry** with the `record_capacity_window` tool, using the prepared `capacity_window` and producing `capacity_ledger_entry`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Select a service capacity window

Purpose: Select a service capacity window.

Tool: `select_capacity_window`

Interface fields: input `capacity_request`; output `capacity_window`.

Use this skill for routine service capacity planning work when the user
asks to select a service capacity window.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `capacity_request`

Date, time, and timezone requested for a service capacity reservation.

Accepted value: object with `date`, `time`, `timezone`.

### Output

Field: `capacity_window`

Return a concise capacity window for the user's current request in the requested
output field. The returned value is a date-time.

### Example Request

```text
Use the supplied capacity_request to select a service capacity window.
Return the result in capacity_window.
```

## 2. Record a capacity-window entry

Purpose: Record a capacity-window entry.

Tool: `record_capacity_window`

Interface fields: input `capacity_window`; output `capacity_ledger_entry`.

Use this skill for routine service capacity planning work when the user
asks to record a capacity-window entry.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `capacity_window`

Timezone-aware service window selected for the capacity ledger.

Accepted value: date-time.

### Output

Field: `capacity_ledger_entry`

Return a concise capacity ledger entry for the user's current request in the requested
output field. The returned value is a object with `capacity_entry_id`, `start_at`, `end_at`, `duration_minutes`, `total_slots`, `requested_slots`, `reserved_slots`, `available_slots`, `capacity_status`, `overlap_status`.

### Example Request

```text
Use the supplied capacity_window to record a capacity-window entry.
Return the result in capacity_ledger_entry.
```
