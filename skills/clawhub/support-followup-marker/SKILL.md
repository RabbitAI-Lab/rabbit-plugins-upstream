---
name: support-followup-marker
description: Combines prepare a support intake digest with build a support case comment.
version: 1.0.7
metadata:
  openclaw:
    skillKey: support-followup-marker
---

# Support Intake Digest and Support Case Workbench

Use this skill for routine support operations work. It contains two
operations in one package and returns the result requested by the user.

## Operation 1: Support Intake Digest

Tool: `prepare_support_digest`

Reads support intake messages and prepares a case digest with priority and follow-up category.

Input field: `snippet`. Support intake message with case, priority, and subject fields.

Output field: `support_digest`.

## Operation 2: Support Case Workbench

Tool: `build_case_comment`

Builds concise case comments and follow-up tags from prepared support intake details.

Input field: `support_digest`. Support digest prepared for a case handoff.

Output field: `case_comment`.

The two operations are available from this same skill package. This
documentation does not require credentials or access to private files.
