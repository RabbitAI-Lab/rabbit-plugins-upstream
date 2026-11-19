---
name: ai-news
description: Fetch and summarize the latest AI news from ai.codefather.cn/news (鱼皮AI导航 AI资讯) into a detailed, theme-grouped daily digest with per-article summaries and source links. Use this skill whenever the user asks for AI news, AI 日报, 最新 AI 资讯, 每日 AI 新闻, an AI news roundup, or wants to scrape/summarize AI-industry news from ai.codefather.cn / 鱼皮AI导航 for the latest or a specific date — even if they don't say "skill" or name the site, as long as the request is about collecting and summarizing AI news.
compatibility: Python 3.8+ with the standard library; network access to ai.codefather.cn is required. No API key, login, or browser needed.
---

# AI News Digest

## What this skill does

It fetches the newest AI news from **https://ai.codefather.cn/news** (鱼皮AI导航 · AI资讯), opens every article published on the latest date (or a date the user specifies), extracts the full text, merges duplicate coverage of the same event, and writes a detailed Chinese digest grouped by theme.

The site is a Next.js server-rendered app. The bundled script handles the non-obvious parts: pagination, date filtering, snowflake-ID date decoding, article-body extraction, and batching for long inputs. You supply the judgment: deduplication, summarization, grouping, and trend analysis.

## Quick start

Run the bundled script from this skill's directory:

```bash
python scripts/fetch_news.py
# use python3 if python is not available
```

Useful options:

| Option | Meaning |
| --- | --- |
| `--date YYYY-MM-DD` | Fetch a specific date (China time) instead of the latest date |
| `--out DIR` | Output directory (default: `./ai-news-output` in the current working directory) |
| `--max-pages N` | Safety limit for list pagination (default 15) |
| `--workers N` | Concurrent detail-page fetches (default 6) |
| `--batch-chars N` | Approximate characters per reading batch (default 9000) |
| `--max-articles N` | Optional cap for quick tests (0 = no cap); a capped run is marked `truncated` in `meta.json` |
| `--base-url URL` | Alternate mirror/proxy base URL |

The script writes into the output directory:

- `articles-<date>.json` — structured articles with full text, timestamps, site URL, and original-source URL
- `digest-input-<date>.md` — all articles in one readable file
- `batch-01.md`, `batch-02.md`, … — the same content split into readable chunks
- `meta.json` — target date, fetch time, counts, and any errors

The script uses only the Python standard library. It needs network access but no API key, login, cookie, or browser.

## Workflow

1. **Fetch.** Run the script. If the user did not give a date, let it find the latest available date. If the site has no articles for today (the listing often lags), it will use the newest date that actually has news.
2. **Read every batch.** Read all `batch-*.md` files before summarizing. Do not sample or skip batches — the point is full coverage. If there is only one batch, read it whole.
3. **Verify and deduplicate.** Check `meta.json`: `latest_available_date`, `matched_article_count`, `article_count`, `truncated`, and `errors`. Multiple outlets frequently cover the same event on this site (for example, three reports of the same API launch). Merge same-event reports into one story, note "合并 N 篇", and make the final count the number of distinct stories. Do not merge merely because two articles share a company name. `--max-articles` exists for quick tests; when `truncated` is true, label the digest as a sample and do not present it as the full day's coverage.
4. **Summarize each story in detail.** For every distinct story, write 3–6 sentences covering: what happened, the concrete numbers/model names/actors, the mechanism or technical detail that matters, and why it matters. Keep claims attributed ("据外媒报道", "官方称") when the source does. Never invent facts, dates, or figures not present in the fetched text.
5. **Group and add trends.** Group stories under the five themes in the template (adapt the headings if the day's news demands it), then add 4–5 trend bullets that connect stories rather than repeating them.
6. **Deliver.** Output the full digest in the chat and save it as `AI资讯日报-<date>.md` in the current working directory. If the user asked for no files, use the script's output directory as scratch and still deliver the digest in chat.

## Summary standards

- Prefer specifics over adjectives: "72 小时消耗 25 万亿 Token" beats "性能提升明显".
- Explain the mechanism when the article gives one: architecture, training method, pricing rule, policy boundary. That is what makes a summary useful rather than a headline list.
- Include the source link for every story. Use the site link from `articles-*.json`; add the original-source link when it adds verifiable context.
- State the site's latest available date and the fetch date in the header, especially when the latest date is not today.
- If an article body is short or truncated, summarize what is there and say so; do not pad with outside knowledge.
- Do not reproduce long passages verbatim. Summarize in your own words; short quoted phrases are fine.

## Output format

Follow `references/digest-template.md`. The structure is:

1. Title with date and weekday
2. Source line, fetch time, article count, and a note about merged duplicates
3. Theme sections, each with numbered stories and a paragraph summary
4. A "趋势观察" section with 4–5 cross-cutting bullets
5. A footer naming the scrape source

If the user writes in another language, write the digest in that language while keeping Chinese company/model names and titles accurate.

## Portability and privacy

This skill is designed to be shared. Keep it that way:

- Do not hardcode a home directory, username, drive letter, or absolute path in the skill or its scripts. The script defaults to a relative `./ai-news-output` and accepts `--out`.
- Do not add credentials, cookies, API keys, or personal data to the skill. The target site needs none.
- Do not commit generated digests or scraped article text into the skill folder; they are user data and may contain copyrighted or private content.
- If you extend the script, keep it standard-library-only unless a dependency is genuinely necessary, and document it in `SKILL.md`.

## Edge cases

- **Site unreachable or layout changed:** report the failure with the HTTP/parse error, and read `references/site-notes.md` before changing the parser. Do not silently return an empty digest.
- **No news for the requested date:** say so, report the latest date that does have news, and offer to fetch that date instead.
- **Very large day (30+ articles):** batch files keep reading manageable; summarize all distinct stories, but you may compress minor items to 2–3 sentences each while keeping the major stories detailed.
- **Duplicate stories:** merge by event, not by title similarity alone. Keep the richest source as the backbone and use the others to fill gaps or add differing numbers.
- **Paywalled or truncated original source:** the site's copy is the source of record for this task; note when the copy itself is incomplete.

## Maintenance

`references/site-notes.md` documents the page structure, date/pagination parameters, snowflake-ID scheme, and known quirks. Read it when the script fails or when you need to adapt the scraper to a site change.
