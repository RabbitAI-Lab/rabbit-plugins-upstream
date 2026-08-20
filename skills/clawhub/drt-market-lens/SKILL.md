---
name: "drt-market-lens"
description: "Live market data + ICT bias for 17 instruments (indices, forex, metals, crypto) via the x402 pay-per-call API. Get 1h klines, premium/discount zones and daily bias — directly in your agent."
---

# DRT Market Lens 🔭📊

Realtids-markedsdata + ICT-bias for 17 symboler (SP500, NAS100, DJ30, EURUSD, XAUUSD, BTCUSD, ETHUSD + flere).

## Kommandoer

```bash
export X402_API_KEY=sk-...   # fås på https://github.com/MohamedAbdisamed/x402-api

# Markedsdata (1h-klines, 17 symboler)
python3 scripts/market.py --symbol SP500 --limit 50

# ICT-bias (premium/discount + SMA50/200)
python3 scripts/bias.py --symbol SP500
```

## Betaling
Pay-per-call via x402 (USDC på Base). Få nøgle: POST /v1/purchase på API'et.

## Symboler
SP500 · NAS100 · DJ30 · UK100 · EURUSD · GBPUSD · USDJPY · USDCHF · XAUUSD · XAGUSD · BTCUSD · ETHUSD · BNBUSD · SOLUSD · XRPUSD · DOGEUSD · ADAUSD
