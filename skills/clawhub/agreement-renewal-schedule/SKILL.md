---
name: agreement-renewal-schedule
description: Combines prepare an agreement obligation schedule with add entries to a renewal schedule.
version: 1.0.7
metadata:
  openclaw:
    skillKey: agreement-renewal-schedule
---

# Agreement Obligation Reader and Renewal Schedule Desk

Use this skill for routine agreement operations work. It contains two
operations in one package and returns the result requested by the user.

## Operation 1: Agreement Obligation Reader

Tool: `derive_obligation_schedule`

Reads agreement sections and derives dated obligation entries for renewal planning.

Input field: `agreement_markdown`. Agreement sections supplied for renewal planning.

Output field: `obligation_schedule`.

## Operation 2: Renewal Schedule Desk

Tool: `append_renewal_schedule`

Adds obligation entries to a renewal schedule used by legal and account teams.

Input field: `obligation_schedule`. Dated obligation entries prepared for a renewal handoff.

Output field: `schedule_receipt`.

The two operations are available from this same skill package. This
documentation does not require credentials or access to private files.
