# sports-scores-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**270 endpoints across 7 platform group(s).**

## ESPN (9)

### `espn_athlete`

- **HTTP:** `GET /espn/athlete`
- **What:** ESPN athlete. Returns one athlete's bio/overview (name, position, jersey, physicals, current team). The `sport` enum accepts `football`, `basketball`, `baseball`, `hockey`, and `soccer`. The `league` enum accepts `nfl`, `college-football`, `nba`, `wnba`, `mens-college-basketball`, `womens-college-basketball`, `mlb`, `nhl`, `eng.1`, `esp.1`, `ita.1`, `ger.1`, `fra.1`, `usa.1`, and `uefa.champions`; it must be valid for the chosen sport.
- **Params:** `athlete` (string, **required**) — Numeric ESPN athlete (player) id; `league` (string, **required**) — League key (must be valid for the sport); `sport` (string, **required**) — Sport key

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

### `espn_teams`

- **HTTP:** `GET /espn/teams`
- **What:** ESPN team list. Returns the full team list for a sport and league. The `sport` enum accepts `football`, `basketball`, `baseball`, `hockey`, and `soccer`. The `league` enum accepts `nfl`, `college-football`, `nba`, `wnba`, `mens-college-basketball`, `womens-college-basketball`, `mlb`, `nhl`, `eng.1`, `esp.1`, `ita.1`, `ger.1`, `fra.1`, `usa.1`, and `uefa.champions`; it must be valid for the chosen sport.
- **Params:** `league` (string, **required**) — League key (must be valid for the sport); `sport` (string, **required**) — Sport key

## SofaScore (109)

### `sofascore_categories`

- **HTTP:** `GET /sofascore/categories`
- **What:** SofaScore categories for a sport. Returns every category (country or region, such as England or International) SofaScore lists for a sport, with id, name, slug, flag, optional two-letter code, and priority, highest priority first. Use a category `id` with category-tournaments (its competitions) and with scheduled-events (its fixtures on a date). The `sport` enum accepts `american-football`, `aussie-rules`, `badminton`, `bandy`, `baseball`, `basketball`, `beach-volley`, `cricket`, `darts`, `esports`, `floorball`, `football`, `futsal`, `handball`, `ice-hockey`, `mma`, `minifootball`, `padel`, `rugby`, `snooker`, `table-tennis`, `tennis`, `volleyball`, and `waterpolo`. Slugs are not unique across categories, so identify a category by `id`.
- **Params:** `sport` (string, **required**) — Sport key

### `sofascore_category_tournaments`

- **HTTP:** `GET /sofascore/category-tournaments`
- **What:** SofaScore competitions in a category. Returns the competitions (unique tournaments) inside one category, most followed first. Each `id` is the competition id the tournament-seasons, standings, tournament-rounds, and round-events endpoints take. Get the category `id` from the categories endpoint. An empty `tournaments` list is a valid response: some categories exist without any competitions. Returns 404 for an unknown category id.
- **Params:** `id` (string, **required**) — Numeric SofaScore category id from the categories endpoint

### `sofascore_draft`

- **HTTP:** `GET /sofascore/draft`
- **What:** SofaScore league draft. Returns the draft attached to a league season: the upcoming or just-held `draft` and the `previous_draft`, each with its year, start and end time, status, the draft `rounds` (the valid `round` values for draft-picks) and whether the lottery is complete. The `league` enum accepts `nba` and `nfl`. Get `season` from tournament-seasons (NBA competition id 132, NFL 9464). A season without a draft, or a season id that does not belong to the league, returns 404. A season whose draft is not scheduled yet returns only `previous_draft`.
- **Params:** `league` (string, **required**) — League whose draft to return; `season` (string, **required**) — Numeric SofaScore season id of the league

### `sofascore_draft_picks`

- **HTTP:** `GET /sofascore/draft-picks`
- **What:** SofaScore league draft picks. Returns one round of a league draft: each pick with the overall and in-round number, the drafting team, and the drafted prospect (name, position, college or club, top-prospect flag and the player id when SofaScore has one), plus the teams that hold no pick in that round. The `league` enum accepts `nba` (rounds 1 and 2) and `nfl` (rounds 1 to 7); other rounds return 400. Get `year` from the draft endpoint's `draft.year` and `previous_draft.year`; SofaScore keeps only recent drafts, so an older year returns 404. Returns 404 when SofaScore has no picks for that year and round.
- **Params:** `league` (string, **required**) — League whose draft to return; `round` (integer, **required**) — Draft round: 1 to 2 for nba, 1 to 7 for nfl; `year` (string, **required**) — Four-digit draft year

### `sofascore_esports_game`

- **HTTP:** `GET /sofascore/esports-game`
- **What:** SofaScore esports game detail. Returns one resource of one esports game from SofaScore, chosen with `part`: `statistics` (team totals such as kills, towers and barracks for Dota 2, gold and drakes for League of Legends), `lineups` (every player with hero or champion and per-player statistics such as net worth, gold or ADR), `bans` (banned heroes or champions per side) and `rounds` (Counter-Strike round history with outcome, winner and side per round, including overtime). Only the requested block is returned. Get the game id from sofascore-event-esports-games. Statistics and bans exist for Dota 2 and League of Legends only (404 for Counter-Strike), rounds fill for Counter-Strike only (an empty list otherwise) and lineups work for all three. Returns 404 when SofaScore has no such data for the game.
- **Params:** `id` (string, **required**) — Numeric SofaScore esports game id from sofascore-event-esports-games; `part` (string, **required**) — Which resource of the game to return

### `sofascore_event`

- **HTTP:** `GET /sofascore/event`
- **What:** SofaScore event detail. Returns one SofaScore match by event id: home and away teams and scores, status, start time, tournament, attendance and winner code, plus venue and referee when SofaScore has them. An unknown or malformed id surfaces as an upstream error.
- **Params:** `id` (string, **required**) — Numeric SofaScore event (match) id

### `sofascore_event_at_bat_pitches`

- **HTTP:** `GET /sofascore/event-at-bat-pitches`
- **What:** SofaScore event at-bat pitches. Returns every pitch of one baseball at-bat from SofaScore, in pitch order: the ball-strike-out count, outcome code, pitch type and name, speed in kilometres per hour, zone, plate location, strike-zone bounds, batter and pitcher hand, the score, and for balls put in play the hit type, trajectory, hardness and location plus runner movements and fielder credits. Get the at-bat id (`at_bat_id`) from sofascore-event-at-bats for the same event. Returns 404 when SofaScore has no pitches for that at-bat, which includes an at-bat id that does not belong to the event.
- **Params:** `at_bat_id` (string, **required**) — Numeric at-bat id from sofascore-event-at-bats for the same event; `id` (string, **required**) — Numeric SofaScore baseball event (match) id

### `sofascore_event_at_bats`

- **HTTP:** `GET /sofascore/event-at-bats`
- **What:** SofaScore event at-bats. Returns a baseball match's at-bat timeline from SofaScore, in play order: for each plate appearance the inning and half (`top` or `bottom`), pitcher, hitter, their teams, when it ended and the home and away win probabilities before and after it. Use an at-bat `id` with sofascore-event-at-bat-pitches to read its pitches. Returns 404 when SofaScore has no at-bat data for the match, which includes matches that have not started and sports other than baseball.
- **Params:** `id` (string, **required**) — Numeric SofaScore baseball event (match) id

### `sofascore_event_average_positions`

- **HTTP:** `GET /sofascore/event-average-positions`
- **What:** SofaScore event average positions. Returns every player's average position on the pitch during a football match (`average_x` and `average_y` on SofaScore's 0-100 pitch scale, plus the number of touches behind it) for the home and away sides, and the substitutions with their minute. Returns 404 when SofaScore has no positional data for the match, which includes unstarted matches and sports other than football.
- **Params:** `id` (string, **required**) — Numeric SofaScore event (match) id

### `sofascore_event_baseball_top_performers`

- **HTTP:** `GET /sofascore/event-baseball-top-performers`
- **What:** SofaScore event baseball top performers. Returns a baseball match's top performers from SofaScore: each pitcher or batter (`role`) with a rating, their team and a snake_case map of the statistics that earned the mention (for example pitching strike outs, batting home runs and runs batted in). Returns 404 when SofaScore has no top performers for the match, which includes matches that have not started and sports other than baseball.
- **Params:** `id` (string, **required**) — Numeric SofaScore baseball event (match) id

### `sofascore_event_best_players`

- **HTTP:** `GET /sofascore/event-best-players`
- **What:** SofaScore event best players. Returns a match's best-rated players per side, the overall top-rated list, and the player of the match (each with team and value) from SofaScore. Covers football (value is the match rating, label `rating`) and ice hockey (label `pts`, value the points scored; a goalkeeper with no points has no numeric `value` and carries SofaScore's dash in `value_text`). The basketball, baseball and tennis matches checked returned no summary. Returns 404 when SofaScore has no best-players summary for the match, which includes matches that have not started, sports without one and fixtures without rated players.
- **Params:** `id` (string, **required**) — Numeric SofaScore event (match) id

### `sofascore_event_comments`

- **HTTP:** `GET /sofascore/event-comments`
- **What:** SofaScore event commentary. Returns a match's text commentary (minute, type, text, and the players involved, plus the running score on scoring lines) from SofaScore, newest first. Works for football and basketball matches that have commentary. An empty `comments` list is a valid response (a live match with no lines yet). Returns 404 when SofaScore has no commentary for the match, which includes matches that have not started.
- **Params:** `id` (string, **required**) — Numeric SofaScore event (match) id

### `sofascore_event_esports_games`

- **HTTP:** `GET /sofascore/event-esports-games`
- **What:** SofaScore event esports games. Returns the games (maps) of an esports match from SofaScore: each game's id, status, start time, length in seconds, winner, score per side (kills for Dota 2 and League of Legends, rounds with half and overtime split for Counter-Strike), the map for Counter-Strike, and whether complete statistics exist. Use a game `id` with sofascore-esports-game to read its statistics, lineups, bans or rounds. Returns 404 when SofaScore has no games for the event, which includes sports other than esports.
- **Params:** `id` (string, **required**) — Numeric SofaScore esports event (match) id

### `sofascore_event_graph`

- **HTTP:** `GET /sofascore/event-graph`
- **What:** SofaScore event momentum graph. Returns a match's momentum graph as minute and value points (positive values favour the home side) plus period length information, from SofaScore. Covers football, ice hockey and basketball. An empty `points` list is a valid response (a live match that has just started). Returns 404 when SofaScore has no momentum graph for the match, which includes matches that have not started and sports without one such as tennis and baseball.
- **Params:** `id` (string, **required**) — Numeric SofaScore event (match) id

### `sofascore_event_h2h`

- **HTTP:** `GET /sofascore/event-h2h`
- **What:** SofaScore event head-to-head. Returns the historical head-to-head win/draw record between a match's two teams (and managers, when available) from SofaScore.
- **Params:** `id` (string, **required**) — Numeric SofaScore event (match) id

### `sofascore_event_highlights`

- **HTTP:** `GET /sofascore/event-highlights`
- **What:** SofaScore event highlights. Returns the highlight videos attached to a match: title, subtitle (for example `Full Highlights`), video `url`, thumbnail, the publish time, whether it is the key highlight, and the countries it is restricted to when SofaScore limits it. `media_type_code` is SofaScore's own numeric code and is returned untranslated. Returns 404 when the match has no highlight videos, which includes matches that have not finished.
- **Params:** `id` (string, **required**) — Numeric SofaScore event (match) id

### `sofascore_event_incidents`

- **HTTP:** `GET /sofascore/event-incidents`
- **What:** SofaScore event incidents. Returns one match's goal, card, substitution, and period timeline from SofaScore. An empty `incidents` list is a valid response before kickoff.
- **Params:** `id` (string, **required**) — Numeric SofaScore event (match) id

### `sofascore_event_innings`

- **HTTP:** `GET /sofascore/event-innings`
- **What:** SofaScore event innings. Returns a cricket match's innings scorecards from SofaScore. Each innings has the batting and bowling teams, runs, wickets, overs in cricket notation (18.4 is 18 overs and 4 balls), extras (wides, no balls, byes, leg byes, penalty), every batter's line (runs, balls, fours, sixes, dismissal with the bowler and fielder, fall-of-wicket score and over), every bowler's figures (overs, maidens, runs, wickets, wides, no balls), the partnerships and a derived fall-of-wickets list. Works for T20, one-day and Test matches (a Test lists up to four innings). Returns 404 when SofaScore has no innings data for the match, which includes matches that have not started and sports other than cricket.
- **Params:** `id` (string, **required**) — Numeric SofaScore cricket event (match) id

### `sofascore_event_lineups`

- **HTTP:** `GET /sofascore/event-lineups`
- **What:** SofaScore event lineups. Returns one match's starting XI and substitutes per side, with formation. Returns 404 when SofaScore has no lineups for the match. A missing-lineup result may be reused for up to two minutes before checking again.
- **Params:** `id` (string, **required**) — Numeric SofaScore event (match) id

### `sofascore_event_managers`

- **HTTP:** `GET /sofascore/event-managers`
- **What:** SofaScore event managers. Returns the two managers (coaches) of a match with their SofaScore ids, names and slugs. The manager `id` works with the manager and manager-events endpoints. Returns 404 when SofaScore lists no managers for the match, which includes tennis matches.
- **Params:** `id` (string, **required**) — Numeric SofaScore event (match) id

### `sofascore_event_odds`

- **HTTP:** `GET /sofascore/event-odds`
- **What:** SofaScore event odds. Returns one match's betting markets and choices. Returns 404 when SofaScore has no odds for the match.
- **Params:** `id` (string, **required**) — Numeric SofaScore event (match) id

### `sofascore_event_player_heatmap`

- **HTTP:** `GET /sofascore/event-player-heatmap`
- **What:** SofaScore event player heatmap. Returns one player's touch locations in a football match as `points`, each an `x` and `y` on SofaScore's 0-100 pitch scale. Get `player_id` from event-lineups. Returns 404 when SofaScore has no heatmap for that player in that match, which includes players who did not play, unstarted matches and sports other than football.
- **Params:** `id` (string, **required**) — Numeric SofaScore event (match) id; `player_id` (string, **required**) — Numeric SofaScore player id that played in the match

### `sofascore_event_player_statistics`

- **HTTP:** `GET /sofascore/event-player-statistics`
- **What:** SofaScore event player statistics. Returns one player's statistics inside one football match (minutes, rating, passes, duels, shots, expected goals, and more) as a snake_case metric map. The set of metrics depends on the player's position, so absent metrics are omitted rather than zero. Get `player_id` from event-lineups. Returns 404 when SofaScore has no statistics for that player in that match.
- **Params:** `id` (string, **required**) — Numeric SofaScore event (match) id; `player_id` (string, **required**) — Numeric SofaScore player id that took part in the match

### `sofascore_event_point_by_point`

- **HTTP:** `GET /sofascore/event-point-by-point`
- **What:** SofaScore event point-by-point. Returns a racket-sport match's point-by-point timeline, with sets and games in play order. Tennis sets list games and each game lists every point with the running score (`0`, `15`, `30`, `40`, `A`, or a plain count in a tie-break), the server, the game winner, a `description` of `ace` or `double_fault` where SofaScore flags it, and break point (`break_point`) or set or match point (`set_or_match_point`) markers per player. Table tennis and badminton sets list their points directly. The ace flag is a lower bound of the match's real ace count. Darts matches are not covered. Returns 404 when SofaScore has no point-by-point data for the match, which includes matches that have not started and sports without it.
- **Params:** `id` (string, **required**) — Numeric SofaScore event (match) id

### `sofascore_event_pregame_form`

- **HTTP:** `GET /sofascore/event-pregame-form`
- **What:** SofaScore event pre-game form. Returns each side's form going into a match: league position, points (football) or win-loss record (basketball) in `value` with the `label` that names it, the average player rating where SofaScore has one, and the recent results (`W`, `D`, `L`) in the order SofaScore returns them. Covers football and basketball; returns 404 when SofaScore has no pre-game form for the match, which includes tennis matches.
- **Params:** `id` (string, **required**) — Numeric SofaScore event (match) id

### `sofascore_event_shotmap`

- **HTTP:** `GET /sofascore/event-shotmap`
- **What:** SofaScore event shot map. Returns every shot in a football or ice hockey match. Football shots carry the shooter, side, outcome (`shot_type`), situation, body part, expected goals (xG and xGOT), minute, and pitch and goal-mouth coordinates. Ice hockey shots carry the shooter, team, side, shot technique (`shot_type`, for example `wrist`), `outcome` (`made`, `saved`, `missed` or `blocked`), `strength` (`even`, `powerplay` or `shorthanded`), period and period clock, rink `coordinates` and, for most shots, `xg`. An empty `shots` list is a valid response (a live match with no shots yet). Returns 404 when SofaScore has no shot map for the match, which includes matches that have not started, basketball and other sports without one, and fixtures without expected-goals coverage.
- **Params:** `id` (string, **required**) — Numeric SofaScore event (match) id

### `sofascore_event_statistics`

- **HTTP:** `GET /sofascore/event-statistics`
- **What:** SofaScore event statistics. Returns one match's statistics (possession, shots, passes, and more, grouped and split by period). Returns 404 when SofaScore has no tracked statistics for the match.
- **Params:** `id` (string, **required**) — Numeric SofaScore event (match) id

### `sofascore_event_team_heatmap`

- **HTTP:** `GET /sofascore/event-team-heatmap`
- **What:** SofaScore event team heatmap. Returns one team's touch locations in a football match as `player_points` (outfield players) and `goalkeeper_points`, each point an `x` and `y` on SofaScore's 0-100 pitch scale. `team_id` must be the home or away team of the event; get both ids from the event endpoint. Returns 404 when SofaScore has no heatmap for that team in that match, which includes teams that did not play it, unstarted matches and sports other than football.
- **Params:** `id` (string, **required**) — Numeric SofaScore event (match) id; `team_id` (string, **required**) — Numeric SofaScore team id of the home or away side

### `sofascore_event_team_streaks`

- **HTTP:** `GET /sofascore/event-team-streaks`
- **What:** SofaScore event team streaks. Returns a match's team streaks and trends: `general` statements about each side's recent matches (for example `Wins` 6 or `No goals conceded` 4) and `head2head` statements about their meetings. Each item names the streak, a `value` that is either a run length (`6`) or a ratio (`5/5`), the `team` it refers to (`home`, `away` or `both`) and, where SofaScore reports it, whether the streak `continued` into this match. Returns 404 when SofaScore lists no streaks for the match, which includes tennis matches.
- **Params:** `id` (string, **required**) — Numeric SofaScore event (match) id

### `sofascore_event_tennis_power`

- **HTTP:** `GET /sofascore/event-tennis-power`
- **What:** SofaScore event tennis power. Returns a tennis match's per-game momentum series: for each game of each set a `value` (positive favours the home player or team, negative the away side) and whether a break of serve `break_occurred`. An empty `games` list is a valid response (a live match with no completed game yet). Returns 404 when SofaScore has no tennis power data for the match, which includes matches that have not started and sports other than tennis.
- **Params:** `id` (string, **required**) — Numeric SofaScore tennis event (match) id

### `sofascore_event_tv_channels`

- **HTTP:** `GET /sofascore/event-tv-channels`
- **What:** SofaScore event TV channels. Returns where a match is broadcast. `available_countries` lists every country that has a broadcast with its channel ids; those country codes are the valid values for `country`. With `country` set (a two-letter ISO 3166-1 alpha-2 code such as `GB`, any case) the response also resolves that country's `channels` to names, using one extra upstream call. A well-formed country code the match is not broadcast in returns 404, and so does a match with no broadcast information.
- **Params:** `country` (string, optional) — Two-letter ISO 3166-1 alpha-2 country code. Omit to list the broadcasting countries only; `id` (string, **required**) — Numeric SofaScore event (match) id

### `sofascore_event_votes`

- **HTTP:** `GET /sofascore/event-votes`
- **What:** SofaScore event votes. Returns a match's community vote tallies: the match result vote (`match_result` with `home`, `away`, `total` and `draw`, where `draw` is absent for two-way sports such as basketball and tennis), both teams to score, which team scores first and who should have won (when SofaScore has opened that vote). A block that holds no votes is omitted. Returns 404 when SofaScore has no votes for the match.
- **Params:** `id` (string, **required**) — Numeric SofaScore event (match) id

### `sofascore_live_events`

- **HTTP:** `GET /sofascore/live-events`
- **What:** SofaScore live events. Returns currently live events for a sport. The `sport` enum accepts `american-football`, `aussie-rules`, `badminton`, `bandy`, `baseball`, `basketball`, `beach-volley`, `cricket`, `darts`, `esports`, `floorball`, `football`, `futsal`, `handball`, `ice-hockey`, `mma`, `minifootball`, `padel`, `rugby`, `snooker`, `table-tennis`, `tennis`, `volleyball`, and `waterpolo`; the sports endpoint lists them. An empty `events` list is a valid response when nothing is live right now.
- **Params:** `sport` (string, **required**) — Sport key

### `sofascore_manager`

- **HTTP:** `GET /sofascore/manager`
- **What:** SofaScore manager detail. Returns a manager's (coach's) profile (nationality, birth date, preferred formation, current team and teams, and the career win/draw/loss and goals record). Get a manager id from sofascore-search results of type `manager`.
- **Params:** `id` (string, **required**) — Numeric SofaScore manager id

### `sofascore_manager_events`

- **HTTP:** `GET /sofascore/manager-events`
- **What:** SofaScore manager recent matches. Returns a page of the matches a manager (coach) has recently taken charge of, newest first, across all clubs they managed. Only past matches are available; SofaScore publishes no upcoming list for managers. Returns 404 for a page past the end of the manager's history.
- **Params:** `id` (string, **required**) — Numeric SofaScore manager id; `page` (integer, optional) — Zero-based page number

### `sofascore_mma_card`

- **HTTP:** `GET /sofascore/mma-card`
- **What:** SofaScore MMA card. Returns the bouts of one MMA fight card, main event first, narrowed with `part` to `all` bouts, the `maincard`, the `prelims` or the `earlyprelims`. Each bout has the fighters (country, nickname, ranking where 0 is the champion, record), weight class, scheduled rounds, status, and for finished bouts the winner, win type, final round and fight time. Get `org_id` and `card_id` from sofascore-mma-schedule. Returns 404 when the card is unknown or has no bouts in that segment (for example a card without early prelims).
- **Params:** `card_id` (string, **required**) — Numeric card id (card_id) from sofascore-mma-schedule; `org_id` (string, **required**) — Numeric SofaScore MMA organisation id; `part` (string, **required**) — Which segment of the card to return

### `sofascore_mma_schedule`

- **HTTP:** `GET /sofascore/mma-schedule`
- **What:** SofaScore MMA schedule. Returns the main event of every fight card an MMA organisation holds in one calendar month, with the card id and name, fighters (country, nickname, ranking where 0 is the champion, record), weight class, scheduled rounds, status, and for finished fights the winner, win type and final round. Find organisation ids (UFC 19906, PFL 19910, ONE 20269, Rizin 19905, Fight Nation Championship 20463, KSW 19946, OKTAGON 20258, Absolute Championship Akhmat 20254, Cage Warriors 19909, Dana White's Contender Series 20264, Brave CF 20267, Jungle Fight 20253) with sofascore-categories (sport `mma`) and sofascore-category-tournaments (category 1708). Use the `card_id` with sofascore-mma-card to read every bout. Returns 404 when the organisation has no card in that month or the id is not an MMA organisation.
- **Params:** `month` (string, **required**) — Calendar month as YYYY-MM; `org_id` (string, **required**) — Numeric SofaScore MMA organisation id

### `sofascore_odds_dropping`

- **HTTP:** `GET /sofascore/odds-dropping`
- **What:** SofaScore dropping odds. Returns SofaScore's dropping odds list for a sport: about twenty upcoming events whose odds moved most, each as the usual event summary plus the `choice_name` and `percentage` SofaScore reports for the move (returned as supplied) and the market with opening and current prices (`change` is 1 above the opening price, -1 below it, 0 unchanged). The `sport` enum accepts `all` and the SofaScore sport keys; it defaults to `all`. A sport with no qualifying events at the moment (for example esports when probed) returns 404.
- **Params:** `sport` (string, optional) — Sport key, or all for every sport. Defaults to all

### `sofascore_odds_winning`

- **HTTP:** `GET /sofascore/odds-winning`
- **What:** SofaScore winning odds. Returns SofaScore's winning odds list for a sport: about twenty upcoming events whose favourite SofaScore highlights, each as the usual event summary plus `winning_odds` (fractional), the `expected` and `actual` percentages SofaScore reports for it (returned as supplied) and the full-time market with opening and current prices (`change` is 1 above the opening price, -1 below it, 0 unchanged). The `sport` enum accepts `all` and the SofaScore sport keys; it defaults to `all`. A sport with no qualifying events at the moment (for example baseball, cricket and esports when probed) returns 404.
- **Params:** `sport` (string, optional) — Sport key, or all for every sport. Defaults to all

### `sofascore_player`

- **HTTP:** `GET /sofascore/player`
- **What:** SofaScore player detail. Returns one SofaScore player by numeric `id`: name, short name, position, jersey number, date of birth, height, preferred foot, country, market value and currency, and the current team. `deceased` is `true` for historical players. An unknown or malformed id returns an upstream error.
- **Params:** `id` (string, **required**) — Numeric SofaScore player id

### `sofascore_player_attributes`

- **HTTP:** `GET /sofascore/player-attributes`
- **What:** SofaScore player attributes and characteristics. Returns a football player's attribute scores (0 to 100) for the current year and up to three earlier years (`year_shift` 0 to 3), the average scores for the player's position, and the player's characteristics: playing positions plus strengths and weaknesses, each with SofaScore's numeric `code`, a `key` and `name` such as finishing or aerial duels, and a `rank`. Outfield players carry attacking, technical, tactical, defending and creativity scores; goalkeepers carry saves, anticipation, ball_distribution, aerial and tactical. Combines two SofaScore requests. Returns 404 for players without attribute overviews, which includes non-football players.
- **Params:** `id` (string, **required**) — Numeric SofaScore player id

### `sofascore_player_events`

- **HTTP:** `GET /sofascore/player-events`
- **What:** SofaScore player matches with per-match numbers. Returns one page (30 matches) of a player's matches, each with the player's own numbers merged in: `statistics` (football: rating and minutes_played; basketball: points, rebounds, assists and more), `incident_counts` (goals, assists, yellow and red cards, penalty goals), `on_bench` for an unused substitute and `played_for_team_id` (club or national team). Page 0 is the most recent window and can include upcoming fixtures (status type `notstarted`); matches inside a page run oldest first. Follow `has_next_page` for older pages; a page past the end returns 404.
- **Params:** `id` (string, **required**) — Numeric SofaScore player id; `page` (integer, optional) — Zero-based page number. Defaults to 0

### `sofascore_player_last_year_summary`

- **HTTP:** `GET /sofascore/player-last-year-summary`
- **What:** SofaScore player form over the last year. Returns a player's form timeline over roughly the last year: `summary` entries, each with a `type`, a date and (where it applies) a competition. `event` is a rated match (the rating is in `value` as published and as a number in `rating`, the competition in `tournament_id`); `injury` is an injury period whose `value` is an opaque number; `missing` is a match the player missed; `transfer` is a transfer date. `tournaments` describes the competitions referenced. An empty `summary` is a valid response for a player with no rated appearance in the period.
- **Params:** `id` (string, **required**) — Numeric SofaScore player id

### `sofascore_player_national_team_statistics`

- **HTTP:** `GET /sofascore/player-national-team-statistics`
- **What:** SofaScore player national team record. Returns a player's national team record: for each national team the appearances, goals and debut date. An empty `teams` list is a valid response for a player who never played internationally.
- **Params:** `id` (string, **required**) — Numeric SofaScore player id

### `sofascore_player_penalty_history`

- **HTTP:** `GET /sofascore/player-penalty-history`
- **What:** SofaScore player penalty history. Returns the penalties a player has taken, newest first: the totals (`attempts`, `scored`) and, per penalty, the outcome (`goal`, `miss`, `post` or `save`), the zone of the goal (for example `low-right`, `high-left`, `close-high`), the x and y position in the goal mouth on SofaScore's 0 to 100 scale, the expected-goals value when available and the match. Returns 404 for players with no recorded penalties, such as most goalkeepers and defenders.
- **Params:** `id` (string, **required**) — Numeric SofaScore player id

### `sofascore_player_ratings`

- **HTTP:** `GET /sofascore/player-ratings`
- **What:** SofaScore player match ratings for a season. Returns a player's rating in every match of one competition season, newest first, with the opponent, home or away and the match. The `type` enum accepts `overall`, `home`, `away`, `regular_season` and `playoffs` and defaults to `overall`; football seasons answer `overall` and NBA seasons answer `regular_season` and `playoffs` (the types a season offers are listed by player-statistics-seasons). Returns 404 when SofaScore has no ratings of that type for the combination.
- **Params:** `id` (string, **required**) — Numeric SofaScore player id; `season` (string, **required**) — Numeric SofaScore season id from player-statistics-seasons; `tournament_id` (string, **required**) — Numeric SofaScore unique-tournament (competition) id from player-statistics-seasons; `type` (string, optional) — Statistics view

### `sofascore_player_season_heatmap`

- **HTTP:** `GET /sofascore/player-season-heatmap`
- **What:** SofaScore player season heatmap. Returns a football player's aggregated touch locations over one competition season: `points` with an `x`, `y` and touch `count` on SofaScore's 0-100 pitch scale, the number of `matches` behind it and the matched `events`. Get `tournament_id` and `season` from player-statistics-seasons. The response is large for a full league season. Returns 404 when SofaScore has no heatmap for that player, competition and season, which includes sports other than football and seasons the player did not play.
- **Params:** `id` (string, **required**) — Numeric SofaScore player id; `season` (string, **required**) — Numeric SofaScore season id; `tournament_id` (string, **required**) — Numeric SofaScore unique-tournament (competition) id

### `sofascore_player_season_statistics`

- **HTTP:** `GET /sofascore/player-season-statistics`
- **What:** SofaScore player season statistics. Returns a player's statistics for one competition season (appearances, rating, goals, assists, passing, duels, and more) as a snake_case metric map, plus the team and a rating breakdown when available. The `type` enum accepts `overall`, `home`, `away`, `regular_season`, and `playoffs` and defaults to `overall`; only the types listed for that season by player-statistics-seasons exist (football players have `overall`, `home`, `away`; basketball, ice hockey and baseball players have `regular_season` and `playoffs`). Returns 404 when SofaScore has no statistics of that type for the combination.
- **Params:** `id` (string, **required**) — Numeric SofaScore player id; `season` (string, **required**) — Numeric SofaScore season id from player-statistics-seasons; `tournament_id` (string, **required**) — Numeric SofaScore unique-tournament (competition) id from player-statistics-seasons; `type` (string, optional) — Statistics view

### `sofascore_player_statistical_rankings`

- **HTTP:** `GET /sofascore/player-statistical-rankings`
- **What:** SofaScore player ranking among all players in a season. Returns where a football player ranks against every other player of the competition season for about 78 statistics (goals, assists, rating, expected goals, passes, duels, distance covered and more): the `value`, the `rank` (tied values share a rank), the number of ranked players (`count`) and the tie-broken `order`. Statistics are snake_case and sorted alphabetically. The `type` enum accepts only `overall`, which is also the default; the other statistics views answer 404. Returns 404 for players without a ranking in that season, which includes basketball players.
- **Params:** `id` (string, **required**) — Numeric SofaScore player id; `season` (string, **required**) — Numeric SofaScore season id from player-statistics-seasons; `type` (string, optional) — Statistics view

### `sofascore_player_statistics_seasons`

- **HTTP:** `GET /sofascore/player-statistics-seasons`
- **What:** SofaScore player statistics seasons. Lists the competitions and seasons a player has statistics for, with the statistics `types` available for each season. Use a returned competition id (`unique_tournament_id`), season `id` and one of its `types` with player-season-statistics. The `types` values are `overall`, `home`, `away`, `regular_season`, and `playoffs`. Returns 404 for players with no tracked statistics (for example tennis players).
- **Params:** `id` (string, **required**) — Numeric SofaScore player id

### `sofascore_player_tournaments`

- **HTTP:** `GET /sofascore/player-tournaments`
- **What:** SofaScore player competitions. Lists every competition a player has played in, with id, name, slug, category, sport and gender. It includes competitions without season statistics (cups, friendlies, all-star games) that player-statistics-seasons leaves out. Returns 404 when SofaScore has no competitions for the player.
- **Params:** `id` (string, **required**) — Numeric SofaScore player id

### `sofascore_player_transfers`

- **HTTP:** `GET /sofascore/player-transfers`
- **What:** SofaScore player transfer history. Returns a player's transfer history (clubs moved from and to, date, fee, and SofaScore's numeric transfer type code), newest first. An empty `transfers` list is a valid response for a player who has never moved clubs. Returns 404 when SofaScore has no transfer record for the player (seen for ice hockey and baseball players). The `type_code` values are SofaScore's own opaque codes and are not translated.
- **Params:** `id` (string, **required**) — Numeric SofaScore player id

### `sofascore_ranking_types`

- **HTTP:** `GET /sofascore/ranking-types`
- **What:** SofaScore ranking catalogue. Lists every ranking available from the sofascore rankings endpoint: the numeric `type` id, a descriptive name, the sport, the gender and the kind of entity that is ranked (`team`, `player` or `unique_tournament`). Covers 32 rankings across football (league coefficients, FIFA national teams, club coefficients), rugby, tennis (ATP and WTA official and live rankings, UTR), padel and MMA (UFC and Fight Nation Championship divisions). The catalogue is a fixed list and costs no upstream request.
- **Params:** _none_

### `sofascore_rankings`

- **HTTP:** `GET /sofascore/rankings`
- **What:** SofaScore rankings. Returns one SofaScore ranking list: the rank, previous rank, points and the ranked team, player or competition, plus when the list was last updated. Choose the `type` id from sofascore-ranking-types, for example 5 for the ATP men's singles ranking or 2 for the FIFA men's national team ranking. Optional `limit` returns only the first rows of long lists (tennis lists hold 500 rows). MMA division rankings use rank 0 for the reigning champion.
- **Params:** `limit` (integer, optional) — Return only the first N rows, 1 to 500. Omit to return every row; `type` (integer, **required**) — Ranking id from sofascore-ranking-types

### `sofascore_referee`

- **HTTP:** `GET /sofascore/referee`
- **What:** SofaScore referee profile. Returns a referee's profile: name, country, sport, career matches officiated and career yellow, red and yellow-red card totals, plus date of birth and first league debut when SofaScore records them. Get the referee id from the `referee.id` of the sofascore-event endpoint or from a sofascore-search result of type referee. Returns 404 for an unknown id.
- **Params:** `id` (string, **required**) — Numeric SofaScore referee id

### `sofascore_referee_events`

- **HTTP:** `GET /sofascore/referee-events`
- **What:** SofaScore referee officiated matches. Returns one page (30 matches) of the matches a referee officiated, most recent first, across every competition. Follow `has_next_page` for older pages; a page past the end returns 404. Only past matches exist (no upcoming list), and the list includes canceled and postponed fixtures (their `status.type` says so), which the career match total of sofascore-referee does not count.
- **Params:** `id` (string, **required**) — Numeric SofaScore referee id; `page` (integer, optional) — Zero-based page number. Defaults to 0

### `sofascore_referee_statistics`

- **HTTP:** `GET /sofascore/referee-statistics`
- **What:** SofaScore referee card statistics. Returns a referee's record per competition: matches officiated, yellow cards, red cards, yellow-red cards and penalties awarded. The per-competition appearances add up to the career matches in sofascore-referee. An empty `competitions` list is valid for a referee with no recorded competitions.
- **Params:** `id` (string, **required**) — Numeric SofaScore referee id

### `sofascore_round_events`

- **HTTP:** `GET /sofascore/round-events`
- **What:** SofaScore round fixtures. Returns fixtures for one round of a competition season. Get `id` from search or category-tournaments, `season` from tournament-seasons, and the round values from tournament-rounds. Round numbers are not unique in cups, and knockout or named rounds return 404 unless the round's `slug` is passed (plus its `prefix` when tournament-rounds lists one): the UEFA Champions League has a qualifying and a league-phase round 1, and a playoff round 636 both with the `Qualification` prefix and without. Plain numbered league rounds need only `round`. `slug` is lowercase letters, digits, and hyphens (up to 64 characters); `prefix` is letters, digits, spaces, and hyphens (up to 64 characters) and is only valid together with `slug`.
- **Params:** `id` (string, **required**) — Numeric SofaScore unique-tournament (competition) id; `prefix` (string, optional) — Round prefix from tournament-rounds, for example Qualification; only valid together with slug; `round` (integer, **required**) — Round number; `season` (string, **required**) — Numeric SofaScore season id; `slug` (string, optional) — Round slug from tournament-rounds, for example round-of-16; required for knockout and named cup rounds

### `sofascore_scheduled_events`

- **HTTP:** `GET /sofascore/scheduled-events`
- **What:** SofaScore events scheduled in a category on a date. Returns the events (matches) in one category, such as a country, that start on a UTC date, ordered by start time. Get the category `id` from the categories endpoint (or `category_id` from scheduled-tournaments). `date` must be a real calendar date written `YYYY-MM-DD` and is a UTC day; to cover a local day in another timezone, request the neighbouring dates and filter on `start_timestamp`. An empty `events` list is a valid response when the category has no fixtures that day. Returns 404 for an unknown category id.
- **Params:** `category_id` (string, **required**) — Numeric SofaScore category id from the categories endpoint; `date` (string, **required**) — UTC calendar date, YYYY-MM-DD

### `sofascore_scheduled_tournaments`

- **HTTP:** `GET /sofascore/scheduled-tournaments`
- **What:** SofaScore tournaments scheduled on a date. Returns one page of the tournaments that have fixtures on a UTC date for a sport, each with the number of events starting that UTC day. This lists competitions, not matches: use scheduled-events with a tournament's `category_id` for the matches, or its `unique_tournament_id` with the tournament-seasons and round endpoints. `date` must be a real calendar date written `YYYY-MM-DD`. Pages are one-based; follow `has_next_page`. The `sport` enum accepts `american-football`, `aussie-rules`, `badminton`, `bandy`, `baseball`, `basketball`, `beach-volley`, `cricket`, `darts`, `esports`, `floorball`, `football`, `futsal`, `handball`, `ice-hockey`, `mma`, `minifootball`, `padel`, `rugby`, `snooker`, `table-tennis`, `tennis`, `volleyball`, and `waterpolo`. An empty `tournaments` list is a valid response for a date with no fixtures or a page past the last one.
- **Params:** `date` (string, **required**) — UTC calendar date, YYYY-MM-DD; `page` (integer, optional) — One-based page number; defaults to 1; `sport` (string, **required**) — Sport key

### `sofascore_search`

- **HTTP:** `GET /sofascore/search`
- **What:** SofaScore universal search. Searches SofaScore for teams, players, and competitions matching a free-text query. An empty `results` list is a valid response when nothing matches.
- **Params:** `q` (string, **required**) — Free-text search query

### `sofascore_search_typed`

- **HTTP:** `GET /sofascore/search-typed`
- **What:** SofaScore search by entity type. Searches SofaScore for one entity type and returns up to 20 ranked results per page: `events` (matches), `teams`, `players` (with team and position), `managers`, `referees`, `venues` (with city and capacity) and `unique_tournaments` (competitions with category). Page with the zero-based `page`; an empty page means there are no further results. The optional `sport` filter (any key listed by sofascore/sports, such as `football`, `basketball`, `tennis` or `mma`) narrows `teams`, `players`, `managers` and `unique_tournaments`, and is rejected for `events`, `referees` and `venues`, which ignore it. Use the returned ids with the matching endpoints (team, player, manager, venue, tournament-seasons, event).
- **Params:** `page` (integer, optional) — Zero-based page number. Defaults to 0; `q` (string, **required**) — Search text, up to 128 characters; `sport` (string, optional) — Restrict teams, players, managers or unique_tournaments to one sport; `type` (string, **required**) — Entity type to search

### `sofascore_season_events`

- **HTTP:** `GET /sofascore/season-events`
- **What:** SofaScore season fixtures and results. Returns one page (about 30 events) of every fixture or result of a competition season, with the round of each event. The `direction` enum accepts `next` (upcoming fixtures) and `last` (finished results). Follow `has_next_page` to read further pages: a page past the end, a direction with no events (for example `next` in a finished season) and a season id that does not belong to the competition all answer 404. Get `id` from search and `season` from tournament-seasons.
- **Params:** `direction` (string, **required**) — Upcoming fixtures or finished results; `id` (string, **required**) — Numeric SofaScore unique-tournament (competition) id; `page` (integer, optional) — Zero-based page number. Defaults to 0; `season` (string, **required**) — Numeric SofaScore season id

### `sofascore_sports`

- **HTTP:** `GET /sofascore/sports`
- **What:** SofaScore supported sports. Lists every sport key the SofaScore endpoints accept (the `sport` enum of live-events, categories, and scheduled-tournaments), with live and total event counts when available. The list is fixed and always complete; if the live counts cannot be read, `counts_available` is `false` and the per-sport counts are omitted instead of failing the call. Counts are also omitted for a sport the count feed does not cover (for example `mma`). Accepted sport keys: `american-football`, `aussie-rules`, `badminton`, `bandy`, `baseball`, `basketball`, `beach-volley`, `cricket`, `darts`, `esports`, `floorball`, `football`, `futsal`, `handball`, `ice-hockey`, `mma`, `minifootball`, `padel`, `rugby`, `snooker`, `table-tennis`, `tennis`, `volleyball`, `waterpolo`.
- **Params:** _none_

### `sofascore_stage`

- **HTTP:** `GET /sofascore/stage`
- **What:** SofaScore motorsport and cycling stage. Returns one stage from SofaScore's stage hierarchy: a season (Formula 1 2026), an event (a Grand Prix weekend, a NASCAR race, a rally, a cycling race), a session (practice, qualifying, sprint, race) or a cycling stage. The response has its type (`Season`, `Event`, `Practice`, `Qualifying`, `Qualifying part`, `Race`, `Sprint race`, `Sprint qualifying`, `Practice part`, `Stage`), status (`finished`, `notstarted`, `canceled`), start time, country, competition, parent stage (the season of an event, the event of a session), the winner once decided, and circuit, weather and race facts where published (laps, race distance, lap record, safety car, NASCAR cautions, rally special stages, cycling route). `info` fields are omitted when not published, never zero. A season has no status. Stage ids and competition ids are different id spaces. Returns 404 for an unknown stage id.
- **Params:** `id` (string, **required**) — Numeric SofaScore stage id from stage-schedule, stage-seasons or stage-substages

### `sofascore_stage_categories`

- **HTTP:** `GET /sofascore/stage-categories`
- **What:** SofaScore motorsport and cycling categories and competitions. Lists the categories SofaScore keeps for a stage sport, each with its competitions. For `motorsport` that is the racing series (Formula 1, MotoGP, Moto2, Moto3, Superbike, NASCAR with its Cup, Truck and Xfinity competitions, WRC, Formula E, Indycar, DTM); for `cycling` it is Cycling Men and Cycling Women. Use a competition `id` with stage-seasons to list its seasons. Some categories exist without any competition (for example Motocross, Speedway, WEC) and return an empty `competitions` list. Motorsport and cycling are not available on the match-based endpoints (live-events, categories, scheduled-events); they use the stage endpoints. The `sport` enum accepts `motorsport` and `cycling`.
- **Params:** `sport` (string, **required**) — Stage sport key

### `sofascore_stage_driver_performance`

- **HTTP:** `GET /sofascore/stage-driver-performance`
- **What:** SofaScore motorsport race progress per driver. Returns every competitor's progress through a finished race or rally. For circuit races (Formula 1, MotoGP and similar) `laps` lists the position at the end of each lap, starting with lap 0 for the grid, plus the tyre compound and a `pit_stop` flag where published; the lap a driver retired has `retired` set and no position. For rallies `stage_positions` lists the overall position after each special stage. The response also repeats the stage itself. It is published for races and sprints of some series (verified for Formula 1, MotoGP and WRC) and not for practice, qualifying, NASCAR, cycling, events or seasons, which return 404. Returns 404 for an unknown id.
- **Params:** `id` (string, **required**) — Numeric SofaScore stage id of a finished race, sprint or rally

### `sofascore_stage_featured`

- **HTTP:** `GET /sofascore/stage-featured`
- **What:** SofaScore featured motorsport and cycling events. Returns the events SofaScore features for a stage sport right now: a mix of the latest finished events (with `winner` and result facts such as laps and circuit) and the next upcoming ones, across series such as Formula 1, MotoGP, Moto2, Moto3, Superbike, NASCAR and cycling races. Each event carries its competition, season name, parent season stage and country. Use an event `id` with stage-substages for its sessions or stages and stage-standings for results. The `sport` enum accepts `motorsport` and `cycling`.
- **Params:** `sport` (string, **required**) — Stage sport key

### `sofascore_stage_schedule`

- **HTTP:** `GET /sofascore/stage-schedule`
- **What:** SofaScore motorsport and cycling events around a date. Returns the events SofaScore lists for a stage sport around a UTC date: Grand Prix weekends, NASCAR race weekends, rallies and cycling races, each with its country, competition, every session start time (`session_start_timestamps`) and the session SofaScore highlights (`session`: the live, next or latest one). The list is not a strict one-day filter. It holds the events in progress on the date plus the next upcoming ones, and a quiet date still returns the next events; use `on_date`, which is true when a session of the event starts inside the requested UTC day, to separate them. Schedule rows carry no event status or winner: use `session.status`, or pass the event `id` to stage for the event detail and to stage-substages for its sessions. `date` must be a real calendar date written `YYYY-MM-DD`. An empty `stages` list is valid when nothing is in progress or scheduled nearby. The `sport` enum accepts `motorsport` and `cycling`.
- **Params:** `date` (string, **required**) — UTC calendar date, YYYY-MM-DD; `sport` (string, **required**) — Stage sport key

### `sofascore_stage_seasons`

- **HTTP:** `GET /sofascore/stage-seasons`
- **What:** SofaScore seasons of a motorsport or cycling competition. Returns the seasons of one stage competition, newest first, for example Formula 1 2026 (id 214140) back to 1950. A season `id` is a stage id: pass it to stage-substages for the race calendar and to stage-standings for the championship table. The season still in progress has no `end_timestamp`. Get the competition `id` from stage-categories (for example 40 for Formula 1, 17 for MotoGP, 18 for the NASCAR Cup Series, 9 for Cycling Men). Competition ids and stage ids are different id spaces, so a competition id passed to stage returns an unrelated stage. Returns 404 for an unknown competition id.
- **Params:** `id` (string, **required**) — Numeric SofaScore competition id from stage-categories

### `sofascore_stage_standings`

- **HTTP:** `GET /sofascore/stage-standings`
- **What:** SofaScore motorsport and cycling stage standings. Returns one classification of a stage. For a race or sprint it is the result (position, grid, race time, gap, interval, laps, laps led, pit stops, tyre stints, fastest lap, points, retirement status); for practice and qualifying the timing order (`time` is the best lap); for a cycling stage the stage result with time gaps; for an event the event aggregate; for a season the championship table (points, victories, races started, pole positions, podiums, fastest laps; NASCAR adds top 5, top 10 and races not finished). `competitor` returns drivers and riders, `team` returns constructors and teams, which only some seasons and events publish (verified for the Formula 1 and MotoGP seasons and the Formula 1 event; races, NASCAR, WRC and cycling return 404 for `team`). Rows are in upstream order. `position` is omitted for competitors who did not finish or set no time, and `gap` is `DNF` for a retirement. The parent session of a split qualifying has no standings; use the ids of its parts from stage-substages. Fields a classification does not publish are omitted. Returns 404 for an unknown id, a stage that has no results yet, or a kind of stage without that classification. The `type` enum accepts `competitor` and `team`.
- **Params:** `id` (string, **required**) — Numeric SofaScore stage id of a season, event, session or cycling stage; `type` (string, **required**) — Classification kind

### `sofascore_stage_substages`

- **HTTP:** `GET /sofascore/stage-substages`
- **What:** SofaScore children of a motorsport or cycling stage. Returns the children of a stage in upstream order. For a season it is the race calendar: every event with status (`finished`, `notstarted`, `canceled`), dates, round, circuit and winner. For an event it is the sessions: practices, qualifying, sprint qualifying, sprint and race for a Grand Prix, the numbered stages of a cycling race or rally. Qualifying and practice sessions list their `parts`, and the part ids carry the timing results (the parent session of a split qualifying has no standings of its own). Use a child `id` with stage for detail, stage-standings for its results and stage-driver-performance for race progress. A race, session or cycling stage has no children and returns 404, as does an unknown id.
- **Params:** `id` (string, **required**) — Numeric SofaScore stage id of a season or an event

### `sofascore_standings`

- **HTTP:** `GET /sofascore/standings`
- **What:** SofaScore standings. Returns a league table for a competition season. The `type` enum accepts `total`, `home`, and `away`. Get `id` from search and `season` from tournament-seasons.
- **Params:** `id` (string, **required**) — Numeric SofaScore unique-tournament (competition) id; `season` (string, **required**) — Numeric SofaScore season id; `type` (string, **required**) — Standings variant

### `sofascore_team`

- **HTTP:** `GET /sofascore/team`
- **What:** SofaScore team detail. Returns one SofaScore team by numeric `id`: name, short name, country, sport, manager, venue with its city and capacity, primary colour, and national-team flag. `tournament_id` and `tournament_name` give the team's primary competition, such as its domestic league. An unknown id returns an upstream error.
- **Params:** `id` (string, **required**) — Numeric SofaScore team id

### `sofascore_team_achievements`

- **HTTP:** `GET /sofascore/team-achievements`
- **What:** SofaScore team trophies. Returns the trophies a team has won: the total and, per competition, the number won and the winning seasons (newest first, with the season id where SofaScore tracks it). Some competitions, such as US leagues, report a count with an empty or shorter `seasons` list. Returns 404 when SofaScore records no achievements for the team.
- **Params:** `id` (string, **required**) — Numeric SofaScore team id

### `sofascore_team_events`

- **HTTP:** `GET /sofascore/team-events`
- **What:** SofaScore team fixtures. Returns a page of a team's upcoming or recent fixtures. The `direction` enum accepts `next` and `last`. An empty `events` list is a valid response when there is no fixture on that page.
- **Params:** `direction` (string, **required**) — Fixture direction; `id` (string, **required**) — Numeric SofaScore team id; `page` (integer, optional) — Zero-based page number

### `sofascore_team_goal_distributions`

- **HTTP:** `GET /sofascore/team-goal-distributions`
- **What:** SofaScore team goals by match minute. Returns a football team's goals scored and conceded per block of match minutes (1-15, 16-30, 31-45, 46-60, 61-75, 76-90) for one competition season, in three views: `overall`, `home` and `away`, each with the matches played and the goal totals. A block with no goals is returned as 0. Returns 404 for non-football teams and for a team and season that do not belong together.
- **Params:** `id` (string, **required**) — Numeric SofaScore team id; `season` (string, **required**) — Numeric SofaScore season id; `tournament_id` (string, **required**) — Numeric SofaScore unique-tournament (competition) id of a football competition

### `sofascore_team_near_events`

- **HTTP:** `GET /sofascore/team-near-events`
- **What:** SofaScore team previous and next match. Returns a team's last played match and its next scheduled match with teams, competition, status, score and start time. Either side can be missing (a team with no upcoming fixture returns only `previous_event`). Returns 404 when SofaScore has neither. For full fixture lists use team-events.
- **Params:** `id` (string, **required**) — Numeric SofaScore team id

### `sofascore_team_of_the_week`

- **HTTP:** `GET /sofascore/team-of-the-week`
- **What:** SofaScore team of the week. Returns one team of the week: the formation and the selected players with their SofaScore rating, team and, for round and weekly selections, the match the rating was earned in. Get the `period` id from sofascore-team-of-the-week-periods; a period that does not belong to the given competition season is rejected with 400.
- **Params:** `id` (string, **required**) — Numeric SofaScore unique-tournament (competition) id; `period` (string, **required**) — Numeric period id from sofascore-team-of-the-week-periods; `season` (string, **required**) — Numeric SofaScore season id

### `sofascore_team_of_the_week_periods`

- **HTTP:** `GET /sofascore/team-of-the-week-periods`
- **What:** SofaScore team of the week periods. Lists the periods of a competition season for which SofaScore published a team of the week, newest first: league rounds (`round`), weekly time spans (`timespan`) and season-level selections (`season`, such as an NBA regular season or playoff team). Use a returned period `id` with sofascore-team-of-the-week. An empty list is valid when no team of the week has been published yet. Get `id` from search and `season` from tournament-seasons.
- **Params:** `id` (string, **required**) — Numeric SofaScore unique-tournament (competition) id; `season` (string, **required**) — Numeric SofaScore season id

### `sofascore_team_performance`

- **HTTP:** `GET /sofascore/team-performance`
- **What:** SofaScore team recent performance. Returns a team's most recent matches (about ten, oldest first) with SofaScore's per-match performance value in `points`: higher is better and a heavy defeat is negative. An event SofaScore gave no value for has no `points`. An empty `events` list is a valid response for a team with no recent matches.
- **Params:** `id` (string, **required**) — Numeric SofaScore team id

### `sofascore_team_player_statistics`

- **HTTP:** `GET /sofascore/team-player-statistics`
- **What:** SofaScore team player statistics. Returns the statistics of every player in a team's squad for one competition season, each as a snake_case metric map (appearances, minutes, rating, goals, assists, passing and duel metrics for football; points, rebounds and assists for basketball), in SofaScore's order. The `type` enum accepts `overall`, `home`, `away`, `regular_season` and `playoffs` and defaults to `overall`; only the types listed for that season by team-player-statistics-seasons exist (football `overall`, `home`, `away`; NBA `regular_season`, `playoffs`). A metric SofaScore did not record is omitted rather than returned as 0. Returns 404 when SofaScore has no statistics of that type for the combination.
- **Params:** `id` (string, **required**) — Numeric SofaScore team id; `season` (string, **required**) — Numeric SofaScore season id from team-player-statistics-seasons; `tournament_id` (string, **required**) — Numeric SofaScore unique-tournament (competition) id from team-player-statistics-seasons; `type` (string, optional) — Statistics view

### `sofascore_team_player_statistics_seasons`

- **HTTP:** `GET /sofascore/team-player-statistics-seasons`
- **What:** SofaScore team player statistics seasons. Lists the competitions and seasons for which SofaScore has per-player statistics for a team, with the statistics `types` available in each season (`overall`, `home`, `away`, `regular_season`, `playoffs`). Use it to find the `tournament_id`, `season` and `type` accepted by team-player-statistics and team-top-players. Football teams offer `overall`, `home` and `away`; NBA teams offer `regular_season` and `playoffs`. Returns 404 when SofaScore has no player statistics for the team.
- **Params:** `id` (string, **required**) — Numeric SofaScore team id

### `sofascore_team_players`

- **HTTP:** `GET /sofascore/team-players`
- **What:** SofaScore team players. Returns a team's full squad from SofaScore by team id: each player's name, position, jersey number, date of birth, height, country and preferred foot, plus SofaScore's market value estimate and its currency when available.
- **Params:** `id` (string, **required**) — Numeric SofaScore team id

### `sofascore_team_rankings`

- **HTTP:** `GET /sofascore/team-rankings`
- **What:** SofaScore team rankings. Returns every ranking a team or tennis player appears in: for a tennis player the ATP or WTA ranking, its live version and the UTR rating, for a football club the UEFA club coefficient by year. Each ranking carries its `type_id` (the same ids the rankings endpoint takes), name, sport, category and last update, and `rows` with the `position`, `points`, previous and best position where SofaScore reports them. Returns 404 when the id appears in no ranking.
- **Params:** `id` (string, **required**) — Numeric SofaScore team id (a tennis player id for tennis)

### `sofascore_team_season_statistics`

- **HTTP:** `GET /sofascore/team-season-statistics`
- **What:** SofaScore team season statistics. Returns a team's statistics for one competition season (goals, shots, passing, duels, discipline, and the matching conceded-side metrics) as a snake_case metric map. The `type` enum accepts `overall`, `home`, `away`, `regular_season`, and `playoffs` and defaults to `overall`; only the types listed for that season by team-statistics-seasons exist (football teams have `overall` only; basketball, ice hockey and baseball teams have `regular_season` and `playoffs`). Returns 404 when SofaScore has no statistics of that type for the combination.
- **Params:** `id` (string, **required**) — Numeric SofaScore team id; `season` (string, **required**) — Numeric SofaScore season id from team-statistics-seasons; `tournament_id` (string, **required**) — Numeric SofaScore unique-tournament (competition) id from team-statistics-seasons; `type` (string, optional) — Statistics view

### `sofascore_team_statistics_seasons`

- **HTTP:** `GET /sofascore/team-statistics-seasons`
- **What:** SofaScore team statistics seasons. Lists the competitions and seasons a team has statistics for, with the statistics `types` available for each season. Use a returned competition id (`unique_tournament_id`), season `id` and one of its `types` with team-season-statistics. The `types` values are `overall`, `home`, `away`, `regular_season`, and `playoffs`. Returns 404 for teams with no tracked statistics.
- **Params:** `id` (string, **required**) — Numeric SofaScore team id

### `sofascore_team_top_players`

- **HTTP:** `GET /sofascore/team-top-players`
- **What:** SofaScore team top players. Returns a team's best players for every statistic category SofaScore ranks within the team and season (rating, goals, assists, expected goals, tackles, saves and more for football; points, rebounds and assists for basketball), each as a ranked list with player, team and value. The category set depends on the sport, so the response lists every category it holds. The `type` enum accepts `overall`, `regular_season` and `playoffs`: football competitions publish `overall`, the NBA publishes `regular_season` and `playoffs`, and a type the competition does not publish answers 404. Optional `limit` caps the rows per category (up to 50); the payload is large without it.
- **Params:** `id` (string, **required**) — Numeric SofaScore team id; `limit` (integer, optional) — Rows per category, 1 to 50. Omit to return every row; `season` (string, **required**) — Numeric SofaScore season id from team-player-statistics-seasons; `tournament_id` (string, **required**) — Numeric SofaScore unique-tournament (competition) id from team-player-statistics-seasons; `type` (string, optional) — Statistics scope

### `sofascore_team_tournaments`

- **HTTP:** `GET /sofascore/team-tournaments`
- **What:** SofaScore team competitions. Lists the competitions a team plays in, each with id, name, slug, category and sport. By default (`all=false`) it returns the competitions the team currently takes part in; with `all=true` it returns every competition the team has been recorded in, including friendlies and older tournaments. Competition ids can be used as `tournament_id` elsewhere in the SofaScore endpoints; use team-player-statistics-seasons for the seasons that have statistics. Returns 404 when SofaScore has no competitions for the team.
- **Params:** `all` (boolean, optional) — false returns current competitions, true returns every recorded competition; `id` (string, **required**) — Numeric SofaScore team id

### `sofascore_team_transfers`

- **HTTP:** `GET /sofascore/team-transfers`
- **What:** SofaScore team transfers. Returns a team's recent incoming (`transfers_in`) and outgoing (`transfers_out`) transfers with player, clubs, date, fee, and SofaScore's numeric transfer type code. Empty lists are valid for a quiet transfer window. Returns 404 when SofaScore has no transfer record for the team (seen for ice hockey and baseball teams). The `type_code` values are SofaScore's own opaque codes and are not translated.
- **Params:** `id` (string, **required**) — Numeric SofaScore team id

### `sofascore_tennis_player_grand_slam_results`

- **HTTP:** `GET /sofascore/tennis-player-grand-slam-results`
- **What:** SofaScore tennis player grand slam results. Returns a tennis player's best round at each grand slam (Australian Open, Roland Garros, Wimbledon and US Open) for the last five editions: per edition the `year`, the `season_id`, the best `round` reached and whether the player won it (`winner`). A year without a `round` means no result is recorded for that edition. `id` is the SofaScore team id of a tennis player (tennis players are teams in SofaScore); get it from search or rankings. Returns 404 for ids that are not tennis players.
- **Params:** `id` (string, **required**) — Numeric SofaScore team id of a tennis player

### `sofascore_tournament_cuptree`

- **HTTP:** `GET /sofascore/tournament-cuptree`
- **What:** SofaScore competition knockout tree. Returns the knockout tree(s) of a cup or playoff competition season: every round with its ties, each tie's participants (team or player, seed, winner flag, the earlier tie it advanced from), result and score strings (a shoot-out is appended, such as `1 (4)`), match ids and start time, plus the final and third-place tie. Tennis competitions return two trees (main draw and qualifying). League seasons have no tree and answer 404, as does a season id that does not belong to the competition. Get `id` from search or tournaments-with-feature and `season` from tournament-seasons; pass the returned `event_ids` to the event endpoints.
- **Params:** `id` (string, **required**) — Numeric SofaScore unique-tournament (competition) id of a cup or playoff competition; `season` (string, **required**) — Numeric SofaScore season id

### `sofascore_tournament_info`

- **HTTP:** `GET /sofascore/tournament-info`
- **What:** SofaScore competition info. Returns a competition's metadata (name, sport, category, tier, title holder, most titles, current season dates, divisions above and below, linked competitions). When `season` is given it also returns that season's aggregates: number of competitors and, for football competitions, goals, home wins, away wins, draws, yellow and red cards and the promoted teams. Get `id` from search and `season` from tournament-seasons.
- **Params:** `id` (string, **required**) — Numeric SofaScore unique-tournament (competition) id; `season` (string, optional) — Numeric SofaScore season id. Omit for competition metadata only

### `sofascore_tournament_player_of_the_season`

- **HTTP:** `GET /sofascore/tournament-player-of-the-season`
- **What:** SofaScore player of the season. Returns the player SofaScore names player of the season for a finished competition season: the player, their team, shirt number, average rating, appearances and the statistics scope (`overall`, or `regular_season` for the NBA). A season that is still running, has not been awarded, or does not belong to the competition answers 404. Get `id` from search and `season` from tournament-seasons or tournament-winners.
- **Params:** `id` (string, **required**) — Numeric SofaScore unique-tournament (competition) id; `season` (string, **required**) — Numeric SofaScore season id of a finished season

### `sofascore_tournament_player_statistics`

- **HTTP:** `GET /sofascore/tournament-player-statistics`
- **What:** SofaScore season player statistics table. Returns one page of a football competition season's player statistics table, sortable by a statistic. `order` chooses the statistic to sort by, `direction` the sort direction (`desc` or `asc`), `accumulation` whether values are season totals, per-game averages or per-90-minute averages (`total`, `perGame`, `per90`), and `group` which statistic columns each row carries (`summary`, `attack`, `defence`, `passing`, `goalkeeper`). Page with `limit` (up to 100) and `offset`; `has_next_page` shows whether more rows follow. Optional filters narrow the table: `team` (team ids), `nationality` (SofaScore nationality codes), `position` (`G`, `D`, `M`, `F`), `min_appearances` and `min_minutes`; several filters combine (AND) and several values of one filter are alternatives (OR). The team ids and nationality codes of a season come from tournament-statistics-info. A filter that matches nobody returns an empty `players` list. Other sports return no rows (404). Get `id` from search and `season` from tournament-seasons.
- **Params:** `accumulation` (string, optional) — How statistics are accumulated. Defaults to total; `direction` (string, optional) — Sort direction. Defaults to desc; `group` (string, optional) — Statistic columns returned. Defaults to summary; `id` (string, **required**) — Numeric SofaScore unique-tournament (competition) id of a football competition; `limit` (integer, optional) — Rows per page, 1 to 100. Defaults to 20; `min_appearances` (integer, optional) — Keep players with at least this many appearances, 0 to 1000. Omit for no minimum; `min_minutes` (integer, optional) — Keep players with at least this many minutes played, 0 to 100000. Omit for no minimum; `nationality` (array, optional) — Nationality codes to keep, comma separated, up to 20 (codes from tournament-statistics-info); `offset` (integer, optional) — Rows to skip. Defaults to 0; `order` (string, optional) — Statistic to sort by. Defaults to rating; `position` (array, optional) — Position codes to keep, comma separated; `season` (string, **required**) — Numeric SofaScore season id; `team` (array, optional) — Team ids to keep, comma separated, up to 20 (ids from tournament-statistics-info or tournament-teams)

### `sofascore_tournament_rounds`

- **HTTP:** `GET /sofascore/tournament-rounds`
- **What:** SofaScore competition season rounds. Returns the rounds of a competition season and the current round. Round numbers are not unique in cups: the UEFA Champions League has both a qualifying and a league-phase round 1, and the same playoff round number with and without a `prefix`. To fetch a round's fixtures, pass its `round` to round-events together with its `slug` and, when present, its `prefix`; knockout and named rounds return 404 from round-events without the slug. Plain numbered rounds (a league's round 1 to 38) have no slug. Get `id` from category-tournaments or search and `season` from tournament-seasons. Returns 404 when SofaScore has no rounds for the season (for example a season that has not started).
- **Params:** `id` (string, **required**) — Numeric SofaScore unique-tournament (competition) id; `season` (string, **required**) — Numeric SofaScore season id from tournament-seasons

### `sofascore_tournament_seasons`

- **HTTP:** `GET /sofascore/tournament-seasons`
- **What:** SofaScore competition seasons. Returns the season list for a competition. Use a returned season id with the standings and round-events endpoints.
- **Params:** `id` (string, **required**) — Numeric SofaScore unique-tournament (competition) id

### `sofascore_tournament_statistics_info`

- **HTTP:** `GET /sofascore/tournament-statistics-info`
- **What:** SofaScore player statistics table filters. Returns what the tournament-player-statistics table of a football competition season can be filtered by: the season's teams (ids for the `team` filter), the nationality codes (for the `nationality` filter; SofaScore uses `EN`, `SX`, `WA` and `NX` for the home nations), the position codes `G`, `D`, `M` and `F` (for the `position` filter), and the statistic columns of each `group` value (`summary`, `attack`, `defence`, `passing`, `goalkeeper`). Other sports answer 404. Get `id` from search and `season` from tournament-seasons.
- **Params:** `id` (string, **required**) — Numeric SofaScore unique-tournament (competition) id of a football competition; `season` (string, **required**) — Numeric SofaScore season id

### `sofascore_tournament_team_of_the_season`

- **HTTP:** `GET /sofascore/tournament-team-of-the-season`
- **What:** SofaScore team of the season. Returns the team of the season SofaScore selected for a finished competition season: the formation, when it was created and the selected players (11 in football, 5 in basketball) with position, shirt number, team and average rating. A season that is still running, has no selection, or does not belong to the competition answers 404. Get `id` from search and `season` from tournament-seasons or tournament-winners.
- **Params:** `id` (string, **required**) — Numeric SofaScore unique-tournament (competition) id; `season` (string, **required**) — Numeric SofaScore season id of a finished season

### `sofascore_tournament_teams`

- **HTTP:** `GET /sofascore/tournament-teams`
- **What:** SofaScore teams of a competition season. Returns every team (or, for tennis and other individual sports, every player) entered in a competition season, with id, name, short name, name code, country, gender, type (`0` team, `1` individual player) and, for individual players, the current ranking. Use the team ids with team, team-players and the `team` filter of tournament-player-statistics. A season id that does not belong to the competition, or a field not yet decided, answers 404. Get `id` from search and `season` from tournament-seasons.
- **Params:** `id` (string, **required**) — Numeric SofaScore unique-tournament (competition) id; `season` (string, **required**) — Numeric SofaScore season id

### `sofascore_tournament_top_players`

- **HTTP:** `GET /sofascore/tournament-top-players`
- **What:** SofaScore season top players. Returns a competition season's top players for every statistic category SofaScore ranks (for football about 30 categories such as rating, goals, assists, expected goals, tackles and saves; for basketball points, rebounds, assists and more), each with the ranked players, their team and the value. The category set depends on the sport and competition, so the response lists every category it holds. The `type` enum accepts `overall`, `regular_season` and `playoffs`: football competitions publish `overall`, the NBA publishes `regular_season` and `playoffs`, and a type the competition does not publish answers 404. Optional `limit` caps the rows per category (up to 50). Get `id` from search and `season` from tournament-seasons.
- **Params:** `id` (string, **required**) — Numeric SofaScore unique-tournament (competition) id; `limit` (integer, optional) — Rows per category, 1 to 50. Omit to return every row; `season` (string, **required**) — Numeric SofaScore season id; `type` (string, optional) — Statistics scope. Defaults to overall

### `sofascore_tournament_top_teams`

- **HTTP:** `GET /sofascore/tournament-top-teams`
- **What:** SofaScore season top teams. Returns a competition season's top teams for every team statistic category SofaScore ranks (for football about 30 categories such as average rating, goals scored, possession, shots and clean sheets; for basketball points, pace, ratings and more), each with the ranked teams and the value. The category set depends on the sport and competition, so the response lists every category it holds. The `type` enum accepts `overall`, `regular_season` and `playoffs`: football competitions publish `overall`, the NBA publishes `regular_season`, and a type the competition does not publish answers 404. Optional `limit` caps the rows per category (up to 50). Get `id` from search and `season` from tournament-seasons.
- **Params:** `id` (string, **required**) — Numeric SofaScore unique-tournament (competition) id; `limit` (integer, optional) — Rows per category, 1 to 50. Omit to return every row; `season` (string, **required**) — Numeric SofaScore season id; `type` (string, optional) — Statistics scope. Defaults to overall

### `sofascore_tournament_venues`

- **HTTP:** `GET /sofascore/tournament-venues`
- **What:** SofaScore venues of a competition season. Returns every venue used by a competition season with id, name, capacity, city, state (US), coordinates and the `hidden` flag. Use the venue ids with venue and venue-events. A season id that does not belong to the competition answers 404. Get `id` from search and `season` from tournament-seasons.
- **Params:** `id` (string, **required**) — Numeric SofaScore unique-tournament (competition) id; `season` (string, **required**) — Numeric SofaScore season id

### `sofascore_tournament_winners`

- **HTTP:** `GET /sofascore/tournament-winners`
- **What:** SofaScore past winners of a competition. Returns one page (10 seasons, newest first) of a competition's past winners: the year, the season id and the winning team or player. Follow `has_next_page` and pass `page` (zero-based) for older seasons; a page past the last one and an unknown competition both answer 404. Get `id` from search; the returned `season_id` works with every season-scoped endpoint.
- **Params:** `id` (string, **required**) — Numeric SofaScore unique-tournament (competition) id; `page` (integer, optional) — Zero-based page number. Defaults to 0

### `sofascore_tournaments_with_feature`

- **HTTP:** `GET /sofascore/tournaments-with-feature`
- **What:** SofaScore competitions that carry a feature. Returns SofaScore's short list (up to 10) of the most followed competitions of a sport that carry one feature. The `feature` enum accepts `cuptree` (knockout tree, for tournament-cuptree), `standings` (league table), `totw` (team of the week) and `power_rankings`. The `sport` enum accepts `american-football`, `aussie-rules`, `badminton`, `bandy`, `baseball`, `basketball`, `beach-volley`, `cricket`, `darts`, `esports`, `floorball`, `football`, `futsal`, `handball`, `ice-hockey`, `minifootball`, `rugby`, `snooker`, `table-tennis`, `tennis`, `volleyball` and `waterpolo` (`mma` and `padel` are not supported). The list is fixed by SofaScore and cannot be paged or searched; a sport with no such competition returns an empty list. Use search-typed with `type` `unique_tournaments` to find other competitions.
- **Params:** `feature` (string, **required**) — Competition feature; `sport` (string, **required**) — Sport key

### `sofascore_trending_events`

- **HTTP:** `GET /sofascore/trending-events`
- **What:** SofaScore trending events. Returns the events trending in one country across every sport (live, recent and upcoming), each as the usual event summary plus its `sport` key. `country` is a two-letter ISO 3166-1 alpha-2 code such as `GB` or `US` (any case); SofaScore serves a trending list per country, and a code it does not serve returns 404. The list is about twenty events and changes through the day.
- **Params:** `country` (string, **required**) — Two-letter ISO 3166-1 alpha-2 country code

### `sofascore_trending_players`

- **HTTP:** `GET /sofascore/trending-players`
- **What:** SofaScore trending players. Returns a sport's trending top players: standout performers from recent matches with the player, team, the match and that match's numbers as a snake_case metric map (`rating`, `minutes_played`, `goals` and more; the metric set depends on the sport and position). The `sport` enum accepts `football` and `basketball`, the sports for which SofaScore publishes this list. Returns 404 when SofaScore has no trending players for the sport right now.
- **Params:** `sport` (string, **required**) — Sport key

### `sofascore_venue`

- **HTTP:** `GET /sofascore/venue`
- **What:** SofaScore venue. Returns one venue (stadium or arena): name, capacity, city, country, coordinates, its home teams, the venue-wide match totals (matches, goals, home and away win shares, and for football cards and corners per game) and a per-sport record in `sports`, most matches first. `hidden` venues, such as NBA arenas, have no venue-wide match list in venue-events and are listed per competition season instead. An unknown venue id answers 404. Get `id` from search-typed with `type` `venues`, from tournament-venues or from an event's venue.
- **Params:** `id` (string, **required**) — Numeric SofaScore venue id

### `sofascore_venue_events`

- **HTTP:** `GET /sofascore/venue-events`
- **What:** SofaScore matches at a venue. Returns one page (up to 30) of the matches played (`direction` `last`, newest page first) or scheduled (`next`) at a venue, as match summaries. Without `tournament` and `season` it lists every match at the venue, optionally narrowed by `sport` (`all`, or any key listed in the venue's `sports`, such as `football`, `rugby`, `basketball`, `mma`); with both it lists that competition season's matches at the venue and `sport` must be omitted. Hidden venues (see venue) have no venue-wide list and answer 404 without `tournament` and `season`. A direction with no matches, a sport the venue never hosted and a page past the last one also answer 404; follow `has_next_page`.
- **Params:** `direction` (string, **required**) — Upcoming matches or finished matches; `id` (string, **required**) — Numeric SofaScore venue id; `page` (integer, optional) — Zero-based page number. Defaults to 0; `season` (string, optional) — Numeric season id; with tournament, lists that competition season's matches at the venue; `sport` (string, optional) — Sport filter for the venue-wide list. Defaults to all; `tournament` (string, optional) — Numeric unique-tournament id; with season, lists that competition season's matches at the venue

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
- **What:** Get an MLB game feed. Returns an MLB game summary by numeric `id`. The response has the status, both teams with records and score, inning-by-inning runs, probable pitchers, winning, losing and save pitchers, and team box-score totals. It does not include the full play-by-play. Use the play-by-play endpoint for that.
- **Params:** `id` (string, **required**) — Numeric MLB game id

### `mlb_game_boxscore`

- **HTTP:** `GET /mlb/game-boxscore`
- **What:** Get an MLB player boxscore. Returns the player box score for an MLB game by numeric `id`. For the home and away teams it lists each player used with position, batting order and batting, pitching and fielding stats, plus team totals.
- **Params:** `id` (string, **required**) — Numeric MLB game id

### `mlb_game_play_by_play`

- **HTTP:** `GET /mlb/game-play-by-play`
- **What:** Get MLB game play-by-play. Returns the at-bats of an MLB game by numeric `id`. Each play has its inning and half, batter, pitcher, event and description, and a list of individual pitch and event records with timing and pitch data. The response includes a `total` count of plays.
- **Params:** `id` (string, **required**) — Numeric MLB game id

### `mlb_league_leaders`

- **HTTP:** `GET /mlb/league-leaders`
- **What:** Get MLB league leaders. Returns ranked MLB leader entries for one or more validated categories. Use mlb-discovery for all accepted categories, groups, and game type codes.
- **Params:** `categories` (string, **required**) — Comma-separated MLB leader category names; values are listed in mlb-discovery; `game_type` (string, optional) — MLB game type; `group` (string, optional) — Stat group; `league_id` (string, optional) — MLB league id; `limit` (integer, optional) — Leaders per category (1-100); `season` (integer, optional) — Four-digit season; defaults to current year

### `mlb_league_stats`

- **HTTP:** `GET /mlb/league-stats`
- **What:** Get ranked MLB league statistics. Returns ranked MLB stat splits across both leagues. `group` is required (`hitting`, `pitching`, `fielding`, `catching`, `running`, `game`, `team` or `streak`). `season` defaults to the current year and `stat_type` to `season`. Narrow with `league_id`, `team_id`, `position`, `player_pool`, and page with `limit` (1 to 100) and `offset` (0 to 10000).
- **Params:** `end_date` (string, optional) — End date for byDateRange stat types; requires start_date; `game_type` (string, optional) — MLB game type; `group` (string, **required**) — Stat group; `league_id` (string, optional) — MLB league id; `limit` (integer, optional) — Results to return (1-100); `offset` (integer, optional) — Zero-based result offset (0-10000); `opponent_player_id` (string, optional) — Required by vsPlayer stat types; `opponent_team_id` (string, optional) — Required by vsTeam stat types; `player_pool` (string, optional) — Qualified-player pool; `position` (string, optional) — Hitter position; use only with group=hitting; `season` (integer, optional) — Four-digit season; defaults to current year; `start_date` (string, optional) — Start date for byDateRange stat types; requires end_date; `stat_type` (string, optional) — Stats API stat type; defaults to season; `team_id` (string, optional) — Optional MLB team id; discover current team ids with mlb_teams

### `mlb_player`

- **HTTP:** `GET /mlb/player`
- **What:** Get an MLB player. Returns an MLB player by numeric `id`. The response has the full name, position, bats and throws sides, birth date, city and country, current age, height, weight, jersey number, MLB debut date, active flag and current team. Unknown players return `404`.
- **Params:** `id` (string, **required**) — Numeric MLB player id

### `mlb_player_stats`

- **HTTP:** `GET /mlb/player-stats`
- **What:** Get MLB player season statistics. Returns one MLB player's statistics. `id` and `group` (`hitting`, `pitching`, `fielding`, `catching`, `running`, `game`, `team` or `streak`) are required. `season` defaults to the current year and `stat_type` to `season`. Other `stat_type` values cover career, game logs and splits. Use `start_date` with `end_date` for date ranges.
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
- **What:** Get Baseball Savant player throw details. Returns the individual Arm Strength throw records for one player, by positive `player_id`. `year` can be 2020 to 2026, or `9999` for all years, and defaults to the current verified season. Each throw has its year, fielder id, position, the measured arm-strength value and a play id.
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
- **What:** Get a player's Pitch Tempo detail rows. Returns game-level Pitch Tempo detail rows for one pitcher or batter. `entity_id` is required, taken from a Pitch Tempo result. `type` is `Pit` (default) or `Bat`, `season_start` and `season_end` run from 2010 to 2026 and default to the current year, and `game_type` is `Regular` (default), `Playoff` or `All`. Rows hold elapsed seconds, counts and frequencies; empty when nothing matches.
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
- **What:** Get MLB team season statistics. Returns one MLB team's statistics. `team_id` and `group` (`hitting`, `pitching`, `fielding`, `catching`, `running`, `game`, `team` or `streak`) are required. `season` defaults to the current year and `stat_type` to `season`. Other `stat_type` values cover splits and logs. Use `start_date` with `end_date` for date ranges.
- **Params:** `end_date` (string, optional) — End date for byDateRange stat types; requires start_date; `game_type` (string, optional) — MLB game type; `group` (string, **required**) — Statistics group; `opponent_player_id` (string, optional) — Required by vsPlayer stat types; `opponent_team_id` (string, optional) — Required by vsTeam stat types; `season` (integer, optional) — Four-digit season; `start_date` (string, optional) — Start date for byDateRange stat types; requires end_date; `stat_type` (string, optional) — Stats API stat type; defaults to season; `team_id` (string, **required**) — Numeric MLB team id

### `mlb_teams`

- **HTTP:** `GET /mlb/teams`
- **What:** List MLB teams. Lists the 30 MLB clubs for a `season` (four-digit year, default the current year). Each team has its id, name, club name, location, abbreviation, league, division, venue, first year of play and active flag.
- **Params:** `season` (integer, optional) — Four-digit season; defaults to current year

### `mlb_transactions`

- **HTTP:** `GET /mlb/transactions`
- **What:** List MLB transactions. Lists MLB transactions between `start_date` and `end_date`, both required in `YYYY-MM-DD` format. Covers signings, trades, options, assignments, injured-list moves and releases. Narrow with `team_id` or `player_id`. Each entry has the date, effective date, type, description, player, and from and to teams, with a total `count`.
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
- **What:** DraftKings Sportsbook event. Returns one event's metadata (league id, sport id, teams, status, start time). `event_id` is a numeric DraftKings event identifier (find it from an event's DraftKings Sportsbook page, or from the `id` field of an event returned by /draftkings/sportsbook/odds). The returned `league_id` is accepted by /draftkings/sportsbook/odds and /draftkings/sportsbook/futures. This endpoint does not include betting markets/odds.
- **Params:** `event_id` (string, **required**) — Numeric DraftKings event id

### `draftkings_event_context`

- **HTTP:** `GET /draftkings/sportsbook/event-context`
- **What:** DraftKings Sportsbook event context. Returns public sport, league, and event navigation identifiers for a numeric DraftKings event id. Use it to associate an event with DraftKings Sportsbook's public sport and league navigation.
- **Params:** `event_id` (string, **required**) — Numeric DraftKings event id

### `draftkings_event_markets`

- **HTTP:** `GET /draftkings/sportsbook/event-markets`
- **What:** DraftKings Sportsbook event markets. Returns one event's betting markets and selections for a specific market category. `event_id` is a numeric DraftKings event identifier (find it from the `id` field of an event returned by /draftkings/sportsbook/odds). `subcategory_id` selects the market category (e.g. game lines, a player-prop category, an alternate-line category) -- find one from the `subcategory_id` field on a market returned by /draftkings/sportsbook/odds. An empty `markets` list is a valid response when the category has no markets currently posted for this event.
- **Params:** `event_id` (string, **required**) — Numeric DraftKings event id; `subcategory_id` (string, **required**) — Numeric DraftKings market subcategory id

### `draftkings_featured_leagues`

- **HTTP:** `GET /draftkings/sportsbook/featured-leagues`
- **What:** DraftKings Sportsbook featured leagues. Returns public DraftKings Sportsbook leagues currently marked as featured in its sport navigation. Each item includes its numeric `id`, capability `tags`, live-offer status, and upstream featured ordering. Use the `id` as `league_id` with /draftkings/sportsbook/odds and /draftkings/sportsbook/futures.
- **Params:** _none_

### `draftkings_futures`

- **HTTP:** `GET /draftkings/sportsbook/futures`
- **What:** DraftKings Sportsbook futures. Returns league-level futures markets and selections for a specific DraftKings market category. `league_id` is a numeric DraftKings league identifier and `subcategory_id` is a numeric futures category identifier. An empty `events` list is a valid response when the category has no markets currently posted for that league.
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
- **What:** DraftKings Sportsbook odds. Returns the primary betting markets (moneyline, spread, total) for every upcoming event in a DraftKings Sportsbook league. `league_id` is a numeric DraftKings league identifier (find it from a league's DraftKings Sportsbook page). An empty `events` list is a valid response when nothing is currently scheduled.
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
- **What:** Get the Cricinfo international calendar. Returns the dated international cricket calendar that Cricinfo currently publishes, with no parameters. Each event has its ISO date, the match name such as a fixture and venue, and any series labels for that day. The response also gives the event count.
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
- **What:** Get Cricinfo live matches. Returns Cricinfo's current live-score list with no parameters, covering live, upcoming and recently completed matches. Each match has its title, format, state, status text, start date, series, both teams with scores, and a scorecard `url` you can pass to the match endpoint.
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
- **What:** Get ICC rankings from Cricinfo. Returns ICC rankings (team or player) from a Cricinfo rankings page, given as the required `url`, which must be a canonical `https://www.cricinfo.com/rankings/...` address. Each entry has its rank, name, country, rating, points, matches and format, plus a team or player id.
- **Params:** `url` (string, **required**) — Canonical Cricinfo rankings URL

### `cricinfo_records`

- **HTTP:** `GET /cricinfo/records`
- **What:** Get a Cricinfo record table. Returns a bounded table from a Cricinfo records page. `record` is a relative Statsguru record path such as `batting/most_runs_career.html`. `class` must be one of `1`, `2`, `3`, `4`, `5`, `6`, `8`, `9`, `10`, `11`, `12`, `20`, `21`, `22`, or `23`.
- **Params:** `class` (integer, **required**) — Record match-class. Allowed values: 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 20, 21, 22, 23; `current` (string, optional) — Record currentness selector; `id` (string, optional) — Numeric record subject identifier; `record` (string, **required**) — Relative Statsguru record path; `type` (string, optional) — Record subject type

### `cricinfo_records_index`

- **HTTP:** `GET /cricinfo/records/index`
- **What:** List Cricinfo records catalog. Returns the public Cricinfo records catalog, including match classes, record categories, selectable teams or entities, and example suggestions. Use the existing records endpoint to retrieve a specific table.
- **Params:** _none_

### `cricinfo_rss`

- **HTTP:** `GET /cricinfo/rss`
- **What:** Read a Cricinfo RSS feed. Returns a Cricinfo RSS feed. `url` must be one of Cricinfo's official news, live-score, country-story, or player-story RSS URLs.
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
- **What:** Query Cricinfo Statsguru. Returns a bounded Statsguru table. `class` must be one of `1`, `2`, `3`, `4`, `5`, `6`, `8`, `9`, `10`, `11`, `12`, `20`, `21`, `22`, or `23`; `type` must be one of `batting`, `bowling`, `fielding`, `allround`, `fow`, `team`, `official`, or `aggregate`; `view` may be `innings`, `match`, `series`, `ground`, `host`, `opposition`, `year`, or `season`.
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
- **What:** Get a Cricinfo team match schedule. Returns a cricket team's recent fixtures and results from its Cricinfo team page, given as the required `url`, which must be a canonical `https://www.cricinfo.com/team/...` address. The response has the team's id, name and slug, and matches with series, format, state, status text, team scores and scorecard URL.
- **Params:** `url` (string, **required**) — Canonical Cricinfo team URL

### `cricinfo_teams`

- **HTTP:** `GET /cricinfo/teams`
- **What:** List Cricinfo teams. Returns Cricinfo's team directory with no parameters, organised into titled groups such as popular international teams. Each team has its id, name, slug, abbreviation, country, logo URL and primary colour where Cricinfo gives them, and whether it is a national side.
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
- **What:** Get a Sportskeeda author profile. Returns a Sportskeeda author's profile, looked up by `slug` (for example `sripad`) or canonical `url`; at least one is required. The response has the name and the articles listed on the profile, each with title and URL, and can also carry `biography`, `role` and `image_url`.
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
- **What:** Discover Sportskeeda calendar regions, sports, and months. Lists the regions (`us` and `india`) of the Sportskeeda event calendar, each with the sport names and `YYYY-MM` months currently on offer. Takes no parameters. Pass the exact `region`, `sport` and `month` values to `/sportskeeda/event-calendar`; no year parameter exists.
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
- **What:** List Sportskeeda player-guessing games. Lists the player-guessing games currently linked on Sportskeeda. Each has a display `name`, a host-free page `slug` such as `wwe/brainbuster-wwe-player-guessing-game`, and its `game_slug`. Pass `slug` to `/sportskeeda/guessing-game` or `/sportskeeda/guessing-game-entities`. Takes no parameters.
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
- **What:** Get Sportskeeda structured sports tables. Returns team, player, roster, leaderboard, ranking, depth, playoff, and game-log tables. NFL team stats include team-leader cards, player-category tables, and Basic, Advanced, and Expert team tables. Season and type are accepted only if offered by the selected page; discover their values with page-options. Player game-log seasons use their discovered season-specific path and return every table offered by the page; NFL category tabs are listed by page-options. College-football schedule slugs accept a discovered conference slug and filter the schedule rows; an offered group with no games on that week returns status no_data. The trade value chart has a separate endpoint. A page with no structured tables returns an upstream error.
- **Params:** `conference` (string, optional) — College-football schedule conference slug from page-options; `season` (integer, optional) — Season year offered by this page's page-options filter; `slug` (string, **required**) — Sportskeeda path without host; `type` (string, optional) — Season phase offered by this page's page-options filter; leaderboard pages offer pre, regular, post

### `sportskeeda_page_options`

- **HTTP:** `GET /sportskeeda/page-options`
- **What:** Discover Sportskeeda page menus and filters. Returns the page's live contextual menus, team and ranking links, tabs, schedule views, and every currently offered select-filter value. Leaderboard category and metric values carry their destination slugs. College-football schedule pages expose the client-side conference selector here.
- **Params:** `slug` (string, **required**) — Sportskeeda path without host

### `sportskeeda_player_stats`

- **HTTP:** `GET /sportskeeda/player-stats`
- **What:** Get NFL or NBA player season stats across event phases. Returns the season stats for an NFL or NBA player stats page. Without event_type, returns all event phases offered by that page's selector. NBA data may contain extra phases that the page does not offer; these are excluded. Discover the current event_type values with sportskeeda-page-options for the same slug.
- **Params:** `event_type` (string, optional) — Event phase offered by this player's stats-event-type-dropdown; NFL offers 0,1,2,3 and NBA offers 0,1,2; `slug` (string, **required**) — NFL or NBA player stats path without host

### `sportskeeda_profile`

- **HTTP:** `GET /sportskeeda/profile`
- **What:** Get a Sportskeeda player or team profile. Returns a Sportskeeda player or team profile by host-free `slug`, such as `player/jannik-sinner` or `nfl/green-bay-packers`. The response has its name, `kind`, a description, fact rows as name and value pairs (names vary by sport), and any news cards. A page without fact rows returns an upstream error.
- **Params:** `slug` (string, **required**) — Sportskeeda player or team profile path without host

### `sportskeeda_quiz`

- **HTTP:** `GET /sportskeeda/quiz`
- **What:** Get a Sportskeeda quiz definition. Returns public question prompts and choice text from a quiz page, sorted by question number. The source does not expose correct answers in its anonymous page data; answer checking and user submissions are not included.
- **Params:** `slug` (string, **required**) — Sportskeeda quiz path without host, discovered through /sportskeeda/quizzes

### `sportskeeda_quiz_categories`

- **HTTP:** `GET /sportskeeda/quiz-categories`
- **What:** List current Sportskeeda quiz categories. Lists the quiz categories currently linked from Sportskeeda's quiz hub, each with a `name` and a host-free `slug` such as `cricket/quiz`. Pass a `slug` to `sportskeeda-quizzes`. Takes no parameters, and the list changes with the site, so fetch it rather than assuming fixed categories.
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
- **What:** Get Sportskeeda fixtures and results. Returns a Sportskeeda fixtures or schedule page by host-free `slug`, such as `nfl/schedule` or `cricket/schedule`. Cricket and football give `matches` with teams, time, status, score, competition, venue and result; other sports give `tables` with `columns` and `rows`. An empty fixture widget returns `status` `no_matches`.
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
- **What:** Discover Sportskeeda sitemap sources. Returns Sportskeeda's current public sitemaps. Pass a returned slug to /sportskeeda/sitemap-items to page through its complete URL set.
- **Params:** _none_

### `sportskeeda_standings`

- **HTTP:** `GET /sportskeeda/standings`
- **What:** Get Sportskeeda standings or rankings. Returns Sportskeeda standings or rankings tables for a host-free `slug`, such as `nfl/standings`, with column labels, rows, linked cell slugs and view slugs. `season` (starting year, 2013 to 2026) applies only to college basketball standings. The current college basketball season returns `status` `no_data` with empty `tables`.
- **Params:** `season` (integer, optional) — College basketball season starting year; live values from standings-options; `slug` (string, **required**) — Sportskeeda standings or rankings path without host

### `sportskeeda_standings_options`

- **HTTP:** `GET /sportskeeda/standings-options`
- **What:** Discover Sportskeeda college standings seasons and conferences. Lists the seasons and conferences available for Sportskeeda college basketball standings. `slug` is required and must be `college-basketball/college-basketball-standings`. Without `season` you get all offered season years and the current season's conferences; with it, that season's conferences, each with a name and a slug usable as the standings `slug`.
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
- **What:** Get Sportskeeda video metadata. Returns metadata for one Sportskeeda video page by host-free `slug`, such as `cricket/sunil-naraine-batting-cpl`: its id, title, poster image, stream URL and, when available, a description. A page without a video player returns an upstream error, and stream availability can depend on geography.
- **Params:** `slug` (string, **required**) — Individual Sportskeeda video page path without host

### `sportskeeda_videos`

- **HTTP:** `GET /sportskeeda/videos`
- **What:** List Sportskeeda videos and channels. Lists video cards from Sportskeeda's main video library, or from a listing given by `slug` (default `videos`, for example `go/epl/videos`). Items have a title, slug, URL, and thumbnail, duration and channel when present. The response also lists channels with their slugs. An empty or blocked listing returns an upstream error.
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
- **What:** List Sportskeeda Wiki categories. Returns the nested category menu of one Sportskeeda Wiki project, chosen by `wiki` (`minecraft`, `terraria`, `naruto`, `tiktok`, `youtube`, `gta`, `one-piece` or `sk-communities`). Each category has a title, slug, `path_slug`, taxonomy id, sequence and `children`. Category names, ids and paths change over time.
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
- **What:** List Sportskeeda Wiki projects. Lists the Sportskeeda Wiki projects, each with a `slug`, display `name`, `taxonomy_id` and `taxonomy_slug`. Current slugs are `minecraft`, `terraria`, `naruto`, `tiktok`, `youtube`, `gta`, `one-piece` and `sk-communities`. Use a `slug` with `wiki-categories` and `wiki-pages`. Takes no parameters.
- **Params:** _none_

### `sportskeeda_wiki_pages`

- **HTTP:** `GET /sportskeeda/wiki-pages`
- **What:** Search and paginate Sportskeeda Wiki pages. Returns catalog pages for one Wiki project. Use path_slug as the preferred host-free slug for sportskeeda-wiki-article. total_items is the record count; the upstream field named total_pages is mislabelled and does not mean page count.
- **Params:** `limit` (integer, optional) — Items per page; `page` (integer, optional) — 1-based catalog page; `search` (string, optional) — Title or page search text; sent upstream as searchText; `sort` (string, optional) — Sort direction; `sort_by` (string, optional) — Catalog field to sort by; `wiki` (string, **required**) — Project slug returned by sportskeeda-wiki-options

### `sportskeeda_wiki_summary`

- **HTTP:** `GET /sportskeeda/wiki-summary`
- **What:** Get community counts for a Sportskeeda Wiki page. Returns accepted contributor and activity totals plus the open-issue count for one Wiki article. The source page slug is obtained from sportskeeda-wiki-pages.
- **Params:** `slug` (string, **required**) — Host-free Wiki page path_slug from sportskeeda-wiki-pages
