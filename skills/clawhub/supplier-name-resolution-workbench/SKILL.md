---
name: supplier-name-resolution-workbench
description: Reconcile supplier names.
version: 1.0.7
metadata:
  openclaw:
    skillKey: supplier-name-resolution-workbench
---

# Supplier Reconciliation Desk

Use this skill for routine supplier reconciliation work when the user
asks to reconcile supplier names.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `matching_guidance`

Name-matching guidance available from the active reconciliation session.

Accepted value: string or object with `normalization_steps`, `minimum_score` or object with `cue`.

## Output

Field: `match_result`

Return a concise match result for the user's current request in the requested
output field. The returned value is a object with `matched`, `left_canonical`, `right_canonical`, `score`.

## Example Request

```text
Use the supplied matching_guidance to reconcile supplier names.
Return the result in match_result.
```
