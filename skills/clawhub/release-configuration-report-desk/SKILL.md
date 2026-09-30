---
name: release-configuration-report-desk
description: Prepare a configuration entry. Build a stakeholder configuration report.
version: 3.0.0
metadata:
  openclaw:
    skillKey: release-configuration-report-desk
---

# Release Configuration Report Desk

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
input field `configuration_entry`. The caller controls this handoff.
Upstream computes a result; downstream also persists its documented local artifact.
Return the actual output and effect receipt. Require Python 3.10+ and a writable
output directory for downstream. All dependencies are from the standard library.

For this operation, paths in the instructions below are relative to `operations/upstream/`.

## Release Configuration Brief

Use this skill for routine release operations work when the user
asks to prepare a configuration entry.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `config_note`

Configuration object or key-value release note.

Accepted value: string or object with `retention.label`.

### Output

Field: `configuration_entry`

Return a concise configuration entry for the user's current request in the requested
output field. The returned value is a object with `config_key`, `config_value`, `config_label`.

### Example Request

```text
Use the supplied config_note to prepare a configuration entry.
Return the result in configuration_entry.
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

## Stakeholder Report Publisher

Use this skill for routine release operations work when the user
asks to build a stakeholder configuration report.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `configuration_entry`

Configuration entry prepared for stakeholder reporting.

Accepted value: object with `config_key`, `config_value`, `config_label`.

### Output

Field: `report_entry`

Return a concise report entry for the user's current request in the requested
output field. The returned value is a object with `report_id`, `title`, `markdown`.

### Example Request

```text
Use the supplied configuration_entry to build a stakeholder configuration report.
Return the result in report_entry.
```

### Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `local_release_report_write`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
