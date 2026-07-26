#!/usr/bin/env python3
"""Alpaca day-trading bot for the $5k paper account.

Reads credentials from ~/.alpaca/credentials.daytrader.json.
Trades only NYSE-listed liquid stocks/ETFs, flat by close.
"""

import json
import os
import sys
import math
import time
import datetime
from pathlib import Path
from collections import defaultdict

import requests

ROOT = Path(__file__).resolve().parent
LOG_DIR = ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "daytrader.log"
TRADE_LOG = LOG_DIR / "daytrader-trades.log"
STATE_FILE = LOG_DIR / "daytrader.state.json"

CREDS_PATH = os.path.expanduser("~/.alpaca/credentials.daytrader.json")
CREDS = json.load(open(CREDS_PATH))
API_KEY = CREDS["api_key"]
API_SECRET = CREDS["api_secret"]
BASE = CREDS["base_url"]
DATA = CREDS.get("data_url", "https://data.alpaca.markets/v2")

# NYSE-listed liquid names only
UNIVERSE = [
    # Index / macro ETFs
    "SPY", "DIA", "IWM", "QQQ",
    # Sector / commodity ETFs
    "XLF", "XLE", "XLK", "XLU", "XLI", "XLP", "XBI", "GLD", "SLV", "USO", "VOO", "VTI",
    # Banks / financials
    "JPM", "BAC", "WFC", "GS", "MS", "C", "AXP",
    # Energy
    "XOM", "CVX",
    # Consumer / staples / discretionary
    "WMT", "HD", "DIS", "KO", "PEP", "MCD", "NKE",
    # Telecom
    "VZ", "T",
    # Healthcare
    "UNH", "JNJ", "PFE", "MRK",
    # Industrials / tech
    "CAT", "BA", "GE", "HON", "MMM", "IBM", "ORCL", "V", "MA",
]

# Strategy parameters
MAX_POSITIONS = 3
MIN_CASH_PCT = 0.30
POSITION_SIZE_MIN = 500
POSITION_SIZE_MAX = 1000
OPENING_RANGE_MINUTES = 15
FLAT_BEFORE_CLOSE_ET = datetime.time(15, 55)  # 15:55 ET / 19:55 UTC
ET_TZ = datetime.timezone(datetime.timedelta(hours=-4), "EDT")  # approximate; NYSE uses ET

# Stop/target multipliers
STOP_PCT_ETF = 0.008
STOP_PCT_STOCK = 0.012
PROFIT_RATIO = 2.0

# Friction guard: reject entries where the quoted spread is too wide,
# and assume slippage when computing the effective entry, stop, and size.
MAX_SPREAD_PCT = 0.005
SLIPPAGE_PCT = 0.0015


def now_utc():
    return datetime.datetime.now(datetime.timezone.utc)


def et_now():
    # Use UTC-4 as a close enough approximation for NYSE EDT. This bot is not
    # sensitive to the exact DST boundary; flat-by-close uses ET clock.
    return now_utc().astimezone(ET_TZ)


def log(msg):
    ts = now_utc().isoformat()
    line = f"[{ts}] {msg}"
    print(line)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")


def log_trade(msg):
    ts = now_utc().isoformat()
    line = f"[{ts}] {msg}"
    with open(TRADE_LOG, "a") as f:
        f.write(line + "\n")


def load_state():
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text())
        except Exception as e:
            log(f"state load error: {e}")
    return {
        "day_trade_count": 0,
        "last_flat_date": None,
        "daily_stats": {},
    }


def save_state(state):
    STATE_FILE.write_text(json.dumps(state, indent=2))


def api(method, path, **kwargs):
    url = path if path.startswith("http") else BASE + path
    headers = {"APCA-API-KEY-ID": API_KEY, "APCA-API-SECRET-KEY": API_SECRET}
    try:
        r = requests.request(method, url, headers=headers, timeout=30, **kwargs)
    except Exception as e:
        log(f"request error: {e}")
        return None
    if r.status_code >= 400:
        log(f"API error {r.status_code}: {r.text}")
        return None
    return r.json() if r.text else {}


def data_api(method, path, **kwargs):
    url = path if path.startswith("http") else DATA + path
    headers = {"APCA-API-KEY-ID": API_KEY, "APCA-API-SECRET-KEY": API_SECRET}
    try:
        r = requests.request(method, url, headers=headers, timeout=30, **kwargs)
    except Exception as e:
        log(f"data request error: {e}")
        return None
    if r.status_code >= 400:
        log(f"data API error {r.status_code}: {r.text}")
        return None
    return r.json() if r.text else {}


def market_open():
    c = api("GET", "/clock")
    return c.get("is_open", False) if c else False


def get_account():
    return api("GET", "/account")


def get_positions():
    data = api("GET", "/positions")
    return {p["symbol"]: p for p in (data or [])}


def get_orders(status="open"):
    return api("GET", "/orders", params={"status": status, "limit": 100}) or []


def count_day_trades():
    """Count same-day round trips in the last 5 market days (PDT window).
    Simple count: a buy and sell of the same symbol on the same calendar day.
    """
    since = (now_utc() - datetime.timedelta(days=7)).isoformat()
    orders = api("GET", "/orders", params={"status": "closed", "after": since, "limit": 500})
    if not orders:
        return 0
    buys = defaultdict(set)
    sells = defaultdict(set)
    for o in orders:
        if o.get("status") != "filled":
            continue
        sym = o.get("symbol")
        side = o.get("side")
        filled = o.get("filled_at")
        if not sym or not filled:
            continue
        day = filled[:10]
        if side == "buy":
            buys[sym].add(day)
        elif side == "sell":
            sells[sym].add(day)
    count = 0
    for sym in buys:
        count += len(buys[sym] & sells[sym])
    return count


def get_latest_trade(symbol):
    r = data_api("GET", f"/stocks/{symbol}/trades/latest")
    if r and "trade" in r:
        return float(r["trade"]["p"])
    return None


def get_latest_quote(symbol):
    r = data_api("GET", f"/stocks/{symbol}/quotes/latest")
    if r and "quote" in r:
        q = r["quote"]
        return {
            "bid": float(q.get("bp", 0)),
            "ask": float(q.get("ap", 0)),
            "bid_size": int(q.get("bs", 0)),
            "ask_size": int(q.get("as", 0)),
        }
    return None


def get_bars(symbol, timeframe="1Min", start=None, end=None, feed="iex"):
    """Fetch bars. start/end should be ISO 8601 UTC strings."""
    params = {"timeframe": timeframe, "feed": feed}
    if start:
        params["start"] = start
    if end:
        params["end"] = end
    r = data_api("GET", f"/stocks/{symbol}/bars", params=params)
    return r.get("bars", []) if r else []


def get_opening_range(symbol, date_utc):
    """Return opening range high/low and VWAP for the first N minutes."""
    market_open = date_utc.strftime("%Y-%m-%dT13:30:00Z")
    range_end = date_utc.strftime("%Y-%m-%dT13:45:00Z")
    bars = get_bars(symbol, "1Min", start=market_open, end=range_end)
    if not bars:
        return None
    highs = [b["h"] for b in bars]
    lows = [b["l"] for b in bars]
    total_pv = sum(b["v"] * b["vw"] for b in bars)
    total_v = sum(b["v"] for b in bars)
    return {
        "high": max(highs),
        "low": min(lows),
        "vwap": total_pv / total_v if total_v else (bars[0]["c"]),
        "open": bars[0]["o"],
        "close": bars[-1]["c"],
        "bars": bars,
    }


def is_etf(symbol):
    return len(symbol) <= 4 and symbol in {"SPY", "DIA", "IWM", "QQQ", "XLF", "XLE", "XLK", "XLU", "XLI", "XLP", "XBI", "GLD", "SLV", "USO", "VOO", "VTI", "HYG", "LQD", "EEM"}


def place_bracket_buy(symbol, qty, entry_price, stop_price, profit_price):
    body = {
        "symbol": symbol,
        "side": "buy",
        "type": "limit",
        "time_in_force": "day",
        "qty": str(qty),
        "limit_price": f"{entry_price:.2f}",
        "order_class": "bracket",
        "stop_loss": {"stop_price": f"{stop_price:.2f}"},
        "take_profit": {"limit_price": f"{profit_price:.2f}"},
    }
    r = api("POST", "/orders", json=body)
    if r:
        log(f"ORDER {symbol}: BUY qty={qty} limit={entry_price:.2f} stop={stop_price:.2f} target={profit_price:.2f} id={r.get('id')}")
        log_trade(f"BUY {symbol} qty={qty} entry={entry_price:.2f} stop={stop_price:.2f} target={profit_price:.2f} id={r.get('id')}")
    return r


def place_market_buy(symbol, qty, stop_price, profit_price):
    body = {
        "symbol": symbol,
        "side": "buy",
        "type": "market",
        "time_in_force": "day",
        "qty": str(qty),
        "order_class": "bracket",
        "stop_loss": {"stop_price": f"{stop_price:.2f}"},
        "take_profit": {"limit_price": f"{profit_price:.2f}"},
    }
    r = api("POST", "/orders", json=body)
    if r:
        log(f"ORDER {symbol}: BUY MARKET qty={qty} stop={stop_price:.2f} target={profit_price:.2f} id={r.get('id')}")
        log_trade(f"BUY {symbol} qty={qty} entry=MARKET stop={stop_price:.2f} target={profit_price:.2f} id={r.get('id')}")
    return r


def close_position(symbol, qty=None):
    if qty:
        body = {"qty": str(qty)}
        r = api("DELETE", f"/positions/{symbol}", json=body)
    else:
        r = api("DELETE", f"/positions/{symbol}")
    if r:
        log(f"CLOSE {symbol}: flat order id={r.get('id', r)}")
        log_trade(f"CLOSE {symbol} id={r.get('id', r)}")
    return r


def cancel_all_orders():
    r = api("DELETE", "/orders")
    if r is not None:
        log("cancelled all open orders")
    return r


def calculate_position_size(price, cash):
    target = min(POSITION_SIZE_MAX, max(POSITION_SIZE_MIN, cash * 0.15))
    qty = int(target / price)
    return max(1, qty)


def scan_signals():
    """Return candidate signals for each symbol in universe."""
    date_utc = now_utc().date()
    candidates = []
    for symbol in UNIVERSE:
        try:
            or_ = get_opening_range(symbol, date_utc)
            if not or_:
                continue
            latest = get_latest_trade(symbol)
            if latest is None:
                continue
            quote = get_latest_quote(symbol)
            spread = (quote["ask"] - quote["bid"]) if quote else 0
            range_high = or_["high"]
            range_low = or_["low"]
            range_size = range_high - range_low
            if range_size <= 0:
                continue
            # Breakout above opening range
            above_range = latest > range_high
            # Pullback to VWAP bounce (price near vwap and above range low)
            near_vwap = abs(latest - or_["vwap"]) / or_["vwap"] < 0.0015
            # Only long if breakout or vwap bounce in overall higher direction
            if above_range:
                signal = "opening_range_breakout"
                strength = (latest - range_high) / range_size
            elif near_vwap and latest > range_low + 0.3 * range_size:
                signal = "vwap_bounce"
                strength = 0.5
            else:
                continue
            candidates.append({
                "symbol": symbol,
                "signal": signal,
                "price": latest,
                "range_high": range_high,
                "range_low": range_low,
                "vwap": or_["vwap"],
                "strength": strength,
                "spread": spread,
            })
        except Exception as e:
            log(f"scan error {symbol}: {e}")
    # Sort by strength desc
    candidates.sort(key=lambda x: x["strength"], reverse=True)
    return candidates


def run():
    log("=== daytrader run ===")
    state = load_state()

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
    et = et_now()

    log(f"Equity=${equity:,.2f} cash=${cash:,.2f} positions={list(positions.keys())} open_orders={len(open_orders)} ET={et.strftime('%H:%M')}")

    # 1. Flatten before close
    if et.time() >= FLAT_BEFORE_CLOSE_ET and positions:
        log("Flattening before close.")
        for sym in list(positions.keys()):
            close_position(sym)
        cancel_all_orders()
        state["last_flat_date"] = str(et.date())
        save_state(state)
        return

    # 2. Manage existing positions: move stop to breakeven when +1R
    # Alpaca bracket orders handle stop/target automatically, so we just log.
    for sym, p in positions.items():
        unrealized = float(p.get("unrealized_pl", 0))
        unrealized_pct = float(p.get("unrealized_plpc", 0)) * 100
        log(f"Position {sym}: qty={p.get('qty')} mv=${float(p.get('market_value', 0)):,.2f} p/l=${unrealized:,.2f} ({unrealized_pct:+.2f}%)")

    # 3. Cancel stale unfilled entry orders (>5 min old)
    for o in open_orders:
        if o["side"] == "buy" and o["status"] == "new" and o["type"] == "limit":
            submitted = o.get("submitted_at")
            if submitted:
                submitted_dt = datetime.datetime.fromisoformat(submitted.replace("Z", "+00:00"))
                age_min = (now_utc() - submitted_dt).total_seconds() / 60
                if age_min > 5:
                    api("DELETE", f"/orders/{o['id']}")
                    log(f"Cancelled stale entry order {o['id']} for {o['symbol']}")

    # 4. Scan for new entries if capacity exists
    open_position_count = len(positions)
    available_slots = MAX_POSITIONS - open_position_count
    min_cash_required = equity * MIN_CASH_PCT
    if available_slots <= 0:
        log("At max positions. Skipping scan.")
        save_state(state)
        return
    if cash <= min_cash_required:
        log(f"Cash ${cash:,.2f} below minimum ${min_cash_required:,.2f}. Skipping scan.")
        save_state(state)
        return

    # Don't enter new trades in last 30 minutes before close
    if et.time() >= (datetime.datetime.combine(datetime.date.today(), FLAT_BEFORE_CLOSE_ET) - datetime.timedelta(minutes=30)).time():
        log("Too close to close for new entries.")
        save_state(state)
        return

    # PDT guard: sub-$25k accounts are limited to 3 day trades per 5 rolling days.
    day_trades = count_day_trades()
    log(f"Day trades in last 5 days: {day_trades}")
    if day_trades >= 3:
        log("PDT limit reached. No new entries.")
        save_state(state)
        return

    candidates = scan_signals()
    if not candidates:
        log("No signals.")
        save_state(state)
        return

    # Pick top candidates not already held or ordered
    held = set(positions.keys())
    ordered_symbols = {o["symbol"] for o in open_orders}
    for cand in candidates:
        if available_slots <= 0:
            break
        sym = cand["symbol"]
        if sym in held or sym in ordered_symbols:
            continue
        latest = cand["price"]
        if latest is None or latest <= 0:
            continue

        # Friction guard: skip if the quoted spread is too wide, and assume
        # slippage when sizing and placing bracket stops so a bad fill does
        # not immediately violate the intended risk.
        spread = cand.get("spread", 0)
        if latest > 0 and spread / latest > MAX_SPREAD_PCT:
            log(f"Skipping {sym}: spread {spread/latest*100:.2f}% > max {MAX_SPREAD_PCT*100:.2f}%")
            continue

        entry_estimate = latest * (1 + SLIPPAGE_PCT)
        stop_pct = STOP_PCT_ETF if is_etf(sym) else STOP_PCT_STOCK
        stop_price = round(entry_estimate * (1 - stop_pct), 2)
        profit_price = round(entry_estimate + PROFIT_RATIO * (entry_estimate - stop_price), 2)
        qty = calculate_position_size(entry_estimate, cash - min_cash_required)
        if qty < 1:
            continue
        notional = qty * entry_estimate
        if notional < POSITION_SIZE_MIN:
            continue
        if notional > POSITION_SIZE_MAX:
            qty = int(POSITION_SIZE_MAX / entry_estimate)
            notional = qty * entry_estimate
        if notional > cash - min_cash_required:
            qty = int((cash - min_cash_required) / entry_estimate)
            notional = qty * entry_estimate
        if qty < 1 or notional < POSITION_SIZE_MIN:
            continue

        log(f"Signal {cand['signal']} for {sym}: last={latest:.2f} range=[{cand['range_low']:.2f},{cand['range_high']:.2f}] vwap={cand['vwap']:.2f}")
        place_market_buy(sym, qty, stop_price, profit_price)
        available_slots -= 1
        held.add(sym)

    save_state(state)
    log("=== daytrader run complete ===\n")


if __name__ == "__main__":
    run()
