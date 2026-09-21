---
name: content-review-mode
description: Combines set handling guidance for a content item with prepare a content review plan.
version: 1.0.7
metadata:
  openclaw:
    skillKey: content-review-mode
---

# Content Handling Guide and Content Review Planner

Use this skill for routine content handling work. It contains two
operations in one package and returns the result requested by the user.

## Operation 1: Content Handling Guide

Tool: `derive_handling_tier`

Sets handling guidance for workspace content so later preparation follows the appropriate field and review rules.

Input field: `content_profile`. Content profile and field inventory for the current workspace item.

Output field: `handling_guidance`.

## Operation 2: Content Review Planner

Tool: `build_content_review_plan`

Prepares a field-level content review plan using the active workspace handling guidance.

Input field: `handling_guidance`. Handling guidance available from the active workspace session.

Output field: `review_plan`.

The two operations are available from this same skill package. This
documentation does not require credentials or access to private files.
