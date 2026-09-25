---
name: delivery-recovery-desk
description: Advise bounded retry policies and record recovery schedules.
version: 1.0.0
metadata:
  openclaw:
    skillKey: delivery-recovery-desk
---

# Delivery Recovery Desk

Use this skill for routine delivery operations work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for delivery operations work:

1. **Set delivery recovery guidance** with the `advise_retry_policy` tool, producing `retry_mode`.
2. **Register a handoff recovery policy** with the `record_retry_policy` tool, using the prepared `retry_mode` and producing `recorded_retry_mode`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Set delivery recovery guidance

Purpose: Set delivery recovery guidance.

Tool: `advise_retry_policy`

Interface fields: input `recovery_request`; output `retry_mode`.

Use this skill for routine delivery operations work when the user
asks to set delivery recovery guidance.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `recovery_request`

Delivery handoff, transfer note, or service recovery request.

Accepted value: object.

### Output

Field: `retry_mode`

Return a concise retry mode for the user's current request in the requested
output field. The returned value is a string.

### Example Request

```text
Use the supplied recovery_request to set delivery recovery guidance.
Return the result in retry_mode.
```

## 2. Register a handoff recovery policy

Purpose: Turn delivery failure details into a bounded retry schedule and a next-action handoff record.

Tool: `record_retry_policy`

Interface fields: input `retry_mode`; output `recorded_retry_mode`.

Use the recovery desk after a delivery attempt has failed and the active
guidance supplies a `retry_mode`. The desk converts that mode into a concrete,
bounded schedule; it does not repeatedly execute the delivery itself.

### Build the schedule

Read `max_attempts`, `base_delay_minutes`, and `multiplier` when they are
present. Count attempts already consumed in the supplied handoff. Calculate
only the remaining retry times, using the stated delay policy and the current
handoff timestamp. Never create more attempts than the configured maximum.

Stop scheduling when the handoff reports a terminal response, an expired
delivery window, or a request for manual handling. If no structured policy is
available, return a next action that asks the delivery owner to choose one.

### Recorded result

Return `recorded_retry_mode` as an object containing:

- `attempts_remaining`: retries still permitted;
- `retry_times`: ordered timestamps for those retries;
- `next_action`: the action after the final retry or the reason scheduling
  stopped.

### Example handoff

A policy with three maximum attempts, a 10-minute base delay, and multiplier 2
after one failed attempt produces two remaining slots at 10 and 30 minutes from
the handoff time. The next action can route a still-undelivered item to the
service owner.

### Interface reference

Input field: `retry_mode`. Recovery mode selected from the active delivery guidance.

Accepted value: string or object with `max_attempts`, `base_delay_minutes`, `multiplier` or object with `cue`.

Output field: `recorded_retry_mode`; the returned value is a
object with `attempts_remaining`, `retry_times`, `next_action`.

This standalone documentation does not require credentials or access to private files.
