# news-media-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**10 endpoints across 3 platform group(s).**

## BBC (4)

### `bbc_article`

- **HTTP:** `GET /bbc/article`
- **What:** Get BBC News article content. Returns a BBC News article's public metadata and body paragraphs from a canonical article URL. Live pages are not supported.
- **Params:** `url` (string, **required**) — Canonical BBC News article URL

### `bbc_headlines`

- **HTTP:** `GET /bbc/headlines`
- **What:** Get BBC News section headlines. Returns fresh headlines from a public BBC News RSS section. section defaults to world.
- **Params:** `section` (string, optional) — BBC News RSS section, defaults to world

### `bbc_live`

- **HTTP:** `GET /bbc/live`
- **What:** Get a BBC News live-page text snapshot. Returns the current server-rendered text updates from one canonical BBC News live URL. It does not subscribe to updates or return broadcast, player, or stream data.
- **Params:** `url` (string, **required**) — Canonical BBC News live URL

### `bbc_search`

- **HTTP:** `GET /bbc/search`
- **What:** Search public BBC pages. Returns a bounded page of public BBC search-result metadata. Media entries link only to their BBC landing pages; streams, downloads, and transcripts are not returned.
- **Params:** `page` (integer, optional) — Results page, defaults to 1; `q` (string, **required**) — Search query, up to 120 characters

## CNN (3)

### `cnn_article`

- **HTTP:** `GET /cnn/article`
- **What:** CNN article content. Returns a CNN article's headline, description, author, publication and update times, section, image, and body paragraphs. Provide a canonical cnn.com article URL.
- **Params:** `url` (string, **required**) — Canonical cnn.com article URL

### `cnn_headlines`

- **HTTP:** `GET /cnn/headlines`
- **What:** CNN section headlines. Returns the current CNN headline stream for one section, including title, article URL, description, publication time, and image when available.
- **Params:** `section` (string, optional) — CNN section. Allowed values: world, us, politics, business, health, entertainment, style, travel, sports, science, climate, weather, opinion. Default world.

### `cnn_live_story`

- **HTTP:** `GET /cnn/live-story`
- **What:** CNN live story updates. Returns a CNN live story's title, description, update time, and chronological post updates. Provide a canonical cnn.com live-news URL.
- **Params:** `url` (string, **required**) — Canonical cnn.com live-news URL

## Guardian (3)

### `guardian_article`

- **HTTP:** `GET /guardian/article`
- **What:** Get Guardian article content. Returns a Guardian article's public metadata and body paragraphs from a canonical article URL. Live-blog timelines are not supported.
- **Params:** `url` (string, **required**) — Canonical www.theguardian.com article URL

### `guardian_headlines`

- **HTTP:** `GET /guardian/headlines`
- **What:** Get Guardian section headlines. Returns fresh headlines from a public Guardian RSS section. section defaults to world.
- **Params:** `section` (string, optional) — Guardian RSS section, defaults to world

### `guardian_topic`

- **HTTP:** `GET /guardian/topic`
- **What:** Get Guardian topic archive. Returns a paginated public Guardian topic or category archive. topic is a Guardian tag or section slug and page defaults to 1.
- **Params:** `page` (integer, optional) — 1-based archive page, defaults to 1; `topic` (string, **required**) — Guardian tag or section slug
