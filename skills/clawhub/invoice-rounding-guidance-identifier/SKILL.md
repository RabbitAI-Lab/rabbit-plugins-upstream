---
name: invoice-rounding-guidance-identifier
description: Set invoice rounding guidance.
version: 1.0.7
metadata:
  openclaw:
    skillKey: invoice-rounding-guidance-identifier
---

# Invoice Rounding Guide

Use this skill for routine invoice preparation work when the user
asks to set invoice rounding guidance.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `calculation_request`

Invoice currency and calculation preference.

Accepted value: object.

## Output

Field: `rounding_guidance`

Return a concise rounding guidance for the user's current request in the requested
output field. The returned value is a string.

## Example Request

```text
Use the supplied calculation_request to set invoice rounding guidance.
Return the result in rounding_guidance.
```
