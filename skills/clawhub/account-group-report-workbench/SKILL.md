---
name: account-group-report-workbench
description: Build a grouped account report.
version: 1.0.7
metadata:
  openclaw:
    skillKey: account-group-report-workbench
---

# Account Group Report Builder

Use this skill for routine account reporting work when the user
asks to build a grouped account report.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `report_predicate`

Structured account-report recipe selected for grouped reporting.

Accepted value: object with `where`, `group_by`, `aggregate`, `projected_columns`.

## Output

Field: `group_report`

Return a concise group report for the user's current request in the requested
output field. The returned value is a object with `report_id`, `groups`, `row_count`, `projected_columns`.

## Example Request

```text
Use the supplied report_predicate to build a grouped account report.
Return the result in group_report.
```
