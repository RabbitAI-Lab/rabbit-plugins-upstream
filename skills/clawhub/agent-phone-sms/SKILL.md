---
name: agent-phone-sms
description: Give your AI agent its own real US phone number - inbound and outbound SMS, and voice calls with transcripts, in seven languages. One call provisions it on the same identity as the agent's inbox and vault. Use when an agent needs to text, call, or be reached on a number of its own.
homepage: https://useanima.sh
docs: https://docs.useanima.sh
metadata: {"api_base": "https://api.useanima.sh"}
---

# Agent Phone Number & SMS

An agent that emails well still stalls the first time someone asks "what's your
number?" — or a driver needs to reach it, or a customer would simply rather
talk.

An Anima identity can hold a real US number. It sends and receives SMS, places
and answers calls, and the transcript comes back as data.

## Provision a number

```bash
anima phone provision --agent <agent-id> --country US
```

Optional: `--area-code` for a preference, `--capabilities sms,mms,voice` to
narrow what the number does.

```bash
anima phone search --country US --area-code 415   # see what's available first
anima phone list --agent <agent-id>
anima phone release --agent <agent-id>            # give it back
```

Phone is a **paid plan**. If the command is refused, the agent asks its owner
rather than retrying:

```bash
anima request phone --agent <agent-id> --reason "needs to text delivery updates"
```

## Text

```bash
anima phone send-sms --agent <agent-id> --to +15551234567 --body "On my way."
```

Inbound SMS arrives on the same number and can be delivered to your endpoint:

```bash
anima webhook create --url https://example.com/hook --events sms.received
```

## Call, and keep the transcript

```bash
anima voice place --agent <agent-id> --to +15551234567
anima voice transcript <call-id>
```

`anima voice` also gives you `calls`, `summary`, `score` and semantic `search`
across transcripts. Outbound calling is gated server-side on TCPA consent, plan
caps and voice spend — the refusal is the product working, not a bug to retry
around.
`anima phone voices` lists the catalog — currently **90 voices across seven
languages** (de, en, es, fr, it, ja, nl).

## What these numbers are, precisely

They are **geographic US lines**. They send and receive SMS and voice, and they
are real numbers a person can call back.

They are **not** mobile lines, so do not promise they will clear a third-party
signup gate that checks line type. Some services accept them and some do not,
and that is the provider's decision, not something this product controls. We
retracted an earlier claim to the contrary; treating it as settled would set an
agent up to fail in front of a user.

## On the same identity

The number sits alongside the agent's own email inbox and an encrypted
credential vault — one identity, one API, one bill. See `agent-email-inbox` and
`agent-credential-vault`.

Phone, SMS and voice need a paid plan; the free tier covers email, vault and
MCP. `anima auth whoami` shows the current tier.
Docs: <https://docs.useanima.sh>
