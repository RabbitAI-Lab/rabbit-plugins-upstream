---
name: inventory-fulfillment-reservation-workbench
description: Record a fulfillment reservation.
version: 1.1.0
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

## Bundled execution

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
