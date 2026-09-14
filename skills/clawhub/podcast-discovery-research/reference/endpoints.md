# podcast-discovery-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**16 endpoints across 2 platform group(s).**

## ApplePodcasts (8)

### `apple_podcasts_charts`

- **HTTP:** `GET /apple-podcasts/charts`
- **What:** Retrieve Apple Podcasts chart rankings. Returns Apple Podcasts show chart rankings from public iTunes RSS JSON feeds. Supported collections are `toppodcasts` and `topaudiopodcasts`.
- **Params:** `category` (integer, optional) — Numeric Apple podcast genre ID; `collection` (string, optional) — Chart collection; `country` (string, optional) — Two-letter storefront country code; `limit` (integer, optional) — Number of chart items to return

### `apple_podcasts_charts_rankings`

- **HTTP:** `GET /apple-podcasts/charts/rankings`
- **What:** Retrieve Apple Podcasts chart rankings by algorithm, type, and genre. Returns Apple Podcasts chart rankings from the modern podcasts.apple.com charts page, covering chart algorithms (`top`, `top-subscriber`, `top-series`) crossed with entity types (`podcasts`, `podcast-episodes`, `podcast-channels`) and an optional genre filter. A richer, differently-sourced capability than the legacy RSS-based `/apple-podcasts/charts` endpoint.
- **Params:** `chart` (string, optional) — Chart algorithm. Allowed values: `top`, `top-subscriber`, `top-series`. Default `top`.; `country` (string, optional) — Two-letter storefront country code; `genre` (integer, optional) — Optional Apple Podcasts genre ID to filter the chart, e.g. 1303 for Comedy; `limit` (integer, optional) — Number of chart entries to return, default 24, max 200; `type` (string, optional) — Entity type. Allowed values: `podcasts`, `podcast-episodes`, `podcast-channels`. Default `podcasts`.

### `apple_podcasts_episodes_search`

- **HTTP:** `GET /apple-podcasts/episodes/search`
- **What:** Search Apple Podcasts episodes. Returns normalized Apple Podcasts episodes from Apple's public iTunes Search API.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `lang` (string, optional) — Result language tag; `limit` (integer, optional) — Number of episodes per page; `page` (integer, optional) — Search page number (1-based); `term` (string, **required**) — Search term

### `apple_podcasts_new`

- **HTTP:** `GET /apple-podcasts/new`
- **What:** Retrieve Apple Podcasts curated "New" editorial shelves. Returns the curated editorial shelves from podcasts.apple.com/{country}/new (New Shows, New Seasons, New Trailers, Essentials, and other seasonal spotlights). Shelves that merely mirror a Charts Rankings query are omitted here since `/apple-podcasts/charts/rankings` already covers that data.
- **Params:** `country` (string, optional) — Two-letter storefront country code

### `apple_podcasts_search`

- **HTTP:** `GET /apple-podcasts/search`
- **What:** Search Apple Podcasts shows. Returns normalized Apple Podcasts shows from Apple's public iTunes Search API.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `lang` (string, optional) — Result language tag; `limit` (integer, optional) — Number of shows per page; `page` (integer, optional) — Search page number (1-based); `term` (string, **required**) — Search term

### `apple_podcasts_show`

- **HTTP:** `GET /apple-podcasts/show/{id}`
- **What:** Retrieve Apple Podcasts show details. Returns normalized show metadata from Apple's public iTunes Lookup API.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `id` (string, **required**) — Apple Podcasts show ID; `lang` (string, optional) — Result language tag

### `apple_podcasts_show_episodes`

- **HTTP:** `GET /apple-podcasts/show/{id}/episodes`
- **What:** Retrieve Apple Podcasts show episodes. Returns a show and its public Apple Podcasts episodes from Apple's iTunes Lookup API.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `id` (string, **required**) — Apple Podcasts show ID; `lang` (string, optional) — Result language tag; `limit` (integer, optional) — Number of episodes to return

### `apple_podcasts_show_related`

- **HTTP:** `GET /apple-podcasts/show/{id}/related`
- **What:** Retrieve Apple Podcasts "You Might Also Like" related shows. Returns the "You Might Also Like" rail for a single show, sourced from the modern podcasts.apple.com show page's listener-cohort recommendation data.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `id` (string, **required**) — Apple Podcasts show ID; `limit` (integer, optional) — Number of related shows to return, default 20, max 50

## SpotifyPodcasts (8)

### `spotify_podcasts_categories`

- **HTTP:** `GET /spotify-podcasts/categories`
- **What:** Retrieve Spotify Podcasts categories. Returns normalized Spotify podcast category sections and items from Spotify's all-categories browsePage Pathfinder response.
- **Params:** `include_episode_content_ratings_v2` (boolean, optional) — Include Spotify episode content ratings v2; `page_limit` (integer, optional) — Page pagination limit, clamped to 1-50; `page_offset` (integer, optional) — Page pagination offset; `section_limit` (integer, optional) — Section pagination limit, clamped to 1-50; `section_offset` (integer, optional) — Section pagination offset; `uri` (string, optional) — Spotify podcast categories page URI

### `spotify_podcasts_charts`

- **HTTP:** `GET /spotify-podcasts/charts`
- **What:** Retrieve Spotify podcast charts. Returns normalized Spotify podcast chart rankings from podcastcharts.byspotify.com. The chart and region parameters are validated against Spotify's supported podcast chart slugs and countries. Category charts are available only in au, br, de, gb, mx, se, and us.
- **Params:** `chart` (string, optional) — Chart slug. Allowed: top-podcasts, top-episodes, trending, arts, business, comedy, education, fiction, health-fitness, history, leisure, music, news, religion-spirituality, science, society-culture, sports, technology, true-crime, tv-film; `limit` (integer, optional) — Result limit, clamped to 1-100; `region` (string, optional) — Two-letter region code. Allowed: ar, au, at, br, ca, cl, co, dk, fi, fr, de, in, id, ie, it, jp, mx, nz, no, ph, pl, es, se, nl, gb, us

### `spotify_podcasts_episode`

- **HTTP:** `GET /spotify-podcasts/episode`
- **What:** Retrieve Spotify podcast episode details. Returns normalized public episode metadata from Spotify's getEpisodeOrChapter Pathfinder response, with episode page, embed page, and anonymous oEmbed fallbacks when Pathfinder is unavailable. Provide either uri or id; defaults to a known public episode when omitted.
- **Params:** `id` (string, optional) — Spotify episode ID. Used when uri is omitted; `uri` (string, optional) — Spotify episode URI or open.spotify.com episode URL

### `spotify_podcasts_home`

- **HTTP:** `GET /spotify-podcasts/home`
- **What:** Retrieve Spotify Podcasts home. Returns normalized sections and items from Spotify's podcast home browsePage Pathfinder response.
- **Params:** `include_episode_content_ratings_v2` (boolean, optional) — Include Spotify episode content ratings v2; `page_limit` (integer, optional) — Page pagination limit, clamped to 1-50; `page_offset` (integer, optional) — Page pagination offset; `section_limit` (integer, optional) — Section pagination limit, clamped to 1-50; `section_offset` (integer, optional) — Section pagination offset; `uri` (string, optional) — Spotify page or genre URI

### `spotify_podcasts_search`

- **HTTP:** `GET /spotify-podcasts/search`
- **What:** Search Spotify Podcasts. Returns normalized Spotify podcast shows, episodes, and top results for a search term.
- **Params:** `include_album_pre_releases` (boolean, optional) — Include album pre-release results; `include_audiobooks` (boolean, optional) — Include audiobooks; `include_authors` (boolean, optional) — Include authors; `include_episode_content_ratings_v2` (boolean, optional) — Include Spotify episode content ratings v2; `include_pre_releases` (boolean, optional) — Include pre-release results; `limit` (integer, optional) — Result limit, clamped to 1-50; `number_of_top_results` (integer, optional) — Top result limit, clamped to 1-50; `offset` (integer, optional) — Search offset; `q` (string, **required**) — Podcast search term

### `spotify_podcasts_show`

- **HTTP:** `GET /spotify-podcasts/show`
- **What:** Retrieve Spotify podcast show metadata. Returns normalized podcast show metadata from Spotify Pathfinder.
- **Params:** `include_content_capability_trait` (boolean, optional) — Include content capability trait; `include_episode_content_ratings_v2` (boolean, optional) — Include Spotify episode content ratings v2; `uri` (string, optional) — Spotify show URI

### `spotify_podcasts_show_episodes`

- **HTTP:** `GET /spotify-podcasts/show/episodes`
- **What:** Retrieve Spotify podcast show episodes. Returns normalized podcast episodes for a Spotify show URI.
- **Params:** `include_episode_content_ratings_v2` (boolean, optional) — Include Spotify episode content ratings v2; `limit` (integer, optional) — Episode limit, clamped to 1-50; `offset` (integer, optional) — Episode offset; `uri` (string, optional) — Spotify show URI

### `spotify_podcasts_show_recommendations`

- **HTTP:** `GET /spotify-podcasts/show/recommendations`
- **What:** Retrieve Spotify podcast recommendations. Returns normalized related Spotify shows and episodes from Spotify's show recommendations response.
- **Params:** `uri` (string, optional) — Spotify show URI
