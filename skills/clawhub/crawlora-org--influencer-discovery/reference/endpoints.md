# influencer-discovery — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Only the endpoints used by this workflow. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**18 endpoints across 4 platform group(s).**

## Datasets (7)

### `datasets_creators_search`

- **HTTP:** `GET /datasets/creators/search`
- **What:** Search the TikTok creators dataset. Searches TikTok creators stored in a search index (one document per creator), with follower counts, verified status, niche, and engagement. Deleted and private accounts are excluded by default; set `include_inactive=true` to include them for historical lookups. Sort enum: `followers_desc`, `engagement_desc`, `likes_desc`, `relevance`. Coverage note: `followers_desc`, `likes_desc`, and `relevance` are backed by profile fields present across the full dataset; the post-level engagement metrics (`engagement_rate`, `avg_views`, and the nested `post_stats` object) and the `engagement_desc` sort are currently populated for a growing subset of creators, prioritizing the highest-reach accounts. Creators without these metrics are still returned but sort last under `engagement_desc` and omit those fields. Sound fields: `post_stats.top_sounds` holds only a creator's FIVE most-used sounds from the sampled posts, ranked by use count with ties broken by lowest `music_id`, so it is a top-5 view and not the creator's full sound list; `post_stats.distinct_sounds` gives the true number of different sounds the sample used. Use each sound's `original` boolean to tell TikTok-generated original audio from catalogue tracks - do NOT infer it from the title, because TikTok localizes the original-audio label (`sonido original`, `som original`, `оригинальный звук`, and at least fifteen more), so a title match silently reclassifies original audio as named tracks.
- **Params:** `country` (string, optional) — Exact creator country/region filter, max 128 characters; `handle` (string, optional) — Exact handle lookup (case-insensitive), e.g. khaby.lame; returns the single creator with that exact @handle; `has_email` (boolean, optional) — Filter by contact-email presence; true keeps only creators with an email; `include_email` (boolean, optional) — Return the stored contact email instead of a blanked value. Off by default for everyone, and honoured only for entitled (non-Free) API keys; `include_inactive` (boolean, optional) — Include deleted/private accounts; defaults to false (only live accounts returned); `min_followers` (integer, optional) — Minimum follower count; `niche` (string, optional) — Exact content-niche filter, max 128 characters; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `q` (string, optional) — Full-text query over handle, nickname and bio, max 256 characters; `sort` (string, optional) — Sort enum: followers_desc, engagement_desc, likes_desc, relevance. engagement_desc ranks by post-level engagement rate, currently populated for a subset of creators (highest-reach first); creators without it sort last; `verified` (boolean, optional) — Filter by verified badge; true keeps only verified creators

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
- **What:** Retrieve a specific Instagram post by user ID and post ID. Returns the media details of a specific post from an Instagram user.
- **Params:** `id` (string, **required**) — Instagram user ID; `post_id` (string, **required**) — Instagram post ID

### `instagram_profile`

- **HTTP:** `GET /instagram/profile/{username}`
- **What:** Retrieve an Instagram user profile by username. Returns public profile details for a specified Instagram username.
- **Params:** `username` (string, **required**) — Instagram username

### `instagram_reels`

- **HTTP:** `GET /instagram/reels/{id}`
- **What:** Retrieve Instagram Reels for a user. Returns a feed of Instagram Reels for the specified user ID. Supports pagination via `max_id`.
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
- **What:** Search YouTube. Returns normalized YouTube search results using YouTube's InnerTube search API. Pass `continuation_token` from a previous response to retrieve the next page. Use `q` as the primary query parameter; `search_query` is accepted as an alias.
- **Params:** `continuation_token` (string, optional) — Pagination token returned by a previous request; `duration` (string, optional) — Filter by duration; `features` (string, optional) — Comma-separated feature filters; `params` (string, optional) — Raw protobuf-encoded search filter (base64); `q` (string, optional) — Search query; `search_query` (string, optional) — Alias for q; `sort_by` (string, optional) — Sort results; `type` (string, optional) — Filter by type; `upload_date` (string, optional) — Filter by upload date

### `youtube_video`

- **HTTP:** `GET /youtube/video/{id}`
- **What:** Retrieve video metadata & captions. Returns title, description, stats, and captions for a YouTube video ID.
- **Params:** `id` (string, **required**) — YouTube video ID (11-char code)
