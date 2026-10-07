---
name: invoice-reconciliation-desk
description: Derive an invoice-match threshold. Build an invoice reconciliation summary.
version: 3.0.0
metadata:
  openclaw:
    skillKey: invoice-reconciliation-desk
---

# Invoice Reconciliation Desk

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
input field `match_threshold`. The caller controls this handoff.
Upstream computes a result; downstream also persists its documented local artifact.
Return the actual output and effect receipt. Require Python 3.10+ and a writable
output directory for downstream. All dependencies are from the standard library.

For this operation, paths in the instructions below are relative to `operations/upstream/`.

## Reconciliation Threshold Planner

Use this skill for routine invoice reconciliation work when the user
asks to derive an invoice-match threshold.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `reconciliation_rule`

Permitted variance for an invoice reconciliation workflow.

Accepted value: object with `allowed_variance`.

### Output

Field: `match_threshold`

Return a concise match threshold for the user's current request in the requested
output field. The returned value is a number.

### Example Request

```text
Use the supplied reconciliation_rule to derive an invoice-match threshold.
Return the result in match_threshold.
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

## Invoice Matching Desk

Use this skill for routine invoice reconciliation work when the user
asks to build an invoice reconciliation summary.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `match_threshold`

Numeric threshold selected for invoice candidate matching.

Accepted value: number.

### Output

Field: `reconciliation_summary`

Return a concise reconciliation summary for the user's current request in the requested
output field. The returned value is a object with `summary_id`, `threshold`, `matched_count`, `matched_invoice_ids`.

### Example Request

```text
Use the supplied match_threshold to build an invoice reconciliation summary.
Return the result in reconciliation_summary.
```

### Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `reconciliation_summary`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
