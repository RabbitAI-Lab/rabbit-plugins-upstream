# Agent Revenue Tracker

Unified revenue dashboard for autonomous AI agents. Tracks earnings across bounty platforms, freelance marketplaces, Stripe, and crypto wallets from a single CLI.

## What it does

- `add` — log a payment with source, amount, and agent
- `status` — full P&L: total revenue, MRR, breakdown by source/agent/category, 14-day sparkline
- `status --agent <name>` — single-agent deep dive
- `digest --days N` — N-day rollup with top source and top agent
- `roi` — per-agent ROI ranking with hourly rate and burn-vs-revenue math
- `export --format csv|json` — export the ledger for tax/accounting

## Why it matters

Running 3+ AI agents means juggling Stripe payouts, Upwork invoices, crypto tips, and bounty task payments across 5+ different ledgers. Reconciling them by hand every week is a tax-prep nightmare. This skill gives you a single CLI where one `add` per payout flows into one dashboard.

## Install

```bash
python3 scripts/agent_revenue.py add clawtasks 250 bounty-bot-1
python3 scripts/agent_revenue.py status
python3 scripts/agent_revenue.py digest --days 7
```

Zero dependencies. Python 3.9+.

## Storage

Ledger persists at `data/ledger.json` (auto-created). One JSON line per logged payment. Export to CSV with `export --format csv` for QuickBooks or your accountant.

## Notes

The CLI ships with no integrations. Wire the `add` command to your payout webhooks (Stripe, Upwork, Fiverr, crypto wallet monitor) to automate ingestion. The data model is intentionally minimal — single ledger, append-only — so it composes with any source that can tell you `$X from $Y on $Z`.
