# entertainment-discovery-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**84 endpoints across 5 platform group(s).**

## IMDb (30)

### `imdb_charts`

- **HTTP:** `GET /imdb/charts`
- **What:** IMDb title charts. Returns normalized rows from public IMDb title charts. Chart values: `top_rated_movies`, `top_rated_tv_shows`, `most_popular_movies`, `most_popular_tv_shows`, `top_rated_english_movies`, `lowest_rated_movies`.
- **Params:** `chart` (string, optional) — IMDb chart; `limit` (integer, optional) — Rows to return, default 25, max 250

### `imdb_image_types`

- **HTTP:** `GET /imdb/image-types`
- **What:** IMDb image types. Lists every value the `type` parameter of the IMDb image endpoints accepts: `behind_the_scenes`, `event`, `poster`, `product`, `production_art`, `publicity`, `still_frame`, `unknown`. Each row carries a display label and a short description.
- **Params:** _none_

### `imdb_name`

- **HTTP:** `GET /imdb/name`
- **What:** IMDb name detail. Returns normalized public IMDb person metadata and known-for rows. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb name id; `url` (string, optional) — Absolute https://www.imdb.com/name/<id>/ URL

### `imdb_name_awards`

- **HTTP:** `GET /imdb/name/awards`
- **What:** IMDb name awards. Returns normalized public IMDb award rows for a person. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb name id; `url` (string, optional) — Absolute https://www.imdb.com/name/<id>/ URL

### `imdb_name_credits`

- **HTTP:** `GET /imdb/name/credits`
- **What:** IMDb name credits. Returns normalized public IMDb filmography sections for a person. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb name id; `url` (string, optional) — Absolute https://www.imdb.com/name/<id>/ URL

### `imdb_name_images`

- **HTTP:** `GET /imdb/name/images`
- **What:** IMDb name images. Returns image metadata from a person's media index, including the original image URL, dimensions, caption and credited people. Filter by image type with `type`, which accepts a single value or a comma-separated list of: `behind_the_scenes`, `event`, `poster`, `product`, `production_art`, `publicity`, `still_frame`, `unknown`. Omit `type` to return every type. Limit defaults to 50 and clamps to 1000. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb name id; `limit` (integer, optional) — Rows to return, default 50, max 1000; `type` (string, optional) — Image type filter, single value or comma-separated list; `url` (string, optional) — Absolute https://www.imdb.com/name/<id>/ URL

### `imdb_name_videos`

- **HTTP:** `GET /imdb/name/videos`
- **What:** IMDb name video metadata. Returns public person video metadata and thumbnail URLs only; playback URLs and media manifests are never returned. IMDb caps the upstream slice at 100 and provides no usable continuation cursor, so `total` can exceed returned rows and `has_more` reports that condition. Limit defaults to 50 and clamps to 100. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb name id; `limit` (integer, optional) — Rows to return, default 50, max 100; `url` (string, optional) — Absolute https://www.imdb.com/name/<id>/ URL

### `imdb_search`

- **HTTP:** `GET /imdb/search`
- **What:** IMDb title search. Returns normalized IMDb title search rows from credential-free public IMDb pages. Limit defaults to 10 and clamps to 20.
- **Params:** `limit` (integer, optional) — Rows to return, default 10, max 20; `query` (string, **required**) — Search query

### `imdb_search_title`

- **HTTP:** `GET /imdb/search/title`
- **What:** IMDb advanced title search. Returns normalized IMDb advanced title-search results (imdb.com/search/title/) from a credential-free public IMDb page. At least one filter is required; sort/limit alone are not enough. Limit defaults to 25 and clamps to 50; only IMDb's first rendered page of results is returned (see `total`/`has_more`), there is no deeper cursor pagination. Genre/company/certificate/country/language/keyword/characters/role are include-only lists; there is no exclude support. Unsupported: genre exclude, three curated `groups` values (best-picture-nominee, best-director-nominee, national-film-registry), and the non-plot "page topic" search fields.
- **Params:** `certificates` (string, optional) — Comma-separated `COUNTRY:RATING` certificate pairs, e.g. `US:PG-13`; `characters` (string, optional) — Comma-separated character names; `colors` (string, optional) — Comma-separated color info: `color`, `black_and_white`, `colorized`, `aces`; `companies` (string, optional) — Comma-separated IMDb company ids, format `co########`; `countries` (string, optional) — Comma-separated ISO country codes; `genres` (string, optional) — Comma-separated genres (include-only): `Action`, `Adventure`, `Animation`, `Biography`, `Comedy`, `Crime`, `Documentary`, `Drama`, `Family`, `Fantasy`, `Film-Noir`, `Game-Show`, `History`, `Horror`, `Music`, `Musical`, `Mystery`, `News`, `Reality-TV`, `Romance`, `Sci-Fi`, `Short`, `Sport`, `Talk-Show`, `Thriller`, `War`, `Western`; `groups` (string, optional) — Comma-separated awards/curated-list groups: `oscar_winner`, `oscar_nominee`, `emmy_winner`, `emmy_nominee`, `golden_globe_winner`, `golden_globe_nominee`, `best_picture_winner`, `best_director_winner`, `razzie_winner`, `razzie_nominee`, `top_100`, `top_250`, `top_1000`, `bottom_100`, `bottom_250`, `bottom_1000`; `include_adult` (boolean, optional) — Include adult titles. Defaults to excluded; `keywords` (string, optional) — Comma-separated plot keywords; `languages` (string, optional) — Comma-separated ISO language codes; `limit` (integer, optional) — Rows to return, default 25, max 50; `max_popularity` (integer, optional) — Maximum IMDb popularity rank; `max_runtime` (integer, optional) — Maximum runtime in minutes; `max_user_rating` (number, optional) — Maximum IMDb user rating, 0-10; `max_votes` (integer, optional) — Maximum number of user rating votes; `min_popularity` (integer, optional) — Minimum IMDb popularity rank (1 is most popular); `min_runtime` (integer, optional) — Minimum runtime in minutes; `min_user_rating` (number, optional) — Minimum IMDb user rating, 0-10; `min_votes` (integer, optional) — Minimum number of user rating votes; `plot` (string, optional) — Plot text search term; `release_date_from` (string, optional) — Release date lower bound: YYYY, YYYY-MM, or YYYY-MM-DD; `release_date_to` (string, optional) — Release date upper bound: YYYY, YYYY-MM, or YYYY-MM-DD; `role` (string, optional) — Comma-separated cast/crew IMDb name ids, format `nm########`; `sort` (string, optional) — One of `moviemeter`, `alpha`, `user_rating`, `num_votes`, `boxoffice_gross_us`, `runtime`, `year`, `release_date`; `sort_order` (string, optional) — `asc` or `desc`. Defaults to `asc` when sort is set; `sound_mixes` (string, optional) — Comma-separated sound mix names: `12-Track Digital Sound`, `3 Channel Stereo`, `4-Track Stereo`, `6-Track Stereo`, `70 mm 6-Track`, `AGA Sound System`, `Auro 11.1`, `CDS`, `Chronophone`, `Cinematophone`, `Cinephone`, `Cinerama 7-Track`, `Cinesound`, `D-Cinema 48kHz 5.1`, `Datasat`, `De Forest Phonofilm`, `Digitrac Digital Audio System`, `Dolby`, `Dolby Atmos`, `Dolby Digital`, `Dolby Digital EX`, `Dolby SR`, `Dolby Stereo`, `Dolby Surround 7.1`, `DTS`, `DTS 70 mm`, `DTS Stereo`, `DTS-ES`, `IMAX 6-Track`, `Kinoplasticon`, `LC-Concept Digital Sound`, `Matrix Surround`, `Mono`, `Perspecta Stereo`, `Phono-Kinema`, `SDDS`, `Sensurround`, `Silent`, `Sonics-DDP`, `Sonix`, `Stereo`, `Ultra Stereo`, `Vitaphone`; `title` (string, optional) — Title-name substring match; `title_type` (string, optional) — Comma-separated title types: `feature`, `tvSeries`, `short`, `tvEpisode`, `tvMiniSeries`, `tvMovie`, `tvSpecial`, `tvShort`, `videoGame`, `video`, `musicVideo`, `podcastSeries`, `podcastEpisode`

### `imdb_title`

- **HTTP:** `GET /imdb/title`
- **What:** IMDb title detail. Returns normalized IMDb title metadata from a credential-free public IMDb title page. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

### `imdb_title_awards`

- **HTTP:** `GET /imdb/title/awards`
- **What:** IMDb title awards. Returns normalized public IMDb award rows for a title. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

### `imdb_title_box_office`

- **HTTP:** `GET /imdb/title/box-office`
- **What:** IMDb title box office summary. Returns a title's public box-office summary: lifetime gross by market (domestic, international, worldwide), the domestic opening weekend, and the production budget. IMDb reports each figure independently, so a real title with no box office data (most TV series, many non-theatrical titles) returns `has_box_office: false` with every figure omitted rather than an error. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

### `imdb_title_company_credits`

- **HTTP:** `GET /imdb/title/company-credits`
- **What:** IMDb title company credits. Returns normalized public IMDb company-credit sections for a title. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

### `imdb_title_connections`

- **HTTP:** `GET /imdb/title/connections`
- **What:** IMDb title connections. Returns a bounded slice of a title's public connections: other titles it references or is referenced by, such as remakes, spin-offs, "featured in" clips, and "edited into" compilations. `category` is upstream-supplied free text, not a closed enum. IMDb's connections list can run to hundreds or thousands of rows, so `total` can exceed the returned rows and `has_more` reports that condition. Limit defaults to 50 and clamps to 250. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `limit` (integer, optional) — Rows to return, default 50, max 250; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

### `imdb_title_credits`

- **HTTP:** `GET /imdb/title/credits`
- **What:** IMDb title credits. Returns normalized public IMDb full cast and crew sections. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

### `imdb_title_episodes`

- **HTTP:** `GET /imdb/title/episodes`
- **What:** IMDb title episodes. Returns normalized public IMDb episode rows for a series title. Limit defaults to 10 and clamps to 20. Optional `season` filters the upstream episodes page. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `limit` (integer, optional) — Rows to return, default 10, max 20; `season` (integer, optional) — Season number to request; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

### `imdb_title_filming_locations`

- **HTTP:** `GET /imdb/title/filming-locations`
- **What:** IMDb title filming locations. Returns normalized public IMDb filming-location rows for a title. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

### `imdb_title_goofs`

- **HTTP:** `GET /imdb/title/goofs`
- **What:** IMDb title goofs. Returns normalized public IMDb goof rows for a title. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

### `imdb_title_images`

- **HTTP:** `GET /imdb/title/images`
- **What:** IMDb title images. Returns image metadata from a title's media index, including the original image URL, dimensions, caption and credited people. Filter by image type with `type`, which accepts a single value or a comma-separated list of: `behind_the_scenes`, `event`, `poster`, `product`, `production_art`, `publicity`, `still_frame`, `unknown`. Omit `type` to return every type. Limit defaults to 50 and clamps to 1000. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `limit` (integer, optional) — Rows to return, default 50, max 1000; `type` (string, optional) — Image type filter, single value or comma-separated list; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

### `imdb_title_keywords`

- **HTTP:** `GET /imdb/title/keywords`
- **What:** IMDb title keywords. Returns normalized public IMDb keyword rows for a title. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

### `imdb_title_parental_guide`

- **HTTP:** `GET /imdb/title/parental-guide`
- **What:** IMDb title parental guide. Returns normalized public IMDb parental-guide categories and severity signals. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

### `imdb_title_public_facts_analysis`

- **HTTP:** `GET /imdb/title/public-facts-analysis`
- **What:** IMDb title public facts analysis. Returns derived public-page summary metrics for IMDb trivia, goofs, quotes, keywords, filming locations, and company credits. This endpoint is not viewing advice. Pass exactly one of `id` or `url`. The six sections are gathered from six independent sources, so a section that cannot be fetched is omitted and named in `missing_sections` with `partial` set to `true`, rather than failing the whole response; an error is returned only when no section could be fetched. Callers that require a complete analysis should check `partial`.
- **Params:** `id` (string, optional) — IMDb title id; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

### `imdb_title_quotes`

- **HTTP:** `GET /imdb/title/quotes`
- **What:** IMDb title quotes. Returns normalized public IMDb quote rows for a title. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

### `imdb_title_ratings`

- **HTTP:** `GET /imdb/title/ratings`
- **What:** IMDb title ratings breakdown. Returns IMDb's aggregate rating, vote count, ten rating buckets, and country rating summaries. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `url` (string, optional) — Absolute IMDb title URL

### `imdb_title_release_info`

- **HTTP:** `GET /imdb/title/release-info`
- **What:** IMDb title release info. Returns normalized public IMDb release date rows and alternate titles. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

### `imdb_title_reviews`

- **HTTP:** `GET /imdb/title/reviews`
- **What:** IMDb title user reviews. Returns normalized public IMDb user review rows. Limit defaults to 10 and clamps to 20. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `limit` (integer, optional) — Rows to return, default 10, max 20; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

### `imdb_title_similar`

- **HTTP:** `GET /imdb/title/similar`
- **What:** IMDb similar titles. Returns normalized titles from IMDb's public More like this recommendations. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `url` (string, optional) — Absolute IMDb title URL

### `imdb_title_technical_specs`

- **HTTP:** `GET /imdb/title/technical-specs`
- **What:** IMDb title technical specs. Returns normalized public IMDb technical specifications such as runtime, sound mix, color, and aspect ratio. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

### `imdb_title_trivia`

- **HTTP:** `GET /imdb/title/trivia`
- **What:** IMDb title trivia. Returns normalized public IMDb trivia rows for a title. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

### `imdb_title_videos`

- **HTTP:** `GET /imdb/title/videos`
- **What:** IMDb title video metadata. Returns public title video metadata and thumbnail URLs only; playback URLs and media manifests are never returned. IMDb server-truncates this connection and exposes no usable continuation cursor, so `total` can exceed returned rows and `has_more` reports that condition. Limit defaults to 50 and clamps to 100. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `limit` (integer, optional) — Rows to return, default 50, max 100; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

## JustWatch (21)

### `justwatch_age_certifications`

- **HTTP:** `GET /justwatch/age-certifications`
- **What:** Get JustWatch age certifications. Returns JustWatch age certification technical names for a country.
- **Params:** `country` (string, optional) — Two-letter country code

### `justwatch_discover`

- **HTTP:** `GET /justwatch/discover`
- **What:** Discover JustWatch titles. Returns popular movies and shows filtered by optional genre short names, provider short names, production countries, monetization types, and release year bounds. Combine `providers` with `production_countries` to build charts such as most popular Korean or Japanese titles on a given service. Type accepts only `all`, `movie`, or `show`; monetization_types accepts only `FLATRATE`, `FREE`, `ADS`, `RENT`, or `BUY`.
- **Params:** `country` (string, optional) — Two-letter country code; `genres` (string, optional) — Comma-separated JustWatch genre short names; `language` (string, optional) — Two-letter language code; `limit` (integer, optional) — Maximum results, defaults to 20 and clamps to 50; `monetization_types` (string, optional) — Comma-separated monetization types: FLATRATE, FREE, ADS, RENT, BUY; `production_countries` (string, optional) — Comma-separated two-letter ISO production-country codes; `providers` (string, optional) — Comma-separated JustWatch provider short names; `type` (string, optional) — Title type: all, movie, show; `year_max` (integer, optional) — Maximum release year; `year_min` (integer, optional) — Minimum release year

### `justwatch_episode_by_id`

- **HTTP:** `GET /justwatch/episode/by-id`
- **What:** Get JustWatch episode by raw id. Looks up an episode by raw JustWatch GraphQL id such as `tse5550494` and returns normalized metadata and offers.
- **Params:** `country` (string, optional) — Two-letter country code; `id` (string, **required**) — Raw JustWatch episode id matching tse[0-9]+; `language` (string, optional) — Two-letter language code

### `justwatch_episode_offers`

- **HTTP:** `GET /justwatch/episode/offers`
- **What:** Get JustWatch episode offers. Returns normalized offers for a raw JustWatch episode id across one to five comma-separated country codes.
- **Params:** `countries` (string, optional) — One to five comma-separated two-letter country codes; `id` (string, **required**) — Raw JustWatch episode id matching tse[0-9]+; `language` (string, optional) — Two-letter language code

### `justwatch_genre_titles`

- **HTTP:** `GET /justwatch/genre/titles`
- **What:** Get JustWatch genre titles. Returns popular titles for one JustWatch genre short name such as `act`. Type accepts only `all`, `movie`, or `show`.
- **Params:** `country` (string, optional) — Two-letter country code; `genre` (string, **required**) — JustWatch genre short name; `language` (string, optional) — Two-letter language code; `limit` (integer, optional) — Maximum results, defaults to 20 and clamps to 50; `type` (string, optional) — Title type: all, movie, show

### `justwatch_genres`

- **HTTP:** `GET /justwatch/genres`
- **What:** Get JustWatch genres. Returns JustWatch genre short names and localized translations.
- **Params:** `language` (string, optional) — Two-letter language code

### `justwatch_monetization_titles`

- **HTTP:** `GET /justwatch/monetization/titles`
- **What:** Get JustWatch monetization titles. Returns popular titles for one monetization type. monetization_type accepts only `FLATRATE`, `FREE`, `ADS`, `RENT`, or `BUY`; type accepts only `all`, `movie`, or `show`.
- **Params:** `country` (string, optional) — Two-letter country code; `language` (string, optional) — Two-letter language code; `limit` (integer, optional) — Maximum results, defaults to 20 and clamps to 50; `monetization_type` (string, **required**) — Monetization type: FLATRATE, FREE, ADS, RENT, BUY; `type` (string, optional) — Title type: all, movie, show

### `justwatch_new`

- **HTTP:** `GET /justwatch/new`
- **What:** Get new JustWatch titles. Returns newly available movies and shows from the public JustWatch website GraphQL endpoint. Type accepts only `all`, `movie`, or `show`; limit defaults to 20 and clamps to 50.
- **Params:** `country` (string, optional) — Two-letter country code; `language` (string, optional) — Two-letter language code; `limit` (integer, optional) — Maximum results, defaults to 20 and clamps to 50; `type` (string, optional) — Title type: all, movie, show

### `justwatch_popular`

- **HTTP:** `GET /justwatch/popular`
- **What:** Get popular JustWatch titles. Returns popular movies and shows from the public JustWatch website GraphQL endpoint. Type accepts only `all`, `movie`, or `show`; limit defaults to 20 and clamps to 50.
- **Params:** `country` (string, optional) — Two-letter country code; `cursor` (string, optional) — Opaque next_cursor from the prior response; omit for the first page; `language` (string, optional) — Two-letter language code; `limit` (integer, optional) — Maximum results, defaults to 20 and clamps to 50; `type` (string, optional) — Title type: all, movie, show

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

### `justwatch_season_by_id`

- **HTTP:** `GET /justwatch/season/by-id`
- **What:** Get JustWatch season by raw id. Looks up a season by raw JustWatch GraphQL id such as `tss297253`.
- **Params:** `country` (string, optional) — Two-letter country code; `id` (string, **required**) — Raw JustWatch season id matching tss[0-9]+; `language` (string, optional) — Two-letter language code

### `justwatch_season_episodes`

- **HTTP:** `GET /justwatch/season/episodes`
- **What:** Get JustWatch season episodes. Returns episodes and normalized episode offers for a raw JustWatch season id such as `tss297253`.
- **Params:** `country` (string, optional) — Two-letter country code; `language` (string, optional) — Two-letter language code; `season_id` (string, **required**) — Raw JustWatch season id matching tss[0-9]+

### `justwatch_show_seasons`

- **HTTP:** `GET /justwatch/show/seasons`
- **What:** Get JustWatch show seasons. Returns seasons for a raw JustWatch show id such as `ts287292`.
- **Params:** `country` (string, optional) — Two-letter country code; `language` (string, optional) — Two-letter language code; `show_id` (string, **required**) — Raw JustWatch show id matching ts[0-9]+

### `justwatch_title`

- **HTTP:** `GET /justwatch/title`
- **What:** Get JustWatch title details. Fetches a JustWatch title page and returns normalized metadata and current offers. Pass exactly one of `path` or `url`.
- **Params:** `path` (string, optional) — JustWatch title path; `url` (string, optional) — Absolute https://www.justwatch.com title URL

### `justwatch_title_analysis`

- **HTTP:** `GET /justwatch/title/analysis`
- **What:** Analyze JustWatch title availability. Fetches a JustWatch title page and summarizes provider availability, monetization buckets, formats, price ranges, and best rent/buy/free/subscription options. Pass exactly one of `path` or `url`.
- **Params:** `path` (string, optional) — JustWatch title path; `url` (string, optional) — Absolute https://www.justwatch.com title URL

### `justwatch_title_by_id`

- **HTTP:** `GET /justwatch/title/by-id`
- **What:** Get JustWatch title by raw id. Looks up a movie or show by raw JustWatch GraphQL id such as `tm92641` or `ts287292`.
- **Params:** `country` (string, optional) — Two-letter country code; `id` (string, **required**) — Raw JustWatch movie/show id matching tm[0-9]+ or ts[0-9]+; `language` (string, optional) — Two-letter language code

### `justwatch_title_media`

- **HTTP:** `GET /justwatch/title/media`
- **What:** Get JustWatch title media. Returns normalized credits, clips, and backdrops for a raw JustWatch movie/show id such as `tm92641`.
- **Params:** `country` (string, optional) — Two-letter country code; `id` (string, **required**) — Raw JustWatch movie/show id matching tm[0-9]+ or ts[0-9]+; `language` (string, optional) — Two-letter language code

### `justwatch_title_offers`

- **HTTP:** `GET /justwatch/title/offers`
- **What:** Get JustWatch title offers. Returns normalized offers for a raw JustWatch movie/show id across one to five comma-separated country codes.
- **Params:** `countries` (string, optional) — One to five comma-separated two-letter country codes; `id` (string, **required**) — Raw JustWatch movie/show id matching tm[0-9]+ or ts[0-9]+; `language` (string, optional) — Two-letter language code

### `justwatch_title_similar`

- **HTTP:** `GET /justwatch/title/similar`
- **What:** Get similar JustWatch titles. Returns similar titles for a raw JustWatch movie/show id such as `tm92641`.
- **Params:** `country` (string, optional) — Two-letter country code; `id` (string, **required**) — Raw JustWatch movie/show id matching tm[0-9]+ or ts[0-9]+; `language` (string, optional) — Two-letter language code; `limit` (integer, optional) — Maximum results, defaults to 10 and clamps to 25

## TMDB (9)

### `tmdb_collection`

- **HTTP:** `GET /tmdb/collection/{id}`
- **What:** Get a TMDB collection. Returns a normalized TMDB collection (franchise grouping), including its overview and server-rendered member movies. Credential-free public TMDB data.
- **Params:** `id` (string, **required**) — TMDB collection id or id-slug

### `tmdb_genres`

- **HTTP:** `GET /tmdb/genres`
- **What:** List TMDB browse genres. Returns every genre ID advertised by TMDB's public movie and TV browse pages. Use movie values only with movie list filters and TV values only with TV list filters. Credential-free public TMDB data.
- **Params:** _none_

### `tmdb_movie`

- **HTTP:** `GET /tmdb/movie/{id}`
- **What:** Get a TMDB movie. Returns a normalized TMDB movie: overview, tagline, genres, countries, runtime, budget/revenue, top-billed cast, top crew (director/writer), and aggregate rating. Credential-free public TMDB data (themoviedb.org) — not the official api.themoviedb.org, which requires an API key.
- **Params:** `id` (string, **required**) — TMDB movie id

### `tmdb_movie_list`

- **HTTP:** `GET /tmdb/movie/list`
- **What:** Get a TMDB movie chart. Returns a TMDB movie chart (popular, top rated, now playing, or upcoming). Credential-free public TMDB data.
- **Params:** `category` (string, optional) — Movie chart, default popular; `date_from` (string, optional) — Release date lower bound (YYYY-MM-DD); `date_to` (string, optional) — Release date upper bound (YYYY-MM-DD); `include_adult` (boolean, optional) — Include adult titles; `limit` (integer, optional) — Max movies, default 10, max 20; `max_rating` (number, optional) — Maximum rating, 0-10; `max_runtime` (integer, optional) — Maximum runtime in minutes; `min_rating` (number, optional) — Minimum rating, 0-10; `min_runtime` (integer, optional) — Minimum runtime in minutes; `min_votes` (integer, optional) — Minimum vote count; `original_language` (string, optional) — Two-letter original-language code; `page` (integer, optional) — 1-based page, default 1; `sort_by` (string, optional) — Sort order; `with_genres` (string, optional) — Comma- or pipe-separated movie genre ids: 28,12,16,35,80,99,18,10751,14,36,27,10402,9648,10749,878,10770,53,10752,37

### `tmdb_person`

- **HTTP:** `GET /tmdb/person/{id}`
- **What:** Get a TMDB person. Returns a normalized TMDB person: biography, birth date, photo, and filmography (movie and TV credits). Credential-free public TMDB data.
- **Params:** `id` (string, **required**) — TMDB person id; `limit` (integer, optional) — Max filmography credits, default 10, max 20

### `tmdb_person_list`

- **HTTP:** `GET /tmdb/person/list`
- **What:** List popular people on TMDB. Returns one page from TMDB's Popular People directory, including each person's id, name, known-for titles, profile image, and detail URL. Credential-free public TMDB data.
- **Params:** `limit` (integer, optional) — Max people, default 10, max 20; `page` (integer, optional) — 1-based page, default 1

### `tmdb_search`

- **HTTP:** `GET /tmdb/search`
- **What:** Search TMDB. Searches TMDB movies, TV shows, people, and collections. An unscoped query interleaves results across all four types rather than returning whichever type happens to rank first upstream. Credential-free public TMDB data.
- **Params:** `limit` (integer, optional) — Max results, default 10, max 20; `page` (integer, optional) — 1-based results page, default 1; `query` (string, **required**) — Search query; `type` (string, optional) — Optional result type filter

### `tmdb_tv`

- **HTTP:** `GET /tmdb/tv/{id}`
- **What:** Get a TMDB TV show. Returns a normalized TMDB TV show: overview, tagline, genres, countries, episode count, first/last air year, top-billed cast, top crew (creator), and aggregate rating. Credential-free public TMDB data.
- **Params:** `id` (string, **required**) — TMDB TV show id

### `tmdb_tv_list`

- **HTTP:** `GET /tmdb/tv/list`
- **What:** Get a TMDB TV chart. Returns a TMDB TV chart (popular, top rated, airing today, or on the air). Credential-free public TMDB data.
- **Params:** `category` (string, optional) — TV chart, default popular; `date_from` (string, optional) — First-air date lower bound (YYYY-MM-DD); `date_to` (string, optional) — First-air date upper bound (YYYY-MM-DD); `include_adult` (boolean, optional) — Include adult titles; `limit` (integer, optional) — Max shows, default 10, max 20; `max_rating` (number, optional) — Maximum rating, 0-10; `max_runtime` (integer, optional) — Maximum runtime in minutes; `min_rating` (number, optional) — Minimum rating, 0-10; `min_runtime` (integer, optional) — Minimum runtime in minutes; `min_votes` (integer, optional) — Minimum vote count; `original_language` (string, optional) — Two-letter original-language code; `page` (integer, optional) — 1-based page, default 1; `sort_by` (string, optional) — Sort order; `with_genres` (string, optional) — Comma- or pipe-separated TV genre ids: 10759,16,35,80,99,18,10751,10762,9648,10763,10764,10765,10766,10767,10768,37

## Rotten Tomatoes (14)

### `rottentomatoes_browse_filters`

- **HTTP:** `GET /rottentomatoes/browse/filters`
- **What:** Rotten Tomatoes browse filter discovery. Returns every filter and accepted value exposed by the selected live Rotten Tomatoes browse page. Call this before building filtered movie or TV browse requests; values differ by list and update with the site's menus.
- **Params:** `list` (string, optional) — Browse list: movies_in_theaters, movies_at_home, movies_coming_soon, tv_series_browse

### `rottentomatoes_browse_movies`

- **HTTP:** `GET /rottentomatoes/browse/movies`
- **What:** Rotten Tomatoes movie discovery rows. Returns normalized movie rows from Rotten Tomatoes' public browse JSON route. Use `/rottentomatoes/browse/filters` to discover current values for each list. Filters accept comma-separated values; pagination uses the opaque `after` cursor from the previous response.
- **Params:** `affiliates` (string, optional) — Comma-separated streaming/service values from browse/filters; `after` (string, optional) — Opaque next-page cursor returned in data.page_info.end_cursor; `audience` (string, optional) — Comma-separated Popcornmeter values from browse/filters; `critics` (string, optional) — Comma-separated Tomatometer values from browse/filters; `genres` (string, optional) — Comma-separated genre values from browse/filters; `limit` (integer, optional) — Rows to return, default 10, max 30; `list` (string, optional) — Movie browse list: movies_in_theaters, movies_at_home, movies_coming_soon; `ratings` (string, optional) — Comma-separated content ratings from browse/filters; `sort` (string, optional) — Sort value from the selected list's browse/filters response

### `rottentomatoes_browse_tv`

- **HTTP:** `GET /rottentomatoes/browse/tv`
- **What:** Rotten Tomatoes TV discovery rows. Returns normalized TV series rows from Rotten Tomatoes' public browse JSON route. Use `/rottentomatoes/browse/filters?list=tv_series_browse` to discover current filters; pagination uses the opaque `after` cursor from the previous response.
- **Params:** `affiliates` (string, optional) — Comma-separated streaming/service values from browse/filters; `after` (string, optional) — Opaque next-page cursor returned in data.page_info.end_cursor; `audience` (string, optional) — Comma-separated Popcornmeter values from browse/filters; `critics` (string, optional) — Comma-separated Tomatometer values from browse/filters; `genres` (string, optional) — Comma-separated genre values from browse/filters; `limit` (integer, optional) — Rows to return, default 10, max 30; `list` (string, optional) — TV browse list: tv_series_browse; `ratings` (string, optional) — Comma-separated content ratings from browse/filters; `sort` (string, optional) — Sort value from browse/filters

### `rottentomatoes_critics_authors`

- **HTTP:** `GET /rottentomatoes/critics/authors`
- **What:** Rotten Tomatoes critic directory. Returns current or inactive critics from Rotten Tomatoes' public author directory. Browse one letter or search by name; use `next_cursor` as `after` or `previous_cursor` as `before`, as indicated by the corresponding page flag. The letter values come from the live directory controls.
- **Params:** `after` (string, optional) — Opaque cursor from data.next_cursor; `before` (string, optional) — Opaque cursor from data.previous_cursor; cannot be combined with after; `inactive` (boolean, optional) — Include the site's inactive critics list; `letter` (string, optional) — Directory letter. Omit when using search; default a.; `limit` (integer, optional) — Rows per page, default 100, range 1 to 100; `search` (string, optional) — Search critics by name; cannot be combined with letter

### `rottentomatoes_editorial_search`

- **HTTP:** `GET /rottentomatoes/editorial/search`
- **What:** Rotten Tomatoes editorial search. Searches public Rotten Tomatoes editorial content, including articles and guides. Results come from its anonymous WordPress REST search endpoint and include content subtype plus total-page metadata.
- **Params:** `limit` (integer, optional) — Rows per page, default 10, range 1 to 100; `page` (integer, optional) — One-based result page from 1 to 10000; default 1; `query` (string, **required**) — Editorial search text; maximum 200 bytes

### `rottentomatoes_episode`

- **HTTP:** `GET /rottentomatoes/episode`
- **What:** Rotten Tomatoes episode detail. Returns normalized Rotten Tomatoes TV episode metadata, scorecard data, parent series/season metadata, and public video metadata from a credential-free public episode page. Pass exactly one of `path` or `url`.
- **Params:** `path` (string, optional) — Rotten Tomatoes episode path; `url` (string, optional) — Absolute https://www.rottentomatoes.com episode URL

### `rottentomatoes_movie`

- **HTTP:** `GET /rottentomatoes/movie`
- **What:** Rotten Tomatoes movie detail. Returns normalized Rotten Tomatoes movie metadata, scorecard data, and representative embedded audience reviews. Pass exactly one of `path` or `url`.
- **Params:** `path` (string, optional) — Rotten Tomatoes movie path; `url` (string, optional) — Absolute https://www.rottentomatoes.com movie URL

### `rottentomatoes_movie_reviews`

- **HTTP:** `GET /rottentomatoes/movie/reviews`
- **What:** Rotten Tomatoes movie reviews. Returns normalized critic or audience reviews from Rotten Tomatoes public review JSON hydrated by the movie review page, including pagination metadata. Pass exactly one of `path` or `url`. Supported `type` values are `critics`, `top-critics`, `audience`, and `verified-audience`.
- **Params:** `after` (string, optional) — Pagination cursor from data.page_info.end_cursor; `limit` (integer, optional) — Reviews to return, default 10, max 20; `path` (string, optional) — Rotten Tomatoes movie path; `type` (string, optional) — Review type: critics, top-critics, audience, verified-audience; `url` (string, optional) — Absolute https://www.rottentomatoes.com movie URL

### `rottentomatoes_person`

- **HTTP:** `GET /rottentomatoes/person`
- **What:** Rotten Tomatoes person detail and filmography. Returns normalized Rotten Tomatoes celebrity/person metadata and filmography rows from public Person JSON-LD and the credential-free filmography module. Pass exactly one of `path` or `url`.
- **Params:** `path` (string, optional) — Rotten Tomatoes person path; `url` (string, optional) — Absolute https://www.rottentomatoes.com person URL

### `rottentomatoes_search`

- **HTTP:** `GET /rottentomatoes/search`
- **What:** Rotten Tomatoes movie search. Returns normalized Rotten Tomatoes movie search rows from credential-free server-rendered search HTML.
- **Params:** `limit` (integer, optional) — Rows to return, default 10, max 20; `query` (string, **required**) — Search query

### `rottentomatoes_season`

- **HTTP:** `GET /rottentomatoes/season`
- **What:** Rotten Tomatoes season detail. Returns normalized Rotten Tomatoes TV season metadata, scorecard data, parent series metadata, and episode rows from a credential-free public season page. Pass exactly one of `path` or `url`.
- **Params:** `path` (string, optional) — Rotten Tomatoes season path; `url` (string, optional) — Absolute https://www.rottentomatoes.com season URL

### `rottentomatoes_series`

- **HTTP:** `GET /rottentomatoes/series`
- **What:** Rotten Tomatoes series detail. Returns normalized Rotten Tomatoes TV series metadata and scorecard data from a credential-free public series page. Pass exactly one of `path` or `url`.
- **Params:** `path` (string, optional) — Rotten Tomatoes series path; `url` (string, optional) — Absolute https://www.rottentomatoes.com series URL

### `rottentomatoes_sitemap_urls`

- **HTTP:** `GET /rottentomatoes/sitemap/urls`
- **What:** Rotten Tomatoes sitemap URL page. Returns a page of URLs from one child sitemap. Discover valid `name` values with `rottentomatoes-sitemaps`; use offset/limit to page through the complete sitemap.
- **Params:** `limit` (integer, optional) — URLs to return, default 100, max 500; `name` (string, **required**) — Sitemap name returned by /rottentomatoes/sitemaps; `offset` (integer, optional) — Zero-based offset, default 0

### `rottentomatoes_sitemaps`

- **HTTP:** `GET /rottentomatoes/sitemaps`
- **What:** Rotten Tomatoes sitemap discovery. Returns the live sitemap index and every named child sitemap, including movie, TV series, season, episode, person, critic, publication, browse-list, and static route inventories.
- **Params:** _none_

## Metacritic (10)

### `metacritic_browse`

- **HTTP:** `GET /metacritic/browse`
- **What:** Browse Metacritic titles. Browse Metacritic titles by content type, optionally filtered by genre and ordered by Metascore, popularity, or release date. Returns paginated title cards with Metascore and user score. Credential-free public Metacritic data.
- **Params:** `genre` (string, optional) — Genre filter (e.g. Action); `page` (integer, optional) — 1-based page number (default 1); `per_page` (integer, optional) — Results per page (default 24, max 100); `sort` (string, optional) — Sort order; `type` (string, **required**) — Content type

### `metacritic_game`

- **HTTP:** `GET /metacritic/game/{slug}`
- **What:** Get a Metacritic game. Returns a normalized Metacritic game: Metascore (critic) and user score with sentiment and review counts, genres, per-platform scores, developer/publisher, rating, release date, and trailer. Credential-free public Metacritic data.
- **Params:** `slug` (string, **required**) — Metacritic game slug

### `metacritic_game_critic_reviews`

- **HTTP:** `GET /metacritic/game/{slug}/critic-reviews`
- **What:** List a Metacritic game's critic reviews. Returns paginated professional/publication reviews for a game: publication, score, quote, author, platform, and source URL. Credential-free public Metacritic data.
- **Params:** `page` (integer, optional) — 1-based page number (default 1); `per_page` (integer, optional) — Results per page (default 20, max 50); `slug` (string, **required**) — Metacritic game slug; `sort` (string, optional) — Sort order

### `metacritic_game_user_reviews`

- **HTTP:** `GET /metacritic/game/{slug}/user-reviews`
- **What:** List a Metacritic game's user reviews. Returns paginated user reviews for a game: author, score (0-10), quote, date, platform, helpfulness, and spoiler flag. Credential-free public Metacritic data.
- **Params:** `page` (integer, optional) — 1-based page number (default 1); `per_page` (integer, optional) — Results per page (default 20, max 50); `slug` (string, **required**) — Metacritic game slug; `sort` (string, optional) — Sort order

### `metacritic_movie`

- **HTTP:** `GET /metacritic/movie/{slug}`
- **What:** Get a Metacritic movie. Returns a normalized Metacritic movie: Metascore (critic) and user score with sentiment and review counts, genres, cast/crew, rating, runtime, release date, IMDb id, and trailer. Credential-free public Metacritic data.
- **Params:** `slug` (string, **required**) — Metacritic movie slug

### `metacritic_movie_critic_reviews`

- **HTTP:** `GET /metacritic/movie/{slug}/critic-reviews`
- **What:** List a Metacritic movie's critic reviews. Returns paginated professional/publication reviews for a movie: publication, score, quote, author, and source URL. Credential-free public Metacritic data.
- **Params:** `page` (integer, optional) — 1-based page number (default 1); `per_page` (integer, optional) — Results per page (default 20, max 50); `slug` (string, **required**) — Metacritic movie slug; `sort` (string, optional) — Sort order

### `metacritic_movie_user_reviews`

- **HTTP:** `GET /metacritic/movie/{slug}/user-reviews`
- **What:** List a Metacritic movie's user reviews. Returns paginated user reviews for a movie: author, score (0-10), quote, date, helpfulness, and spoiler flag. Credential-free public Metacritic data.
- **Params:** `page` (integer, optional) — 1-based page number (default 1); `per_page` (integer, optional) — Results per page (default 20, max 50); `slug` (string, **required**) — Metacritic movie slug; `sort` (string, optional) — Sort order

### `metacritic_tv`

- **HTTP:** `GET /metacritic/tv/{slug}`
- **What:** Get a Metacritic TV show. Returns a normalized Metacritic TV show: Metascore (critic) and user score with sentiment and review counts, genres, networks, season count, rating, release date, IMDb id, and trailer. Credential-free public Metacritic data.
- **Params:** `slug` (string, **required**) — Metacritic TV show slug

### `metacritic_tv_critic_reviews`

- **HTTP:** `GET /metacritic/tv/{slug}/critic-reviews`
- **What:** List a Metacritic TV show's critic reviews. Returns paginated professional/publication reviews for a TV show: publication, score, quote, author, and source URL. Credential-free public Metacritic data.
- **Params:** `page` (integer, optional) — 1-based page number (default 1); `per_page` (integer, optional) — Results per page (default 20, max 50); `slug` (string, **required**) — Metacritic TV show slug; `sort` (string, optional) — Sort order

### `metacritic_tv_user_reviews`

- **HTTP:** `GET /metacritic/tv/{slug}/user-reviews`
- **What:** List a Metacritic TV show's user reviews. Returns paginated user reviews for a TV show: author, score (0-10), quote, date, helpfulness, and spoiler flag. Credential-free public Metacritic data.
- **Params:** `page` (integer, optional) — 1-based page number (default 1); `per_page` (integer, optional) — Results per page (default 20, max 50); `slug` (string, **required**) — Metacritic TV show slug; `sort` (string, optional) — Sort order
