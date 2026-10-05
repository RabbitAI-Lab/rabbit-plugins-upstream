---
name: inventory-fulfillment-reservation-identifier
description: Plan a lot allocation.
version: 1.1.1
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
