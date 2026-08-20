---
name: inventory-fulfillment-reservation-workbench
description: Record a fulfillment reservation.
version: 1.0.7
metadata:
  openclaw:
    skillKey: inventory-fulfillment-reservation-workbench
---

# Fulfillment Reservation Ledger

Use this skill for routine fulfillment operations work when the user
asks to record a fulfillment reservation.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `allocation_plan`

Date-ordered lot allocation prepared for a fulfillment handoff.

Accepted value: object with `request_id`, `allocations`, `unfilled_quantity`.

## Output

Field: `reservation_receipt`

Return a concise reservation receipt for the user's current request in the requested
output field. The returned value is a object with `reservation_id`, `status`, `allocations`, `unfilled_quantity`.

## Example Request

```text
Use the supplied allocation_plan to record a fulfillment reservation.
Return the result in reservation_receipt.
```
