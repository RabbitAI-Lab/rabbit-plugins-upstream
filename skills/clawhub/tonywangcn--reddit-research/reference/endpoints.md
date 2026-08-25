# reddit-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**12 endpoints across 1 platform group(s).**

## Reddit (12)

### `reddit_comments`

- **HTTP:** `GET /reddit/comments/{id}`
- **What:** Get Reddit post comments. Returns a Reddit post with its public comments. The default 1-credit mode uses RSS. Set `include_metrics=true` to use the anonymous HTML post page as the sole content request and return the server-rendered comments with public net score and award count plus post engagement metrics for 3 credits. Large threads may expose only an initial comment subset in anonymous HTML. Reddit does not expose per-comment upvote ratios or exact upvote/downvote totals anonymously. A post that exists but has no comments yet returns a 200 response with an empty comments list; a post that does not exist returns 404, and a temporary block or upstream failure returns 503 (retryable) rather than 404.
- **Params:** `depth` (integer, optional) — Maximum flat comment depth returned in metrics mode.; `id` (string, **required**) — Reddit post id or t3_ id; `include_metrics` (boolean, optional) — Include public post and per-comment engagement metrics; costs 3 credits instead of 1; `limit` (integer, optional) — Maximum comments returned, defaults to 25 and clamps to 100; `sort` (string, optional) — Comment order: confidence, top, new, controversial, old, or qa. Applied to the anonymous HTML request when metrics are enabled.

### `reddit_domain_posts`

- **HTTP:** `GET /reddit/domain/{domain}/posts`
- **What:** List Reddit domain posts. Returns normalized public posts submitted from a linked domain. A `503` with a `Retry-After` header means Reddit is temporarily throttling the request; wait that many seconds and retry.
- **Params:** `after` (string, optional) — Reddit pagination token; `domain` (string, **required**) — Domain hostname, without scheme or path; `limit` (integer, optional) — Maximum posts, defaults to 25 and clamps to 100; `sort` (string, optional) — Sort: hot, new, top, or rising; `time` (string, optional) — Time window for top sort: hour, day, week, month, year, or all

### `reddit_leads`

- **HTTP:** `GET /reddit/leads`
- **What:** Find Reddit buying-intent leads. Scans a Reddit search page for people actively asking for a product or service, scores each post 0-10 for buying intent, and returns them ranked highest-first with the signals that fired. Self-promotion, hiring posts, freelancer service adverts, revenue-milestone posts, duplicate reposts, and Title Case article headlines are filtered out before scoring. A deterministic prefilter always runs; when `classifier` resolves to `llm` the surviving candidates are additionally refined in one batched model call. A `503` with a `Retry-After` header means Reddit is temporarily throttling the request; wait that many seconds and retry.
- **Params:** `classifier` (string, optional) — Classifier: auto uses the model when configured, heuristic skips it, llm requires it; `limit` (integer, optional) — Maximum leads returned, defaults to 25 and clamps to 100; `min_score` (integer, optional) — Minimum buying-intent score to return, 0-10, defaults to 4; `q` (string, **required**) — What you offer, in plain language; `sort` (string, optional) — Sort: relevance, hot, new, top, or comments; `subreddit` (string, optional) — Restrict the search to a subreddit name, without r/; `time` (string, optional) — Time window: hour, day, week, month, year, or all

### `reddit_post`

- **HTTP:** `GET /reddit/post/{id}`
- **What:** Get Reddit post. Returns a normalized public Reddit post. The default 1-credit mode uses RSS. Set `include_metrics=true` to use the anonymous HTML post page as the sole content request and return public net score, upvote ratio, comment count, award count, and estimated upvote/downvote totals for 3 credits. Reddit fuzzes voting data, so estimates are approximate; share, repost/crosspost, and view counts are not exposed anonymously.
- **Params:** `id` (string, **required**) — Reddit post id or t3_ id; `include_metrics` (boolean, optional) — Include public engagement metrics; costs 3 credits instead of 1

### `reddit_search`

- **HTTP:** `GET /reddit/search`
- **What:** Search Reddit posts. Searches public Reddit content and returns normalized public post entries. A `503` with a `Retry-After` header means Reddit is temporarily throttling the request; wait that many seconds and retry.
- **Params:** `after` (string, optional) — Reddit pagination token; `limit` (integer, optional) — Maximum posts, defaults to 25 and clamps to 100; `q` (string, **required**) — Search keywords; `sort` (string, optional) — Sort: relevance, hot, new, top, or comments; `subreddit` (string, optional) — Restrict search to a subreddit name, without r/; `time` (string, optional) — Time window for top/comments sorts: hour, day, week, month, year, or all

### `reddit_subreddit_about`

- **HTTP:** `GET /reddit/subreddit/{subreddit}/about`
- **What:** Get Reddit subreddit metadata. Returns public metadata and sample posts for a subreddit. Subscriber counts, icons, and banners are omitted because they are not available on anonymous Reddit pages. A `503` with a `Retry-After` header means Reddit is temporarily throttling the request; wait that many seconds and retry.
- **Params:** `limit` (integer, optional) — Maximum sample posts inspected, defaults to 25 and clamps to 100; `subreddit` (string, **required**) — Subreddit name, without r/

### `reddit_subreddit_comments`

- **HTTP:** `GET /reddit/subreddit/{subreddit}/comments`
- **What:** List Reddit subreddit comments. Returns flat public comment entries from a subreddit latest-comments feed. A `503` with a `Retry-After` header means Reddit is temporarily throttling the request; wait that many seconds and retry.
- **Params:** `after` (string, optional) — Reddit pagination token; `limit` (integer, optional) — Maximum comments, defaults to 25 and clamps to 100; `subreddit` (string, **required**) — Subreddit name, without r/

### `reddit_subreddit_posts`

- **HTTP:** `GET /reddit/subreddit/{subreddit}/posts`
- **What:** List Reddit subreddit posts. Returns normalized public posts from a subreddit. A `503` with a `Retry-After` header means Reddit is temporarily throttling the request; wait that many seconds and retry.
- **Params:** `after` (string, optional) — Reddit pagination token; `limit` (integer, optional) — Maximum posts, defaults to 25 and clamps to 100; `sort` (string, optional) — Sort: hot, new, top, or rising; `subreddit` (string, **required**) — Subreddit name, without r/; `time` (string, optional) — Time window for top sort: hour, day, week, month, year, or all

### `reddit_subreddits_posts`

- **HTTP:** `GET /reddit/subreddits/posts`
- **What:** List Reddit multi-subreddit posts. Returns normalized public posts from a combined multi-subreddit feed. A `503` with a `Retry-After` header means Reddit is temporarily throttling the request; wait that many seconds and retry.
- **Params:** `after` (string, optional) — Reddit pagination token; `limit` (integer, optional) — Maximum posts, defaults to 25 and clamps to 100; `sort` (string, optional) — Sort: hot, new, top, or rising; `subreddits` (string, **required**) — Comma-separated subreddit names, without r/, maximum 10; `time` (string, optional) — Time window for top sort: hour, day, week, month, year, or all

### `reddit_trends`

- **HTTP:** `GET /reddit/trends`
- **What:** List Reddit trends. Returns normalized public posts from broad Reddit hot, new, rising, or top feeds. For subreddit-specific trends, use `/reddit/subreddit/{subreddit}/posts` with `sort=hot`, `sort=new`, `sort=rising`, or `sort=top`. A `503` with a `Retry-After` header means Reddit is temporarily throttling the request; wait that many seconds and retry.
- **Params:** `after` (string, optional) — Reddit pagination token; `limit` (integer, optional) — Maximum posts, defaults to 25 and clamps to 100; `sort` (string, optional) — Sort: hot, new, rising, or top; `time` (string, optional) — Time window for top sort: hour, day, week, month, year, or all

### `reddit_user_comments`

- **HTTP:** `GET /reddit/user/{username}/comments`
- **What:** List Reddit user comments. Returns flat public comment entries from a public Reddit user's comments feed. A `503` with a `Retry-After` header means Reddit is temporarily throttling the request; wait that many seconds and retry.
- **Params:** `after` (string, optional) — Reddit pagination token; `limit` (integer, optional) — Maximum comments, defaults to 25 and clamps to 100; `username` (string, **required**) — Public Reddit username, without u/

### `reddit_user_posts`

- **HTTP:** `GET /reddit/user/{username}/posts`
- **What:** List Reddit user posts. Returns normalized public posts from a public Reddit user's submitted feed. A `503` with a `Retry-After` header means Reddit is temporarily throttling the request; wait that many seconds and retry.
- **Params:** `after` (string, optional) — Reddit pagination token; `limit` (integer, optional) — Maximum posts, defaults to 25 and clamps to 100; `username` (string, **required**) — Public Reddit username, without u/
