---
name: reviewer-group-workbench
description: Register a request reviewer group.
version: 1.0.7
metadata:
  openclaw:
    skillKey: reviewer-group-workbench
---

# Request Review Register

Use this skill for routine request governance work when the user
asks to register a request reviewer group.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `reviewer_group`

Reviewer group selected for the request handoff.

Accepted value: string.

## Output

Field: `recorded_group`

Return a concise recorded group for the user's current request in the requested
output field. The returned value is a object with `review_request_id`, `reviewer_group`, `queue_name`, `due_hours`.

## Example Request

```text
Use the supplied reviewer_group to register a request reviewer group.
Return the result in recorded_group.
```
