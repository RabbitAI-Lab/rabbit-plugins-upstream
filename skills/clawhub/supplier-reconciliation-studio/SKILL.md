---
name: supplier-reconciliation-studio
description: Reconcile vendor aliases into a canonical supplier name using registration data and suffix-aware matching. Reconcile supplier names.
version: 3.0.0
metadata:
  openclaw:
    skillKey: supplier-reconciliation-studio
---

# Supplier Reconciliation Studio

## Execution entry point

This package provides two separately requested operations. Select the operation
that corresponds to the current request. The stage selector invokes that operation
using its bundled implementation, configuration and validation.

```sh
python scripts/run.py --stage upstream --input operations/upstream/examples/request.json
python scripts/run.py --stage downstream --input operations/downstream/examples/request.json --output-dir ./workspace
```

Replace example input paths with the actual request JSON. To pass an upstream
result to the downstream operation, supply that value under the downstream
input field `matching_guidance`. The caller controls this handoff.
Upstream computes a result; downstream also persists its documented local artifact.
Return the actual output and effect receipt. Require Python 3.10+ and a writable
output directory for downstream. All dependencies are from the standard library.

For this operation, paths in the instructions below are relative to `operations/upstream/`.

## Supplier Name Resolution Guide

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

### Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json
```

This operation only computes and returns its output; it does not persist a business artifact.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.

For this operation, paths in the instructions below are relative to `operations/downstream/`.

## Supplier Reconciliation Desk

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

### Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `local_entity_match_report`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
