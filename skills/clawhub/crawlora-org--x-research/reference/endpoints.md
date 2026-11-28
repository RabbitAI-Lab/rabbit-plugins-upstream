# x-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**8 endpoints across 1 platform group(s).**

## X (8)

### `x_post`

- **HTTP:** `GET /x/post/{id}`
- **What:** Retrieve an X post. Returns a public X post by numeric post id, including author, text, visible metrics, and a quoted post preview when present.
- **Params:** `id` (string, **required**) — X post id; `username` (string, optional) — Expected author username. When provided, mismatched authors return 404.

### `x_post_detail`

- **HTTP:** `GET /x/post/{id}/detail`
- **What:** Retrieve full public X post detail. Returns the rich public payload for one X post: full text (including long-form note text), creation time, language, author, complete interaction counts (replies, reposts, likes, bookmarks, quotes, views), media attachments with dimensions and video URLs, hashtags, mentions, expanded URLs, and a quoted-post preview. Use this when `x_post`'s smaller page-parsed payload is not enough; it reads the same public post X's logged-out client receives and does not require login.
- **Params:** `id` (string, **required**) — X post id

### `x_profile`

- **HTTP:** `GET /x/profile/{username}`
- **What:** Retrieve an X profile. Returns the public profile of an X account by `username`, with or without a leading `@`: name, description, location, avatar and banner images, creation date, verification flags, and `metrics` for followers, following, posts, likes, listed and media. `verified_type` and `affiliate_label` appear only when the account has them. Returns 404 when the profile is not public.
- **Params:** `username` (string, **required**) — X username

### `x_profile_highlights`

- **HTTP:** `GET /x/profile/{username}/highlights`
- **What:** List public X profile highlights. Returns a page of an X profile's curated `highlights` timeline: the posts X selects for the profile's Highlights area, not the chronological timeline. This feed is curated rather than real-time and can lag the profile's newest posts. Pass `next_cursor` back as `cursor` to fetch the next page; a page with `has_more: false` and no `next_cursor` is the end of the list.
- **Params:** `cursor` (string, optional) — Opaque pagination cursor from a previous page's next_cursor.; `limit` (integer, optional) — Maximum posts returned per page. Defaults to 20 and must be 1-50.; `username` (string, **required**) — X username

### `x_profile_posts`

- **HTTP:** `GET /x/profile/{username}/posts`
- **What:** List public X profile posts. Returns posts present in the first public profile page payload for an X username. The endpoint does not paginate replies, media-only tabs, or search results.
- **Params:** `limit` (integer, optional) — Maximum posts returned from the first page payload. Defaults to 20 and must be 1-50.; `username` (string, **required**) — X username

### `x_trending`

- **HTTP:** `GET /x/trending`
- **What:** List public X trending posts. Returns the posts in X's logged-out trending timeline, newest first as X serves them. This is a post feed, not a trends/topic list: the payload carries no trend names, ranks, or categories. X returns one fixed set per call (no pagination cursor) and may include fewer than twenty posts.
- **Params:** _none_

### `x_trends`

- **HTTP:** `GET /x/trends`
- **What:** List X trending topics for a location. Returns X's trending topics for one WOEID location: each trend's name, the search query and URL X links it to, whether it is promoted, and X's tweet-volume estimate when X supplies one. This is the topics list that complements `x_trending` (which returns posts); it is not a paginated search. `woeid` defaults to `1` (Worldwide); discover the complete accepted value space with `x_trends_locations`. X returns one fixed set per call (no cursor) with up to fifty trends, and `tweet_volume` is null for many trends.
- **Params:** `woeid` (integer, optional) — X trends location WOEID. Defaults to 1 (Worldwide); use x_trends_locations to list valid values.

### `x_trends_locations`

- **HTTP:** `GET /x/trends/locations`
- **What:** List or resolve X trends locations. Without coordinates, returns X's complete trends location catalog: each location's name, WOEID, place type, parent WOEID, country and ISO country code. Pass those WOEIDs to `x_trends` for that location's trending topics. With both `lat` and `long`, resolves the single nearest catalog location instead of listing the catalog; both coordinates are required together.
- **Params:** `lat` (number, optional) — Latitude (-90 to 90) for nearest-location resolution; requires long.; `long` (number, optional) — Longitude (-180 to 180) for nearest-location resolution; requires lat.
