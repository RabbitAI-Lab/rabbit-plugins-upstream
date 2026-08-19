---
name: inventory-reorder-quantity-workbench
description: Record an inventory planning quantity.
version: 1.0.7
metadata:
  openclaw:
    skillKey: inventory-reorder-quantity-workbench
---

# Inventory Planning Ledger

Use this skill for routine inventory planning work when the user
asks to record an inventory planning quantity.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `quantity`

Replenishment quantity selected for the inventory ledger.

Accepted value: integer.

## Output

Field: `recorded_quantity`

Return a concise recorded quantity for the user's current request in the requested
output field. The returned value is a object with `plan_entry_id`, `quantity`, `case_pack`, `carton_count`, `planning_action`.

## Example Request

```text
Use the supplied quantity to record an inventory planning quantity.
Return the result in recorded_quantity.
```
