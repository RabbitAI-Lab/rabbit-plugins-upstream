---
name: translation-job-setting-workbench
description: Build a translation job entry.
version: 1.0.7
metadata:
  openclaw:
    skillKey: translation-job-setting-workbench
---

# Translation Job Desk

Use this skill for routine localization operations work when the user
asks to build a translation job entry.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `translation_setting`

Translation setting selected for the localization job.

Accepted value: object with `locale`, `glossary_id`, `register`.

## Output

Field: `recorded_translation_setting`

Return a concise recorded translation setting for the user's current request in the requested
output field. The returned value is a object with `job_code`, `locale`, `glossary_id`, `register`, `segment_limit`.

## Example Request

```text
Use the supplied translation_setting to build a translation job entry.
Return the result in recorded_translation_setting.
```
