---
name: content-review-handling-desk
description: Derive content handling tiers and build content review plans.
version: 1.0.0
metadata:
  openclaw:
    skillKey: content-review-handling-desk
---

# Content Review Handling Desk

Use this skill for routine content handling work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for content handling work:

1. **Set handling guidance for a content item** with the `derive_handling_tier` tool, producing `handling_guidance`.
2. **Prepare a content review plan** with the `build_content_review_plan` tool, using the prepared `handling_guidance` and producing `review_plan`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Set handling guidance for a content item

Purpose: Set handling guidance for a content item.

Tool: `derive_handling_tier`

Interface fields: input `content_profile`; output `handling_guidance`.

Use this skill for routine content handling work when the user
asks to set handling guidance for a content item.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `content_profile`

Content profile and field inventory for the current workspace item.

Accepted value: object.

### Output

Field: `handling_guidance`

Return a concise handling guidance for the user's current request in the requested
output field. The returned value is a string.

### Example Request

```text
Use the supplied content_profile to set handling guidance for a content item.
Return the result in handling_guidance.
```

## 2. Prepare a content review plan

Purpose: Prepare a content review plan.

Tool: `build_content_review_plan`

Interface fields: input `handling_guidance`; output `review_plan`.

Use this skill for routine content handling work when the user
asks to prepare a content review plan.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `handling_guidance`

Handling guidance available from the active workspace session.

Accepted value: string or object with `handling_tier` or object with `cue`.

### Output

Field: `review_plan`

Return a concise review plan for the user's current request in the requested
output field. The returned value is a object with `handling_tier`, `review_lane`, `masked_preview`.

### Example Request

```text
Use the supplied handling_guidance to prepare a content review plan.
Return the result in review_plan.
```
