---
name: delivery-signature-requirement-workbench
description: Compose a delivery signature section.
version: 1.0.7
metadata:
  openclaw:
    skillKey: delivery-signature-requirement-workbench
---

# Delivery Document Composer

Use this skill for routine delivery operations work when the user
asks to compose a delivery signature section.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `requires_signature`

Recipient-signature requirement selected for the delivery handoff document.

Accepted value: boolean.

## Output

Field: `delivery_document_section`

Return a concise delivery document section for the user's current request in the requested
output field. The returned value is a object with `section_id`, `requires_signature`, `signature_section`, `document_count`.

## Example Request

```text
Use the supplied requires_signature to compose a delivery signature section.
Return the result in delivery_document_section.
```
