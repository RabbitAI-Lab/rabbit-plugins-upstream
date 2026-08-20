---
name: "drt-trading"
description: "Dealing Range Theory (DRT) — Ali Khan's complete ICT structure: Type 1 (continuation), Type 2 (reversal), Type 3 (consolidation), quadrant levels (25/50/75), entry models, SMT confirmation and news filter. For market analysis and trade setups."
---

# DRT — Dealing Range Theory (Ali Khan) 📐

## Fundament
- Prisen leveres af IPDA-algoritmen: søger **likviditet over gamle highs / under gamle lows**, og rebalancerer Fair Value Gaps.
- En **Dealing Range** dannes efter et **liquidity raid** (sweep af swing high/low).
- Range-grænser: **DRH** (Dealing Range High) og **DRL** (Dealing Range Low).
- Prisen roterer mellem **intern range-likviditet** og **ekstern range-likviditet** (raids).
- Range opdeles i **4 lige store kvadranter** → niveauer: **25DRT, 50DRT, 75DRT**.
  - **25DRT** = ekstrem discount (købszone)
  - **50DRT** = equilibrium (balance)
  - **75DRT** = ekstrem premium (salgszone)
- Køb i discount → sell i premium.

## De 3 Typer af Dealing Ranges

### Type 1 — Continuation ⬆️⬇️
- **Situation:** Efter raid fortsætter prisen i **samme retning** som raidet → trend/fortsættelse mod DRH eller DRL.
- **Hvad algoritmen laver:** Leverer pris mod den modsatte range-grænse uden dyb tilbagetrækning.
- **Detektion:** Raid af swing high/low → pris bryder **igennem** de relative equal levels med **displacement** (stærk candle) → fortsætter.
- **Entry:** Retest af brudt niveau eller **50DRT** efter displacement.
- **Target:** DRH (for longs) / DRL (for shorts) — ofte 3R+.
- **SL:** Bag raid-niveauet (sweep-ekstrem + buffer).

### Type 2 — Reversal 🔄
- **Situation:** Raid → reversal tilbage mod modsatte side af range.
- **Hvad algoritmen laver:** Samler likviditet (raid), vender og leverer pris mod modsatte kvadrant.
- **Detektion:** Sweep af swing high/low → **relative equal levels** på modsatte side → bias:
  - Equal **highs** dannet først → **long** bias (mod equal highs)
  - Equal **lows** dannet først → **short** bias (mod equal lows)
- **Entry Model 1:** Ved **25DRT** (long) / **75DRT** (short) efter **closure** (candle lukker over/under niveauet).
  - Target: modsatte side af range = **3R**
  - SL: bag sweep-ekstrem + buffer (0.5 × ATR)
- **Entry Model 2:** Ved **50DRT** efter **displacement** (body > 1.5 × ATR).
  - Target: **2R** (tighter stop)
  - SL: tættere (bag 50DRT-reaktion)

### Type 3 — Consolidation 📦
- **Situation:** Range-kompression — pris roterer internt mellem kvadranterne uden raid af begge sider.
- **Hvad algoritmen laver:** Bygger likviditet, venter på udløser.
- **Regel:** **Undgå trades** i Type 3-miljø — det spilder trades og sænker win rate.
- **Detektion:** Lav ATR relativt til range; pris mellem 25-75 uden raid af nogen side; lave equal highs/lows uden sweep.
- **Hvis man handler:** Kun på **udbrud** med displacement + retest (breakout-model).

## SMT — Smart Money Technique (bekræftelse) 🤝
- **Divergens** mellem korrelerede instrumenter bekræfter reversal:
  - **EUR/USD ↔ GBP/USD** — når EU laver nyt low men GU ikke gør = bullish SMT → bekræfter long.
  - **DXY ↔ indices/guld** — DXY svaghed = risk-on.
- Brug SMT som **filter**: hvis SMT modsiger DRT-signalet → skip trade.

## News-filter ⛔
- Undgå trades **15 min før/efter high-impact events**: FOMC, NFP, CPI, PCE, renter.
- Red folder news = flat eller ude.

## Eksekveringsrammer (DK-tid)
- Intraday/scalp: kun i killzones (London 09-11, NY AM 14:30-17:00, SB PM 19:30-21:00, ⛔ 15:30-16:00).
- Swing: entry kan ske når som helst.
- Max 3 trades/dag, SL altid, journal i TradeVault.

## Checkliste — FØR trade
1. ✅ Er der en etableret dealing range (DRH/DRL defineret efter raid)?
2. ✅ **Range ≥ 5×ATR?** (backtestet: ≥5×ATR = 89,7% WR, ≥7×ATR = 92%)
3. ✅ **Er tiden NY-session (15:00-20:00 DK)?** (backtestet: 15-20 = 80,8% WR)
4. ✅ Hvilken type: Type 1 (continuation) / Type 2 (reversal) / Type 3 (undgå)?
5. ✅ Er prisen i discount (25DRT) for longs / premium (75DRT) for shorts?
6. ✅ Entry-model: 25/75DRT closure (3R) eller 50DRT displacement (2R)?
7. ✅ SMT-bekræftelse (EU/GU/DXY)?
8. ✅ Ingen high-impact news i vinduet?
9. ✅ R:R mindst 2:1 — ellers skip.

## Endelige filtre (backtestet 31/7, 1h DRT, 2 år, 2.531 trades)
- **Kun ranges ≥ 5×ATR** → 89,7% WR (+NY-timer → 92,5%)
- **Kun NY-timer 15:00-20:00 DK** → 80,8% WR
- **≥6×ATR + NY** → 93,8% WR (144 trades)
- **≥5×ATR + NY** → 92,5% WR (226 trades = ~2-3/uge) ⭐ ANBEFALET

## Backtest-referencer (1h DRT, 2 år)
- Baseline: 2.531 trades, 71,8% WR, +4741R
- ≥5×ATR: 474 trades, 89,7% WR, +1226R
- ≥5×ATR + NY-timer: 226 trades, **92,5% WR**, +610R
- Primære instrumenter: GBP/USD (71,8%), XAU/USD (72,6%), US30 (70,3%), XAG/USD (70,4%)
- Scripts: `tradevault/scripts/backtest_drt.py`, `backtest_drt_v2.py`, `backtest_combo.py`
