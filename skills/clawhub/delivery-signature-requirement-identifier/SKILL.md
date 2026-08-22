---
name: delivery-signature-requirement-identifier
description: Determine a signature requirement.
version: 1.0.7
metadata:
  openclaw:
    skillKey: delivery-signature-requirement-identifier
---

# Delivery Requirement Advisor

Use this skill for routine delivery operations work when the user
asks to determine a signature requirement.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `delivery_request`

Package class and service level for a delivery handoff.

Accepted value: object with `package_class`, `service_level`.

## Output

Field: `requires_signature`

Return a concise requires signature for the user's current request in the requested
output field. The returned value is a boolean.

## Example Request

```text
Use the supplied delivery_request to determine a signature requirement.
Return the result in requires_signature.
```
