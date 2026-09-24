---
name: support-case-intake-desk
description: Digest support snippets and post prepared case comments.
version: 1.0.0
metadata:
  openclaw:
    skillKey: support-case-intake-desk
---

# Support Case Intake Desk

Use this skill for routine support operations work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for support operations work:

1. **Prepare a support intake digest** with the `prepare_support_digest` tool, producing `support_digest`.
2. **Build a support case comment** with the `build_case_comment` tool, using the prepared `support_digest` and producing `case_comment`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Prepare a support intake digest

Purpose: Prepare a support intake digest.

Tool: `prepare_support_digest`

Interface fields: input `snippet`; output `support_digest`.

Use this skill for routine support operations work when the user
asks to prepare a support intake digest.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `snippet`

Support intake message with case, priority, and subject fields.

Accepted value: string.

### Output

Field: `support_digest`

Return a concise support digest for the user's current request in the requested
output field. The returned value is a object with `case_id`, `priority`, `subject`, `follow_up_category`.

### Example Request

```text
Use the supplied snippet to prepare a support intake digest.
Return the result in support_digest.
```

## 2. Build a support case comment

Purpose: Build a support case comment.

Tool: `build_case_comment`

Interface fields: input `support_digest`; output `case_comment`.

Use this skill for routine support operations work when the user
asks to build a support case comment.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `support_digest`

Support digest prepared for a case handoff.

Accepted value: object with `case_id`, `priority`, `subject`, `follow_up_category`.

### Output

Field: `case_comment`

Return a concise case comment for the user's current request in the requested
output field. The returned value is a object with `comment_id`, `case_id`, `comment`, `tags`.

### Example Request

```text
Use the supplied support_digest to build a support case comment.
Return the result in case_comment.
```
