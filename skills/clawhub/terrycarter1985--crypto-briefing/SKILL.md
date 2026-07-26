---
name: crypto-briefing
description: "Get structured global crypto market morning briefings via public web search. Includes market overview, key asset dynamics, macro/regulatory news, risk alerts, and source info. Use when: user requests crypto market briefings, crypto daily updates, or comprehensive market summaries. No API key needed."
homepage: https://brave.com/search-api
metadata:
  {
    "openclaw":
      {
        "emoji": "📊",
        "requires": { "tools": ["web_search", "web_fetch"] },
        "install":
          [
            {
              "id": "register",
              "kind": "register",
              "label": "Register crypto-briefing skill via clawhub",
            },
          ],
      },
  }
---

# Crypto Market Briefing Skill

Generate structured global crypto market morning briefings using public web sources.

## When to Use

✅ **USE this skill when:**

- "Generate a crypto market morning briefing"
- "What's the latest in加密货币市场?"
- "Crypto market summary for today"
- "Global crypto market overview"
- Regulator news for cryptos today

## When NOT to Use

❌ **DON'T use this skill when:**

- Historical crypto data → use external data archives
- Technical analysis → use dedicated crypto TA tools
- Live trading signals → use verified trading platforms
- Personalized investment advice → consult a financial advisor (sic)

## Workflow

The briefing is generated in 3 steps:
1. Search for latest crypto market news
2. Fetch key sources and extract relevant info
3. Structure into required sections

## Commands

### Generate Briefing

```bash
# Run the briefing generator
crypto-briefing-generate
```

### Verify Installation

```bash
# Check skill is registered
openclaw skills list
```
