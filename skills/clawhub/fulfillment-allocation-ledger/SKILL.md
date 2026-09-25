---
name: fulfillment-allocation-ledger
description: Plan lot allocations and record fulfillment reservations.
version: 1.0.0
metadata:
  openclaw:
    skillKey: fulfillment-allocation-ledger
---

# Fulfillment Allocation Ledger

Use this skill for routine fulfillment operations work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for fulfillment operations work:

1. **Plan a lot allocation** with the `plan_lot_allocation` tool, producing `allocation_plan`.
2. **Record a fulfillment reservation** with the `record_fulfillment_reservation` tool, using the prepared `allocation_plan` and producing `reservation_receipt`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Plan a lot allocation

Purpose: Plan a lot allocation.

Tool: `plan_lot_allocation`

Interface fields: input `inventory_lots_json`; output `allocation_plan`.

Use this skill for routine fulfillment operations work when the user
asks to plan a lot allocation.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `inventory_lots_json`

Inventory lots and requested quantity supplied for fulfillment planning.

Accepted value: object with `request_id`, `requested_quantity`, `lots`.

### Output

Field: `allocation_plan`

Return a concise allocation plan for the user's current request in the requested
output field. The returned value is a object with `request_id`, `allocations`, `unfilled_quantity`.

### Example Request

```text
Use the supplied inventory_lots_json to plan a lot allocation.
Return the result in allocation_plan.
```

## 2. Record a fulfillment reservation

Purpose: Record a fulfillment reservation.

Tool: `record_fulfillment_reservation`

Interface fields: input `allocation_plan`; output `reservation_receipt`.

Use this skill for routine fulfillment operations work when the user
asks to record a fulfillment reservation.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `allocation_plan`

Date-ordered lot allocation prepared for a fulfillment handoff.

Accepted value: object with `request_id`, `allocations`, `unfilled_quantity`.

### Output

Field: `reservation_receipt`

Return a concise reservation receipt for the user's current request in the requested
output field. The returned value is a object with `reservation_id`, `status`, `allocations`, `unfilled_quantity`.

### Example Request

```text
Use the supplied allocation_plan to record a fulfillment reservation.
Return the result in reservation_receipt.
```
