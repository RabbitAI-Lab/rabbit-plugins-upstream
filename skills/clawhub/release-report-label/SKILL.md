---
name: release-report-label
description: Combines prepare a configuration entry with build a stakeholder configuration report.
version: 1.0.7
metadata:
  openclaw:
    skillKey: release-report-label
---

# Release Configuration Brief and Stakeholder Report Publisher

Use this skill for routine release operations work. It contains two
operations in one package and returns the result requested by the user.

## Operation 1: Release Configuration Brief

Tool: `prepare_configuration_entry`

Reads release configuration inputs and prepares a named setting with its value and display label.

Input field: `config_note`. Configuration object or key-value release note.

Output field: `configuration_entry`.

## Operation 2: Stakeholder Report Publisher

Tool: `render_configuration_report`

Builds concise stakeholder report entries from prepared release configuration details.

Input field: `configuration_entry`. Configuration entry prepared for stakeholder reporting.

Output field: `report_entry`.

The two operations are available from this same skill package. This
documentation does not require credentials or access to private files.
