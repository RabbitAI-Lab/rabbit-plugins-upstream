---
name: x-research
description: Researches X (formerly Twitter) profiles and posts via the Crawlora API, returning clean JSON. Use when the user wants a public X profile's stats, a user's recent posts, or a single post's content/engagement — instead of scraping x.com or using the official (paid, rate-limited) X API.
---

# X (Twitter) research

Look up public X profiles, recent posts, and individual post content/engagement
— all as normalized JSON from the Crawlora API, no browser automation or
official X API access required.

## When to use this skill

- "What's <handle>'s profile / follower count on X?"
- "Pull <handle>'s recent posts on X."
- "What does this X post say, and what's its engagement?"
- Competitor or influencer social-listening on X without X API access.

## Setup (one-time)

- Get a free Crawlora API key (2,000 credits/mo, no card) at [https://crawlora.net](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills).
- `export CRAWLORA_API_KEY=sk_your_key_here`
- All requests: `x-api-key: $CRAWLORA_API_KEY` against
  `https://api.crawlora.net/api/v1`. Missing/invalid key → `401`.

## How it works

1. **Profile** — `GET /x/profile/{username}` returns public profile details
   for an X username, including visible counts and profile media when
   available.
2. **Profile posts** — `GET /x/profile/{username}/posts` returns posts from
   the first public profile page payload (defaults to 20, max 50 via
   `limit`). It does not paginate replies, media-only tabs, or search
   results.
3. **Post detail** — `GET /x/post/{id}` returns a single public post by
   numeric post id, including author, text, visible metrics, and a quoted
   post preview when present. Pass `username` to require the author match
   (mismatches return 404).

Full endpoint list, methods, and params: [`reference/endpoints.md`](reference/endpoints.md).

## Calling the API

```sh
# Profile:
scripts/crawlora.sh /x/profile/nasa | jq '.'

# Profile posts (capped at 50 per page):
scripts/crawlora.sh /x/profile/nasa/posts limit=30 | jq '.'

# Single post, with author check:
scripts/crawlora.sh /x/post/1234567890 username=nasa | jq '.'
```

Raw `curl` fallback:

```sh
curl -fsS -H "x-api-key: $CRAWLORA_API_KEY" \
  "https://api.crawlora.net/api/v1/x/profile/nasa/posts?limit=30" | jq '.'
```

## Endpoint reference

See [`reference/endpoints.md`](reference/endpoints.md) for all 3 X endpoints
this skill uses.

## Examples

- **Profile snapshot:** `/x/profile/<handle>` for follower/following counts
  and bio before deciding whether an account is worth tracking.
- **Recent activity check:** `/x/profile/<handle>/posts` to see posting
  cadence and topics without paging into replies or media tabs.
- **Single post lookup:** `/x/post/<id>` to pull a specific post's text and
  metrics, e.g. from a link shared elsewhere, optionally verifying the
  author with `username=`.

## Notes & limits

- **Credits / pay-on-success:** billed only on `2xx`; free tier 2,000 credits/mo.
  Key at [https://crawlora.net](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills).
- **Public data only** — public profiles/posts; no login, no private content.
  Respect X's terms.
- **Security:** key lives in `CRAWLORA_API_KEY` only — never hardcode, query-param, or commit it.
- **No search or trending on X** — this skill only covers profile, profile
  posts, and post detail; there is no `/x/search` or trending endpoint.
- **Profile posts is single-page, not cursor-paginated** — `/x/profile/{username}/posts`
  only returns what's in the first page payload (`limit` 1-50, default 20);
  it won't walk further back in a timeline.
- **Post lookup is by numeric id only** — `/x/post/{id}` needs the post's
  numeric id, not a tweet URL slug or username; pass `username` to guard
  against id collisions/mismatches.
