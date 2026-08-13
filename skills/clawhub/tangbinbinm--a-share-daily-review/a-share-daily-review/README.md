# Global Market Daily Review (全球市场每日复盘)

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

> **v1.1** — Now covers 6 markets across the globe in a single report.

## Quick Start

1. Install: `pip install akshare pandas`
2. Say "今日复盘" or "A股日报" or "global market review"
3. Get a structured Markdown report in ~10 seconds

## Requirements

- Python 3.8+
- `pip install akshare pandas`

## Disclaimer

This skill presents market facts only. It does NOT provide investment advice.
