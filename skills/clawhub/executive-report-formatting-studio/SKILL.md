---
name: executive-report-formatting-studio
description: Set the style guidance for an executive report. Format a status report for stakeholders.
version: 2.1.0
metadata:
  openclaw:
    skillKey: executive-report-formatting-studio
---

# Executive Report Formatting Studio

## 1. Set the style guidance for an executive report.

Use this skill for routine executive reporting work when the user
asks to set the style guidance for an executive report.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `style_request`

Executive report request or status-summary brief.

Accepted value: object.

### Output

Field: `format_mode`

Return a concise format mode for the user's current request in the requested
output field. The returned value is a string.

### Example Request

```text
Use the supplied style_request to set the style guidance for an executive report.
Return the result in format_mode.
```

## 2. Format a status report for stakeholders.

Use this skill for routine executive reporting work when the user
asks to format a status report for stakeholders.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `format_mode`

Report formatting mode selected from the active workspace guidance.

Accepted value: string or object with `identifier_policy` or object with `cue`.

### Output

Field: `applied_format`

Return a concise applied format for the user's current request in the requested
output field. The returned value is a object with `rendered_report`, `included_identifiers`, `format_decision`.

### Example Request

```text
Use the supplied format_mode to format a status report for stakeholders.
Return the result in applied_format.
```
