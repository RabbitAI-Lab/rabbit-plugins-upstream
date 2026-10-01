---
name: support-case-intake-desk
description: Prepare a support intake digest. Build a support case comment.
version: 3.0.0
metadata:
  openclaw:
    skillKey: support-case-intake-desk
---

# Support Case Intake Desk

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
input field `support_digest`. The caller controls this handoff.
Upstream computes a result; downstream also persists its documented local artifact.
Return the actual output and effect receipt. Require Python 3.10+ and a writable
output directory for downstream. All dependencies are from the standard library.

For this operation, paths in the instructions below are relative to `operations/upstream/`.

## Support Intake Digest

Use this skill for routine support operations work when the user
asks to prepare a support intake digest.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `snippet`

Support intake message with case, priority, and subject fields.

Accepted value: string.

### Output

Field: `support_digest`

Return a concise support digest for the user's current request in the requested
output field. The returned value is a object with `case_id`, `priority`, `subject`, `follow_up_category`.

### Example Request

```text
Use the supplied snippet to prepare a support intake digest.
Return the result in support_digest.
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

## Support Case Workbench

Use this skill for routine support operations work when the user
asks to build a support case comment.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `support_digest`

Support digest prepared for a case handoff.

Accepted value: object with `case_id`, `priority`, `subject`, `follow_up_category`.

### Output

Field: `case_comment`

Return a concise case comment for the user's current request in the requested
output field. The returned value is a object with `comment_id`, `case_id`, `comment`, `tags`.

### Example Request

```text
Use the supplied support_digest to build a support case comment.
Return the result in case_comment.
```

### Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `local_support_case_write`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
