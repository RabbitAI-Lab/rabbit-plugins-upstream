---
name: repository-release-changes-identifier
description: Summarize repository changes for a release.
version: 1.1.1
metadata:
  openclaw:
    skillKey: repository-release-changes-identifier
---

# Release Change Analyzer

Use this skill for routine release coordination work when the user
asks to summarize repository changes for a release.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `commit_patch`

Repository patch supplied for a release handoff.

Accepted value: string.

## Output

Field: `release_change_set`

Return a concise release change set for the user's current request in the requested
output field. The returned value is a object with `change_id`, `files`, `components`, `additions`, `deletions`.

## Example Request

```text
Use the supplied commit_patch to summarize repository changes for a release.
Return the result in release_change_set.
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
local records are included for reproducibility. This package computes its declared output without external communication or persistence.
