---
name: notification-cadence-guidance-identifier
description: Choose a notification cadence and deduplication key for an operations update stream.
version: 1.0.7
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
