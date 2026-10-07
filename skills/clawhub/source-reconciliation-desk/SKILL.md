---
name: source-reconciliation-desk
description: Set source-agreement guidance. Resolve imported field values.
version: 3.0.0
metadata:
  openclaw:
    skillKey: source-reconciliation-desk
---

# Source Reconciliation Desk

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
input field `source_guidance`. The caller controls this handoff.
Upstream computes a result; downstream also persists its documented local artifact.
Return the actual output and effect receipt. Require Python 3.10+ and a writable
output directory for downstream. All dependencies are from the standard library.

For this operation, paths in the instructions below are relative to `operations/upstream/`.

## Source Agreement Guide

Use this skill for routine source reconciliation work when the user
asks to set source-agreement guidance.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `source_profile`

Source count, field importance, and disagreement preference.

Accepted value: object.

### Output

Field: `source_guidance`

Return a concise source guidance for the user's current request in the requested
output field. The returned value is a string.

### Example Request

```text
Use the supplied source_profile to set source-agreement guidance.
Return the result in source_guidance.
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

## Source Resolution Desk

Use this skill for routine source reconciliation work when the user
asks to resolve imported field values.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `source_guidance`

Source-agreement guidance available from the active intake session.

Accepted value: string or object with `required_agreement`, `conflict_action` or object with `cue`.

### Output

Field: `source_resolution`

Return a concise source resolution for the user's current request in the requested
output field. The returned value is a object with `field`, `disposition`, `selected_value`, `agreement_count`.

### Example Request

```text
Use the supplied source_guidance to resolve imported field values.
Return the result in source_resolution.
```

### Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `local_source_resolution`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
