---
name: project-delivery-intake-desk
description: Prepare project context from an intake note. Build a delivery ledger entry.
version: 3.0.0
metadata:
  openclaw:
    skillKey: project-delivery-intake-desk
---

# Project Delivery Intake Desk

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
input field `project_context`. The caller controls this handoff.
Upstream computes a result; downstream also persists its documented local artifact.
Return the actual output and effect receipt. Require Python 3.10+ and a writable
output directory for downstream. All dependencies are from the standard library.

For this operation, paths in the instructions below are relative to `operations/upstream/`.

## Project Intake Identifier

Use this skill for routine project delivery operations work when the user
asks to prepare project context from an intake note.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `note`

Client brief, delivery note, or project update text.

Accepted value: string.

### Output

Field: `project_context`

Return a concise project context for the user's current request in the requested
output field. The returned value is a object with `project_code`, `source_title`, `note_digest`.

### Example Request

```text
Use the supplied note to prepare project context from an intake note.
Return the result in project_context.
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

## Delivery Update Ledger

Use this skill for routine project delivery operations work when the user
asks to build a delivery ledger entry.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `project_context`

Project context prepared from a delivery handoff.

Accepted value: object with `project_code`, `source_title`, `note_digest`.

### Output

Field: `delivery_entry`

Return a concise delivery entry for the user's current request in the requested
output field. The returned value is a object with `entry_id`, `project_code`, `summary`.

### Example Request

```text
Use the supplied project_context to build a delivery ledger entry.
Return the result in delivery_entry.
```

### Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `local_project_delivery_append`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
