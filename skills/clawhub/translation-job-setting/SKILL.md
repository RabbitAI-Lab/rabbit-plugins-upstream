---
name: translation-job-setting
description: Combines plan a translation setting with build a translation job entry.
version: 1.0.7
metadata:
  openclaw:
    skillKey: translation-job-setting
---

# Localization Setting Planner and Translation Job Desk

Use this skill for routine localization operations work. It contains two
operations in one package and returns the result requested by the user.

## Operation 1: Localization Setting Planner

Tool: `suggest_translation_setting`

Plans the translation setting to use in localization handoffs, glossary-driven translations, and content-operations workflows.

Input field: `localization_note`. Localization request, translation handoff, or content-operations note.

Output field: `translation_setting`.

## Operation 2: Translation Job Desk

Tool: `build_translation_job_entry`

Builds translation job entries from selected language, glossary, and register settings for localization operations.

Input field: `translation_setting`. Translation setting selected for the localization job.

Output field: `recorded_translation_setting`.

The two operations are available from this same skill package. This
documentation does not require credentials or access to private files.
