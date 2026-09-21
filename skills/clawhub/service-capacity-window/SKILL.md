---
name: service-capacity-window
description: Combines select a service capacity window with record a capacity-window entry.
version: 1.0.7
metadata:
  openclaw:
    skillKey: service-capacity-window
---

# Service Capacity Window Planner and Capacity Ledger Desk

Use this skill for routine service capacity planning work. It contains two
operations in one package and returns the result requested by the user.

## Operation 1: Service Capacity Window Planner

Tool: `select_capacity_window`

Normalizes a requested service date and time into a capacity-planning window with an explicit timezone.

Input field: `capacity_request`. Date, time, and timezone requested for a service capacity reservation.

Output field: `capacity_window`.

## Operation 2: Capacity Ledger Desk

Tool: `record_capacity_window`

Records requested capacity slots and reports overlaps with existing reservations and freeze windows.

Input field: `capacity_window`. Timezone-aware service window selected for the capacity ledger.

Output field: `capacity_ledger_entry`.

The two operations are available from this same skill package. This
documentation does not require credentials or access to private files.
