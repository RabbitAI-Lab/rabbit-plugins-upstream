#!/usr/bin/env python3
"""
sd_zones.py - Deteksi SUPPORT/RESISTANCE (touch count) + SUPPLY/DEMAND zones
dari CSV history riil. Tanpa ICT/SMC. Honest backtest S/D reversion.
"""
import csv, json, os
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(BASE, "..", "data", "xauusd_2y.csv")

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

def sma(vals, n):
    return sum(vals[-n:])/n if len(vals) >= n else None

def atr(rows, n=14):
    trs = [max(rows[i]["h"]-rows[i]["l"], abs(rows[i]["h"]-rows[i-1]["c"]), abs(rows[i]["l"]-rows[i-1]["c"]))
           for i in range(1, len(rows))]
    return sum(trs[-n:])/n if len(trs) >= n else None

def swing_points(rows, win=4):
    hi = []; lo = []
    for i in range(win, len(rows)-win):
        seg = rows[i-win:i+win+1]
        if rows[i]["h"] == max(r["h"] for r in seg): hi.append(rows[i])
        if rows[i]["l"] == min(r["l"] for r in seg): lo.append(rows[i])
    return hi, lo

def cluster(pivots, tol=None):
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

def count_touches(rows, level, tol=0.004):
    """Hitung baris di mana harga MENDATANGI level (dlm tol) lalu BERBALIK."""
    n = 0
    for i in range(1, len(rows)):
        c = rows[i]["c"]; lo = rows[i]["l"]; hi = rows[i]["h"]
        prev = rows[i-1]["c"]
        near = abs(c - level)/level <= tol or (lo <= level <= hi)
        if near:
            # reversal: close bergerak menjauhi level vs bar sebelumnya
            if (level < c and c < prev) or (level > c and c > prev):
                n += 1
    return n

def detect_sd(rows, tight=0.45, dep=0.015, min_base=2, max_base=8):
    """Base = run baris tight (range kecil). Departure = bar berikutnya break jauh.
    RBR (rally-base-rally) -> demand. DBD -> supply."""
    ar = sum(r["h"]-r["l"] for r in rows[-80:]) / 80
    zones = []
    n = len(rows); i = 2
    while i < n - 2:
        seg = rows[i-2:i+1]
        tight_ok = all((r["h"]-r["l"]) <= tight*ar for r in seg)
        if tight_ok:
            j = i
            while j < n-1 and (rows[j]["h"]-rows[j]["l"]) <= tight*ar:
                j += 1
            base = rows[i-2:j]
            bhi = max(r["h"] for r in base); blo = min(r["l"] for r in base)
            db = rows[j]
            up = (db["c"] - bhi)/bhi >= dep
            dn = (blo - db["c"])/blo >= dep
            if up:
                zones.append({"type": "demand", "zh": round(bhi,2), "zl": round(blo,2),
                              "formed": base[-1]["d"].strftime("%Y-%m-%d"),
                              "dep": round((db["c"]-bhi)/bhi, 4), "tested": False})
                i = j + 1; continue
            elif dn:
                zones.append({"type": "supply", "zh": round(bhi,2), "zl": round(blo,2),
                              "formed": base[-1]["d"].strftime("%Y-%m-%d"),
                              "dep": round((blo-db["c"])/blo, 4), "tested": False})
                i = j + 1; continue
        i += 1
    return zones

def backtest_sd(rows, zones):
    closes = [r["c"] for r in rows]
    trades = []; pos = None
    sma50_list = [sma(closes[:i+1], 50) for i in range(len(closes))]
    for i in range(60, len(rows)):
        c = rows[i]["c"]; s50 = sma50_list[i]
        if s50 is None: continue
        a = atr(rows[:i+1], 14)
        # cari zone yang sedang di-test (harga masuk area zone)
        if pos is None:
            for z in zones:
                in_zone = (z["zl"] <= rows[i]["l"] <= z["zh"]) or (z["zl"] <= c <= z["zh"])
                if not in_zone: continue
                if z["type"] == "demand" and c > s50:
                    sl = z["zl"] - 0.5*a; tp = c + 2*(c - sl)
                    if tp - c >= 1.5*(c - sl):
                        pos = {"side": "BUY", "entry": c, "sl": sl, "tp": tp, "i": i, "z": z}
                        break
                elif z["type"] == "supply" and c < s50:
                    sl = z["zh"] + 0.5*a; tp = c - 2*(sl - c)
                    if c - tp >= 1.5*(sl - c):
                        pos = {"side": "SELL", "entry": c, "sl": sl, "tp": tp, "i": i, "z": z}
                        break
        else:
            if pos["side"] == "BUY":
                if rows[i]["h"] >= pos["tp"] or rows[i]["l"] <= pos["sl"] or (i-pos["i"] >= 20):
                    hit = rows[i]["h"] >= pos["tp"]
                    pnl = (pos["tp"]-pos["entry"])/pos["entry"] if hit else (pos["sl"]-pos["entry"])/pos["entry"]
                    trades.append(pnl); pos = None
            else:
                if rows[i]["l"] <= pos["tp"] or rows[i]["h"] >= pos["sl"] or (i-pos["i"] >= 20):
                    hit = rows[i]["l"] <= pos["tp"]
                    pnl = (pos["entry"]-pos["tp"])/pos["entry"] if hit else (pos["entry"]-pos["sl"])/pos["entry"]
                    trades.append(pnl); pos = None
    wins = [t for t in trades if t > 0]; losses = [t for t in trades if t <= 0]
    wr = len(wins)/len(trades) if trades else 0
    pf = (sum(wins)/abs(sum(losses))) if losses and sum(losses) else (float('inf') if wins else 0)
    return {"trades": len(trades), "win_rate": round(wr,3),
            "avg_win": round(sum(wins)/len(wins),4) if wins else 0,
            "avg_loss": round(sum(losses)/len(losses),4) if losses else 0,
            "profit_factor": round(pf,2) if pf != float('inf') else None,
            "net_return": round(sum(trades),4)}

def main():
    rows = load(CSV)
    hi, lo = swing_points(rows, 4)
    sup = cluster(lo); res = cluster(hi)
    sup_r = [(lv, ct, count_touches(rows, lv)) for lv, ct in sup]
    res_r = [(lv, ct, count_touches(rows, lv)) for lv, ct in res]
    zones = detect_sd(rows)
    bt = backtest_sd(rows, zones)
    out = {
        "updated": rows[-1]["d"].strftime("%Y-%m-%d"),
        "bars": len(rows),
        "support_levels(touch_count)": sorted([(lv, t) for lv, _, t in sup_r if t >= 2], reverse=True)[:10],
        "resistance_levels(touch_count)": sorted([(lv, t) for lv, _, t in res_r if t >= 2])[:10],
        "sd_zones": zones,
        "sd_backtest": bt,
    }
    print(json.dumps(out, indent=2, ensure_ascii=False))
    with open(os.path.join(BASE, "..", "data", "sd_zones.json"), "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print("\nSimpan: data/sd_zones.json")

if __name__ == "__main__":
    main()
