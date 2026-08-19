---
name: account-group-report-identifier
description: Compose an account grouping recipe.
version: 1.0.7
metadata:
  openclaw:
    skillKey: account-group-report-identifier
---

# Account Report Recipe Planner

Use this skill for routine account reporting work when the user
asks to compose an account grouping recipe.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `report_request`

Account segment, grouping field, measure, calculation, and requested report columns.

Accepted value: object with `segment`, `group_by`, `measure`, `calculation`, `columns`.

## Output

Field: `report_predicate`

Return a concise report predicate for the user's current request in the requested
output field. The returned value is a object with `where`, `group_by`, `aggregate`, `projected_columns`.

## Example Request

```text
Use the supplied report_request to compose an account grouping recipe.
Return the result in report_predicate.
```
