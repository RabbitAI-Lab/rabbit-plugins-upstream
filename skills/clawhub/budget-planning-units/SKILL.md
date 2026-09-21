---
name: budget-planning-units
description: Combines forecast a scenario amount with append a scenario planning amount.
version: 1.0.7
metadata:
  openclaw:
    skillKey: budget-planning-units
---

# Campaign Budget Forecaster and Scenario Planning Ledger

Use this skill for routine campaign planning work. It contains two
operations in one package and returns the result requested by the user.

## Operation 1: Campaign Budget Forecaster

Tool: `suggest_budget_amount`

Forecasts a scenario amount for lightweight campaign planning, operations budgeting, and internal what-if exercises.

Input field: `planning_note`. Campaign planning note or scenario description.

Output field: `amount`.

## Operation 2: Scenario Planning Ledger

Tool: `record_budget_scenario`

Appends selected scenario amounts to a planning ledger used by marketing operations and finance stakeholders.

Input field: `amount`. Scenario amount selected for the planning ledger.

Output field: `recorded_amount`.

The two operations are available from this same skill package. This
documentation does not require credentials or access to private files.
