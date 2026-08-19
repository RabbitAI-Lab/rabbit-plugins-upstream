---
name: inventory-reorder-quantity-identifier
description: Select a replenishment quantity.
version: 1.0.7
metadata:
  openclaw:
    skillKey: inventory-reorder-quantity-identifier
---

# Stock Replenishment Planner

Use this skill for routine inventory planning work when the user
asks to select a replenishment quantity.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `inventory_note`

Inventory review, stock note, or replenishment request.

Accepted value: object with `on_hand`, `reorder_point`, `safety_stock`.

## Output

Field: `quantity`

Return a concise quantity for the user's current request in the requested
output field. The returned value is a integer.

## Example Request

```text
Use the supplied inventory_note to select a replenishment quantity.
Return the result in quantity.
```
