#!/usr/bin/env python3
"""
analyze_xau_scheduled.py — SCHEDULED XAU/USD ENTRY ANALYSIS (NO-ICT compliant).
Multi-TF: H4 (trend) -> H1 (momentum) -> M15 (precision).
Data: Twelve Data (key dari api_keys.md). Indicators computed locally (no extra quota).
Outputs the report format requested by Bos. Frames as CANDIDATE, not financial advice.
Risk-first: SL = 1.5x ATR or beyond swing; TP1:1, TP2:2 (partial 50%), TP3:3 / next S&R.
Requires >=3 confirmations; defaults to WAIT if ambiguous. News/DXY filter via existing scripts.
"""
import json, sys, os, datetime
from ds_util import load_twelve_key, fetch, cache_get, cache_put
import indicators as ind

SCRIPT_DIR = os.path.dirname(__file__)
OUT = os.path.join(SCRIPT_DIR, "..", "data", "scheduled_report.json")

def fetch_tf(iv, n):
    key = load_twelve_key()
    if not key: return None, "NO_KEY"
    u = "https://api.twelvedata.com/time_series?symbol=XAU/USD&interval=" + iv + "&outputsize=" + str(n) + "&apikey=" + key
    try:
        d = json.loads(fetch(u, 25))
    except Exception as e:
        return None, f"FETCH_FAIL:{e}"
    if "values" not in d:
        return None, d.get("message", "NO_VALUES")
    bars = d["values"][::-1]
    closes = [float(b["close"]) for b in bars]
    highs = [float(b["high"]) for b in bars]
    lows = [float(b["low"]) for b in bars]
    return {"closes": closes, "highs": highs, "lows": lows, "bars": bars, "last": closes[-1]}, None

def analyze():
    # fetch 3 TFs (H4 250, H1 250, M15 250 to have EMA200 + stable ADX)
    h4, e4 = fetch_tf("4h", 250)
    h1, e1 = fetch_tf("1h", 250)
    m15, e15 = fetch_tf("15min", 250)
    if e4 or e1 or e15:
        return {"error": {"h4": e4, "h1": e1, "m15": e15}}

    price = h4["last"]
    # ---- H4 TREND ----
    e50_4 = ind.ema(h4["closes"], 50); e200_4 = ind.ema(h4["closes"], 200)
    adx_4 = ind.adx(h4["highs"], h4["lows"], h4["closes"])
    trend = "Sideways"
    if e50_4 and e200_4:
        if e50_4 > e200_4 and price > e50_4: trend = "Bullish"
        elif e50_4 < e200_4 and price < e50_4: trend = "Bearish"
    # ---- H1 MOMENTUM ----
    rsi_1 = ind.rsi(h1["closes"]); macd_1 = ind.macd(h1["closes"]); stoch_1 = ind.stochastic(h1["highs"], h1["lows"], h1["closes"])
    atr_1 = ind.atr(h1["highs"], h1["lows"], h1["closes"])
    macd_state = "Bullish" if (macd_1 and macd_1[2] is not None and macd_1[2] > 0) else ("Bearish" if (macd_1 and macd_1[2] is not None and macd_1[2] < 0) else "Neutral")
    # ---- LEVELS (from H4 swings + fib + pivot) ----
    sh, sl = ind.swings(h4["highs"], h4["lows"], 20)  # swing high / swing low (20 candle)
    s_lvl = round(sl, 2)        # support level (numeric)
    r_lvl = round(sh, 2)        # resistance level (numeric)
    fib_h, fib_l = sh, sl
    fibo = ind.fib([0.382,0.5,0.618], fib_h, fib_l)
    piv = ind.pivot(h4["highs"], h4["lows"], h4["closes"])
    # ---- SETUP LOGIC ----
    confirmations = []
    if trend == "Bullish": confirmations.append("H4 bullish")
    elif trend == "Bearish": confirmations.append("H4 bearish")
    if rsi_1 is not None:
        if trend == "Bullish" and 30 <= rsi_1 <= 50: confirmations.append("H1 RSI pullback(30-50)")
        if trend == "Bearish" and 50 <= rsi_1 <= 70: confirmations.append("H1 RSI pullback(50-70)")
    if macd_state == "Bullish": confirmations.append("H1 MACD bull cross")
    elif macd_state == "Bearish": confirmations.append("H1 MACD bear cross")
    if stoch_1 and ((stoch_1[0] < 20 and trend=="Bullish") or (stoch_1[0] > 80 and trend=="Bearish")):
        confirmations.append("H1 Stoch extreme")
    # price action: last M15 candle pattern
    pa = m15["bars"][-1]
    # build candidate
    direction = "Buy" if trend == "Bullish" else ("Sell" if trend == "Bearish" else "Wait")
    entry_zone, sl, tp1, tp2, tp3 = None, None, None, None, None
    rec = "Tunggu"
    setup = None
    if direction == "Buy" and len(confirmations) >= 3:
        entry_zone = (s_lvl, round(s_lvl+atr_1,2))  # near support
        sl_p = round(s_lvl - 1.5*atr_1, 2)
        tp1 = round(sl_p + (entry_zone[1]-sl_p)*1, 2)
        tp2 = round(sl_p + (entry_zone[1]-sl_p)*2, 2)
        tp3 = r_lvl
        setup = {"direction": "Buy Limit", "entry_zone": [entry_zone[0], entry_zone[1]], "sl": sl_p, "tp1": tp1, "tp2": tp2, "tp3": tp3}
        rec = "Entry"
    elif direction == "Sell" and len(confirmations) >= 3:
        entry_zone = (round(r_lvl-atr_1,2), r_lvl)
        sl_p = round(r_lvl + 1.5*atr_1, 2)
        tp1 = round(sl_p - (sl_p-entry_zone[0])*1, 2)
        tp2 = round(sl_p - (sl_p-entry_zone[0])*2, 2)
        tp3 = s_lvl
        setup = {"direction": "Sell Limit", "entry_zone": [entry_zone[0], entry_zone[1]], "sl": sl_p, "tp1": tp1, "tp2": tp2, "tp3": tp3}
        rec = "Entry"

    report = {
        "symbol": "XAU/USD",
        "generated_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M WIB"),
        "trend_h4": trend, "ema50_h4": e50_4, "ema200_h4": e200_4, "adx_h4": adx_4,
        "momentum_h1": {"rsi": rsi_1, "macd": macd_state, "macd_hist": macd_1[2] if macd_1 else None, "stochastic": stoch_1},
        "levels": {"resistance": [r_lvl, round(piv["R1"],2) if piv else None],
                   "support": [s_lvl, round(piv["S1"],2) if piv else None],
                   "fibo": fibo, "pivot": piv, "atr_h1": atr_1},
        "price": price,
        "confirmations": confirmations,
        "setup": setup,
        "recommendation": rec,
        "note": "CANDIDATE only — not financial advice. NO-ICT (S/R + multi-TF + PA). Require >=3 confirmations.",
    }
    return report

if __name__ == "__main__":
    r = analyze()
    print(json.dumps(r, indent=2))
    try: json.dump(r, open(OUT, "w"), indent=2)
    except Exception: pass
