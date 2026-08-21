---
name: "drt-market-lens"
description: "Live market data + ICT bias for 17 instruments (indices, forex, metals, crypto) via the x402 pay-per-call API. Get 1h klines, premium/discount zones and daily bias — directly in your agent."
metadata: {"clawbot": {"requires": {"python3": true, "network": ["https://186.240.156.169:8791"], "env": ["X402_API_KEY"]}}}
---

# DRT Market Lens 🔭📊

Real-time market data + ICT bias for 17 symbols (SP500, NAS100, DJ30, EURUSD, XAUUSD, BTCUSD, ETHUSD + more).

## Security 🔒
- The API key is **spending-capable** (pays per call) — it is only sent over **HTTPS**.
- Default endpoint is HTTPS. Override with `X402_BASE` if you self-host the API.
- NEVER use HTTP without understanding the risk: set `X402_ALLOW_HTTP=1` only on a secure/local network.

## Commands

```bash
export X402_API_KEY=sk-...   # get it at https://github.com/MohamedAbdisamed/x402-api
# (optional) point to your own HTTPS endpoint:
export X402_BASE=https://api.your-server.dk:8791

# Market data (1h klines, 17 symbols)
python3 scripts/market.py --symbol SP500 --limit 50

# ICT bias (premium/discount + SMA50/200)
python3 scripts/bias.py --symbol SP500
```

## Payment
Pay-per-call via x402 (USDC on Base). Get a key: POST /v1/purchase on the API.

## Symbols
SP500 · NAS100 · DJ30 · UK100 · EURUSD · GBPUSD · USDJPY · USDCHF · XAUUSD · XAGUSD · BTCUSD · ETHUSD · BNBUSD · SOLUSD · XRPUSD · DOGEUSD · ADAUSD
