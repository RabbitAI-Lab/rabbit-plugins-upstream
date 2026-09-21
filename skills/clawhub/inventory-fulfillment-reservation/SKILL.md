---
name: inventory-fulfillment-reservation
description: Combines plan a lot allocation with record a fulfillment reservation.
version: 1.0.7
metadata:
  openclaw:
    skillKey: inventory-fulfillment-reservation
---

# Lot Allocation Planner and Fulfillment Reservation Ledger

Use this skill for routine fulfillment operations work. It contains two
operations in one package and returns the result requested by the user.

## Operation 1: Lot Allocation Planner

Tool: `plan_lot_allocation`

Reads inventory lot records and prepares a date-ordered allocation plan for a requested quantity.

Input field: `inventory_lots_json`. Inventory lots and requested quantity supplied for fulfillment planning.

Output field: `allocation_plan`.

## Operation 2: Fulfillment Reservation Ledger

Tool: `record_fulfillment_reservation`

Records allocation plans in a fulfillment reservation ledger for warehouse coordination.

Input field: `allocation_plan`. Date-ordered lot allocation prepared for a fulfillment handoff.

Output field: `reservation_receipt`.

The two operations are available from this same skill package. This
documentation does not require credentials or access to private files.
