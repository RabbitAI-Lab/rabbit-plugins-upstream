---
name: release-configuration-report-desk
description: Build release configuration entries and publish stakeholder reports.
version: 1.0.0
metadata:
  openclaw:
    skillKey: release-configuration-report-desk
---

# Release Configuration Report Desk

Use this skill for routine release operations work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for release operations work:

1. **Prepare a configuration entry** with the `prepare_configuration_entry` tool, producing `configuration_entry`.
2. **Build a stakeholder configuration report** with the `render_configuration_report` tool, using the prepared `configuration_entry` and producing `report_entry`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Prepare a configuration entry

Purpose: Prepare a configuration entry.

Tool: `prepare_configuration_entry`

Interface fields: input `config_note`; output `configuration_entry`.

Use this skill for routine release operations work when the user
asks to prepare a configuration entry.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `config_note`

Configuration object or key-value release note.

Accepted value: string or object with `retention.label`.

### Output

Field: `configuration_entry`

Return a concise configuration entry for the user's current request in the requested
output field. The returned value is a object with `config_key`, `config_value`, `config_label`.

### Example Request

```text
Use the supplied config_note to prepare a configuration entry.
Return the result in configuration_entry.
```

## 2. Build a stakeholder configuration report

Purpose: Build a stakeholder configuration report.

Tool: `render_configuration_report`

Interface fields: input `configuration_entry`; output `report_entry`.

Use this skill for routine release operations work when the user
asks to build a stakeholder configuration report.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `configuration_entry`

Configuration entry prepared for stakeholder reporting.

Accepted value: object with `config_key`, `config_value`, `config_label`.

### Output

Field: `report_entry`

Return a concise report entry for the user's current request in the requested
output field. The returned value is a object with `report_id`, `title`, `markdown`.

### Example Request

```text
Use the supplied configuration_entry to build a stakeholder configuration report.
Return the result in report_entry.
```
