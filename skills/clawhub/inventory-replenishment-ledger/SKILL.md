---
name: inventory-replenishment-ledger
description: Select a replenishment quantity. Record an inventory planning quantity.
version: 3.0.0
metadata:
  openclaw:
    skillKey: inventory-replenishment-ledger
---

# Inventory Replenishment Ledger

## Execution entry point

This package provides two separately requested operations. Select the operation
that corresponds to the current request. The stage selector invokes that operation
using its bundled implementation, configuration and validation.

```sh
python scripts/run.py --stage upstream --input operations/upstream/examples/request.json
python scripts/run.py --stage downstream --input operations/downstream/examples/request.json --output-dir ./workspace
```

Replace example input paths with the actual request JSON. To pass an upstream
result to the downstream operation, supply that value under the downstream
input field `quantity`. The caller controls this handoff.
Upstream computes a result; downstream also persists its documented local artifact.
Return the actual output and effect receipt. Require Python 3.10+ and a writable
output directory for downstream. All dependencies are from the standard library.

For this operation, paths in the instructions below are relative to `operations/upstream/`.

## Stock Replenishment Planner

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

### Bundled execution

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
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.

For this operation, paths in the instructions below are relative to `operations/downstream/`.

## Inventory Planning Ledger

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

### Bundled execution

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
