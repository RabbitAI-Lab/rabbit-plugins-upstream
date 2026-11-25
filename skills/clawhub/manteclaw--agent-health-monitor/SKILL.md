---
name: agent-health-monitor
description: Health monitoring for AI agent infrastructure. Checks API key validity, wallet gas balances, and service endpoint reachability, and sends threshold-based alerts via Telegram/Discord. No mining, earning, revenue reporting, or background workers — this skill only observes and alerts.
version: 1.0.3
allowed-tools: Read, Bash
permissions:
  - env
  - file_read
  - file_write
  - network
  - shell
---

# Agent Health Monitor

## Overview

Monitoring stack for autonomous AI agents. Checks API keys, wallet gas balances, and service endpoints, and alerts on failures via Telegram/Discord. It only observes and alerts: it does not start, stop, or restart any process, does not move funds, and does not aggregate earnings or revenue.

What this skill does **not** do (removed in v1.0.1, see Changelog):

- No mining, earning-task, or contribution workers — nothing is launched or kept running in the background.
- No revenue, profit, or earnings aggregation or reporting.
- No systemd/cron installation and no `sudo` step.
- No credential files are read (no `.env` loading anywhere in the skill).

## Tool scope (declared)

The skill's code uses exactly these capabilities — nothing else:

| Capability | What the code actually does |
|---|---|
| `env` | Reads the operator's own API keys and wallet addresses from environment variables only (see `CONFIGURATION.md`). No credential is ever hardcoded, and no default key exists. |
| `file_read` | Reads only its own scripts. `api_key_monitor.py --export` writes one JSON results file, but only when the operator explicitly passes `--export <path>`. |
| `file_write` | Same `--export` output only. No other script writes files. |
| `network` | HTTPS requests only, to the operator's own services' official endpoints (allow-list below). No other destination is contacted. |
| `shell` | Runs its own Python scripts via `sys.executable`. No shell commands, no `eval`, no `subprocess` with `shell=True`. |

External endpoints contacted (allow-list — all HTTPS, all official first-party APIs):

| Endpoint | Used by | For |
|---|---|---|
| `api.groq.com`, `api.mistral.ai`, `openrouter.ai`, `api.dune.com`, `api.github.com` | `api_key_monitor.py` | Key-validity checks (key sent only to its own owner) |
| `api.groq.com`, `api.mistral.ai`, `openrouter.ai`, `api.dune.com`, `api.github.com` | `healthcheck.py` | Keyless reachability probes — no credential is sent |
| `base-mainnet.g.alchemy.com` | `healthcheck.py`, `balance-monitor.py` | Alchemy RPC (key in URL path, Alchemy's own design) |
| `api.telegram.org` | `alert_bot.py` | Sending alerts to the operator's own Telegram chat |
| `discord.com/api/webhooks/` | `alert_bot.py` | Sending alerts to the operator's own Discord webhook |
| `meshledger.io` | `api_key_monitor.py` | MeshLedger key-validity check |

## Privacy warning — read before setup (SQP-2)

Alerts leave your machine. Every alert sent to Telegram or Discord contains operational information: which service failed, wallet addresses (truncated to the first 10 characters), ETH balances, and short error details. That information becomes visible to anyone who can read the configured Telegram chat or Discord channel.

- Use a **private** Telegram chat / private Discord channel for alerts, and keep the webhook URL and bot token secret — anyone with them can read your alerts (Discord) or impersonate the bot (Telegram).
- **No API key, token, or private key is ever included in an alert, a log line, or an export.** Error details are scrubbed of key material before they are printed or sent.
- If you do not want anything to leave the machine, simply do not configure Telegram/Discord: alerts then print to local stdout only (local-only logging).

## How credentials are handled (why this is not exfiltration)

The ClawHub audit flagged any flow where a credential reaches a network call. Here is exactly what happens, so a reviewer can verify it:

- **Key-validity checks (`api_key_monitor.py`) are the tool's purpose.** There is no way to test whether an API key is valid without presenting it to its owner. Each key is sent **only to that key owner's own official HTTPS endpoint** (Groq's key to `api.groq.com`, Mistral's to `api.mistral.ai`, and so on) — never to any third party, never in a message body, and never in a log. Keys come from environment variables only.
- **Endpoint checks (`healthcheck.py`) send no credential at all.** They are keyless reachability probes: the key is only checked for presence, and the request carries no `Authorization` header. A live service answers (200, or 401/403 because no key was presented); a dead one times out. Key validity is `api_key_monitor.py`'s job, not this script's.
- **Telegram/Discord delivery requires the credential by design.** Telegram's Bot API puts the bot token in the request URL and Discord webhooks are capability URLs — there is no token-free way to use either. Both go to the operator's own configured channels over HTTPS, and the Discord URL is allow-listed to `discord.com` / `discordapp.com` webhook hosts.
- **Alchemy keys** go in the RPC URL path because that is Alchemy's own API design, over HTTPS.
- **`EXECUTOR_PRIVATE_KEY` (healthcheck only) is used locally only**: it derives the wallet address to compare against `EXECUTOR_ADDRESS`. It is never transmitted anywhere.
- **No key material in output.** Every error detail is scrubbed of configured key values before it is printed, alerted on, or exported.

## Core Capabilities

### 1. API Key Health

Tests 8 APIs (`scripts/api_key_monitor.py`, run daily or on demand):

| Service | Test | Fail Action |
|---------|------|-------------|
| Alchemy | RPC call (`eth_blockNumber`) | Alert |
| Groq | Key-validity check | Alert |
| Mistral | Key-validity check | Alert |
| OpenRouter | Key-validity check | Alert |
| GitHub | Key-validity check | Alert |
| Dune | Key-validity check | Alert |
| Bankr | Key-validity check via its SDK | Alert |
| MeshLedger | Key-validity check | Alert |

### 2. Wallet Balance Monitor

Monitors ETH gas balances of the configured wallets (`scripts/balance-monitor.py`):

- Executor wallet (`EXECUTOR_ADDRESS`)
- Two additional wallets (`WALLET_ADDRESS_1`, `WALLET_ADDRESS_2`)

Wallets left unconfigured are skipped, not checked. (Before v1.0.3 the two extra wallets defaulted to the zero address, which always reported LOW.)

Alerts when a balance falls below the threshold (default 0.005 ETH, set `GAS_ALERT_THRESHOLD` to change it).

### 3. Service Endpoint Checks

`scripts/healthcheck.py` verifies each service is reachable (keyless probes — see above), plus the Alchemy RPC and the Bankr SDK. Run it after any key rotation or deployment. Exit code 0 means healthy.

## Alert Channels

| Channel | Config | Use |
|---------|--------|-----|
| Telegram | `TELEGRAM_BOT_TOKEN` + `TELEGRAM_CHAT_ID` | Critical alerts |
| Discord | `DISCORD_WEBHOOK_URL` | Status summaries |
| Stdout | (no config) | All alerts print locally when no channel is configured |

## Workflow

### Setup

```bash
# 0. Install the Python dependencies (see requirements.txt)
pip install -r requirements.txt

# 1. Configure alerts (see the Privacy warning above first)
export TELEGRAM_BOT_TOKEN=...
export TELEGRAM_CHAT_ID=...
export DISCORD_WEBHOOK_URL=...

# 2. Configure the keys and wallets to monitor (see CONFIGURATION.md)
export ALCHEMY_API_KEY=...
export GROQ_API_KEY=...
export EXECUTOR_ADDRESS=...

# 3. Run a check (no sudo, nothing runs in the background)
python3 scripts/healthcheck.py
python3 scripts/master_monitor.py
```

Optional: run `scripts/master_monitor.py` from cron every 5 minutes for continuous monitoring. The skill itself installs no services or daemons — the only install is the `pip` command above. The Bankr check needs the optional `litcoin` SDK (see `requirements.txt`); without it that check reports "SDK not installed" and skips.

### Daily Operations

```bash
# Check all systems (exits non-zero if anything is wrong)
python3 scripts/master_monitor.py

# Full endpoint + key-presence check
python3 scripts/healthcheck.py

# Test a specific API key
python3 scripts/api_key_monitor.py --check groq

# Check wallet gas balances
python3 scripts/balance-monitor.py
```

### Recovery Procedures

| Failure | Manual Fallback |
|---------|-------------|
| API key expired | Rotate the key via the provider's dashboard, update the env var, re-run `healthcheck.py` |
| Service unreachable | Check the provider's status page and your network; the probe sends no credential, so a 401/403 means the service is up |
| Wallet low on gas | Fund the wallet; alert only — this skill never moves funds |
| Alert not received | Check `TELEGRAM_BOT_TOKEN` / `TELEGRAM_CHAT_ID` / `DISCORD_WEBHOOK_URL` and run `python3 scripts/alert_bot.py --test` |

## Scripts

- `scripts/healthcheck.py` — API/endpoint health checker (keyless probes + Alchemy RPC + Bankr SDK)
- `scripts/balance-monitor.py` — Wallet balance tracker
- `scripts/api_key_monitor.py` — API key tester
- `scripts/master_monitor.py` — Unified monitor runner (healthcheck + balance)
- `scripts/alert_bot.py` — Telegram/Discord alert dispatcher

## References

- `references/alert-config.md` — Channel setup and webhook formats
- `CONFIGURATION.md` — Every environment variable the skill reads
- `requirements.txt` — Python dependencies (`pip install -r requirements.txt`)

## Stats

- **8 APIs** checked for key validity
- **3 wallets** tracked for gas
- **0 background workers** — nothing is launched or kept running
- **0 credential files read** — env vars only

## Changelog

### v1.0.3 — 2026-11-19 (vetting follow-up)

- **Fixed phantom low-gas alerts (F1):** `balance-monitor.py` defaulted the two extra wallets to the zero address, which is a valid address with a 0 balance, so every default-config run reported two false LOW wallets. Unconfigured wallets are now skipped (empty default, same as `EXECUTOR_ADDRESS`), and the dead-lane label "AWP / Old" is renamed "Additional Wallet".
- **Fixed silent pass on a crashed sub-check (F2):** `master_monitor.py` only recorded an issue when the balance monitor's stdout contained "LOW" or "error", so a crash (e.g. `web3` not installed) with empty stdout was reported as "All systems nominal" with exit 0. A nonzero exit with no parsed issue line now records "balance monitor failed to run (exit code N)" and exits nonzero.
- **Added dependency documentation (F3):** new `requirements.txt` (`web3`, `eth-account`; optional `python-telegram-bot`, `litcoin`) and a `pip install -r requirements.txt` step in Setup. The old "no install step" claim was false on a bare machine. The Bankr check's `litcoin` SDK requirement is now stated in Setup and `CONFIGURATION.md`.

### v1.0.2 — 2026-11-19 (rescan follow-up)

- Declared the full tool scope in the frontmatter (`permissions: [env, file_read, file_write, network, shell]`) — the v1.0.1 list omitted `env` and `file_write`, which the rescan flagged as HIGH LP1. No code change; behavior is identical to v1.0.1.

### v1.0.1 — 2026-11-18 (security audit remediation)

- **Removed `scripts/revenue_reporter.py`** (ClawHub audit TP4): it aggregated daily revenue, task rewards, and trading profits and sent financial summaries to Telegram/Discord by default — undisclosed financial reporting in a health monitor. Deleted; the original is preserved in the pre-publish archive, not in this bundle.
- **Removed `scripts/supervisor.sh` and mining-worker supervision** (TP4, PE3, AE1): the supervisor auto-launched and maintained mining/earning workers (AWP, 0xWork, Nookplot, Litcoiin) with wallet and API-key env vars and a mining-platform endpoint, and blanket-sourced the workspace `.env` under `set -a`, exporting every credential to every daemon and wrapper. The whole file is deleted, along with the service checks for those workers in `master_monitor.py`. This skill no longer starts, maintains, or monitors any worker process.
- **Healthcheck endpoint checks are now keyless probes** (TT3): `healthcheck.py` no longer sends Groq/Mistral/OpenRouter/Dune/GitHub credentials over the network — it probes reachability without any `Authorization` header. Key validity stays in `api_key_monitor.py`, where each key goes only to its own owner's official HTTPS endpoint (documented above).
- **Key material scrubbed from all output**: error details in `api_key_monitor.py`, `healthcheck.py`, and `balance-monitor.py` are redacted of configured key values before printing, alerting, or exporting.
- **Discord webhook allow-listed** (`alert_bot.py`): the webhook URL must be an `https://discord.com/api/webhooks/` (or `discordapp.com`) URL; anything else is refused.
- **Removed dangling references** (PE2 and prior gap): `scripts/install-services.sh` (with its `sudo` step), `scripts/alert.sh`, and `references/recovery-playbook.md` never shipped and are no longer referenced.
- **Declared tool scope** (LP3): `allowed-tools` + `permissions` in the frontmatter and the Tool scope table above.
- **Privacy warning** (SQP-2): the section above, before Setup.
- **Fixed healthcheck false-negatives**: HTTP 401 (expired/invalid key) used to count as healthy for Dune/GitHub.
- **Removed unimplemented claims**: cron-stack integrity and disk/memory monitoring were described but implemented by no shipped script; those sections are gone.
- **Hardening kept from the pre-audit pass**: Alchemy keys URL-quoted in RPC URLs; `master_monitor.py` resolves sibling scripts relative to its own file and no longer depends on the working directory; `balance-monitor.py` validates wallet addresses and the gas threshold instead of crashing on bad env values; bare `except:` clauses narrowed; the MeshLedger credential-file read (dead code — the key was loaded but never used) was removed with `revenue_reporter.py`.

## Known limitations

- `healthcheck.py`'s endpoint probes confirm a service is reachable, not that a key is valid — use `api_key_monitor.py` for key validity. (That split is deliberate: the frequent healthcheck never transmits credentials.)
- `api_key_monitor.py` and `alert_bot.py` still send credentials over the network by necessity (a key to its own owner's endpoint; a Telegram token / Discord webhook URL to its own service). See "How credentials are handled" above. A rescan may still flag the pattern; the pattern is the documented function, not exfiltration.
- Telegram alerts use `parse_mode: Markdown`; alert text comes from the operator's own monitoring data, but unusual characters in service/error text can disturb formatting. No code execution is involved.
- Restarting a failed service is manual — this skill observes and alerts only.
- `EXECUTOR_PRIVATE_KEY` is optional; when set, `healthcheck.py` uses it only locally to verify it matches `EXECUTOR_ADDRESS`. It is never sent anywhere.
