#!/usr/bin/env python3
"""
agent-revenue-tracker: Unified revenue dashboard for autonomous AI agents.
Aggregates earnings across bounty, freelance, and payment platforms.

Usage:
    python3 agent_revenue.py add clawtasks 250.0 bounty-bot-1
    python3 agent_revenue.py status
    python3 agent_revenue.py status --agent bounty-bot-1
    python3 agent_revenue.py digest --days 7
    python3 agent_revenue.py roi
    python3 agent_revenue.py export --format csv
"""
import argparse
import csv
import json
import os
import sys
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path


SCRIPT_DIR = Path(__file__).parent
DATA_DIR = SCRIPT_DIR.parent / "data"
LEDGER_PATH = DATA_DIR / "ledger.json"

VALID_SOURCES = {"clawtasks", "openwork", "dework", "layer3", "upwork",
                 "fiverr", "stripe", "crypto", "gumroad", "buymeacoffee",
                 "kofi", "lemon", "etsy", "github_sponsors"}


def load_ledger() -> list:
    if not LEDGER_PATH.exists():
        return []
    with open(LEDGER_PATH) as f:
        return json.load(f)


def save_ledger(rows: list) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(LEDGER_PATH, "w") as f:
        json.dump(rows, f, indent=2)


def cmd_add(source: str, amount: float, agent: str, category: str) -> int:
    source = source.lower()
    if source not in VALID_SOURCES:
        print(json.dumps({"error": f"unknown source. valid: {sorted(VALID_SOURCES)}"}))
        return 1
    if amount <= 0:
        print(json.dumps({"error": "amount must be positive"}))
        return 1
    rows = load_ledger()
    rows.append({
        "ts": datetime.now(timezone.utc).isoformat(),
        "source": source,
        "agent": agent,
        "category": category or "bounty",
        "amount_usd": round(amount, 2),
    })
    save_ledger(rows)
    print(json.dumps({"status": "logged", "entry": rows[-1]}, indent=2))
    return 0


def cmd_status(agent: str = None) -> int:
    rows = load_ledger()
    if agent:
        rows = [r for r in rows if r["agent"] == agent]
    if not rows:
        print(json.dumps({"total_revenue_usd": 0, "count": 0, "note": "ledger empty"}))
        return 0

    total = sum(r["amount_usd"] for r in rows)
    by_source = defaultdict(float)
    by_agent = defaultdict(float)
    by_category = defaultdict(float)
    for r in rows:
        by_source[r["source"]] += r["amount_usd"]
        by_agent[r["agent"]] += r["amount_usd"]
        by_category[r["category"]] += r["amount_usd"]

    # MRR (last 30 days, normalized)
    cutoff = datetime.now(timezone.utc) - timedelta(days=30)
    recent = [r for r in rows
              if datetime.fromisoformat(r["ts"].replace("Z", "+00:00")) >= cutoff]
    mrr = sum(r["amount_usd"] for r in recent)

    # 14-day sparkline
    sparkline = []
    today = datetime.now(timezone.utc).date()
    for i in range(14):
        d = today - timedelta(days=13 - i)
        day_total = sum(
            r["amount_usd"] for r in rows
            if datetime.fromisoformat(r["ts"].replace("Z", "+00:00")).date() == d
        )
        sparkline.append({"date": d.isoformat(), "revenue_usd": round(day_total, 2)})

    top = max(by_agent.items(), key=lambda kv: kv[1])
    print(json.dumps({
        "total_revenue_usd": round(total, 2),
        "mrr_usd": round(mrr, 2),
        "transaction_count": len(rows),
        "by_source": {k: round(v, 2) for k, v in sorted(by_source.items(), key=lambda kv: -kv[1])},
        "by_agent": {k: round(v, 2) for k, v in sorted(by_agent.items(), key=lambda kv: -kv[1])},
        "by_category": {k: round(v, 2) for k, v in sorted(by_category.items(), key=lambda kv: -kv[1])},
        "top_performer": {"agent": top[0], "revenue_usd": round(top[1], 2)},
        "sparkline_14d": sparkline,
    }, indent=2))
    return 0


def cmd_digest(days: int) -> int:
    rows = load_ledger()
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    recent = [r for r in rows
              if datetime.fromisoformat(r["ts"].replace("Z", "+00:00")) >= cutoff]
    if not recent:
        print(json.dumps({"period_days": days, "revenue_usd": 0, "transactions": 0}))
        return 0

    total = sum(r["amount_usd"] for r in recent)
    by_source = defaultdict(float)
    by_agent = defaultdict(float)
    for r in recent:
        by_source[r["source"]] += r["amount_usd"]
        by_agent[r["agent"]] += r["amount_usd"]

    avg_per_tx = total / len(recent)
    top_source = max(by_source.items(), key=lambda kv: kv[1])
    top_agent = max(by_agent.items(), key=lambda kv: kv[1])

    print(json.dumps({
        "period_days": days,
        "revenue_usd": round(total, 2),
        "transactions": len(recent),
        "avg_per_tx_usd": round(avg_per_tx, 2),
        "top_source": {"name": top_source[0], "revenue_usd": round(top_source[1], 2)},
        "top_agent": {"name": top_agent[0], "revenue_usd": round(top_agent[1], 2)},
        "by_source": {k: round(v, 2) for k, v in sorted(by_source.items(), key=lambda kv: -kv[1])},
        "by_agent": {k: round(v, 2) for k, v in sorted(by_agent.items(), key=lambda kv: -kv[1])},
    }, indent=2))
    return 0


def cmd_roi() -> int:
    """
    Compute a simple ROI ranking.
    Each agent's effective hourly rate is total / hours_logged.
    Hours are inferred from tx count: assume each tx = 1 hour of agent runtime.
    """
    rows = load_ledger()
    by_agent = defaultdict(lambda: {"revenue": 0.0, "txs": 0})
    for r in rows:
        a = by_agent[r["agent"]]
        a["revenue"] += r["amount_usd"]
        a["txs"] += 1

    out = []
    for agent, data in by_agent.items():
        hours = max(1, data["txs"])
        hourly = data["revenue"] / hours
        # Treat a $25 baseline cost per agent-month as burn
        burn = 25.0
        roi_pct = round(((data["revenue"] - burn) / burn) * 100, 1)
        out.append({
            "agent": agent,
            "revenue_usd": round(data["revenue"], 2),
            "transactions": data["txs"],
            "hourly_rate_usd": round(hourly, 2),
            "estimated_burn_usd": burn,
            "roi_pct": roi_pct,
        })
    out.sort(key=lambda r: r["roi_pct"], reverse=True)
    print(json.dumps({"ranking": out, "count": len(out)}, indent=2))
    return 0


def cmd_export(fmt: str) -> int:
    rows = load_ledger()
    out_path = DATA_DIR / f"ledger_export.{fmt}"
    if fmt == "csv":
        with open(out_path, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["ts", "source", "agent", "category", "amount_usd"])
            w.writeheader()
            w.writerows(rows)
    else:
        with open(out_path, "w") as f:
            json.dump(rows, f, indent=2)
    print(json.dumps({"exported": str(out_path), "rows": len(rows)}))
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="Agent revenue tracker")
    sub = p.add_subparsers(dest="cmd", required=True)

    p1 = sub.add_parser("add")
    p1.add_argument("source")
    p1.add_argument("amount", type=float)
    p1.add_argument("agent")
    p1.add_argument("--category", default="bounty")

    p2 = sub.add_parser("status")
    p2.add_argument("--agent", default=None)

    p3 = sub.add_parser("digest")
    p3.add_argument("--days", type=int, default=7)

    p4 = sub.add_parser("roi")

    p5 = sub.add_parser("export")
    p5.add_argument("--format", choices=["csv", "json"], default="csv")

    args = p.parse_args()
    if args.cmd == "add":
        return cmd_add(args.source, args.amount, args.agent, args.category)
    if args.cmd == "status":
        return cmd_status(args.agent)
    if args.cmd == "digest":
        return cmd_digest(args.days)
    if args.cmd == "roi":
        return cmd_roi()
    if args.cmd == "export":
        return cmd_export(args.format)
    return 0


if __name__ == "__main__":
    sys.exit(main())
