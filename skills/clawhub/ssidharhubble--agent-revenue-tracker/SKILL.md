---
name: agent-revenue-tracker
description: Track revenue from autonomous AI agents across multiple platforms. Aggregates earnings from ClawTasks, OpenWork, Dework, Layer3, Upwork, Fiverr, Stripe, and crypto wallets into a single dashboard. Computes MRR, take rate, hourly rate, and ROI per agent. Categorizes by skill type (bounty, freelance, recurring, tip) and platform. Built for AI agent operators running multiple bots, side hustlers with several income streams, and AI founders tracking burn vs revenue across an agent fleet.
compatibility: Created for Zo Computer
metadata:
  author: ssyopros.zo.computer
allowed-tools: Bash
---

# Agent Revenue Tracker

Unified revenue dashboard for autonomous AI agents. Aggregates earnings across bounty platforms, freelance marketplaces, Stripe, and crypto wallets. Computes per-agent ROI and the income breakdown by source.

## When to use

- User runs multiple AI agents and wants a single P&L view
- Tracking bounty income (ClawTasks, OpenWork, Dework, Layer3)
- Reconciling freelance earnings (Upwork, Fiverr) with crypto tips
- Computing per-agent ROI and hourly rate
- Producing a weekly revenue digest for a multi-agent portfolio

## Commands

```bash
python3 scripts/agent_revenue.py add <source> <amount> <agent>  # Log a payment
python3 scripts/agent_revenue.py status                         # Dashboard
python3 scripts/agent_revenue.py status --agent <name>          # Single agent P&L
python3 scripts/agent_revenue.py digest --days 7                # Weekly digest
python3 scripts/agent_revenue.py roi                            # ROI ranking
python3 scripts/agent_revenue.py export --format csv            # Export ledger
```

## Output

JSON dashboard with: total_revenue_usd, mrr_usd, by_source (ClawTasks, OpenWork, Dework, Layer3, Upwork, Fiverr, Stripe, crypto), by_agent (with hours_logged, hourly_rate_usd, roi_pct), top_performer, week_over_week_change_pct, and a 14-day revenue sparkline.

## Storage

Local JSON ledger at `/home/workspace/Skills/agent-revenue-tracker/data/ledger.json` (auto-created). Use the `add` command to log payments; the rest of the CLI reads from there.
