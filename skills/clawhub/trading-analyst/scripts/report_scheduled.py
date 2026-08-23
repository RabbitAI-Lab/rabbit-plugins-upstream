#!/usr/bin/env python3
"""
report_scheduled.py — formatted XAU/USD scheduled report (Bos's exact template).
Runs analyze_xau_scheduled + news_check + correlation_check, prints the report,
and (if cron) writes to memory/trading/scheduled_report.md. NO-ICT, candidate-only.
"""
import json, os, sys, subprocess, datetime
SCRIPT_DIR = os.path.dirname(__file__)
sys.path.insert(0, SCRIPT_DIR)

def run_script(name, *args):
    try:
        out = subprocess.run([sys.executable, os.path.join(SCRIPT_DIR, name)] + list(args),
                             capture_output=True, text=True, timeout=60).stdout
        return json.loads(out)
    except Exception as e:
        return {"error": str(e)}

def main():
    r = run_script("analyze_xau_scheduled.py")
    if "error" in r or "trend_h4" not in r:
        print("ANALYSIS ERROR:", r.get("error", r))
        return
    news = run_script("news_check.py", "--pretty")
    corr = run_script("correlation_check.py", "--pretty")

    now = r["generated_at"]
    trend = r["trend_h4"]
    mom = r["momentum_h1"]
    lvl = r["levels"]
    setup = r["setup"]

    # news / DXY
    high_impact = news.get("high_impact_today", False) if isinstance(news, dict) else False
    news_note = news.get("news_clear", "n/a") if isinstance(news, dict) else "n/a"
    dxy = None
    if isinstance(corr, dict):
        d = corr.get("detail", {}).get("DXY", {})
        dxy = d.get("price")

    # probability (heuristic): more confirmations + clean news + aligned DXY = higher
    nconf = len(r.get("confirmations", []))
    prob = "Rendah"
    if setup and nconf >= 4 and not high_impact: prob = "Tinggi"
    elif setup and nconf >= 3: prob = "Sedang"

    lines = []
    lines.append("📊 LAPORAN ANALISIS XAU/USD — " + now)
    lines.append("")
    lines.append("🔹 TREND H4: " + trend + f"  (EMA50 {r['ema50_h4']} / EMA200 {r['ema200_h4']}, ADX {r['adx_h4']})")
    lines.append("🔹 MOMENTUM H1: " + f"RSI: {mom['rsi']} | MACD: {mom['macd']} | Stoch: {mom['stochastic']}")
    lines.append("🔹 LEVEL KUNCI:")
    lines.append(" - Resistance: $" + " / $".join(str(x) for x in lvl["resistance"] if x))
    lines.append(" - Support: $" + " / $".join(str(x) for x in lvl["support"] if x))
    f = lvl["fibo"]
    lines.append(f" - Fibo: 50% @ ${f.get('0.5')} | 61.8% @ ${f.get('0.618')}")
    if lvl.get("pivot"):
        p = lvl["pivot"]
        lines.append(f" - Pivot: P ${p['P']} | R1 ${p['R1']} | S1 ${p['S1']} | R2 ${p['R2']} | S2 ${p['S2']}")
    lines.append("")
    lines.append("🎯 SETUP ENTRY:")
    if setup:
        ez = setup["entry_zone"]
        lines.append(" - Jenis: " + setup["direction"])
        lines.append(f" - Entry Zone: ${ez[0]} – ${ez[1]}")
        lines.append(f" - Stop Loss: ${setup['sl']}")
        lines.append(f" - Take Profit 1: ${setup['tp1']} (RR 1:1)")
        lines.append(f" - Take Profit 2: ${setup['tp2']} (RR 1:2, partial 50%)")
        lines.append(f" - Take Profit 3: ${setup['tp3']} (RR 1:3 / next S&R)")
    else:
        lines.append(" - (Tidak ada setup — konfirmasi < 3, tunggu pullback)")
    lines.append("")
    lines.append("⚠️ RISK WARNING:")
    lines.append(" - News hari ini: " + ("ADA (high impact)" if high_impact else "tidak ada high-impact"))
    lines.append(" - DXY: " + (str(dxy) if dxy else "n/a") + " (korelasi negatif emas)")
    lines.append(" - Rekomendasi: " + r["recommendation"])
    lines.append("")
    lines.append("📈 Probabilitas Setup: " + prob)
    lines.append("")
    lines.append("🔸 Konfirmasi terpenuhi: " + (", ".join(r["confirmations"]) if r["confirmations"] else "(kosong)") + f"  [{nconf}/3 minimal]")
    lines.append("🔸 " + r["note"])
    report = "\n".join(lines)

    # save
    try:
        out_md = os.path.join(os.path.expanduser("~"), ".openclaw", "workspace", "memory", "trading", "scheduled_report.md")
        with open(out_md, "w") as fh:
            fh.write(report + "\n")
        json.dump(r, open(os.path.join(SCRIPT_DIR, "..", "data", "scheduled_report.json"), "w"), indent=2)
    except Exception:
        pass
    print(report)

if __name__ == "__main__":
    main()
