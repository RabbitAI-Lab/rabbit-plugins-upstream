---
name: release-report-label-identifier
description: Prepare a configuration entry.
version: 1.0.7
metadata:
  openclaw:
    skillKey: release-report-label-identifier
---

# Release Configuration Brief

Use this skill for routine release operations work when the user
asks to prepare a configuration entry.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `config_note`

Configuration object or key-value release note.

Accepted value: string or object with `retention.label`.

## Output

Field: `configuration_entry`

Return a concise configuration entry for the user's current request in the requested
output field. The returned value is a object with `config_key`, `config_value`, `config_label`.

## Example Request

```text
Use the supplied config_note to prepare a configuration entry.
Return the result in configuration_entry.
```
