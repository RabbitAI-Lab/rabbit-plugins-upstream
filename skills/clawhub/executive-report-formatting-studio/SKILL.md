---
name: executive-report-formatting-studio
description: Set report style guidance and format stakeholder status reports.
version: 1.0.0
metadata:
  openclaw:
    skillKey: executive-report-formatting-studio
---

# Executive Report Formatting Studio

Use this skill for routine executive reporting work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for executive reporting work:

1. **Set the style guidance for an executive report** with the `advise_report_style` tool, producing `format_mode`.
2. **Format a status report for stakeholders** with the `format_report_with_style` tool, using the prepared `format_mode` and producing `applied_format`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Set the style guidance for an executive report

Purpose: Set the style guidance for an executive report.

Tool: `advise_report_style`

Interface fields: input `style_request`; output `format_mode`.

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

## 2. Format a status report for stakeholders

Purpose: Format a status report for stakeholders.

Tool: `format_report_with_style`

Interface fields: input `format_mode`; output `applied_format`.

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
