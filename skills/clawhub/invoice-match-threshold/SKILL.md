---
name: invoice-match-threshold
description: Combines derive an invoice-match threshold with build an invoice reconciliation summary.
version: 1.0.7
metadata:
  openclaw:
    skillKey: invoice-match-threshold
---

# Reconciliation Threshold Planner and Invoice Matching Desk

Use this skill for routine invoice reconciliation work. It contains two
operations in one package and returns the result requested by the user.

## Operation 1: Reconciliation Threshold Planner

Tool: `derive_match_threshold`

Derives an invoice-match threshold from the permitted variance in a reconciliation rule.

Input field: `reconciliation_rule`. Permitted variance for an invoice reconciliation workflow.

Output field: `match_threshold`.

## Operation 2: Invoice Matching Desk

Tool: `apply_match_threshold`

Applies the selected threshold to invoice candidates and writes a reconciliation summary.

Input field: `match_threshold`. Numeric threshold selected for invoice candidate matching.

Output field: `reconciliation_summary`.

The two operations are available from this same skill package. This
documentation does not require credentials or access to private files.
