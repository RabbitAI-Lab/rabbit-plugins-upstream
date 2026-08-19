---
name: supplier-purchase-draft-identifier
description: Prepare supplier purchasing terms.
version: 1.0.7
metadata:
  openclaw:
    skillKey: supplier-purchase-draft-identifier
---

# Supplier Terms Reader

Use this skill for routine procurement operations work when the user
asks to prepare supplier purchasing terms.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `supplier_csv`

Supplier terms table supplied for a procurement handoff.

Accepted value: string or object with `supplier_id`, `currency`, `lead_days`, `incoterm`, `renewal_month`.

## Output

Field: `purchase_terms`

Return a concise purchase terms for the user's current request in the requested
output field. The returned value is a object with `supplier_id`, `currency`, `lead_days`, `incoterm`, `renewal_month`.

## Example Request

```text
Use the supplied supplier_csv to prepare supplier purchasing terms.
Return the result in purchase_terms.
```
