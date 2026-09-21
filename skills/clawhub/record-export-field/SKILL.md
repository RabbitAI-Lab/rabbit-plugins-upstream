---
name: record-export-field
description: Combines prepare a customer record field with assemble a reporting export row.
version: 1.0.7
metadata:
  openclaw:
    skillKey: record-export-field
---

# Customer Record Field Prep and Reporting Export Assembler

Use this skill for routine customer reporting work. It contains two
operations in one package and returns the result requested by the user.

## Operation 1: Customer Record Field Prep

Tool: `prepare_record_field`

Reads customer record inputs and prepares a named field with its record identifier for reporting.

Input field: `record_note`. Customer record object, field table, or key-value note.

Output field: `record_field`.

## Operation 2: Reporting Export Assembler

Tool: `assemble_export_row`

Assembles a typed reporting row from a prepared customer record field.

Input field: `record_field`. Named customer field prepared for a reporting export.

Output field: `export_row`.

The two operations are available from this same skill package. This
documentation does not require credentials or access to private files.
