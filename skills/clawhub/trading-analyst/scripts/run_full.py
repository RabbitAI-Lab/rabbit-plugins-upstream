#!/usr/bin/env python3
"""
run_full.py - SATU ENTRY POINT analisa XAU/USD.
Input: CSV history (default ../data/xauusd_2y.csv).
Output: laporan level + bias + setup konkret (entry/SL/TP/RR/skor) + auto-journal.

Tanpa ICT/SMC. Data-first. Bukan saran keuangan.
"""
import importlib.util, json, os, subprocess, sys

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "..", "data")

def load_mod(name, fn):
    spec = importlib.util.spec_from_file_location(name, os.path.join(BASE, fn))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

ag = load_mod("ag", "analyze_gold.py")
sd = load_mod("sd", "sd_zones.py")

def call(cmd_args):
    try:
        r = subprocess.run([sys.executable] + cmd_args, capture_output=True, text=True, timeout=30)
        return r.stdout + r.stderr
    except Exception as e:
        return ""

def main(csv_path=None):
    csv_path = csv_path or os.path.join(DATA, "xauusd_2y.csv")
    rows = ag.load(csv_path)
    closes = [r["c"] for r in rows]
    c = closes[-1]
    n = len(closes)
    rsi = ag.rsi(closes, 14)
    e20 = ag.ema(closes, 20); s50 = ag.sma(closes, 50); s200 = ag.sma(closes, 200)
    a = ag.atr(rows, 14)
    bb = ag.bollinger(closes)
    hi, lo = ag.swing_points(rows, 4)
    sup = ag.cluster(lo); res = ag.cluster(hi)
    sup_t = [(lv, ct, sd.count_touches(rows, lv)) for lv, ct in sup]
    res_t = [(lv, ct, sd.count_touches(rows, lv)) for lv, ct in res]

    bias = "BULLISH" if (e20 and s50 and c > e20 > s50) else ("BEARISH" if (e20 and s50 and c < e20 < s50) else "NEUTRAL")
    overbought = rsi > 70
    above_bb = c > bb[2]

    support_below = sorted([lv for lv, _, t in sup_t if lv < c and t >= 2], reverse=True)[:3]
    res_above = sorted([lv for lv, _, t in res_t if lv > c and t >= 2])[:2]
    nearest_sup = support_below[0] if support_below else None
    nearest_res = res_above[0] if res_above else None

    setups = []
    # BUY LIMIT di support terdekat (pullback dalam uptrend)
    if bias == "BULLISH" and nearest_sup:
        entry = nearest_sup
        sl = entry - 0.6 * a
        tp = nearest_res if nearest_res else entry + 2 * (entry - sl)
        rr = (tp - entry) / (entry - sl) if entry > sl else 0
        if rr >= 1.5:
            setups.append({"type": "BUY_LIMIT", "entry": round(entry, 1), "sl": round(sl, 1),
                           "tp": round(tp, 1), "rr": round(rr, 2), "basis": f"support {entry} (pullback uptrend)"})
    # BUY STOP breakout resistance terdekat
    if bias == "BULLISH" and nearest_res:
        entry = nearest_res + 5
        sl = nearest_res - 10
        tp = entry + 2 * (entry - sl)
        rr = (tp - entry) / (entry - sl) if entry > sl else 0
        if rr >= 1.5:
            setups.append({"type": "BUY_STOP", "entry": round(entry, 1), "sl": round(sl, 1),
                           "tp": round(tp, 1), "rr": round(rr, 2), "basis": f"breakout {nearest_res}"})

    # skor + risk tiap setup
    for s in setups:
        sc = {"symbol": "XAUUSD", "direction": "LONG", "entry": s["entry"], "sl": s["sl"],
              "tp": s["tp"], "bias": bias.lower(), "confluence_count": 3, "rr": s["rr"], "risk_pct": 1.0,
              "macro_filter": "unknown", "rsi_extreme": overbought, "zone_fresh": False,
              "news_clear": False, "spread_ok": False}
        out = call([os.path.join(BASE, "setup_scorer.py"), "--json", json.dumps(sc)])
        import re
        m = re.search(r'"score":\s*(\d+)', out)
        v = re.search(r'"verdict":\s*"([^"]*)"', out)
        s["score"] = int(m.group(1)) if m else None
        s["verdict"] = v.group(1) if v else "?"
        rc = call([os.path.join(BASE, "risk_calc.py"), "--equity", "1000", "--risk", "0.01",
                   "--entry", str(s["entry"]), "--sl", str(s["sl"]), "--tp", str(s["tp"]),
                   "--direction", "LONG"])
        s["risk_ok"] = "OK" in rc

    # journal
    jpath = os.path.join(DATA, "forward_test.jsonl")
    with open(jpath, "a") as f:
        for s in setups:
            f.write(json.dumps({"date": rows[-1]["d"].strftime("%Y-%m-%d"), "symbol": "XAUUSD",
                                "type": s["type"], "entry": s["entry"], "sl": s["sl"], "tp": s["tp"],
                                "rr": s["rr"], "score": s["score"], "verdict": s["verdict"],
                                "status": "PENDING"}, ensure_ascii=False) + "\n")

    rep = {
        "updated": rows[-1]["d"].strftime("%Y-%m-%d"),
        "price": round(c, 2), "rsi": round(rsi, 1), "ema20": round(e20, 1) if e20 else None,
        "sma50": round(s50, 1) if s50 else None, "sma200": round(s200, 1) if s200 else None,
        "bollinger_upper": round(bb[2], 1), "bias": bias,
        "overbought": overbought, "above_bollinger": above_bb,
        "support_levels": sorted([(lv, t) for lv, _, t in sup_t if t >= 2], reverse=True)[:6],
        "resistance_levels": sorted([(lv, t) for lv, _, t in res_t if t >= 2])[:6],
        "setups": setups,
    }
    out_path = os.path.join(DATA, "run_full_report.json")
    json.dump(rep, open(out_path, "w"), indent=2, ensure_ascii=False)
    print(json.dumps(rep, indent=2, ensure_ascii=False))
    print(f"\nJournal: {jpath} | Report: {out_path}")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
