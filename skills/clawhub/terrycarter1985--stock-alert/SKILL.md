---
name: stock-alert
description: Generate a daily stock price watchlist alert and deliver it to a WhatsApp chat/group via the wacli (`wu`) CLI. Live quotes use yfinance with automatic fallback to a bundled local CSV snapshot when the network/Yahoo is unavailable or rate-limited. Use when a user wants scheduled or on-demand stock price notifications pushed to WhatsApp. NOT for trading execution or real-time tick streaming.
metadata:
  {
    "openclaw":
      {
        "requires": { "bins": ["python3"] },
        "install":
          [
            {
              "id": "pydeps",
              "kind": "shell",
              "command": "pip install -r requirements.txt",
              "label": "Install Python deps (yfinance, pandas, pyyaml)"
            },
            {
              "id": "wacli",
              "kind": "node",
              "package": "@ibrahimwithi/wu-cli",
              "bins": ["wu"],
              "label": "Install WhatsApp CLI (wacli) — optional, for sending"
            }
          ]
      }
  }
---

# Stock Alert (WhatsApp)

Generate a formatted stock watchlist alert and send it to WhatsApp.

## Quick start

```bash
# Print the alert without sending (no WhatsApp needed)
python3 stock_alert_workflow.py --dry-run

# Send to the configured recipient (requires `wu` logged in)
python3 stock_alert_workflow.py

# Custom symbols + recipient
STOCK_ALERT_RECIPIENT="123456@g.us" python3 stock_alert_workflow.py --symbols AAPL NVDA AMD
```

## How it works

1. `lib/finance_tools.get_stock_price()` fetches a live quote via **yfinance**.
2. On any failure (no network, HTTP 429 rate limit, missing dependency) it
   **falls back to `data/nasdaq_stock_prices.csv`** so the alert still renders.
3. The workflow formats each symbol defensively (never crashes on `N/A`).
4. Delivery uses the **wacli `wu send <jid> <message>`** command.
   - If `wu` is not installed, the run **degrades to dry-run** (exit 0) instead
     of crashing, and prints how to install it.

## Configuration

- `config/wacli_config.yaml` — wacli chat constraints (which JIDs may receive).
- Env overrides:
  - `STOCK_ALERT_RECIPIENT` — target WhatsApp JID (default `finance-alerts@g.us`)
  - `STOCK_ALERT_DATA_DIR` — override the CSV data directory

## Requirements

See `requirements.txt`. The `wu` CLI is only needed to actually send:
`npm i -g @ibrahimwithi/wu-cli && wu login`.

## Scheduling

Use OpenClaw cron for a daily 09:30 alert, e.g. an `agentTurn` that runs
`python3 stock_alert_workflow.py`. Keep one consolidated send per run to respect
WhatsApp rate limits.

## Permissions

This skill sends messages on the user's behalf and (optionally) syncs reports to
Feishu/Lark docs. Document-permission handling follows the project's Feishu
permission standard — see `docs/PERMISSIONS.md`.

## Files

- `stock_alert_workflow.py` — entry point
- `lib/finance_tools.py` — quote fetch + local fallback
- `data/nasdaq_stock_prices.csv` — offline snapshot
- `config/wacli_config.yaml` — delivery constraints
- `docs/PERMISSIONS.md` — Feishu permission configuration
