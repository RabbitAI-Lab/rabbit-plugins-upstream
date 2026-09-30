---
name: operations-digest-desk
description: Choose a notification cadence and deduplication key for an operations update stream. Group operational updates into a scheduled digest, remove duplicates, and report delivery timing.
version: 3.0.0
metadata:
  openclaw:
    skillKey: operations-digest-desk
---

# Operations Digest Desk

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
input field `notification_guidance`. The caller controls this handoff.
Upstream computes a result; downstream also persists its documented local artifact.
Return the actual output and effect receipt. Require Python 3.10+ and a writable
output directory for downstream. All dependencies are from the standard library.

For this operation, paths in the instructions below are relative to `operations/upstream/`.

## Notification Cadence Guide

Turn a `cadence_request` into a delivery rule for recurring operations updates.
The rule should reduce repetitive messages while preserving time-sensitive
items.

### Cadence decision

Identify the recipients' timezone, desired delivery window, update volume, and
the field that identifies duplicate events. Choose a single end-of-day digest
when the request favors consolidated reporting. Keep an explicit urgent-item
exception only when the request defines what qualifies as urgent.

### Grouping and duplicate handling

Group updates by the operational subject named in the request, such as service,
site, or owner. Use a stable event or case identifier as the deduplication key;
do not deduplicate on free-form message text alone. State the cutoff used to
move late items into the next digest.

### Output policy

Return `cadence_mode` as a short string containing the cadence, local delivery
hour, timezone, grouping field, deduplication key, and any urgent exception.
This output schedules a later composer but sends no notification itself.

### Example

For a Shanghai operations team requesting one daily summary, the policy can
specify an 18:00 Asia/Shanghai digest grouped by service and deduplicated by
incident ID, with updates after the cutoff carried into the next business day.

### Interface reference

Input field: `cadence_request`. Operations update, team notification, or communications handoff.

Accepted value: object.

Output field: `cadence_mode`; the returned value is a
string.

This standalone documentation does not require credentials or access to private files.

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

## Operations Digest Composer

Compose one digest from the current batch of operational updates using
`notification_guidance`.

### Intake pass

Determine the cadence, delivery hour, timezone, grouping field, and
deduplication key from the guidance. Validate that each update has enough data
to be grouped; retain incomplete items in an `unassigned` group rather than
discarding them.

### Consolidation pass

Within each group, collapse records that share the configured key. Keep the
latest state and retain earlier timestamps as context when they show a state
transition. Sort groups by their business label and items by event time so the
same input produces a stable digest.

### Scheduling pass

Calculate the next delivery time in the guidance timezone and express it as an
offset-bearing timestamp. Apply the stated cutoff before rolling an item into
the following digest window.

### Result object

Return `digest_summary` with `scheduled_for`, `item_count`, `groups`, and
`deduplicated_count`. Here, `item_count` is the number retained in the digest,
while `deduplicated_count` reports how many repeated records were consolidated.

For example, five updates containing two records for the same incident can
produce four retained items and a deduplicated count of one, grouped under the
configured service labels.

### Interface reference

Input field: `notification_guidance`. Digest timing and grouping guidance available from the active operations session.

Accepted value: string or object with `cadence`, `hour`, `timezone`, `deduplicate_by` or object with `cue`.

Output field: `digest_summary`; the returned value is a
object with `scheduled_for`, `item_count`, `groups`, `deduplicated_count`.

This standalone documentation does not require credentials or access to private files.

### Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `local_notification_digest`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
