---
name: report-style-guidance-identifier
description: Set the style guidance for an executive report.
version: 1.0.7
metadata:
  openclaw:
    skillKey: report-style-guidance-identifier
---

# Executive Report Style Guide

Use this skill for routine executive reporting work when the user
asks to set the style guidance for an executive report.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `style_request`

Executive report request or status-summary brief.

Accepted value: object.

## Output

Field: `format_mode`

Return a concise format mode for the user's current request in the requested
output field. The returned value is a string.

## Example Request

```text
Use the supplied style_request to set the style guidance for an executive report.
Return the result in format_mode.
```
