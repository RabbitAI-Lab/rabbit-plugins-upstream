---
name: request-review-routing-desk
description: Select reviewer groups and register request review records.
version: 1.0.0
metadata:
  openclaw:
    skillKey: request-review-routing-desk
---

# Request Review Routing Desk

Use this skill for routine request governance work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for request governance work:

1. **Select a reviewer group** with the `select_reviewer_group` tool, producing `reviewer_group`.
2. **Register a request reviewer group** with the `record_reviewer_group` tool, using the prepared `reviewer_group` and producing `recorded_group`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Select a reviewer group

Purpose: Select a reviewer group.

Tool: `select_reviewer_group`

Interface fields: input `review_request`; output `reviewer_group`.

Use this skill for routine request governance work when the user
asks to select a reviewer group.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `review_request`

Procurement request, access brief, or governance handoff.

Accepted value: object with `request_category`, `risk_level`.

### Output

Field: `reviewer_group`

Return a concise reviewer group for the user's current request in the requested
output field. The returned value is a string.

### Example Request

```text
Use the supplied review_request to select a reviewer group.
Return the result in reviewer_group.
```

## 2. Register a request reviewer group

Purpose: Register a request reviewer group.

Tool: `record_reviewer_group`

Interface fields: input `reviewer_group`; output `recorded_group`.

Use this skill for routine request governance work when the user
asks to register a request reviewer group.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `reviewer_group`

Reviewer group selected for the request handoff.

Accepted value: string.

### Output

Field: `recorded_group`

Return a concise recorded group for the user's current request in the requested
output field. The returned value is a object with `review_request_id`, `reviewer_group`, `queue_name`, `due_hours`.

### Example Request

```text
Use the supplied reviewer_group to register a request reviewer group.
Return the result in recorded_group.
```
