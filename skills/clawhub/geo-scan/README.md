# geo-scan — Answer-Engine Readiness Audit

One file. No API key. No account. No dependencies beyond the Python standard library.

`geo_scan.py` reads a public website the way an answer engine's crawler would and scores
**how readily engines such as ChatGPT search, Perplexity, Claude, Gemini / Google AI
Overviews and Copilot can fetch, parse and quote it**, on a 0–100 scale. It then lists
the changes that would raise the score. Version 1.2.3.

**Language coverage:** quotability scoring matches definitional, comparison and question
phrases in **English and German**. German patterns landed in 1.2.3, after a 45-site
Oldenburg batch showed all 45 scanned sites at ≤ 8/20 on that axis — a real gap, partly inflated
by an English-only phrase list. Re-scanning the 44 reachable URLs at `pages=2` moved sites at
≤ 8/20 from **44 to 39** and median quotability from **4.0 to 6.0**. Other languages
score lower on that axis, and the report notes the page language. Requests also
carry a fixed `Accept-Language: en,en-US;q=0.8,de;q=0.6` header.

```bash
python3 geo_scan.py https://self-attention.org --pages 6 --md report.md --json report.json
python3 geo_scan.py --url https://example.com --quiet; echo $?
```

## What it checks

| axis | max | what it looks at |
|---|---:|---|
| Crawler access | 20 | Whether `robots.txt` lets **search/retrieval agents** fetch the root and a few sampled pages: Googlebot, Bingbot, OAI-SearchBot, ChatGPT-User, PerplexityBot, Perplexity-User, Claude-SearchBot and Claude-User. **Training crawlers** (GPTBot, ClaudeBot, Google-Extended, Applebot-Extended, CCBot, Bytespider, Meta-ExternalAgent, Amazonbot, cohere-ai) are listed in the report but score nothing: blocking them is a legitimate policy and does not stop citation. **Gate:** if every search agent is blocked from the root, the total is the crawler score alone. |
| Machine readability | 15 | A sitemap, found via the robots.txt `Sitemap:` lines, `/sitemap.xml` or `/wp-sitemap.xml`. Sitemap indexes are expanded and gzip is supported. A sitemap with at least one page URL earns 7 points and `<lastmod>` coverage up to 4 more (11 points; the URL count is reported, not scored), plus `llms.txt` / `llms-full.txt` (4 points). llms.txt is a proposal with no confirmed consumer among the major engines, so it is weighted low. |
| Snippet permissions | 10 | `<meta name="robots">` (also `googlebot`, `bingbot`), `X-Robots-Tag`: `noindex`, `nosnippet`, `max-snippet:0`; `data-nosnippet` regions. These decide whether Google may quote a page. |
| Page structure | 25 | One `<h1>`, article-level JSON-LD (`Article`, `BlogPosting`, `QAPage`, …), meta description, author, word count, lists, canonical. |
| Quotability | 20 | Definitional phrases ("is defined as", "the difference between", "key takeaways"), hard figures (currency, %, measured units), comparison tables, question-form titles, `<h2>` sections. |
| Freshness | 10 | The median across sampled pages of each page's newest JSON-LD date, or the median sitemap `<lastmod>`. Future dates are discarded. |

Every score ships with the evidence line that produced it. A number without its evidence
is a vibe, and you cannot fix a vibe.

## Output and exit codes

Markdown report (score, grade, axis table, prioritised action list, per-page table,
notes) and JSON with the same facts for pipelines. Progress goes to stderr.

Grades: A ≥ 80 · B ≥ 65 · C ≥ 50 · D ≥ 35 · F below.

Exit 0 means a report was produced; a low score is a finding, not a failure. Exit 2 means
the scan or its output failed. That covers a DNS failure, a TLS certificate error, an
unreachable robots.txt, a robots.txt that disallows `geo-scan`, no analysable page, and a
`--json` / `--md` file that could not be written.
On a TLS certificate error the message says so: geo-scan never falls back to unverified
TLS. On macOS with a python.org Python, run `Install Certificates.command` once.

## How it behaves on your site

* User-Agent: `geo-scan/1.2.3 (+https://github.com/AureliusClaw/geo-scan; answer-engine readiness audit)`.
* It reads `robots.txt` first and obeys it for its own token `geo-scan` (and `*`) on every
  later request, redirect targets included. URLs it skips are listed in the report's Notes.
* It fetches the root page right after `robots.txt`. With a long `Crawl-delay`, optional
  requests (child sitemaps after the first, `llms-full.txt`) are skipped when they would
  leave too little time for pages; the Notes say so.
* It waits at least 1 s between requests, or longer if `Crawl-delay` asks for it. It stays
  on the audited host (with or without `www.`) and does not follow redirects off it. Downloads are capped (512 KiB robots.txt,
  1 MB llms.txt, 5 MB per sitemap, 2 MB per page), and a whole scan is capped at 120 s
  (`--budget`).
* At most 25 pages per run (`--pages`, default 8). A typical run makes 5–35 requests.
* **Opt out:** add this to your robots.txt:

  ```
  User-agent: geo-scan
  Disallow: /
  ```

## Honest limits

* **The weights are our judgement.** They have not been validated against observed
  citations. The score measures on-page readiness, not visibility. Whether an engine
  actually cites you depends on its index, competitors and the query. Measuring that needs
  probe runs against model APIs, which cost money and need a key; geo-scan stops at what
  is free and checkable.
* **An open robots.txt is not the same as being reachable.** CDN or WAF bot blocking (for
  example Cloudflare's AI-crawler blocking) acts on the crawler's user-agent and IP. It is
  invisible to this tool, which sends its own user-agent.
* **robots.txt matching** uses the stdlib `urllib.robotparser`. Rules are re-ordered so
  that first-match gives RFC 9309's longest-match, and a trailing `*` is understood.
  Wildcards in mid-path (`/*.pdf$`) are not, so they read as "allowed". When several
  groups name the same agent, only the first counts. Only the audited host's robots.txt
  is read: it is applied to every sampled path, including `www.` / apex variants that
  would strictly have their own robots.txt.
* **Quotability heuristics are English-only (documented v1 limitation).** Non-English
  pages score lower, near zero, on the phrase check; the report notes the page language
  when it is not English. The fixed `Accept-Language` header is English-first.
* **No JavaScript rendering.** Pages that are almost empty and script-heavy are flagged as
  probably JS-rendered. Most AI crawlers do not render JS either.
* **Single automated sample, no human review.** The score moves with the sample, so use the
  same `--pages` value for before/after comparisons. Read the Notes section.

## Hermes plugin

The repo root is also a Hermes plugin (`plugin.yaml`, `__init__.py`). It registers the
`geo_scan` tool with a 90 s budget, and it refuses hosts that resolve to private,
loopback or link-local addresses, redirects included. Scanning is read-only; with
`save=true` the tool also writes a Markdown and a JSON report to `out_dir` (default
`~/.hermes/cache/scratch/geo-scan`). The scoring engine is always the `geo_scan.py` next
to `__init__.py`; it cannot be overridden by environment variable or fallback path.

MIT licensed.
