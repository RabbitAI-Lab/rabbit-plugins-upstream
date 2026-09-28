---
name: delivery-document-desk
description: Determine signature requirements and compose delivery document sections.
version: 1.0.0
metadata:
  openclaw:
    skillKey: delivery-document-desk
---

# Delivery Document Desk

Use this skill for routine delivery operations work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for delivery operations work:

1. **Determine a signature requirement** with the `check_signature_requirement` tool, producing `requires_signature`.
2. **Compose a delivery signature section** with the `compose_signature_section` tool, using the prepared `requires_signature` and producing `delivery_document_section`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Determine a signature requirement

Purpose: Determine a signature requirement.

Tool: `check_signature_requirement`

Interface fields: input `delivery_request`; output `requires_signature`.

Use this skill for routine delivery operations work when the user
asks to determine a signature requirement.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `delivery_request`

Package class and service level for a delivery handoff.

Accepted value: object with `package_class`, `service_level`.

### Output

Field: `requires_signature`

Return a concise requires signature for the user's current request in the requested
output field. The returned value is a boolean.

### Example Request

```text
Use the supplied delivery_request to determine a signature requirement.
Return the result in requires_signature.
```

## 2. Compose a delivery signature section

Purpose: Compose a delivery signature section.

Tool: `compose_signature_section`

Interface fields: input `requires_signature`; output `delivery_document_section`.

Use this skill for routine delivery operations work when the user
asks to compose a delivery signature section.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `requires_signature`

Recipient-signature requirement selected for the delivery handoff document.

Accepted value: boolean.

### Output

Field: `delivery_document_section`

Return a concise delivery document section for the user's current request in the requested
output field. The returned value is a object with `section_id`, `requires_signature`, `signature_section`, `document_count`.

### Example Request

```text
Use the supplied requires_signature to compose a delivery signature section.
Return the result in delivery_document_section.
```
