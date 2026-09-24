---
name: agreement-renewal-desk
description: Derive obligation schedules and append renewal schedule records.
version: 1.0.0
metadata:
  openclaw:
    skillKey: agreement-renewal-desk
---

# Agreement Renewal Desk

Use this skill for routine agreement operations work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for agreement operations work:

1. **Prepare an agreement obligation schedule** with the `derive_obligation_schedule` tool, producing `obligation_schedule`.
2. **Add entries to a renewal schedule** with the `append_renewal_schedule` tool, using the prepared `obligation_schedule` and producing `schedule_receipt`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Prepare an agreement obligation schedule

Purpose: Prepare an agreement obligation schedule.

Tool: `derive_obligation_schedule`

Interface fields: input `agreement_markdown`; output `obligation_schedule`.

Use this skill for routine agreement operations work when the user
asks to prepare an agreement obligation schedule.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `agreement_markdown`

Agreement sections supplied for renewal planning.

Accepted value: string.

### Output

Field: `obligation_schedule`

Return a concise obligation schedule for the user's current request in the requested
output field. The returned value is a object with `agreement_id`, `obligations`.

### Example Request

```text
Use the supplied agreement_markdown to prepare an agreement obligation schedule.
Return the result in obligation_schedule.
```

## 2. Add entries to a renewal schedule

Purpose: Add entries to a renewal schedule.

Tool: `append_renewal_schedule`

Interface fields: input `obligation_schedule`; output `schedule_receipt`.

Use this skill for routine agreement operations work when the user
asks to add entries to a renewal schedule.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `obligation_schedule`

Dated obligation entries prepared for a renewal handoff.

Accepted value: object with `agreement_id`, `obligations`.

### Output

Field: `schedule_receipt`

Return a concise schedule receipt for the user's current request in the requested
output field. The returned value is a object with `schedule_id`, `rows`.

### Example Request

```text
Use the supplied obligation_schedule to add entries to a renewal schedule.
Return the result in schedule_receipt.
```
