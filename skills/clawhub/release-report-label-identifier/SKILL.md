---
name: release-report-label-identifier
description: Prepare a configuration entry.
version: 1.1.0
metadata:
  openclaw:
    skillKey: release-report-label-identifier
---

# Release Configuration Brief

Use this skill for routine release operations work when the user
asks to prepare a configuration entry.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `config_note`

Configuration object or key-value release note.

Accepted value: string or object with `retention.label`.

## Output

Field: `configuration_entry`

Return a concise configuration entry for the user's current request in the requested
output field. The returned value is a object with `config_key`, `config_value`, `config_label`.

## Example Request

```text
Use the supplied config_note to prepare a configuration entry.
Return the result in configuration_entry.
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
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
