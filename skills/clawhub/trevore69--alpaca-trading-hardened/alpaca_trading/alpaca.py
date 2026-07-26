#!/usr/bin/env python3
"""Minimal Alpaca paper-trading CLI.

Usage:
  python3 alpaca.py account
  python3 alpaca.py positions
  python3 alpaca.py orders [--status open|closed|all]
  python3 alpaca.py quote SYMBOL [SYMBOL...]
  python3 alpaca.py buy SYMBOL QTY [--notional] [--limit PRICE] [--stop-loss PRICE] [--take-profit PRICE] [--extended]
  python3 alpaca.py sell SYMBOL QTY [--limit PRICE] [--stop-loss PRICE] [--take-profit PRICE] [--extended]
  python3 alpaca.py close SYMBOL
  python3 alpaca.py cancel ORDER_ID | --all
  python3 alpaca.py clock

Reads credentials from ~/.alpaca/credentials.json.
Crypto symbols use slash form on the command line, e.g. BTC/USD.
"""
import json
import sys
import os
import requests

CREDS_PATH = os.path.expanduser("~/.alpaca/credentials.json")


def load():
    with open(CREDS_PATH) as f:
        return json.load(f)


C = load()
HEADERS = {"APCA-API-KEY-ID": C["api_key"], "APCA-API-SECRET-KEY": C["api_secret"]}
BASE = C["base_url"]
DATA = C.get("data_url", "https://data.alpaca.markets/v2")


def req(method, path, **kw):
    url = path if path.startswith("http") else BASE + path
    r = requests.request(method, url, headers=HEADERS, timeout=30, **kw)
    if r.status_code >= 400:
        print(f"ERROR {r.status_code}: {r.text}", file=sys.stderr)
        sys.exit(1)
    return r.json() if r.text else {}


def fmt_money(x):
    return f"${float(x):,.2f}"


def cmd_account():
    a = req("GET", "/account")
    print(f"status={a['status']} equity={fmt_money(a['equity'])} cash={fmt_money(a['cash'])} "
          f"buying_power={fmt_money(a['buying_power'])} portfolio={fmt_money(a['portfolio_value'])} "
          f"last_equity={fmt_money(a['last_equity'])}")


def cmd_positions():
    ps = req("GET", "/positions")
    if not ps:
        print("no open positions")
        return
    total_pl = 0.0
    for p in ps:
        pl = float(p["unrealized_pl"])
        total_pl += pl
        print(f"{p['symbol']:>10} qty={p['qty']:>10} avg={fmt_money(p['avg_entry_price']):>12} "
              f"now={fmt_money(p['current_price']):>12} value={fmt_money(p['market_value']):>12} "
              f"uPL={fmt_money(pl):>10} ({float(p['unrealized_plpc'])*100:+.2f}%)")
    print(f"TOTAL unrealized P/L: {fmt_money(total_pl)}")


def cmd_orders(status):
    ps = {"status": status, "limit": 50, "nested": "true"}
    os_ = req("GET", "/orders", params=ps)
    if not os_:
        print(f"no {status} orders")
        return
    for o in os_:
        leg = ""
        if o.get("legs"):
            for l in o["legs"]:
                leg += f" | leg {l['side']} {l['type']} @ {l.get('limit_price') or l.get('stop_price')}"
        print(f"{o['id'][:8]} {o['symbol']:>10} {o['side']:>4} {o.get('qty') or o.get('notional')} "
              f"{o['type']} @ {o.get('limit_price') or o.get('stop_price') or 'mkt'} "
              f"status={o['status']} filled_avg={o.get('filled_avg_price')}{leg}")


def cmd_quote(symbols):
    # crypto vs stocks
    stocks = [s for s in symbols if "/" not in s]
    cryptos = [s for s in symbols if "/" in s]
    for s in stocks:
        try:
            q = req("GET", f"{DATA}/stocks/{s}/snapshot")
            latest = q.get("latestTrade", {}).get("p")
            prev = q.get("prevDailyBar", {}).get("c")
            chg = (latest / prev - 1) * 100 if latest and prev else 0
            print(f"{s:>10}: {fmt_money(latest)} ({chg:+.2f}% vs prev close)")
        except SystemExit:
            print(f"{s:>10}: quote failed")
    if cryptos:
        syms = ",".join(cryptos)
        try:
            q = req("GET", "https://data.alpaca.markets/v1beta3/crypto/us/latest/trades", params={"symbols": syms})
            for sym, t in q.get("trades", {}).items():
                print(f"{sym:>10}: {fmt_money(t['p'])}")
        except SystemExit:
            print("crypto quote failed")


def parse_order_args(args):
    opts = {"limit": None, "sl": None, "tp": None, "notional": False, "extended": False, "tif": "day"}
    i = 0
    while i < len(args):
        a = args[i]
        if a == "--limit":
            opts["limit"] = args[i + 1]; i += 2
        elif a == "--stop-loss":
            opts["sl"] = args[i + 1]; i += 2
        elif a == "--take-profit":
            opts["tp"] = args[i + 1]; i += 2
        elif a == "--notional":
            opts["notional"] = True; i += 1
        elif a == "--extended":
            opts["extended"] = True; i += 1
        else:
            i += 1
    return opts


def cmd_order(side, symbol, qty, args):
    o = parse_order_args(args)
    is_crypto = "/" in symbol
    body = {
        "symbol": symbol.replace("/", "") if is_crypto else symbol,
        "side": side,
        "time_in_force": "gtc" if is_crypto else o["tif"],
    }
    if is_crypto:
        body["symbol"] = symbol  # alpaca accepts BTC/USD form
    if o["notional"]:
        body["notional"] = qty
    else:
        body["qty"] = qty
    if o["limit"]:
        body["type"] = "limit"
        body["limit_price"] = o["limit"]
        if o["extended"]:
            body["extended_hours"] = True
    elif o["sl"] or o["tp"]:
        body["type"] = "market"
    else:
        body["type"] = "market"
        if o["extended"]:
            print("market orders cannot use extended hours; use --limit", file=sys.stderr)
            sys.exit(1)
    if o["sl"] or o["tp"]:
        body["order_class"] = "bracket"
        if o["sl"]:
            body["stop_loss"] = {"stop_price": o["sl"]}
        if o["tp"]:
            body["take_profit"] = {"limit_price": o["tp"]}
    r = req("POST", "/orders", json=body)
    print(f"OK {r['side']} {r['symbol']} qty={r.get('qty') or r.get('notional')} "
          f"type={r['type']} class={r.get('order_class')} status={r['status']} id={r['id']}")


def cmd_close(symbol):
    r = req("DELETE", f"/positions/{symbol}")
    print(f"close order placed: {r.get('id', r)}")


def cmd_cancel(arg):
    if arg == "--all":
        req("DELETE", "/orders")
        print("all open orders cancelled")
    else:
        req("DELETE", f"/orders/{arg}")
        print(f"cancelled {arg}")


def cmd_clock():
    c = req("GET", "/clock")
    print(f"open={c['is_open']} next_open={c['next_open']} next_close={c['next_close']} now={c['timestamp']}")


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return
    cmd = args[0]
    if cmd == "account":
        cmd_account()
    elif cmd == "positions":
        cmd_positions()
    elif cmd == "orders":
        st = "open"
        if "--status" in args:
            st = args[args.index("--status") + 1]
        cmd_orders(st)
    elif cmd == "quote":
        cmd_quote(args[1:])
    elif cmd in ("buy", "sell"):
        cmd_order(cmd, args[1], args[2], args[3:])
    elif cmd == "close":
        cmd_close(args[1])
    elif cmd == "cancel":
        cmd_cancel(args[1])
    elif cmd == "clock":
        cmd_clock()
    else:
        print(f"unknown command: {cmd}")
        print(__doc__)


if __name__ == "__main__":
    main()
