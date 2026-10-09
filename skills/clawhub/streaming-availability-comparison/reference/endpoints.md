# streaming-availability-comparison — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Only the endpoints used by this workflow. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**8 endpoints across 1 platform group(s).**

## JustWatch (8)

### `justwatch_episode_offers`

- **HTTP:** `GET /justwatch/episode/offers`
- **What:** Get JustWatch episode offers. Returns normalized offers for a raw JustWatch episode id across one to five comma-separated country codes.
- **Params:** `countries` (string, optional) — One to five comma-separated two-letter country codes; `id` (string, **required**) — Raw JustWatch episode id matching tse[0-9]+; `language` (string, optional) — Two-letter language code

### `justwatch_provider_titles`

- **HTTP:** `GET /justwatch/provider/titles`
- **What:** Get JustWatch provider titles. Returns popular movie/show titles available through a JustWatch provider short name such as `nfx`.
- **Params:** `country` (string, optional) — Two-letter country code; `language` (string, optional) — Two-letter language code; `limit` (integer, optional) — Maximum results, defaults to 20 and clamps to 50; `provider` (string, **required**) — JustWatch provider short name; `type` (string, optional) — Title type: all, movie, show

### `justwatch_providers`

- **HTTP:** `GET /justwatch/providers`
- **What:** Get JustWatch providers. Returns the credential-free public JustWatch provider catalog for a country.
- **Params:** `country` (string, optional) — Two-letter country code

### `justwatch_search`

- **HTTP:** `GET /justwatch/search`
- **What:** Search JustWatch titles. Searches JustWatch titles using the public credential-free website GraphQL endpoint. Country must be a two-letter ISO code such as `US`; language must be a two-letter code such as `en`.
- **Params:** `country` (string, optional) — Two-letter country code; `language` (string, optional) — Two-letter language code; `limit` (integer, optional) — Maximum results, defaults to 10 and clamps to 25; `query` (string, **required**) — Search query

### `justwatch_season_episodes`

- **HTTP:** `GET /justwatch/season/episodes`
- **What:** Get JustWatch season episodes. Returns episodes and normalized episode offers for a raw JustWatch season id such as `tss297253`.
- **Params:** `country` (string, optional) — Two-letter country code; `language` (string, optional) — Two-letter language code; `season_id` (string, **required**) — Raw JustWatch season id matching tss[0-9]+

### `justwatch_show_seasons`

- **HTTP:** `GET /justwatch/show/seasons`
- **What:** Get JustWatch show seasons. Returns seasons for a raw JustWatch show id such as `ts287292`.
- **Params:** `country` (string, optional) — Two-letter country code; `language` (string, optional) — Two-letter language code; `show_id` (string, **required**) — Raw JustWatch show id matching ts[0-9]+

### `justwatch_title_by_id`

- **HTTP:** `GET /justwatch/title/by-id`
- **What:** Get JustWatch title by raw id. Looks up a movie or show by raw JustWatch GraphQL id such as `tm92641` or `ts287292`.
- **Params:** `country` (string, optional) — Two-letter country code; `id` (string, **required**) — Raw JustWatch movie/show id matching tm[0-9]+ or ts[0-9]+; `language` (string, optional) — Two-letter language code

### `justwatch_title_offers`

- **HTTP:** `GET /justwatch/title/offers`
- **What:** Get JustWatch title offers. Returns normalized offers for a raw JustWatch movie/show id across one to five comma-separated country codes.
- **Params:** `countries` (string, optional) — One to five comma-separated two-letter country codes; `id` (string, **required**) — Raw JustWatch movie/show id matching tm[0-9]+ or ts[0-9]+; `language` (string, optional) — Two-letter language code
