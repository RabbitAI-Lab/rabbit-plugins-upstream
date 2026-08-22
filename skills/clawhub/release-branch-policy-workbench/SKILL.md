---
name: release-branch-policy-workbench
description: Assess a release branch.
version: 1.0.7
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
