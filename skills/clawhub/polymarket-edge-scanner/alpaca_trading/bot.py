#!/usr/bin/env python3
"""Alpaca paper-trading bot.

Runs hourly during market hours. Follows STRATEGY.md:
- Long-biased swing trading.
- Core ETF exposure (SPY/QQQ).
- Momentum large caps.
- Max 15% equity per position, 20% minimum cash, bracket orders.
"""

import json
import os
import sys
import subprocess
import datetime
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LOG_DIR = ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "bot.log"
TRADE_LOG = LOG_DIR / "trades.log"
STATE_FILE = LOG_DIR / "bot.state.json"

CREDS = json.load(open(os.path.expanduser("~/.alpaca/credentials.json")))
API_KEY = CREDS["api_key"]
API_SECRET = CREDS["api_secret"]
BASE = CREDS["base_url"]
DATA = CREDS.get("data_url", "https://data.alpaca.markets/v2")

WATCHLIST = {
    "core": ["SPY", "QQQ"],
    "momentum": ["AAPL", "GOOGL", "MSFT", "AMZN", "JPM", "GS", "TSM"],
}

MAX_POSITION_PCT = 0.15
MIN_CASH_PCT = 0.20
STOP_LOSS_PCT = 0.07
TAKE_PROFIT_PCT = 0.15
CORE_TARGET_PCT = 0.35


def log(msg):
    ts = datetime.datetime.now(datetime.timezone.utc).isoformat()
    line = f"[{ts}] {msg}"
    print(line)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")


def log_trade(msg):
    ts = datetime.datetime.now(datetime.timezone.utc).isoformat()
    line = f"[{ts}] {msg}"
    with open(TRADE_LOG, "a") as f:
        f.write(line + "\n")


def load_state():
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text())
        except Exception:
            pass
    return {}


def save_state(state):
    STATE_FILE.write_text(json.dumps(state, indent=2))


def today_str():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")


def alpaca_py(cmd):
    """Run the workspace alpaca.py CLI and return parsed JSON where possible."""
    full = ["python3", str(ROOT / "alpaca.py"), *cmd]
    result = subprocess.run(full, capture_output=True, text=True)
    if result.returncode != 0:
        log(f"alpaca.py error: {result.stderr.strip()}")
        return None
    return result.stdout.strip()


def api(method, path, **kwargs):
    import requests
    url = path if path.startswith("http") else BASE + path
    headers = {"APCA-API-KEY-ID": API_KEY, "APCA-API-SECRET-KEY": API_SECRET}
    r = requests.request(method, url, headers=headers, timeout=30, **kwargs)
    if r.status_code >= 400:
        log(f"API error {r.status_code}: {r.text}")
        return None
    return r.json() if r.text else {}


def market_open():
    clock = api("GET", "/clock")
    if not clock:
        return False
    return clock.get("is_open", False)


def get_account():
    return api("GET", "/account")


def get_positions():
    data = api("GET", "/positions")
    return {p["symbol"]: p for p in (data or [])}


def get_orders(status="open"):
    data = api("GET", "/orders", params={"status": status})
    return data or []


def get_quote(symbol):
    is_crypto = "/" in symbol
    if is_crypto:
        r = api("GET", "https://data.alpaca.markets/v1beta3/crypto/us/latest/trades", params={"symbols": symbol})
        if r and r.get("trades"):
            return float(r["trades"][symbol]["p"])
        return None
    r = api("GET", f"{DATA}/stocks/{symbol}/quotes/latest")
    if r and "quote" in r:
        return float(r["quote"].get("ap", r["quote"].get("bp", 0)))
    return None


def buy_bracket(symbol, notional, stop_pct=STOP_LOSS_PCT, profit_pct=TAKE_PROFIT_PCT):
    price = get_quote(symbol)
    if price is None or price <= 0:
        log(f"No quote for {symbol}; skipping")
        return None
    stop_price = round(price * (1 - stop_pct), 2)
    profit_price = round(price * (1 + profit_pct), 2)
    qty = max(1, int(notional / price))
    out = alpaca_py([
        "buy", symbol, str(qty),
        "--stop-loss", str(stop_price),
        "--take-profit", str(profit_price),
    ])
    log(f"BUY {symbol}: qty={qty} @ ~{price:.2f}, stop={stop_price}, target={profit_price}")
    log_trade(f"BUY {symbol} qty={qty} price={price:.2f} stop={stop_price} target={profit_price}")
    return out


def submit_order(side, symbol, qty, stop_loss=None, take_profit=None):
    body = {
        "symbol": symbol,
        "side": side,
        "type": "market",
        "time_in_force": "day",
        "qty": qty,
    }
    if stop_loss or take_profit:
        body["order_class"] = "bracket"
        if stop_loss:
            body["stop_loss"] = {"stop_price": str(stop_loss)}
        if take_profit:
            body["take_profit"] = {"limit_price": str(take_profit)}
    r = api("POST", "/orders", json=body)
    if r:
        log(f"Order {side} {symbol} qty={qty} id={r.get('id')}")
        log_trade(f"ORDER {side} {symbol} qty={qty} id={r.get('id')}")
    return r


def current_equity():
    acc = get_account()
    return float(acc.get("equity", 0)) if acc else 0


def current_cash():
    acc = get_account()
    return float(acc.get("cash", 0)) if acc else 0


def total_position_value(positions):
    return sum(float(p.get("market_value", 0)) for p in positions.values())


def run():
    log("=== bot run ===")
    state = load_state()
    today = today_str()

    if not market_open():
        log("Market closed. Exiting.")
        return

    account = get_account()
    if not account:
        log("Could not fetch account. Exiting.")
        return

    equity = float(account.get("equity", 0))
    cash = float(account.get("cash", 0))
    positions = get_positions()
    open_orders = get_orders("open")

    log(f"Equity={equity:.2f} cash={cash:.2f} positions={list(positions.keys())} open_orders={len(open_orders)}")

    # 1. Check existing positions for stop/target management.
    # Alpaca bracket orders handle stops automatically, so we just log status.
    for sym, p in positions.items():
        unrealized = float(p.get("unrealized_pl", 0))
        unrealized_pct = float(p.get("unrealized_plpc", 0)) * 100
        log(f"Position {sym}: qty={p.get('qty')} mv={p.get('market_value')} p/l={unrealized:.2f} ({unrealized_pct:.2f}%)")

    # 2. Build core ETF exposure if underweight and cash allows.
    # Limit core additions to once per day to avoid deploying cash too fast.
    core_value = sum(float(positions.get(s, {}).get("market_value", 0)) for s in WATCHLIST["core"])
    core_pct = core_value / equity if equity else 0
    last_core_date = state.get("last_core_add_date")
    if last_core_date != today and core_pct < CORE_TARGET_PCT and cash / equity > MIN_CASH_PCT:
        target_add = min(
            (CORE_TARGET_PCT - core_pct) * equity,
            cash - equity * MIN_CASH_PCT,
            equity * MAX_POSITION_PCT,
        )
        if target_add > 1000:
            # Split add between SPY and QQQ, favoring SPY.
            spy_add = target_add * 0.6
            qqq_add = target_add * 0.4
            traded = False
            if "SPY" not in positions or float(positions.get("SPY", {}).get("market_value", 0)) < equity * 0.20:
                buy_bracket("SPY", spy_add)
                traded = True
            if "QQQ" not in positions or float(positions.get("QQQ", {}).get("market_value", 0)) < equity * 0.10:
                buy_bracket("QQQ", qqq_add)
                traded = True
            if traded:
                state["last_core_add_date"] = today

    # 3. Add a momentum position if we have cash and fewer than 5 positions.
    # Limit momentum additions to one new name per day.
    last_momentum_date = state.get("last_momentum_add_date")
    if last_momentum_date != today and len(positions) < 5 and cash / equity > MIN_CASH_PCT:
        available = min(equity * MAX_POSITION_PCT, cash - equity * MIN_CASH_PCT)
        if available > 2000:
            for sym in WATCHLIST["momentum"]:
                if sym not in positions:
                    buy_bracket(sym, available)
                    state["last_momentum_add_date"] = today
                    break

    save_state(state)
    log("=== bot run complete ===\n")


if __name__ == "__main__":
    run()
