#!/usr/bin/env python3
"""Quick status view for the day-trader account."""
import json
import requests
from datetime import datetime, timezone

CREDS = json.load(open("/root/.alpaca/credentials.daytrader.json"))
H = {"APCA-API-KEY-ID": CREDS["api_key"], "APCA-API-SECRET-KEY": CREDS["api_secret"]}
BASE = CREDS["base_url"]

def fmt(x):
    return f"${float(x):,.2f}"

print("Day Trader Account:", datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"))
a = requests.get(BASE + "/account", headers=H, timeout=30).json()
print(f"  equity={fmt(a['equity'])} cash={fmt(a['cash'])} bp={fmt(a['buying_power'])} day_trade_count={a.get('daytrade_count', 'N/A')}")
print()
print("Positions:")
positions = requests.get(BASE + "/positions", headers=H, timeout=30).json()
if not positions:
    print("  none")
for p in positions:
    pl = float(p["unrealized_pl"])
    plpct = float(p["unrealized_plpc"]) * 100
    print(f"  {p['symbol']:>6} qty={p['qty']:>4} avg={fmt(p['avg_entry_price']):>12} now={fmt(p['current_price']):>12} "
          f"PL={fmt(pl):>10} ({plpct:+.2f}%)")
print()
print("Open orders:")
orders = requests.get(BASE + "/orders", headers=H, params={"status": "open", "nested": "true"}, timeout=30).json()
if not orders:
    print("  none")
for o in orders:
    leg_info = ""
    for l in (o.get("legs") or []):
        leg_info += f" | leg {l['side']} {l['type']} @ {l.get('limit_price') or l.get('stop_price')} ({l['status']})"
    print(f"  {o['id'][:8]} {o['symbol']:>6} {o['side']:>4} {o['type']:>6} @ "
          f"{o.get('limit_price') or o.get('stop_price') or 'mkt'}{leg_info}")
