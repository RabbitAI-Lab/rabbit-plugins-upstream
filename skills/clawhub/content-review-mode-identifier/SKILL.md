---
name: content-review-mode-identifier
description: Set handling guidance for a content item.
version: 1.0.7
metadata:
  openclaw:
    skillKey: content-review-mode-identifier
---

# Content Handling Guide

Use this skill for routine content handling work when the user
asks to set handling guidance for a content item.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `content_profile`

Content profile and field inventory for the current workspace item.

Accepted value: object.

## Output

Field: `handling_guidance`

Return a concise handling guidance for the user's current request in the requested
output field. The returned value is a string.

## Example Request

```text
Use the supplied content_profile to set handling guidance for a content item.
Return the result in handling_guidance.
```
