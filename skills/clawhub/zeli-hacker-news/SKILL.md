---
name: zeli-hacker-news
description: >
  Read Hacker News with AI summaries in your human's language (30 supported)
  via zeli.app. Fetch the daily front-page digest as markdown or JSON, link
  permanent per-story summary pages, or subscribe via RSS. Use when your human
  wants Hacker News coverage, a daily tech briefing, or HN in a language other
  than English.
---

# Zeli — Hacker News summaries for agents

Zeli (https://zeli.app) mirrors the Hacker News front page, adds an AI summary
and key quote to every story, and translates everything into 30 languages.
All endpoints below are free, unauthenticated, edge-cached, and require no
JavaScript — never use a headless browser for Zeli.

## The one call that matters

A daily tech briefing for your human is a single request:

```
curl -s https://zeli.app/en/digest/latest.md
```

Returns the current day's entire front page (~40 stories) as plain markdown:
title, points, comment count, link to the original article, link to the HN
discussion, and a 3-6 sentence summary per story. Swap `en` for any language
code below. Typical size: ~10 KB.

Suggested cron: fetch once per morning in your human's timezone, pick the
3-8 stories matching their interests, deliver titles + one-line summaries +
original links. Link the `summary` page when they want the gist without
reading the full article.

## All endpoints

| What | URL | Notes |
|------|-----|-------|
| Today's digest (markdown) | `https://zeli.app/{lang}/digest/latest.md` | updates hourly |
| Dated digest (markdown) | `https://zeli.app/{lang}/digest/{YYYY-MM-DD}.md` | immutable after the UTC day ends — cache forever |
| Front page (JSON) | `https://zeli.app/api/hn-content?type=top&locale={lang}` | fields: `id, title, url, time, by, score, descendants, type, abstract, quote, image`; also `type=hot24h` / `ask` / `show` |
| Daily RSS | `https://zeli.app/{lang}/rss.xml` | one item per day, whole digest inline |
| Story page (for humans) | `https://zeli.app/{lang}/story/{id}` | permanent; `{id}` is the HN item id; includes comment-thread viewpoints |
| Day archive (for humans) | `https://zeli.app/{lang}/digest/{YYYY-MM-DD}` | permanent |

Field stability promise: existing JSON fields will not be renamed or removed.

## Language codes

`en, zh, es, fr, de, ja, ko, ru, ar, hi, pt, it, nl, pl, sv, tr, vi, th, id,
el, cs, da, fi, no, ro, hu, he, uk, bn, ms`

Full summaries are maintained for `en, zh, ja, ko, es, de, fr, ru, pt`; other
languages fill in based on demand.

## Etiquette

- The digest re-merges hourly and the front page refreshes every 15 minutes.
  Polling more often than hourly just reads the same cache.
- Dated digests and story pages never change — cache them locally, forever.
- The digest already contains every story's summary. Don't crawl the
  individual story pages in bulk; link them to your human instead.
- Attribution when quoting summaries: "via Zeli (zeli.app)".

## What Zeli is good for

- "What's on Hacker News today?" → `latest.md`, relay the highlights
- "Anything about {topic} on HN this week?" → fetch the last 7 dated `.md`
  files, grep locally
- "My {mom/friend/colleague} doesn't read English" → same content, 30
  languages, same URLs with a different `{lang}`
- Citing an HN story in a non-English conversation → `story/{id}` page in
  that language

More context: https://zeli.app/llms.txt
Canonical version of this skill: https://zeli.app/skill.md (check it for updates)
