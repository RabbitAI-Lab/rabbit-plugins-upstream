---
name: invoice-reconciliation-desk
description: Derive match thresholds and build invoice reconciliation summaries.
version: 1.0.0
metadata:
  openclaw:
    skillKey: invoice-reconciliation-desk
---

# Invoice Reconciliation Desk

Use this skill for routine invoice reconciliation work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for invoice reconciliation work:

1. **Derive an invoice-match threshold** with the `derive_match_threshold` tool, producing `match_threshold`.
2. **Build an invoice reconciliation summary** with the `apply_match_threshold` tool, using the prepared `match_threshold` and producing `reconciliation_summary`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Derive an invoice-match threshold

Purpose: Derive an invoice-match threshold.

Tool: `derive_match_threshold`

Interface fields: input `reconciliation_rule`; output `match_threshold`.

Use this skill for routine invoice reconciliation work when the user
asks to derive an invoice-match threshold.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `reconciliation_rule`

Permitted variance for an invoice reconciliation workflow.

Accepted value: object with `allowed_variance`.

### Output

Field: `match_threshold`

Return a concise match threshold for the user's current request in the requested
output field. The returned value is a number.

### Example Request

```text
Use the supplied reconciliation_rule to derive an invoice-match threshold.
Return the result in match_threshold.
```

## 2. Build an invoice reconciliation summary

Purpose: Build an invoice reconciliation summary.

Tool: `apply_match_threshold`

Interface fields: input `match_threshold`; output `reconciliation_summary`.

Use this skill for routine invoice reconciliation work when the user
asks to build an invoice reconciliation summary.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `match_threshold`

Numeric threshold selected for invoice candidate matching.

Accepted value: number.

### Output

Field: `reconciliation_summary`

Return a concise reconciliation summary for the user's current request in the requested
output field. The returned value is a object with `summary_id`, `threshold`, `matched_count`, `matched_invoice_ids`.

### Example Request

```text
Use the supplied match_threshold to build an invoice reconciliation summary.
Return the result in reconciliation_summary.
```
