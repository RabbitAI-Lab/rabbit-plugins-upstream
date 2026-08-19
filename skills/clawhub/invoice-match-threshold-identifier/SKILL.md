---
name: invoice-match-threshold-identifier
description: Derive an invoice-match threshold.
version: 1.0.7
metadata:
  openclaw:
    skillKey: invoice-match-threshold-identifier
---

# Reconciliation Threshold Planner

Use this skill for routine invoice reconciliation work when the user
asks to derive an invoice-match threshold.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `reconciliation_rule`

Permitted variance for an invoice reconciliation workflow.

Accepted value: object with `allowed_variance`.

## Output

Field: `match_threshold`

Return a concise match threshold for the user's current request in the requested
output field. The returned value is a number.

## Example Request

```text
Use the supplied reconciliation_rule to derive an invoice-match threshold.
Return the result in match_threshold.
```
