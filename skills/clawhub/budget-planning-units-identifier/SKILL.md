---
name: budget-planning-units-identifier
description: Forecast a scenario amount.
version: 1.0.7
metadata:
  openclaw:
    skillKey: budget-planning-units-identifier
---

# Campaign Budget Forecaster

Use this skill for routine campaign planning work when the user
asks to forecast a scenario amount.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `planning_note`

Campaign planning note or scenario description.

Accepted value: object with `currency`, `major_units`, `minor_units`.

## Output

Field: `amount`

Return a concise amount for the user's current request in the requested
output field. The returned value is a object with `currency`, `minor_units`.

## Example Request

```text
Use the supplied planning_note to forecast a scenario amount.
Return the result in amount.
```
