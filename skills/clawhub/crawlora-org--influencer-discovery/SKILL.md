---
name: influencer-discovery
description: Find and shortlist TikTok, Instagram, and YouTube creators for a campaign using Crawlora's creator datasets and live profile/content endpoints. Use for creator sourcing, comparing campaign fit, and producing an evidence-backed influencer shortlist.
---

# Influencer discovery

Translate a campaign brief into a creator shortlist, then refresh the candidates
that merit a closer look. Distinguish creator location and content signals from
audience demographics, which these endpoints do not establish.

## Setup and requests

Set `CRAWLORA_API_KEY` to your key from [crawlora.net](https://crawlora.net).
Run the bundled `scripts/crawlora.sh` from this skill directory or by absolute
path. It sends `x-api-key` to `https://api.crawlora.net/api/v1`; keep the key in
the environment. Read [reference/endpoints.md](reference/endpoints.md) for
platform-specific filters and ID shapes.

## Discover and qualify

1. Extract the platforms, topic, geography, follower range, requested count,
   and campaign constraints. Ask only for missing information that changes selection.
2. Discover a small candidate pool using the datasets below. Bio keyword matches
   are candidate evidence, not proof of sustained content focus. Use returned
   facets where supported for exact categories and regions.

   | Platform | Dataset search | Non-obvious differences |
   |---|---|---|
   | TikTok | `/datasets/creators/search` | `country`, `niche`, `min_followers`; no `max_followers` filter, so enforce the upper bound locally |
   | Instagram | `/datasets/instagram-users/search` | `min_followers`, `max_followers`, `category_name`, `crawled_after`; no country filter |
   | YouTube | `/datasets/youtube-creators/search` | `region`, `min_followers`, `max_followers`, `hydrated_after`; followers mean subscribers |

   Use `page_size` up to 100; `page * page_size` must not exceed 10,000.
   Dataset results are periodically refreshed, not live. If the candidate pool
   is too small, relax a stated criterion or use supported live search; disclose it.
3. Refresh shortlisted creators with `/tiktok/profile/{handler}`,
   `/instagram/profile/{username}`, or `/youtube/profile/{id}`. Preserve the
   platform ID and original dataset timestamps. TikTok dataset `unique_id` is
   the handle for the profile route; `creator_uid` is a dataset identity, not
   a handle. For recent-content sampling,
   TikTok posts require the profile's `secUid`; Instagram Reels require a numeric
   user ID; YouTube channel videos accept the channel ID and return continuation
   tokens. Do not substitute display names for these identifiers.
4. Inspect a bounded, consistent content sample per candidate when content fit
   or engagement matters. Record sample size and dates. Separate organic content
   from observed sponsorship disclosures; do not invent partnership histories.
5. Rank by the user's criteria with brief supporting evidence. Deduplicate within
   each platform by stable ID. Link identities across platforms only when public
   profile links or other direct evidence establish the relationship.

```sh
scripts/crawlora.sh /datasets/creators/search \
  q=fitness min_followers=50000 page_size=10
scripts/crawlora.sh /datasets/instagram-users/search \
  q=fitness min_followers=50000 max_followers=500000 page_size=10
scripts/crawlora.sh /datasets/youtube-creators/search \
  q=fitness min_followers=50000 max_followers=500000 page_size=10
```

## Metrics and output

- TikTok `engagement_rate`, `avg_views`, and `post_stats` cover only an enriched
  subset. `engagement_desc` sorts missing metrics last; it is not a complete
  population ranking. Keep absent metrics unknown, never zero.
- YouTube count fields can be zero when their `*_available` flag is false.
  Respect those flags before filtering or comparing creators.
- If calculating an engagement rate, name the formula, denominator, sample size,
  and dates. Do not compare unlike platform definitions in a single engagement
  ranking. Neither high engagement nor a verification badge proves audience authenticity.
- Public contacts can be unavailable. TikTok email output requires
  `include_email=true` and an entitled non-Free key; `has_email=true` alone
  does not reveal an address. Do not guess hidden contact information.

Return the requested shortlist/table/CSV with platform, handle/channel ID,
profile URL, topic-fit evidence, follower count, refresh time/status, sampled
content URLs, metric definitions, and fit rationale. Mark unverified geography
or audience assumptions explicitly. Sending messages requires a separate user request.

Use a bounded number of discovery pages and profile refreshes. On `429`, back
off; retry a transient `5xx` once. Stop on `401`/`403` and inspect application
`code` before using `data`. A failed live refresh may leave a clearly labeled
dataset-only candidate; it must not silently become a current observation.
