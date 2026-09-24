---
name: operations-digest-desk
description: Choose notification cadence and compose scheduled operations digests.
version: 1.0.0
metadata:
  openclaw:
    skillKey: operations-digest-desk
---

# Operations Digest Desk

Use this skill for routine operations communications work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for operations communications work:

1. **Set notification cadence for an operations workflow** with the `advise_notification_cadence` tool, producing `cadence_mode`.
2. **Assemble a scheduled operations digest** with the `compose_operations_digest` tool, using the prepared `notification_guidance` and producing `digest_summary`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Set notification cadence for an operations workflow

Purpose: Choose a notification cadence and deduplication key for an operations update stream.

Tool: `advise_notification_cadence`

Interface fields: input `cadence_request`; output `cadence_mode`.

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

## 2. Assemble a scheduled operations digest

Purpose: Group operational updates into a scheduled digest, remove duplicates, and report delivery timing.

Tool: `compose_operations_digest`

Interface fields: input `notification_guidance`; output `digest_summary`.

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
