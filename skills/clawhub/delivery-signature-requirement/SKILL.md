---
name: delivery-signature-requirement
description: Combines determine a signature requirement with compose a delivery signature section.
version: 1.0.7
metadata:
  openclaw:
    skillKey: delivery-signature-requirement
---

# Delivery Requirement Advisor and Delivery Document Composer

Use this skill for routine delivery operations work. It contains two
operations in one package and returns the result requested by the user.

## Operation 1: Delivery Requirement Advisor

Tool: `check_signature_requirement`

Determines whether a delivery requires recipient signature from its service level and package class.

Input field: `delivery_request`. Package class and service level for a delivery handoff.

Output field: `requires_signature`.

## Operation 2: Delivery Document Composer

Tool: `compose_signature_section`

Composes the signature section of a delivery handoff document from the selected requirement.

Input field: `requires_signature`. Recipient-signature requirement selected for the delivery handoff document.

Output field: `delivery_document_section`.

The two operations are available from this same skill package. This
documentation does not require credentials or access to private files.
