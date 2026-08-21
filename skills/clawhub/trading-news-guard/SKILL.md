---
name: "trading-news-guard"
description: "Paid news-status check before trading: fetch live high-impact event data (NFP/CPI/FOMC) via the x402 pay-per-call API and see if a blackout window is active. The agent decides whether to trade — the skill provides the data. ⚠️ PAID external API call."
metadata: {"clawbot": {"requires": {"python3": true, "network": ["https://186.240.156.169:8791"], "env": ["X402_API_KEY"]}}}
---

# Trading News Guard 🛡️📰

Fetch live high-impact event data before entry — NFP/CPI/FOMC status via a paid external API.

## ⚠️ Important (read first)

- **PAID API call:** every run costs money (x402, USDC on Ethereum) and sends your API key + query to an external service at a raw-IP endpoint.
- **This skill provides DATA, not enforcement.** It fetches the news status — your agent must decide whether to skip the trade. Do not assume safety is guaranteed.
- **Fail closed:** if the API is unreachable, treat it as a blackout (do not trade) rather than proceeding.

## Why it is critical

High-impact news (NFP, CPI, FOMC, ECB) can move the market 50-200+ points in seconds. Even perfect DRT/ICT setups get run over if you are in a position during a news candle. Professional traders close positions or wait — your agent should do the same.

## Command

```bash
# 1) Set your API key (get it at https://github.com/MohamedAbdisamed/x402-api)
export X402_API_KEY=***

# 2) Check news status BEFORE entry
python3 scripts/news_check.py
```

## Output (example)

```json
{
  "status": "blackout" | "clear",
  "current_event": "CPI m/m — High Impact",
  "next_events": [
    {"name": "FOMC Statement", "impact": "High", "time": "19:00 UTC"}
  ]
}
```

## Use in your agent (pseudo-code)

```python
news = check_news()                      # calls the API
if news["status"] == "blackout":
    skip_trade("News blackout: " + news["current_event"])
else:
    place_trade()                        # only when the market is clear
```

## Payment

Pay-per-call via x402 (USDC on Base/Ethereum/BSC). Pay per call — no subscription needed for sporadic use. Bulk users can choose a monthly plan.

## Files

```
trading-news-guard/
├── SKILL.md
└── scripts/
    └── news_check.py   # x402 client: GET /v1/news
```

## Rules
- ALWAYS check news before entry — especially in London/NY windows (08:00-17:00 CET)
- Blackout = no new position. The period typically lasts 5-30 min around the event
- Exception: if your strategy explicitly trades news (not DRT/ICT) — then use this skill to KNOW when it happens
