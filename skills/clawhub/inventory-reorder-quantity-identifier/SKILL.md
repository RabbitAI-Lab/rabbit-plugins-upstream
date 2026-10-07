---
name: inventory-reorder-quantity-identifier
description: Select a replenishment quantity.
version: 1.1.1
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

## Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json
```

This operation only computes and returns its output; it does not persist a business artifact.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. This package computes its declared output without external communication or persistence.
