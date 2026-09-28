---
name: supplier-reconciliation-studio
description: Derive supplier matching rules and reconcile supplier names.
version: 1.0.0
metadata:
  openclaw:
    skillKey: supplier-reconciliation-studio
---

# Supplier Reconciliation Studio

Use this skill for routine supplier reconciliation work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for supplier reconciliation work:

1. **Set supplier-name matching guidance** with the `derive_supplier_matching_rule` tool, producing `matching_guidance`.
2. **Reconcile supplier names** with the `reconcile_supplier_names` tool, using the prepared `matching_guidance` and producing `match_result`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Set supplier-name matching guidance

Purpose: Reconcile vendor aliases into a canonical supplier name using registration data and suffix-aware matching.

Tool: `derive_supplier_matching_rule`

Interface fields: input `matching_request`; output `matching_guidance`.

Use this guide when invoices, purchase requests, and vendor records refer to
the same supplier with different spellings. The goal is to produce one
reviewable matching rule before a reconciliation desk applies it.

### Resolution inputs

Read the `matching_request` supplied by the user. Prefer evidence in this
order: registration or tax identifier, country and registered address, known
aliases, then normalized name text. Treat punctuation and common company
suffixes such as Ltd, LLC, GmbH, or Inc as formatting differences rather than
identity evidence.

### Matching procedure

1. Preserve the observed supplier name for the audit trail.
2. Normalize case, spacing, punctuation, and recognized legal suffixes.
3. Compare stable identifiers before relying on a name-only match.
4. Separate an exact, alias, and ambiguous result; do not force an ambiguous
   record into a canonical supplier.
5. State which evidence resolved the record and whether a person should review
   it.

### Decision record

Return `matching_guidance` as a concise string naming the canonicalization
rule, the strongest evidence to use, and the condition that requires review.
The guide prepares a rule only; it does not edit vendor master data.

### Example

For an observed name such as `Northwind Trading, L.L.C.` with a matching
registration number, the guidance can direct the reconciliation desk to retain
the registered canonical name, record the observed spelling as an alias, and
flag any registration-number conflict for review.

### Interface reference

Input field: `matching_request`. Supplier-name reconciliation request and matching preference.

Accepted value: object.

Output field: `matching_guidance`; the returned value is a
string.

This standalone documentation does not require credentials or access to private files.

## 2. Reconcile supplier names

Purpose: Reconcile supplier names.

Tool: `reconcile_supplier_names`

Interface fields: input `matching_guidance`; output `match_result`.

Use this skill for routine supplier reconciliation work when the user
asks to reconcile supplier names.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `matching_guidance`

Name-matching guidance available from the active reconciliation session.

Accepted value: string or object with `normalization_steps`, `minimum_score` or object with `cue`.

### Output

Field: `match_result`

Return a concise match result for the user's current request in the requested
output field. The returned value is a object with `matched`, `left_canonical`, `right_canonical`, `score`.

### Example Request

```text
Use the supplied matching_guidance to reconcile supplier names.
Return the result in match_result.
```
