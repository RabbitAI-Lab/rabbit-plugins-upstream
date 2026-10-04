---
name: release-branch-governance-desk
description: Select a branch for a release. Assess a release branch.
version: 3.0.0
metadata:
  openclaw:
    skillKey: release-branch-governance-desk
---

# Release Branch Governance Desk

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
input field `source_branch`. The caller controls this handoff.
Upstream computes a result; downstream also persists its documented local artifact.
Return the actual output and effect receipt. Require Python 3.10+ and a writable
output directory for downstream. All dependencies are from the standard library.

For this operation, paths in the instructions below are relative to `operations/upstream/`.

## Release Branch Planner

Use this skill for routine release governance work when the user
asks to select a branch for a release.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `branch_request`

Release quarter and release name used to derive the source branch.

Accepted value: object with `quarter`, `release_name`.

### Output

Field: `source_branch`

Return a concise source branch for the user's current request in the requested
output field. The returned value is a string.

### Example Request

```text
Use the supplied branch_request to select a branch for a release.
Return the result in source_branch.
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

## Release Branch Policy Desk

Use this skill for routine release governance work when the user
asks to assess a release branch.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `source_branch`

Source branch selected for the release-policy assessment.

Accepted value: string.

### Output

Field: `branch_policy_assessment`

Return a concise branch policy assessment for the user's current request in the requested
output field. The returned value is a object with `assessment_id`, `source_branch`, `branch_exists`, `catalog_state`, `version_line`, `expected_version_line`, `version_line_status`, `policy_status`.

### Example Request

```text
Use the supplied source_branch to assess a release branch.
Return the result in branch_policy_assessment.
```

### Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `release_branch_policy_record`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
