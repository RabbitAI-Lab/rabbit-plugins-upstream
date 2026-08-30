# Short-Form Market Research Brain

Your AI agent's brain for short-form video market research, powered by the [Virlo API](https://dev.virlo.ai).

## What This Skill Does

Gives your OpenClaw agent deep expertise in social media market research across TikTok, YouTube Shorts, and Instagram Reels. Everything runs through the unified **Content Research Agents API** (`POST /v1/agents`): set `is_recurring: false` for a one-shot niche search, or `is_recurring: true` for recurring monitoring — one resource, one set of read paths.

- **Niche Research** — Search any topic and get AI-generated intelligence reports covering trends, creators, platform dynamics, sentiment, and viral patterns
- **Creator Discovery** — Find rising creators who outperform their follower count, analyze any creator's profile and engagement metrics
- **Trend Tracking** — See what's trending across platforms right now, drill into hashtag performance
- **Ad Intelligence** — See what Meta ads are running for any topic or niche
- **Automated Monitoring** — Set up recurring agents that run daily, weekly, or monthly and self-optimize their keywords

> The older `/v1/orbit` and `/v1/comet` endpoints are **deprecated and will be removed on August 3, 2026** — migrate to `/v1/agents` (IDs are interchangeable).

## Install

```bash
clawhub install short-form-market-research-brain
```

## Setup

1. Get a Virlo API key at [dev.virlo.ai/dashboard](https://dev.virlo.ai/dashboard)
2. Add funds to your prepaid balance (minimum $10) at [dev.virlo.ai/dashboard/billing](https://dev.virlo.ai/dashboard/billing) — no subscriptions, balance never expires
3. Provide the key as the `VIRLO_API_KEY` environment variable. In `~/.openclaw/openclaw.json`:

```json5
{
  skills: {
    entries: {
      "short-form-market-research-brain": {
        env: { VIRLO_API_KEY: "virlo_tkn_YOUR_KEY" }
      }
    }
  }
}
```

The skill declares `VIRLO_API_KEY` as a required env var, so OpenClaw keeps it hidden until the key is configured — once set, it activates automatically.

## Example Prompts

- "Research the TikTok Shop niche — give me a full market analysis"
- "Find trending content about AI coding tools across all platforms"
- "Analyze the TikTok creator @username — how are they performing?"
- "What's trending on social media today?"
- "Set up weekly monitoring for wedding photography content"
- "Is this video an outlier? [paste URL]"
- "Show me the top performing hashtags on YouTube this week"
- "Find creators making content about personal injury law"
- "Compare what's working on TikTok vs YouTube for meal prep content"

## Pricing (1 credit = $0.01)

| Action | Cost |
|--------|------|
| Hashtag lookup | $0.05 |
| Sound detail / usage history | $0.05 |
| Sound search | $0.10 |
| Video digest / Trends / Tracking creation / Trending sounds / Breakout sounds | $0.25 |
| Agent one-shot search (`is_recurring: false`, full niche analysis) | $0.50 |
| Creator profile lookup | $0.50 |
| Video outlier analysis | $0.50 |
| Agent recurring monitor (`is_recurring: true`) | Free to create, $0.50 per run |
| Data Intelligence add-on (per search / run) | +$1.00 |
| Agent autonomy (activity, proposals, apply/dismiss/revert) | Free |
| Retrieving results (videos, ads, outliers, analysis, sounds) | Free |

## Links

- [API Documentation](https://dev.virlo.ai/docs)
- [Full API Reference for Agents](https://dev.virlo.ai/llms-full.txt)
- [Pricing](https://dev.virlo.ai/pricing)
- [Dashboard](https://dev.virlo.ai/dashboard)
