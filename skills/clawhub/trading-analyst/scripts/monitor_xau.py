#!/usr/bin/env python3
"""
monitor_xau.py — terapkan skill trading-analyst (S&R + S/D) TIAP MENIT.

Loop tiap 60 detik:
  1. Fetch harga XAU/USD live (gold-api).
  2. Fetch indikator REAL dari Twelve Data (RSI/EMA/SMA harian, cache 10 mnt).
  3. Baca level target dari analysis_log.jsonl (entry/SL/TP terakhir).
  4. Cek: harga menyentuh level kunci + RSI overbought/oversold.
  5. Tulis tick ke memory/trading/tick_log.jsonl (silent, tiap menit).
  6. Bila level tersentuh / RSI ekstrem / bias berubah -> alert ke alerts.jsonl + print.

Tujuannya: uji skill secara berkesinambungan tanpa spam chat.
Hanya alert (bukan tick) yang diteruskan ke pengguna.

Key Twelve Data dibaca dari env TWELVE_DATA_API_KEY atau memory/trading/api_keys.md.
Key TIDAK PERNAH di-print.

Usage:
  python3 monitor_xau.py            # loop tiap menit (background)
  python3 monitor_xau.py --once    # satu iterasi (test)

No secrets printed, no network mutation, no destructive ops.
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone

WS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# ^ 4 dirname dari skills/trading-analyst/scripts/file -> workspace
TRADING = os.path.join(WS, "memory", "trading")
TICK = os.path.join(TRADING, "tick_log.jsonl")
ALERTS = os.path.join(TRADING, "alerts.jsonl")
ANALYSIS = os.path.join(TRADING, "analysis_log.jsonl")
IND_CACHE = os.path.join(TRADING, "ind_cache.json")
GOLDAPI = "https://api.gold-api.com/price/XAU"


def _workspace():
    return WS


def load_twelve_key():
    """Ambil key dari memory/trading/api_keys.md (lokal privat). Tidak di-print."""
    p = os.path.join(TRADING, "api_keys.md")
    try:
        with open(p, encoding="utf-8") as f:
            for line in f:
                m = re.search(r"Key:\s*([a-f0-9]{32})", line)
                if m:
                    return m.group(1)
    except FileNotFoundError:
        return None
    return None


def http_get(url, timeout=15):
    req = urllib.request.Request(url, headers={"User-Agent": "clara-monitor/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def fetch_price():
    try:
        return float(http_get(GOLDAPI).get("price", 0))
    except Exception:
        return None


def rsi(values, period=14):
    if len(values) <= period:
        return None
    gains = losses = 0.0
    for i in range(1, period + 1):
        d = values[-i] - values[-i - 1]
        if d >= 0:
            gains += d
        else:
            losses -= d
    gains /= period
    losses /= period
    if losses == 0:
        return 100.0
    return 100.0 - (100.0 / (1 + gains / losses))


def ema(values, period):
    if len(values) < period:
        return None
    k = 2.0 / (period + 1)
    prev = sum(values[:period]) / period
    for v in values[period:]:
        prev = v * k + prev * (1 - k)
    return prev


def sma(values, period):
    if len(values) < period:
        return None
    return sum(values[-period:]) / period


def fetch_indicators_twelvedata(key, cache_sec=600):
    """Indikator harian dari Twelve Data. Cache 10 mnt agar hemat kuota (800/hari)."""
    now = time.time()
    if os.path.exists(IND_CACHE):
        try:
            if now - os.path.getmtime(IND_CACHE) < cache_sec:
                with open(IND_CACHE, encoding="utf-8") as f:
                    return json.load(f)
        except Exception:
            pass
    if not key:
        return None
    base = "https://api.twelvedata.com"
    try:
        ts = http_get(f"{base}/time_series?symbol=XAU/USD&interval=1day&outputsize=60&apikey={key}")
        closes = [float(c["close"]) for c in ts.get("values", [])][::-1]
        out = {}
        if closes:
            out["rsi14"] = rsi(closes)
            out["ema20"] = ema(closes, 20)
            out["sma50"] = sma(closes, 50)
            out["sma200"] = sma(closes, 200)
            out["last_close"] = closes[-1]
            try:
                with open(IND_CACHE, "w", encoding="utf-8") as f:
                    json.dump(out, f)
            except Exception:
                pass
        return out
    except Exception as e:
        print(f"[warn] twelvedata failed: {e}", file=sys.stderr)
        return None


def load_targets():
    targets = []
    try:
        with open(ANALYSIS, encoding="utf-8") as f:
            lines = [l for l in f if l.strip()]
        if lines:
            last = json.loads(lines[-1])
            for lv in last.get("levels", []):
                targets.append({
                    "name": lv.get("type", "?"),
                    "entry": float(lv.get("entry", 0)),
                    "sl": float(lv.get("sl", 0)),
                    "tp": float(lv.get("tp", 0)),
                })
    except FileNotFoundError:
        pass
    return targets


def bias_of(price):
    if price >= 4545:
        return "bullish (breakout > Resistance)"
    if price <= 4400:
        return "bearish (breakdown < Support)"
    return "neutral (range 4400-4545)"


# Level kunci statis (dari analisa S&R + S/D terakhir)
KEY_LEVELS = [
    {"name": "Resistance/Supply", "price": 4545.0, "kind": "resistance"},
    {"name": "Breakout entry", "price": 4550.0, "kind": "buy_stop"},
    {"name": "Support/Demand", "price": 4400.0, "kind": "support"},
    {"name": "Support bawah", "price": 4345.0, "kind": "support"},
]


def check_alerts(price, r, state):
    alerts = []
    # RSI ekstrem (hanya alert sekali per episode)
    if r is not None:
        if r >= 70 and "rsi_ob" not in state["fired"]:
            alerts.append(f"RSI OVERBOUGHT: {r:.1f} (rawan rejection di supply)")
            state["fired"].add("rsi_ob")
        if r <= 30 and "rsi_os" not in state["fired"]:
            alerts.append(f"RSI OVERSOLD: {r:.1f} (rawan bounce di demand)")
            state["fired"].add("rsi_os")
        if 30 < r < 70:
            state["fired"].discard("rsi_ob")
            state["fired"].discard("rsi_os")
    # target entry triggers
    for t in state["targets"]:
        key = f"entry_{t['name']}_{t['entry']}"
        if key in state["fired"]:
            continue
        trig = False
        if t["name"] in ("BUY_STOP",):
            trig = price >= t["entry"]
        elif t["name"] in ("BUY_LIMIT",):
            trig = price <= t["entry"]
        elif t["name"] in ("SELL_LIMIT",):
            trig = price >= t["entry"]
        if trig:
            alerts.append(f"ENTRY TERSEDIA: {t['name']} @ {t['entry']} (SL {t['sl']} TP {t['tp']})")
            state["fired"].add(key)
    # key level touch
    for kl in KEY_LEVELS:
        key = f"level_{kl['name']}"
        if key in state["fired"]:
            continue
        if abs(price - kl["price"]) <= 2.0:
            side = "menyentuh RESISTANCE" if kl["kind"] == "resistance" else "menyentuh SUPPORT"
            alerts.append(f"HARGA {side}: {kl['name']} @ {kl['price']}")
            state["fired"].add(key)
    return alerts


def tick(once):
    price = fetch_price()
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    state = tick.__dict__.get("state")
    if state is None:
        state = {"targets": load_targets(), "fired": set(), "last_bias": None}
        tick.__dict__["state"] = state

    if price is None:
        print(f"[{ts}] fetch gagal, skip", file=sys.stderr)
        return

    bias = bias_of(price)
    bias_changed = bias != state["last_bias"]
    state["last_bias"] = bias

    # indikator REAL dari Twelve Data (cache 10 mnt)
    key = os.environ.get("TWELVE_DATA_API_KEY") or load_twelve_key()
    ind = fetch_indicators_twelvedata(key)
    r = ind.get("rsi14") if ind else None
    e = ind.get("ema20") if ind else None
    s50 = ind.get("sma50") if ind else None
    s200 = ind.get("sma200") if ind else None

    ind_note = ""
    if r is not None:
        ind_note = f" | RSI {r:.1f}"
        if r >= 70:
            ind_note += " (OB)"
        elif r <= 30:
            ind_note += " (OS)"
    if e is not None:
        ind_note += f" | EMA20 {e:.0f}"
    if s50 is not None:
        ind_note += f" | SMA50 {s50:.0f}"

    os.makedirs(TRADING, exist_ok=True)
    with open(TICK, "a", encoding="utf-8") as f:
        f.write(json.dumps({
            "ts": ts, "price": price, "bias": bias,
            "rsi": round(r, 1) if r is not None else None,
            "ema20": round(e, 2) if e is not None else None,
            "sma50": round(s50, 2) if s50 is not None else None,
            "sma200": round(s200, 2) if s200 is not None else None,
        }) + "\n")

    line = f"[{ts}] XAU {price:.2f} | bias: {bias}{ind_note}"
    alerts = check_alerts(price, r, state)
    if alerts:
        for a in alerts:
            print(f"ALERT {ts}: {a}", file=sys.stderr)
            with open(ALERTS, "a", encoding="utf-8") as f:
                f.write(json.dumps({"ts": ts, "alert": a, "price": price,
                                     "rsi": round(r, 1) if r is not None else None}) + "\n")
        line += f" | ALERTS: {len(alerts)}"
    elif bias_changed:
        print(f"BIAS CHANGE {ts}: {bias}", file=sys.stderr)
    print(line, file=sys.stderr if once else sys.stdout)

    if once:
        print(f"[once] done. price={price}, bias={bias}, rsi={r}, targets={len(state['targets'])}")


def main():
    p = argparse.ArgumentParser(description="Monitor XAU/USD tiap menit (S&R + S/D + indikator REAL).")
    p.add_argument("--once", action="store_true", help="Jalankan satu iterasi lalu keluar")
    p.add_argument("--interval", type=int, default=60, help="Detik antar cek (default 60)")
    args = p.parse_args()

    if args.once:
        tick(True)
        return

    print(f"Monitor XAU start (interval {args.interval}s, indikator REAL Twelve Data). Tick -> {TICK}, Alert -> {ALERTS}",
          file=sys.stderr)
    while True:
        try:
            tick(False)
        except Exception as e:
            print(f"[err] {e}", file=sys.stderr)
        time.sleep(args.interval)


if __name__ == "__main__":
    main()
