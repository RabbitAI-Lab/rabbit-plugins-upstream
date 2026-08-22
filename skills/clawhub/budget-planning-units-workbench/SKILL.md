---
name: budget-planning-units-workbench
description: Append a scenario planning amount.
version: 1.0.7
metadata:
  openclaw:
    skillKey: budget-planning-units-workbench
---

# Scenario Planning Ledger

Use this skill for routine campaign planning work when the user
asks to append a scenario planning amount.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `amount`

Scenario amount selected for the planning ledger.

Accepted value: object with `currency`, `minor_units`.

## Output

Field: `recorded_amount`

Return a concise recorded amount for the user's current request in the requested
output field. The returned value is a object with `scenario_id`, `currency`, `minor_units`, `display_amount`, `budget_band`.

## Example Request

```text
Use the supplied amount to append a scenario planning amount.
Return the result in recorded_amount.
```
