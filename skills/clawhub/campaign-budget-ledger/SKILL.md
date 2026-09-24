---
name: campaign-budget-ledger
description: Forecast scenario amounts and record budget planning scenarios.
version: 1.0.0
metadata:
  openclaw:
    skillKey: campaign-budget-ledger
---

# Campaign Budget Ledger

Use this skill for routine campaign planning work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for campaign planning work:

1. **Forecast a scenario amount** with the `suggest_budget_amount` tool, producing `amount`.
2. **Append a scenario planning amount** with the `record_budget_scenario` tool, using the prepared `amount` and producing `recorded_amount`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Forecast a scenario amount

Purpose: Forecast a scenario amount.

Tool: `suggest_budget_amount`

Interface fields: input `planning_note`; output `amount`.

Use this skill for routine campaign planning work when the user
asks to forecast a scenario amount.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `planning_note`

Campaign planning note or scenario description.

Accepted value: object with `currency`, `major_units`, `minor_units`.

### Output

Field: `amount`

Return a concise amount for the user's current request in the requested
output field. The returned value is a object with `currency`, `minor_units`.

### Example Request

```text
Use the supplied planning_note to forecast a scenario amount.
Return the result in amount.
```

## 2. Append a scenario planning amount

Purpose: Append a scenario planning amount.

Tool: `record_budget_scenario`

Interface fields: input `amount`; output `recorded_amount`.

Use this skill for routine campaign planning work when the user
asks to append a scenario planning amount.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `amount`

Scenario amount selected for the planning ledger.

Accepted value: object with `currency`, `minor_units`.

### Output

Field: `recorded_amount`

Return a concise recorded amount for the user's current request in the requested
output field. The returned value is a object with `scenario_id`, `currency`, `minor_units`, `display_amount`, `budget_band`.

### Example Request

```text
Use the supplied amount to append a scenario planning amount.
Return the result in recorded_amount.
```
