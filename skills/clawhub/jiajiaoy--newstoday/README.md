# NewsToday — Daily News Briefing Skill

> Get 10 curated stories in 5 minutes. Hero story deep-dive · financial impact ratings · morning & evening push · breaking alerts.

[![clawhub](https://img.shields.io/badge/clawhub-newstoday-blue)](https://clawhub.ai/skills/newstoday)
[![version](https://img.shields.io/badge/version-2.3.3-green)](https://clawhub.ai/skills/newstoday)
[![license](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE)

## What it does

NewsToday is an [OpenClaw](https://openclaw.ai) skill that delivers a personalized daily news briefing without you having to read anything. Every morning it picks the 10 most important stories, gives the top one a full **Hero Story** treatment (context + analysis + financial impact), and rates each finance/market story with 📈📉➡️ so you immediately know what moved the needle.

**Morning briefing** — 10 curated stories, 1 Hero Story deep-dive, financial impact ratings  
**Evening briefing** — day recap + what to watch tomorrow  
**Breaking alerts** — checked every 2 hours, only fires on genuinely significant events  
**RSS aggregation** — pull in your own feeds on top of default sources  
**AI briefing mode** — dedicated mode for LLM/AI industry news  
**Personalization** — weight topics you care about (tech / finance / geopolitics / military)

Fully bilingual: **Chinese and English**.

## Data sources

| Source | What it covers |
|---|---|
| 微博热搜 | China trending topics |
| 知乎热榜 | China in-depth discussions |
| 百度热搜 | China general news |
| X (Twitter) | Global trending |
| Google News | International headlines |
| Hacker News | Tech & startup news |
| Reuters / AP | Breaking international news |
| 36Kr / The Paper | China tech & business |

## Installation

```bash
openclaw install newstoday
```

Or search `newstoday` on [clawhub.ai](https://clawhub.ai).

## Usage

```bash
# Morning briefing (on-demand, no setup needed)
openclaw run newstoday morning

# Evening briefing
openclaw run newstoday evening

# Enable daily push (Telegram / Slack / Feishu / Discord)
openclaw run newstoday push-on <userId> --morning 08:00 --evening 20:00 --channel telegram

# Breaking news check
openclaw run newstoday breaking

# AI/LLM news mode
openclaw run newstoday morning --lang en   # triggers AI briefing for tech topics

# Personalize topic weights
node scripts/preference.js set <userId> 财经 0.9
node scripts/preference.js set <userId> 娱乐 0.2
```

## Ecosystem

Part of the **OpenClaw Smart Consumer** skill suite:

| Skill | Description |
|---|---|
| **NewsToday** | Daily news briefing ← you are here |
| [TrendRadar](https://github.com/jiajiaoy/TrendRadar) | Detect trending products from news + social media |
| [BuyWise](https://github.com/jiajiaoy/BuyWise) | Shopping decision: buy / wait / skip |
| [CouponClaw](https://github.com/jiajiaoy/CouponClaw) | Find coupons and stack cashback |
| [TravelHound](https://github.com/jiajiaoy/TravelHound) | Flight and hotel price comparison |

## Trigger phrases

- **English voice queries:** "morning news brief", "daily news digest", "what happened today", "tech news brief", "AI news brief", "financial news today", "breaking news now", "track <topic> news", "Chinese news roundup", "what's trending"
- **中文:** 早报、晚报、今天新闻、新闻摘要、热搜、AI 早报、追踪 XX、突发、有什么大事
- **日本語:** 今日のニュース、朝刊
- **한국어:** 오늘 뉴스, 모닝 브리핑
- **Tiếng Việt:** tin tức hôm nay

## When to use a different skill

| Need | Use |
|---|---|
| Only CCTV / 新闻联播 | [cctv-news-fetcher](https://clawhub.ai/skills/cctv-news-fetcher) |
| Only X (Twitter) posters | [x-news-daily](https://clawhub.ai/skills/x-news-daily) |
| Only military news | [military-news-collector](https://clawhub.ai/skills/military-news-collector) |
| Generic personalized news (no aggregation logic) | [news](https://clawhub.ai/skills/news) |

NewsToday is for the **broad daily-brief + Hero Story + multi-source aggregation** niche.

## Keywords

daily news brief · morning briefing · news digest · news aggregator · breaking news alert · AI news brief · tech news digest · financial news · topic tracking · trending topics · Hero Story · hot list aggregator · RSS news · 早报 · 晚报 · 新闻摘要 · 今日新闻 · 热榜 · 突发新闻 · 微博热搜 · 知乎热榜 · AI早报 · 财经早报 · 话题追踪 · 朝刊 · 오늘 뉴스 · tin tức hôm nay

---

Built for [OpenClaw](https://openclaw.ai) · Published on [clawhub.ai/skills/newstoday](https://clawhub.ai/skills/newstoday)
