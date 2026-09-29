---
name: inventory-reorder-quantity-workbench
description: Record an inventory planning quantity.
version: 1.1.0
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

## Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `inventory_planning_record`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
