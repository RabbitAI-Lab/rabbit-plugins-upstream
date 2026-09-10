---
name: tiktok-research
description: Research public TikTok profiles, videos, comments, hashtags, search results, trending feeds, and Creative Center signals through Crawlora. Use for TikTok-specific discovery or verification instead of scraping TikTok directly; use tiktok-ad-research for ad-only comparisons and influencer-discovery for cross-platform creator shortlists.
---

# TikTok research

Use Crawlora's normalized REST endpoints to answer TikTok-specific research
questions. Keep the result tied to the returned public data: a feed or search
sample is not a complete census, and a metric is not evidence of why a video or
ad performed well.

## Setup and requests

Set `CRAWLORA_API_KEY` to a key from [crawlora.net](https://crawlora.net), then
run the helper bundled with this skill. It sends `x-api-key` to
`https://api.crawlora.net/api/v1`; keep the key in the environment and never
put it in a URL, prompt output, or saved file.

```sh
Set `CRAWLORA_API_KEY` in the environment before running the helper.

scripts/crawlora.sh /tiktok/profile/chatgpt | jq '.'
scripts/crawlora.sh /tiktok/search keyword="ai agents" count=20 | jq '.'
scripts/crawlora.sh /tiktok/post/7444278905264983342 | jq '.'
```

Read [`reference/endpoints.md`](reference/endpoints.md) for the complete
endpoint list and current parameter names. Check both the HTTP result and the
JSON envelope: a successful HTTP response can still contain a nonzero
application `code`, a nested upstream error, or no usable results.

## Choose the workflow

### Profile, videos, and comments

1. Call `/tiktok/profile/{handler}` with the handle without `@`.
2. For the profile's videos, pass the returned `user.secUid` exactly to
   `/tiktok/posts`. Do not substitute the numeric user id or display name.
   `sort_type` is `0` latest, `1` popular, or `2` oldest.
3. Use `/tiktok/post/{id}` for one video's detail. Use `/tiktok/comments` with
   that video's `aweme_id` (the video id from its URL) for top-level comments.
4. Follow returned cursors only to the user's requested bound. Preserve the
   cursor type and stop when `has_more`/`hasMore` is false; do not assume every
   TikTok response uses the same casing.

### Search and discovery

- `/tiktok/search` finds videos by keyword.
- `/tiktok/search/hashtag` finds hashtag/challenge candidates.
- `/tiktok/search/user` finds users by keyword.
- `/tiktok/hashtag/{name}` resolves a hashtag and returns its id; pass that id
  to `/tiktok/hashtags` to retrieve its videos.
- `/tiktok/category` discovers Explore categories; pass a returned category
  `type` to `/tiktok/explore/{id}`.

Use identifiers returned by the preceding call. Search matches and hashtag
counts are evidence from TikTok's current index, not proof that every result is
about the requested brand or topic. Verify identity from the returned profile,
caption, source URL, or detail record before making a strong attribution.

### Trending and Creative Center

- `/tiktok/trending` returns a current recommended/trending feed.
- `/tiktok/creative-center/hashtags` returns ranked hashtags for a country and
  period.
- `/tiktok/creative-center/videos` returns ranked videos, optionally filtered
  by content label or `organic_only` and sorted by `views`, `engagement`, or
  `six_second_views`.
- `/tiktok/popular-trend/country-industry-meta` provides country and industry
  metadata when a Creative Center context needs to be explained.

Always report country, period, sort/filter choices, retrieval time, and sample
size. “Trending” is surface- and time-dependent; do not present it as a global
or historical ranking.

### Top Ads intelligence

For a matched ad study, first call `/tiktok/top-ads/filters` to discover current
dynamic country, industry, objective, language, and pattern-label ids. Keep
period, country, objective, and sort consistent across comparisons. Then:

1. Search `/tiktok/top-ads/list` with the agreed filters and a bounded `limit`.
   State `period` (`7`, `30`, or `180`) and `order_by` (`for_you`, `impression`,
   `ctr`, `play_2s_rate`, `play_6s_rate`, `cvr`, or `like`) in the output.
2. Deduplicate the returned materials and pass each returned `id` as
   `material_id` to `/tiktok/top-ads/detail`. This is a Top Ads material id,
   not the ad's TikTok video id; `id` and `materialId` are not accepted by the
   detail endpoint.
3. Use `/tiktok/top-ads/analysis` for interactive-time charts and percentiles.
   Match `metric` and `period_type` across ads. Supported metrics are
   `retain_ctr`, `retain_cvr`, `click_cnt`, `convert_cnt`, and
   `play_retain_cnt`.
4. Use `/tiktok/top-ads/recommend` or `/tiktok/top-ads/spotlight` only as
   supplemental discovery. Do not mix
   those handpicked/related materials into a matched filtered sample without
   labeling them.

For a dedicated competitor-ad comparison or creative brief, the narrower
`tiktok-ad-research` skill provides the same Top Ads endpoints with a more
focused deliverable.

## Interpretation and limits

- Public data only: no login, private content, hidden contacts, or audience
  demographics. A verification badge does not establish audience authenticity.
- Anonymous Creative Center access is limited. Hashtags return at most three
  records; videos return only page one (four videos), regardless of the
  apparent upstream totals. Treat those totals as upstream-reported context,
  not accessible coverage.
- Creative Center video availability varies by country. US, JP, ID, VN, and TH
  have reliably returned populated samples; a valid empty response in another
  market can mean that TikTok has no anonymous data for that market. Do not
  retry it indefinitely or call it an outage without other evidence.
- Creative Center `engagement_rate` and `six_seconds_vtr` are ratios, not
  percentages. Period-scoped and lifetime fields must not be compared as if
  they covered the same window.
- A Top Ads percentile is not a raw CTR/CVR, spend, conversion count, or ROI.
  Preserve the metric label, period, and units exactly as returned.
- Signed image/video URLs may expire. Retain stable TikTok source links and
  ids so the research can be repeated. Do not claim to have watched or heard a
  creative unless the environment actually exposed the media.
- Missing fields are unknown, not zero. A failed live refresh may support a
  clearly labeled stale/dataset observation, but must not silently become a
  current fact.

## Output and reliability

Return the requested answer with source URLs or stable ids, retrieval time,
filters, and sample size. For comparisons, keep the same definition and window
across rows. Separate observed facts from interpretation and label hypotheses
as hypotheses.

Use bounded requests. On `429`, back off; retry one transient `5xx` when useful.
Stop on `401`/`403` and report the access limitation. Preserve a clearly
labeled partial result when some details or comments fail, and inspect the
application-level `code` before treating an empty or nested response as valid
data.
