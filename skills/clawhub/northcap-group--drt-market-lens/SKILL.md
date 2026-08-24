---
name: "drt-market-lens"
description: "DRT/ICT market analysis framework: 1h klines, premium/discount zones and daily bias for 17 instruments (indices, forex, metals, crypto). 100% lokal analyse — ingen netværkskald, ingen API-nøgle."
metadata: {"clawbot": {"requires": {"python3": true}, "notes": "100% lokal analyse — ingen netværkskald, ingen API-nøgle."}}
---

# DRT Market Lens 🔭📊

Real-time market data + ICT bias for 17 symbols (SP500, NAS100, DJ30, EURUSD, XAUUSD, BTCUSD, ETHUSD + more).

## Security 🔒
- The API key is **spending-capable** (pays per call) — it is only sent over **HTTPS**.

## Commands

```bash
# (optional) point to your own HTTPS endpoint:

# Market data (1h klines, 17 symbols)
python3 scripts/market.py --symbol SP500 --limit 50

# ICT bias (premium/discount + SMA50/200)
python3 scripts/bias.py --symbol SP500
```

## Payment

## Symbols
SP500 · NAS100 · DJ30 · UK100 · EURUSD · GBPUSD · USDJPY · USDCHF · XAUUSD · XAGUSD · BTCUSD · ETHUSD · BNBUSD · SOLUSD · XRPUSD · DOGEUSD · ADAUSD
---
