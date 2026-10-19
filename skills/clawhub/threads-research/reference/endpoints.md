# threads-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**5 endpoints across 1 platform group(s).**

## Threads (5)

### `threads_post`

- **HTTP:** `GET /threads/post/{username}/{code}`
- **What:** Retrieve a public Threads post. Returns one public Threads post by `username` (with or without a leading `@`) and the post `code` from its URL. The response has the post text, canonical URL, preview image URL, and the author's id, name and username. Replies and logged-in fields are not included. An unavailable post returns 404.
- **Params:** `code` (string, **required**) — Threads post code; `username` (string, **required**) — Threads username

### `threads_post_replies`

- **HTTP:** `GET /threads/post/{username}/{code}/replies`
- **What:** Retrieve public replies to a Threads post. Returns the public replies currently exposed to logged-out visitors. The response identifies when Threads reports additional replies but withholds a usable continuation cursor.
- **Params:** `code` (string, **required**) — Threads post code; `username` (string, **required**) — Threads username

### `threads_profile`

- **HTTP:** `GET /threads/profile/{username}`
- **What:** Retrieve a public Threads profile. Returns a public Threads profile by `username` (with or without a leading `@`): name, profile URL, biography, avatar URL, `followers_count` and `threads_count`. Counts are derived from the compact figures shown on the profile page. An unavailable profile returns 404.
- **Params:** `username` (string, **required**) — Threads username

### `threads_profile_posts`

- **HTTP:** `GET /threads/profile/{username}/posts`
- **What:** Retrieve public posts from a Threads profile. Lists public posts from a Threads profile by `username`. Each item has its code, URL, text, creation time, image and video URLs, like, reply, repost and quote counts, reply flag and author. When `has_more` is true, pass `next_cursor` unchanged as `cursor` to fetch the next page.
- **Params:** `cursor` (string, optional) — Opaque cursor returned by the previous response; `username` (string, **required**) — Threads username

### `threads_search`

- **HTTP:** `GET /threads/search`
- **What:** Search public Threads posts. Returns the public first page of Threads search results for a query. Logged-out search does not expose a continuation cursor.
- **Params:** `q` (string, **required**) — Search query (1-100 characters)
