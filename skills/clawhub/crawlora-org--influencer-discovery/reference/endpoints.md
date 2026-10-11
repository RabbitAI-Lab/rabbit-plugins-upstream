# influencer-discovery — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Only the endpoints used by this workflow. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**28 endpoints across 5 platform group(s).**

## Datasets (7)

### `datasets_creators_search`

- **HTTP:** `GET /datasets/creators/search`
- **What:** Search the TikTok creators dataset. Searches TikTok creators stored in a search index (one document per creator), with follower counts, verified status, niche, and engagement. Deleted and private accounts are excluded by default; set `include_inactive=true` to include them for historical lookups. Sort enum: `followers_desc`, `engagement_desc`, `engagement_qualified_desc`, `likes_desc`, `relevance`. Coverage note: `followers_desc`, `likes_desc`, and `relevance` are backed by profile fields present across the full dataset; the post-level engagement metrics (`engagement_rate`, `avg_views`, and the nested `post_stats` object) and the `engagement_desc`/`engagement_qualified_desc` sorts are currently populated for a growing subset of creators, prioritizing the highest-reach accounts. Creators without these metrics are still returned but sort last under `engagement_desc` and omit those fields; `engagement_qualified_desc` excludes them outright (they cannot clear its floors). `engagement_desc` ranks by raw `engagement_rate` with no eligibility floor — it surfaces a real stale-record + ratio-by-design trap: an account whose last real post was years ago can still carry an unrealistic rate computed from a handful of old posts. `engagement_qualified_desc` is the same metric restricted to creators with a recent post (`last_post_at` within 90 days), a minimum reach (`avg_views >= 10000`) and sample size (`post_stats.sampled_posts >= 10`), and a sanity ceiling (`engagement_rate <= 50%`) — use this, not the raw sort, for a "best engagement" leaderboard. Sound fields: `post_stats.top_sounds` holds only a creator's FIVE most-used sounds from the sampled posts, ranked by use count with ties broken by lowest `music_id`, so it is a top-5 view and not the creator's full sound list; `post_stats.distinct_sounds` gives the true number of different sounds the sample used. Use each sound's `original` boolean to tell TikTok-generated original audio from catalogue tracks - do NOT infer it from the title, because TikTok localizes the original-audio label (`sonido original`, `som original`, `оригинальный звук`, and at least fifteen more), so a title match silently reclassifies original audio as named tracks.
- **Params:** `country` (string, optional) — Exact creator country/region filter, max 128 characters; `handle` (string, optional) — Exact handle lookup (case-insensitive), e.g. khaby.lame; returns the single creator with that exact @handle; `has_email` (boolean, optional) — Filter by contact-email presence; true keeps only creators with an email; `include_email` (boolean, optional) — Return the stored contact email instead of a blanked value. Off by default for everyone, and honoured only for entitled (non-Free) API keys; `include_inactive` (boolean, optional) — Include deleted/private accounts; defaults to false (only live accounts returned); `min_followers` (integer, optional) — Minimum follower count; `niche` (string, optional) — Exact content-niche filter, max 128 characters; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `q` (string, optional) — Full-text query over handle, nickname and bio, max 256 characters; `sort` (string, optional) — Sort enum: followers_desc, engagement_desc, engagement_qualified_desc, likes_desc, relevance. engagement_desc ranks by raw post-level engagement rate, currently populated for a subset of creators (highest-reach first); creators without it sort last. engagement_qualified_desc is the same metric restricted to creators with a recent post (<=90d), a minimum reach (avg_views>=10000) and sample size (>=10 posts), and a sanity ceiling (<=50%) -- use this, not the raw sort, for a 'best engagement' leaderboard; `verified` (boolean, optional) — Filter by verified badge; true keeps only verified creators

### `datasets_instagram_users_facets`

- **HTTP:** `GET /datasets/instagram-users/facets`
- **What:** Facet the Instagram users dataset. Returns terms aggregation counts for the Instagram users dataset. Facet enum: `is_verified`, `is_business_account`, `has_bio`, `has_external_url`, `category_name`, `source_tier`.
- **Params:** `category_name` (string, optional) — Exact category filter (case-insensitive, e.g. Digital Creator), max 128 characters; `crawled_after` (string, optional) — Records last refreshed on or after this date (RFC3339 or YYYY-MM-DD); `crawled_before` (string, optional) — Records last refreshed on or before this date (RFC3339 or YYYY-MM-DD); `created_after` (string, optional) — Accounts created on or after this date (RFC3339 or YYYY-MM-DD); `created_before` (string, optional) — Accounts created on or before this date (RFC3339 or YYYY-MM-DD); `facet` (string, **required**) — Facet enum: is_verified, is_business_account, has_bio, has_external_url, category_name, source_tier; `has_bio` (boolean, optional) — Filter by a non-empty profile biography; `has_external_url` (boolean, optional) — Filter by a linked external URL; `is_business_account` (boolean, optional) — Filter by business or creator accounts; `is_verified` (boolean, optional) — Filter by the Instagram verification checkmark; `max_followers` (integer, optional) — Maximum follower count; `max_ratio` (number, optional) — Maximum follower-to-following ratio; `min_followers` (integer, optional) — Minimum follower count; `min_ratio` (number, optional) — Minimum follower-to-following ratio; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `q` (string, optional) — Full-text query over username, full_name and biography, max 256 characters; `sort` (string, optional) — Sort enum: relevance, followers_desc, followers_asc, crawled_at_desc, crawled_at_asc, created_at_desc, created_at_asc; `source_tier` (string, optional) — Exact filter for seed tier (e.g. crossref, vertical-hashtags, mention-graph, head-directory); `username` (string, optional) — Exact username filter (case-insensitive), max 128 characters

### `datasets_instagram_users_item`

- **HTTP:** `GET /datasets/instagram-users/items/{username}`
- **What:** Get an Instagram user from the dataset. Returns one Instagram user record by username from dataset id enum value `instagram-users`.
- **Params:** `username` (string, **required**) — Instagram username, with or without a leading @, max 128 characters

### `datasets_instagram_users_search`

- **HTTP:** `GET /datasets/instagram-users/search`
- **What:** Search the Instagram users dataset. Searches public Instagram user profiles stored in a search index. Sort enum: `relevance`, `followers_desc`, `followers_asc`, `crawled_at_desc`, `crawled_at_asc`, `created_at_desc`, `created_at_asc`.
- **Params:** `category_name` (string, optional) — Exact category filter (case-insensitive, e.g. Digital Creator), max 128 characters; `crawled_after` (string, optional) — Records last refreshed on or after this date (RFC3339 or YYYY-MM-DD); `crawled_before` (string, optional) — Records last refreshed on or before this date (RFC3339 or YYYY-MM-DD); `created_after` (string, optional) — Accounts created on or after this date (RFC3339 or YYYY-MM-DD); `created_before` (string, optional) — Accounts created on or before this date (RFC3339 or YYYY-MM-DD); `has_bio` (boolean, optional) — Filter by a non-empty profile biography; `has_external_url` (boolean, optional) — Filter by a linked external URL; `is_business_account` (boolean, optional) — Filter by business or creator accounts; `is_verified` (boolean, optional) — Filter by the Instagram verification checkmark; `max_followers` (integer, optional) — Maximum follower count; `max_ratio` (number, optional) — Maximum follower-to-following ratio; `min_followers` (integer, optional) — Minimum follower count; `min_ratio` (number, optional) — Minimum follower-to-following ratio; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `q` (string, optional) — Full-text query over username, full_name and biography, max 256 characters; `sort` (string, optional) — Sort enum: relevance, followers_desc, followers_asc, crawled_at_desc, crawled_at_asc, created_at_desc, created_at_asc; `source_tier` (string, optional) — Exact filter for seed tier (e.g. crossref, vertical-hashtags, mention-graph, head-directory), max 128 characters; `username` (string, optional) — Exact username filter (case-insensitive), max 128 characters

### `datasets_youtube_creators_facets`

- **HTTP:** `GET /datasets/youtube-creators/facets`
- **What:** Facet the YouTube creators dataset. Returns terms aggregation counts for the YouTube creators dataset. Facet enum: `region`, `discovery_source`.
- **Params:** `channel_id` (string, optional) — Exact channel id filter, max 128 characters; `discovery_source` (string, optional) — Exact filter for how the channel was discovered, max 128 characters; `facet` (string, **required**) — Facet enum: region, discovery_source; `followers_count_available` (boolean, optional) — Filter by whether the channel exposes a public subscriber count; `has_bio` (boolean, optional) — Filter by a non-empty About bio; `has_links` (boolean, optional) — Filter by at least one linked external URL; `hydrated_after` (string, optional) — Records last refreshed on or after this date (RFC3339 or YYYY-MM-DD); `hydrated_before` (string, optional) — Records last refreshed on or before this date (RFC3339 or YYYY-MM-DD); `joined_after` (string, optional) — Channels created on or after this date (RFC3339 or YYYY-MM-DD); `joined_before` (string, optional) — Channels created on or before this date (RFC3339 or YYYY-MM-DD); `max_followers` (integer, optional) — Maximum subscriber count; `max_videos` (integer, optional) — Maximum uploaded-video count; `max_views` (integer, optional) — Maximum total view count; `min_followers` (integer, optional) — Minimum subscriber count; `min_videos` (integer, optional) — Minimum uploaded-video count; `min_views` (integer, optional) — Minimum total view count; `q` (string, optional) — Full-text query over channel_name and bio, max 256 characters; `region` (string, optional) — Exact channel region/country filter (case-insensitive), max 128 characters; `sort` (string, optional) — Sort enum: relevance, followers_desc, followers_asc, views_desc, videos_desc, hydrated_at_desc, hydrated_at_asc; `videos_count_available` (boolean, optional) — Filter by whether the channel has a known uploaded-video count; `views_count_available` (boolean, optional) — Filter by whether the channel has a known total view count

### `datasets_youtube_creators_item`

- **HTTP:** `GET /datasets/youtube-creators/items/{channel_id}`
- **What:** Get a YouTube creator from the dataset. Returns one YouTube channel record by channel id from dataset id enum value `youtube-creators`.
- **Params:** `channel_id` (string, **required**) — YouTube channel id, e.g. UCxxxxxxxxxxxxxxxxxxxxxxxx

### `datasets_youtube_creators_search`

- **HTTP:** `GET /datasets/youtube-creators/search`
- **What:** Search the YouTube creators dataset. Searches public YouTube channel profiles stored in a search index — subscriber, video and view counts, region, bio and links, discovered via Common Crawl and Wikidata and hydrated from each channel's public About page. Sort enum: `relevance`, `followers_desc`, `followers_asc`, `views_desc`, `videos_desc`, `hydrated_at_desc`, `hydrated_at_asc`. Some channels hide their subscriber, video, or view count; the `_available` flags on each item distinguish a hidden count (stored as `0`, `*_available: false`) from a genuine `0`.
- **Params:** `channel_id` (string, optional) — Exact channel id filter (e.g. UCxxxxxxxxxxxxxxxxxxxxxxxx), max 128 characters; `discovery_source` (string, optional) — Exact filter for how the channel was discovered (e.g. commoncrawl, wikidata), max 128 characters; `followers_count_available` (boolean, optional) — Filter by whether the channel exposes a public subscriber count; `has_bio` (boolean, optional) — Filter by a non-empty About bio; `has_links` (boolean, optional) — Filter by at least one linked external URL; `hydrated_after` (string, optional) — Records last refreshed on or after this date (RFC3339 or YYYY-MM-DD); `hydrated_before` (string, optional) — Records last refreshed on or before this date (RFC3339 or YYYY-MM-DD); `joined_after` (string, optional) — Channels created on or after this date (RFC3339 or YYYY-MM-DD); `joined_before` (string, optional) — Channels created on or before this date (RFC3339 or YYYY-MM-DD); `max_followers` (integer, optional) — Maximum subscriber count; `max_videos` (integer, optional) — Maximum uploaded-video count; `max_views` (integer, optional) — Maximum total view count; `min_followers` (integer, optional) — Minimum subscriber count; `min_videos` (integer, optional) — Minimum uploaded-video count; `min_views` (integer, optional) — Minimum total view count; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `q` (string, optional) — Full-text query over channel_name and bio, max 256 characters; `region` (string, optional) — Exact channel region/country filter (case-insensitive), max 128 characters; `sort` (string, optional) — Sort enum: relevance, followers_desc, followers_asc, views_desc, videos_desc, hydrated_at_desc, hydrated_at_asc; `videos_count_available` (boolean, optional) — Filter by whether the channel has a known uploaded-video count; `views_count_available` (boolean, optional) — Filter by whether the channel has a known total view count

## TikTok (4)

### `tiktok_post`

- **HTTP:** `GET /tiktok/post/{id}`
- **What:** Retrieve TikTok video details. Returns the TikTok video detail payload for a video id.
- **Params:** `id` (string, **required**) — TikTok video id

### `tiktok_posts`

- **HTTP:** `GET /tiktok/posts`
- **What:** Retrieve posts from a TikTok profile. Returns posts from a TikTok profile by `secUid`, with optional cursor pagination and sort mode.
- **Params:** `cursor` (integer, optional) — Pagination cursor; `secUid` (string, **required**) — TikTok secUid for the profile; `sort_type` (integer, optional) — Sort mode: 0 latest, 1 popular, 2 oldest

### `tiktok_profile`

- **HTTP:** `GET /tiktok/profile/{handler}`
- **What:** Retrieve a TikTok profile. Returns the TikTok profile payload for a public handle.
- **Params:** `handler` (string, **required**) — TikTok handle without the leading @

### `tiktok_search_user`

- **HTTP:** `GET /tiktok/search/user`
- **What:** Search TikTok users. Searches TikTok users by keyword with cursor-based pagination.
- **Params:** `cursor` (integer, optional) — Pagination cursor; `keyword` (string, **required**) — Search keyword

## Instagram (3)

### `instagram_post`

- **HTTP:** `GET /instagram/post/{id}/{post_id}`
- **What:** Retrieve a specific Instagram post by URL shortcode. Returns media details for an Instagram URL shortcode. Use media.code from the reels response or shortcode from a public post URL; numeric media IDs are rejected.
- **Params:** `id` (string, **required**) — Instagram user ID retained for route compatibility; ownership is not verified; `post_id` (string, **required**) — Instagram URL shortcode (media.code), not a numeric media ID

### `instagram_profile`

- **HTTP:** `GET /instagram/profile/{username}`
- **What:** Retrieve an Instagram user profile by username. Returns public profile details for a specified Instagram username.
- **Params:** `username` (string, **required**) — Instagram username

### `instagram_reels`

- **HTTP:** `GET /instagram/reels/{id}`
- **What:** Retrieve Instagram Reels for a user. Returns up to 12 public Reels via anonymous proxied HTTP for the numeric Instagram user ID. Supports opaque `max_id` pagination. Captions, timestamps and original image dimensions are omitted when the public source does not expose them.
- **Params:** `id` (string, **required**) — Numeric Instagram user ID (not a username); `max_id` (string, optional) — Pagination cursor for fetching the next page of Reels

## YouTube (4)

### `youtube_channel_videos`

- **HTTP:** `GET /youtube/channel/{id}/videos`
- **What:** Retrieve the videos tab for a YouTube channel. Returns normalized video items from a channel's Videos tab and an optional continuation token.
- **Params:** `continuation_token` (string, optional) — Pagination token returned by a previous request; `id` (string, **required**) — Channel ID, @handle, /c path, /user path, or full YouTube channel URL

### `youtube_profile`

- **HTTP:** `GET /youtube/profile/{id}`
- **What:** Retrieve channel profile. Returns full profile details for a YouTube channel.
- **Params:** `id` (string, **required**) — Channel ID, @handle, /c path, /user path, bare username, or full YouTube channel URL

### `youtube_search`

- **HTTP:** `GET /youtube/search`
- **What:** Search YouTube. Returns normalized YouTube search results using YouTube's InnerTube search API. Pass `continuation_token` from a previous response to retrieve the next page. Use `q` as the primary query parameter; `search_query` is accepted as an alias. `hl` and `gl` localize ranking and result context; they default to `en` and `US`. Named filters cover the public web search filters. Account-only chips such as Watched and Unwatched are not exposed.
- **Params:** `continuation_token` (string, optional) — Pagination token returned by a previous request; `duration` (string, optional) — Filter by duration; short, medium, and long preserve their previous upstream encodings; `features` (string, optional) — Comma-separated feature filters. Allowed values: live, 4k, hd, subtitles, cc, creative_commons, 360, vr180, 3d, hdr, location, purchased; `gl` (string, optional) — Two-letter YouTube region code; `hl` (string, optional) — YouTube interface language; `params` (string, optional) — Raw protobuf-encoded search filter (base64); `q` (string, optional) — Search query; `search_query` (string, optional) — Alias for q; `sort_by` (string, optional) — Sort results; `type` (string, optional) — Filter by type; `upload_date` (string, optional) — Filter by upload date

### `youtube_video`

- **HTTP:** `GET /youtube/video/{id}`
- **What:** Retrieve video metadata & captions. Returns title, description, stats, and captions for a YouTube video ID.
- **Params:** `id` (string, **required**) — YouTube video ID (11-char code)

## Substack (10)

### `substack_categories`

- **HTTP:** `GET /substack/categories`
- **What:** List Substack categories. Returns every public Substack category, with the category id required by /substack/category. Ids span two spaces: 32 categories use a numeric id and one uses the string id `podcast`. Both are accepted by /substack/category.
- **Params:** _none_

### `substack_leaderboard`

- **HTTP:** `GET /substack/leaderboard`
- **What:** List a Substack category's bestseller leaderboard. Returns one page of a category's bestseller leaderboard, pairing each ranked publication with its author. This is a different surface from /substack/category: it exposes the trending ranking (the site's "Rising" tab), validates its ranking values rather than silently defaulting, accepts the extra cross-category id `bestseller`, and returns the author alongside the publication. Use a category_id from /substack/categories whose in_leaderboard is true. Upstream serves 25 rows per page and accepts pages 0-25.
- **Params:** `category_id` (string, **required**) — Category id from /substack/categories with in_leaderboard true. Numeric, or the string ids podcast or bestseller.; `page` (integer, optional) — Zero-based page, 0-25; `type` (string, optional) — Ranking to read

### `substack_post`

- **HTTP:** `GET /substack/post`
- **What:** Get one public Substack post. Returns one public post with the extended metadata the archive listing omits, including word count, every credited byline, and podcast audio details where the post has them. Post bodies are not returned.
- **Params:** `publication` (string, **required**) — Publication subdomain or custom domain; `slug` (string, **required**) — Post slug, the trailing path segment of the post URL

### `substack_publication`

- **HTTP:** `GET /substack/publication`
- **What:** Get a Substack publication and its subscription offering. Returns a publication's public profile and its complete subscription offering: every purchasable web plan with per-currency pricing, the separately priced App Store plans, per-tier benefit copy, and the toggles governing which tiers are sold. Identify the publication by name (a subdomain such as semianalysis, or a custom domain such as www.thefp.com) or by numeric publication_id -- exactly one is required. Prefer publication_id when you have it: it reads a compact document, while resolving by name has to parse the publication's full homepage.
- **Params:** `publication` (string, optional) — Publication subdomain or custom domain. Provide this or publication_id.; `publication_id` (integer, optional) — Numeric publication id. Cheaper than resolving by name. Provide this or publication.

### `substack_publication_posts`

- **HTTP:** `GET /substack/publication/posts`
- **What:** List a Substack publication's public post archive. Returns one page of a publication's public post archive with title, subtitle, canonical URL, publish date, engagement counts, and whether each post is paywalled. search filters the publication's own posts full-text; a query with no matches returns an empty list rather than the unfiltered archive.
- **Params:** `limit` (integer, optional) — Rows per page, 1-50; `offset` (integer, optional) — Zero-based row offset; `publication` (string, **required**) — Publication subdomain or custom domain; `search` (string, optional) — Full-text filter over the publication's own posts; `sort` (string, optional) — Archive ordering

### `substack_publication_recommendations`

- **HTTP:** `GET /substack/publication/recommendations`
- **What:** List the publications one Substack publication recommends. Returns the publications a given publication recommends to its own readers, as a publication-to-publication graph. Useful for discovering publications beyond the 675-per-category ceiling on /substack/category. publication_id is the numeric id returned by /substack/publication, /substack/category, or /substack/user.
- **Params:** `publication_id` (integer, **required**) — Numeric publication id

### `substack_search`

- **HTTP:** `GET /substack/search`
- **What:** Search posts and publications across Substack. Searches posts across all of Substack and returns the publications that also matched, unlike /substack/publication/posts which searches within a single publication. Set focus_publication_id to additionally receive that one publication's own matching posts in focused_posts alongside the site-wide results.
- **Params:** `focus_limit` (integer, optional) — Cap on focused_posts, 1-20. Requires focus_publication_id.; `focus_publication_id` (integer, optional) — Numeric publication id whose own matching posts are returned in focused_posts; `page` (integer, optional) — Zero-based page, 20 posts per page; `query` (string, **required**) — Search text

### `substack_user`

- **HTTP:** `GET /substack/user`
- **What:** Get a public Substack writer profile. Returns one public Substack profile: identity, the publications the writer contributes to, their publicly visible subscriptions, and every subscriber signal Substack publishes. total is opt-in per writer and rounded to roughly three significant figures; when a writer hides it, total_hidden is true and total is 0, which must not be read as zero subscribers. paid_rough, paid_rough_int, and paid_tier are buckets - no exact paid subscriber count is published anywhere. follower_count is exact but counts followers, not subscribers.
- **Params:** `handle` (string, **required**) — Substack profile handle

### `substack_user_activity`

- **HTTP:** `GET /substack/user/activity`
- **What:** List a Substack user's public activity. Returns one page of a user's public activity: the notes they wrote, posts they published, and items they liked, replied to, or restacked. types is an optional comma-separated filter accepting `note`, `post`, `like`, `replies` and `restack`; omit it for the default mixed feed. Each item's kind is the upstream's own finer-grained label, so filtering on `restack` returns both `comment_restack` and `post_restack` items. Pagination is cursor-based.
- **Params:** `cursor` (string, optional) — Opaque cursor from a previous response's next_cursor; `types` (string, optional) — Comma-separated activity kinds: note, post, like, replies, restack; `user_id` (integer, **required**) — Numeric user id from the user endpoint

### `substack_user_search`

- **HTTP:** `GET /substack/user/search`
- **What:** Search public Substack writer profiles. Searches public Substack profiles by name or handle. Each result carries the same subscriber signals as /substack/user, so a search enumerates writers without a second lookup per profile. Returns 20 profiles per page; use has_more rather than assuming a fixed depth, since result counts vary by query.
- **Params:** `page` (integer, optional) — Zero-based page; `query` (string, **required**) — Search text matched against profile names and handles
