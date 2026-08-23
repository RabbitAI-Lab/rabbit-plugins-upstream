#!/usr/bin/env python3
"""monte_carlo.py - Bootstrap per-trade returns dari backtest 2Y.
Tarik distribusi PF & win-rate lewat resampling (dengan replacement).
Tujuannya: lihat berapa persen simulasi yang masih PF > 1.5."""
import importlib.util, json, random
spec = importlib.util.spec_from_file_location("ag", "analyze_gold.py")
ag = importlib.util.module_from_spec(spec); spec.loader.exec_module(ag)

def trade_pnls(rows):
    closes = [r["c"] for r in rows]
    hi, lo = ag.swing_points(rows, 4)
    sup = ag.cluster(lo); res = ag.cluster(hi)
    sup_p = sorted(z[0] for z in sup); res_p = sorted(z[0] for z in res)
    out = []; pos = None
    for i in range(30, len(rows)):
        c = rows[i]["c"]; r = ag.rsi(closes[:i+1], 14); a = ag.atr(rows[:i+1], 14)
        e20 = ag.ema(closes[:i+1], 20); s50 = ag.sma(closes[:i+1], 50)
        if a is None or r is None or e20 is None or s50 is None: continue
        ns = min((s for s in sup_p if s < c), default=None, key=lambda s: abs(s-c))
        nr = min((s for s in res_p if s > c), default=None, key=lambda s: abs(s-c))
        if pos is None:
            if c > e20 > s50 and ((abs(c-e20)/c < 0.01) or (ns and abs(c-ns)/c < 0.005)) and 35 <= r <= 75 and nr:
                sl = min(ns, e20-0.6*a) if ns else e20-0.6*a; tp = nr
                if tp-c >= 1.5*(c-sl): pos = {"side":"BUY","entry":c,"sl":sl,"tp":tp,"i":i}
            elif c < e20 < s50 and ((abs(c-e20)/c < 0.01) or (nr and abs(c-nr)/c < 0.005)) and 30 <= r <= 65 and ns:
                sl = max(nr, e20+0.6*a) if nr else e20+0.6*a; tp = ns
                if c-tp >= 1.5*(sl-c): pos = {"side":"SELL","entry":c,"sl":sl,"tp":tp,"i":i}
        else:
            if pos["side"]=="BUY":
                hit=rows[i]["h"]>=pos["tp"]; stop=rows[i]["l"]<=pos["sl"]
                if hit or stop or (i-pos["i"]>=20):
                    out.append((pos["tp"]-pos["entry"])/pos["entry"] if hit else (pos["sl"]-pos["entry"])/pos["entry"] if stop else (c-pos["entry"])/pos["entry"])
                    pos=None
            else:
                hit=rows[i]["l"]<=pos["tp"]; stop=rows[i]["h"]>=pos["sl"]
                if hit or stop or (i-pos["i"]>=20):
                    out.append((pos["entry"]-pos["tp"])/pos["entry"] if hit else (pos["entry"]-pos["sl"])/pos["entry"] if stop else (pos["entry"]-c)/pos["entry"])
                    pos=None
    return out

rows = ag.load("../data/xauusd_2y.csv")
pnls = trade_pnls(rows)
N = len(pnls)
random.seed(42)
SIM = 5000
pfs = []; wrs = []
for _ in range(SIM):
    sample = [random.choice(pnls) for _ in range(N)]
    wins = [t for t in sample if t > 0]; losses = [t for t in sample if t <= 0]
    if not wins: pfs.append(0); wrs.append(0); continue
    pf = (sum(wins)/abs(sum(losses))) if losses and sum(losses) else 999
    pfs.append(min(pf, 999)); wrs.append(len(wins)/len(sample))

pf_sorted = sorted(pfs)
wr_sorted = sorted(wrs)
def pct(arr, p): return arr[int(p/100*len(arr))]
print(f"Trades asli: {N}  | WR asli: {sum(1 for t in pnls if t>0)/N:.3f}  | PF asli: {sum(t for t in pnls if t>0)/abs(sum(t for t in pnls if t<=0)):.2f}")
print(f"Monte Carlo ({SIM} sims, N={N}):")
print(f"  PF  median: {pct(pf_sorted,50):.2f}  | 5th pct: {pct(pf_sorted,5):.2f}  | 95th pct: {pct(pf_sorted,95):.2f}")
print(f"  WR  median: {pct(wr_sorted,50):.3f}  | 5th pct: {pct(wr_sorted,5):.3f}  | 95th pct: {pct(wr_sorted,95):.3f}")
print(f"  % sim PF>1.5: {100*sum(1 for p in pfs if p>1.5)/SIM:.1f}%")
print(f"  % sim PF<1.0 (rugi): {100*sum(1 for p in pfs if p<1.0)/SIM:.1f}%")
