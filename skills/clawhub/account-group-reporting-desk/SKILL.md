---
name: account-group-reporting-desk
description: Compose grouping recipes and build grouped account reports.
version: 1.0.0
metadata:
  openclaw:
    skillKey: account-group-reporting-desk
---

# Account Group Reporting Desk

Use this skill for routine account reporting work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for account reporting work:

1. **Compose an account grouping recipe** with the `compose_group_report_recipe` tool, producing `report_predicate`.
2. **Build a grouped account report** with the `build_account_group_report` tool, using the prepared `report_predicate` and producing `group_report`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Compose an account grouping recipe

Purpose: Compose an account grouping recipe.

Tool: `compose_group_report_recipe`

Interface fields: input `report_request`; output `report_predicate`.

Use this skill for routine account reporting work when the user
asks to compose an account grouping recipe.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `report_request`

Account segment, grouping field, measure, calculation, and requested report columns.

Accepted value: object with `segment`, `group_by`, `measure`, `calculation`, `columns`.

### Output

Field: `report_predicate`

Return a concise report predicate for the user's current request in the requested
output field. The returned value is a object with `where`, `group_by`, `aggregate`, `projected_columns`.

### Example Request

```text
Use the supplied report_request to compose an account grouping recipe.
Return the result in report_predicate.
```

## 2. Build a grouped account report

Purpose: Build a grouped account report.

Tool: `build_account_group_report`

Interface fields: input `report_predicate`; output `group_report`.

Use this skill for routine account reporting work when the user
asks to build a grouped account report.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `report_predicate`

Structured account-report recipe selected for grouped reporting.

Accepted value: object with `where`, `group_by`, `aggregate`, `projected_columns`.

### Output

Field: `group_report`

Return a concise group report for the user's current request in the requested
output field. The returned value is a object with `report_id`, `groups`, `row_count`, `projected_columns`.

### Example Request

```text
Use the supplied report_predicate to build a grouped account report.
Return the result in group_report.
```
