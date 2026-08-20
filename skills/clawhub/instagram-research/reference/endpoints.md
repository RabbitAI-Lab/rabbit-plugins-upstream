# instagram-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**3 endpoints across 1 platform group(s).**

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
