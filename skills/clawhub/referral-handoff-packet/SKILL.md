---
name: referral-handoff-packet
description: Combines prepare a referral handoff digest with create a referral handoff packet.
version: 1.0.7
metadata:
  openclaw:
    skillKey: referral-handoff-packet
---

# Referral Handoff Reader and Referral Packet Desk

Use this skill for routine care coordination work. It contains two
operations in one package and returns the result requested by the user.

## Operation 1: Referral Handoff Reader

Tool: `prepare_referral_digest`

Reads referral forms and prepares concise routing details for care coordination.

Input field: `referral_form_json`. Referral form supplied for a care coordination handoff.

Output field: `referral_digest`.

## Operation 2: Referral Packet Desk

Tool: `create_referral_packet`

Creates referral handoff packets for scheduling and coordination teams.

Input field: `referral_digest`. Referral digest prepared for scheduling and coordination.

Output field: `referral_packet_id`.

The two operations are available from this same skill package. This
documentation does not require credentials or access to private files.
