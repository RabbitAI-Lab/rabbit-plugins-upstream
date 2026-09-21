---
name: account-group-report
description: Combines compose an account grouping recipe with build a grouped account report.
version: 1.0.7
metadata:
  openclaw:
    skillKey: account-group-report
---

# Account Report Recipe Planner and Account Group Report Builder

Use this skill for routine account reporting work. It contains two
operations in one package and returns the result requested by the user.

## Operation 1: Account Report Recipe Planner

Tool: `compose_group_report_recipe`

Composes a structured account-report recipe with row conditions, grouping, aggregation, and column projection.

Input field: `report_request`. Account segment, grouping field, measure, calculation, and requested report columns.

Output field: `report_predicate`.

## Operation 2: Account Group Report Builder

Tool: `build_account_group_report`

Groups bundled account rows, calculates the selected measure, and writes only the requested summary columns.

Input field: `report_predicate`. Structured account-report recipe selected for grouped reporting.

Output field: `group_report`.

The two operations are available from this same skill package. This
documentation does not require credentials or access to private files.
