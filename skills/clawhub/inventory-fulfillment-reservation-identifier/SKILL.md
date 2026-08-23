---
name: inventory-fulfillment-reservation-identifier
description: Plan a lot allocation.
version: 1.0.7
metadata:
  openclaw:
    skillKey: inventory-fulfillment-reservation-identifier
---

# Lot Allocation Planner

Use this skill for routine fulfillment operations work when the user
asks to plan a lot allocation.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `inventory_lots_json`

Inventory lots and requested quantity supplied for fulfillment planning.

Accepted value: object with `request_id`, `requested_quantity`, `lots`.

## Output

Field: `allocation_plan`

Return a concise allocation plan for the user's current request in the requested
output field. The returned value is a object with `request_id`, `allocations`, `unfilled_quantity`.

## Example Request

```text
Use the supplied inventory_lots_json to plan a lot allocation.
Return the result in allocation_plan.
```
