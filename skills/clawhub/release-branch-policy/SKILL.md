---
name: release-branch-policy
description: Combines select a branch for a release with assess a release branch.
version: 1.0.7
metadata:
  openclaw:
    skillKey: release-branch-policy
---

# Release Branch Planner and Release Branch Policy Desk

Use this skill for routine release governance work. It contains two
operations in one package and returns the result requested by the user.

## Operation 1: Release Branch Planner

Tool: `select_release_branch`

Builds a normalized release branch name from the requested quarter and release name.

Input field: `branch_request`. Release quarter and release name used to derive the source branch.

Output field: `source_branch`.

## Operation 2: Release Branch Policy Desk

Tool: `assess_release_branch`

Compares a selected branch with the branch catalog, expected version line, and eligible release states.

Input field: `source_branch`. Source branch selected for the release-policy assessment.

Output field: `branch_policy_assessment`.

The two operations are available from this same skill package. This
documentation does not require credentials or access to private files.
