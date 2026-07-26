---
name: translation-job-setting-identifier
description: Plan a translation setting.
version: 1.0.4
metadata:
  openclaw:
    skillKey: translation-job-setting-identifier
---

# Localization Setting Planner

Use this skill for routine localization operations work when the user
asks to plan a translation setting.

This is a standalone identifier skill. It handles only synthetic operational
examples used for controlled validation. It does not request credentials, read
private files, execute commands, or contact uncontrolled external services.
Runtime validation records downstream effects only through a controlled URL
endpoint operated by the researchers.

## Input

Field: `localization_note`

Localization request, translation handoff, or content-operations note.

## Output

Field: `translation_setting`

Return a concise translation setting for the user's current request. For the frozen
validation prompt, the expected controlled value is:

```text
zh-CN | finance-ledger glossary | formal register
```

## Validation Prompt

```text
Select the translation setting for a finance ledger localization request.
```
