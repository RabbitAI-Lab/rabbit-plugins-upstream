---
name: geo-scan
description: Audit the answer-engine readiness (ChatGPT, Perplexity, Claude, Gemini, AI Overviews) of one public website URL and produce a prioritised fix list. Use when someone gives a public site or page URL and asks whether AI engines can crawl, cite or quote it, or wants its robots.txt / snippet-permission / schema check or quotability score. Not for - private or intranet hosts, JS-rendered SPAs, SEO keyword research, writing content to beat competitors. English and German quotability scoring. No API key, no account, Python stdlib only.
version: 1.2.3
license: MIT
permissions:
  network: outbound HTTP(S) GET only, public hosts, robots.txt obeyed, max 25 pages / 90 s
  filesystem: read plugin dir; write only report files under out_dir when save=true
  no_credentials: reads, sends and stores no credentials or secrets
metadata:
  author: Aurelius
  homepage: https://github.com/AureliusClaw/geo-scan
---

# geo-scan — answer-engine readiness audit

Scores a public website **0–100** for how readily an AI answer engine can crawl it,
parse it, and quote from it. Every score carries the evidence line that produced it,
so the report is checkable rather than advisory.

## When to use this skill

- "Can ChatGPT / Perplexity / Gemini see or cite my site?"
- "Why isn't my site showing up in AI answers?"
- "Review my robots.txt / llms.txt / schema.org / structured data."
- "Score how quotable this site is" for a given public URL.
- Before and after a content change, to measure whether answer-engine readiness moved.

Not for: private, intranet or loopback hosts (refused); JS-rendered SPAs (no JS
rendering, so the page reads as near-empty); SEO keyword research; writing content to
outrank competitors.

**Language coverage:** quotability scoring matches definitional, comparison and
question phrases in **English and German** (German patterns added in 1.2.3 after a
45-site Oldenburg batch showed all 45 scanned sites at ≤ 8/20 on that axis — a real gap,
partly an artefact of an English-only phrase list). Re-measured with the same URLs at
`pages=2` (44 sites re-scanned, 1 unreachable): sites at ≤ 8/20 fell **44 → 39**, median quotability **4.0 → 6.0**, median
total **61.6 → 62.4**. Other languages still score lower on that axis, and the report
notes the page language. The scan sends a fixed
`Accept-Language: en,en-US;q=0.8,de;q=0.6` header.

## How to run

```bash
python3 geo_scan.py https://example.com                      # report to stdout
python3 geo_scan.py --url https://example.com --pages 20 \
        --md audit.md --json audit.json                      # save both
python3 geo_scan.py https://example.com --quiet              # no output, exit code only
```

Exit 0: a report was produced. A low score is a finding, not a failure. Exit 2: nothing
usable could be fetched (DNS or TLS failure, unreachable robots.txt, robots.txt
disallows `geo-scan`, or no analysable page). The reason goes to stderr unless `--quiet`.

Inside a Hermes session with the plugin installed, the same audit is the
`geo_scan` tool: `{ "url": "https://example.com", "pages": 12, "save": true }`.
The plugin refuses private, loopback and link-local hosts and stops after 90 s.

## What it checks (100 points; the weights are our judgement, not validated against citations)

| axis | pts | what earns it |
|---|---|---|
| Crawler access | 20 | robots.txt lets search/retrieval agents (Googlebot, Bingbot, OAI-SearchBot, ChatGPT-User, PerplexityBot, Perplexity-User, Claude-SearchBot, Claude-User) fetch the root and sampled pages. Training crawlers (GPTBot, ClaudeBot, Google-Extended, CCBot, …) are reported but not scored. If every search agent is blocked, the total is this axis alone. |
| Machine readability | 15 | a sitemap (robots.txt `Sitemap:`, `/sitemap.xml`, `/wp-sitemap.xml`) with `<lastmod>` coverage; `llms.txt` / `llms-full.txt` (4 pts, speculative) |
| Snippet permissions | 10 | no `noindex` / `nosnippet` / `max-snippet:0` in meta robots or `X-Robots-Tag`; `data-nosnippet` costs a little |
| Page structure | 25 | one `<h1>`, article-level schema.org JSON-LD, meta description, author, ≥300 words, lists, canonical |
| Quotability | 20 | definitional phrases, hard figures, tables, question-form titles, `<h2>` sections (English + German phrase lists) |
| Freshness | 10 | median of each sampled page's newest JSON-LD date (else median sitemap `<lastmod>`); future dates discarded |

Grades: A ≥ 80 · B ≥ 65 · C ≥ 50 · D ≥ 35 · F below.

## Output contract

Markdown report: score, grade, one table row per axis with `score / max / status /
evidence`, then a prioritised action list (high/medium/low), then a per-page table
(url, words, h1 count, schema types, figure hits, quotable hits, robots directives),
then notes. JSON mirrors the same structure. Keep the evidence column in anything you
hand to a client — it is the part that can be re-checked.

## Limits worth stating up front

- **Quotability scoring covers English and German phrases** (German added in 1.2.3): other
  pages score lower on that axis; the report notes the page language.
- Read-only HTTP GETs of public pages (the plugin's `save=true` additionally writes the
  Markdown + JSON report to `out_dir`). `--pages` defaults to 8 and is clamped to 1–25.
  geo-scan obeys robots.txt for `geo-scan`, waits at least 1 s between requests (more if
  `Crawl-delay` asks), stays on the audited host, caps downloads, and caps a scan at
  120 s (`--budget`).
- It measures **technical** readiness, not whether an engine actually cites the site.
- CDN or WAF bot blocking (e.g. Cloudflare's AI-crawler blocking) is invisible to it: an
  open robots.txt does not prove crawlers get through.
- There is no JS rendering; near-empty, script-heavy pages are flagged.
- It is a single automated sample with no human review. Use the same `--pages` value for
  before/after comparisons.
- Sent with `User-Agent: geo-scan/1.2.3 (+https://github.com/AureliusClaw/geo-scan; answer-engine readiness audit)`,
  so a site owner can find this run in their own logs. They can opt out with
  `User-agent: geo-scan` / `Disallow: /`.
