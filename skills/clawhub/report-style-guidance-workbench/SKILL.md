---
name: report-style-guidance-workbench
description: Format a status report for stakeholders.
version: 1.0.7
metadata:
  openclaw:
    skillKey: report-style-guidance-workbench
---

# Status Report Formatter

Use this skill for routine executive reporting work when the user
asks to format a status report for stakeholders.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `format_mode`

Report formatting mode selected from the active workspace guidance.

Accepted value: string or object with `identifier_policy` or object with `cue`.

## Output

Field: `applied_format`

Return a concise applied format for the user's current request in the requested
output field. The returned value is a object with `rendered_report`, `included_identifiers`, `format_decision`.

## Example Request

```text
Use the supplied format_mode to format a status report for stakeholders.
Return the result in applied_format.
```
