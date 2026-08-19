---
name: record-export-field-identifier
description: Prepare a customer record field.
version: 1.0.7
metadata:
  openclaw:
    skillKey: record-export-field-identifier
---

# Customer Record Field Prep

Use this skill for routine customer reporting work when the user
asks to prepare a customer record field.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `record_note`

Customer record object, field table, or key-value note.

Accepted value: string or object with `record_id`, `field_name`, `field_value`.

## Output

Field: `record_field`

Return a concise record field for the user's current request in the requested
output field. The returned value is a object with `record_id`, `field_name`, `field_value`.

## Example Request

```text
Use the supplied record_note to prepare a customer record field.
Return the result in record_field.
```
