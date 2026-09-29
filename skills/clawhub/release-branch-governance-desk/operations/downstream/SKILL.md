---
name: release-branch-policy-workbench
description: Assess a release branch.
version: 1.1.0
metadata:
  openclaw:
    skillKey: release-branch-policy-workbench
---

# Release Branch Policy Desk

Use this skill for routine release governance work when the user
asks to assess a release branch.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `source_branch`

Source branch selected for the release-policy assessment.

Accepted value: string.

## Output

Field: `branch_policy_assessment`

Return a concise branch policy assessment for the user's current request in the requested
output field. The returned value is a object with `assessment_id`, `source_branch`, `branch_exists`, `catalog_state`, `version_line`, `expected_version_line`, `version_line_status`, `policy_status`.

## Example Request

```text
Use the supplied source_branch to assess a release branch.
Return the result in branch_policy_assessment.
```

## Bundled execution

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
