---
name: document-release-desk
description: Select the highest approved document version within the requested major release line. Select a document release.
version: 3.0.0
metadata:
  openclaw:
    skillKey: document-release-desk
---

# Document Release Desk

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
input field `selection_guidance`. The caller controls this handoff.
Upstream computes a result; downstream also persists its documented local artifact.
Return the actual output and effect receipt. Require Python 3.10+ and a writable
output directory for downstream. All dependencies are from the standard library.

For this operation, paths in the instructions below are relative to `operations/upstream/`.

## Document Release Guide

Derive a release-selection rule from `release_profile`. This is useful when a
document repository contains drafts, approved revisions, and versions from
several major release lines.

### Eligibility gate

A candidate is eligible only when its approval state satisfies the profile and
its major version matches the requested release line. Exclude withdrawn,
superseded, or draft-only candidates unless the request explicitly permits
them. A newer timestamp does not override an ineligible approval state.

### Precedence within the line

Compare semantic versions numerically. Select the greatest approved version in
the requested major line, using approval time only to resolve duplicate records
for the same version. If no candidate is eligible, return a no-selection rule
with the missing requirement.

### Output

Return `selection_guidance` as a concise string describing the eligibility
gate, the version ordering, the duplicate tie-breaker, and the no-selection
condition. The guide chooses a rule; it does not publish or overwrite a
document.

### Worked case

For requested major version 3, approved `3.4.1` outranks approved `3.3.9`.
Draft `3.5.0` remains ineligible, and approved `4.0.0` belongs to a different
release line.

### Interface reference

Input field: `release_profile`. Current release line and candidate eligibility preference.

Accepted value: object.

Output field: `selection_guidance`; the returned value is a
string.

This standalone documentation does not require credentials or access to private files.

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

## Document Release Selector

Use this skill for routine document release selection work when the user
asks to select a document release.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `selection_guidance`

Release selection guidance available from the active document session.

Accepted value: string or object with `current_major`, `require_approved`, `allow_prerelease` or object with `cue`.

### Output

Field: `selection_result`

Return a concise selection result for the user's current request in the requested
output field. The returned value is a object with `selected_version`, `eligible_versions`, `reason`.

### Example Request

```text
Use the supplied selection_guidance to select a document release.
Return the result in selection_result.
```

### Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `local_document_selection`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
