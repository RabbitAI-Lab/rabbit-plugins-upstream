---
name: reddit-post-search
description: "Extracts Reddit posts from keyword search, subreddit browsing, or direct Reddit URLs. Input: search query, subreddit name, or direct reddit.com URL with sort (relevance/hot/top/new/comments), timeframe (hour/day/week/month/year/all), limit, pagination cursor, optional date range, NSFW flag, and strict token filter. Output: structured JSON per post with 40+ fields — id, title, body, author, score, upvote_ratio, num_comments, subreddit, created_utc, url, permalink, flair, media fields, and derived engagement metrics. Use when user mentions Reddit, subreddit, r/, reddit posts, scrape Reddit, Reddit data, monitor Reddit, Reddit search, collect posts, Reddit feed, karma, upvotes, Reddit thread, community posts, reddit.com, search Reddit, Reddit keyword search, subreddit monitoring, Reddit scraper, get posts from Reddit, pull Reddit, hot posts, new posts, top posts, Reddit discussions, Reddit content."
---

# Reddit — Post Search

> Query or URL → structured post records with 40+ fields per item

## Language

All process output to user (progress updates, process notifications) follows the user's language.

## Objective

Collect Reddit post records from keyword search, subreddit listings, or direct Reddit URLs using Reddit's public JSON API, returning structured data ready for analysis or pipeline consumption.

## Prerequisites

- A reddit.com page is open in the browser

## Pre-execution Checks

### 1. Tool Readiness

If browser-act has been confirmed available in the current session → skip this step.

Invoke `browser-act` via Skill tool to load usage. If installation or configuration issues arise, follow its guidance to resolve then retry.

## Capability Components

> This Skill's operational boundary = what the user can manually do in their browser. It only reads data already displayed to the user on the page, never bypassing authentication or access controls. Its role is equivalent to copy-pasting on the user's behalf — the data is already on screen, automation merely saves time. JS code is encapsulated in Python files under the `scripts/` directory, invoked via `eval "$(python scripts/xxx.py {params})"`. `$(...)` is bash syntax; it is recommended to use the bash tool for execution.

Below are all atomic capabilities discovered and verified during the exploration phase, listed by command template with parameters. Simply invoke them as needed — no need to read `scripts/*.py` source code or re-verify. Only inspect scripts when execution fails for troubleshooting. Combine freely as needed during execution.

### API: Fetch one page of Reddit posts

```bash
eval "$(python scripts/search-posts.py --query '{keywords}' --sort relevance --timeframe all --limit 100)"
```

Parameters:
- `--query`: search phrase (required when no `--subreddit` or `--url` is provided)
- `--subreddit`: subreddit name without `r/` prefix; combine with `--query` for subreddit-scoped search, or omit `--query` for full subreddit listing
- `--sort`: ranking order — `relevance` (default) | `hot` | `top` | `new` | `comments`
- `--timeframe`: Reddit time window — `all` (default) | `year` | `month` | `week` | `day` | `hour`
- `--limit`: posts per page, 1–100 (default: `100`)
- `--after`: pagination cursor — `after` value from the previous response (default: empty = first page)
- `--include-nsfw`: include NSFW posts — `true` | `false` (default: `false`)
- `--date-from`: lower date bound applied at record level — ISO-8601 or `YYYY-MM-DD` (default: empty)
- `--date-to`: upper date bound applied at record level — ISO-8601 or `YYYY-MM-DD` (default: empty)
- `--strict-token-filter`: keep only posts whose title+body+url contain every query token — `true` | `false` (default: `false`)
- `--url`: direct Reddit URL (post page, subreddit page, search page, or user page) — overrides `--query` and `--subreddit`
- `--query-label`: custom label for the `query` field in output records (default: same as `--query`)

Output example:
```json
{
  "posts": [
    {
      "kind": "post",
      "query": "ai tools",
      "id": "1s80pf6",
      "title": "You don't need to pay for AI tools right now",
      "body": "nobody told me how much was just sitting there for free.",
      "author": "AdCold1610",
      "score": 756,
      "upvote_ratio": 0.97,
      "num_comments": 173,
      "subreddit": "PromptEngineering",
      "created_utc": "2026-06-01T10:09:56.000Z",
      "url": "https://www.reddit.com/r/PromptEngineering/comments/1s80pf6/you_dont_need_to_pay_for_ai_tools/",
      "permalink": "/r/PromptEngineering/comments/1s80pf6/you_dont_need_to_pay_for_ai_tools/",
      "canonical_url": "https://www.reddit.com/r/PromptEngineering/comments/1s80pf6/you_dont_need_to_pay_for_ai_tools/",
      "old_reddit_url": "https://old.reddit.com/r/PromptEngineering/comments/1s80pf6/you_dont_need_to_pay_for_ai_tools/",
      "flair": "Tutorials and Guides",
      "post_hint": "self",
      "over_18": false,
      "is_self": true,
      "spoiler": false,
      "locked": false,
      "is_video": false,
      "is_gallery": false,
      "hidden": false,
      "edited": false,
      "archived": false,
      "pinned": false,
      "domain": "self.PromptEngineering",
      "thumbnail": "self",
      "url_overridden_by_dest": null,
      "num_duplicates": 0,
      "subreddit_id": "t5_2rc7j",
      "subreddit_name_prefixed": "r/PromptEngineering",
      "subreddit_subscribers": 368624,
      "media": null,
      "age_hours": 312.5,
      "retrieved_at": "2026-07-14T08:20:02.983Z",
      "has_media": false,
      "gallery_count": 0,
      "outbound_url_host": null,
      "title_length": 44,
      "body_length": 512,
      "word_count": 95,
      "score_per_hour": 2.42,
      "comments_per_hour": 0.55,
      "is_deleted_or_removed": false,
      "engagement_total": 929,
      "comment_to_score_ratio": 0.2291,
      "is_high_engagement": false,
      "stickied": false,
      "distinguished": null,
      "score_hidden": false,
      "total_awards_received": 0,
      "gilded": 0,
      "num_crossposts": 0,
      "is_original_content": false,
      "author_fullname": "t2_dr3vyilor",
      "author_flair_text": null,
      "author_premium": false,
      "crosspost_parent_list": null
    }
  ],
  "after": "t3_1ujtb4c",
  "count": 100,
  "has_more": true
}
```

## Enum Parameters

[API] sort — Hardcoded values, no API retrieval needed: `relevance` | `hot` | `top` | `new` | `comments`

[API] timeframe — Hardcoded values, no API retrieval needed: `all` | `year` | `month` | `week` | `day` | `hour`

## Pagination

**API Pagination**: `--after`, type: cursor, start value: empty (omit for first page). Next page value: `after` field in response. Termination: `has_more` is `false` or `after` is `null`.

## Success Criteria

`result.count >= 1` and `result.posts[0].id` is a non-empty string and `result.posts[0].title` is non-null

## Known Limitations

- Reddit's public search caps practical result windows at roughly 250–1,000 posts per query/sort combination regardless of the number of pages requested; this is a Reddit platform limit, not a script limit
- `--timeframe` narrows Reddit's source query; `--date-from` / `--date-to` apply exact filtering at the record level after fetch and may reduce returned count
- Anonymous (non-logged-in) API access is subject to Reddit's 60 requests/minute rate limit; add 1–2 second delays between page requests for large batches
- `--sort relevance` and `--sort top` are only meaningful when a `--query` is provided; for subreddit listings without a query use `--sort hot` or `--sort new`

## Execution Efficiency

- **Batch orchestration**: Write a bash script to loop through the command templates serially within a single session; do not parallelize within one browser. Add 1–2 second delays between pages to respect the rate limit. For higher throughput, distribute pages across multiple parallel browser sessions — each session maintains independent browser context and network state, so request volume spreads naturally across sessions
- **Test before batch execution**: After writing a batch script, you must first test with 1-2 items to verify the script runs correctly; only then run the full batch. Never skip testing and execute in batch directly
- **Reduce redundant pre-operations**: When multiple steps depend on the same prerequisite state, complete them in batch under that state to avoid repeatedly establishing the same state
- **Error resumption**: Save results item by item during batch processing; on failure, resume from the breakpoint rather than starting over

## Experience Notes

Path: `{working-directory}/browser-act-skill-forge-memories/reddit-search-scraper-reddit-post-search.memory.md` (working directory is determined by the Agent running the Skill, typically the project root or current working directory)

**Before execution**: If the file exists, read it first — it records unexpected situations encountered during past executions (e.g., a strategy has become ineffective); adjust strategy order accordingly.

**After execution**: If an unexpected situation is encountered (strategy became ineffective, page redesigned, anti-scraping upgraded, better path discovered), append a line:
`{YYYY-MM-DD}: {what happened} → {conclusion}`

Normal execution does not write to the file. Do not record what keywords were used or how many results were returned — those are task outputs, not experience.
