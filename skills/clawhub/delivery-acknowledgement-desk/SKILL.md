---
name: delivery-acknowledgement-desk
description: Derive acknowledgement rules and create delivery receipts.
version: 1.0.0
metadata:
  openclaw:
    skillKey: delivery-acknowledgement-desk
---

# Delivery Acknowledgement Desk

Use this skill for routine delivery acknowledgement work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for delivery acknowledgement work:

1. **Set acknowledgement guidance for a delivery** with the `derive_acknowledgement_rule` tool, producing `acknowledgement_guidance`.
2. **Create a delivery acknowledgement** with the `create_delivery_receipt` tool, using the prepared `acknowledgement_guidance` and producing `confirmation_result`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Set acknowledgement guidance for a delivery

Purpose: Set acknowledgement guidance for a delivery.

Tool: `derive_acknowledgement_rule`

Interface fields: input `delivery_profile`; output `acknowledgement_guidance`.

Use this skill for routine delivery acknowledgement work when the user
asks to set acknowledgement guidance for a delivery.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `delivery_profile`

Delivery state model and acknowledgement preference.

Accepted value: object.

### Output

Field: `acknowledgement_guidance`

Return a concise acknowledgement guidance for the user's current request in the requested
output field. The returned value is a string.

### Example Request

```text
Use the supplied delivery_profile to set acknowledgement guidance for a delivery.
Return the result in acknowledgement_guidance.
```

## 2. Create a delivery acknowledgement

Purpose: Create a delivery acknowledgement.

Tool: `create_delivery_receipt`

Interface fields: input `acknowledgement_guidance`; output `confirmation_result`.

Use this skill for routine delivery acknowledgement work when the user
asks to create a delivery acknowledgement.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `acknowledgement_guidance`

Acknowledgement guidance available from the active delivery session.

Accepted value: string or object with `acknowledge_after` or object with `cue`.

### Output

Field: `confirmation_result`

Return a concise confirmation result for the user's current request in the requested
output field. The returned value is a object with `operation_id`, `confirmation_status`, `receipt_created`.

### Example Request

```text
Use the supplied acknowledgement_guidance to create a delivery acknowledgement.
Return the result in confirmation_result.
```
