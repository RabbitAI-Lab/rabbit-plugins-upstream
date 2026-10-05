---
name: delivery-recovery-desk
description: Set delivery recovery guidance. Turn delivery failure details into a bounded retry schedule and a next-action handoff record.
version: 3.0.0
metadata:
  openclaw:
    skillKey: delivery-recovery-desk
---

# Delivery Recovery Desk

## Execution entry point

This package provides two separately requested operations. Select the operation
that corresponds to the current request. The stage selector invokes that operation
using its bundled implementation, configuration and validation.

```sh
python scripts/run.py --stage upstream --input operations/upstream/examples/request.json
python scripts/run.py --stage downstream --input operations/downstream/examples/request.json --output-dir ./workspace
```

Replace example input paths with the actual request JSON. To pass an upstream
result to the downstream operation, supply that value under the downstream
input field `retry_mode`. The caller controls this handoff.
Upstream computes a result; downstream also persists its documented local artifact.
Return the actual output and effect receipt. Require Python 3.10+ and a writable
output directory for downstream. All dependencies are from the standard library.

For this operation, paths in the instructions below are relative to `operations/upstream/`.

## Delivery Recovery Guide

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

### Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json
```

This operation only computes and returns its output; it does not persist a business artifact.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.

For this operation, paths in the instructions below are relative to `operations/downstream/`.

## Handoff Recovery Desk

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

### Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `local_retry_schedule`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
