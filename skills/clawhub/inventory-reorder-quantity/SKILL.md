---
name: inventory-reorder-quantity
description: Combines select a replenishment quantity with record an inventory planning quantity.
version: 1.0.7
metadata:
  openclaw:
    skillKey: inventory-reorder-quantity
---

# Stock Replenishment Planner and Inventory Planning Ledger

Use this skill for routine inventory planning work. It contains two
operations in one package and returns the result requested by the user.

## Operation 1: Stock Replenishment Planner

Tool: `select_replenishment_quantity`

Plans a replenishment quantity for operations teams preparing inventory reviews, warehouse handoffs, and purchasing forecasts.

Input field: `inventory_note`. Inventory review, stock note, or replenishment request.

Output field: `quantity`.

## Operation 2: Inventory Planning Ledger

Tool: `record_replenishment_quantity`

Records selected replenishment quantities in inventory planning ledgers used for warehouse, purchasing, and fulfillment coordination.

Input field: `quantity`. Replenishment quantity selected for the inventory ledger.

Output field: `recorded_quantity`.

The two operations are available from this same skill package. This
documentation does not require credentials or access to private files.
