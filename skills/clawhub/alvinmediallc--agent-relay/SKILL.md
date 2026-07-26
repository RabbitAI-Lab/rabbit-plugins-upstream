---
name: agent-relay
description: "Bridge between an AI agent and a phone — send/receive messages with attachments and push notifications. Push-first webhook architecture with polling fallback."
metadata:
  version: "1.0.0"
  clawhub:
    emoji: "📱"
    os: ["darwin", "linux"]
---

# Agent Relay

Bridge between an AI agent and its human's phone. Push-first webhook architecture
with polling fallback. Supports text messages, image/file attachments, and
standalone push notifications.

## Architecture

```
Phone → Relay Server (replit.app) → Webhook POST /hooks/agent-relay
                                        ↓
                                Reverse proxy (Caddy/nginx)
                                        ↓
                                OpenClaw hooks engine
                                        ↓
                            Transform: downloads attachments
                                        ↓
                            Isolated agent session
                            (full tools, memory, search)
                                        ↓
                                relay send → Phone

FALLBACK (runs every 2 min):
  cron:poll-inbox-fallback → GET inbox → dedup → re-submit to webhook
```

Push-first, polling as insurance. No message is lost.

## Quick Start

### 1. Deploy the Relay Server

Deploy to Replit (or any Node.js host):
- Fork the Agent Relay server repo
- Create an agent in the app → get your API key
- Save the key — it's shown only once

### 2. Install the Skill

```bash
openclaw skills install agent-relay
```

### 3. Configure Environment

```bash
export RELAY_API_KEY="your-api-key"
export RELAY_BASE_URL="https://your-app.replit.app/api"
```

### 4. Configure OpenClaw Hooks

Follow the template in `references/hooks-config.md`. Copy `references/transform.mjs`
to `~/.openclaw/hooks/transforms/agent-relay.mjs` (edit `MEDIA_ROOT` and paths).

Then restart OpenClaw.

### 5. Set Up the Webhook in the Relay App

1. Open the relay app on your phone
2. Connect → Instant delivery → enter `https://your-domain.com/hooks/agent-relay`
3. Optionally set a shared secret (validates `X-Webhook-Secret` header)
4. Tap "Send test ping" → you should get back `{"ok":true}`

### 6. Set Up the Inbox Fallback

Add a cron job that runs every 2 minutes:

```bash
cron add:
  schedule: every 120s
  session: isolated
  payload: agentTurn
  message: "Run: scripts/poll-inbox-fallback. Report only if messages were found."
  delivery: none
```

This catches any messages that webhook delivery missed or retried and failed.

## CLI Reference

```bash
./scripts/relay whoami                    # check connection
./scripts/relay inbox                     # read pending messages (JSON)
./scripts/relay send "text"               # send text message
./scripts/relay notify "title" "body"     # push notification (no chat)
./scripts/relay attach "text" "url" "type" "name"  # send with attachment
```

## Attachment Processing

When a push webhook payload includes `message.attachment`:

1. **Transform module** downloads the file to a per-message subdirectory
2. **Agent prompt** includes file path and type: `[Image attached: photo.jpg (33 KB)]`
3. **Agent** uses `read` tool (images) or `exec` (other files) to inspect
4. **Agent** replies via `./scripts/relay send`

No attachment or failed download → plain text message still flows through.

## Push vs Polling

| Mode | Latency | Reliability | Setup |
|------|---------|-------------|-------|
| **Push (webhook)** | Instant | Best | Needs HTTPS endpoint |
| **Polling** | 15-120s delay | Good (no HTTPS needed) | Just cron |
| **Both** (recommended) | Instant | Best of both | Push + fallback cron |

If you can't expose an HTTPS endpoint, use polling-only mode with
`scripts/poll-inbox`.

## Etiquette

- Short answers (1-3 lines) — the user reads on a phone
- No greetings, sign-offs, emoji fluff
- Direct answers to direct questions
- Match the user's communication style

## Files

| File | Purpose |
|------|---------|
| `SKILL.md` | This document |
| `scripts/relay` | CLI for sending messages, reading inbox, pushing notifications |
| `scripts/poll-inbox` | Polling-only inbox reader |
| `scripts/poll-inbox-fallback` | Fallback poller with dedup (for webhook failures) |
| `references/RELAY_API.md` | Full Agent Relay API reference |
| `references/hooks-config.md` | Template for OpenClaw hooks config |
| `references/transform.mjs` | Transform module for attachment downloads |

## Security

- Never commit the API key to version control
- Use environment variables (`$RELAY_API_KEY`, `$RELAY_BASE_URL`)
- Use a separate bearer token for the hooks endpoint (not the gateway token)
- The relay server keeps undelivered messages in its inbox — nothing is lost
- If the API key is rotated, update `$RELAY_API_KEY` and restart
