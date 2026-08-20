---
name: delivery-recovery-guidance-identifier
description: Set delivery recovery guidance.
version: 1.0.7
metadata:
  openclaw:
    skillKey: delivery-recovery-guidance-identifier
---

# Delivery Recovery Guide

Use this skill for routine delivery operations work when the user
asks to set delivery recovery guidance.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `recovery_request`

Delivery handoff, transfer note, or service recovery request.

Accepted value: object.

## Output

Field: `retry_mode`

Return a concise retry mode for the user's current request in the requested
output field. The returned value is a string.

## Example Request

```text
Use the supplied recovery_request to set delivery recovery guidance.
Return the result in retry_mode.
```
