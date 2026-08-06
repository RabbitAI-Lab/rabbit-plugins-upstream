---
name: zai-search
description: "Free live web search powered by Z.AI GLM-4.5-Flash with built-in web_search tool. Real-time results, real URLs, zero cost. Works with Z.AI Coding Plan keys — no separate API balance required."
homepage: https://docs.z.ai/guides/tools/web-search
metadata: {"clawdbot":{"emoji":"🔍","requires":{"bins":["node"],"env":["ZAI_API_KEY"]},"primaryEnv":"ZAI_API_KEY"}}
---

# Z.AI Web Search (Free)

**Free live web search using GLM-4.5-Flash with Z.AI's built-in `web_search` tool.**

Real-time web results with real URLs — not training data, not hallucinations. Zero cost: uses the free Flash model tier with integrated web access. No separate Web Search API balance needed.

## Why This Skill

| Problem | Solution |
|---|---|
| Z.AI Web Search API requires paid balance | Uses GLM-4.5-Flash (free) with built-in `web_search` tool |
| Web scraping from servers gets blocked | Search runs through Z.AI's infrastructure |
| Other search skills need API keys + payment | Works with existing Coding Plan API key |
| Models hallucinate URLs | GLM returns only real search results |

## Requirements

- **Node.js** 18+ (native `fetch` + ESM)
- **ZAI_API_KEY** — any valid Z.AI API key (Coding Plan works)

## Usage

```bash
# Basic search
node scripts/search.mjs "latest pfSense release notes"

# Limit results (default: 10, max: 20)
node scripts/search.mjs "Home Assistant integrations" -n 5

# Domain filter
node scripts/search.mjs "VPN setup" --domain netgate.com

# Raw mode — faster, no summarization
node scripts/search.mjs "python asyncio tutorial" --raw
```

## How It Works

```
User Query
    │
    ▼
GLM-4.5-Flash (free model)
    │
    ├──► web_search tool (live results from Z.AI infrastructure)
    │
    ▼
Structured Output
    ├── Sources with real URLs
    ├── Brief summaries per result
    └── Combined analysis
```

1. Query goes to GLM-4.5-Flash with `tools: [{type: "web_search", web_search: {enable: true}}]`
2. Z.AI performs a real live web search server-side
3. GLM structures the results with titles, URLs, and summaries
4. Returns Markdown-formatted output in the query's language

## Features

- 🔍 **Live search** — real-time web results, not cached training data
- 💰 **Zero cost** — GLM-4.5-Flash is free, web_search tool is included
- 🌍 **Multilingual** — responds in the query's language automatically
- 🎯 **Domain filter** — restrict results to specific sites
- 📋 **Raw mode** — skip summarization for faster output
- 🚫 **No hallucination** — if nothing is found, says so honestly
- 🔑 **Coding Plan compatible** — works with Z.AI Coding Plan API keys

## Limitations

- Results depend on Z.AI's search index — obscure topics may return nothing
- GLM-4.5-Flash may occasionally misattribute dates in summaries
- Rate limits follow your Z.AI plan's standard quotas
