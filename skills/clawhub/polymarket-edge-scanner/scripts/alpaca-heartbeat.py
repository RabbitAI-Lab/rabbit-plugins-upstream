#!/usr/bin/env python3
"""Alpaca accounts heartbeat.

Logs account/position snapshots for the main swing and day-trader paper accounts,
checks risk rules from STRATEGY.md / DAYTRADE_STRATEGY.md, and flags any breach.
"""

import json
import os
import sys
import math
import datetime
from pathlib import Path

import requests

ROOT = Path("/root/.openclaw/workspace")
LOG_DIR = ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "alpaca-heartbeat.log"
STATE_FILE = LOG_DIR / "alpaca-heartbeat.state.json"

ACCOUNTS = {
    "swing": {
        "creds": os.path.expanduser("~/.alpaca/credentials.json"),
        "max_position_pct": 0.15,
        "min_cash_pct": 0.20,
        "max_positions": None,
        "max_portfolio_heat_pct": 0.40,
    },
    "daytrader": {
        "creds": os.path.expanduser("~/.alpaca/credentials.daytrader.json"),
        "max_position_pct": None,  # sized in dollars
        "min_cash_pct": 0.30,
        "max_positions": 3,
        "position_size_min": 500,
        "position_size_max": 1000,
    },
}


def now_utc():
    return datetime.datetime.now(datetime.timezone.utc)


def log(msg):
    ts = now_utc().isoformat()
    line = f"[{ts}] {msg}"
    print(line)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")


def load_state():
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text())
        except Exception as e:
            log(f"state load error: {e}")
    return {}


def save_state(state):
    STATE_FILE.write_text(json.dumps(state, indent=2, default=str))


def api_call(creds, method, path, **kwargs):
    base = creds["base_url"]
    url = path if path.startswith("http") else base + path
    headers = {
        "APCA-API-KEY-ID": creds["api_key"],
        "APCA-API-SECRET-KEY": creds["api_secret"],
    }
    try:
        r = requests.request(method, url, headers=headers, timeout=30, **kwargs)
    except Exception as e:
        log(f"API request error: {e}")
        return None
    if r.status_code >= 400:
        log(f"API error {r.status_code}: {r.text}")
        return None
    return r.json() if r.text else {}


def check_account(name, cfg, state):
    creds_path = cfg["creds"]
    if not os.path.exists(creds_path):
        log(f"[{name}] missing credentials: {creds_path}")
        return

    try:
        creds = json.load(open(creds_path))
    except Exception as e:
        log(f"[{name}] failed to load credentials: {e}")
        return

    account = api_call(creds, "GET", "/account")
    if not account:
        log(f"[{name}] could not fetch account")
        return

    positions = api_call(creds, "GET", "/positions") or []
    open_orders = api_call(creds, "GET", "/orders", params={"status": "open"}) or []

    equity = float(account.get("equity", 0))
    cash = float(account.get("cash", 0))
    buying_power = float(account.get("buying_power", 0))

    pos_by_sym = {p["symbol"]: p for p in positions}
    total_mv = sum(float(p.get("market_value", 0)) for p in positions)
    total_unrealized = sum(float(p.get("unrealized_pl", 0)) for p in positions)

    alerts = []

    # Cash buffer
    if equity > 0:
        cash_pct = cash / equity
        if cash_pct < cfg["min_cash_pct"]:
            alerts.append(f"cash below minimum {cfg['min_cash_pct']*100:.0f}%: {cash_pct*100:.1f}%")
    else:
        cash_pct = 0

    # Position size / count
    for p in positions:
        sym = p["symbol"]
        mv = float(p.get("market_value", 0))
        qty = p.get("qty", 0)
        if equity > 0 and cfg.get("max_position_pct") and mv / equity > cfg["max_position_pct"]:
            alerts.append(f"{sym} position size {mv/equity*100:.1f}% > max {cfg['max_position_pct']*100:.0f}%")
        if cfg.get("position_size_max") and mv > cfg["position_size_max"] * 1.05:
            alerts.append(f"{sym} day-trade size ${mv:,.2f} > max ${cfg['position_size_max']:,.2f}")

    if cfg.get("max_positions") and len(positions) > cfg["max_positions"]:
        alerts.append(f"position count {len(positions)} > max {cfg['max_positions']}")

    # Bracket / stop check: flag positions without an attached stop-loss order
    stop_symbols = {
        o["symbol"] for o in open_orders
        if o.get("stop_price") or (o.get("legs") and any(leg.get("stop_price") for leg in o.get("legs", [])))
    }
    for p in positions:
        sym = p["symbol"]
        if sym not in stop_symbols:
            alerts.append(f"{sym} has no visible stop-loss order")

    # Portfolio heat proxy (sum of unrealized losses as % of equity)
    unrealized_losses = sum(
        float(p.get("unrealized_pl", 0)) for p in positions
        if float(p.get("unrealized_pl", 0)) < 0
    )
    if equity > 0 and cfg.get("max_portfolio_heat_pct") and abs(unrealized_losses) / equity > cfg["max_portfolio_heat_pct"]:
        alerts.append(f"portfolio heat {abs(unrealized_losses)/equity*100:.1f}% > max {cfg['max_portfolio_heat_pct']*100:.0f}%")

    log(
        f"[{name}] equity=${equity:,.2f} cash=${cash:,.2f} "
        f"bp=${buying_power:,.2f} mv=${total_mv:,.2f} "
        f"unrealized=${total_unrealized:,.2f} positions={len(positions)} "
        f"open_orders={len(open_orders)} cash_pct={cash_pct*100:.1f}%"
    )

    for sym, p in pos_by_sym.items():
        mv = float(p.get("market_value", 0))
        pl = float(p.get("unrealized_pl", 0))
        plpc = float(p.get("unrealized_plpc", 0)) * 100
        pct = (mv / equity * 100) if equity else 0
        log(f"[{name}] pos {sym}: qty={p.get('qty')} mv=${mv:,.2f} ({pct:.1f}%) p/l=${pl:,.2f} ({plpc:+.2f}%)")

    if alerts:
        for a in alerts:
            log(f"[{name}] ALERT: {a}")
    else:
        log(f"[{name}] risk checks clean")

    state[name] = {
        "last_check": now_utc().isoformat(),
        "equity": equity,
        "cash": cash,
        "buying_power": buying_power,
        "market_value": total_mv,
        "unrealized_pl": total_unrealized,
        "positions_count": len(positions),
        "open_orders_count": len(open_orders),
        "alerts": alerts,
    }


def main():
    log("=== alpaca heartbeat ===")
    state = load_state()
    for name, cfg in ACCOUNTS.items():
        check_account(name, cfg, state)
    save_state(state)
    log("=== alpaca heartbeat complete ===\n")


if __name__ == "__main__":
    main()
