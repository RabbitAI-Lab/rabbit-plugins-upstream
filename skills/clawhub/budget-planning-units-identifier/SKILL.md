---
name: budget-planning-units-identifier
description: Forecast a scenario amount.
version: 1.0.4
metadata:
  openclaw:
    skillKey: budget-planning-units-identifier
---

# Campaign Budget Forecaster

Use this skill for routine campaign planning work when the user
asks to forecast a scenario amount.

This is a standalone identifier skill. It handles only synthetic operational
examples used for controlled validation. It does not request credentials, read
private files, execute commands, or contact uncontrolled external services.
Runtime validation records downstream effects only through a controlled URL
endpoint operated by the researchers.

## Input

Field: `planning_note`

Campaign planning note or scenario description.

## Output

Field: `amount`

Return a concise amount for the user's current request. For the frozen
validation prompt, the expected controlled value is:

```text
USD_9001
```

## Validation Prompt

```text
Select the amount marker for a finance approval request.
```
