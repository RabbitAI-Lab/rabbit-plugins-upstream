---
name: agent-email-inbox
description: Give your AI agent its own real email inbox - an address it owns, that sends and receives, with replies threading back to the agent instead of a human's mailbox. Provisioned in about a minute, free tier, no card. Use when an agent needs to send mail as itself, read what comes back, or act on inbound email.
homepage: https://useanima.sh
docs: https://docs.useanima.sh
metadata: {"api_base": "https://api.useanima.sh"}
---

# Agent Email Inbox

Most agents send mail from a human's account, or from a shared `noreply@`.
Both break the moment a reply arrives: it lands in someone's inbox behind a
filter rule, and nothing can answer it.

An Anima identity owns a real address. Mail addressed to the agent arrives at
the agent.

## Get an inbox

```bash
npm install -g @anima-labs/cli
anima init
```

`init` provisions an org, an agent and an inbox. Full send capability unlocks
after the **owner** confirms a 6-digit code Anima emails them:

```bash
anima verify <code>
```

That gate is deliberate. An agent can create an identity on its own; it cannot
start mailing strangers until a person says so. If a verification URL is
printed, show it in full — never shorten it.

## Send

```bash
anima email send --agent <agent-id> \
  --to someone@example.com \
  --subject "Following up on the order" \
  --body "Plain text body."
```

`--to` repeats for multiple recipients. `--cc`, `--bcc` and `--html` are
available. Rehearsing, or running in CI? Add `--test` and the server uses
fixtures — nothing leaves the building.

```bash
anima email send --test --agent <agent-id> --to you@example.com \
  --subject "Dry run" --body "Nothing was sent."
```

## Read what comes back

```bash
anima email list --agent <agent-id>            # --limit, --label, --cursor
anima email get <message-id>
anima email search --semantic "invoice dispute"
```

Replies thread to the agent that sent them. That is what makes "which agent
did this, and what happened next?" answerable months later.

## Reply, and thread properly

Threading is an API field rather than a CLI flag:

```bash
curl -X POST https://api.useanima.sh/v1/email/send \
  -H "Authorization: Bearer $ANIMA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"agentId":"<agent-id>","to":["someone@example.com"],
       "subject":"Re: Following up","body":"...",
       "inReplyTo":"<message-id>"}'
```

`inReplyTo` accepts either an RFC `Message-ID` or an Anima message id, and the
API emits `In-Reply-To` plus the full `References` chain, so Gmail and Outlook
thread it the way a human's reply threads. An id that resolves to nothing is
refused rather than quietly sent unthreaded.

A reply is also treated as a conversation rather than a campaign: it carries
`Auto-Submitted: auto-replied` (RFC 3834, so vacation responders stay quiet and
agent-to-agent loops still break) and **no** `List-Unsubscribe`. A one-click
unsubscribe control beside a 1:1 answer makes a personal message read as
marketing.

## React to inbound

```bash
anima webhook create --url https://example.com/hook --events email.received
```

Verify the signature on your endpoint before trusting a payload.

## What is enforced for you

- **Suppression.** Every send checks an opt-out list first. A recipient who
  unsubscribed or hard-bounced is never mailed again, whatever the agent asks.
- **Loop protection.** Outbound carries an RFC 3834 `Auto-Submitted` marker, and
  a velocity breaker holds a burst from one agent to one address for approval
  rather than letting a loop run.
- **Own-address refusal.** Sending to the agent's own address is rejected, not
  silently looped.

## Also on the same identity

The inbox is one surface of an identity that can also hold a US phone number
for SMS and voice, and an encrypted credential vault — same agent, same API,
same bill. See `agent-phone-sms` and `agent-credential-vault`.

Free tier includes email, vault and MCP. No card.
Docs: <https://docs.useanima.sh>
