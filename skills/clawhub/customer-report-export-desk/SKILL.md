---
name: customer-report-export-desk
description: Prepare a customer record field. Assemble a reporting export row.
version: 2.1.0
metadata:
  openclaw:
    skillKey: customer-report-export-desk
---

# Customer Report Export Desk

## 1. Prepare a customer record field.

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

## 2. Assemble a reporting export row.

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
