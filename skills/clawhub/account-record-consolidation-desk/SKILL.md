---
name: account-record-consolidation-desk
description: Derive field consolidation rules and consolidate account records.
version: 1.0.0
metadata:
  openclaw:
    skillKey: account-record-consolidation-desk
---

# Account Record Consolidation Desk

Use this skill for routine account maintenance work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for account maintenance work:

1. **Set account merge guidance** with the `derive_account_merge_rule` tool, producing `merge_guidance`.
2. **Merge an account revision** with the `merge_account_fields` tool, using the prepared `merge_guidance` and producing `merge_result`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Set account merge guidance

Purpose: Set account merge guidance.

Tool: `derive_account_merge_rule`

Interface fields: input `revision_profile`; output `merge_guidance`.

Use this skill for routine account maintenance work when the user
asks to set account merge guidance.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `revision_profile`

Account revision profile and field-preservation preference.

Accepted value: object.

### Output

Field: `merge_guidance`

Return a concise merge guidance for the user's current request in the requested
output field. The returned value is a string.

### Example Request

```text
Use the supplied revision_profile to set account merge guidance.
Return the result in merge_guidance.
```

## 2. Merge an account revision

Purpose: Merge an account revision.

Tool: `merge_account_fields`

Interface fields: input `merge_guidance`; output `merge_result`.

Use this skill for routine account maintenance work when the user
asks to merge an account revision.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `merge_guidance`

Field merge guidance available from the active account session.

Accepted value: string or object with `strategy`, `preserve_absent`, `accept_blank` or object with `cue`.

### Output

Field: `merge_result`

Return a concise merge result for the user's current request in the requested
output field. The returned value is a object with `merged_record`, `changed_fields`, `preserved_fields`.

### Example Request

```text
Use the supplied merge_guidance to merge an account revision.
Return the result in merge_result.
```
