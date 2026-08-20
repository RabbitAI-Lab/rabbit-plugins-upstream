---
name: reddit-research
description: Researches Reddit via the Crawlora API — subreddit posts/comments/about, a single post plus its comment thread, keyword search, user post/comment history, domain-linked posts, and hot/new/rising/top trends — returning clean JSON. Use when the user wants community sentiment, a post's discussion, a user's Reddit history, or trending topics on a subreddit or across Reddit, instead of scraping Reddit or using an unofficial client.
---

# Reddit research

Look up subreddit posts and comments, a single post's full comment thread,
keyword search results, a public user's post/comment history, and
hot/new/rising/top trends — all as normalized JSON from the Crawlora API, no
Reddit scraping or unofficial client libraries.

## When to use this skill

- "What's <subreddit> talking about right now?"
- "Pull the comments on this Reddit post/thread."
- "Search Reddit for posts about <topic/product/brand>."
- "What has <username> posted or commented recently?"
- "What's trending on Reddit today?" or "What's the sentiment in r/<subreddit>?"
- Brand-mention monitoring, community research, or competitor sentiment tracking on Reddit.

## Setup (one-time)

- Get a free Crawlora API key (2,000 credits/mo, no card) at [https://crawlora.net](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills).
- `export CRAWLORA_API_KEY=sk_your_key_here`
- All requests: `x-api-key: $CRAWLORA_API_KEY` against
  `https://api.crawlora.net/api/v1`. Missing/invalid key → `401`.

## How it works

1. **Search** — `/reddit/search` for keyword-matched posts, optionally
   scoped to a `subreddit`.
2. **One post + its thread** — `/reddit/post/{id}` for the post itself,
   `/reddit/comments/{id}` for its public comments (add `include_metrics=true`
   on either for net score/upvote-ratio/award data at 3 credits instead of 1).
3. **Browse a subreddit** — `/reddit/subreddit/{subreddit}/posts` (hot/new/
   top/rising), `/reddit/subreddit/{subreddit}/comments` (latest flat
   comments feed), and `/reddit/subreddit/{subreddit}/about` for metadata +
   sample posts.
4. **Multi-subreddit feed** — `/reddit/subreddits/posts` with a
   comma-separated `subreddits` list (max 10) for a combined hot/new/top feed.
5. **User history** — `/reddit/user/{username}/posts` and
   `/reddit/user/{username}/comments` for a public user's submitted/comment
   feeds.
6. **Domain mentions** — `/reddit/domain/{domain}/posts` for public posts
   linking to a given hostname.
7. **Trends** — `/reddit/trends` for broad hot/new/rising/top feeds; for a
   single subreddit's trend, use `/reddit/subreddit/{subreddit}/posts` with
   `sort=hot|new|rising|top` instead.

Full endpoint list, methods, and params: [`reference/endpoints.md`](reference/endpoints.md).

## Calling the API

```sh
# Search + subreddit browse:
scripts/crawlora.sh /reddit/search q="web scraping" | jq '.'
scripts/crawlora.sh /reddit/subreddit/programming/posts sort=top time=week | jq '.'

# Post + comment thread:
scripts/crawlora.sh /reddit/post/1abcxyz include_metrics=true | jq '.'
scripts/crawlora.sh /reddit/comments/1abcxyz sort=top limit=50 | jq '.'

# User history + trends:
scripts/crawlora.sh /reddit/user/spez/posts | jq '.'
scripts/crawlora.sh /reddit/trends sort=rising | jq '.'
```

Raw `curl` fallback:

```sh
curl -fsS -H "x-api-key: $CRAWLORA_API_KEY" \
  "https://api.crawlora.net/api/v1/reddit/subreddit/programming/posts" | jq '.'
```

## Endpoint reference

See [`reference/endpoints.md`](reference/endpoints.md) for all 11 Reddit endpoints this skill uses.

## Examples

- **Community sentiment research:** `/reddit/subreddit/{subreddit}/posts` +
  `/reddit/subreddit/{subreddit}/comments` for a topic-relevant subreddit,
  scan post titles and comment text for recurring sentiment/pain points.
- **Thread deep-dive:** `/reddit/post/{id}` for the original post plus
  `/reddit/comments/{id}?include_metrics=true` for the full discussion with
  net score and award counts, to summarize a viral thread.
- **Brand-mention sweep:** `/reddit/search q="<brand>"` across all of Reddit
  or scoped with `subreddit=`, paginated via the returned `after` token, to
  count and read every public mention.

## Notes & limits

- **Credits / pay-on-success:** billed only on `2xx`; free tier 2,000 credits/mo.
  Key at [https://crawlora.net](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills).
- **Public data only** — public posts/comments/subreddits; no login, no private content.
  Respect Reddit's terms.
- **Security:** key lives in `CRAWLORA_API_KEY` only — never hardcode, query-param, or commit it.
- **Anonymous-page limits:** subscriber counts, icons, and banners are omitted
  from `/reddit/subreddit/{subreddit}/about` (not available on anonymous
  Reddit pages); exact upvote/downvote totals, upvote ratios, and share/repost/
  view counts are estimated or unavailable without `include_metrics=true`, and
  even then Reddit fuzzes voting data so figures are approximate.
- **Metrics cost more:** `include_metrics=true` on `/reddit/post/{id}` or
  `/reddit/comments/{id}` switches to the anonymous HTML page and costs 3
  credits instead of 1; large comment threads may only expose an initial
  subset in that mode.
- **Throttling:** most list endpoints return `503` with a `Retry-After` header
  when Reddit is temporarily throttling the request — wait that many seconds
  and retry rather than treating it as a hard failure.
- List endpoints are cursor-paginated via `after` — follow the returned
  cursor to walk beyond the first page (defaults to 25 results, clamps to 100).
