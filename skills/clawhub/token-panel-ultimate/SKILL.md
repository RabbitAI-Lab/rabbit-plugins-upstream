---
name: token-panel-ultimate
version: 2.5.1
description: "Know exactly where your AI tokens go. Multi-provider tracking, budget alerts, and a local REST API—all in one dashboard. Provider credentials are supplied by you and sealed in the OS keychain; it never reads another application's credential store. Transcript parsing is opt-in. See Permissions, Data Flow & Consent."
metadata:
  openclaw:
    permissions:
      network:
        required: true
        scope: "Provider usage endpoints only (Anthropic, OpenAI, Google, Manus) plus a REST API bound to localhost. No third-party telemetry."
      file_read:
        required: true
        scope: "Its own keychain entry (or warned owner-only 0600 fallback file); and, ONLY with TOKEN_PANEL_READ_TRANSCRIPTS=1, local session transcripts under ~/.openclaw/agents."
      file_write:
        required: true
        scope: "A local SQLite database of token COUNTS. Message content is never stored."
      env_read:
        required: true
        scope: "TOKEN_PANEL_* provider variables (plus standard provider API-key variables) as an optional CI/one-shot fallback. No .env files are scraped."
      credentials:
        required: true
        scope: "First-party provider API keys supplied by you, stored under token-panel-ultimate in the OS keychain. It never reads Claude Code, OpenClaw, browser, or other application credential stores."
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

> One of dozens of skills and plugins in **[TinkerClaw](https://github.com/globalcaos/tinkerclaw)** — a self-improving OpenClaw fork that's been running 24/7 for months.


**One dashboard for every token you spend.** Anthropic, Gemini, OpenAI, Manus—tracked, stored, and queryable before the bill arrives.



**Part of [TinkerClaw](https://github.com/globalcaos/tinkerclaw)** — real-time token tracking, self-improving crons, persistent cognitive memory. This is one piece of that stack; the repo has dozens more.

👉 **https://github.com/globalcaos/tinkerclaw**

_Clone it. Fork it. Break it. Make it yours._


## ⚠️ Permissions, Data Flow & Consent — read before installing

**What it does that a "dashboard" does not imply:**

- **It uses only credentials you supply to Token Panel itself.** `python3 secretstore.py --login
  anthropic` reads an Admin API key from stdin and seals it in the OS keychain. The same command
  supports `openai`, `gemini`, and `manus`. It never reads Claude Code, OpenClaw, browser, or
  another application's credential store. `--logout PROVIDER` clears both local stores and prints
  the provider's server-side revoke URL.
- **It can parse your session transcripts**, which contain your prompts and replies in full.
  This is **opt-in and off by default**: nothing is read unless you set
  `TOKEN_PANEL_READ_TRANSCRIPTS=1`. Only token counts are extracted; message text is never
  written to the database or returned by the API.
- **It serves a REST API.** Bind it to localhost and do not expose it — it reports your usage
  and quota.

**What it does NOT do:** no credential reuse, no browser-token extraction, no silent secrets
scraping, no `.env` reads, no message content in the database, no telemetry, no third-party
endpoint. If no OS keychain exists, the CLI warns on every use before falling back to an
owner-only `0600` file inside a `0700` directory. The local API allows CORS only from localhost
dashboard origins, not `*`.

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
