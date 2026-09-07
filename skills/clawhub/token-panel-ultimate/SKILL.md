---
name: token-panel-ultimate
version: 2.4.0
description: "Know exactly where your AI tokens go. Multi-provider tracking, budget alerts, and a local REST API—all in one dashboard. It reads Claude Code's own credential file to query Anthropic usage, calls provider usage APIs, and (opt-in) parses local session transcripts. Serves a REST API on localhost. See Permissions, Data Flow & Consent."
metadata:
  openclaw:
    permissions:
      network:
        required: true
        scope: "Provider usage endpoints only (Anthropic, OpenAI, Google, Manus) plus a REST API bound to localhost. No third-party telemetry."
      file_read:
        required: true
        scope: "~/.claude/.credentials.json to read Claude Code's OAuth token (see the warning below); and, ONLY with TOKEN_PANEL_READ_TRANSCRIPTS=1, local session transcripts under ~/.openclaw/agents."
      file_write:
        required: true
        scope: "A local SQLite database of token COUNTS. Message content is never stored."
      env_read:
        required: true
        scope: "OPENAI_API_KEY / provider keys. A secrets FILE is only read if you name it via OPENAI_ENV_FILE (absolute, owner-only 0600) — there is no silent .env scraping."
      credentials:
        required: true
        scope: "Reads an existing Anthropic OAuth token from Claude Code's credential store. Not minted for this tool — see the warning."
    owner: kn7623hrcwt6rg73a67xw3wyx580asdw
    category: monitoring
    tags:
      - tokens
      - usage
      - budget
      - anthropic
      - openai
      - gemini
      - manus
      - dashboard
    license: MIT
    notes:
      security: "Runs a local REST API on localhost:8765 for usage tracking. SQLite database stored locally. Reads provider usage from local transcripts and official APIs using your existing credentials. No external data sharing, no cloud dependencies. Systemd service runs as your user, not root."
---

# Token Panel Ultimate

**One dashboard for every token you spend.** Anthropic, Gemini, OpenAI, Manus—tracked, stored, and queryable before the bill arrives.


## ⚠️ Permissions, Data Flow & Consent — read before installing

**What it does that a "dashboard" does not imply:**

- **It reads Claude Code's credential file** (`~/.claude/.credentials.json`) to get an OAuth
  token and query Anthropic's usage endpoint. That token was issued to Claude Code, not to this
  tool. ClawHub's scanner flags this as credential re-use and **it is right to** — we are not
  going to soften that. If you are not comfortable with it, skip the Claude collector; every
  other provider works from a key you supply yourself.
- **It can parse your session transcripts**, which contain your prompts and replies in full.
  This is **opt-in and off by default**: nothing is read unless you set
  `TOKEN_PANEL_READ_TRANSCRIPTS=1`. Only token counts are extracted; message text is never
  written to the database or returned by the API.
- **It serves a REST API.** Bind it to localhost and do not expose it — it reports your usage
  and quota.

**What it does NOT do:** no silent secrets scraping (Gemini and Manus keys come from the
environment only; a secrets file is read only if you name it in `OPENAI_ENV_FILE`, and it must
be an absolute, owner-only `0600` file), no message content in the database, no telemetry, no
third-party endpoint. The local API allows CORS only from localhost dashboard origins, not `*`.

**Diagnostics are off by default.** The browser widget logs nothing unless you set
`localStorage.BP_DEBUG = "1"` — console output is readable by anything sharing the page.

**Dependencies are pinned above known-vulnerable releases.** The floor for `fastapi` is
`0.109.1`; the previous `>=0.100.0` permitted a release affected by CVE-2024-24762.


## Why This Exists

You've checked your Anthropic console, squinted at the OpenAI dashboard, opened a Gemini tab, and still weren't sure where last Tuesday's $14 went. Token Panel Ultimate puts all four providers in one place so the answer is always one query away.

## What It Does

- **Multi-Provider Tracking** — Anthropic, Gemini, OpenAI, and Manus in a single SQLite database
- **Budget Alerts** — Set monthly limits per provider. Get warned before you overspend, not after
- **REST API** — Query usage programmatically on port 8765. Plug it into your own scripts or dashboards
- **Transcript Parsing** — Automatically extracts token counts from OpenClaw session transcripts
- **Zero Dependencies** — SQLite storage. No Postgres, no Redis, no cloud account required
- **Runs as a Daemon** — Systemd service keeps it alive in the background

## Quick Start

```bash
pip install -r requirements.txt
python3 api.py
```

## Architecture

```
OpenClaw Plugin → Budget Collector API → SQLite DB
                        ↓
                Transcripts / Anthropic API / Manus Tracker
```

## API Endpoints

| Method | Path              | Description                  |
|--------|-------------------|------------------------------|
| GET    | /usage            | All provider usage           |
| GET    | /usage/:provider  | Usage for a single provider  |
| GET    | /budget           | Current budget limits        |
| POST   | /budget           | Set or update budget limits  |

*Clone it. Fork it. Break it. Make it yours.*

👉 Explore the full project: [github.com/globalcaos/clawdbot-moltbot-openclaw](https://github.com/globalcaos/clawdbot-moltbot-openclaw)
