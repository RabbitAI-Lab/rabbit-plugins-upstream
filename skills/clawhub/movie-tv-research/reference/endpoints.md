# movie-tv-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**96 endpoints across 7 platform group(s).**

## IMDb (20)

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

### `imdb_title_company_credits`

- **HTTP:** `GET /imdb/title/company-credits`
- **What:** IMDb title company credits. Returns normalized public IMDb company-credit sections for a title. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

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

### `imdb_title_release_info`

- **HTTP:** `GET /imdb/title/release-info`
- **What:** IMDb title release info. Returns normalized public IMDb release date rows and alternate titles. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

### `imdb_title_reviews`

- **HTTP:** `GET /imdb/title/reviews`
- **What:** IMDb title user reviews. Returns normalized public IMDb user review rows. Limit defaults to 10 and clamps to 20. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `limit` (integer, optional) — Rows to return, default 10, max 20; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

### `imdb_title_technical_specs`

- **HTTP:** `GET /imdb/title/technical-specs`
- **What:** IMDb title technical specs. Returns normalized public IMDb technical specifications such as runtime, sound mix, color, and aspect ratio. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

### `imdb_title_trivia`

- **HTTP:** `GET /imdb/title/trivia`
- **What:** IMDb title trivia. Returns normalized public IMDb trivia rows for a title. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

## TMDB (7)

### `tmdb_movie`

- **HTTP:** `GET /tmdb/movie/{id}`
- **What:** Get a TMDB movie. Returns a normalized TMDB movie: overview, tagline, genres, countries, runtime, budget/revenue, top-billed cast, top crew (director/writer), and aggregate rating. Credential-free public TMDB data (themoviedb.org) — not the official api.themoviedb.org, which requires an API key.
- **Params:** `id` (string, **required**) — TMDB movie id

### `tmdb_movie_list`

- **HTTP:** `GET /tmdb/movie/list`
- **What:** Get a TMDB movie chart. Returns a TMDB movie chart (popular, top rated, now playing, or upcoming). Credential-free public TMDB data.
- **Params:** `category` (string, optional) — Movie chart, default popular; `date_from` (string, optional) — Release date lower bound (YYYY-MM-DD); `date_to` (string, optional) — Release date upper bound (YYYY-MM-DD); `include_adult` (boolean, optional) — Include adult titles; `limit` (integer, optional) — Max movies, default 10, max 20; `max_rating` (number, optional) — Maximum rating, 0-10; `max_runtime` (integer, optional) — Maximum runtime in minutes; `min_rating` (number, optional) — Minimum rating, 0-10; `min_runtime` (integer, optional) — Minimum runtime in minutes; `min_votes` (integer, optional) — Minimum vote count; `original_language` (string, optional) — Two-letter original-language code; `page` (integer, optional) — 1-based page, default 1; `sort_by` (string, optional) — Sort order; `with_genres` (string, optional) — Comma- or pipe-separated TMDB genre ids

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
- **What:** Search TMDB. Searches TMDB movies, TV shows, and people. An unscoped query interleaves results across all three types rather than returning whichever type happens to rank first upstream. Credential-free public TMDB data.
- **Params:** `limit` (integer, optional) — Max results, default 10, max 20; `page` (integer, optional) — 1-based results page, default 1; `query` (string, **required**) — Search query; `type` (string, optional) — Optional result type filter

### `tmdb_tv`

- **HTTP:** `GET /tmdb/tv/{id}`
- **What:** Get a TMDB TV show. Returns a normalized TMDB TV show: overview, tagline, genres, countries, episode count, first/last air year, top-billed cast, top crew (creator), and aggregate rating. Credential-free public TMDB data.
- **Params:** `id` (string, **required**) — TMDB TV show id

### `tmdb_tv_list`

- **HTTP:** `GET /tmdb/tv/list`
- **What:** Get a TMDB TV chart. Returns a TMDB TV chart (popular, top rated, airing today, or on the air). Credential-free public TMDB data.
- **Params:** `category` (string, optional) — TV chart, default popular; `date_from` (string, optional) — First-air date lower bound (YYYY-MM-DD); `date_to` (string, optional) — First-air date upper bound (YYYY-MM-DD); `include_adult` (boolean, optional) — Include adult titles; `limit` (integer, optional) — Max shows, default 10, max 20; `max_rating` (number, optional) — Maximum rating, 0-10; `max_runtime` (integer, optional) — Maximum runtime in minutes; `min_rating` (number, optional) — Minimum rating, 0-10; `min_runtime` (integer, optional) — Minimum runtime in minutes; `min_votes` (integer, optional) — Minimum vote count; `original_language` (string, optional) — Two-letter original-language code; `page` (integer, optional) — 1-based page, default 1; `sort_by` (string, optional) — Sort order; `with_genres` (string, optional) — Comma- or pipe-separated TMDB genre ids

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
- **Params:** `country` (string, optional) — Two-letter country code; `language` (string, optional) — Two-letter language code; `limit` (integer, optional) — Maximum results, defaults to 20 and clamps to 50; `type` (string, optional) — Title type: all, movie, show

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

## Letterboxd (8)

### `letterboxd_film`

- **HTTP:** `GET /letterboxd/film/{slug}`
- **What:** Get a Letterboxd film. Returns a normalized Letterboxd film: synopsis, director, cast, genres, countries, languages, runtime, and aggregate member rating. Credential-free public Letterboxd data (letterboxd.com), parsed from the film page's schema.org structured data.
- **Params:** `slug` (string, **required**) — Letterboxd film slug

### `letterboxd_film_rating_histogram`

- **HTTP:** `GET /letterboxd/film/{slug}/rating-histogram`
- **What:** Get a Letterboxd film's rating distribution. Returns a film's full star-rating distribution (0.5 to 5.0 in half-star buckets) with counts and percentages. Credential-free public Letterboxd data.
- **Params:** `slug` (string, **required**) — Letterboxd film slug

### `letterboxd_film_reviews`

- **HTTP:** `GET /letterboxd/film/{slug}/reviews`
- **What:** Get a Letterboxd film's popular reviews. Returns a film's popular reviews (reviewer, rating, date, text, like/comment counts, spoiler flag). Credential-free public Letterboxd data.
- **Params:** `limit` (integer, optional) — Max reviews, default 10, max 50; `slug` (string, **required**) — Letterboxd film slug

### `letterboxd_film_similar`

- **HTTP:** `GET /letterboxd/film/{slug}/similar`
- **What:** Get films similar to a Letterboxd film. Returns films Letterboxd recommends as similar to the given film. Credential-free public Letterboxd data.
- **Params:** `limit` (integer, optional) — Max films, default 10, max 50; `slug` (string, **required**) — Letterboxd film slug

### `letterboxd_member`

- **HTTP:** `GET /letterboxd/member/{username}`
- **What:** Get a Letterboxd member's public profile stats. Returns a member's public profile stats (films watched, lists, following/followers). No private data — everything is visible to a logged-out visitor. Credential-free public Letterboxd data.
- **Params:** `username` (string, **required**) — Letterboxd username

### `letterboxd_person`

- **HTTP:** `GET /letterboxd/person/{slug}`
- **What:** Get a Letterboxd person's filmography. Returns a person's Letterboxd filmography for a credit role. Credential-free public Letterboxd data.
- **Params:** `limit` (integer, optional) — Max films, default 10, max 50; `role` (string, optional) — Credit role, default actor; `slug` (string, **required**) — Letterboxd person slug

### `letterboxd_popular`

- **HTTP:** `GET /letterboxd/popular`
- **What:** Get a Letterboxd popularity-ranked film chart. Returns a popularity-ranked film chart, optionally scoped to a time window, genre, and/or decade. Credential-free public Letterboxd data.
- **Params:** `decade` (string, optional) — Decade filter, e.g. 2010s; `genre` (string, optional) — Genre slug filter; `limit` (integer, optional) — Max films, default 10, max 50; `period` (string, optional) — Popularity window, omit for all-time

### `letterboxd_search`

- **HTTP:** `GET /letterboxd/search`
- **What:** Search Letterboxd. Searches Letterboxd films, people, lists, and tags. Credential-free public Letterboxd data.
- **Params:** `limit` (integer, optional) — Max results, default 10, max 50; `q` (string, **required**) — Search query; `type` (string, optional) — Optional result type filter

## Rotten Tomatoes (9)

### `rottentomatoes_browse_movies`

- **HTTP:** `GET /rottentomatoes/browse/movies`
- **What:** Rotten Tomatoes movie discovery rows. Returns normalized movie rows from Rotten Tomatoes public browse pages using credential-free JSON-LD ItemList data. Supported `list` values are `movies_in_theaters`, `movies_at_home`, and `movies_coming_soon`. Supported `sort` values are `popular`, `newest`, and `top_box_office`; `top_box_office` is only valid with `movies_in_theaters`.
- **Params:** `limit` (integer, optional) — Rows to return, default 10, max 20; `list` (string, optional) — Movie browse list: movies_in_theaters, movies_at_home, movies_coming_soon; `sort` (string, optional) — Sort: popular, newest, top_box_office

### `rottentomatoes_browse_tv`

- **HTTP:** `GET /rottentomatoes/browse/tv`
- **What:** Rotten Tomatoes TV discovery rows. Returns normalized TV series rows from Rotten Tomatoes public browse pages using credential-free JSON-LD ItemList data. Supported `list` value is `tv_series_browse`. Supported `sort` values are `popular` and `newest`.
- **Params:** `limit` (integer, optional) — Rows to return, default 10, max 20; `list` (string, optional) — TV browse list: tv_series_browse; `sort` (string, optional) — Sort: popular, newest

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

## Box Office Mojo (21)

### `boxofficemojo_brand`

- **HTTP:** `GET /boxofficemojo/brand`
- **What:** Box Office Mojo brand detail. Returns normalized release rows from a public Box Office Mojo brand page. Pass exactly one of `id`, `path`, or `url`.
- **Params:** `id` (string, optional) — Box Office Mojo brand id; `offset` (integer, optional) — Row offset for pagination (page size 100); `path` (string, optional) — Box Office Mojo brand path; `sort` (string, optional) — Sort field; `sortDir` (string, optional) — Sort direction; `url` (string, optional) — Absolute https://www.boxofficemojo.com brand URL

### `boxofficemojo_brands`

- **HTTP:** `GET /boxofficemojo/brands`
- **What:** Box Office Mojo brand chart. Returns normalized rows from Box Office Mojo's public brand chart.
- **Params:** `sort` (string, optional) — Sort field; `sortDir` (string, optional) — Sort direction

### `boxofficemojo_calendar`

- **HTTP:** `GET /boxofficemojo/calendar`
- **What:** Box Office Mojo domestic release schedule. Returns normalized grouped rows from Box Office Mojo's public domestic release schedule. Provide `year` and `month`.
- **Params:** `month` (integer, **required**) — Calendar month, 1 through 12; `year` (integer, **required**) — Calendar year, from 1921 through 2100

### `boxofficemojo_calendar_changes`

- **HTTP:** `GET /boxofficemojo/calendar/changes`
- **What:** Box Office Mojo domestic release schedule changes. Returns normalized grouped rows from Box Office Mojo's public domestic release-schedule changes page.
- **Params:** `offset` (integer, optional) — Changes page offset. Allowed values: 0, 30, 60, ... 780

### `boxofficemojo_calendar_date`

- **HTTP:** `GET /boxofficemojo/calendar/date`
- **What:** Box Office Mojo domestic release schedule date. Returns normalized release rows for one public Box Office Mojo domestic release-schedule date.
- **Params:** `date` (string, **required**) — Calendar date in YYYY-MM-DD format

### `boxofficemojo_date_domestic`

- **HTTP:** `GET /boxofficemojo/date/domestic`
- **What:** Box Office Mojo domestic daily box office. Returns normalized rows from Box Office Mojo's public domestic daily chart. Empty upstream daily pages return a typed not-found error rather than an empty success.
- **Params:** `date` (string, **required**) — Domestic box office date in YYYY-MM-DD format

### `boxofficemojo_franchise`

- **HTTP:** `GET /boxofficemojo/franchise`
- **What:** Box Office Mojo franchise detail. Returns normalized release rows from a public Box Office Mojo franchise page. Pass exactly one of `id`, `path`, or `url`.
- **Params:** `id` (string, optional) — Box Office Mojo franchise id; `offset` (integer, optional) — Row offset for pagination (page size 100); `path` (string, optional) — Box Office Mojo franchise path; `sort` (string, optional) — Sort field; `sortDir` (string, optional) — Sort direction; `url` (string, optional) — Absolute https://www.boxofficemojo.com franchise URL

### `boxofficemojo_franchises`

- **HTTP:** `GET /boxofficemojo/franchises`
- **What:** Box Office Mojo franchise chart. Returns normalized rows from Box Office Mojo's public franchise chart.
- **Params:** `sort` (string, optional) — Sort field; `sortDir` (string, optional) — Sort direction

### `boxofficemojo_genre`

- **HTTP:** `GET /boxofficemojo/genre`
- **What:** Box Office Mojo genre detail. Returns normalized release rows from a public Box Office Mojo genre page. Pass exactly one of `id`, `path`, or `url`.
- **Params:** `id` (string, optional) — Box Office Mojo genre id; `offset` (integer, optional) — Row offset for pagination (page size 100); `path` (string, optional) — Box Office Mojo genre path; `sort` (string, optional) — Sort field; `sortDir` (string, optional) — Sort direction; `url` (string, optional) — Absolute https://www.boxofficemojo.com genre URL

### `boxofficemojo_genres`

- **HTTP:** `GET /boxofficemojo/genres`
- **What:** Box Office Mojo genre chart. Returns normalized rows from Box Office Mojo's public genre chart.
- **Params:** `sort` (string, optional) — Sort field; `sortDir` (string, optional) — Sort direction

### `boxofficemojo_lifetime_grosses`

- **HTTP:** `GET /boxofficemojo/lifetime-grosses`
- **What:** Box Office Mojo lifetime gross chart. Returns normalized rows from Box Office Mojo's credential-free lifetime gross chart. `area` values: `worldwide`, `domestic`.
- **Params:** `area` (string, optional) — Chart area. Allowed values: worldwide, domestic; `offset` (integer, optional) — Chart page offset. Allowed values: 0, 200, 400, 600, 800

### `boxofficemojo_release`

- **HTTP:** `GET /boxofficemojo/release`
- **What:** Box Office Mojo release detail. Returns normalized Box Office Mojo release summary fields and domestic daily rows from a public release page. Pass exactly one of `id`, `path`, or `url`.
- **Params:** `id` (string, optional) — Box Office Mojo release id; `path` (string, optional) — Box Office Mojo release path; `url` (string, optional) — Absolute https://www.boxofficemojo.com release URL

### `boxofficemojo_release_group`

- **HTTP:** `GET /boxofficemojo/release-group`
- **What:** Box Office Mojo release group detail. Returns normalized market release rows grouped by region from a public Box Office Mojo release-group page. Pass exactly one of `id`, `path`, or `url`.
- **Params:** `id` (string, optional) — Box Office Mojo release-group id; `path` (string, optional) — Box Office Mojo release-group path; `url` (string, optional) — Absolute https://www.boxofficemojo.com release-group URL

### `boxofficemojo_showdown`

- **HTTP:** `GET /boxofficemojo/showdown`
- **What:** Box Office Mojo showdown detail. Returns normalized release comparison metrics from a public Box Office Mojo showdown page. Pass exactly one of `id`, `path`, or `url`.
- **Params:** `id` (string, optional) — Box Office Mojo showdown id; `path` (string, optional) — Box Office Mojo showdown path; `url` (string, optional) — Absolute https://www.boxofficemojo.com showdown URL

### `boxofficemojo_showdowns`

- **HTTP:** `GET /boxofficemojo/showdowns`
- **What:** Box Office Mojo showdowns. Returns normalized comparison rows from Box Office Mojo's public showdowns page.
- **Params:** _none_

### `boxofficemojo_title`

- **HTTP:** `GET /boxofficemojo/title`
- **What:** Box Office Mojo title detail. Returns normalized Box Office Mojo title release-group and market-gross tables from a public title page. Pass exactly one of `id`, `path`, or `url`.
- **Params:** `id` (string, optional) — Box Office Mojo title id; `path` (string, optional) — Box Office Mojo title path; `url` (string, optional) — Absolute https://www.boxofficemojo.com title URL

### `boxofficemojo_weekend_domestic`

- **HTTP:** `GET /boxofficemojo/weekend/domestic`
- **What:** Box Office Mojo domestic weekend box office. Returns normalized rows from Box Office Mojo's public domestic weekend chart. Empty upstream weekend pages return a typed not-found error rather than an empty success.
- **Params:** `week` (integer, **required**) — Weekend number, 1 through 53; `year` (integer, **required**) — Domestic weekend year, from 1982 through 2100

### `boxofficemojo_weekend_domestic_by_distributor`

- **HTTP:** `GET /boxofficemojo/weekend/domestic/by-distributor`
- **What:** Box Office Mojo domestic weekend by distributor. Returns normalized distributor rows from Box Office Mojo's public domestic weekend by-distributor chart. Empty upstream weekend pages return a typed not-found error rather than an empty success.
- **Params:** `week` (integer, **required**) — Weekend number, 1 through 53; `year` (integer, **required**) — Domestic weekend year, from 1982 through 2100

### `boxofficemojo_weekend_domestic_estimates`

- **HTTP:** `GET /boxofficemojo/weekend/domestic/estimates`
- **What:** Box Office Mojo domestic weekend estimates. Returns normalized estimate-vs-actual rows from Box Office Mojo's public domestic weekend estimates chart. Empty upstream weekend pages return a typed not-found error rather than an empty success.
- **Params:** `week` (integer, **required**) — Weekend number, 1 through 53; `year` (integer, **required**) — Domestic weekend year, from 1982 through 2100

### `boxofficemojo_year_domestic`

- **HTTP:** `GET /boxofficemojo/year/domestic`
- **What:** Box Office Mojo domestic yearly box office. Returns normalized release rows from Box Office Mojo's public domestic yearly calendar-grosses chart.
- **Params:** `year` (integer, **required**) — Domestic box office year, from 1977 through 2100

### `boxofficemojo_year_worldwide`

- **HTTP:** `GET /boxofficemojo/year/worldwide`
- **What:** Box Office Mojo worldwide yearly box office. Returns normalized release-group rows from Box Office Mojo's public worldwide yearly chart.
- **Params:** `year` (integer, **required**) — Box office year, from 1977 through 2100
