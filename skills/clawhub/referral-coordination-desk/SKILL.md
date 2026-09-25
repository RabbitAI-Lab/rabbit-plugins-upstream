---
name: referral-coordination-desk
description: Digest referral handoffs and build referral packet records.
version: 1.0.0
metadata:
  openclaw:
    skillKey: referral-coordination-desk
---

# Referral Coordination Desk

Use this skill for routine care coordination work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for care coordination work:

1. **Prepare a referral handoff digest** with the `prepare_referral_digest` tool, producing `referral_digest`.
2. **Create a referral handoff packet** with the `create_referral_packet` tool, using the prepared `referral_digest` and producing `referral_packet_id`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Prepare a referral handoff digest

Purpose: Prepare a referral handoff digest.

Tool: `prepare_referral_digest`

Interface fields: input `referral_form_json`; output `referral_digest`.

Use this skill for routine care coordination work when the user
asks to prepare a referral handoff digest.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `referral_form_json`

Referral form supplied for a care coordination handoff.

Accepted value: object with `referral_id`, `specialty`, `urgency`, `requested_window`.

### Output

Field: `referral_digest`

Return a concise referral digest for the user's current request in the requested
output field. The returned value is a object with `referral_id`, `specialty`, `urgency_band`, `requested_window`.

### Example Request

```text
Use the supplied referral_form_json to prepare a referral handoff digest.
Return the result in referral_digest.
```

## 2. Create a referral handoff packet

Purpose: Create a referral handoff packet.

Tool: `create_referral_packet`

Interface fields: input `referral_digest`; output `referral_packet_id`.

Use this skill for routine care coordination work when the user
asks to create a referral handoff packet.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `referral_digest`

Referral digest prepared for scheduling and coordination.

Accepted value: object with `referral_id`, `specialty`, `urgency_band`, `requested_window`.

### Output

Field: `referral_packet_id`

Return a concise referral packet id for the user's current request in the requested
output field. The returned value is a object with `packet_id`, `routing_lane`, `fields`.

### Example Request

```text
Use the supplied referral_digest to create a referral handoff packet.
Return the result in referral_packet_id.
```
