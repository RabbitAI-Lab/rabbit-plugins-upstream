# sports-scores-research — endpoint reference — ESPN

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**14 endpoints across 1 platform group(s).**

## ESPN (14)

### `espn_athlete`

- **HTTP:** `GET /espn/athlete`
- **What:** ESPN athlete. Returns one athlete's bio/overview (name, position, jersey, physicals, current team). The `sport` enum accepts `football`, `basketball`, `baseball`, `hockey`, and `soccer`. The `league` enum accepts `nfl`, `college-football`, `nba`, `wnba`, `mens-college-basketball`, `womens-college-basketball`, `mlb`, `nhl`, `eng.1`, `esp.1`, `ita.1`, `ger.1`, `fra.1`, `usa.1`, and `uefa.champions`; it must be valid for the chosen sport.
- **Params:** `athlete` (string, **required**) — Numeric ESPN athlete (player) id; `league` (string, **required**) — League key (must be valid for the sport); `sport` (string, **required**) — Sport key

### `espn_athlete_gamelog`

- **HTTP:** `GET /espn/athlete-gamelog`
- **What:** ESPN athlete game log. Returns one athlete's game-by-game log for a season, grouped by season type (regular season, postseason, preseason) and by ESPN's blocks within it, such as months. Each game carries the event id, date, home or away, opponent, score, result and the athlete's `stats` map keyed by the column `name` in `columns`, plus block totals and season-type totals or averages. A season the athlete did not play returns an empty `season_types` list. The `sport` enum accepts `football`, `basketball`, `baseball`, `hockey`, and `soccer`. The `league` enum accepts `nfl`, `college-football`, `nba`, `wnba`, `mens-college-basketball`, `womens-college-basketball`, `mlb`, `nhl`, `eng.1`, `esp.1`, `ita.1`, `ger.1`, `fra.1`, `usa.1`, and `uefa.champions`; it must be valid for the chosen sport. The optional `category` enum accepts `batting` and `pitching` and only for baseball. The response lists the seasons ESPN offers for the athlete in `available_seasons`.
- **Params:** `athlete` (string, **required**) — Numeric ESPN athlete (player) id; `category` (string, optional) — Stat view (baseball only); `league` (string, **required**) — League key (must be valid for the sport); `season` (integer, optional) — Four-digit ESPN season year from available_seasons; defaults to the current season; `sport` (string, **required**) — Sport key

### `espn_athlete_splits`

- **HTTP:** `GET /espn/athlete-splits`
- **What:** ESPN athlete season splits. Returns one athlete's season splits table as ESPN's player Splits page shows it: the same stat columns broken down by home and away, wins and losses, month, opponent, half or quarter and more (the split families depend on the sport). Each row carries a `stats` map keyed by the column `name` in `columns`. The `sport` enum accepts `football`, `basketball`, `baseball`, and `hockey`; ESPN publishes no soccer splits. The `league` enum accepts `nfl`, `college-football`, `nba`, `wnba`, `mens-college-basketball`, `womens-college-basketball`, `mlb`, and `nhl`; it must be valid for the chosen sport. The optional `category` enum accepts `batting` and `pitching` for baseball, and `per_game`, `total`, and `per_48` for basketball; it is rejected for football and hockey. The response lists the seasons and categories ESPN offers for the athlete in `available_seasons` and `available_categories`.
- **Params:** `athlete` (string, **required**) — Numeric ESPN athlete (player) id; `category` (string, optional) — Stat view: batting or pitching (baseball); per_game, total or per_48 (basketball); `league` (string, **required**) — League key (must be valid for the sport); `season` (integer, optional) — Four-digit ESPN season year from available_seasons; defaults to the current season; `sport` (string, **required**) — Sport key

### `espn_game_summary`

- **HTTP:** `GET /espn/game-summary`
- **What:** ESPN game summary. Returns one game's matchup, betting odds, and boxscore stat totals. The `sport` enum accepts `football`, `basketball`, `baseball`, `hockey`, and `soccer`. The `league` enum accepts `nfl`, `college-football`, `nba`, `wnba`, `mens-college-basketball`, `womens-college-basketball`, `mlb`, `nhl`, `eng.1`, `esp.1`, `ita.1`, `ger.1`, `fra.1`, `usa.1`, and `uefa.champions`; it must be valid for the chosen sport. Get an `event` id from the scoreboard endpoint.
- **Params:** `event` (string, **required**) — Numeric ESPN event (game) id; `league` (string, **required**) — League key (must be valid for the sport); `sport` (string, **required**) — Sport key

### `espn_news`

- **HTTP:** `GET /espn/news`
- **What:** ESPN league news. Returns recent news articles (headline, description, link) for a league. The `sport` enum accepts `football`, `basketball`, `baseball`, `hockey`, and `soccer`. The `league` enum accepts `nfl`, `college-football`, `nba`, `wnba`, `mens-college-basketball`, `womens-college-basketball`, `mlb`, `nhl`, `eng.1`, `esp.1`, `ita.1`, `ger.1`, `fra.1`, `usa.1`, and `uefa.champions`; it must be valid for the chosen sport.
- **Params:** `league` (string, **required**) — League key (must be valid for the sport); `sport` (string, **required**) — Sport key

### `espn_rankings`

- **HTTP:** `GET /espn/rankings`
- **What:** ESPN poll rankings. Returns poll rankings (e.g. AP Top 25) for a college league. Rankings are only published for college leagues: the `sport` enum accepts `football` and `basketball`, and the `league` enum accepts `college-football`, `mens-college-basketball`, and `womens-college-basketball`.
- **Params:** `league` (string, **required**) — College league key; `sport` (string, **required**) — Sport key

### `espn_scoreboard`

- **HTTP:** `GET /espn/scoreboard`
- **What:** ESPN scoreboard. Returns games (scores, schedule, status, and odds when available) for a sport and league. The `sport` enum accepts `football`, `basketball`, `baseball`, `hockey`, and `soccer`. The `league` enum accepts `nfl`, `college-football`, `nba`, `wnba`, `mens-college-basketball`, `womens-college-basketball`, `mlb`, `nhl`, `eng.1`, `esp.1`, `ita.1`, `ger.1`, `fra.1`, `usa.1`, and `uefa.champions`; it must be valid for the chosen sport. The `seasontype` enum accepts `1` (preseason), `2` (regular season), `3` (postseason), and `4` (offseason).
- **Params:** `dates` (string, optional) — Date or range as YYYYMMDD, YYYYMMDD-YYYYMMDD, or YYYY; defaults to the current scoreboard; `league` (string, **required**) — League key (must be valid for the sport); `seasontype` (integer, optional) — Season type; `sport` (string, **required**) — Sport key; `week` (integer, optional) — Week number (football leagues)

### `espn_standings`

- **HTTP:** `GET /espn/standings`
- **What:** ESPN standings. Returns league standings grouped by conference/division. The `sport` enum accepts `football`, `basketball`, `baseball`, `hockey`, and `soccer`. The `league` enum accepts `nfl`, `college-football`, `nba`, `wnba`, `mens-college-basketball`, `womens-college-basketball`, `mlb`, `nhl`, `eng.1`, `esp.1`, `ita.1`, `ger.1`, `fra.1`, `usa.1`, and `uefa.champions`; it must be valid for the chosen sport. The `seasontype` enum accepts `1` (preseason), `2` (regular season), and `3` (postseason).
- **Params:** `league` (string, **required**) — League key (must be valid for the sport); `season` (integer, optional) — Four-digit season year; defaults to the current season; `seasontype` (integer, optional) — Season type; `sport` (string, **required**) — Sport key

### `espn_team`

- **HTTP:** `GET /espn/team`
- **What:** ESPN team detail. Returns one team's detail (identity, colors, record, standing summary). The `sport` enum accepts `football`, `basketball`, `baseball`, `hockey`, and `soccer`. The `league` enum accepts `nfl`, `college-football`, `nba`, `wnba`, `mens-college-basketball`, `womens-college-basketball`, `mlb`, `nhl`, `eng.1`, `esp.1`, `ita.1`, `ger.1`, `fra.1`, `usa.1`, and `uefa.champions`; it must be valid for the chosen sport.
- **Params:** `league` (string, **required**) — League key (must be valid for the sport); `sport` (string, **required**) — Sport key; `team` (string, **required**) — Team id (numeric) or abbreviation

### `espn_team_roster`

- **HTTP:** `GET /espn/team-roster`
- **What:** ESPN team roster. Returns a team's roster (players with position, jersey, age, and experience) plus head coach. The `sport` enum accepts `football`, `basketball`, `baseball`, `hockey`, and `soccer`. The `league` enum accepts `nfl`, `college-football`, `nba`, `wnba`, `mens-college-basketball`, `womens-college-basketball`, `mlb`, `nhl`, `eng.1`, `esp.1`, `ita.1`, `ger.1`, `fra.1`, `usa.1`, and `uefa.champions`; it must be valid for the chosen sport.
- **Params:** `league` (string, **required**) — League key (must be valid for the sport); `sport` (string, **required**) — Sport key; `team` (string, **required**) — Team id (numeric) or abbreviation

### `espn_team_schedule`

- **HTTP:** `GET /espn/team-schedule`
- **What:** ESPN team schedule. Returns one team's schedule for a season: every game with its event id, date, week, status, venue, TV networks and both sides with scores and records once played, plus the team's record, standing summary and, for football, bye week. A season type with no games returns an empty `games` list. The `sport` enum accepts `football`, `basketball`, `baseball`, `hockey`, and `soccer`. The `league` enum accepts `nfl`, `college-football`, `nba`, `wnba`, `mens-college-basketball`, `womens-college-basketball`, `mlb`, `nhl`, `eng.1`, `esp.1`, `ita.1`, `ger.1`, `fra.1`, `usa.1`, and `uefa.champions`; it must be valid for the chosen sport. The `seasontype` enum accepts `1` (preseason), `2` (regular season), `3` (postseason), and `4` (offseason). For soccer, `fixture=true` returns upcoming fixtures instead of played results; it is rejected for other sports.
- **Params:** `fixture` (boolean, optional) — Soccer only: return upcoming fixtures instead of played results; `league` (string, **required**) — League key (must be valid for the sport); `season` (integer, optional) — Four-digit ESPN season year; defaults to the current season; `seasontype` (integer, optional) — Season type; `sport` (string, **required**) — Sport key; `team` (string, **required**) — Team id (numeric) or abbreviation

### `espn_team_stats`

- **HTTP:** `GET /espn/team-stats`
- **What:** ESPN team season statistics. Returns one team's season statistics grouped into categories such as passing, rushing and defense or batting, pitching and fielding. Each statistic has its key, name, value, display value and, where ESPN gives them, per-game values and league ranks. Football responses add the opponents' totals against the team in `opponent`; baseball responses add splits such as home, away and by opponent in `splits`. The `sport` enum accepts `football`, `basketball`, `baseball`, and `hockey`; ESPN publishes no soccer team statistics. The `league` enum accepts `nfl`, `college-football`, `nba`, `wnba`, `mens-college-basketball`, `womens-college-basketball`, `mlb`, and `nhl`; it must be valid for the chosen sport. The `seasontype` enum accepts `1` (preseason), `2` (regular season), `3` (postseason), and `4` (offseason). A team and season without statistics returns not found.
- **Params:** `league` (string, **required**) — League key (must be valid for the sport); `season` (integer, optional) — Four-digit ESPN season year; defaults to the current season; `seasontype` (integer, optional) — Season type; `sport` (string, **required**) — Sport key; `team` (string, **required**) — Team id (numeric) or abbreviation

### `espn_teams`

- **HTTP:** `GET /espn/teams`
- **What:** ESPN team list. Returns the full team list for a sport and league. The `sport` enum accepts `football`, `basketball`, `baseball`, `hockey`, and `soccer`. The `league` enum accepts `nfl`, `college-football`, `nba`, `wnba`, `mens-college-basketball`, `womens-college-basketball`, `mlb`, `nhl`, `eng.1`, `esp.1`, `ita.1`, `ger.1`, `fra.1`, `usa.1`, and `uefa.champions`; it must be valid for the chosen sport.
- **Params:** `league` (string, **required**) — League key (must be valid for the sport); `sport` (string, **required**) — Sport key

### `espn_transactions`

- **HTTP:** `GET /espn/transactions`
- **What:** ESPN league transactions. Returns one page of a league's transaction wire, newest first: signings, releases, trades, practice-squad and injured-list moves, each with its date, ESPN's description and the team. Pass `team` to return only one team's moves. Paging follows ESPN: `page` starts at 1, `limit` sets the page size (1 to 100, default 25), and `total` and `page_count` describe the full list; a page past the end returns an empty list. Leagues ESPN keeps no wire for, such as the soccer leagues, return an empty list. The `sport` enum accepts `football`, `basketball`, `baseball`, `hockey`, and `soccer`. The `league` enum accepts `nfl`, `college-football`, `nba`, `wnba`, `mens-college-basketball`, `womens-college-basketball`, `mlb`, `nhl`, `eng.1`, `esp.1`, `ita.1`, `ger.1`, `fra.1`, `usa.1`, and `uefa.champions`; it must be valid for the chosen sport.
- **Params:** `league` (string, **required**) — League key (must be valid for the sport); `limit` (integer, optional) — Transactions per page (1-100, default 25); `page` (integer, optional) — 1-based page number; `season` (integer, optional) — Four-digit ESPN season year; defaults to the current season; `sport` (string, **required**) — Sport key; `team` (string, optional) — Team id (numeric) or abbreviation to filter to one team
