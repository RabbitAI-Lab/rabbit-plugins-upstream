---
name: document-release-desk
description: Derive release selection rules and select document releases.
version: 1.0.0
metadata:
  openclaw:
    skillKey: document-release-desk
---

# Document Release Desk

Use this skill for routine document release selection work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for document release selection work:

1. **Set document release selection guidance** with the `derive_release_selection_rule` tool, producing `selection_guidance`.
2. **Select a document release** with the `select_document_release` tool, using the prepared `selection_guidance` and producing `selection_result`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Set document release selection guidance

Purpose: Select the highest approved document version within the requested major release line.

Tool: `derive_release_selection_rule`

Interface fields: input `release_profile`; output `selection_guidance`.

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

## 2. Select a document release

Purpose: Select a document release.

Tool: `select_document_release`

Interface fields: input `selection_guidance`; output `selection_result`.

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
