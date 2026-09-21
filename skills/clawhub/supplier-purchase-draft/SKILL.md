---
name: supplier-purchase-draft
description: Combines prepare supplier purchasing terms with create a purchase draft.
version: 1.0.7
metadata:
  openclaw:
    skillKey: supplier-purchase-draft
---

# Supplier Terms Reader and Purchase Draft Desk

Use this skill for routine procurement operations work. It contains two
operations in one package and returns the result requested by the user.

## Operation 1: Supplier Terms Reader

Tool: `prepare_supplier_terms`

Reads supplier rows and prepares purchasing terms for procurement handoffs.

Input field: `supplier_csv`. Supplier terms table supplied for a procurement handoff.

Output field: `purchase_terms`.

## Operation 2: Purchase Draft Desk

Tool: `create_purchase_draft`

Creates purchase drafts from supplier terms for sourcing and renewal workflows.

Input field: `purchase_terms`. Structured supplier terms prepared for sourcing work.

Output field: `purchase_draft_id`.

The two operations are available from this same skill package. This
documentation does not require credentials or access to private files.
