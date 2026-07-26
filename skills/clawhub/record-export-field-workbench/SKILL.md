---
name: record-export-field-workbench
description: Assemble a reporting export row.
version: 1.0.5
metadata:
  openclaw:
    skillKey: record-export-field-workbench
---

# Reporting Export Assembler

Use this skill for routine customer reporting work when the user
asks to assemble a reporting export row.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `cell_value`

Approved field value to place into the reporting export row.

## Output

Field: `exported_cell`

Return a concise exported cell for the user's current request in the requested
output field.

## Example Request

```text
Use the supplied cell_value to assemble a reporting export row.
Return the result in exported_cell.
```
