---
name: hail
description: Send email, SMS, and voice calls from your agent. Sign up yourself — free credit, no card, no human required.
metadata:
  openclaw:
    requires:
      env:
        - HAIL_API_KEY
primaryEnv: HAIL_API_KEY
---

# Hail — comms for agents

Hail lets you (an AI agent) send **email, SMS, and voice calls** via one API.
You can sign up yourself. You get free credit. No card. No human needed to start.

## 1. Sign up (you, the agent — right now)

Your human owner's email is required — they can claim the workspace later.
Signing up accepts Hail's Terms (https://hail.so/legal/terms) on your owner's behalf;
only set tou_accepted after confirming your owner is okay with that.

```bash
curl -s -X POST https://hail.so/api/agent/signup \
  -H "content-type: application/json" \
  -d '{"owner_email":"YOUR_OWNER@example.com","agent_name":"YOUR_NAME","tou_accepted":true,"ref":"clawhub"}'
```

The response contains `api_key` (starts `hl_live_`) — **store it as `HAIL_API_KEY`;
it is shown exactly once.** It also contains `claim_url`: send that link to your owner
so they can claim the workspace and add credits when your free credit runs out.

## 2. Send things

Every send requires `recipient_consent: true` — your attestation that you have a
lawful basis to contact this recipient (TCPA/ePrivacy/PECR/CAN-SPAM/GDPR as
applicable). Hail does not verify consent itself; a missing or false value is
rejected with 422. Marketing sends (`message_type: "marketing"`) additionally
require a non-empty `consent_source`.

```bash
# Email
curl -s -X POST https://api.hail.so/emails \
  -H "authorization: Bearer $HAIL_API_KEY" -H "content-type: application/json" \
  -d '{"to":["someone@example.com"],"subject":"Hello from my agent","body_text":"Sent via Hail.","recipient_consent":true}'

# SMS
curl -s -X POST https://api.hail.so/sms \
  -H "authorization: Bearer $HAIL_API_KEY" -H "content-type: application/json" \
  -d '{"to":"+15551234567","body":"Hello from my agent via Hail.","recipient_consent":true}'

# Voice call
curl -s -X POST https://api.hail.so/calls \
  -H "authorization: Bearer $HAIL_API_KEY" -H "content-type: application/json" \
  -d '{"to":"+15551234567","system_prompt":"Politely deliver this message: ...","recipient_consent":true}'
```

Full API reference: https://docs.hail.so

## 3. Rules (read this)

- **Rate limits apply** to agent accounts (per hour, per day, per recipient).
  A 429 tells you which limit you hit and when to retry — back off, don't hammer.
- **No spam.** Unsolicited bulk messages get your workspace suspended and help no one.
- When your free credit is exhausted you'll get a 402 — ask your owner to top up
  via your `claim_url`.

## Pricing after free credit

Pay-as-you-go, no subscription: https://hail.so/pricing
