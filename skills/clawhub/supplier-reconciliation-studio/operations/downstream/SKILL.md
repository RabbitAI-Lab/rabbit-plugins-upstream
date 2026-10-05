---
name: supplier-name-resolution-workbench
description: Reconcile supplier names.
version: 1.1.0
metadata:
  openclaw:
    skillKey: supplier-name-resolution-workbench
---

# Supplier Reconciliation Desk

Use this skill for routine supplier reconciliation work when the user
asks to reconcile supplier names.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `matching_guidance`

Name-matching guidance available from the active reconciliation session.

Accepted value: string or object with `normalization_steps`, `minimum_score` or object with `cue`.

## Output

Field: `match_result`

Return a concise match result for the user's current request in the requested
output field. The returned value is a object with `matched`, `left_canonical`, `right_canonical`, `score`.

## Example Request

```text
Use the supplied matching_guidance to reconcile supplier names.
Return the result in match_result.
```

## Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `local_entity_match_report`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
