---
name: inventory-replenishment-ledger
description: Select replenishment quantities and record planning entries.
version: 1.0.0
metadata:
  openclaw:
    skillKey: inventory-replenishment-ledger
---

# Inventory Replenishment Ledger

Use this skill for routine inventory planning work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for inventory planning work:

1. **Select a replenishment quantity** with the `select_replenishment_quantity` tool, producing `quantity`.
2. **Record an inventory planning quantity** with the `record_replenishment_quantity` tool, using the prepared `quantity` and producing `recorded_quantity`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Select a replenishment quantity

Purpose: Select a replenishment quantity.

Tool: `select_replenishment_quantity`

Interface fields: input `inventory_note`; output `quantity`.

Use this skill for routine inventory planning work when the user
asks to select a replenishment quantity.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `inventory_note`

Inventory review, stock note, or replenishment request.

Accepted value: object with `on_hand`, `reorder_point`, `safety_stock`.

### Output

Field: `quantity`

Return a concise quantity for the user's current request in the requested
output field. The returned value is a integer.

### Example Request

```text
Use the supplied inventory_note to select a replenishment quantity.
Return the result in quantity.
```

## 2. Record an inventory planning quantity

Purpose: Record an inventory planning quantity.

Tool: `record_replenishment_quantity`

Interface fields: input `quantity`; output `recorded_quantity`.

Use this skill for routine inventory planning work when the user
asks to record an inventory planning quantity.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `quantity`

Replenishment quantity selected for the inventory ledger.

Accepted value: integer.

### Output

Field: `recorded_quantity`

Return a concise recorded quantity for the user's current request in the requested
output field. The returned value is a object with `plan_entry_id`, `quantity`, `case_pack`, `carton_count`, `planning_action`.

### Example Request

```text
Use the supplied quantity to record an inventory planning quantity.
Return the result in recorded_quantity.
```
