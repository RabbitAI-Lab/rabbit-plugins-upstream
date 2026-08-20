# sports-scores-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**40 endpoints across 4 platform group(s).**

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

## MLB (12)

### `mlb_game`

- **HTTP:** `GET /mlb/game`
- **What:** Get an MLB game feed. Returns a compact MLB game feed with status, teams, score, innings, probable pitchers, decisions, and team box-score totals.
- **Params:** `id` (string, **required**) — Numeric MLB game id

### `mlb_game_boxscore`

- **HTTP:** `GET /mlb/game-boxscore`
- **What:** Get an MLB player boxscore. Returns both teams' player batting, pitching, and fielding lines for a game.
- **Params:** `id` (string, **required**) — Numeric MLB game id

### `mlb_game_play_by_play`

- **HTTP:** `GET /mlb/game-play-by-play`
- **What:** Get MLB game play-by-play. Returns every at-bat and pitch/event record for an MLB game.
- **Params:** `id` (string, **required**) — Numeric MLB game id

### `mlb_league_stats`

- **HTTP:** `GET /mlb/league-stats`
- **What:** Get ranked MLB league statistics. Returns ranked MLB season stat splits across both leagues. The group enum accepts `hitting`, `pitching`, and `fielding`.
- **Params:** `group` (string, **required**) — Stat group; `limit` (integer, optional) — Results to return (1-100); `season` (integer, optional) — Four-digit season; defaults to current year

### `mlb_player`

- **HTTP:** `GET /mlb/player`
- **What:** Get an MLB player. Returns an MLB player's identity, biographical information, position, handedness, active status, and current team.
- **Params:** `id` (string, **required**) — Numeric MLB player id

### `mlb_player_stats`

- **HTTP:** `GET /mlb/player-stats`
- **What:** Get MLB player season statistics. Returns one player's MLB season statistics. The group enum accepts `hitting`, `pitching`, and `fielding`.
- **Params:** `group` (string, **required**) — Stat group; `id` (string, **required**) — Numeric MLB player id; `season` (integer, optional) — Four-digit season; defaults to current year

### `mlb_schedule`

- **HTTP:** `GET /mlb/schedule`
- **What:** Get the MLB schedule and scores. Returns MLB games, teams, scores, status, probable pitchers, venue, and series information for one date or date range, optionally filtered to a team.
- **Params:** `date` (string, optional) — Single date in YYYY-MM-DD format; `end_date` (string, optional) — Range end in YYYY-MM-DD format; `start_date` (string, optional) — Range start in YYYY-MM-DD format; `team_id` (string, optional) — Numeric MLB team id

### `mlb_standings`

- **HTTP:** `GET /mlb/standings`
- **What:** Get MLB standings. Returns American League and National League standings grouped by division. The type enum accepts `regularSeason`, `wildCard`, and `springTraining`.
- **Params:** `season` (integer, optional) — Four-digit season; defaults to current year; `type` (string, optional) — Standings type

### `mlb_team_roster`

- **HTTP:** `GET /mlb/team-roster`
- **What:** Get an MLB team roster. Returns a team's players, jersey numbers, positions, and roster status. The roster_type enum accepts `active`, `40Man`, and `fullSeason`.
- **Params:** `roster_type` (string, optional) — Roster type; `season` (integer, optional) — Four-digit season; defaults to current year; `team_id` (string, **required**) — Numeric MLB team id

### `mlb_team_stats`

- **HTTP:** `GET /mlb/team-stats`
- **What:** Get MLB team season statistics. Returns one team's season statistics. Group accepts `hitting`, `pitching`, and `fielding`.
- **Params:** `group` (string, **required**) — Statistics group; `season` (integer, optional) — Four-digit season; `team_id` (string, **required**) — Numeric MLB team id

### `mlb_teams`

- **HTTP:** `GET /mlb/teams`
- **What:** List MLB teams. Returns the 30 MLB clubs for a season with league, division, venue, and abbreviation metadata.
- **Params:** `season` (integer, optional) — Four-digit season; defaults to current year

### `mlb_transactions`

- **HTTP:** `GET /mlb/transactions`
- **What:** List MLB transactions. Lists signings, trades, options, assignments, injured-list moves, and other MLB transactions for a date range.
- **Params:** `end_date` (string, **required**) — Range end in YYYY-MM-DD format; `player_id` (string, optional) — Numeric MLB player id; `start_date` (string, **required**) — Range start in YYYY-MM-DD format; `team_id` (string, optional) — Numeric MLB team id

## Strava (4)

### `strava_challenges`

- **HTTP:** `GET /strava/challenges`
- **What:** Strava's public challenge gallery. Returns Strava's public challenge gallery: the currently promoted challenge plus every gallery section (partner challenges, and one section per sport such as run/ride), each with its challenges' goal, duration, and cover art. Public data, sourced from Strava's own challenge gallery.
- **Params:** _none_

### `strava_club`

- **HTTP:** `GET /strava/clubs/{id}`
- **What:** A Strava club's public profile. Returns a Strava club's public profile: name, verified/private flags, location, description, member count, and cover/avatar images. Only the base public profile is returned -- discussion, leaderboard, member list, and recent-activity data require a logged-in Strava session and are not available. Public data, sourced from Strava's own server-rendered club page.
- **Params:** `id` (string, **required**) — Strava club ID

### `strava_route_detail`

- **HTTP:** `GET /strava/routes/detail`
- **What:** A single Strava route's detail page. Returns a single Strava route's detail: type, difficulty, distance, elevation gain, estimated time, and summary. `path` is the relative route path returned by `/strava/routes` results (e.g. `hiking/usa/colorado/boulder/mallory-cave_5171952737974445730`). Public data, sourced from Strava's own server-rendered route pages.
- **Params:** `path` (string, **required**) — Relative route path, from a /strava/routes result's path field

### `strava_routes`

- **HTTP:** `GET /strava/routes`
- **What:** Strava route-index listing for a sport, country, and region. Returns a page of Strava's public route recommendations for a sport, country, and region (state, or state/city). `sport` values: `hiking`, `road-biking`, `mountain-biking`, `trail-running`, `gravel-biking`. Public data, sourced from Strava's own server-rendered route pages.
- **Params:** `country` (string, **required**) — Country slug, e.g. usa; `page` (integer, optional) — Page number, starting at 1; `region` (string, **required**) — Region slug: a state (colorado) or state/city (colorado/boulder); `sport` (string, **required**) — Route sport. Allowed values: hiking, road-biking, mountain-biking, trail-running, gravel-biking
