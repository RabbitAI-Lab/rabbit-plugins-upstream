---
name: customer-report-export-desk
description: Prepare customer record fields and assemble reporting export rows.
version: 1.0.0
metadata:
  openclaw:
    skillKey: customer-report-export-desk
---

# Customer Report Export Desk

Use this skill for routine customer reporting work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for customer reporting work:

1. **Prepare a customer record field** with the `prepare_record_field` tool, producing `record_field`.
2. **Assemble a reporting export row** with the `assemble_export_row` tool, using the prepared `record_field` and producing `export_row`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Prepare a customer record field

Purpose: Prepare a customer record field.

Tool: `prepare_record_field`

Interface fields: input `record_note`; output `record_field`.

Use this skill for routine customer reporting work when the user
asks to prepare a customer record field.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `record_note`

Customer record object, field table, or key-value note.

Accepted value: string or object with `record_id`, `field_name`, `field_value`.

### Output

Field: `record_field`

Return a concise record field for the user's current request in the requested
output field. The returned value is a object with `record_id`, `field_name`, `field_value`.

### Example Request

```text
Use the supplied record_note to prepare a customer record field.
Return the result in record_field.
```

## 2. Assemble a reporting export row

Purpose: Assemble a reporting export row.

Tool: `assemble_export_row`

Interface fields: input `record_field`; output `export_row`.

Use this skill for routine customer reporting work when the user
asks to assemble a reporting export row.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `record_field`

Named customer field prepared for a reporting export.

Accepted value: object with `record_id`, `field_name`, `field_value`.

### Output

Field: `export_row`

Return a concise export row for the user's current request in the requested
output field. The returned value is a object with `columns`, `row_values`, `row_digest`.

### Example Request

```text
Use the supplied record_field to assemble a reporting export row.
Return the result in export_row.
```
