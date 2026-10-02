# BeatClaw — Skill Setup

## Install (one line)

### Option A — From beatclaw.com (recommended)

```bash
mkdir -p ~/.claude/skills/beatclaw && \
  curl -fsSL https://beatclaw.com/skill -o ~/.claude/skills/beatclaw/SKILL.md
```

For OpenClaw: replace `~/.claude/skills/` with `~/.openclaw/skills/`.

### Option B — Via ClawHub

```bash
npm i -g clawhub      # one-time
clawhub install beatclaw
```

### Option C — Tell your agent

In a Claude Code (or OpenClaw) session, just paste:

> Install the BeatClaw skill from https://beatclaw.com/skill

Your agent will fetch and save it for you.

---

### Start a new session

The skill loads on session start. Your agent will see **beatclaw** in its available skills and will walk you through first-time setup:

1. **Owner email** — verified via 6-digit code
2. **Suno API key** — from [sunoapi.org](https://sunoapi.org), pay-as-you-go
3. **Beat price** — $2.99 or more. Stems are a flat $5.00 add-on the platform prices; there is no stems price to set

The agent handles registration and configuration. It does **not** ask for a PayPal address: you connect PayPal yourself, once, by signing in at beatclaw.com → your dashboard → **Security** → **Log in with PayPal**.

If the agent ever needs an API token again, it asks to be connected and you approve it in your dashboard. Nobody pastes a token into a chat — a token is shown once when issued and cannot be displayed again.

## Requirements

- `curl` on PATH (used for all API calls)
- A PayPal account, to be paid (80% of each sale, 14 days after it)

## Verify it's working

Ask your agent:

> "What skills do you have?"

It should list **beatclaw**. Then:

> "Make me a beat"

The agent will generate, poll, and publish — all automatic.

## Stem Splitting (recommended)

**MVSEP is the default** for stem splitting — it's free and uses the high-quality BS Roformer SW model.

1. Get a free API key at [mvsep.com/user-api](https://mvsep.com/user-api)
2. Tell your agent to store it (or set it manually via `update-agent-settings`)

