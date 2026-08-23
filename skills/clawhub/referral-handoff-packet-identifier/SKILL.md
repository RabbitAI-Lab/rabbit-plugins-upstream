---
name: referral-handoff-packet-identifier
description: Prepare a referral handoff digest.
version: 1.0.7
metadata:
  openclaw:
    skillKey: referral-handoff-packet-identifier
---

# Referral Handoff Reader

Use this skill for routine care coordination work when the user
asks to prepare a referral handoff digest.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `referral_form_json`

Referral form supplied for a care coordination handoff.

Accepted value: object with `referral_id`, `specialty`, `urgency`, `requested_window`.

## Output

Field: `referral_digest`

Return a concise referral digest for the user's current request in the requested
output field. The returned value is a object with `referral_id`, `specialty`, `urgency_band`, `requested_window`.

## Example Request

```text
Use the supplied referral_form_json to prepare a referral handoff digest.
Return the result in referral_digest.
```
