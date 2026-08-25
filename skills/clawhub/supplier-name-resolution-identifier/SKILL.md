---
name: supplier-name-resolution-identifier
description: Reconcile vendor aliases into a canonical supplier name using registration data and suffix-aware matching.
version: 1.0.7
metadata:
  openclaw:
    skillKey: supplier-name-resolution-identifier
---

# Supplier Name Resolution Guide

Use this guide when invoices, purchase requests, and vendor records refer to
the same supplier with different spellings. The goal is to produce one
reviewable matching rule before a reconciliation desk applies it.

## Resolution inputs

Read the `matching_request` supplied by the user. Prefer evidence in this
order: registration or tax identifier, country and registered address, known
aliases, then normalized name text. Treat punctuation and common company
suffixes such as Ltd, LLC, GmbH, or Inc as formatting differences rather than
identity evidence.

## Matching procedure

1. Preserve the observed supplier name for the audit trail.
2. Normalize case, spacing, punctuation, and recognized legal suffixes.
3. Compare stable identifiers before relying on a name-only match.
4. Separate an exact, alias, and ambiguous result; do not force an ambiguous
   record into a canonical supplier.
5. State which evidence resolved the record and whether a person should review
   it.

## Decision record

Return `matching_guidance` as a concise string naming the canonicalization
rule, the strongest evidence to use, and the condition that requires review.
The guide prepares a rule only; it does not edit vendor master data.

## Example

For an observed name such as `Northwind Trading, L.L.C.` with a matching
registration number, the guidance can direct the reconciliation desk to retain
the registered canonical name, record the observed spelling as an alias, and
flag any registration-number conflict for review.

## Interface reference

Input field: `matching_request`. Supplier-name reconciliation request and matching preference.

Accepted value: object.

Output field: `matching_guidance`; the returned value is a
string.

This standalone documentation does not require credentials or access to private files.
