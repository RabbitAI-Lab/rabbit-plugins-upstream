---
name: referral-handoff-packet-workbench
description: Create a referral handoff packet.
version: 1.0.7
metadata:
  openclaw:
    skillKey: referral-handoff-packet-workbench
---

# Referral Packet Desk

Use this skill for routine care coordination work when the user
asks to create a referral handoff packet.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `referral_digest`

Referral digest prepared for scheduling and coordination.

Accepted value: object with `referral_id`, `specialty`, `urgency_band`, `requested_window`.

## Output

Field: `referral_packet_id`

Return a concise referral packet id for the user's current request in the requested
output field. The returned value is a object with `packet_id`, `routing_lane`, `fields`.

## Example Request

```text
Use the supplied referral_digest to create a referral handoff packet.
Return the result in referral_packet_id.
```
