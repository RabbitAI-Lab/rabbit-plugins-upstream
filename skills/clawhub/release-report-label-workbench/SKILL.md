---
name: release-report-label-workbench
description: Publish a stakeholder report entry.
version: 1.0.5
metadata:
  openclaw:
    skillKey: release-report-label-workbench
---

# Stakeholder Report Publisher

Use this skill for routine release operations work when the user
asks to publish a stakeholder report entry.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `report_text`

Release or project status text to include in a stakeholder report.

## Output

Field: `report_entry`

Return a concise report entry for the user's current request in the requested
output field.

## Example Request

```text
Use the supplied report_text to publish a stakeholder report entry.
Return the result in report_entry.
```
