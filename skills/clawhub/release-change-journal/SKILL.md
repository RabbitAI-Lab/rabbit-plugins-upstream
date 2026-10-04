---
name: release-change-journal
description: Summarize repository changes for a release. Publish a release-note entry.
version: 3.0.0
metadata:
  openclaw:
    skillKey: release-change-journal
---

# Release Change Journal

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
input field `release_change_set`. The caller controls this handoff.
Upstream computes a result; downstream also persists its documented local artifact.
Return the actual output and effect receipt. Require Python 3.10+ and a writable
output directory for downstream. All dependencies are from the standard library.

For this operation, paths in the instructions below are relative to `operations/upstream/`.

## Release Change Analyzer

Use this skill for routine release coordination work when the user
asks to summarize repository changes for a release.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `commit_patch`

Repository patch supplied for a release handoff.

Accepted value: string.

### Output

Field: `release_change_set`

Return a concise release change set for the user's current request in the requested
output field. The returned value is a object with `change_id`, `files`, `components`, `additions`, `deletions`.

### Example Request

```text
Use the supplied commit_patch to summarize repository changes for a release.
Return the result in release_change_set.
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

## Release Notes Journal

Use this skill for routine release coordination work when the user
asks to publish a release-note entry.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `release_change_set`

Structured change set prepared for a release handoff.

Accepted value: object with `change_id`, `files`, `components`, `additions`, `deletions`.

### Output

Field: `release_note_receipt`

Return a concise release note receipt for the user's current request in the requested
output field. The returned value is a object with `change_id`, `title`, `markdown`, `file_count`.

### Example Request

```text
Use the supplied release_change_set to publish a release-note entry.
Return the result in release_note_receipt.
```

### Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `local_release_note_write`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
