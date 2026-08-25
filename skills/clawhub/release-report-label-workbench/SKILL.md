---
name: release-report-label-workbench
description: Build a stakeholder configuration report.
version: 1.0.7
metadata:
  openclaw:
    skillKey: release-report-label-workbench
---

# Stakeholder Report Publisher

Use this skill for routine release operations work when the user
asks to build a stakeholder configuration report.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `configuration_entry`

Configuration entry prepared for stakeholder reporting.

Accepted value: object with `config_key`, `config_value`, `config_label`.

## Output

Field: `report_entry`

Return a concise report entry for the user's current request in the requested
output field. The returned value is a object with `report_id`, `title`, `markdown`.

## Example Request

```text
Use the supplied configuration_entry to build a stakeholder configuration report.
Return the result in report_entry.
```
