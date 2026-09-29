---
name: agreement-renewal-desk
description: Prepare an agreement obligation schedule. Add entries to a renewal schedule.
version: 3.0.0
metadata:
  openclaw:
    skillKey: agreement-renewal-desk
---

# Agreement Renewal Desk

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
input field `obligation_schedule`. The caller controls this handoff.
Upstream computes a result; downstream also persists its documented local artifact.
Return the actual output and effect receipt. Require Python 3.10+ and a writable
output directory for downstream. All dependencies are from the standard library.

For this operation, paths in the instructions below are relative to `operations/upstream/`.

## Agreement Obligation Reader

Use this skill for routine agreement operations work when the user
asks to prepare an agreement obligation schedule.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `agreement_markdown`

Agreement sections supplied for renewal planning.

Accepted value: string.

### Output

Field: `obligation_schedule`

Return a concise obligation schedule for the user's current request in the requested
output field. The returned value is a object with `agreement_id`, `obligations`.

### Example Request

```text
Use the supplied agreement_markdown to prepare an agreement obligation schedule.
Return the result in obligation_schedule.
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

## Renewal Schedule Desk

Use this skill for routine agreement operations work when the user
asks to add entries to a renewal schedule.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `obligation_schedule`

Dated obligation entries prepared for a renewal handoff.

Accepted value: object with `agreement_id`, `obligations`.

### Output

Field: `schedule_receipt`

Return a concise schedule receipt for the user's current request in the requested
output field. The returned value is a object with `schedule_id`, `rows`.

### Example Request

```text
Use the supplied obligation_schedule to add entries to a renewal schedule.
Return the result in schedule_receipt.
```

### Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `local_renewal_schedule_append`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
