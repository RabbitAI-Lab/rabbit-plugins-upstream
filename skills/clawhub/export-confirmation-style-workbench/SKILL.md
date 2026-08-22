---
name: export-confirmation-style-workbench
description: Create a delivery acknowledgement.
version: 1.0.7
metadata:
  openclaw:
    skillKey: export-confirmation-style-workbench
---

# Delivery Receipt Desk

Use this skill for routine delivery acknowledgement work when the user
asks to create a delivery acknowledgement.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `acknowledgement_guidance`

Acknowledgement guidance available from the active delivery session.

Accepted value: string or object with `acknowledge_after` or object with `cue`.

## Output

Field: `confirmation_result`

Return a concise confirmation result for the user's current request in the requested
output field. The returned value is a object with `operation_id`, `confirmation_status`, `receipt_created`.

## Example Request

```text
Use the supplied acknowledgement_guidance to create a delivery acknowledgement.
Return the result in confirmation_result.
```
