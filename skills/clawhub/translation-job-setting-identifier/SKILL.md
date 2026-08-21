---
name: translation-job-setting-identifier
description: Plan a translation setting.
version: 1.0.7
metadata:
  openclaw:
    skillKey: translation-job-setting-identifier
---

# Localization Setting Planner

Use this skill for routine localization operations work when the user
asks to plan a translation setting.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `localization_note`

Localization request, translation handoff, or content-operations note.

Accepted value: object with `locale`, `glossary_name`, `register`.

## Output

Field: `translation_setting`

Return a concise translation setting for the user's current request in the requested
output field. The returned value is a object with `locale`, `glossary_id`, `register`.

## Example Request

```text
Use the supplied localization_note to plan a translation setting.
Return the result in translation_setting.
```
