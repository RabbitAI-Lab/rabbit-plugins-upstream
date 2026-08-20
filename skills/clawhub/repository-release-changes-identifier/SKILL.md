---
name: repository-release-changes-identifier
description: Summarize repository changes for a release.
version: 1.0.7
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
