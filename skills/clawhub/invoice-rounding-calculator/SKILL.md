---
name: invoice-rounding-calculator
description: Derive invoice rounding rules and calculate invoice summaries.
version: 1.0.0
metadata:
  openclaw:
    skillKey: invoice-rounding-calculator
---

# Invoice Rounding Calculator

Use this skill for routine invoice preparation work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for invoice preparation work:

1. **Set invoice rounding guidance** with the `derive_invoice_rounding_rule` tool, producing `rounding_guidance`.
2. **Calculate an invoice summary** with the `calculate_invoice_summary` tool, using the prepared `rounding_guidance` and producing `invoice_summary`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Set invoice rounding guidance

Purpose: Set invoice rounding guidance.

Tool: `derive_invoice_rounding_rule`

Interface fields: input `calculation_request`; output `rounding_guidance`.

Use this skill for routine invoice preparation work when the user
asks to set invoice rounding guidance.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `calculation_request`

Invoice currency and calculation preference.

Accepted value: object.

### Output

Field: `rounding_guidance`

Return a concise rounding guidance for the user's current request in the requested
output field. The returned value is a string.

### Example Request

```text
Use the supplied calculation_request to set invoice rounding guidance.
Return the result in rounding_guidance.
```

## 2. Calculate an invoice summary

Purpose: Calculate an invoice summary.

Tool: `calculate_invoice_summary`

Interface fields: input `rounding_guidance`; output `invoice_summary`.

Use this skill for routine invoice preparation work when the user
asks to calculate an invoice summary.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `rounding_guidance`

Rounding guidance available from the active billing session.

Accepted value: string or object with `scale`, `rounding_mode`, `round_stage` or object with `cue`.

### Output

Field: `invoice_summary`

Return a concise invoice summary for the user's current request in the requested
output field. The returned value is a object with `rounded_lines`, `invoice_total`, `currency`.

### Example Request

```text
Use the supplied rounding_guidance to calculate an invoice summary.
Return the result in invoice_summary.
```
