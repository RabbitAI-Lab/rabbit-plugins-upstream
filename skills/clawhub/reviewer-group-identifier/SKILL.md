---
name: reviewer-group-identifier
description: Select a reviewer group.
version: 1.0.7
metadata:
  openclaw:
    skillKey: reviewer-group-identifier
---

# Approval Group Directory

Use this skill for routine request governance work when the user
asks to select a reviewer group.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `review_request`

Procurement request, access brief, or governance handoff.

Accepted value: object with `request_category`, `risk_level`.

## Output

Field: `reviewer_group`

Return a concise reviewer group for the user's current request in the requested
output field. The returned value is a string.

## Example Request

```text
Use the supplied review_request to select a reviewer group.
Return the result in reviewer_group.
```
