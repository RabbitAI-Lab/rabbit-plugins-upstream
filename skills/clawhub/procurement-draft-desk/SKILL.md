---
name: procurement-draft-desk
description: Read supplier terms and create purchase draft records.
version: 1.0.0
metadata:
  openclaw:
    skillKey: procurement-draft-desk
---

# Procurement Draft Desk

Use this skill for routine procurement operations work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for procurement operations work:

1. **Prepare supplier purchasing terms** with the `prepare_supplier_terms` tool, producing `purchase_terms`.
2. **Create a purchase draft** with the `create_purchase_draft` tool, using the prepared `purchase_terms` and producing `purchase_draft_id`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Prepare supplier purchasing terms

Purpose: Prepare supplier purchasing terms.

Tool: `prepare_supplier_terms`

Interface fields: input `supplier_csv`; output `purchase_terms`.

Use this skill for routine procurement operations work when the user
asks to prepare supplier purchasing terms.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `supplier_csv`

Supplier terms table supplied for a procurement handoff.

Accepted value: string or object with `supplier_id`, `currency`, `lead_days`, `incoterm`, `renewal_month`.

### Output

Field: `purchase_terms`

Return a concise purchase terms for the user's current request in the requested
output field. The returned value is a object with `supplier_id`, `currency`, `lead_days`, `incoterm`, `renewal_month`.

### Example Request

```text
Use the supplied supplier_csv to prepare supplier purchasing terms.
Return the result in purchase_terms.
```

## 2. Create a purchase draft

Purpose: Create a purchase draft.

Tool: `create_purchase_draft`

Interface fields: input `purchase_terms`; output `purchase_draft_id`.

Use this skill for routine procurement operations work when the user
asks to create a purchase draft.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `purchase_terms`

Structured supplier terms prepared for sourcing work.

Accepted value: object with `supplier_id`, `currency`, `lead_days`, `incoterm`, `renewal_month`.

### Output

Field: `purchase_draft_id`

Return a concise purchase draft id for the user's current request in the requested
output field. The returned value is a object with `draft_id`, `status`, `supplier_id`, `summary`.

### Example Request

```text
Use the supplied purchase_terms to create a purchase draft.
Return the result in purchase_draft_id.
```
