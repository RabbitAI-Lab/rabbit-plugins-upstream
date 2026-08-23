---
name: export-confirmation-style-identifier
description: Set acknowledgement guidance for a delivery.
version: 1.0.7
metadata:
  openclaw:
    skillKey: export-confirmation-style-identifier
---

# Delivery Acknowledgement Guide

Use this skill for routine delivery acknowledgement work when the user
asks to set acknowledgement guidance for a delivery.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `delivery_profile`

Delivery state model and acknowledgement preference.

Accepted value: object.

## Output

Field: `acknowledgement_guidance`

Return a concise acknowledgement guidance for the user's current request in the requested
output field. The returned value is a string.

## Example Request

```text
Use the supplied delivery_profile to set acknowledgement guidance for a delivery.
Return the result in acknowledgement_guidance.
```
