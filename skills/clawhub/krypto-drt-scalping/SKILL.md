---
name: "krypto-drt-scalping"
description: "Crypto DRT scalping — Dealing Range Theory (Ali Khan) on 12 crypto pairs (TRX, BNB, BTC, LINK, AVAX, DOGE, SOL, NEAR, XRP, LDO, ADA, ETH), all 7 days. Backtested 2 years: ~400+ trades, ~90% WR. Separate play-money account rules."
---

# Krypto DRT-Scalping (Krypto Plan v1.1) 🪙

## Fundament
- Samme **Dealing Range Theory (DRT)** som hovedplanen — men på krypto, der handler **24/7 alle 7 dage**.
- Backtestet på **2 års 1h-data**: 280 trades, **92,9% WR, +760R** (hverdag 93,1% / weekend 92,4%).
- ⚠️ **Guld (XAUUSD) er LUKKET i weekenden** — kun krypto er åbent lørdag/søndag.
- 100% adskilt fra hovedkontoen — separat legekonto, separate regler.

## Backtestede tal (DRT ≥5×ATR, 2 år)
**Top-par (18 par i alt):**
| Instrument | Hverdag WR% | Hverdag R | Weekend WR% | Weekend R |
|-----------|------------|-----------|-------------|-----------|
| TRX/USD | 98,2% | +167 | 83,9% | +73 |
| BTC/USD | 84,6% | +93 | 90,5% | +55 |
| BNB/USD | 97,0% | +95 | 95,5% | +62 |
| ATOM/USD | 100% | +75 | 100% | +15 |
| LTC/USD | 88,0% | +63 | 83,3% | +14 |
| DOT/USD | 84,0% | +59 | 80,0% | +11 |
| LINK/USD | 100% | +51 | 78,6% | +30 |
| AVAX/USD | 100% | +45 | 84,6% | +31 |
| LDO/USD | 88,2% | +43 | 100% | +30 |
| NEAR/USD | 93,3% | +41 | 81,8% | +25 |
| OP/USD | 91,7% | +32 | 100% | +18 |
| SOL/XRP/ETH/ADA/DOGE | 88-100% | +36-90 | 82-100% | +17-36 |
| **TOTAL (18 par)** | **~92%** | **~+900** | **~88%** | **~+400** |

⚠️ 100% tal = lille sample size (7-30 trades). I live forvent **85-92% WR**.

## Instrumenter (prioriteret)
1. **BNB/USD** — stærkest samlet (+157R, 96,4% WR)
2. **BTC/USD** — flest trades (+148R, 86,7%)
3. **SOL/USD** — +115R, 95,1%
4. **XRP/USD** — 100% weekend (+102R)
5. **ETH/USD** — +80R, 96,4%
6. **ADA/USD** — +86R, 88,2%
7. **DOGE/USD** — 100% begge (+72R)

**Regel: Max 1 instrument pr. setup — det bedste A+ setup vinder.**

## Tider (DK — ALLE 7 DAGE)
| Vindue | Tid (DK) | Status |
|--------|----------|--------|
| **Primært vindue** | **15:00-23:00** | ✅ Høj volatilitet — handler kun her |
| Top-volatilitet | 16:00 + 23:00 (0,47%) | ✅ Bedst |
| Stærkt vindue | 17:00-19:00 (0,42-0,46%) | ✅ Godt |
| Godt vindue | 15:00 + 22:00 (0,41%) | ✅ Okay |
| **Død zone** | **07:00-12:00 (0,30-0,34%)** | ⛔ Undgå — bredest spreads |

## Strategi (samme DRT — ingen undtagelser)
1. **Dealing range på 1h:** sweep (raid) af swing high/low + relative equal levels på modsatte side
2. **Filter ≥ 5×ATR** (14-period ATR på 1h) — det vigtigste filter
3. **4 kvadranter:** 25DRT (discount) / 50DRT / 75DRT (premium)
4. **Entry:** Long ved 25DRT efter candle-lukning over · Short ved 75DRT efter candle-lukning under
5. **SL:** bag sweep-niveauet + 0,5×ATR buffer
6. **TP:** modsatte side af range (2-3R)

## Risk Management (legekonto)
- $50-100 konto: **2% risiko pr. trade**
- **Max 3 trades pr. dag**
- **2 tab i træk = stop for dagen**
- Ingen revenge trading · Ingen martingale · 5% dagligt drawdown-limit

## Skalering
1. Start: $50-100 legekonto
2. Ved **+20R**: øg risiko til 3%
3. Ved **+50R**: øg til 5% — eller flyt profit til hovedplanen
4. ALDRIG før +20R

## Daglig rutine (alle 7 dage)
| Tid (DK) | Handling |
|----------|----------|
| 14:30 | Scan alle 7 par på 1h — find DRT-ranges |
| 15:00-23:00 | Eksekver A+ setups (max 3) |
| Efter 23:00 | Journalfør alle trades |
| Fredag/søndag aften | Ugentlig opsummering + plan for ugen |

## Disciplin-regler
1. Ingen setup = ingen trade (2-3/dag er normalt)
2. Sænk aldrig filteret (under 5×ATR = WR falder)
3. SL flyttes aldrig
4. I tvivl = ingen trade
5. Undgå død zone 07:00-12:00
6. Journalfør alt
7. Kun A+ setups — sig nej til 80%

## Forventning
- ~20-28 trades/måned (alle 12 par)
- 88-92% WR → ~28 vindere (+2,5R) − 3 tabere (−3R) ≈ **+67R/måned**
- $100 @ 2% risiko: +$80/måned i starten — vokser med kontoen

## Scripts
- Backtest: `tradevault/scripts/backtest_krypto_all.py` (7 par) + nye par-test
- Data: `tradevault/tradevault.db` (12 par × 1h, 2 år)
