---
name: notification-cadence-guidance-identifier
description: Choose a notification cadence and deduplication key for an operations update stream.
version: 1.1.0
metadata:
  openclaw:
    skillKey: notification-cadence-guidance-identifier
---

# Notification Cadence Guide

Turn a `cadence_request` into a delivery rule for recurring operations updates.
The rule should reduce repetitive messages while preserving time-sensitive
items.

## Cadence decision

Identify the recipients' timezone, desired delivery window, update volume, and
the field that identifies duplicate events. Choose a single end-of-day digest
when the request favors consolidated reporting. Keep an explicit urgent-item
exception only when the request defines what qualifies as urgent.

## Grouping and duplicate handling

Group updates by the operational subject named in the request, such as service,
site, or owner. Use a stable event or case identifier as the deduplication key;
do not deduplicate on free-form message text alone. State the cutoff used to
move late items into the next digest.

## Output policy

Return `cadence_mode` as a short string containing the cadence, local delivery
hour, timezone, grouping field, deduplication key, and any urgent exception.
This output schedules a later composer but sends no notification itself.

## Example

For a Shanghai operations team requesting one daily summary, the policy can
specify an 18:00 Asia/Shanghai digest grouped by service and deduplicated by
incident ID, with updates after the cutoff carried into the next business day.

## Interface reference

Input field: `cadence_request`. Operations update, team notification, or communications handoff.

Accepted value: object.

Output field: `cadence_mode`; the returned value is a
string.

This standalone documentation does not require credentials or access to private files.

## Bundled execution

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
