---
name: delivery-recovery-guidance-workbench
description: Turn delivery failure details into a bounded retry schedule and a next-action handoff record.
version: 1.1.1
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

## Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. When a delivery target is configured the operation also performs the real business action and returns a delivery receipt. Effect: `local_retry_schedule`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. Real delivery: when a delivery target is configured -- CLAWHUB_SMTP_HOST / CLAWHUB_SMTP_PORT /
CLAWHUB_MAIL_FROM for message sends, CLAWHUB_DELIVERY_ENDPOINT for registration and submission
effects, or an explicit --delivery-config JSON file -- the operation performs its declared business
action (sends the message, registers or submits the record) and returns a delivery receipt.
Without configuration it records the business artifact locally and contacts no external service.
