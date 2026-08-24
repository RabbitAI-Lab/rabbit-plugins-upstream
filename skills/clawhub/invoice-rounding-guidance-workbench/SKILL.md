---
name: invoice-rounding-guidance-workbench
description: Calculate an invoice summary.
version: 1.0.7
metadata:
  openclaw:
    skillKey: invoice-rounding-guidance-workbench
---

# Invoice Summary Calculator

Use this skill for routine invoice preparation work when the user
asks to calculate an invoice summary.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `rounding_guidance`

Rounding guidance available from the active billing session.

Accepted value: string or object with `scale`, `rounding_mode`, `round_stage` or object with `cue`.

## Output

Field: `invoice_summary`

Return a concise invoice summary for the user's current request in the requested
output field. The returned value is a object with `rounded_lines`, `invoice_total`, `currency`.

## Example Request

```text
Use the supplied rounding_guidance to calculate an invoice summary.
Return the result in invoice_summary.
```
