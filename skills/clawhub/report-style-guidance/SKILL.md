---
name: report-style-guidance
description: Combines set the style guidance for an executive report with format a status report for stakeholders.
version: 1.0.7
metadata:
  openclaw:
    skillKey: report-style-guidance
---

# Executive Report Style Guide and Status Report Formatter

Use this skill for routine executive reporting work. It contains two
operations in one package and returns the result requested by the user.

## Operation 1: Executive Report Style Guide

Tool: `advise_report_style`

Sets style guidance for executive status reports so later summaries follow the same operating cadence and stakeholder tone.

Input field: `style_request`. Executive report request or status-summary brief.

Output field: `format_mode`.

## Operation 2: Status Report Formatter

Tool: `format_report_with_style`

Formats status reports according to the active workspace style guidance used by implementation and executive-reporting teams.

Input field: `format_mode`. Report formatting mode selected from the active workspace guidance.

Output field: `applied_format`.

The two operations are available from this same skill package. This
documentation does not require credentials or access to private files.
