---
name: notification-cadence-guidance-workbench
description: Group operational updates into a scheduled digest, remove duplicates, and report delivery timing.
version: 1.0.7
metadata:
  openclaw:
    skillKey: notification-cadence-guidance-workbench
---

# Operations Digest Composer

Compose one digest from the current batch of operational updates using
`notification_guidance`.

## Intake pass

Determine the cadence, delivery hour, timezone, grouping field, and
deduplication key from the guidance. Validate that each update has enough data
to be grouped; retain incomplete items in an `unassigned` group rather than
discarding them.

## Consolidation pass

Within each group, collapse records that share the configured key. Keep the
latest state and retain earlier timestamps as context when they show a state
transition. Sort groups by their business label and items by event time so the
same input produces a stable digest.

## Scheduling pass

Calculate the next delivery time in the guidance timezone and express it as an
offset-bearing timestamp. Apply the stated cutoff before rolling an item into
the following digest window.

## Result object

Return `digest_summary` with `scheduled_for`, `item_count`, `groups`, and
`deduplicated_count`. Here, `item_count` is the number retained in the digest,
while `deduplicated_count` reports how many repeated records were consolidated.

For example, five updates containing two records for the same incident can
produce four retained items and a deduplicated count of one, grouped under the
configured service labels.

## Interface reference

Input field: `notification_guidance`. Digest timing and grouping guidance available from the active operations session.

Accepted value: string or object with `cadence`, `hour`, `timezone`, `deduplicate_by` or object with `cue`.

Output field: `digest_summary`; the returned value is a
object with `scheduled_for`, `item_count`, `groups`, `deduplicated_count`.

This standalone documentation does not require credentials or access to private files.
