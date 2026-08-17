# social-media-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**67 endpoints across 9 platform group(s).**

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

## TikTok (25)

### `tiktok_category`

- **HTTP:** `GET /tiktok/category`
- **What:** List TikTok explore categories. Returns the category list exposed by the TikTok Explore page.
- **Params:** _none_

### `tiktok_challenge`

- **HTTP:** `GET /tiktok/hashtag/{name}`
- **What:** Retrieve TikTok hashtag details. Returns the metadata payload for a TikTok hashtag page.
- **Params:** `name` (string, **required**) — Hashtag name (e.g., 'christmas')

### `tiktok_challenge_list`

- **HTTP:** `GET /tiktok/hashtags`
- **What:** Retrieve TikTok hashtag posts. Returns the videos listed for a TikTok hashtag id with cursor-based pagination.
- **Params:** `cursor` (integer, optional) — Pagination cursor; `id` (string, **required**) — Hashtag id returned by the hashtag detail endpoint

### `tiktok_comments`

- **HTTP:** `GET /tiktok/comments`
- **What:** Retrieve TikTok video comments. Returns top-level TikTok video comments with cursor-based pagination.
- **Params:** `aweme_id` (string, **required**) — TikTok video id from the video URL; `cursor` (integer, optional) — Pagination cursor

### `tiktok_creative_center_hashtags`

- **HTTP:** `GET /tiktok/creative-center/hashtags`
- **What:** Retrieve TikTok Creative Center trending hashtags. Returns TikTok Creative Center's ranked trending hashtags for a country and period. TikTok gates this endpoint's full result set behind a logged-in TikTok One account: an anonymous request always receives at most 3 hashtags regardless of country or period.
- **Params:** `country_code` (string, **required**) — ISO-2 country code; `period` (integer, optional) — Lookback window in days

### `tiktok_creative_center_videos`

- **HTTP:** `GET /tiktok/creative-center/videos`
- **What:** Retrieve TikTok Creative Center trending videos. Returns TikTok Creative Center's ranked trending videos for a country, period, and sort order. TikTok reports the true result-set size (see total_count/page_count in the response) but gates access to it behind a logged-in TikTok One account: an anonymous request always receives page 1 (4 videos) regardless of sort order or period. Country coverage is uneven: US, JP, ID, VN, and TH reliably return populated results; other countries have been observed to return an empty videos array (a genuine no-data response, not an error).
- **Params:** `content_label_id` (string, optional) — Content tag id to filter by; `country_code` (string, **required**) — ISO-2 country code; `organic_only` (boolean, optional) — Restrict to organic (non-paid) videos only; `period` (integer, optional) — Lookback window in days; `sort_by` (string, optional) — Sort order

### `tiktok_explore`

- **HTTP:** `GET /tiktok/explore/{id}`
- **What:** Retrieve the TikTok explore feed for a category. Returns explore videos for a TikTok category id from the category endpoint.
- **Params:** `id` (integer, **required**) — Category type id returned by the category endpoint

### `tiktok_popular_trend_country_industry_meta`

- **HTTP:** `GET /tiktok/popular-trend/country-industry-meta`
- **What:** Retrieve TikTok popular-trend country and industry metadata. Returns the country and industry metadata used by the TikTok Creative Center popular-trend endpoints.
- **Params:** _none_

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

### `tiktok_search`

- **HTTP:** `GET /tiktok/search`
- **What:** Search TikTok videos. Searches TikTok videos by keyword with cursor-based pagination.
- **Params:** `count` (integer, optional) — Result count, clamped to 50; `cursor` (integer, optional) — Pagination cursor; `keyword` (string, **required**) — Search keyword

### `tiktok_search_hashtag`

- **HTTP:** `GET /tiktok/search/hashtag`
- **What:** Search TikTok hashtags. Searches TikTok hashtags/challenges by keyword with cursor-based pagination.
- **Params:** `count` (integer, optional) — Result count, clamped to 50; `cursor` (integer, optional) — Pagination cursor; `keyword` (string, **required**) — Search keyword

### `tiktok_search_user`

- **HTTP:** `GET /tiktok/search/user`
- **What:** Search TikTok users. Searches TikTok users by keyword with cursor-based pagination.
- **Params:** `cursor` (integer, optional) — Pagination cursor; `keyword` (string, **required**) — Search keyword

### `tiktok_top_ads_analysis`

- **HTTP:** `GET /tiktok/top-ads/analysis`
- **What:** Retrieve TikTok Top Ads interactive time analysis. Returns the detail-page interactive time analysis chart and percentile for a Top Ads material. Metric values are `retain_ctr` (CTR), `retain_cvr` (CVR), `click_cnt` (Clicks), `convert_cnt` (Conversion), and `play_retain_cnt` (Remain).
- **Params:** `material_id` (string, **required**) — Top Ads material id; `metric` (string, optional) — Interactive time analysis metric; `period_type` (integer, optional) — Percentile lookback period in days

### `tiktok_top_ads_detail`

- **HTTP:** `GET /tiktok/top-ads/detail`
- **What:** Retrieve TikTok Top Ads detail. Returns detail for one TikTok Creative Center Top Ads material. Use `material_id`; the upstream does not accept `id` or `materialId`.
- **Params:** `material_id` (string, **required**) — Top Ads material id

### `tiktok_top_ads_filters`

- **HTTP:** `GET /tiktok/top-ads/filters`
- **What:** Retrieve TikTok Top Ads filters. Returns filter metadata for TikTok Creative Center Top Ads. Dynamic values come from TikTok; static UI enums are included for `order_by`, `duration`, `like`, and `ad_format`.
- **Params:** _none_

### `tiktok_top_ads_list`

- **HTTP:** `GET /tiktok/top-ads/list`
- **What:** Retrieve TikTok Top Ads. Returns high-performing auction ads from TikTok Creative Center. The service defaults `period` to 30, `page` to 1, `limit` to 20, and `order_by` to `for_you`. Use `/tiktok/top-ads/filters` for dynamic enum values and static enums for order, duration, likes, and ad format.
- **Params:** `ad_format` (string, optional) — Ad format id; `ad_language` (string, optional) — Ad language id or comma-separated ids from /tiktok/top-ads/filters; `country_code` (string, optional) — Country code or comma-separated country codes from /tiktok/top-ads/filters; `duration` (string, optional) — Video duration bucket; `industry` (string, optional) — Industry filter id or comma-separated ids from /tiktok/top-ads/filters; `keyword` (string, optional) — Brand or product keyword search; `like` (string, optional) — Like percentile bucket id or comma-separated ids; `limit` (integer, optional) — Maximum number of ads to return; `objective` (string, optional) — Objective filter id or comma-separated ids from /tiktok/top-ads/filters; `order_by` (string, optional) — Sort order; `page` (integer, optional) — Page number; `pattern_label` (string, optional) — Pattern label id or comma-separated ids from /tiktok/top-ads/filters; `period` (integer, optional) — Lookback period in days

### `tiktok_top_ads_location_info`

- **HTTP:** `GET /tiktok/top-ads/location-info`
- **What:** Retrieve TikTok Top Ads location info. Returns the initial location and industry context used by TikTok Creative Center Top Ads.
- **Params:** `module` (integer, optional) — Creative Center module id

### `tiktok_top_ads_locations`

- **HTTP:** `GET /tiktok/top-ads/locations`
- **What:** Retrieve TikTok Top Ads locations. Returns available Top Ads location filters from TikTok Creative Center.
- **Params:** _none_

### `tiktok_top_ads_recommend`

- **HTTP:** `GET /tiktok/top-ads/recommend`
- **What:** Retrieve TikTok Top Ads recommendations. Returns recommended Top Ads materials related to a material id.
- **Params:** `limit` (integer, optional) — Maximum number of ads to return; `material_id` (string, **required**) — Top Ads material id; `page` (integer, optional) — Page number

### `tiktok_top_ads_safety`

- **HTTP:** `GET /tiktok/top-ads/safety`
- **What:** Retrieve TikTok Top Ads safety configuration. Returns public Creative Center safety configuration flags related to search surfaces.
- **Params:** _none_

### `tiktok_top_ads_spotlight`

- **HTTP:** `GET /tiktok/top-ads/spotlight`
- **What:** Retrieve TikTok Top Ads Spotlight. Returns Top Ads Spotlight materials handpicked by TikTok Creative Center.
- **Params:** `limit` (integer, optional) — Maximum number of ads to return; `page` (integer, optional) — Page number

### `tiktok_top_ads_suggestions`

- **HTTP:** `GET /tiktok/top-ads/suggestions`
- **What:** Retrieve TikTok Top Ads suggestions. Returns Top Ads search suggestions from TikTok Creative Center.
- **Params:** `count` (integer, optional) — Maximum number of suggestions to return; `scenario` (integer, optional) — Suggestion scenario id

### `tiktok_trending`

- **HTTP:** `GET /tiktok/trending`
- **What:** Retrieve TikTok trending posts. Returns the current TikTok trending feed.
- **Params:** _none_

## Threads (5)

### `threads_post`

- **HTTP:** `GET /threads/post/{username}/{code}`
- **What:** Retrieve a public Threads post. Returns the public text, author, canonical URL, and preview image for a Threads post.
- **Params:** `code` (string, **required**) — Threads post code; `username` (string, **required**) — Threads username

### `threads_post_replies`

- **HTTP:** `GET /threads/post/{username}/{code}/replies`
- **What:** Retrieve public replies to a Threads post. Returns the public replies currently exposed to logged-out visitors. The response identifies when Threads reports additional replies but withholds a usable continuation cursor.
- **Params:** `code` (string, **required**) — Threads post code; `username` (string, **required**) — Threads username

### `threads_profile`

- **HTTP:** `GET /threads/profile/{username}`
- **What:** Retrieve a public Threads profile. Returns public profile metadata for a Threads username, including the visible biography and counts.
- **Params:** `username` (string, **required**) — Threads username

### `threads_profile_posts`

- **HTTP:** `GET /threads/profile/{username}/posts`
- **What:** Retrieve public posts from a Threads profile. Returns public profile posts with an opaque continuation cursor when more posts are available.
- **Params:** `cursor` (string, optional) — Opaque cursor returned by the previous response; `username` (string, **required**) — Threads username

### `threads_search`

- **HTTP:** `GET /threads/search`
- **What:** Search public Threads posts. Returns the public first page of Threads search results for a query. Logged-out search does not expose a continuation cursor.
- **Params:** `q` (string, **required**) — Search query (1-100 characters)

## Bluesky (7)

### `bluesky_author_feed`

- **HTTP:** `GET /bluesky/author-feed`
- **What:** A Bluesky account's posts. Returns a page of a Bluesky account's posts, newest first, including text, engagement counts, and any attached images/link card/quoted post. Public data, sourced from the AT Protocol's public, credential-free AppView API.
- **Params:** `actor` (string, **required**) — A handle (e.g. bsky.app) or DID; `cursor` (string, optional) — Pagination cursor from a previous response's cursor field; `limit` (integer, optional) — Page size, 1-100

### `bluesky_followers`

- **HTTP:** `GET /bluesky/followers`
- **What:** A Bluesky account's followers. Returns a page of a Bluesky account's followers. Public data, sourced from the AT Protocol's public, credential-free AppView API.
- **Params:** `actor` (string, **required**) — A handle (e.g. bsky.app) or DID; `cursor` (string, optional) — Pagination cursor from a previous response's cursor field; `limit` (integer, optional) — Page size, 1-100

### `bluesky_follows`

- **HTTP:** `GET /bluesky/follows`
- **What:** Accounts a Bluesky account follows. Returns a page of the accounts a Bluesky account follows. Public data, sourced from the AT Protocol's public, credential-free AppView API.
- **Params:** `actor` (string, **required**) — A handle (e.g. bsky.app) or DID; `cursor` (string, optional) — Pagination cursor from a previous response's cursor field; `limit` (integer, optional) — Page size, 1-100

### `bluesky_post_thread`

- **HTTP:** `GET /bluesky/post-thread`
- **What:** A Bluesky post and its reply tree. Returns a Bluesky post along with its nested replies (and, when the post is itself a reply, its parent chain), up to `depth` levels deep. Public data, sourced from the AT Protocol's public, credential-free AppView API.
- **Params:** `depth` (integer, optional) — Reply-tree depth, 1-10; `uri` (string, **required**) — The post's at:// URI, e.g. from an author-feed or search-actors result's post uri field

### `bluesky_profile`

- **HTTP:** `GET /bluesky/profile`
- **What:** A Bluesky account's full public profile. Returns a Bluesky account's public profile: display name, description, avatar/banner images, and follower/follows/posts counts. Public data, sourced from the AT Protocol's public, credential-free AppView API.
- **Params:** `actor` (string, **required**) — A handle (e.g. bsky.app) or DID (e.g. did:plc:z72i7hdynmk6r22z27h6tvur)

### `bluesky_search_actors`

- **HTTP:** `GET /bluesky/search-actors`
- **What:** Search Bluesky accounts. Returns Bluesky accounts matching a query against display name, handle, and profile description. Public data, sourced from the AT Protocol's public, credential-free AppView API.
- **Params:** `cursor` (string, optional) — Pagination cursor from a previous response's cursor field; `limit` (integer, optional) — Page size, 1-100; `q` (string, **required**) — Search text

### `bluesky_trending_topics`

- **HTTP:** `GET /bluesky/trending-topics`
- **What:** Bluesky's current trending topics. Returns Bluesky's current trending topics and suggested feeds, each with a link to its feed. Public data, sourced from the AT Protocol's public, credential-free AppView API. This surface is less stable than the rest of this family -- Bluesky may change its shape without notice.
- **Params:** _none_

## X (3)

### `x_post`

- **HTTP:** `GET /x/post/{id}`
- **What:** Retrieve an X post. Returns a public X post by numeric post id, including author, text, visible metrics, and a quoted post preview when present.
- **Params:** `id` (string, **required**) — X post id; `username` (string, optional) — Expected author username. When provided, mismatched authors return 404.

### `x_profile`

- **HTTP:** `GET /x/profile/{username}`
- **What:** Retrieve an X profile. Returns public profile details for an X username, including visible counts and profile media when available.
- **Params:** `username` (string, **required**) — X username

### `x_profile_posts`

- **HTTP:** `GET /x/profile/{username}/posts`
- **What:** List public X profile posts. Returns posts present in the first public profile page payload for an X username. The endpoint does not paginate replies, media-only tabs, or search results.
- **Params:** `limit` (integer, optional) — Maximum posts returned from the first page payload. Defaults to 20 and must be 1-50.; `username` (string, **required**) — X username

## Pinterest (8)

### `pinterest_board`

- **HTTP:** `GET /pinterest/board/{username}/{slug}`
- **What:** Get a Pinterest board's detail. Returns a Pinterest board's metadata (name, description, cover image, pin/follower counts, owner) plus a page of pins from that board. Public data sourced from Pinterest's own board pages.
- **Params:** `slug` (string, **required**) — Board URL slug, from the board's own /{username}/{slug}/ URL; `username` (string, **required**) — Pinterest username that owns the board

### `pinterest_categories`

- **HTTP:** `GET /pinterest/categories`
- **What:** Get Pinterest's "Ideas" category list. Returns Pinterest's top-level "Ideas" category taxonomy (e.g. "Animals", "Home Decor", "Food And Drink"). Each entry's id is usable directly with GET /pinterest/ideas/{id}. Public data sourced from Pinterest's own ideas.pinterest.com-style category hub.
- **Params:** _none_

### `pinterest_idea`

- **HTTP:** `GET /pinterest/ideas/{id}`
- **What:** Get a Pinterest "Ideas" category's detail feed. Returns one "Ideas" category's metadata (name, description, follower count) plus a page of pins from that category's feed. Public data sourced from Pinterest's own ideas category pages.
- **Params:** `id` (string, **required**) — Pinterest ideas category id. See GET /pinterest/categories for the full list.

### `pinterest_pin`

- **HTTP:** `GET /pinterest/pin/{id}`
- **What:** Get a Pinterest pin's full detail. Returns a single Pinterest pin's full detail: title, description, image, board, pinner, comment count, save count, and creation time. Public data sourced from Pinterest's own pin pages.
- **Params:** `id` (string, **required**) — Pinterest pin id

### `pinterest_search`

- **HTTP:** `GET /pinterest/search`
- **What:** Search Pinterest pins. Returns public Pinterest pins matching a text query: title, description, image, board, and pinner for each result. Public data sourced from Pinterest's own web search.
- **Params:** `query` (string, **required**) — Search text

### `pinterest_user`

- **HTTP:** `GET /pinterest/user/{username}`
- **What:** Get a Pinterest user's public profile. Returns a Pinterest user's public profile: display name, bio, website, avatar, and follower/following/pin/board counts. Public data sourced from Pinterest's own profile pages.
- **Params:** `username` (string, **required**) — Pinterest username

### `pinterest_user_boards`

- **HTTP:** `GET /pinterest/user/{username}/boards`
- **What:** Get a Pinterest user's boards. Returns a page of a Pinterest user's own boards: name, description, cover image, and pin/follower counts for each. Public data sourced from Pinterest's own profile pages.
- **Params:** `username` (string, **required**) — Pinterest username

### `pinterest_user_pins`

- **HTTP:** `GET /pinterest/user/{username}/pins`
- **What:** Get a Pinterest user's own pins. Returns a page of a Pinterest user's own pins: title, description, image, board, and pinner for each. Public data sourced from Pinterest's own profile pages.
- **Params:** `username` (string, **required**) — Pinterest username

## LinkedIn (3)

### `linkedin_company`

- **HTTP:** `GET /linkedin/company/{id}`
- **What:** Get LinkedIn Company info by ID. Returns detailed company information by LinkedIn ID.
- **Params:** `id` (string, **required**) — LinkedIn Company ID

### `linkedin_product`

- **HTTP:** `GET /linkedin/product/{id}`
- **What:** Get LinkedIn Product info by ID. Returns detailed product information from LinkedIn by product ID.
- **Params:** `id` (string, **required**) — LinkedIn Product ID

### `linkedin_showcase`

- **HTTP:** `GET /linkedin/showcase/{id}`
- **What:** Get Linkedin Showcase Page Info. Returns detailed information about a LinkedIn showcase page by ID.
- **Params:** `id` (string, **required**) — LinkedIn Showcase Page ID

## Facebook (2)

### `facebook_marketplace_search`

- **HTTP:** `GET /facebook/marketplace/search`
- **What:** Search Facebook Marketplace. Fetches Facebook Marketplace search or browse results for a location: listing id, title, price, city/state, and a thumbnail image per result. Only the first page Facebook's own server-rendered results page returns is available — Facebook's own further pagination requires a logged-in session and is out of scope. Omit both query and category to get the location's browse feed instead of running a search. minPrice, maxPrice, sortBy, daysSinceListed, and condition only take effect alongside a query or category (Facebook itself ignores them on the plain browse feed), except for the property_rentals category, which has its own always-filtered listing page. This endpoint can take noticeably longer than other search endpoints (up to roughly a minute in the slowest case) as it retries to get past an intermittent upstream condition; priced accordingly.
- **Params:** `category` (string, optional) — Marketplace category; `condition` (string, optional) — Comma-separated listing conditions; requires query or category; `days_since_listed` (integer, optional) — Restrict to listings posted within this many days; requires query or category; `location` (string, **required**) — Facebook Marketplace location vanity slug; `max_price` (integer, optional) — Maximum price in whole currency units; requires query or category; `min_price` (integer, optional) — Minimum price in whole currency units; requires query or category; `query` (string, optional) — Free-text search terms; omit (with category) for the location's browse feed; `sort_by` (string, optional) — Result order; requires query or category

### `facebook_page`

- **HTTP:** `GET /facebook/{page}`
- **What:** Get Facebook page details. Fetches public data about a Facebook Page given its page ID, vanity name, or full page URL: name, follower/like counts, intro, category, business hours/price range, review count, and any public contact details (email, phone, address, website, WhatsApp number) exposed on the Page's About tab.
- **Params:** `page` (string, **required**) — Facebook Page reference: vanity name, handle, profile.php id, or full Facebook URL

## Reddit (11)

### `reddit_comments`

- **HTTP:** `GET /reddit/comments/{id}`
- **What:** Get Reddit post comments. Returns a Reddit post with its public comments. The default 1-credit mode uses RSS. Set `include_metrics=true` to use the anonymous HTML post page as the sole content request and return the server-rendered comments with public net score and award count plus post engagement metrics for 3 credits. Large threads may expose only an initial comment subset in anonymous HTML. Reddit does not expose per-comment upvote ratios or exact upvote/downvote totals anonymously. A post that exists but has no comments yet returns a 200 response with an empty comments list; a post that does not exist returns 404, and a temporary block or upstream failure returns 503 (retryable) rather than 404.
- **Params:** `depth` (integer, optional) — Maximum flat comment depth returned in metrics mode.; `id` (string, **required**) — Reddit post id or t3_ id; `include_metrics` (boolean, optional) — Include public post and per-comment engagement metrics; costs 3 credits instead of 1; `limit` (integer, optional) — Maximum comments returned, defaults to 25 and clamps to 100; `sort` (string, optional) — Comment order: confidence, top, new, controversial, old, or qa. Applied to the anonymous HTML request when metrics are enabled.

### `reddit_domain_posts`

- **HTTP:** `GET /reddit/domain/{domain}/posts`
- **What:** List Reddit domain posts. Returns normalized public posts submitted from a linked domain. A `503` with a `Retry-After` header means Reddit is temporarily throttling the request; wait that many seconds and retry.
- **Params:** `after` (string, optional) — Reddit pagination token; `domain` (string, **required**) — Domain hostname, without scheme or path; `limit` (integer, optional) — Maximum posts, defaults to 25 and clamps to 100; `sort` (string, optional) — Sort: hot, new, top, or rising; `time` (string, optional) — Time window for top sort: hour, day, week, month, year, or all

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
