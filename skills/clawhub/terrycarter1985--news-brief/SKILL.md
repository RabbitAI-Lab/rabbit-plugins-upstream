---
name: news-brief
description: Generate structured daily news briefs by searching and summarizing latest public information on any topic. Supports tech news, policy updates, and custom topics.
license: MIT
allowed-tools:
  - web_search
  - web_fetch
metadata:
  openclaw:
    emoji: "📰"
    requires:
      bins:
        - python3
    categories:
      - research
      - summary
---

# News Brief Skill

Generate structured daily news briefs from the web. Search for latest news, fetch article previews, and compile into a professional brief with curated sections.

## When to Use

✅ **USE this skill when:**

- "Give me a briefing on tech news today"
- "What are the latest industry policies?"
- "Summarize the top news stories from today"
- "Show me trending topics in AI/tech"
- "Prepare a morning briefing on [topic]"

## Supported Briefing Types

### Global Tech News Brief
- Focus: Major tech companies, AI breakthroughs, venture capital, product launches, tech regulations
- Command: `news-brief tech` or `web_search: tech news latest developments`

### Industry Policy Brief
- Focus: Regulatory changes, government policies, legislation affecting specific industries
- Command: `news-brief policy` or `web_search: policy regulations changes for [industry]`

### Custom Topic Brief
- Focus: Any specific topic, theme, or keyword
- Command: `news-brief custom [topic]` or `web_search: [topic] news latest`

## Brief Structure

Each briefing includes:

1. **Overview** - 2-3 sentences summarizing the day's key developments
2. **Top Headlines** - 3-5 selected stories with sources and summaries
3. **Key Highlights** - Bullet points of important takeaways
4. **Trending Topics** - Emerging themes gathering momentum
5. **Sources & Links** - Links to original articles (when fetched)

## Implementation Workflow

This skill uses the `web_search` and `web_fetch` tools to:

1. **Search** - Use `web_search` to find latest public information on the specified topic
2. **Fetch** - Optionally use `web_fetch` to extract readable content from key articles
3. **Format** - Curate and structure the information into a coherent brief

## Example: Tech News Brief

```
User: Give me the latest tech news briefing

Assistant executes:
web_search(query="global technology news latest today 2026", count=10)
web_fetch(url="https://example.com/article1")
web_fetch(url="https://example.com/article2")
Then formats results into structured brief.
```

## Example: Policy Brief for Industry

```
User: What's the latest policy on semiconductor manufacturing?

Assistant executes:
web_search(query="semiconductor manufacturing policy regulations today 2026", count=10)
Then formats results into structured brief.
```

## Brief Output Format

```markdown
# 📰 [Brief Title]

---

## Overview
[2-3 sentences summarizing key developments]

## 📋 Top Headlines
1. **[Headline 1]**
   - Source: [URL]
   - Summary: [2-3 sentences]

2. **[Headline 2]**
   - Source: [URL]
   - Summary: [2-3 sentences]

## 🔑 Key Highlights
• [Highlight 1]
• [Highlight 2]
• [Highlight 3]

## 🔥 Trending Topics
• [Trend 1]
• [Trend 2]
• [Trend 3]

## 🔗 Sources
- [Source URL 1]
- [Source URL 2]
- [Source URL 3]
```

## Resources

### scripts/news_brief.py
Helper script that demonstrates how to structure search queries and output format.

Run directly for guidance:
```bash
python3 scripts/news_brief.py tech
python3 scripts/news_brief.py policy
python3 scripts/news_brief.py custom "climate tech"
```
