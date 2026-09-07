# bluesky-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**7 endpoints across 1 platform group(s).**

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
