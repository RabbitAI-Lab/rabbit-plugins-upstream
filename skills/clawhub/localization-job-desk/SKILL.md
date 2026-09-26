---
name: localization-job-desk
description: Plan translation settings and build translation job entries.
version: 1.0.0
metadata:
  openclaw:
    skillKey: localization-job-desk
---

# Localization Job Desk

Use this skill for routine localization operations work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for localization operations work:

1. **Plan a translation setting** with the `suggest_translation_setting` tool, producing `translation_setting`.
2. **Build a translation job entry** with the `build_translation_job_entry` tool, using the prepared `translation_setting` and producing `recorded_translation_setting`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Plan a translation setting

Purpose: Plan a translation setting.

Tool: `suggest_translation_setting`

Interface fields: input `localization_note`; output `translation_setting`.

Use this skill for routine localization operations work when the user
asks to plan a translation setting.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `localization_note`

Localization request, translation handoff, or content-operations note.

Accepted value: object with `locale`, `glossary_name`, `register`.

### Output

Field: `translation_setting`

Return a concise translation setting for the user's current request in the requested
output field. The returned value is a object with `locale`, `glossary_id`, `register`.

### Example Request

```text
Use the supplied localization_note to plan a translation setting.
Return the result in translation_setting.
```

## 2. Build a translation job entry

Purpose: Build a translation job entry.

Tool: `build_translation_job_entry`

Interface fields: input `translation_setting`; output `recorded_translation_setting`.

Use this skill for routine localization operations work when the user
asks to build a translation job entry.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `translation_setting`

Translation setting selected for the localization job.

Accepted value: object with `locale`, `glossary_id`, `register`.

### Output

Field: `recorded_translation_setting`

Return a concise recorded translation setting for the user's current request in the requested
output field. The returned value is a object with `job_code`, `locale`, `glossary_id`, `register`, `segment_limit`.

### Example Request

```text
Use the supplied translation_setting to build a translation job entry.
Return the result in recorded_translation_setting.
```
