---
name: tiktok-research
description: Researches TikTok profiles, videos, hashtags, search, trending content, and Creative Center ads intelligence via the Crawlora API, returning clean JSON. Use when the user wants a TikTok creator's profile/videos, hashtag or keyword search, trending hashtags/videos, or competitor ad analysis from TikTok Top Ads — instead of scraping TikTok or the Creative Center directly.
---

# TikTok research

Look up public TikTok profiles, videos, and comments, run keyword/hashtag/user
search, track trending hashtags and videos, and pull TikTok Creative Center
Top Ads intelligence — all as normalized JSON from the Crawlora API, no app
scraping or unofficial client libraries.

## When to use this skill

- "What's <handle>'s TikTok profile / follower count / recent videos?"
- "Pull the comments on this TikTok video."
- "Search TikTok for videos/hashtags/users about <topic>."
- "What's trending on TikTok right now (hashtags or Creative Center videos)?"
- "Show me the top-performing TikTok ads for <brand/industry/keyword>."
- Competitor ad-creative research, hashtag-trend research, or influencer
  vetting on TikTok.

## Setup (one-time)

- Get a free Crawlora API key (2,000 credits/mo, no card) at [https://crawlora.net](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills).
- `export CRAWLORA_API_KEY=sk_your_key_here`
- All requests: `x-api-key: $CRAWLORA_API_KEY` against
  `https://api.crawlora.net/api/v1`. Missing/invalid key → `401`.

## How it works

Pick the job:

1. **Profile & content** — `/tiktok/profile/{handler}` for a public profile,
   `/tiktok/posts` for a profile's videos by `secUid`, `/tiktok/post/{id}` for
   one video's detail, `/tiktok/comments` for a video's top-level comments.
2. **Search & discovery** — `/tiktok/search` (videos by keyword),
   `/tiktok/search/hashtag` (hashtags by keyword), `/tiktok/search/user`
   (users by keyword), `/tiktok/hashtag/{name}` + `/tiktok/hashtags` (hashtag
   detail then its videos by id), `/tiktok/category` + `/tiktok/explore/{id}`
   (explore categories then a category's feed).
3. **Trending** — `/tiktok/trending` (current trending feed),
   `/tiktok/creative-center/hashtags` and `/tiktok/creative-center/videos`
   (Creative Center's ranked trending hashtags/videos by country and period —
   both are anonymous-access-limited, see Notes), `/tiktok/popular-trend/country-industry-meta`
   (metadata for the popular-trend endpoints).
4. **Ads intelligence (Creative Center Top Ads)** — `/tiktok/top-ads/list`
   (search/filter high-performing ads), `/tiktok/top-ads/detail` and
   `/tiktok/top-ads/analysis` (one ad's detail and interactive-time chart),
   `/tiktok/top-ads/recommend` and `/tiktok/top-ads/spotlight` (related /
   handpicked ads), `/tiktok/top-ads/filters`, `/tiktok/top-ads/locations`,
   `/tiktok/top-ads/location-info`, `/tiktok/top-ads/suggestions`, and
   `/tiktok/top-ads/safety` (filter/location/suggestion metadata to drive the
   above).

Full endpoint list, methods, and params: [`reference/endpoints.md`](reference/endpoints.md).

## Calling the API

```sh
# Profile + videos:
scripts/crawlora.sh /tiktok/profile/nasa | jq '.'
scripts/crawlora.sh /tiktok/post/7123456789012345678 | jq '.'

# Search:
scripts/crawlora.sh /tiktok/search keyword="ai agents" | jq '.'
scripts/crawlora.sh /tiktok/search/hashtag keyword="fitness" | jq '.'

# Trending + ads intelligence:
scripts/crawlora.sh /tiktok/trending | jq '.'
scripts/crawlora.sh /tiktok/top-ads/list keyword="skincare" country_code=US | jq '.'
```

Raw `curl` fallback:

```sh
curl -fsS -H "x-api-key: $CRAWLORA_API_KEY" \
  "https://api.crawlora.net/api/v1/tiktok/creative-center/hashtags?country_code=US&period=7" | jq '.'
```

## Endpoint reference

See [`reference/endpoints.md`](reference/endpoints.md) for all 25 TikTok endpoints this skill uses.

## Examples

- **Hashtag trend research:** `/tiktok/search/hashtag` for candidate
  hashtags, then `/tiktok/hashtag/{name}` + `/tiktok/hashtags` to pull the id
  and its top videos, cross-checked against
  `/tiktok/creative-center/hashtags` for the same country/period.
- **Competitor ad analysis:** `/tiktok/top-ads/list` filtered by
  `keyword`/`industry`/`country_code` to find a competitor's top-performing
  ads, then `/tiktok/top-ads/detail` and `/tiktok/top-ads/analysis` per
  `material_id` for creative detail and CTR/CVR percentile.
- **Creator vetting:** `/tiktok/profile/{handler}` + `/tiktok/posts` to check
  follower count and recent posting cadence, then `/tiktok/comments` on a
  recent video to sample engagement quality before a partnership.

## Notes & limits

- **Credits / pay-on-success:** billed only on `2xx`; free tier 2,000 credits/mo.
  Key at [https://crawlora.net](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills).
- **Public data only** — public profiles/videos; no login, no private content.
  Respect TikTok's terms.
- **Security:** key lives in `CRAWLORA_API_KEY` only — never hardcode, query-param, or commit it.
- **Creative Center anonymous limits:** `/tiktok/creative-center/hashtags`
  always returns at most 3 hashtags, and `/tiktok/creative-center/videos`
  always returns just page 1 (4 videos) regardless of `country_code`,
  `period`, or `sort_by` — TikTok gates the full result set behind a
  logged-in TikTok One account.
- **Creative Center video coverage is uneven by country:** US, JP, ID, VN,
  and TH reliably return populated `/tiktok/creative-center/videos` results;
  other countries have been observed to return an empty array (a genuine
  no-data response, not an error).
- **Top Ads `material_id` only:** `/tiktok/top-ads/detail` requires
  `material_id` — the upstream does not accept `id` or `materialId`.
- List/search endpoints (`posts`, `hashtags`, `search*`, `comments`) are
  cursor-paginated — follow the returned `cursor` to walk beyond the first page.
