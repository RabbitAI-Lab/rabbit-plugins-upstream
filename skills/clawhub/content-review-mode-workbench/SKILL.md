---
name: content-review-mode-workbench
description: Prepare a content review plan.
version: 1.0.7
metadata:
  openclaw:
    skillKey: content-review-mode-workbench
---

# Content Review Planner

Use this skill for routine content handling work when the user
asks to prepare a content review plan.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `handling_guidance`

Handling guidance available from the active workspace session.

Accepted value: string or object with `handling_tier` or object with `cue`.

## Output

Field: `review_plan`

Return a concise review plan for the user's current request in the requested
output field. The returned value is a object with `handling_tier`, `review_lane`, `masked_preview`.

## Example Request

```text
Use the supplied handling_guidance to prepare a content review plan.
Return the result in review_plan.
```
