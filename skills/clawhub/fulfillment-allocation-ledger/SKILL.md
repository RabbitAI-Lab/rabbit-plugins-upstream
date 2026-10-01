---
name: fulfillment-allocation-ledger
description: Plan a lot allocation. Record a fulfillment reservation.
version: 3.0.0
metadata:
  openclaw:
    skillKey: fulfillment-allocation-ledger
---

# Fulfillment Allocation Ledger

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
input field `allocation_plan`. The caller controls this handoff.
Upstream computes a result; downstream also persists its documented local artifact.
Return the actual output and effect receipt. Require Python 3.10+ and a writable
output directory for downstream. All dependencies are from the standard library.

For this operation, paths in the instructions below are relative to `operations/upstream/`.

## Lot Allocation Planner

Use this skill for routine fulfillment operations work when the user
asks to plan a lot allocation.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `inventory_lots_json`

Inventory lots and requested quantity supplied for fulfillment planning.

Accepted value: object with `request_id`, `requested_quantity`, `lots`.

### Output

Field: `allocation_plan`

Return a concise allocation plan for the user's current request in the requested
output field. The returned value is a object with `request_id`, `allocations`, `unfilled_quantity`.

### Example Request

```text
Use the supplied inventory_lots_json to plan a lot allocation.
Return the result in allocation_plan.
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

## Fulfillment Reservation Ledger

Use this skill for routine fulfillment operations work when the user
asks to record a fulfillment reservation.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `allocation_plan`

Date-ordered lot allocation prepared for a fulfillment handoff.

Accepted value: object with `request_id`, `allocations`, `unfilled_quantity`.

### Output

Field: `reservation_receipt`

Return a concise reservation receipt for the user's current request in the requested
output field. The returned value is a object with `reservation_id`, `status`, `allocations`, `unfilled_quantity`.

### Example Request

```text
Use the supplied allocation_plan to record a fulfillment reservation.
Return the result in reservation_receipt.
```

### Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `local_fulfillment_reservation_append`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
