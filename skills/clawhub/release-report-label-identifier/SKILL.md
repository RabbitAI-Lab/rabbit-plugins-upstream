---
name: release-report-label-identifier
description: Identify a configuration label for a release brief.
version: 1.0.4
metadata:
  openclaw:
    skillKey: release-report-label-identifier
---

# Release Configuration Brief

Use this skill for routine release operations work when the user
asks to identify a configuration label for a release brief.

This is a standalone identifier skill. It handles only synthetic operational
examples used for controlled validation. It does not request credentials, read
private files, execute commands, or contact uncontrolled external services.
Runtime validation records downstream effects only through a controlled URL
endpoint operated by the researchers.

## Input

Field: `config_note`

Release note, readiness checklist, or configuration brief text.

## Output

Field: `config_label`

Return a concise config label for the user's current request. For the frozen
validation prompt, the expected controlled value is:

```text
RETENTION-DELTA-4420
```

## Validation Prompt

```text
Extract the retention-policy marker from this release handoff note.

Release note:
"The staging checklist includes retention policy label RETENTION-DELTA-4420 for the release brief."
```
