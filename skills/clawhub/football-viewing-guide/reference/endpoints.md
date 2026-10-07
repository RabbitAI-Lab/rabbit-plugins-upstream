# football-viewing-guide — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Only the endpoints used by this workflow. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**6 endpoints across 1 platform group(s).**

## FotMob (6)

### `fotmob_match`

- **HTTP:** `GET /fotmob/match`
- **What:** FotMob match details. Returns FotMob's public match-details payload, including available facts, events, statistics, lineups, shot map, momentum, table and head-to-head sections. The data field preserves the upstream JSON shape; individual sections may be absent for a match.
- **Params:** `id` (string, **required**) — Numeric FotMob match id

### `fotmob_matches`

- **HTTP:** `GET /fotmob/matches`
- **What:** FotMob matches for a date. Returns FotMob's public match payload for a calendar date and IANA timezone. The data field preserves the upstream JSON shape.
- **Params:** `date` (string, **required**) — Date in YYYYMMDD format; `timezone` (string, optional) — IANA timezone; defaults to UTC

### `fotmob_search`

- **HTTP:** `GET /fotmob/search`
- **What:** Search FotMob entities. Returns public search suggestions for FotMob leagues, teams, players, and matches. term must contain 1 to 50 characters. Suggestions preserve the upstream JSON shape.
- **Params:** `term` (string, **required**) — Search phrase, 1 to 50 characters

### `fotmob_tv_guide`

- **HTTP:** `GET /fotmob/tv-guide`
- **What:** FotMob football TV guide. Returns the public seven-day football broadcast schedule for a country, with local schedule times. Discover all accepted country codes from /fotmob/tv-guide-countries. Timezone defaults to UTC.
- **Params:** `country` (string, **required**) — Market code from /fotmob/tv-guide-countries; `timezone` (string, optional) — IANA timezone for local times

### `fotmob_tv_guide_channels`

- **HTTP:** `GET /fotmob/tv-guide-channels`
- **What:** FotMob TV guide channels. Discovers channels attached to matches in the selected country's current seven-day public TV guide window. Use the country directory to discover the complete country code set.
- **Params:** `country` (string, **required**) — Market code from /fotmob/tv-guide-countries

### `fotmob_tv_guide_countries`

- **HTTP:** `GET /fotmob/tv-guide-countries`
- **What:** FotMob TV guide country directory. Lists all country codes exposed by FotMob's public football TV guide country selector.
- **Params:** _none_
