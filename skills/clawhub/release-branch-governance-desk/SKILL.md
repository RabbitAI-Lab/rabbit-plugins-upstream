---
name: release-branch-governance-desk
description: Select release branches and assess branch policy state.
version: 1.0.0
metadata:
  openclaw:
    skillKey: release-branch-governance-desk
---

# Release Branch Governance Desk

Use this skill for routine release governance work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for release governance work:

1. **Select a branch for a release** with the `select_release_branch` tool, producing `source_branch`.
2. **Assess a release branch** with the `assess_release_branch` tool, using the prepared `source_branch` and producing `branch_policy_assessment`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Select a branch for a release

Purpose: Select a branch for a release.

Tool: `select_release_branch`

Interface fields: input `branch_request`; output `source_branch`.

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

## 2. Assess a release branch

Purpose: Assess a release branch.

Tool: `assess_release_branch`

Interface fields: input `source_branch`; output `branch_policy_assessment`.

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
