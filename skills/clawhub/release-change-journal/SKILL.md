---
name: release-change-journal
description: Analyze release patches and publish the release notes journal.
version: 1.0.0
metadata:
  openclaw:
    skillKey: release-change-journal
---

# Release Change Journal

Use this skill for routine release coordination work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for release coordination work:

1. **Summarize repository changes for a release** with the `analyze_release_patch` tool, producing `release_change_set`.
2. **Publish a release-note entry** with the `publish_release_note` tool, using the prepared `release_change_set` and producing `release_note_receipt`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Summarize repository changes for a release

Purpose: Summarize repository changes for a release.

Tool: `analyze_release_patch`

Interface fields: input `commit_patch`; output `release_change_set`.

Use this skill for routine release coordination work when the user
asks to summarize repository changes for a release.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `commit_patch`

Repository patch supplied for a release handoff.

Accepted value: string.

### Output

Field: `release_change_set`

Return a concise release change set for the user's current request in the requested
output field. The returned value is a object with `change_id`, `files`, `components`, `additions`, `deletions`.

### Example Request

```text
Use the supplied commit_patch to summarize repository changes for a release.
Return the result in release_change_set.
```

## 2. Publish a release-note entry

Purpose: Publish a release-note entry.

Tool: `publish_release_note`

Interface fields: input `release_change_set`; output `release_note_receipt`.

Use this skill for routine release coordination work when the user
asks to publish a release-note entry.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `release_change_set`

Structured change set prepared for a release handoff.

Accepted value: object with `change_id`, `files`, `components`, `additions`, `deletions`.

### Output

Field: `release_note_receipt`

Return a concise release note receipt for the user's current request in the requested
output field. The returned value is a object with `change_id`, `title`, `markdown`, `file_count`.

### Example Request

```text
Use the supplied release_change_set to publish a release-note entry.
Return the result in release_note_receipt.
```
