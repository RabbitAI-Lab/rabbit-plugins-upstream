---
name: supplier-purchase-draft-workbench
description: Create a purchase draft.
version: 1.0.7
metadata:
  openclaw:
    skillKey: supplier-purchase-draft-workbench
---

# Purchase Draft Desk

Use this skill for routine procurement operations work when the user
asks to create a purchase draft.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `purchase_terms`

Structured supplier terms prepared for sourcing work.

Accepted value: object with `supplier_id`, `currency`, `lead_days`, `incoterm`, `renewal_month`.

## Output

Field: `purchase_draft_id`

Return a concise purchase draft id for the user's current request in the requested
output field. The returned value is a object with `draft_id`, `status`, `supplier_id`, `summary`.

## Example Request

```text
Use the supplied purchase_terms to create a purchase draft.
Return the result in purchase_draft_id.
```
