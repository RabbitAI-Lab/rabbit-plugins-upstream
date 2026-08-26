# Global Market Daily Review (全球市场每日复盘) v1.2

Zero-config global market daily review generator. Uses public akshare data — no API keys needed.

## Features

- 🇨🇳 **A-Shares**: 6 major indices + market sentiment + sector leaders/laggards TOP 5
- 🔥 **Concept Boards**: Hot concepts TOP 5 (dual data source with auto-failover)
- 🚀 **Limit-Up Analysis**: Streak height, tier structure, industry
- 💰 **Dragon-Tiger Board**: TOP 5 net buyers
- 🇭🇰 **Hong Kong**: Hang Seng / HSCEI / HSCCI / HSTECH indices
- 🇺🇸 **US Markets**: DJIA / NASDAQ / S&P 500
- 🌏 **Asia-Pacific**: Nikkei 225 / KOSPI / Taiwan Weighted
- 🇪🇺 **Europe**: FTSE 100 / DAX / CAC 40
- 💵 **North-bound Capital Flow**: Shanghai & Shenzhen Connect net inflow
- 🔒 All data stays local, zero telemetry
- 🧭 **Deterministic insights**: fact-only summaries, board move alerts and data quality counts
- 📋 **Plain text mode**: copy-friendly output with `--format plain`

> **v1.2** — Adds deterministic insights and copy-friendly plain text output while preserving the v1.1 JSON sections.

## Quick Start

1. Install: `pip install akshare pandas`
2. Say "今日复盘" or "A股日报" or "global market review"
3. Get a structured Markdown report in ~10 seconds

For a copy-friendly text version:

```bash
python3 daily_review.py --format plain
```

## Requirements

- Python 3.8+
- `pip install akshare pandas`

## Disclaimer

This skill presents market facts only. It does NOT provide investment advice.
