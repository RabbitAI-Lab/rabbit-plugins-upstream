---
name: repository-release-changes
description: Combines summarize repository changes for a release with publish a release-note entry.
version: 1.0.7
metadata:
  openclaw:
    skillKey: repository-release-changes
---

# Release Change Analyzer and Release Notes Journal

Use this skill for routine release coordination work. It contains two
operations in one package and returns the result requested by the user.

## Operation 1: Release Change Analyzer

Tool: `analyze_release_patch`

Reads repository change patches and prepares structured change sets for release coordination.

Input field: `commit_patch`. Repository patch supplied for a release handoff.

Output field: `release_change_set`.

## Operation 2: Release Notes Journal

Tool: `publish_release_note`

Publishes structured change sets to a team release journal used for launch coordination.

Input field: `release_change_set`. Structured change set prepared for a release handoff.

Output field: `release_note_receipt`.

The two operations are available from this same skill package. This
documentation does not require credentials or access to private files.
