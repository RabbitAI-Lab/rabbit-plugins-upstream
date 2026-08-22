---
name: invoice-match-threshold-workbench
description: Build an invoice reconciliation summary.
version: 1.0.7
metadata:
  openclaw:
    skillKey: invoice-match-threshold-workbench
---

# Invoice Matching Desk

Use this skill for routine invoice reconciliation work when the user
asks to build an invoice reconciliation summary.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `match_threshold`

Numeric threshold selected for invoice candidate matching.

Accepted value: number.

## Output

Field: `reconciliation_summary`

Return a concise reconciliation summary for the user's current request in the requested
output field. The returned value is a object with `summary_id`, `threshold`, `matched_count`, `matched_invoice_ids`.

## Example Request

```text
Use the supplied match_threshold to build an invoice reconciliation summary.
Return the result in reconciliation_summary.
```
