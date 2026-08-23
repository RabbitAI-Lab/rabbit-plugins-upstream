#!/usr/bin/env python3
"""walk_forward.py - Validasi OOS (out-of-sample) jujur.
Expanding walk-forward: train level di data awal, test di data berikutnya.
Tidak ada curve-fit ke test set."""
import importlib.util, json
spec = importlib.util.spec_from_file_location("ag", "analyze_gold.py")
ag = importlib.util.module_from_spec(spec); spec.loader.exec_module(ag)

rows = ag.load("../data/xauusd_2y.csv")
n = len(rows)
cuts = [n//4, n//2, 3*n//4]  # 3 expanding folds

def oos_test(train, test):
    hi, lo = ag.swing_points(train, 4)
    sup = ag.cluster(lo); res = ag.cluster(hi)
    sup_p = sorted(z[0] for z in sup); res_p = sorted(z[0] for z in res)
    closes = [r["c"] for r in test]
    trades = []; pos = None
    for i in range(30, len(test)):
        c = test[i]["c"]; r = ag.rsi(closes[:i+1], 14); a = ag.atr(test[:i+1], 14)
        e20 = ag.ema(closes[:i+1], 20); s50 = ag.sma(closes[:i+1], 50)
        if a is None or r is None or e20 is None or s50 is None: continue
        near_sup = min((s for s in sup_p if s < c), default=None, key=lambda s: abs(s-c))
        near_res = min((s for s in res_p if s > c), default=None, key=lambda s: abs(s-c))
        if pos is None:
            if c > e20 > s50 and ((abs(c-e20)/c < 0.01) or (near_sup and abs(c-near_sup)/c < 0.005)) and 35 <= r <= 75 and near_res:
                sl = min(near_sup, e20-0.6*a) if near_sup else e20-0.6*a
                tp = near_res
                if tp - c >= 1.5*(c-sl): pos = {"side":"BUY","entry":c,"sl":sl,"tp":tp,"i":i}
            elif c < e20 < s50 and ((abs(c-e20)/c < 0.01) or (near_res and abs(c-near_res)/c < 0.005)) and 30 <= r <= 65 and near_sup:
                sl = max(near_res, e20+0.6*a) if near_res else e20+0.6*a
                tp = near_sup
                if c - tp >= 1.5*(sl-c): pos = {"side":"SELL","entry":c,"sl":sl,"tp":tp,"i":i}
        else:
            if pos["side"]=="BUY":
                hit = test[i]["h"]>=pos["tp"]; stop = test[i]["l"]<=pos["sl"]
                if hit or stop or (i-pos["i"]>=20):
                    pnl=(pos["tp"]-pos["entry"])/pos["entry"] if hit else (pos["sl"]-pos["entry"])/pos["entry"] if stop else (c-pos["entry"])/pos["entry"]
                    trades.append(pnl); pos=None
            else:
                hit=test[i]["l"]<=pos["tp"]; stop=test[i]["h"]>=pos["sl"]
                if hit or stop or (i-pos["i"]>=20):
                    pnl=(pos["entry"]-pos["tp"])/pos["entry"] if hit else (pos["entry"]-pos["sl"])/pos["entry"] if stop else (pos["entry"]-c)/pos["entry"]
                    trades.append(pnl); pos=None
    wins=[t for t in trades if t>0]; losses=[t for t in trades if t<=0]
    wr=len(wins)/len(trades) if trades else 0
    pf=(sum(wins)/abs(sum(losses))) if losses and sum(losses) else (float('inf') if wins else 0)
    return {"test_bars":len(test),"trades":len(trades),"win_rate":round(wr,3),
            "profit_factor":round(pf,2) if pf!=float('inf') else None,"net":round(sum(trades),4)}

print(f"Total bars: {n}")
folds = []
prev = 0
for k, c in enumerate(cuts, 1):
    res = oos_test(rows[:c], rows[c:])
    folds.append(res)
    print(f"Fold {k}: train[0:{c}] test[{c}:{n}] -> {res}")

avg_pf = sum(f["profit_factor"] for f in folds if f["profit_factor"] is not None)/max(1,sum(1 for f in folds if f["profit_factor"] is not None))
tot_trades = sum(f["trades"] for f in folds)
print(f"\nTotal OOS trades: {tot_trades} | avg PF (folds w/ trades): {round(avg_pf,2)}")
print("Kesimpulan: PF OOS > 1.5 = layak. < 1.5 = gak layak (curve-fit).")
