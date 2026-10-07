# sports-scores-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**176 endpoints across 7 platform group(s).**

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

## MLB (66)

### `mlb_discovery`

- **HTTP:** `GET /mlb/discovery`
- **What:** Discover MLB sections and Stats API values. Returns MLB.com's live navigation tree, including hidden nodes labeled with visibility, and the MLB-only value sets for leagues, divisions, game types, roster types, standings types, stat groups, supported stat types, leader categories, MLB Pipeline prospect filters, league-stats hitter positions and player pools, and observed Baseball Savant leaderboard categories and filters including Top Performers, ABS Challenges, Expected Statistics, Outs Above Average, Arm Strength, Arm Value, Home Runs, Percentile Rankings, Pitch Movement, Rolling Windows, Pitcher Arm Angle, Year-to-Year Changes, Catcher Blocking, Catcher Framing, Catcher Throwing, First Base Receiving, and Fielding Run Value. Use these values to discover sections and supported filters before calling MLB endpoints.
- **Params:** _none_

### `mlb_editorial_feed`

- **HTTP:** `GET /mlb/editorial-feed`
- **What:** Get an MLB.com editorial feed. Returns a paginated first-party MLB.com news, video, or selection feed. Slugs are dynamic and not a complete closed topic catalog; discover current topic suggestions with mlb-search and sections with mlb-discovery. Feed items retain upstream Article, ShortContent, VSMContent, or Video fields.
- **Params:** `language` (string, optional) — Feed locale; `limit` (integer, optional) — Items per page (1-100); `skip` (integer, optional) — Number of items to skip (0-100000); `slug` (string, **required**) — MLB feed or selection slug, such as mlb-news-list or sel-vvc-mlb-stories

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

### `mlb_league_leaders`

- **HTTP:** `GET /mlb/league-leaders`
- **What:** Get MLB league leaders. Returns ranked MLB leader entries for one or more validated categories. Use mlb-discovery for all accepted categories, groups, and game type codes.
- **Params:** `categories` (string, **required**) — Comma-separated MLB leader category names; values are listed in mlb-discovery; `game_type` (string, optional) — MLB game type; `group` (string, optional) — Stat group; `league_id` (string, optional) — MLB league id; `limit` (integer, optional) — Leaders per category (1-100); `season` (integer, optional) — Four-digit season; defaults to current year

### `mlb_league_stats`

- **HTTP:** `GET /mlb/league-stats`
- **What:** Get ranked MLB league statistics. Returns ranked MLB season stat splits across both leagues. The group enum accepts every value returned by mlb_discovery.
- **Params:** `end_date` (string, optional) — End date for byDateRange stat types; requires start_date; `game_type` (string, optional) — MLB game type; `group` (string, **required**) — Stat group; `league_id` (string, optional) — MLB league id; `limit` (integer, optional) — Results to return (1-100); `offset` (integer, optional) — Zero-based result offset (0-10000); `opponent_player_id` (string, optional) — Required by vsPlayer stat types; `opponent_team_id` (string, optional) — Required by vsTeam stat types; `player_pool` (string, optional) — Qualified-player pool; `position` (string, optional) — Hitter position; use only with group=hitting; `season` (integer, optional) — Four-digit season; defaults to current year; `start_date` (string, optional) — Start date for byDateRange stat types; requires end_date; `stat_type` (string, optional) — Stats API stat type; defaults to season; `team_id` (string, optional) — Optional MLB team id; discover current team ids with mlb_teams

### `mlb_player`

- **HTTP:** `GET /mlb/player`
- **What:** Get an MLB player. Returns an MLB player's identity, biographical information, position, handedness, active status, and current team.
- **Params:** `id` (string, **required**) — Numeric MLB player id

### `mlb_player_stats`

- **HTTP:** `GET /mlb/player-stats`
- **What:** Get MLB player season statistics. Returns one player's MLB season statistics. The group enum accepts every value returned by mlb_discovery.
- **Params:** `end_date` (string, optional) — End date for byDateRange stat types; requires start_date; `game_type` (string, optional) — MLB game type; `group` (string, **required**) — Stat group; `id` (string, **required**) — Numeric MLB player id; `opponent_player_id` (string, optional) — Required by vsPlayer stat types; `opponent_team_id` (string, optional) — Required by vsTeam stat types; `season` (integer, optional) — Four-digit season; defaults to current year; `start_date` (string, optional) — Start date for byDateRange stat types; requires end_date; `stat_type` (string, optional) — Stats API stat type; defaults to season

### `mlb_prospect_rankings`

- **HTTP:** `GET /mlb/prospect-rankings`
- **What:** Get MLB Pipeline curated prospect rankings. Returns MLB Pipeline's curated Top 100, Top 30 by Team, Top 10 by Position, Draft Top 200, or International Top 50 ranking. The anonymous first-party page embeds full ranked data. Search, sort, team filtering on Top 100, and pagination are applied to the extracted rows. Use mlb_discovery for the exact view, year, team, position, and sort values.
- **Params:** `limit` (integer, optional) — Rows per page (1-250); `offset` (integer, optional) — Zero-based row offset; `position` (string, optional) — Required for view=position; `q` (string, optional) — Case-insensitive player-name substring; `sort` (string, optional) — Local sort field; `sort_dir` (string, optional) — Local sort direction; `team_filter` (string, optional) — Optional organization filter for view=top100; use a team slug from mlb_discovery.; `team_slug` (string, optional) — Required for view=team; one of the MLB Pipeline team ranking slugs. See mlb_discovery.; `view` (string, optional) — Ranking view; `year` (integer, optional) — Ranking year

### `mlb_prospect_stats`

- **HTTP:** `GET /mlb/prospect-stats`
- **What:** Get MLB Pipeline prospect statistics and rankings. Returns MLB Pipeline prospect stats from the anonymous first-party prospect tables. Supports the Top 100, all-prospect, or one-team list; batter/pitcher views; validated date periods and minimum thresholds; and local name/position filters. Use mlb_discovery for date periods, minimum thresholds, and positions. Team ids come from mlb_teams.
- **Params:** `date_range` (string, optional) — Prospect table period; `limit` (integer, optional) — Rows to return (1-100); `list_type` (string, optional) — Prospect pool; `min_pa` (integer, optional) — Minimum PA threshold; `offset` (integer, optional) — Zero-based row offset; `player_type` (string, optional) — Player table; `position` (string, optional) — Position filter; `q` (string, optional) — Case-insensitive player-name substring; `team_id` (string, optional) — Optional MLB team id; selects that team's prospect list and overrides list_type

### `mlb_schedule`

- **HTTP:** `GET /mlb/schedule`
- **What:** Get the MLB schedule and scores. Returns MLB games, teams, scores, status, probable pitchers, venue, and series information for one date or date range, optionally filtered to a team.
- **Params:** `date` (string, optional) — Single date in YYYY-MM-DD format; `end_date` (string, optional) — Range end in YYYY-MM-DD format; `game_type` (string, optional) — Game type; `start_date` (string, optional) — Range start in YYYY-MM-DD format; `team_id` (string, optional) — Numeric MLB team id

### `mlb_search`

- **HTTP:** `GET /mlb/search`
- **What:** Search MLB players, teams, and content topics. Returns the same anonymous MLB typeahead categories used by MLB.com: player suggestions, team suggestions, content topics, and search terms. Queries need at least three characters.
- **Params:** `q` (string, **required**) — Search text; 3-100 characters

### `mlb_standings`

- **HTTP:** `GET /mlb/standings`
- **What:** Get MLB standings. Returns American League and National League standings, including source-provided expected, home/away, last-ten, ranking, and elimination fields when available, using any supported standings type returned by mlb_discovery.
- **Params:** `date` (string, optional) — Snapshot date in YYYY-MM-DD format; returns standings as of that date; `season` (integer, optional) — Four-digit season; defaults to current year; `type` (string, optional) — Standings type

### `mlb_statcast`

- **HTTP:** `GET /mlb/statcast-leaders`
- **What:** Get Baseball Savant Statcast leaderboard data. Returns the standard anonymous Baseball Savant Statcast leaderboard for batters, pitchers, teams, or pitcher teams. Supports the page's season, team, batter position, minimum batted-ball event, and sortable metric filters, plus local pagination. Use mlb_discovery for exact filter sets. Other Baseball Savant leaderboard pages are listed there but are not represented by this route.
- **Params:** `limit` (integer, optional) — Rows per page (1-500); `min_bbe` (string, optional) — Minimum batted-ball event threshold; `offset` (integer, optional) — Zero-based row offset; `position` (string, optional) — Batter position; `sort` (string, optional) — Sort field; `sort_dir` (string, optional) — Sort direction; `team_id` (string, optional) — Optional MLB team id from mlb_teams; `type` (string, optional) — Leaderboard row type; `year` (integer, optional) — Season; current season back 11 seasons

### `mlb_statcast_abs_challenges`

- **HTTP:** `GET /mlb/statcast-abs-challenges`
- **What:** Get Baseball Savant ABS challenge rankings. Returns Baseball Savant's ABS challenge table with repeated season, game type, split, challenging-team, opponent-team, pitch-type, and shadow-zone filters, plus challenger type, level, thresholds, leverage, pitch location, breakeven, and split-year controls. Filter values are live-verified and listed by /mlb/discovery. The entire filtered table is returned; UI-only drawer details and client-side sorting are not separate source filters.
- **Params:** `ball_strike` (string, optional) — Pitch location; empty selects All; `breakeven` (string, optional) — Challenge breakeven band; empty selects All; `challenge_team_ids` (array, optional) — Challenging MLB team ids; `challenge_type` (string, optional) — Challenge board group; `data_count` (string, optional) — Challenge count or run value; `data_mode` (string, optional) — Challenges made or against; `game_types` (array, optional) — Game type codes; `level` (string, optional) — Competition level; `leverage` (string, optional) — Leverage bucket; empty selects All; `min_challenges` (string, optional) — Minimum challenges made; `min_opponent_challenges` (string, optional) — Minimum challenges against; `opponent_team_ids` (array, optional) — Opponent MLB team ids; `pitch_types` (array, optional) — Pitch type codes; `seasons` (array, optional) — Season values; `shadow_zones` (array, optional) — Shadow zone codes; `split_year` (string, optional) — Separate year groups; `splits` (array, optional) — Split dimensions

### `mlb_statcast_active_spin`

- **HTTP:** `GET /mlb/statcast-active-spin`
- **What:** Get Baseball Savant Active Spin rows. Returns pitcher Active Spin table rows for the selected season/calculation method, minimum pitch count, and throwing hand. Table sorting and pagination are applied locally. The player search only highlights pitchers in the first-party SVG visualization; the SVG chart and CSV download remain outside this JSON table contract.
- **Params:** `hand` (string, optional) — Pitcher throwing hand; omit for both; `limit` (integer, optional) — Rows per page (1-500); `min` (string, optional) — Minimum total pitches; `offset` (integer, optional) — Zero-based row offset; `sort` (string, optional) — Local table sort field; `sort_dir` (string, optional) — Sort direction; `year` (string, optional) — Season and calculation method

### `mlb_statcast_arm_angle`

- **HTTP:** `GET /mlb/statcast-arm-angle`
- **What:** Get Baseball Savant Pitcher Arm Angle rows. Returns Pitcher Arm Angle table rows and the matching MLB-average reference. Supports season, team, game type, pitch type, hand, batter side, pitch-count thresholds, date range, and up to four group-by selectors. Table sorting and pagination run locally. Visualization-only controls, animation, and CSV output are separate formats.
- **Params:** `bat_side` (string, optional) — Batter side; omit for both.; `date_end` (string, optional) — Inclusive end date, YYYY-MM-DD.; `date_start` (string, optional) — Inclusive start date, YYYY-MM-DD.; `game_types` (array, optional) — Game type codes; defaults to R.; `group_by` (array, optional) — Up to four grouping fields.; `limit` (integer, optional) — Rows per page (1-500).; `min` (string, optional) — Minimum total pitches; defaults to q.; `min_group_pitches` (string, optional) — Minimum pitches per group; defaults to 1.; `offset` (integer, optional) — Zero-based row offset (0-5000).; `pitch_hand` (string, optional) — Pitcher throwing hand; omit for both.; `pitch_types` (array, optional) — Pitch type codes; defaults to FF.; `seasons` (array, optional) — Seasons; at most three may be combined. Defaults to 2026.; `sort` (string, optional) — Local table sort field; defaults to arm_angle.; `sort_dir` (string, optional) — Local sort direction; defaults to asc.; `teams` (array, optional) — MLB team ids; omit for all teams.

### `mlb_statcast_arm_strength`

- **HTTP:** `GET /mlb/statcast-arm-strength`
- **What:** Get Baseball Savant Arm Strength leaderboard data. Returns the player or team Arm Strength leaderboard with verified year, team, position metric, minimum throws, local sort, and pagination filters. The player detail route returns individual throw records.
- **Params:** `limit` (integer, optional) — Rows per page (1-500); `min_throws` (string, optional) — Minimum throws; `offset` (integer, optional) — Zero-based row offset; `position` (string, optional) — Position metric; `sort` (string, optional) — Local sort field; `sort_dir` (string, optional) — Sort direction; `team_id` (string, optional) — MLB team id; `type` (string, optional) — Leaderboard row type; `year` (string, optional) — Season or all years

### `mlb_statcast_arm_strength_player`

- **HTTP:** `GET /mlb/statcast-arm-strength-player`
- **What:** Get Baseball Savant player throw details. Returns the player's individual Arm Strength throw records for a verified season or all years.
- **Params:** `player_id` (string, **required**) — Positive MLB player id; `year` (string, optional) — Season or all years

### `mlb_statcast_arm_value`

- **HTTP:** `GET /mlb/statcast-arm-value`
- **What:** Get Baseball Savant Extra Bases Run Value leaderboard data. Returns the Arm Value section's complete embedded table, including its Run, Fld, Pit, team, and league views, filters, local sorting, and pagination. Expanded player rows are available from mlb-statcast-arm-value-details. The JSON rows contain the same selected records as the upstream CSV export.
- **Params:** `end_year` (integer, optional) — End season, 2016 through current season; must be >= start_year; `game_type` (string, optional) — Game type; `key_base_out` (string, optional) — Baserunner situation; `limit` (integer, optional) — Rows per page (1-500); `minimum_opps` (string, optional) — Minimum opportunities; `offset` (integer, optional) — Zero-based row offset; `q` (string, optional) — Case- and accent-insensitive local substring on the displayed row name; up to 100 characters; `sort` (string, optional) — Local table sort field; `sort_dir` (string, optional) — Local sort direction; `split` (string, optional) — Return one row per season; `start_year` (integer, optional) — Start season, 2016 through current season; `team_id` (string, optional) — MLB team id from mlb_discovery, split for All Teams Split by Team, or empty for All Teams; `type` (string, optional) — Leaderboard view; `with_team_only` (string, optional) — Team-roster membership for a selected team

### `mlb_statcast_arm_value_details`

- **HTTP:** `GET /mlb/statcast-arm-value-details`
- **What:** Get expanded Baseball Savant Arm Value player plays. Returns the game-level play details displayed when expanding a Run, Fld, or Pit player row in the Arm Value leaderboard. Pass the leaderboard filters used to produce the selected row.
- **Params:** `end_year` (integer, optional) — End season, 2016 through current season; must be >= start_year; `entity_id` (string, **required**) — Positive player id from an Arm Value player row; `game_type` (string, optional) — Game type; `key_base_out` (string, optional) — Baserunner situation; `minimum_opps` (string, optional) — Minimum opportunities; `split` (string, optional) — Split leaderboard records by season; `start_year` (integer, optional) — Start season, 2016 through current season; `team_id` (string, optional) — MLB team id from mlb_discovery, split, or empty; `type` (string, optional) — Player view; `with_team_only` (string, optional) — Team-roster membership for a selected team

### `mlb_statcast_baserunning`

- **HTTP:** `GET /mlb/statcast-baserunning`
- **What:** Get Baseball Savant baserunning leaderboard tables. Returns Baseball Savant Baserunning Run Value, Basestealing, or Extra Bases Taken tables. All filter value sets were read from the live first-party controls; rows are embedded in the page response and searched, sorted, and paged locally. Use mlb_discovery.statcast_baserunning_filters for board-specific groups, thresholds, and sort fields. CSV and visual expansion modes are excluded; this returns the underlying JSON table rows.
- **Params:** `board` (string, **required**) — Baseball Savant table; `game_type` (string, optional) — Game scope; `key_base_out` (string, optional) — Extra Bases Taken situation; `limit` (integer, optional) — Rows per page, 1-500; `n` (string, optional) — Board-specific row threshold; `offset` (integer, optional) — Zero-based row offset; `pitch_hand` (string, optional) — Basestealing pitcher hand; `prior_pk` (string, optional) — Basestealing prior pickoffs; `runner_moved` (string, optional) — Basestealing runner outcome; `search` (string, optional) — Case-insensitive substring in the displayed player or team name; `season_end` (integer, optional) — Inclusive last season; `season_start` (integer, optional) — Inclusive first season; `sort` (string, optional) — Local sort field; accepted values depend on board; `sort_dir` (string, optional) — Local sort direction; `split` (string, optional) — Return separate year rows; `target_base` (string, optional) — Basestealing target base; `team` (string, optional) — MLB team id or split-team rows; `type` (string, optional) — Board group; accepted values depend on board; `with_team_only` (boolean, optional) — Restrict to selected team's active player rows; requires a specific team id

### `mlb_statcast_bat_tracking`

- **HTTP:** `GET /mlb/statcast-bat-tracking`
- **What:** Get Baseball Savant bat-tracking rows. Returns batter, batting-team, pitcher, pitching-team, or league bat-tracking rows with the live page's season, game type, swing threshold, date, side, contact, attack zone, team, pitch, count, and grouping filters. Use mlb_discovery for the same complete value sets. Multi-value filters are passed as repeated query parameters.
- **Params:** `attack_zone` (string, optional) — Attack zone; `bat_side` (string, optional) — Batter side; `contact_type` (string, optional) — Contact type; `counts` (array, optional) — One or more ball-strike counts; `date_end` (string, optional) — Optional date range end in YYYY-MM-DD; `date_start` (string, optional) — Optional date range start in YYYY-MM-DD; `game_type` (string, optional) — Game type; `group_by` (array, optional) — Up to four grouping columns; `is_hard_hit` (string, optional) — Hard-hit filter; `limit` (integer, optional) — Rows per page (1-500); `min_group_swings` (string, optional) — Minimum swings per grouped row; `min_swings` (string, optional) — Minimum swing qualifier; `offset` (integer, optional) — Zero-based row offset; `pitch_hand` (string, optional) — Pitcher hand; `pitch_types` (array, optional) — One or more pitch types; `season_end` (string, optional) — Last season; must be >= season_start; `season_start` (string, optional) — First season; `sort` (string, optional) — Local row sort field; `sort_dir` (string, optional) — Sort direction; `teams` (array, optional) — One or more MLB team ids; `type` (string, optional) — Table row type

### `mlb_statcast_batted_ball`

- **HTTP:** `GET /mlb/statcast-batted-ball`
- **What:** Get Baseball Savant Batted Ball Profile rows. Returns the Batted Ball Profile table for batters, batting teams, pitchers, pitching teams, or league totals. Supports first-party season, game type, split, team, date, side, hand, pitch type, event threshold, and split-group threshold filters. The All-Star A game type is accepted by the live page query although its checkbox is hidden. Sorting and pagination are local. The league-average reference row is returned separately when requested; CSV and visualization controls are outside this JSON contract.
- **Params:** `bat_side` (string, optional) — Batter side; `date_end` (string, optional) — YYYY-MM-DD date range end (2015-04-05 through today); `date_start` (string, optional) — YYYY-MM-DD date range start (2015-04-05 through today); `game_types` (array, optional) — One or more game type codes; `include_league_average` (boolean, optional) — Include the first-party league-average reference row; `limit` (integer, optional) — Rows per page (1-500); `min` (string, optional) — Minimum batted-ball events; `min_split` (string, optional) — Minimum rows per split group; `offset` (integer, optional) — Zero-based row offset; `pitch_hand` (string, optional) — Pitcher throwing hand; `pitch_types` (array, optional) — One or more pitch type codes; `seasons` (array, optional) — One or more seasons; `sort` (string, optional) — Local table sort field; `sort_dir` (string, optional) — Sort direction; `split_year` (string, optional) — Split seasons into separate rows; `splits` (array, optional) — One or more split dimensions; `teams` (array, optional) — One or more MLB team ids; `type` (string, optional) — Row type

### `mlb_statcast_birthday_index`

- **HTTP:** `GET /mlb/statcast-birthday-index`
- **What:** Get Baseball Savant Sarah Langs Birthday Index rows. Returns today's birthday tables for batters and pitchers plus the selected upcoming-birthday table. Type and minimum-games are first-party filters; date must fall inside the live page's season date range. The active-player toggle, sorting, and pagination are applied locally. The MLB Terms of Use notes a private, non-commercial-use boundary and restrictions on redistribution; this endpoint exposes statistical rows only and excludes media, graphics, and CSV.
- **Params:** `date` (string, optional) — Optional birthday date in M-D form; accepted dates are bounded by the current live page season window; `limit` (integer, optional) — Rows per page (1-500); `min_games` (string, optional) — Minimum games played on the birthday; `offset` (integer, optional) — Zero-based row offset (0-5000); `show_inactives` (boolean, optional) — Include inactive and deceased players in upcoming rows; `sort` (string, optional) — Local sort column. Some values are type- or date-specific and invalid combinations are rejected.; `sort_dir` (string, optional) — Local sort direction; omitted values use the selected column's live first-party initial direction; `type` (string, optional) — Upcoming table

### `mlb_statcast_catcher_blocking`

- **HTTP:** `GET /mlb/statcast-catcher-blocking`
- **What:** Get Baseball Savant Catcher Blocking leaderboard rows. Returns catcher, pitcher, catching-team, or league Catcher Blocking rows. Filters cover game type, season range, minimum opportunities, team/stint, and local table sorting. Use mlb_discovery for the exact filter sets. Row detail events are available from mlb-statcast-catcher-blocking-details; chart playback and CSV export controls are not data rows.
- **Params:** `end_year` (integer, optional) — Last season, start_year through current season; `game_type` (string, optional) — Game type; `limit` (integer, optional) — Rows per page (1-500); `min` (string, optional) — Minimum opportunities; applies to Cat and Pit; `offset` (integer, optional) — Zero-based row offset; `sort` (string, optional) — Local sort field from mlb_discovery; `sort_dir` (string, optional) — Local sort direction; `split` (string, optional) — Split rows by season; `start_year` (integer, optional) — First season, 2018 through current season; `team` (string, optional) — Optional team filter: split or an MLB team id from mlb_discovery; `type` (string, optional) — Leaderboard group; `with_team_only` (boolean, optional) — For a specific Cat or Pit team, include only rows for that team; defaults true

### `mlb_statcast_catcher_blocking_details`

- **HTTP:** `GET /mlb/statcast-catcher-blocking-details`
- **What:** Get Baseball Savant Catcher Blocking play details. Expands a Catcher Blocking Cat, Pit, or Pitching Team table row into paginated play-location events. entity_id must come from the matching leaderboard rows and other filters must match that row query. League rows have no detail feed.
- **Params:** `end_year` (integer, optional) — Last season, start_year through current season; `entity_id` (string, **required**) — Entity id from a Cat, Pit, or Pitching Team leaderboard row; `game_type` (string, optional) — Game type; `limit` (integer, optional) — Rows per page (1-500); `offset` (integer, optional) — Zero-based row offset; `split` (string, optional) — Split details by season; `start_year` (integer, optional) — First season, 2018 through current season; `team` (string, optional) — Optional team id or split selector from mlb_discovery; `type` (string, optional) — Row group; `with_team_only` (boolean, optional) — For a specific Cat or Pit team, include only rows for that team; defaults true

### `mlb_statcast_catcher_framing`

- **HTTP:** `GET /mlb/statcast-catcher-framing`
- **What:** Get Baseball Savant Catcher Framing leaderboard rows. Returns the Catcher Framing table for catcher, catching-team, batter, batting-team, pitcher, or league groups. Supports observed game, season, one-team, pitch/result minimum, date, bat-side, pitch-hand, pitch-type, ball/strike, and call-model filters, plus local sort and pagination. Use mlb_discovery for exact enum values; chart-only groupings and player comparison controls are excluded.
- **Params:** `ball_strike` (string, optional) — Pitch location relative to strike zone; `bat_side` (string, optional) — Batter side; `call` (string, optional) — Framing model; `date_end` (string, optional) — Inclusive end date; `date_start` (string, optional) — Inclusive start date; `game_type` (string, optional) — Game type; `limit` (integer, optional) — Rows per page (1-500); `min_pitches` (string, optional) — Minimum pitches; `min_results` (integer, optional) — Minimum results; `offset` (integer, optional) — Zero-based row offset; `pitch_hand` (string, optional) — Pitcher hand; `pitch_type` (string, optional) — Single pitch type; `season_end` (integer, optional) — Last season; `season_start` (integer, optional) — First season; `sort` (string, optional) — Local sort field; `sort_dir` (string, optional) — Local sort direction; `team` (string, optional) — Optional single MLB team id; `type` (string, optional) — Table group

### `mlb_statcast_catcher_framing_details`

- **HTTP:** `GET /mlb/statcast-catcher-framing-details`
- **What:** Get Baseball Savant Catcher Framing pitch-event details. Returns paginated pitch events for a Catcher Framing entity_id. Repeat the leaderboard filters used to obtain the entity; league aggregate rows have no detail feed. The upstream detail response may be large, so use limit and offset.
- **Params:** `ball_strike` (string, optional) — Pitch location relative to strike zone; `bat_side` (string, optional) — Batter side; `call` (string, optional) — Framing model; `date_end` (string, optional) — Inclusive end date; `date_start` (string, optional) — Inclusive start date; `entity_id` (string, **required**) — Entity id from a Catcher Framing leaderboard row; `game_type` (string, optional) — Game type; `limit` (integer, optional) — Rows per page (1-500); `min_pitches` (string, optional) — Minimum pitches; `min_results` (integer, optional) — Minimum results; `offset` (integer, optional) — Zero-based row offset; `pitch_hand` (string, optional) — Pitcher hand; `pitch_type` (string, optional) — Single pitch type; `season_end` (integer, optional) — Last season; `season_start` (integer, optional) — First season; `team` (string, optional) — Optional single MLB team id; `type` (string, optional) — Table group; league details are unavailable

### `mlb_statcast_catcher_pop_time`

- **HTTP:** `GET /mlb/statcast-catcher-pop-time`
- **What:** Get Baseball Savant Catcher Pop Time leaderboard. Returns catchers ranked by pop-time metrics, filtered by season, team, and minimum steal attempts to second or third. Sort and pagination are applied locally.
- **Params:** `limit` (integer, optional) — Rows to return (1-500); `min2b` (string, optional) — Minimum attempts to second base; `min3b` (string, optional) — Minimum attempts to third base; `offset` (integer, optional) — Zero-based offset; `sort` (string, optional) — Sort field from mlb_discovery; `sort_dir` (string, optional) — Sort direction; `team_id` (string, optional) — MLB team id; `year` (string, optional) — Season from 2015 through 2026

### `mlb_statcast_catcher_stance`

- **HTTP:** `GET /mlb/statcast-catcher-stance`
- **What:** Get Baseball Savant Catcher Stance rows. Returns the public Catcher Stance table for catchers, catching teams, batters, batting teams, pitchers, or league totals. Supports the live year, game, date, threshold, team, pitch type, batter/pitcher hand, knee posture, grouping, sorting, and pagination controls. Grouping accepts up to four values. Use mlb_discovery for exact value sets. Chart series and page-local search/column toggles are not included.
- **Params:** `bat_side` (string, optional) — Batter side; omit for all; `date_end` (string, optional) — End date YYYY-MM-DD; `date_start` (string, optional) — Start date YYYY-MM-DD; `game_type` (string, optional) — Game type; `group_by` (array, optional) — Up to four grouping dimensions; none disables grouping; `knee_code` (string, optional) — Knee posture; `limit` (integer, optional) — Rows per page (1-500); `min_pitches` (string, optional) — Minimum pitches; `min_results` (string, optional) — Minimum results; `offset` (integer, optional) — Zero-based row offset; `pitch_hand` (string, optional) — Pitcher hand; omit for all; `pitch_types` (array, optional) — One or more pitch types; `season_end` (string, optional) — Last season; must be >= season_start; `season_start` (string, optional) — First season; `sort` (string, optional) — Local row sort field; `sort_dir` (string, optional) — Sort direction; `teams` (array, optional) — One or more MLB team ids; `type` (string, optional) — Table entity type

### `mlb_statcast_catcher_throwing`

- **HTTP:** `GET /mlb/statcast-catcher-throwing`
- **What:** Get Baseball Savant Catcher Throwing leaderboard rows. Returns catcher, catching-team, or league caught-stealing and throw-quality rows with the public season, game, attempt-threshold, target-base, split-years, team, and roster-membership filters. Table sorting and pagination are applied locally. Catcher rows can be expanded with mlb-statcast-catcher-throwing-details. CSV, charts, and page-local display controls are excluded.
- **Params:** `game_type` (string, optional) — Game type; `limit` (integer, optional) — Rows per page (1-500); `minimum` (string, optional) — Minimum steal attempts; `offset` (integer, optional) — Zero-based row offset; `season_end` (string, optional) — Last season; must be >= season_start; `season_start` (string, optional) — First season; `sort` (string, optional) — Local sort field; `sort_dir` (string, optional) — Local sort direction; `split` (string, optional) — Split results by season; `target_base` (string, optional) — Throw target; `team` (string, optional) — Empty for all teams, split for team stints, or an MLB team id; `type` (string, optional) — Table group; `with_team_only` (boolean, optional) — For a selected team, include only catchers on that team

### `mlb_statcast_catcher_throwing_details`

- **HTTP:** `GET /mlb/statcast-catcher-throwing-details`
- **What:** Get Catcher Throwing attempt details. Returns per-attempt play records expanded from a Catcher Throwing catcher row. Supply the entity_id from a Cat row and the row's year/team when it represents a season or team stint. Details are ungrouped source attempts, paginated locally.
- **Params:** `entity_id` (integer, **required**) — Positive catcher id from a Cat row; `game_type` (string, optional) — Game type; `limit` (integer, optional) — Rows per page (1-500); `minimum` (string, optional) — Minimum steal attempts; `offset` (integer, optional) — Zero-based row offset; `split` (string, optional) — Split rows by season; `target_base` (string, optional) — Throw target; `team` (string, optional) — Empty, split, or team id from the corresponding leaderboard row; `with_team_only` (boolean, optional) — Team roster membership filter; `year` (integer, optional) — Season

### `mlb_statcast_expected`

- **HTTP:** `GET /mlb/statcast-expected`
- **What:** Get Baseball Savant Expected Statistics. Returns the separate Expected Statistics leaderboard with batter, pitcher, and team views; season, team, batter-position, BIP/PA qualifier and threshold filters; local metric sorting; and pagination. League-average values are returned separately.
- **Params:** `filter_type` (string, optional) — Minimum qualifier type; `limit` (integer, optional) — Rows per page (1-500); `minimum` (string, optional) — Minimum BIP/PA threshold; `offset` (integer, optional) — Zero-based row offset; `position` (string, optional) — Batter position; only supported for type=batter; `sort` (string, optional) — Sort field; `sort_dir` (string, optional) — Sort direction; `team_id` (string, optional) — Optional MLB team id from mlb_teams; `type` (string, optional) — Leaderboard view; `year` (integer, optional) — Season from 2015 through the current season

### `mlb_statcast_fielding_run_value`

- **HTTP:** `GET /mlb/statcast-fielding-run-value`
- **What:** Get Baseball Savant Fielding Run Value rows. Returns fielding run value for fielder, fielding-team, batter, batting-team, or pitcher views. Dates and grouping dimensions follow the first-party leaderboard. Minimum 0.1 is available only for fielder and fielding-team views; the batting/pitching views omit it. Sorting and pagination are applied locally. CSV and player-page visualizations are outside this table contract.
- **Params:** `date_end` (string, optional) — End date, YYYY-MM-DD, from 2018-03-29 through today; `date_start` (string, optional) — Start date, YYYY-MM-DD, from 2018-03-29 through today; `game_type` (string, optional) — Game type; `group_by` (array, optional) — Repeated split dimensions; `limit` (integer, optional) — Rows per page (1-500); `minimum` (string, optional) — Total minimum; 0.1 only for fielder and fielding-team; `minimum_split` (string, optional) — Minimum within each split; 0.1 only for fielder and fielding-team; `offset` (integer, optional) — Zero-based row offset (0-5000); `position` (string, optional) — Position / position group; `season_end` (string, optional) — Last season; must be >= season_start; `season_start` (string, optional) — First season; `sort` (string, optional) — Local sort field; `sort_dir` (string, optional) — Local sort direction; `team_id` (array, optional) — Repeated MLB team ids; `type` (string, optional) — Table type

### `mlb_statcast_first_base_receiving`

- **HTTP:** `GET /mlb/statcast-first-base-receiving`
- **What:** Get Baseball Savant First Base Receiving leaderboards. Returns first baseman, throwing fielder, fielding team, batting team, or league receiving rows. Includes season/game selections, threshold and group filters, team/date/hand/height/outcome filters, and validated page-local split filters and sorting. Per-play source records are available through mlb-statcast-first-base-receiving-details. 3D trajectory visualizations are not included.
- **Params:** `bin_time_X10[]` (array, optional) — Time bins; `dateEnd` (string, optional) — Inclusive end date (YYYY-MM-DD); `dateStart` (string, optional) — Inclusive start date (YYYY-MM-DD); `fielder_3_hand` (string, optional) — First baseman batting hand; `gameType[]` (array, optional) — Game types; `is_hit_into_play_field_out` (string, optional) — Field-out flag; `limit` (integer, optional) — Rows per page, 1-500; `min` (string, optional) — Minimum opportunities; `minSplit` (string, optional) — Minimum opportunities within each group; `min_height_in_inches` (string, optional) — Minimum fielder height, inches; `offset` (integer, optional) — Zero-based row offset; `runners_on_cd[]` (array, optional) — Base occupancy codes; `season[]` (array, optional) — Season values; `sortColumn` (string, optional) — Local sort field; `sortDirection` (string, optional) — Local sort direction; `splitYear` (string, optional) — Year split selector; `split[]` (array, optional) — Group dimensions; `team[]` (array, optional) — MLB team ids; `throw_height_code[]` (array, optional) — Throw heights; `throw_location_code_full[]` (array, optional) — Throw outcomes; `throw_pos_id[]` (array, optional) — Throwing position ids; `type` (string, optional) — Leaderboard group

### `mlb_statcast_first_base_receiving_details`

- **HTTP:** `GET /mlb/statcast-first-base-receiving-details`
- **What:** Get a player's First Base Receiving play records. Returns per-play records backing an individual first-base receiving leaderboard row, including game/play ids, outcome codes, receiving OAA, expected out rate, timing, and field coordinates. This is tabular JSON; the separate 3D skeletal visualization route is excluded.
- **Params:** `bin_time_X10[]` (array, optional) — Time bins; `dateEnd` (string, optional) — Inclusive end date (YYYY-MM-DD); `dateStart` (string, optional) — Inclusive start date (YYYY-MM-DD); `fielder_3_hand` (string, optional) — First baseman batting hand; `gameType[]` (array, optional) — Game types; `is_hit_into_play_field_out` (string, optional) — Field-out flag; `limit` (integer, optional) — Rows per page, 1-500; `min` (string, optional) — Minimum opportunities; `minSplit` (string, optional) — Grouped opportunity threshold; `min_height_in_inches` (string, optional) — Minimum fielder height; `offset` (integer, optional) — Zero-based row offset; `player_id` (integer, **required**) — Positive MLB player id; `runners_on_cd[]` (array, optional) — Base occupancy codes; `season[]` (array, optional) — Season values; `splitYear` (string, optional) — Year split selector; `split[]` (array, optional) — Group dimensions; `team[]` (array, optional) — MLB team ids; `throw_height_code[]` (array, optional) — Throw heights; `throw_location_code_full[]` (array, optional) — Throw outcomes; `throw_pos_id[]` (array, optional) — Throwing position ids; `type` (string, optional) — Leaderboard group

### `mlb_statcast_home_runs`

- **HTTP:** `GET /mlb/statcast-home-runs`
- **What:** Get Baseball Savant Home Runs Tracking. Returns Batter or Pitcher Home Runs Tracking rows. Year, team id, minimum home runs, and Standard/Adjusted mode are first-party filters. The first-party table sorts client-side; this endpoint applies a named local sort and pagination. Use mlb_discovery for the exact filter sets. Per-player home-run plays are available from mlb-statcast-home-runs-details; trajectory images, video media, and CSV downloads are separate representations.
- **Params:** `cat` (string, optional) — Trajectory mode; `limit` (integer, optional) — Rows per page (1-500); `min` (string, optional) — Minimum home run total; `offset` (integer, optional) — Zero-based row offset; `player_type` (string, optional) — Table type; `sort` (string, optional) — Local sort column; `sort_dir` (string, optional) — Local sort direction; `team` (string, optional) — MLB team id; blank selects all teams; `year` (string, optional) — Season

### `mlb_statcast_home_runs_details`

- **HTTP:** `GET /mlb/statcast-home-runs-details`
- **What:** Get Baseball Savant Home Runs play details. Returns the home-run plays expanded from one batter or pitcher leaderboard row, with event measurements and park outcomes. Provide the exact player id, player type, year, and mode from the row. Play identifiers and source links are returned; trajectory images, video media, and CSV output are not included.
- **Params:** `cat` (string, optional) — Trajectory mode; `limit` (integer, optional) — Rows per page (1-500); `offset` (integer, optional) — Zero-based row offset; `player_id` (string, **required**) — Positive MLB player id from mlb-statcast-home-runs; `player_type` (string, optional) — Table type; `year` (string, optional) — Season

### `mlb_statcast_oaa`

- **HTTP:** `GET /mlb/statcast-oaa`
- **What:** Get Baseball Savant Outs Above Average. Returns the separate Outs Above Average leaderboard for fielders, fielding teams, batters, batting teams, or pitchers. Supports season range, split years, team, monthly range, attempts, position, detailed fielder roles, local sorting, and pagination.
- **Params:** `end_year` (integer, optional) — End season from 2016 through the current season; `limit` (integer, optional) — Rows per page (1-500); `minimum` (string, optional) — Minimum attempts; `offset` (integer, optional) — Zero-based row offset; `position` (string, optional) — Position filter; `range` (string, optional) — Time range; `roles` (string, optional) — Comma-separated detailed fielder role ids. Values: 32,30,31,77,71,70,72,78,43,42,40,41,46,87,81,82,89,64,62,60,61,98,91,90,92,99,51,50,52; `sort` (string, optional) — Sort field; `sort_dir` (string, optional) — Sort direction; `split` (string, optional) — Return one row per season in a year range; `start_year` (integer, optional) — Start season from 2016 through the current season; `team_id` (string, optional) — Optional MLB team id from mlb_teams; `type` (string, optional) — Leaderboard view

### `mlb_statcast_park_factors`

- **HTTP:** `GET /mlb/statcast-park-factors`
- **What:** Get Baseball Savant Statcast Park Factors rows. Returns season, venue, distance, distance-all, raw, or dimensions rows from Baseball Savant. Query filters are conditional on type and are live-echo validated; local sorting and pagination are applied to returned rows. The fence-stat and allDiffs controls only change display columns and do not change row data; CSV and linked venue detail pages are separate surfaces.
- **Params:** `bat_side` (string, optional) — Optional batter side for year, venue, or raw mode; `condition` (string, optional) — Park condition for year and venue modes; `limit` (integer, optional) — Rows per page (1-500); `offset` (integer, optional) — Zero-based row offset; `parks` (string, optional) — Park population selector; `rolling` (string, optional) — Rolling year count for year and venue modes; `sort` (string, optional) — Local row field present in the selected mode's data; `sort_dir` (string, optional) — Local sort direction; `stat` (string, optional) — Venue mode metric; `type` (string, optional) — Park Factors table mode; `year` (string, optional) — Mode-specific season; see endpoint markdown and mlb_discovery for exact values

### `mlb_statcast_percentile`

- **HTTP:** `GET /mlb/statcast-percentile`
- **What:** Get Baseball Savant Percentile Rankings. Returns batter or pitcher percentile rankings. Type, season, and team are first-party table filters. Repeated pctl filters, table sorting, and pagination are applied locally to the embedded rows. Use mlb_discovery for exact type-specific fields, comparators, seasons, and team ids. CSV is a separate download.
- **Params:** `limit` (integer, optional) — Rows per page (1-500); `offset` (integer, optional) — Zero-based row offset; `pctl` (array, optional) — Repeated field-comparator-value filter from the type-specific field set in mlb_discovery; value range 0-100; `sort` (string, optional) — Local sort field from the type-specific set in mlb_discovery; `sort_dir` (string, optional) — Local sort direction; `team` (string, optional) — MLB team id; blank selects all teams; `type` (string, optional) — Table type; `year` (string, optional) — Season

### `mlb_statcast_pitch_arsenal`

- **HTTP:** `GET /mlb/statcast-pitch-arsenal`
- **What:** Get Baseball Savant Pitch Arsenal Stats. Returns pitcher or batter pitch-level arsenal leaderboards. Season, team, pitch type, minimum PA, and minimum-pitch qualification filters are replayed against the anonymous first-party table; sorting and pagination are applied locally. Use mlb_discovery for the full selector set. Player rows can be expanded with mlb-statcast-pitch-arsenal-details.
- **Params:** `limit` (integer, optional) — Rows per page (1-500); `min_pa` (string, optional) — Minimum plate appearances; `min_pitches` (string, optional) — Minimum pitches; q means qualified; `offset` (integer, optional) — Zero-based row offset; `pitch_type` (string, optional) — Pitch code; blank means all pitch types; `sort` (string, optional) — Local sort field; `sort_dir` (string, optional) — Local sort direction; `team_id` (string, optional) — MLB team id from mlb_teams; `type` (string, optional) — Row type; `year` (string, optional) — Season

### `mlb_statcast_pitch_arsenal_details`

- **HTTP:** `GET /mlb/statcast-pitch-arsenal-details`
- **What:** Get Baseball Savant Pitch Arsenal play details. Returns game-level pitches expanded from one batter or pitcher pitch-arsenal row. Supply player_id, player_type, year, and the row's pitch_type. The upstream's min_ab request parameter is ignored, so it is not exposed. Rows include play_id values used by Baseball Savant's video pages; this endpoint returns play data and identifiers, not video media.
- **Params:** `limit` (integer, optional) — Rows per page (1-500); `offset` (integer, optional) — Zero-based row offset; `pitch_type` (string, **required**) — Pitch type from the selected row; `player_id` (string, **required**) — Positive MLB player id from mlb-statcast-pitch-arsenal; `player_type` (string, optional) — Row type; `year` (string, optional) — Season

### `mlb_statcast_pitch_arsenals`

- **HTTP:** `GET /mlb/statcast-pitch-arsenals`
- **What:** Get Baseball Savant Pitch Arsenals. Returns pitcher pitch speed, percentage, or spin rankings by pitch class. Year, minimum-pitch threshold, and hand are first-party filters. Team filtering and table sorting are applied locally because the page JavaScript applies them after receiving the embedded rows. Use mlb_discovery for exact values. CSV and pitch movement visualizations remain separate representations.
- **Params:** `hand` (string, optional) — Throwing hand; omit for all pitchers; `limit` (integer, optional) — Rows per page (1-500); `min_pitches` (string, optional) — Minimum pitches; `offset` (integer, optional) — Zero-based row offset; `sort` (string, optional) — Local sort column; `sort_dir` (string, optional) — Local sort direction; `team` (string, optional) — Current MLB team abbreviation; applied locally; `type` (string, optional) — Metric; `year` (string, optional) — Season

### `mlb_statcast_pitch_movement`

- **HTTP:** `GET /mlb/statcast-pitch-movement`
- **What:** Get Baseball Savant Pitch Movement rows. Returns pitcher-level pitch movement table rows for the selected season, pitch type, throwing hand, and minimum pitch count. Sorting and pagination are applied locally. The page's X/Z visualization axes and CSV download are separate presentation formats and are not returned by this JSON table contract.
- **Params:** `hand` (string, optional) — Pitcher throwing hand; omit for both; `limit` (integer, optional) — Rows per page (1-500); `min` (string, optional) — Minimum pitch count; `offset` (integer, optional) — Zero-based row offset; `pitch_type` (string, optional) — Pitch class; `sort` (string, optional) — Local table sort field; `sort_dir` (string, optional) — Sort direction; `year` (string, optional) — Season

### `mlb_statcast_pitch_tempo`

- **HTTP:** `GET /mlb/statcast-pitch-tempo`
- **What:** Get Baseball Savant Pitch Tempo rows. Returns pitcher, batter, pitching-team, batting-team, or league tempo rows. Season, game type, minimum pitch, team, year comparison, and team membership options mirror the live first-party controls; q and sorting are applied locally before pagination. Use mlb_discovery for exact value sets.
- **Params:** `game_type` (string, optional) — Game type; `limit` (integer, optional) — Rows per page (1-500); `n` (string, optional) — Minimum pitch count; `offset` (integer, optional) — Zero-based row offset; `q` (string, optional) — Case-insensitive local entity-name filter; `season_end` (string, optional) — Last season; must be >= season_start; `season_start` (string, optional) — First season; `sort` (string, optional) — Local sort field; `sort_dir` (string, optional) — Sort direction; `split` (string, optional) — Compare seasons separately; `team` (string, optional) — Optional MLB team id; `type` (string, optional) — Table group; `with_team_only` (string, optional) — Team membership mode; requires team

### `mlb_statcast_pitch_tempo_player`

- **HTTP:** `GET /mlb/statcast-pitch-tempo-player`
- **What:** Get a player's Pitch Tempo detail rows. Returns game-level time buckets for the selected pitcher or batter. Use entity_id from an mlb_statcast_pitch_tempo result.
- **Params:** `entity_id` (string, **required**) — Numeric entity id from a Pitch Tempo row; `game_type` (string, optional) — Game type; `season_end` (string, optional) — Last season; must be >= season_start; `season_start` (string, optional) — First season; `type` (string, optional) — Entity type

### `mlb_statcast_pitch_timer`

- **HTTP:** `GET /mlb/statcast-pitch-timer`
- **What:** Get Baseball Savant Pitch Timer infraction rows. Returns the Pitch Timer Infractions table for pitchers, batters, catchers, teams, or opposing teams. Filters for type, season, minimum pitches, and zero-infraction rows are upstream-backed; entity search, table sorting, and pagination are applied locally. The chart ordering is included as view metadata; the endpoint returns table rows, not the SVG chart.
- **Params:** `chart_sort` (string, optional) — Chart ordering metadata; `include_zeroes` (string, optional) — Include entities without infractions; `limit` (integer, optional) — Rows per page (1-500); `min_pitches` (string, optional) — Minimum pitches; `offset` (integer, optional) — Zero-based row offset; `q` (string, optional) — Local case-insensitive entity-name substring filter; `season` (string, optional) — Season; `sort` (string, optional) — Local table sort field; `sort_dir` (string, optional) — Sort direction; `type` (string, optional) — Entity group

### `mlb_statcast_player_details`

- **HTTP:** `GET /mlb/statcast-player-details`
- **What:** Get expanded standard Baseball Savant Statcast player plays. Returns the game-level pitch or batted-ball rows shown when expanding a batter or pitcher row in the standard Statcast leaderboard, including matchup, date, event, exit velocity, launch angle, distance, play id, and video availability.
- **Params:** `player_id` (string, **required**) — Positive MLB player id from a batter or pitcher row; `player_type` (string, optional) — Player row type; `year` (integer, optional) — Season from 2015 through the current season

### `mlb_statcast_rolling`

- **HTTP:** `GET /mlb/statcast-rolling`
- **What:** Get Baseball Savant Rolling Windows rows. Returns the six embedded Batter/Pitcher rolling-window tables, filtered by metric, role, and plate-appearance window. Each group is sorted by the selected metric delta in the same direction as the first-party page and paginated independently. The upstream page has no season, team, or game-type filters.
- **Params:** `limit` (integer, optional) — Rows per group (1-500); `metric` (string, optional) — Displayed metric; `offset` (integer, optional) — Zero-based row offset per group (0-5000); `role` (string, optional) — Optional player role; omit for both; `window_pa` (string, optional) — Optional rolling plate-appearance window; omit for all

### `mlb_statcast_run_value`

- **HTTP:** `GET /mlb/statcast-run-value`
- **What:** Get Baseball Savant Run Value rows. Returns batting or pitching Run Value rows from the Swing-Take leaderboard. Filters are cold-replay verified; sorting and pagination are applied locally. The Bat-side R/L selector was verified to leave the embedded rows byte-identical and is omitted. The page's visual charts and CSV export are separate formats.
- **Params:** `group` (string, optional) — Row group; `leverage` (string, optional) — Run-value method; `limit` (integer, optional) — Rows per page (1-500); `min` (string, optional) — Minimum plate appearances; `offset` (integer, optional) — Zero-based row offset; `sort` (string, optional) — Local table sort field; supported set varies by view; `sort_dir` (string, optional) — Sort direction; `sub_type` (string, optional) — Conditional subtype: Swing/Take; pitch name; or Heart/Shadow/Chase/Waste; `team` (string, optional) — MLB numeric team id; omit for all teams; `type` (string, optional) — Table view; `year` (string, optional) — Season, All, or Career

### `mlb_statcast_running_game`

- **HTTP:** `GET /mlb/statcast-running-game`
- **What:** Get Baseball Savant Running Game leaderboards. Returns the Running Game table for pitchers, pitching teams, or league. Season/game, hand, runner movement, target base, prior pickoff count, minimum opportunities, team, and team-stint controls are live-verified; named sorting, player/team search, and pagination are applied locally. Per-play records are available from mlb-statcast-running-game-details. The expanded-column toggle returns the same source fields, and the first-party CSV download is not a separate JSON response mode.
- **Params:** `game_type` (string, optional) — Game scope; `limit` (integer, optional) — Rows per page, 1-500; `n` (string, optional) — Minimum pitcher opportunities; `offset` (integer, optional) — Zero-based row offset; `pitch_hand` (string, optional) — Pitcher's throwing hand; `prior_pk` (string, optional) — Prior pickoff/disengagement count; `runner_moved` (string, optional) — Runner movement outcome; `search` (string, optional) — Case-insensitive substring of the displayed player or team name; `season_end` (integer, optional) — Inclusive last season; `season_start` (integer, optional) — Inclusive first season; `sort` (string, optional) — Local table sort field; `sort_dir` (string, optional) — Local sort direction; `split` (string, optional) — Return separate year rows; `target_base` (string, optional) — Target base; `team` (string, optional) — MLB team id, or split team stints; `type` (string, optional) — Leaderboard group; `with_team_only` (boolean, optional) — Restrict pitcher rows to the selected team; only valid with one specific team id

### `mlb_statcast_running_game_details`

- **HTTP:** `GET /mlb/statcast-running-game-details`
- **What:** Get Baseball Savant Running Game play details. Returns individual attempted-running plays expanded from a pitcher or pitching-team Running Game row. Pass its entity_id and repeat the same table filters. For team-stint rows, pass that row's team id; League rows do not expose a detail feed.
- **Params:** `entity_id` (integer, **required**) — Positive player or team entity id from the Running Game leaderboard; `game_type` (string, optional) — Game scope; `limit` (integer, optional) — Play rows per page, 1-500; `n` (string, optional) — Minimum pitcher opportunities; `offset` (integer, optional) — Zero-based play-row offset; `pitch_hand` (string, optional) — Pitcher's throwing hand; `prior_pk` (string, optional) — Prior pickoff/disengagement count; `runner_moved` (string, optional) — Runner movement outcome; `season_end` (integer, optional) — Inclusive last season; `season_start` (integer, optional) — Inclusive first season; `split` (string, optional) — Return separate year rows; `target_base` (string, optional) — Target base; `team` (string, optional) — One MLB team id; use the row's team id for split-team rows; `type` (string, optional) — Detail group; `with_team_only` (boolean, optional) — Restrict player rows to selected team; only valid with a specific team and Pit type

### `mlb_statcast_sprint_speed`

- **HTTP:** `GET /mlb/statcast-sprint-speed`
- **What:** Get Baseball Savant Sprint Speed player rows. Returns player Sprint Speed rows from the Baseball Savant leaderboard. The source filters season range, position, and minimum competitive runs; team filtering and sorting are applied locally. Use mlb_discovery for every closed value set.
- **Params:** `limit` (integer, optional) — Rows per page (1-500); `max_season` (string, optional) — Last season; must be >= min_season; `min_season` (string, optional) — First season; `minimum_runs` (string, optional) — Minimum competitive runs; `offset` (integer, optional) — Zero-based row offset; `position` (string, optional) — Position code; omitted is All Positions; `sort` (string, optional) — Local sort field; `sort_dir` (string, optional) — Sort direction; `team_id` (string, optional) — MLB team id

### `mlb_statcast_sprint_speed_teams`

- **HTTP:** `GET /mlb/statcast-sprint-speed-teams`
- **What:** Get Baseball Savant Sprint Speed team rows. Returns team-level Sprint Speed rows. Season is selected upstream; team filtering and sorting are applied locally because the first-party page embeds every team before its client-side filter. Use mlb_discovery for all accepted seasons, teams, and sort fields.
- **Params:** `limit` (integer, optional) — Rows per page (1-500); `offset` (integer, optional) — Zero-based row offset; `season` (string, optional) — Season or all seasons; `sort` (string, optional) — Local sort field; `sort_dir` (string, optional) — Sort direction; `team` (string, optional) — Optional first-party team selector abbreviation

### `mlb_statcast_swing_path`

- **HTTP:** `GET /mlb/statcast-swing-path`
- **What:** Get Baseball Savant Swing Path and Attack Angle rows. Returns batter, batting-team, or league Swing Path and Attack Angle rows with the first-party season, game, swing, team, date, side, contact, hard-hit, attack-zone, and pitcher-hand filters. Use mlb_discovery for exact values.
- **Params:** `attack_zone` (string, optional) — Attack zone; `bat_side` (string, optional) — Batter side; `contact_type` (string, optional) — Contact type; `date_end` (string, optional) — Optional range end in YYYY-MM-DD; `date_start` (string, optional) — Optional range start in YYYY-MM-DD; `game_type` (string, optional) — Game type; `is_hard_hit` (string, optional) — Hard-hit filter; `limit` (integer, optional) — Rows per page (1-500); `min_group_swings` (string, optional) — Minimum swings per group; `min_swings` (string, optional) — Minimum swing threshold; `offset` (integer, optional) — Zero-based row offset; `pitch_hand` (string, optional) — Pitcher hand; `season_end` (string, optional) — Last season; must be >= season_start; `season_start` (string, optional) — First season; `sort` (string, optional) — Local sort field; `sort_dir` (string, optional) — Sort direction; `team_id` (string, optional) — Optional MLB team id; `type` (string, optional) — Row type

### `mlb_statcast_swing_timing`

- **HTTP:** `GET /mlb/statcast-swing-timing`
- **What:** Get Baseball Savant Swing Timing and Miss Distance rows. Returns batter, batting-team, pitcher, pitching-team, or league rows with the page's season, game type, pitch-group, split, team, date, swing, contact, zone, pitch hand/type, count, timing-axis, and timing-flag filters. Sorting is local. Use mlb_discovery for exact values.
- **Params:** `attack_zone` (string, optional) — Attack zone; `bat_side` (string, optional) — Batter side; `contact_type` (string, optional) — Contact type; `counts` (array, optional) — One or more ball-strike counts; `date_end` (string, optional) — Optional range end in YYYY-MM-DD; `date_start` (string, optional) — Optional range start in YYYY-MM-DD; `flags` (array, optional) — Positive timing flags; `game_types` (array, optional) — One or more game types; `limit` (integer, optional) — Rows per page (1-500); `min_split` (string, optional) — Minimum swings per split group; `min_swings` (string, optional) — Minimum swing threshold; `not_flags` (array, optional) — Excluded timing flags; `offset` (integer, optional) — Zero-based row offset; `pitch_hand` (string, optional) — Pitcher hand; `pitch_types` (array, optional) — One or more pitch type codes; `seasons` (array, optional) — One or more seasons; `sort` (string, optional) — Local sort field; `sort_dir` (string, optional) — Sort direction; `split_year` (string, optional) — Split years into separate rows; `splits` (array, optional) — One or more split dimensions; `swing_timing_x` (array, optional) — Tied-up, centered, or flailed; `swing_timing_y` (array, optional) — Early, on-time, or late; `swing_timing_z` (array, optional) — Under, lined-up, or over; `teams` (array, optional) — One or more MLB team ids; `type` (string, optional) — Row type

### `mlb_statcast_swing_timing_details`

- **HTTP:** `GET /mlb/statcast-swing-timing-details`
- **What:** Get Baseball Savant Swing Timing player details. Returns the four anonymous per-swing detail arrays expanded from a batter or pitcher Swing Timing row. Pass the row_id uniqueId from mlb-statcast-swing-timing and repeat its type and table filters so split values can be mapped to the upstream detail query.
- **Params:** `attack_zone` (string, optional) — Attack zone; `bat_side` (string, optional) — Batter side; `contact_type` (string, optional) — Contact type; `counts` (array, optional) — Ball-strike counts; `date_end` (string, optional) — Filter end date in YYYY-MM-DD format; `date_start` (string, optional) — Filter start date in YYYY-MM-DD format; `flags` (array, optional) — Positive swing timing flags; `game_types` (array, optional) — Game-type filters; `min_split` (string, optional) — Minimum group swings; `min_swings` (string, optional) — Minimum swings; `not_flags` (array, optional) — Excluded swing timing flags; `pitch_hand` (string, optional) — Pitcher hand; `pitch_types` (array, optional) — Pitch type codes; `row_id` (string, **required**) — Unique row id from mlb-statcast-swing-timing, including any selected split values; `seasons` (array, optional) — Season filters; `split_year` (string, optional) — Include year in the row grouping; `splits` (array, optional) — Split dimensions; `swing_timing_x` (array, optional) — Tied-up/flail axis values; `swing_timing_y` (array, optional) — Early/late axis values; `swing_timing_z` (array, optional) — Over/under axis values; `teams` (array, optional) — MLB team ids; `type` (string, **required**) — Player row type

### `mlb_statcast_top_performers`

- **HTTP:** `GET /mlb/statcast-top-performers`
- **What:** Get Baseball Savant Top Performers. Returns every current Top Performers card for the selected season, including batter and pitcher rankings across batting, batted-ball, expected-stat, fielding, catching, running, and pitch-metric views. The page exposes a season selector but no per-card filters; use the specialist Statcast endpoints for complete filtered leaderboards.
- **Params:** `year` (integer, optional) — Season from 2015 through the current season; defaults to the current season

### `mlb_statcast_year_to_year`

- **HTTP:** `GET /mlb/statcast-year-to-year`
- **What:** Get Baseball Savant Year-to-Year Changes. Returns one of Baseball Savant's Year-to-Year Changes tables for batters, pitchers, batting teams, or pitching teams. Select one of the live statistic types and comparison start years; the page data contains available yearly values and differences. Table sorting and pagination are applied locally. Use mlb_discovery for all accepted group, type, and year values.
- **Params:** `group` (string, optional) — Table group; `limit` (integer, optional) — Rows per page (1-500); `offset` (integer, optional) — Zero-based row offset (0-5000); `sort` (string, optional) — Local sortable column; name_display_last_first, year_YYYY, TYPE_YYYY, or TYPE_diff_YYYY. Defaults to the selected metric's difference for the selected comparison year.; `sort_dir` (string, optional) — Sort direction; defaults to Batter descending and Pitcher ascending; `type` (string, optional) — Statistic type; `year` (string, optional) — Comparison start year; compares this season with the following year

### `mlb_team_roster`

- **HTTP:** `GET /mlb/team-roster`
- **What:** Get an MLB team roster. Returns a team's players, jersey numbers, positions, and roster status. The roster_type parameter accepts every value in the live MLB value set returned by mlb_discovery.
- **Params:** `roster_type` (string, optional) — Roster type; `season` (integer, optional) — Four-digit season; defaults to current year; `team_id` (string, **required**) — Numeric MLB team id

### `mlb_team_stats`

- **HTTP:** `GET /mlb/team-stats`
- **What:** Get MLB team season statistics. Returns one team's season statistics. Group accepts every value returned by mlb_discovery.
- **Params:** `end_date` (string, optional) — End date for byDateRange stat types; requires start_date; `game_type` (string, optional) — MLB game type; `group` (string, **required**) — Statistics group; `opponent_player_id` (string, optional) — Required by vsPlayer stat types; `opponent_team_id` (string, optional) — Required by vsTeam stat types; `season` (integer, optional) — Four-digit season; `start_date` (string, optional) — Start date for byDateRange stat types; requires end_date; `stat_type` (string, optional) — Stats API stat type; defaults to season; `team_id` (string, **required**) — Numeric MLB team id

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

## Cricinfo (22)

### `cricinfo_calendar`

- **HTTP:** `GET /cricinfo/calendar`
- **What:** Get the Cricinfo international calendar. Returns the dated international match calendar currently published by Cricinfo. It includes match-day names and the associated series labels.
- **Params:** _none_

### `cricinfo_commentary`

- **HTTP:** `GET /cricinfo/commentary`
- **What:** Get Cricinfo match commentary. Returns the latest ball-by-ball and editorial commentary embedded in a public Cricinfo match page. `url` may be a canonical full-scorecard or live-score URL.
- **Params:** `limit` (integer, optional) — Maximum commentary entries returned, from 1 to 100; `url` (string, **required**) — Canonical Cricinfo full-scorecard or live-score URL

### `cricinfo_grounds`

- **HTTP:** `GET /cricinfo/grounds`
- **What:** List Cricinfo grounds. Returns the featured public ground directory snapshot and the country index used to discover Cricinfo venue pages. Use the existing venue endpoint for detailed ground profiles.
- **Params:** `limit` (integer, optional) — Maximum featured grounds returned, from 1 to 100

### `cricinfo_live_matches`

- **HTTP:** `GET /cricinfo/live`
- **What:** Get Cricinfo live matches. Returns the current public live-score feed, including live, upcoming, and recently completed match cards with their canonical scorecard URLs.
- **Params:** _none_

### `cricinfo_match`

- **HTTP:** `GET /cricinfo/match`
- **What:** Get a Cricinfo match scorecard. Returns a public Cricinfo match scorecard with match state, team scores, and available innings totals and batter/bowler lines. Upcoming matches return an empty innings list. `url` must be a canonical `https://www.cricinfo.com/series/.../(full-scorecard|live-cricket-score)` URL; live-score URLs are normalized to the paired scorecard.
- **Params:** `url` (string, **required**) — Canonical Cricinfo full-scorecard or live-cricket-score URL

### `cricinfo_news`

- **HTTP:** `GET /cricinfo/news`
- **What:** Get latest Cricinfo news. Returns a bounded snapshot of Cricinfo's latest public stories, including titles, summaries, authors, genres, publication times, images, and associated match or series identifiers.
- **Params:** `limit` (integer, optional) — Maximum stories returned, from 1 to 100

### `cricinfo_photos`

- **HTTP:** `GET /cricinfo/photos`
- **What:** Get latest Cricinfo photos. Returns bounded metadata for the latest public Cricinfo photos, including captions, credits, dimensions, dates, and image variants. Media files are not downloaded by the endpoint.
- **Params:** `limit` (integer, optional) — Maximum photos returned, from 1 to 100

### `cricinfo_rankings`

- **HTTP:** `GET /cricinfo/rankings`
- **What:** Get ICC rankings from Cricinfo. Returns ICC rankings (team or player) from a Cricinfo rankings page. `url` must be a canonical `https://www.cricinfo.com/rankings/...` URL.
- **Params:** `url` (string, **required**) — Canonical Cricinfo rankings URL

### `cricinfo_records`

- **HTTP:** `GET /cricinfo/records`
- **What:** Get a Cricinfo record table. Returns a bounded normalized table from a public Cricinfo records page. `record` is a relative Statsguru record path such as `batting/most_runs_career.html`. `class` must be one of `1`, `2`, `3`, `4`, `5`, `6`, `8`, `9`, `10`, `11`, `12`, `20`, `21`, `22`, or `23`.
- **Params:** `class` (integer, **required**) — Record match-class. Allowed values: 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 20, 21, 22, 23; `current` (string, optional) — Record currentness selector; `id` (string, optional) — Numeric record subject identifier; `record` (string, **required**) — Relative Statsguru record path; `type` (string, optional) — Record subject type

### `cricinfo_records_index`

- **HTTP:** `GET /cricinfo/records/index`
- **What:** List Cricinfo records catalog. Returns the public Cricinfo records catalog, including match classes, record categories, selectable teams or entities, and example suggestions. Use the existing records endpoint to retrieve a specific table.
- **Params:** _none_

### `cricinfo_rss`

- **HTTP:** `GET /cricinfo/rss`
- **What:** Read a Cricinfo RSS feed. Returns a normalized public Cricinfo RSS feed. `url` must be one of Cricinfo's official news, live-score, country-story, or player-story RSS URLs.
- **Params:** `url` (string, **required**) — Official Cricinfo RSS feed URL

### `cricinfo_scores`

- **HTTP:** `GET /cricinfo/scores`
- **What:** Get current Cricinfo match scores. Returns the current match cards in Cricinfo's public homepage snapshot, including match state, scores, and canonical scorecard URLs. This is a point-in-time feed, not a fixture archive or streaming subscription.
- **Params:** _none_

### `cricinfo_series`

- **HTTP:** `GET /cricinfo/series`
- **What:** Get a Cricinfo series schedule and standings. Returns a series's match schedule and standings from its dedicated page. `series_id` must be the slug-and-ID portion of a canonical Cricinfo series URL, such as `indian-premier-league-2024-1410320`.
- **Params:** `series_id` (string, **required**) — Slug-and-ID portion of a canonical series URL

### `cricinfo_squads`

- **HTTP:** `GET /cricinfo/squads`
- **What:** Get a Cricinfo team squad. Returns recent public squad announcements and player rosters from a Cricinfo team profile, including player roles and withdrawal or overseas markers when published.
- **Params:** `url` (string, **required**) — Canonical Cricinfo team profile URL

### `cricinfo_stats`

- **HTTP:** `GET /cricinfo/stats`
- **What:** Query Cricinfo Statsguru. Returns a bounded normalized Statsguru table. `class` must be one of `1`, `2`, `3`, `4`, `5`, `6`, `8`, `9`, `10`, `11`, `12`, `20`, `21`, `22`, or `23`; `type` must be one of `batting`, `bowling`, `fielding`, `allround`, `fow`, `team`, `official`, or `aggregate`; `view` may be `innings`, `match`, `series`, `ground`, `host`, `opposition`, `year`, or `season`.
- **Params:** `class` (integer, **required**) — Statsguru match-class. Allowed values: 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 20, 21, 22, 23; `ground` (string, optional) — Numeric ground identifier; `host` (string, optional) — Numeric host-country identifier; `limit` (integer, optional) — Maximum rows returned, from 1 to 100; `opposition` (string, optional) — Numeric opposition team identifier; `orderby` (string, optional) — Statsguru sort column; `orderby_desc` (boolean, optional) — Sort descending when true; `player` (string, optional) — Numeric Cricinfo player identifier; `season` (string, optional) — Season formatted as YYYY or YYYY/YY; `span_max` (string, optional) — Statsguru ending date; `span_min` (string, optional) — Statsguru starting date; `team` (string, optional) — Numeric Cricinfo team identifier; `type` (string, **required**) — Statsguru statistic family; `view` (string, optional) — Statsguru table view

### `cricinfo_story`

- **HTTP:** `GET /cricinfo/story`
- **What:** Get a Cricinfo story. Returns a public Cricinfo news article, match report, preview, or live blog. The response includes stable story metadata, typed content blocks, live-blog entries when present, and related links.
- **Params:** `url` (string, **required**) — Canonical Cricinfo story, report, preview, or live-blog URL

### `cricinfo_team`

- **HTTP:** `GET /cricinfo/team`
- **What:** Get a Cricinfo team profile. Returns public team identity, profile text, recent fixtures and results, and the rolling batting and bowling leaders shown on a Cricinfo team page.
- **Params:** `url` (string, **required**) — Canonical Cricinfo team profile URL

### `cricinfo_team_schedule`

- **HTTP:** `GET /cricinfo/team/schedule`
- **What:** Get a Cricinfo team match schedule. Returns a team's recent fixtures and results from its dedicated page. `url` must be a canonical `https://www.cricinfo.com/team/...` URL.
- **Params:** `url` (string, **required**) — Canonical Cricinfo team URL

### `cricinfo_teams`

- **HTTP:** `GET /cricinfo/teams`
- **What:** List Cricinfo teams. Returns Cricinfo's grouped public team directory, including international, domestic, and franchise team identities.
- **Params:** _none_

### `cricinfo_venue`

- **HTTP:** `GET /cricinfo/venue`
- **What:** Get a Cricinfo cricket-ground profile. Returns structured metadata, associated home teams, and the editorial profile for a public Cricinfo cricket-ground page. `url` must be a canonical `https://www.cricinfo.com/cricket-grounds/...` or legacy `/ci/content/ground/...html` URL.
- **Params:** `url` (string, **required**) — Canonical Cricinfo cricket-ground URL

### `cricinfo_venue_matches`

- **HTTP:** `GET /cricinfo/venue/matches`
- **What:** Get matches at a Cricinfo venue. Returns upcoming fixtures and recent results listed on a public Cricinfo ground page. `url` must be a canonical `https://www.cricinfo.com/cricket-grounds/...` URL.
- **Params:** `url` (string, **required**) — Canonical Cricinfo cricket-ground URL

### `cricinfo_videos`

- **HTTP:** `GET /cricinfo/videos`
- **What:** Get Cricinfo videos. Returns a bounded snapshot of Cricinfo's public video hub, including curated, trending, and genre-associated video metadata. Media files are not downloaded by the endpoint.
- **Params:** `limit` (integer, optional) — Maximum videos returned, from 1 to 100

## Sportskeeda (48)

### `sportskeeda_article`

- **HTTP:** `GET /sportskeeda/article`
- **What:** Get a Sportskeeda article. Returns public article metadata and body paragraphs for a Sportskeeda article slug. Discovered slugs may contain case-preserving percent-encoded characters. A canonical Sportskeeda URL remains accepted for existing clients. Provide exactly one of slug or url; use /sportskeeda/sections and /sportskeeda/sitemaps for topic discovery.
- **Params:** `slug` (string, optional) — Sportskeeda article path without host; preferred over url; `url` (string, optional) — Canonical Sportskeeda article URL; alternative to slug

### `sportskeeda_author`

- **HTTP:** `GET /sportskeeda/author`
- **What:** Get a Sportskeeda author profile. Returns one public Sportskeeda author's name and recent article links from the canonical author profile.
- **Params:** `slug` (string, optional) — Sportskeeda author slug, e.g. sripad; `url` (string, optional) — Canonical Sportskeeda /author/<slug> URL; alternative to slug

### `sportskeeda_college_basketball_schedule`

- **HTTP:** `GET /sportskeeda/college-basketball-schedule`
- **What:** Get Sportskeeda college basketball games for a date. Returns all games and published scores for the requested date and season from Sportskeeda's first-party JSON feed. Discover valid season values with college-basketball-schedule-options. The upstream conference filter is currently unreliable and this endpoint does not accept it.
- **Params:** `date` (string, **required**) — Game date in YYYY-MM-DD format; `season` (integer, **required**) — Season starting year returned by college-basketball-schedule-options

### `sportskeeda_college_basketball_schedule_options`

- **HTTP:** `GET /sportskeeda/college-basketball-schedule-options`
- **What:** Discover college basketball schedule seasons and date window. Reads Sportskeeda's current college basketball schedule configuration. It returns every season from the published minimum through the current schedule season and the date-picker window. The conference selector is shown by the site, but its current-season feed metadata is incomplete.
- **Params:** `season` (integer, optional) — A season starting year from the live seasons list; defaults to the current schedule season

### `sportskeeda_cricket_commentary`

- **HTTP:** `GET /sportskeeda/cricket-commentary`
- **What:** Get Sportskeeda cricket ball-by-ball commentary. Returns the current commentary feed. To page to older events, pass a 24-character lowercase hexadecimal cursor from an event in /sportskeeda/cricket-match's commentary field (the full feed may contain zero-filled IDs); language then selects an upstream language. The match page's commentary selector offers en, hi, ta, te, and bho. Language without cursor is rejected because the upstream feed ignores it.
- **Params:** `cursor` (string, optional) — Nonzero 24-character lowercase hexadecimal commentary ID from /sportskeeda/cricket-match commentary; `language` (string, optional) — Older-comment language; valid only with cursor; `slug` (string, **required**) — Host-free match path returned by /sportskeeda/schedule

### `sportskeeda_cricket_match`

- **HTTP:** `GET /sportskeeda/cricket-match`
- **What:** Get a Sportskeeda cricket match center. Returns the public scorecard, innings, teams, squads, player data, and latest commentary for a cricket match slug discovered from /sportskeeda/schedule. Betting fields are excluded.
- **Params:** `slug` (string, **required**) — Host-free match path returned by /sportskeeda/schedule

### `sportskeeda_depth_chart`

- **HTTP:** `GET /sportskeeda/depth-chart`
- **What:** Get the NFL depth chart for all teams. Returns every team and listed position/player from the live NFL depth chart. Players and team detail pages include slugs when Sportskeeda links them.
- **Params:** `slug` (string, **required**) — Must be nfl/depth-chart

### `sportskeeda_draft_picks`

- **HTTP:** `GET /sportskeeda/draft-picks`
- **What:** Get all historical NFL team draft picks from Sportskeeda. Reads the complete public draft JSON asset, not only the rows initially visible on the page. Filter by year, round, position or player name. Discover each team's exact filter values with draft-picks-options. Source history and latest available year are published by Sportskeeda and may lag the current season.
- **Params:** `page` (integer, optional) — Page number, 1-1000; default 1; `per_page` (integer, optional) — Records per page, 1-500; default 100; `position` (string, optional) — Exact position from draft-picks-options; `q` (string, optional) — Case-insensitive player-name substring, at most 100 characters; `round` (string, optional) — Exact round from draft-picks-options; historical special labels are accepted; `slug` (string, **required**) — NFL team draft-picks page path without host; `year` (integer, optional) — Year from draft-picks-options; omit for all years

### `sportskeeda_draft_picks_options`

- **HTTP:** `GET /sportskeeda/draft-picks-options`
- **What:** Discover an NFL team's complete Sportskeeda draft filters. Reads the public draft JSON asset named by the team page and returns every available year, round and position, including historical special rounds. Team page slugs are discoverable from page-options on an NFL team overview.
- **Params:** `slug` (string, **required**) — NFL team draft-picks page path without host

### `sportskeeda_event_calendar`

- **HTTP:** `GET /sportskeeda/event-calendar`
- **What:** Get Sportskeeda regional sports calendar events. Returns all events from the embedded Sports Calendar, optionally filtered by an offered region-specific sport, one or more offered months, or an inclusive date range. Discover the current region, sport, and month values through /sportskeeda/event-calendar-options.
- **Params:** `end_date` (string, optional) — Inclusive range end in YYYY-MM-DD; provide together with start_date; `month` (array, optional) — One or more offered calendar months in YYYY-MM format; repeat this parameter for multiple months; `region` (string, optional) — Calendar region; `sport` (string, optional) — Exact sport label offered for the selected region; see event-calendar-options; `start_date` (string, optional) — Inclusive range start in YYYY-MM-DD; provide together with end_date

### `sportskeeda_event_calendar_options`

- **HTTP:** `GET /sportskeeda/event-calendar-options`
- **What:** Discover Sportskeeda calendar regions, sports, and months. Returns the live region-specific sport and month filters from Sportskeeda's embedded event calendar feed. Use these values with /sportskeeda/event-calendar.
- **Params:** _none_

### `sportskeeda_feed`

- **HTTP:** `GET /sportskeeda/feed`
- **What:** Get articles from a Sportskeeda section or topic. Fetches the public article cards for a Sportskeeda section, event, team-news, or player-news slug. Page pagination is accepted only when the source advertises it.
- **Params:** `page` (integer, optional) — Source page, for feeds with pagination; defaults to 1; `slug` (string, **required**) — Sportskeeda path without host, such as wwe, go/epl, or player/jannik-sinner/news

### `sportskeeda_football_data`

- **HTTP:** `GET /sportskeeda/football-data`
- **What:** Get football fixtures and standings. Returns first-party football widget fixtures and standings. Event and optional matchday must be offered by football-options. Omit matchday for the widget's selected round. Scores and standings reflect upstream data, which may be stale.
- **Params:** `event` (string, **required**) — Tournament slug from football-options; current selector: featured, epl, uefa-champions-league, uefa-nations-league, la-liga, ligue-1, mls, bundesliga; `matchday` (string, optional) — Round slug from football-options for the selected event

### `sportskeeda_football_options`

- **HTTP:** `GET /sportskeeda/football-options`
- **What:** Discover football tournaments and matchdays. Lists the live football widget's tournament selector. With event, follows the full previous/next matchday chain and returns every currently offered round slug. The discovered values feed sportskeeda-football-data.
- **Params:** `event` (string, optional) — Live tournament slug; current selector: featured, epl, uefa-champions-league, uefa-nations-league, la-liga, ligue-1, mls, bundesliga. Omit to list tournaments only

### `sportskeeda_guessing_game`

- **HTTP:** `GET /sportskeeda/guessing-game`
- **What:** Get a Sportskeeda daily guessing-game puzzle. Returns the public clues and image metadata for a discovered player-guessing game and ISO date. The answer is omitted so the endpoint does not reveal the active puzzle solution.
- **Params:** `date` (string, **required**) — Puzzle date in YYYY-MM-DD format; `slug` (string, **required**) — Discovered host-free game page path

### `sportskeeda_guessing_game_entities`

- **HTTP:** `GET /sportskeeda/guessing-game-entities`
- **What:** List players for a Sportskeeda guessing game. Returns the live public entity list used by a discovered player-guessing game, including the game-specific team, position, and profile fields.
- **Params:** `slug` (string, **required**) — Discovered host-free game page path

### `sportskeeda_guessing_games`

- **HTTP:** `GET /sportskeeda/guessing-games`
- **What:** List Sportskeeda player-guessing games. Discovers every currently linked player-guessing game and returns its host-free page slug for the daily instance and entity endpoints.
- **Params:** _none_

### `sportskeeda_nba_queries`

- **HTTP:** `GET /sportskeeda/nba-queries`
- **What:** List Sportskeeda NBA player query pages. Pages through the server-rendered questions on Sportskeeda's Top NBA Queries page. Slugs are host-free and can be passed to sportskeeda_page_data for the linked player stats table. The live category directory is returned on every page.
- **Params:** `category` (string, optional) — Optional category id; `limit` (integer, optional) — Page size; 0 or omitted defaults to 100, maximum is 500; `offset` (integer, optional) — Zero-based result offset

### `sportskeeda_news`

- **HTTP:** `GET /sportskeeda/news`
- **What:** Get Sportskeeda's latest news. Returns the current public Sportskeeda news sitemap entries. Use /sportskeeda/sections to discover all navigation groups and sports landing pages, and /sportskeeda/taxonomy-search to search categories, events, teams, players, wiki pages, and wiki tags.
- **Params:** _none_

### `sportskeeda_page_data`

- **HTTP:** `GET /sportskeeda/page-data`
- **What:** Get Sportskeeda structured sports tables. Returns server-rendered team, player, roster, leaderboard, ranking, depth, playoff, and game-log tables. NFL team stats include team-leader cards, player-category tables, and Basic, Advanced, and Expert team tables. Season and type are accepted only if offered by the selected page; discover their values with page-options. Player game-log seasons use their discovered season-specific path and return every table offered by the page; NFL category tabs are listed by page-options. College-football schedule slugs accept a discovered conference slug and filter the embedded schedule rows locally; an offered group with no games on that week returns status no_data. The trade value chart uses its public JSON asset and has a separate endpoint. A page with no structured tables returns an upstream error.
- **Params:** `conference` (string, optional) — College-football schedule conference slug from page-options; `season` (integer, optional) — Season year offered by this page's page-options filter; `slug` (string, **required**) — Sportskeeda path without host; `type` (string, optional) — Season phase offered by this page's page-options filter; leaderboard pages offer pre, regular, post

### `sportskeeda_page_options`

- **HTTP:** `GET /sportskeeda/page-options`
- **What:** Discover Sportskeeda page menus and filters. Returns the page's live contextual menus, team and ranking links, tabs, schedule views, and every currently offered select-filter value. Leaderboard category and metric values carry their destination slugs. College-football schedule pages expose the client-side conference selector here.
- **Params:** `slug` (string, **required**) — Sportskeeda path without host

### `sportskeeda_player_stats`

- **HTTP:** `GET /sportskeeda/player-stats`
- **What:** Get NFL or NBA player season stats across event phases. Reads the anonymous season-stats JSON embedded in an NFL or NBA player stats page. Without event_type, returns all event phases offered by that page's selector. NBA source data may contain extra internal phases that the page does not offer; these are excluded. Discover the current event_type values with sportskeeda-page-options for the same slug.
- **Params:** `event_type` (string, optional) — Event phase offered by this player's stats-event-type-dropdown; NFL offers 0,1,2,3 and NBA offers 0,1,2; `slug` (string, **required**) — NFL or NBA player stats path without host

### `sportskeeda_profile`

- **HTTP:** `GET /sportskeeda/profile`
- **What:** Get a Sportskeeda player or team profile. Returns facts and available news cards from a public player or team profile path, including sport-specific slugs.
- **Params:** `slug` (string, **required**) — Sportskeeda player or team profile path without host

### `sportskeeda_quiz`

- **HTTP:** `GET /sportskeeda/quiz`
- **What:** Get a Sportskeeda quiz definition. Returns public question prompts and choice text from a quiz page, sorted by question number. The source does not expose correct answers in its anonymous page data; answer checking and user submissions are not included.
- **Params:** `slug` (string, **required**) — Sportskeeda quiz path without host, discovered through /sportskeeda/quizzes

### `sportskeeda_quiz_categories`

- **HTTP:** `GET /sportskeeda/quiz-categories`
- **What:** List current Sportskeeda quiz categories. Discovers every quiz category linked from the public quiz hub. Use a returned host-free category slug with /sportskeeda/quizzes.
- **Params:** _none_

### `sportskeeda_quizzes`

- **HTTP:** `GET /sportskeeda/quizzes`
- **What:** List quizzes in a Sportskeeda category. Returns public quiz cards for one category path discovered through /sportskeeda/quiz-categories. The source currently renders its first quiz page; page pagination is not exposed because the visible page links currently repeat the same cards.
- **Params:** `slug` (string, **required**) — Sportskeeda quiz category path without host

### `sportskeeda_salary_cap`

- **HTTP:** `GET /sportskeeda/salary-cap`
- **What:** Get NFL team salary-cap figures from Sportskeeda. Returns the source's published season, team totals, every player cap scenario and expanded salary breakdown. The site's player search and sortable columns are applied to the complete server-rendered rows. The published season may lag the current season.
- **Params:** `order` (string, optional) — Sort direction; requires sort_by; default asc; `q` (string, optional) — Case-insensitive player-name substring, at most 100 characters; `slug` (string, **required**) — NFL team salary-cap page path without host; `sort_by` (string, optional) — Sortable column; omit to preserve source order

### `sportskeeda_schedule`

- **HTTP:** `GET /sportskeeda/schedule`
- **What:** Get Sportskeeda fixtures and results. Parses public cricket and football match cards or sport-specific schedule tables. A genuine no-matches widget returns status no_matches.
- **Params:** `slug` (string, **required**) — Sportskeeda schedule path without host

### `sportskeeda_sections`

- **HTTP:** `GET /sportskeeda/sections`
- **What:** Discover Sportskeeda sections and topics. Returns the live parent/child navigation tree, including external destinations marked explicitly, plus every public sports landing URL from Sportskeeda's sports sitemap.
- **Params:** _none_

### `sportskeeda_sitemap_items`

- **HTTP:** `GET /sportskeeda/sitemap-items`
- **What:** Page through a Sportskeeda sitemap. Returns canonical URLs and host-free path slugs from one sitemap discovered by /sportskeeda/sitemaps. Returned path slugs preserve case and percent-encode unusual characters. A sitemap_url remains accepted for existing callers. Provide exactly one; the source is checked against the live index and robots sitemap list on each call.
- **Params:** `limit` (integer, optional) — Page size from 1 to 500; defaults to 100; `offset` (integer, optional) — Zero-based item offset; `sitemap_url` (string, optional) — Exact sitemap URL; alternative to slug; `slug` (string, optional) — Sitemap slug returned by /sportskeeda/sitemaps; preferred

### `sportskeeda_sitemaps`

- **HTTP:** `GET /sportskeeda/sitemaps`
- **What:** Discover Sportskeeda sitemap sources. Returns current public sitemaps from Sportskeeda's sitemap index and robots.txt. Pass a returned slug to /sportskeeda/sitemap-items to page through its complete URL set.
- **Params:** _none_

### `sportskeeda_standings`

- **HTTP:** `GET /sportskeeda/standings`
- **What:** Get Sportskeeda standings or rankings. Parses current standings tables. College basketball supports a live-discovered season value; its unpopulated current season returns status no_data.
- **Params:** `season` (integer, optional) — College basketball season starting year; live values from standings-options; `slug` (string, **required**) — Sportskeeda standings or rankings path without host

### `sportskeeda_standings_options`

- **HTTP:** `GET /sportskeeda/standings-options`
- **What:** Discover Sportskeeda college standings seasons and conferences. Returns all live-offered college basketball season years and the conference slugs for the selected season.
- **Params:** `season` (integer, optional) — A live-offered starting year; selects its conference list; `slug` (string, **required**) — College basketball standings slug

### `sportskeeda_taxonomy_search`

- **HTTP:** `GET /sportskeeda/taxonomy-search`
- **What:** Search Sportskeeda categories and entities. Calls Sportskeeda's anonymous frontend taxonomy search across categories, events, teams, players, wiki pages, and wiki tags. The upstream UI always searches all six types; the q phrase is sanitized and capped at 100 characters just like the site.
- **Params:** `q` (string, **required**) — Search phrase; punctuation is replaced with spaces and the result is capped at 100 characters

### `sportskeeda_topic`

- **HTTP:** `GET /sportskeeda/topic`
- **What:** Get a Sportskeeda topic or entity overview's full content. Returns ordered prose, headings, lists, tables, images and embeds from a public topic, event, team or player overview page, plus available byline, modification text and related stories. Discover slugs with /sportskeeda/sitemap-items using tags.xml, tournaments.xml, teams.xml, players.xml or us-sitemap.xml. Pages without a CMS body return an upstream error.
- **Params:** `slug` (string, **required**) — Canonical Sportskeeda topic, event, team or player path without host

### `sportskeeda_trade_values`

- **HTTP:** `GET /sportskeeda/trade-values`
- **What:** Get NFL redraft or dynasty trade values. Reads the same anonymous JSON asset as the public chart. Returns source update time, ranks, values, and linked player slugs. The All position includes all source rows, including positions not displayed as chart sections. Discover current chart and filter choices with page-options.
- **Params:** `limit` (integer, optional) — Page size from 1 to 500; `offset` (integer, optional) — Zero-based player offset; `position` (string, optional) — Displayed position section; defaults to All; `scoring` (string, optional) — Scoring system; defaults to ppr; `slug` (string, **required**) — Chart path without host; `superflex` (boolean, optional) — Use superflex chart; defaults to false

### `sportskeeda_transactions`

- **HTTP:** `GET /sportskeeda/transactions`
- **What:** Get complete monthly NFL league or team transactions. Reads the first-party public transaction feed in month-sized windows, avoiding its 10000-row broad-range cap. Discover accepted seasons, months, and team slugs with sportskeeda-transactions-options.
- **Params:** `month` (string, **required**) — MMYYYY month code from transactions-options for the selected season; current live union is listed here; `page` (integer, optional) — Page number, 1-1000; default 1; `per_page` (integer, optional) — Records per page, 1-500; default 100; `season` (integer, optional) — Season start year; current live choices: 2020,2021,2022,2023,2024,2025,2026; defaults to current; `slug` (string, optional) — Host-free page slug; nfl/transactions or an NFL team transactions slug

### `sportskeeda_transactions_options`

- **HTTP:** `GET /sportskeeda/transactions-options`
- **What:** List NFL transaction seasons, months and team slugs. Discovers the complete live NFL transaction season list, months for the selected season, and all team transaction page slugs. Use these values with sportskeeda-transactions.
- **Params:** `season` (integer, optional) — Season start year; current live choices: 2020,2021,2022,2023,2024,2025,2026; defaults to current

### `sportskeeda_video`

- **HTTP:** `GET /sportskeeda/video`
- **What:** Get Sportskeeda video metadata. Returns the public video player's ID, title, poster, and stream URL for a video page slug.
- **Params:** `slug` (string, **required**) — Individual Sportskeeda video page path without host

### `sportskeeda_videos`

- **HTTP:** `GET /sportskeeda/videos`
- **What:** List Sportskeeda videos and channels. Lists public video cards from the main video library or a sport/event video listing.
- **Params:** `slug` (string, optional) — Video listing path without host; defaults to videos

### `sportskeeda_wiki_activity`

- **HTTP:** `GET /sportskeeda/wiki-activity`
- **What:** List accepted edits for a Sportskeeda Wiki page. Returns the public accepted activity history for one Wiki article, with bounded pagination and the page's live sort fields. The source page slug is obtained from sportskeeda-wiki-pages.
- **Params:** `limit` (integer, optional) — Activity items per page; `page` (integer, optional) — 1-based page; `slug` (string, **required**) — Host-free Wiki page path_slug from sportskeeda-wiki-pages; `sort` (string, optional) — Sort direction; `sort_by` (string, optional) — Activity sort field

### `sportskeeda_wiki_article`

- **HTTP:** `GET /sportskeeda/wiki-article`
- **What:** Get a Sportskeeda Wiki article. Returns the rendered article title, metadata, and body paragraphs. Pass the path_slug returned by sportskeeda-wiki-pages; URL and host input are not accepted.
- **Params:** `slug` (string, **required**) — Host-free Wiki page path_slug from sportskeeda-wiki-pages

### `sportskeeda_wiki_categories`

- **HTTP:** `GET /sportskeeda/wiki-categories`
- **What:** List Sportskeeda Wiki categories. Returns the nested live category menu for one Sportskeeda Wiki project, including child categories beneath expandable groups.
- **Params:** `wiki` (string, **required**) — Project slug returned by sportskeeda-wiki-options

### `sportskeeda_wiki_contributors`

- **HTTP:** `GET /sportskeeda/wiki-contributors`
- **What:** List contributors to a Sportskeeda Wiki page. Returns public accepted contributors for one Wiki article. The source page slug is obtained from sportskeeda-wiki-pages; user IP and private account fields are never returned.
- **Params:** `limit` (integer, optional) — Contributors per page; `page` (integer, optional) — 1-based page; `slug` (string, **required**) — Host-free Wiki page path_slug from sportskeeda-wiki-pages; `sort` (string, optional) — Sort direction; `sort_by` (string, optional) — Contributor sort field

### `sportskeeda_wiki_issues`

- **HTTP:** `GET /sportskeeda/wiki-issues`
- **What:** List reported issues for a Sportskeeda Wiki page. Returns public opened or closed issues for one Wiki article. The upstream also returns submitter IP addresses; this endpoint deliberately omits them.
- **Params:** `limit` (integer, optional) — Issues per page; `page` (integer, optional) — 1-based page; `slug` (string, **required**) — Host-free Wiki page path_slug from sportskeeda-wiki-pages; `status` (string, optional) — Issue status

### `sportskeeda_wiki_options`

- **HTTP:** `GET /sportskeeda/wiki-options`
- **What:** List Sportskeeda Wiki projects. Returns the live-verified project slugs and taxonomy mappings accepted by the Wiki category, catalog, and article endpoints.
- **Params:** _none_

### `sportskeeda_wiki_pages`

- **HTTP:** `GET /sportskeeda/wiki-pages`
- **What:** Search and paginate Sportskeeda Wiki pages. Returns catalog pages for one Wiki project. Use path_slug as the preferred host-free slug for sportskeeda-wiki-article. total_items is the record count; the upstream field named total_pages is mislabelled and does not mean page count.
- **Params:** `limit` (integer, optional) — Items per page; `page` (integer, optional) — 1-based catalog page; `search` (string, optional) — Title or page search text; sent upstream as searchText; `sort` (string, optional) — Sort direction; `sort_by` (string, optional) — Catalog field to sort by; `wiki` (string, **required**) — Project slug returned by sportskeeda-wiki-options

### `sportskeeda_wiki_summary`

- **HTTP:** `GET /sportskeeda/wiki-summary`
- **What:** Get community counts for a Sportskeeda Wiki page. Returns accepted contributor and activity totals plus the open-issue count for one Wiki article. The source page slug is obtained from sportskeeda-wiki-pages.
- **Params:** `slug` (string, **required**) — Host-free Wiki page path_slug from sportskeeda-wiki-pages
