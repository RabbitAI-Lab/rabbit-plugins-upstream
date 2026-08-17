# anime-manga-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**12 endpoints across 2 platform group(s).**

## Anime (9)

### `anime_airing_schedule`

- **HTTP:** `GET /anime/airing-schedule`
- **What:** Upcoming anime airing schedule. Returns upcoming anime episode broadcasts (episode number, air time, countdown, and the normalized title), soonest first, paginated. Credential-free public AniList data.
- **Params:** `page` (integer, optional) — 1-based page number, default 1; `per_page` (integer, optional) — Results per page, default 20, max 50

### `anime_character`

- **HTTP:** `GET /anime/character/{id}`
- **What:** Get an anime/manga character. Returns a normalized character profile by AniList id: names, image, description, gender, age, blood type, birthday, favourites, and the titles the character appears in with their billed role. Credential-free public AniList data.
- **Params:** `id` (string, **required**) — AniList character id

### `anime_character_search`

- **HTTP:** `GET /anime/character/search`
- **What:** Search anime & manga characters. Searches anime and manga characters by name. Returns character summaries (name, native name, image, favourites), paginated. Credential-free public AniList data.
- **Params:** `page` (integer, optional) — 1-based page number, default 1; `per_page` (integer, optional) — Results per page, default 10, max 50; `query` (string, **required**) — Search text

### `anime_rankings`

- **HTTP:** `GET /anime/rankings`
- **What:** Rank anime. Returns a filterable, sorted anime ranking. Credential-free public AniList data. Filter by season, year, format, genre, and status.
- **Params:** `format` (string, optional) — Format filter: TV, TV_SHORT, MOVIE, SPECIAL, OVA, ONA, MUSIC.; `genre` (string, optional) — Genre filter, e.g. Fantasy.; `page` (integer, optional) — 1-based page number, default 1; `per_page` (integer, optional) — Results per page, default 20, max 50; `season` (string, optional) — Airing season filter: WINTER, SPRING, SUMMER, FALL.; `season_year` (integer, optional) — Airing year filter, 1940-2100.; `sort` (string, optional) — Order: TRENDING_DESC, POPULARITY_DESC, SCORE_DESC, FAVOURITES_DESC, START_DATE_DESC, UPDATED_AT_DESC. Default TRENDING_DESC.; `status` (string, optional) — Status filter: FINISHED, RELEASING, NOT_YET_RELEASED, CANCELLED, HIATUS.

### `anime_search`

- **HTTP:** `GET /anime/search`
- **What:** Search anime. Searches anime by free-text query. Credential-free public anime data from AniList. Returns normalized entries: titles, scores, popularity, format, status, season, genres, tags, and studios.
- **Params:** `page` (integer, optional) — 1-based page number, default 1; `per_page` (integer, optional) — Results per page, default 10, max 50; `query` (string, **required**) — Search text; `sort` (string, optional) — Ordering: SEARCH_MATCH, POPULARITY_DESC, SCORE_DESC, TRENDING_DESC, FAVOURITES_DESC, START_DATE_DESC. Default SEARCH_MATCH.

### `anime_title`

- **HTTP:** `GET /anime/title/{id}`
- **What:** Get an anime. Returns a normalized anime by AniList id: titles (romaji/english/native), MyAnimeList id, scores, popularity, favourites, format, status, season, episodes, duration, genres, ranked tags, studios, dates, description, images, and next-airing countdown. Pass mal=true to additionally enrich the response with the MyAnimeList community score (mal block: score on a 0-10 scale, plus scored-by count), scraped credential-free from the public MAL page. Credential-free public AniList data.
- **Params:** `id` (string, **required**) — AniList anime id; `mal` (boolean, optional) — Enrich with the MyAnimeList community score (adds one fetch; omitted when the title has no MAL id)

### `anime_title_characters`

- **HTTP:** `GET /anime/title/{id}/characters`
- **What:** List an anime's characters. Returns an anime's cast (character name, native name, billed role, image, favourites), paginated. Credential-free public AniList data.
- **Params:** `id` (string, **required**) — AniList anime id; `page` (integer, optional) — 1-based page number, default 1; `per_page` (integer, optional) — Results per page, default 10, max 50

### `anime_title_recommendations`

- **HTTP:** `GET /anime/title/{id}/recommendations`
- **What:** List an anime's recommendations. Returns community-recommended titles for an anime, each with a recommendation rating and the full normalized media entry, paginated. Credential-free public AniList data.
- **Params:** `id` (string, **required**) — AniList anime id; `page` (integer, optional) — 1-based page number, default 1; `per_page` (integer, optional) — Results per page, default 10, max 50

### `anime_title_staff`

- **HTTP:** `GET /anime/title/{id}/staff`
- **What:** List an anime's staff. Returns the people credited on an anime (name, production role, occupations, image), paginated. Credential-free public AniList data.
- **Params:** `id` (string, **required**) — AniList anime id; `page` (integer, optional) — 1-based page number, default 1; `per_page` (integer, optional) — Results per page, default 10, max 50

## Manga (3)

### `manga_rankings`

- **HTTP:** `GET /manga/rankings`
- **What:** Rank manga. Returns a filterable, sorted manga ranking. Credential-free public AniList data. Filter by format, genre, and status.
- **Params:** `format` (string, optional) — Format filter: MANGA, NOVEL, ONE_SHOT.; `genre` (string, optional) — Genre filter, e.g. Fantasy.; `page` (integer, optional) — 1-based page number, default 1; `per_page` (integer, optional) — Results per page, default 20, max 50; `sort` (string, optional) — Order: TRENDING_DESC, POPULARITY_DESC, SCORE_DESC, FAVOURITES_DESC, START_DATE_DESC, UPDATED_AT_DESC. Default TRENDING_DESC.; `status` (string, optional) — Status filter: FINISHED, RELEASING, NOT_YET_RELEASED, CANCELLED, HIATUS.

### `manga_search`

- **HTTP:** `GET /manga/search`
- **What:** Search manga. Searches manga by free-text query. Credential-free public manga data from AniList. Returns normalized entries: titles, scores, popularity, format, status, chapters, volumes, genres, and tags.
- **Params:** `page` (integer, optional) — 1-based page number, default 1; `per_page` (integer, optional) — Results per page, default 10, max 50; `query` (string, **required**) — Search text; `sort` (string, optional) — Ordering: SEARCH_MATCH, POPULARITY_DESC, SCORE_DESC, TRENDING_DESC, FAVOURITES_DESC, START_DATE_DESC. Default SEARCH_MATCH.

### `manga_title`

- **HTTP:** `GET /manga/title/{id}`
- **What:** Get a manga. Returns a normalized manga by AniList id: titles, MyAnimeList id, scores, popularity, favourites, format, status, chapters, volumes, genres, ranked tags, dates, description, and images. Pass mal=true to additionally enrich the response with the MyAnimeList community score (mal block: score on a 0-10 scale, plus scored-by count), scraped credential-free from the public MAL page. Credential-free public AniList data.
- **Params:** `id` (string, **required**) — AniList manga id; `mal` (boolean, optional) — Enrich with the MyAnimeList community score (adds one fetch; omitted when the title has no MAL id)
