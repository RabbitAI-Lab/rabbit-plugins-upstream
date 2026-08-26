---
name: delivery-recovery-guidance-workbench
description: Turn delivery failure details into a bounded retry schedule and a next-action handoff record.
version: 1.0.7
metadata:
  openclaw:
    skillKey: delivery-recovery-guidance-workbench
---

# Handoff Recovery Desk

Use the recovery desk after a delivery attempt has failed and the active
guidance supplies a `retry_mode`. The desk converts that mode into a concrete,
bounded schedule; it does not repeatedly execute the delivery itself.

## Build the schedule

Read `max_attempts`, `base_delay_minutes`, and `multiplier` when they are
present. Count attempts already consumed in the supplied handoff. Calculate
only the remaining retry times, using the stated delay policy and the current
handoff timestamp. Never create more attempts than the configured maximum.

Stop scheduling when the handoff reports a terminal response, an expired
delivery window, or a request for manual handling. If no structured policy is
available, return a next action that asks the delivery owner to choose one.

## Recorded result

Return `recorded_retry_mode` as an object containing:

- `attempts_remaining`: retries still permitted;
- `retry_times`: ordered timestamps for those retries;
- `next_action`: the action after the final retry or the reason scheduling
  stopped.

## Example handoff

A policy with three maximum attempts, a 10-minute base delay, and multiplier 2
after one failed attempt produces two remaining slots at 10 and 30 minutes from
the handoff time. The next action can route a still-undelivered item to the
service owner.

## Interface reference

Input field: `retry_mode`. Recovery mode selected from the active delivery guidance.

Accepted value: string or object with `max_attempts`, `base_delay_minutes`, `multiplier` or object with `cue`.

Output field: `recorded_retry_mode`; the returned value is a
object with `attempts_remaining`, `retry_times`, `next_action`.

This standalone documentation does not require credentials or access to private files.
