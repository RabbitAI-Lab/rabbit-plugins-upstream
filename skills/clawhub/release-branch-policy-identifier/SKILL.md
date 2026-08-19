---
name: release-branch-policy-identifier
description: Select a branch for a release.
version: 1.0.7
metadata:
  openclaw:
    skillKey: release-branch-policy-identifier
---

# Release Branch Planner

Use this skill for routine release governance work when the user
asks to select a branch for a release.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `branch_request`

Release quarter and release name used to derive the source branch.

Accepted value: object with `quarter`, `release_name`.

## Output

Field: `source_branch`

Return a concise source branch for the user's current request in the requested
output field. The returned value is a string.

## Example Request

```text
Use the supplied branch_request to select a branch for a release.
Return the result in source_branch.
```
