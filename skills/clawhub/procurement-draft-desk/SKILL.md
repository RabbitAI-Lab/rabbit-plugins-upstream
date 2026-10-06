---
name: procurement-draft-desk
description: Prepare supplier purchasing terms. Create a purchase draft.
version: 3.0.0
metadata:
  openclaw:
    skillKey: procurement-draft-desk
---

# Procurement Draft Desk

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
input field `purchase_terms`. The caller controls this handoff.
Upstream computes a result; downstream also persists its documented local artifact.
Return the actual output and effect receipt. Require Python 3.10+ and a writable
output directory for downstream. All dependencies are from the standard library.

For this operation, paths in the instructions below are relative to `operations/upstream/`.

## Supplier Terms Reader

Use this skill for routine procurement operations work when the user
asks to prepare supplier purchasing terms.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `supplier_csv`

Supplier terms table supplied for a procurement handoff.

Accepted value: string or object with `supplier_id`, `currency`, `lead_days`, `incoterm`, `renewal_month`.

### Output

Field: `purchase_terms`

Return a concise purchase terms for the user's current request in the requested
output field. The returned value is a object with `supplier_id`, `currency`, `lead_days`, `incoterm`, `renewal_month`.

### Example Request

```text
Use the supplied supplier_csv to prepare supplier purchasing terms.
Return the result in purchase_terms.
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

## Purchase Draft Desk

Use this skill for routine procurement operations work when the user
asks to create a purchase draft.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `purchase_terms`

Structured supplier terms prepared for sourcing work.

Accepted value: object with `supplier_id`, `currency`, `lead_days`, `incoterm`, `renewal_month`.

### Output

Field: `purchase_draft_id`

Return a concise purchase draft id for the user's current request in the requested
output field. The returned value is a object with `draft_id`, `status`, `supplier_id`, `summary`.

### Example Request

```text
Use the supplied purchase_terms to create a purchase draft.
Return the result in purchase_draft_id.
```

### Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `local_purchase_draft_insert`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
