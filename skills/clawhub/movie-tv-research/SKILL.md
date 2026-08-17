---
name: movie-tv-research
description: Researches movies and TV shows — metadata, cast/crew, ratings, reviews, streaming availability, and box-office performance — via the Crawlora API across IMDb, TMDB, JustWatch, Letterboxd, Rotten Tomatoes, Metacritic, and Box Office Mojo, returning clean JSON. Use when the user asks about a title's cast, ratings/scores, where to stream it, critic or user reviews, or its box-office numbers.
---

# Movie & TV research

Pull title metadata, cast/crew, ratings, streaming availability, reviews, and
box-office numbers across seven film/TV data sources as normalized JSON from
the Crawlora API — no scraping IMDb pages or parsing streaming-provider HTML.

## When to use this skill

- "Who's in / who directed <title>?" / cast, crew, and credits lookups.
- "What's <title> rated on IMDb / Rotten Tomatoes / Metacritic / Letterboxd?"
- "Where can I stream <title>?" (JustWatch offers by provider).
- "How did <title> do at the box office?" (Box Office Mojo).
- "Find titles similar to <title>" or "what's popular right now."
- Critic vs. audience review comparisons; franchise/genre box-office analysis.

## Setup (one-time)

- Get a free Crawlora API key (2,000 credits/mo, no card) at [https://crawlora.net](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills).
- `export CRAWLORA_API_KEY=sk_your_key_here`
- All requests: `x-api-key: $CRAWLORA_API_KEY` against
  `https://api.crawlora.net/api/v1`. Missing/invalid key → `401`.

## How it works

Pick the source by job:

1. **Identity & credits (IMDb / TMDB)** — search first: `/imdb/search` or
   `/tmdb/search`; then detail: `/imdb/title` (needs the IMDb id) or
   `/tmdb/movie/{id}` / `/tmdb/tv/{id}`. Cast/crew: `/imdb/title/credits` or
   TMDB's title payload. Person pages: `/imdb/name`, `/tmdb/person/{id}`.
2. **Scores & reviews** — Rotten Tomatoes (`/rottentomatoes/movie`, `/series`,
   `/movie/reviews`), Metacritic (`/metacritic/movie/{slug}`,
   `/critic-reviews`, `/user-reviews`), IMDb (`/imdb/title/reviews`),
   Letterboxd (`/letterboxd/film/{slug}`, `/reviews`, `/rating-histogram`).
3. **Where to watch (JustWatch)** — `/justwatch/search` → raw id, then
   `/justwatch/title/offers` (or `/title-by-id` + `/title/offers`) for
   per-provider streaming/rental/purchase links; `/justwatch/title/similar`
   for recommendations.
4. **Box office (Box Office Mojo)** — `/boxofficemojo/title` or `/release`
   for one film's numbers; `/weekend/domestic`, `/year/domestic`,
   `/year/worldwide` for charts; `/franchise` / `/genre` / `/brand` for
   rollups; `/showdown` to compare two releases head-to-head.

Full endpoint list, methods, and params: [`reference/endpoints.md`](reference/endpoints.md).

## Calling the API

```sh
# Identity + scores:
scripts/crawlora.sh /imdb/search query="Dune Part Two" | jq '.'
scripts/crawlora.sh /tmdb/search query="Dune Part Two" | jq '.'
scripts/crawlora.sh /rottentomatoes/search query="Dune Part Two" | jq '.'

# Streaming availability:
scripts/crawlora.sh /justwatch/search query="Dune Part Two" | jq '.'
scripts/crawlora.sh /justwatch/title/offers id=<raw-justwatch-id> | jq '.'

# Box office:
scripts/crawlora.sh /boxofficemojo/title id=<mojo-title-id> | jq '.'
```

Raw `curl` fallback:

```sh
curl -fsS -H "x-api-key: $CRAWLORA_API_KEY" \
  "https://api.crawlora.net/api/v1/metacritic/movie/dune-part-two" | jq '.'
```

## Endpoint reference

See [`reference/endpoints.md`](reference/endpoints.md) for every IMDb, TMDB,
JustWatch, Letterboxd, Rotten Tomatoes, Metacritic, and Box Office Mojo
endpoint this skill uses.

## Examples

- **Critic-vs-audience gap:** `/metacritic/movie/{slug}` (critic Metascore
  vs. user score) alongside `/rottentomatoes/movie` (Tomatometer vs.
  audience score) for the same title.
- **Where-to-watch fan-out:** `/justwatch/search` → `/justwatch/title/offers`
  to list every subscription/rent/buy option and price by provider.
- **Franchise box-office trend:** `/boxofficemojo/franchise` for every
  entry's opening/lifetime gross, sorted chronologically.
- **Taste-matching:** `/letterboxd/film/{slug}/similar` or
  `/tmdb/movie/{id}` (TMDB includes recommendations) for "more like this."

## Notes & limits

- **Credits / pay-on-success:** billed only on `2xx`; free tier 2,000 credits/mo.
  Key at [https://crawlora.net](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills).
- **Public data only** — public title/review/box-office pages.
- **Security:** key lives in `CRAWLORA_API_KEY` only — never hardcode, query-param, or commit it.
- **JustWatch uses its own raw GraphQL ids** (not IMDb/TMDB ids) — resolve
  via `/justwatch/search` or `/justwatch/title/by-id` first.
- Results are paginated where noted — pass `page` to walk longer lists
  (reviews, charts, filmographies).
