# sports-betting-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**36 endpoints across 3 platform group(s).**

## DraftKings Sportsbook (12)

### `draftkings_event`

- **HTTP:** `GET /draftkings/sportsbook/event`
- **What:** DraftKings Sportsbook event. Returns one event's metadata (league id, sport id, teams, status, start time) from DraftKings' credential-free public JSON. `event_id` is a numeric DraftKings event identifier (find it from an event's DraftKings Sportsbook page, or from the `id` field of an event returned by /draftkings/sportsbook/odds). The returned `league_id` is accepted by /draftkings/sportsbook/odds and /draftkings/sportsbook/futures. This endpoint does not include betting markets/odds.
- **Params:** `event_id` (string, **required**) — Numeric DraftKings event id

### `draftkings_event_context`

- **HTTP:** `GET /draftkings/sportsbook/event-context`
- **What:** DraftKings Sportsbook event context. Returns public sport, league, and event navigation identifiers for a numeric DraftKings event id. Use it to associate an event with DraftKings Sportsbook's public sport and league navigation.
- **Params:** `event_id` (string, **required**) — Numeric DraftKings event id

### `draftkings_event_markets`

- **HTTP:** `GET /draftkings/sportsbook/event-markets`
- **What:** DraftKings Sportsbook event markets. Returns one event's betting markets and selections for a specific market category, from DraftKings' credential-free public JSON. `event_id` is a numeric DraftKings event identifier (find it from the `id` field of an event returned by /draftkings/sportsbook/odds). `subcategory_id` selects the market category (e.g. game lines, a player-prop category, an alternate-line category) -- find one from the `subcategory_id` field on a market returned by /draftkings/sportsbook/odds, or from a DraftKings Sportsbook event page's own network traffic. An empty `markets` list is a valid response when the category has no markets currently posted for this event.
- **Params:** `event_id` (string, **required**) — Numeric DraftKings event id; `subcategory_id` (string, **required**) — Numeric DraftKings market subcategory id

### `draftkings_featured_leagues`

- **HTTP:** `GET /draftkings/sportsbook/featured-leagues`
- **What:** DraftKings Sportsbook featured leagues. Returns public DraftKings Sportsbook leagues currently marked as featured in its sport navigation. Each item includes its numeric `id`, capability `tags`, live-offer status, and upstream featured ordering. Use the `id` as `league_id` with /draftkings/sportsbook/odds and /draftkings/sportsbook/futures.
- **Params:** _none_

### `draftkings_futures`

- **HTTP:** `GET /draftkings/sportsbook/futures`
- **What:** DraftKings Sportsbook futures. Returns league-level futures markets and selections for a specific DraftKings market category, from DraftKings' credential-free public JSON. `league_id` is a numeric DraftKings league identifier and `subcategory_id` is a numeric futures category identifier. An empty `events` list is a valid response when the category has no markets currently posted for that league.
- **Params:** `league_id` (string, **required**) — Numeric DraftKings league id; `subcategory_id` (string, **required**) — Numeric DraftKings futures market subcategory id

### `draftkings_league_events`

- **HTTP:** `GET /draftkings/sportsbook/league-events`
- **What:** DraftKings Sportsbook league event directory. Returns a DraftKings Sportsbook league's current public event directory, including event IDs, teams or other participants, start times, status, and public availability tags. Supply a numeric `league_id` from /draftkings/sportsbook/leagues, /draftkings/sportsbook/quick-links, /draftkings/sportsbook/featured-leagues, or /draftkings/sportsbook/event. This endpoint does not include betting markets or odds.
- **Params:** `league_id` (string, **required**) — Numeric DraftKings league id

### `draftkings_leagues`

- **HTTP:** `GET /draftkings/sportsbook/leagues`
- **What:** DraftKings Sportsbook sports and leagues. Returns DraftKings Sportsbook's current public sport and league directory. Each league `id` is accepted as `league_id` by /draftkings/sportsbook/odds and /draftkings/sportsbook/futures.
- **Params:** _none_

### `draftkings_live`

- **HTTP:** `GET /draftkings/sportsbook/live`
- **What:** DraftKings Sportsbook live events. Returns the live events currently shown by DraftKings Sportsbook, including score state, period, primary markets, and market categories that can be used with /draftkings/sportsbook/event-markets. An empty `events` list is valid when DraftKings has no live events at request time.
- **Params:** _none_

### `draftkings_odds`

- **HTTP:** `GET /draftkings/sportsbook/odds`
- **What:** DraftKings Sportsbook odds. Returns the primary betting markets (moneyline, spread, total) for every upcoming event in a DraftKings Sportsbook league, from DraftKings' credential-free public JSON. `league_id` is a numeric DraftKings league identifier (find it from a league's DraftKings Sportsbook page). An empty `events` list is a valid response when nothing is currently scheduled.
- **Params:** `league_id` (string, **required**) — Numeric DraftKings league id

### `draftkings_quick_links`

- **HTTP:** `GET /draftkings/sportsbook/quick-links`
- **What:** DraftKings Sportsbook quick links. Returns the ordered league shortcuts currently prioritized on DraftKings Sportsbook's public home page. Each item includes a numeric `league_id` accepted by /draftkings/sportsbook/odds and /draftkings/sportsbook/futures.
- **Params:** _none_

### `draftkings_team`

- **HTTP:** `GET /draftkings/sportsbook/team`
- **What:** DraftKings Sportsbook team. Returns stable team metadata embedded in a public DraftKings Sportsbook team page. Supply `team_id`, `sport`, and `slug` from an item returned by /draftkings/sportsbook/teams. Allowed `sport` values: `football`, `hockey`, `basketball`, `baseball`.
- **Params:** `slug` (string, **required**) — Lowercase DraftKings team slug; `sport` (string, **required**) — Sport: football, hockey, basketball, baseball; `team_id` (string, **required**) — Numeric DraftKings team id

### `draftkings_teams`

- **HTTP:** `GET /draftkings/sportsbook/teams`
- **What:** DraftKings Sportsbook league teams. Returns the teams listed on DraftKings Sportsbook's public Teams page for one league. Allowed `league` values: `nfl`, `nhl`, `nba`, `cbb`, `mlb`, `cfb`.
- **Params:** `league` (string, **required**) — League: nfl, nhl, nba, cbb, mlb, cfb

## ESPN (9)

### `espn_athlete`

- **HTTP:** `GET /espn/athlete`
- **What:** ESPN athlete. Returns one athlete's bio/overview (name, position, jersey, physicals, current team) from ESPN's credential-free public JSON. The `sport` enum accepts `football`, `basketball`, `baseball`, `hockey`, and `soccer`. The `league` enum accepts `nfl`, `college-football`, `nba`, `wnba`, `mens-college-basketball`, `womens-college-basketball`, `mlb`, `nhl`, `eng.1`, `esp.1`, `ita.1`, `ger.1`, `fra.1`, `usa.1`, and `uefa.champions`; it must be valid for the chosen sport.
- **Params:** `athlete` (string, **required**) — Numeric ESPN athlete (player) id; `league` (string, **required**) — League key (must be valid for the sport); `sport` (string, **required**) — Sport key

### `espn_game_summary`

- **HTTP:** `GET /espn/game-summary`
- **What:** ESPN game summary. Returns one game's matchup, betting odds, and boxscore stat totals from ESPN's credential-free public JSON. The `sport` enum accepts `football`, `basketball`, `baseball`, `hockey`, and `soccer`. The `league` enum accepts `nfl`, `college-football`, `nba`, `wnba`, `mens-college-basketball`, `womens-college-basketball`, `mlb`, `nhl`, `eng.1`, `esp.1`, `ita.1`, `ger.1`, `fra.1`, `usa.1`, and `uefa.champions`; it must be valid for the chosen sport. Get an `event` id from the scoreboard endpoint.
- **Params:** `event` (string, **required**) — Numeric ESPN event (game) id; `league` (string, **required**) — League key (must be valid for the sport); `sport` (string, **required**) — Sport key

### `espn_news`

- **HTTP:** `GET /espn/news`
- **What:** ESPN league news. Returns recent news articles (headline, description, link) for a league from ESPN's credential-free public JSON. The `sport` enum accepts `football`, `basketball`, `baseball`, `hockey`, and `soccer`. The `league` enum accepts `nfl`, `college-football`, `nba`, `wnba`, `mens-college-basketball`, `womens-college-basketball`, `mlb`, `nhl`, `eng.1`, `esp.1`, `ita.1`, `ger.1`, `fra.1`, `usa.1`, and `uefa.champions`; it must be valid for the chosen sport.
- **Params:** `league` (string, **required**) — League key (must be valid for the sport); `sport` (string, **required**) — Sport key

### `espn_rankings`

- **HTTP:** `GET /espn/rankings`
- **What:** ESPN poll rankings. Returns poll rankings (e.g. AP Top 25) for a college league from ESPN's credential-free public JSON. Rankings are only published for college leagues: the `sport` enum accepts `football` and `basketball`, and the `league` enum accepts `college-football`, `mens-college-basketball`, and `womens-college-basketball`.
- **Params:** `league` (string, **required**) — College league key; `sport` (string, **required**) — Sport key

### `espn_scoreboard`

- **HTTP:** `GET /espn/scoreboard`
- **What:** ESPN scoreboard. Returns games (scores, schedule, status, and odds when available) for a sport and league from ESPN's credential-free public JSON. The `sport` enum accepts `football`, `basketball`, `baseball`, `hockey`, and `soccer`. The `league` enum accepts `nfl`, `college-football`, `nba`, `wnba`, `mens-college-basketball`, `womens-college-basketball`, `mlb`, `nhl`, `eng.1`, `esp.1`, `ita.1`, `ger.1`, `fra.1`, `usa.1`, and `uefa.champions`; it must be valid for the chosen sport. The `seasontype` enum accepts `1` (preseason), `2` (regular season), `3` (postseason), and `4` (offseason).
- **Params:** `dates` (string, optional) — Date or range as YYYYMMDD, YYYYMMDD-YYYYMMDD, or YYYY; defaults to the current scoreboard; `league` (string, **required**) — League key (must be valid for the sport); `seasontype` (integer, optional) — Season type; `sport` (string, **required**) — Sport key; `week` (integer, optional) — Week number (football leagues)

### `espn_standings`

- **HTTP:** `GET /espn/standings`
- **What:** ESPN standings. Returns league standings grouped by conference/division from ESPN's credential-free public JSON. The `sport` enum accepts `football`, `basketball`, `baseball`, `hockey`, and `soccer`. The `league` enum accepts `nfl`, `college-football`, `nba`, `wnba`, `mens-college-basketball`, `womens-college-basketball`, `mlb`, `nhl`, `eng.1`, `esp.1`, `ita.1`, `ger.1`, `fra.1`, `usa.1`, and `uefa.champions`; it must be valid for the chosen sport. The `seasontype` enum accepts `1` (preseason), `2` (regular season), and `3` (postseason).
- **Params:** `league` (string, **required**) — League key (must be valid for the sport); `season` (integer, optional) — Four-digit season year; defaults to the current season; `seasontype` (integer, optional) — Season type; `sport` (string, **required**) — Sport key

### `espn_team`

- **HTTP:** `GET /espn/team`
- **What:** ESPN team detail. Returns one team's detail (identity, colors, record, standing summary) from ESPN's credential-free public JSON. The `sport` enum accepts `football`, `basketball`, `baseball`, `hockey`, and `soccer`. The `league` enum accepts `nfl`, `college-football`, `nba`, `wnba`, `mens-college-basketball`, `womens-college-basketball`, `mlb`, `nhl`, `eng.1`, `esp.1`, `ita.1`, `ger.1`, `fra.1`, `usa.1`, and `uefa.champions`; it must be valid for the chosen sport.
- **Params:** `league` (string, **required**) — League key (must be valid for the sport); `sport` (string, **required**) — Sport key; `team` (string, **required**) — Team id (numeric) or abbreviation

### `espn_team_roster`

- **HTTP:** `GET /espn/team-roster`
- **What:** ESPN team roster. Returns a team's roster (players with position, jersey, age, and experience) plus head coach from ESPN's credential-free public JSON. The `sport` enum accepts `football`, `basketball`, `baseball`, `hockey`, and `soccer`. The `league` enum accepts `nfl`, `college-football`, `nba`, `wnba`, `mens-college-basketball`, `womens-college-basketball`, `mlb`, `nhl`, `eng.1`, `esp.1`, `ita.1`, `ger.1`, `fra.1`, `usa.1`, and `uefa.champions`; it must be valid for the chosen sport.
- **Params:** `league` (string, **required**) — League key (must be valid for the sport); `sport` (string, **required**) — Sport key; `team` (string, **required**) — Team id (numeric) or abbreviation

### `espn_teams`

- **HTTP:** `GET /espn/teams`
- **What:** ESPN team list. Returns the full team list for a sport and league from ESPN's credential-free public JSON. The `sport` enum accepts `football`, `basketball`, `baseball`, `hockey`, and `soccer`. The `league` enum accepts `nfl`, `college-football`, `nba`, `wnba`, `mens-college-basketball`, `womens-college-basketball`, `mlb`, `nhl`, `eng.1`, `esp.1`, `ita.1`, `ger.1`, `fra.1`, `usa.1`, and `uefa.champions`; it must be valid for the chosen sport.
- **Params:** `league` (string, **required**) — League key (must be valid for the sport); `sport` (string, **required**) — Sport key

## SofaScore (15)

### `sofascore_event`

- **HTTP:** `GET /sofascore/event`
- **What:** SofaScore event detail. Returns one match's detail (teams, score, status, venue, referee) from SofaScore's credential-free public JSON.
- **Params:** `id` (string, **required**) — Numeric SofaScore event (match) id

### `sofascore_event_h2h`

- **HTTP:** `GET /sofascore/event-h2h`
- **What:** SofaScore event head-to-head. Returns the historical head-to-head win/draw record between a match's two teams (and managers, when available) from SofaScore's credential-free public JSON.
- **Params:** `id` (string, **required**) — Numeric SofaScore event (match) id

### `sofascore_event_incidents`

- **HTTP:** `GET /sofascore/event-incidents`
- **What:** SofaScore event incidents. Returns one match's goal, card, substitution, and period timeline from SofaScore's credential-free public JSON. An empty `incidents` list is a valid response before kickoff.
- **Params:** `id` (string, **required**) — Numeric SofaScore event (match) id

### `sofascore_event_lineups`

- **HTTP:** `GET /sofascore/event-lineups`
- **What:** SofaScore event lineups. Returns one match's starting XI and substitutes per side, with formation, from SofaScore's credential-free public JSON. Returns 404 when SofaScore has no lineups for the match.
- **Params:** `id` (string, **required**) — Numeric SofaScore event (match) id

### `sofascore_event_odds`

- **HTTP:** `GET /sofascore/event-odds`
- **What:** SofaScore event odds. Returns one match's betting markets and choices from SofaScore's credential-free public JSON. Returns 404 when SofaScore has no odds for the match.
- **Params:** `id` (string, **required**) — Numeric SofaScore event (match) id

### `sofascore_event_statistics`

- **HTTP:** `GET /sofascore/event-statistics`
- **What:** SofaScore event statistics. Returns one match's statistics (possession, shots, passes, and more, grouped and split by period) from SofaScore's credential-free public JSON. Returns 404 when SofaScore has no tracked statistics for the match.
- **Params:** `id` (string, **required**) — Numeric SofaScore event (match) id

### `sofascore_live_events`

- **HTTP:** `GET /sofascore/live-events`
- **What:** SofaScore live events. Returns currently live events for a sport from SofaScore's credential-free public JSON. The `sport` enum accepts `football`, `basketball`, and `tennis`. An empty `events` list is a valid response when nothing is live right now.
- **Params:** `sport` (string, **required**) — Sport key

### `sofascore_player`

- **HTTP:** `GET /sofascore/player`
- **What:** SofaScore player detail. Returns one player's bio (position, height, market value, current team) from SofaScore's credential-free public JSON.
- **Params:** `id` (string, **required**) — Numeric SofaScore player id

### `sofascore_round_events`

- **HTTP:** `GET /sofascore/round-events`
- **What:** SofaScore round fixtures. Returns fixtures for one round of a competition season from SofaScore's credential-free public JSON. Get `id` from search and `season` from tournament-seasons.
- **Params:** `id` (string, **required**) — Numeric SofaScore unique-tournament (competition) id; `round` (integer, **required**) — Round number; `season` (string, **required**) — Numeric SofaScore season id

### `sofascore_search`

- **HTTP:** `GET /sofascore/search`
- **What:** SofaScore universal search. Searches SofaScore's credential-free public JSON for teams, players, and competitions matching a free-text query. An empty `results` list is a valid response when nothing matches.
- **Params:** `q` (string, **required**) — Free-text search query

### `sofascore_standings`

- **HTTP:** `GET /sofascore/standings`
- **What:** SofaScore standings. Returns a league table for a competition season from SofaScore's credential-free public JSON. The `type` enum accepts `total`, `home`, and `away`. Get `id` from search and `season` from tournament-seasons.
- **Params:** `id` (string, **required**) — Numeric SofaScore unique-tournament (competition) id; `season` (string, **required**) — Numeric SofaScore season id; `type` (string, **required**) — Standings variant

### `sofascore_team`

- **HTTP:** `GET /sofascore/team`
- **What:** SofaScore team detail. Returns one team's detail (identity, manager, venue, primary competition) from SofaScore's credential-free public JSON.
- **Params:** `id` (string, **required**) — Numeric SofaScore team id

### `sofascore_team_events`

- **HTTP:** `GET /sofascore/team-events`
- **What:** SofaScore team fixtures. Returns a page of a team's upcoming or recent fixtures from SofaScore's credential-free public JSON. The `direction` enum accepts `next` and `last`. An empty `events` list is a valid response when there is no fixture on that page.
- **Params:** `direction` (string, **required**) — Fixture direction; `id` (string, **required**) — Numeric SofaScore team id; `page` (integer, optional) — Zero-based page number

### `sofascore_team_players`

- **HTTP:** `GET /sofascore/team-players`
- **What:** SofaScore team players. Returns a team's full squad from SofaScore's credential-free public JSON.
- **Params:** `id` (string, **required**) — Numeric SofaScore team id

### `sofascore_tournament_seasons`

- **HTTP:** `GET /sofascore/tournament-seasons`
- **What:** SofaScore competition seasons. Returns the season list for a competition from SofaScore's credential-free public JSON. Use a returned season id with the standings and round-events endpoints.
- **Params:** `id` (string, **required**) — Numeric SofaScore unique-tournament (competition) id
