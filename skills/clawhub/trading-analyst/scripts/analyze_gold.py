#!/usr/bin/env python3
"""
analyze_gold.py v2 - Upgrade analisa emas BERBASIS HISTORY (data-first).
Input : data/xauusd_1y.csv (history harian riil, dikirim Bos)
Output: S&R (swing + value-area + Fib + year H/L), indikator, backtest disciplined.

Metode: murni Support/Resistance + Supply/Demand (NO ICT/SMC).
Backtest pakai disiplin NO-TRADE gate (confluence>=2, RR>=1.5, risk<=2%).
"""
import csv, json, os, sys
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(BASE, "..", "data", "xauusd_1y.csv")

def load(path):
    rows = []
    with open(path) as f:
        for r in csv.DictReader(f):
            try:
                d = datetime.fromisoformat(r["Date"].replace("Z", ""))
                rows.append({"d": d, "o": float(r["Open"]), "h": float(r["High"]),
                             "l": float(r["Low"]), "c": float(r["Close"]), "v": float(r["Volume"])})
            except Exception:
                pass
    rows.sort(key=lambda x: x["d"])
    return rows

def rsi(closes, n=14):
    if len(closes) < n + 1: return None
    gains = []; losses = []
    for i in range(1, len(closes)):
        ch = closes[i] - closes[i-1]
        gains.append(max(ch, 0)); losses.append(max(-ch, 0))
    ag = sum(gains[-n:]) / n; al = sum(losses[-n:]) / n
    if al == 0: return 100.0
    return 100 - (100 / (1 + ag/al))

def ema(vals, n):
    if len(vals) < n: return None
    k = 2/(n+1); e = vals[0]
    for v in vals[1:]: e = v*k + e*(1-k)
    return e

def sma(vals, n):
    return sum(vals[-n:])/n if len(vals) >= n else None

def stddev(vals, n):
    if len(vals) < n: return None
    m = sum(vals[-n:])/n
    return (sum((x-m)**2 for x in vals[-n:])/n) ** 0.5

def bollinger(closes, n=20, k=2):
    """Return (lower, middle, upper, pctB). pctB = (price-mid)/(upper-lower)."""
    if len(closes) < n: return (None, None, None, None)
    mid = sma(closes, n); sd = stddev(closes, n)
    if sd is None: return (None, mid, None, None)
    up = mid + k*sd; lo = mid - k*sd
    return (round(lo, 2), round(mid, 2), round(up, 2), None)

def atr(rows, n=14):
    trs = []
    for i in range(1, len(rows)):
        h, l, pc = rows[i]["h"], rows[i]["l"], rows[i-1]["c"]
        trs.append(max(h-l, abs(h-pc), abs(l-pc)))
    return sum(trs[-n:])/n if len(trs) >= n else None

def swing_points(rows, win=4):
    hi = []; lo = []
    for i in range(win, len(rows)-win):
        seg = rows[i-win:i+win+1]
        if rows[i]["h"] == max(r["h"] for r in seg): hi.append(rows[i])
        if rows[i]["l"] == min(r["l"] for r in seg): lo.append(rows[i])
    return hi, lo

def cluster(pivots, tol=None):
    """Pivot -> zone. tol otomatis skala ke harga (0.6% range)."""
    prices = sorted(p["h"] if "h" in p else p["l"] for p in pivots)
    if not prices: return []
    tol = tol or max(20, prices[-1]*0.006)
    zones = []
    for p in prices:
        if not zones: zones.append([p, p, 1])
        elif abs(p - zones[-1][1]) <= tol:
            zones[-1][1] = p; zones[-1][2] += 1
        else: zones.append([p, p, 1])
    return [(round((z[0]+z[1])/2, 2), z[2]) for z in zones]

def value_area(closes, width=25, top=6):
    bins = {}
    for c in closes:
        b = round(c/width)*width
        bins[b] = bins.get(b, 0) + 1
    return sorted([b for b, _ in sorted(bins.items(), key=lambda x: -x[1])[:top]])

def fib(high, low):
    diff = high - low
    return {f"{p}": round(high - diff*p, 2) for p in [0.236, 0.382, 0.5, 0.618, 0.786]}

def backtest_disciplined(rows):
    """Backtest DISCIPLINED (pullback EMA20 / sentuh S&R di tren naik-turun).
    SIGNAL BUY: tren naik (c>ema20>sma50) & (harga narik ke EMA20<1% | sentuh support<0.5%)
               & 35<=RSI<=75 & ada resistance di atas (TP).
    SIGNAL SELL: tren turun & (harga narik ke EMA20 | sentuh resistance) & 30<=RSI<=65.
    SL = level +/- 0.6*ATR, TP = S/R berlawanan (min RR 1.5). Exit: TP/SL/20 bar.
    HONEST: close-to-close approx, tanpa slippage/spread."""
    closes = [r["c"] for r in rows]
    hi_piv, lo_piv = swing_points(rows, win=4)
    sup = cluster(lo_piv); res = cluster(hi_piv)
    sup_p = sorted(z[0] for z in sup); res_p = sorted(z[0] for z in res)
    trades = []; pos = None
    for i in range(30, len(rows)):
        c = rows[i]["c"]
        r = rsi(closes[:i+1], 14); a = atr(rows[:i+1], 14)
        e20 = ema(closes[:i+1], 20); s50 = sma(closes[:i+1], 50)
        if a is None or r is None or e20 is None or s50 is None: continue
        near_sup = min((s for s in sup_p if s < c), default=None, key=lambda s: abs(s-c))
        near_res = min((s for s in res_p if s > c), default=None, key=lambda s: abs(s-c))
        if pos is None:
            if c > e20 > s50 and ((abs(c-e20)/c < 0.01) or (near_sup and abs(c-near_sup)/c < 0.005)) and 35 <= r <= 75 and near_res:
                sl = min(near_sup, e20 - 0.6*a) if near_sup else e20 - 0.6*a
                tp = near_res
                if tp - c >= 1.5*(c - sl):
                    pos = {"side": "BUY", "entry": c, "sl": sl, "tp": tp, "i": i}
            elif c < e20 < s50 and ((abs(c-e20)/c < 0.01) or (near_res and abs(c-near_res)/c < 0.005)) and 30 <= r <= 65 and near_sup:
                sl = max(near_res, e20 + 0.6*a) if near_res else e20 + 0.6*a
                tp = near_sup
                if c - tp >= 1.5*(sl - c):
                    pos = {"side": "SELL", "entry": c, "sl": sl, "tp": tp, "i": i}
        else:
            if pos["side"] == "BUY":
                hit = rows[i]["h"] >= pos["tp"]; stop = rows[i]["l"] <= pos["sl"]
                if hit or stop or (i - pos["i"] >= 20):
                    pnl = (pos["tp"]-pos["entry"])/pos["entry"] if hit else \
                          (pos["sl"]-pos["entry"])/pos["entry"] if stop else (c-pos["entry"])/pos["entry"]
                    trades.append(pnl); pos = None
            else:
                hit = rows[i]["l"] <= pos["tp"]; stop = rows[i]["h"] >= pos["sl"]
                if hit or stop or (i - pos["i"] >= 20):
                    pnl = (pos["entry"]-pos["tp"])/pos["entry"] if hit else \
                          (pos["entry"]-pos["sl"])/pos["entry"] if stop else (pos["entry"]-c)/pos["entry"]
                    trades.append(pnl); pos = None
    wins = [t for t in trades if t > 0]; losses = [t for t in trades if t <= 0]
    wr = len(wins)/len(trades) if trades else 0
    pf = (sum(wins)/abs(sum(losses))) if losses and sum(losses) else (float('inf') if wins else 0)
    return {"trades": len(trades), "win_rate": round(wr, 3),
            "avg_win": round(sum(wins)/len(wins), 4) if wins else 0,
            "avg_loss": round(sum(losses)/len(losses), 4) if losses else 0,
            "profit_factor": round(pf, 2) if pf != float('inf') else None,
            "net_return": round(sum(trades), 4)}

def main(path=None):
    path = path or CSV
    rows = load(path); closes = [r["c"] for r in rows]; last = rows[-1]
    hi_piv, lo_piv = swing_points(rows, win=4)
    sup = cluster(lo_piv); res = cluster(hi_piv)
    va = value_area(closes, width=25, top=6)
    recent = rows[-60:]; rhi = max(r["h"] for r in recent); rlo = min(r["l"] for r in recent)
    out = {
        "updated": last["d"].strftime("%Y-%m-%d"),
        "last_close": last["c"],
        "year_low": min(r["l"] for r in rows), "year_high": max(r["h"] for r in rows),
        "d60_high": rhi, "d60_low": rlo,
        "rsi14": round(rsi(closes, 14), 2), "ema20": round(ema(closes, 20), 2),
        "sma50": round(sma(closes, 50), 2), "sma20": round(sma(closes, 20), 2),
                "sma200": round(sma(closes, 200), 2) if len(closes) >= 200 else None,
        "bollinger20_2": (lambda b: {"lower": b[0], "middle": b[1], "upper": b[2]})(bollinger(closes)),
        "fib_d60": fib(rhi, rlo),
        "support_clusters(>=2touch)": [z for z in sup if z[1] >= 2][-8:],
        "resistance_clusters(>=2touch)": [z for z in res if z[1] >= 2][:8],
        "value_area_top6": va,
        "backtest_disciplined": backtest_disciplined(rows),
    }
    print(json.dumps(out, indent=2, ensure_ascii=False))
    suffix = os.path.splitext(os.path.basename(path))[0]
    outname = "gold_analysis.json" if path == CSV else f"gold_analysis_{suffix}.json"
    with open(os.path.join(BASE, "..", "data", outname), "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"\nSimpan: data/{outname}")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
