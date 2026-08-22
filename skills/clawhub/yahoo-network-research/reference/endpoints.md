# yahoo-network-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**45 endpoints across 8 platform group(s).**

## Yahoo Autos (3)

### `yahoo_autos_article`

- **HTTP:** `GET /yahoo-autos/article`
- **What:** Yahoo Autos article content. Returns a single Yahoo Autos article's full content: title, description, author, publish/update time, section, image, keywords, original publisher, and body paragraphs. Accepts a canonical autos.yahoo.com article URL, such as one returned by the home or category story streams.
- **Params:** `url` (string, **required**) — Canonical autos.yahoo.com article URL

### `yahoo_autos_category`

- **HTTP:** `GET /yahoo-autos/category`
- **What:** Yahoo Autos section story stream. Returns a Yahoo Autos section's editorial story feed: title, destination URL, category, and thumbnail image for each story, with page-based pagination. Sourced from Yahoo Autos's own server-rendered section pages.
- **Params:** `category` (string, **required**) — Yahoo Autos section; `page` (integer, optional) — 1-based page number, defaults to 1

### `yahoo_autos_home`

- **HTTP:** `GET /yahoo-autos/home`
- **What:** Yahoo Autos homepage story stream. Returns Yahoo Autos's homepage editorial story feed: title, destination URL, category, and thumbnail image for each story. Sourced from Yahoo Autos's own server-rendered homepage.
- **Params:** _none_

## Yahoo Entertainment (3)

### `yahoo_entertainment_article`

- **HTTP:** `GET /yahoo-entertainment/article`
- **What:** Yahoo Entertainment article content. Returns a single Yahoo Entertainment article's full content: title, description, author, publish/update time, section, image, keywords, original publisher, and body paragraphs. Accepts a canonical www.yahoo.com/entertainment/ article URL, such as one returned by the home or category story streams.
- **Params:** `url` (string, **required**) — Canonical www.yahoo.com/entertainment/ article URL

### `yahoo_entertainment_category`

- **HTTP:** `GET /yahoo-entertainment/category`
- **What:** Yahoo Entertainment section story stream. Returns a Yahoo Entertainment section's editorial story feed: title, destination URL, category, and thumbnail image for each story, with page-based pagination. Sourced from Yahoo Entertainment's own server-rendered section pages.
- **Params:** `category` (string, **required**) — Yahoo Entertainment section; `page` (integer, optional) — 1-based page number, defaults to 1

### `yahoo_entertainment_home`

- **HTTP:** `GET /yahoo-entertainment/home`
- **What:** Yahoo Entertainment homepage story stream. Returns Yahoo Entertainment's homepage editorial story feed: title, destination URL, category, and thumbnail image for each story. Sourced from Yahoo Entertainment's own server-rendered homepage.
- **Params:** _none_

## Yahoo Health (3)

### `yahoo_health_article`

- **HTTP:** `GET /yahoo-health/article`
- **What:** Yahoo Health article content. Returns a single Yahoo Health article's full content: title, description, author, publish/update time, section, image, keywords, original publisher, and body paragraphs. Accepts a canonical health.yahoo.com article URL, such as one returned by the home or category story streams.
- **Params:** `url` (string, **required**) — Canonical health.yahoo.com article URL

### `yahoo_health_category`

- **HTTP:** `GET /yahoo-health/category`
- **What:** Yahoo Health section story stream. Returns a Yahoo Health section's editorial story feed: title, destination URL, category, and thumbnail image for each story, with page-based pagination. Sourced from Yahoo Health's own server-rendered section pages.
- **Params:** `category` (string, **required**) — Yahoo Health section; `page` (integer, optional) — 1-based page number, defaults to 1

### `yahoo_health_home`

- **HTTP:** `GET /yahoo-health/home`
- **What:** Yahoo Health homepage story stream. Returns Yahoo Health's homepage editorial story feed: title, destination URL, category, and thumbnail image for each story. Sourced from Yahoo Health's own server-rendered homepage.
- **Params:** _none_

## Yahoo Life (2)

### `yahoo_life_article`

- **HTTP:** `GET /yahoo-life/article`
- **What:** Yahoo Life article content. Returns a single Yahoo Life article's full content: title, description, author, publish/update time, section, image, keywords, original publisher, and body paragraphs. Accepts a canonical www.yahoo.com/lifestyle article URL, such as one returned by the home story stream.
- **Params:** `url` (string, **required**) — Canonical www.yahoo.com/lifestyle article URL

### `yahoo_life_home`

- **HTTP:** `GET /yahoo-life/home`
- **What:** Yahoo Life homepage story stream. Returns Yahoo Life's homepage editorial story feed: title, destination URL, and thumbnail image for each story. Sourced from Yahoo Life's own server-rendered homepage.
- **Params:** _none_

## Yahoo News (6)

### `yahoo_news_article`

- **HTTP:** `GET /yahoo-news/article`
- **What:** Yahoo News article content. Returns a single Yahoo News article's full content: headline, description, author, publish/update time, section, image, keywords, original publisher, and body paragraphs. Accepts a canonical yahoo.com/news article URL, such as one returned by the home or category story streams.
- **Params:** `url` (string, **required**) — Canonical www.yahoo.com/news article URL

### `yahoo_news_category`

- **HTTP:** `GET /yahoo-news/category`
- **What:** Yahoo News section story stream. Returns a Yahoo News section's story stream: title, destination URL, summary, source, publish time, comment count, and thumbnail images for each story. Sourced from Yahoo News's own server-rendered section pages.
- **Params:** `category` (string, **required**) — Yahoo News section

### `yahoo_news_comment_replies`

- **HTTP:** `GET /yahoo-news/comments/replies`
- **What:** Yahoo News comment replies. Returns a page of a comment's replies: author, body, reaction counts, and pin status, with sort order and cursor-based pagination. Sourced from Yahoo's own comment platform gateway.
- **Params:** `comment_id` (string, **required**) — Parent comment id (the id field returned by /yahoo-news/comments); `content_id` (string, **required**) — Article id (the id field returned by home/category/article); `count` (integer, optional) — Number of replies to return, default 10, clamped to 1..50; `cursor` (string, optional) — Pagination cursor from a previous response's next_cursor; `sort` (string, optional) — Sort order, defaults to newest

### `yahoo_news_comments`

- **HTTP:** `GET /yahoo-news/comments`
- **What:** Yahoo News article comments. Returns a page of an article's top-level comments: author, body, reaction counts, reply count, and pin status, with sort order and cursor-based pagination. Sourced from Yahoo's own comment platform gateway.
- **Params:** `content_id` (string, **required**) — Article id (the id field returned by home/category/article); `count` (integer, optional) — Number of comments to return, default 10, clamped to 1..50; `cursor` (string, optional) — Pagination cursor from a previous response's next_cursor; `sort` (string, optional) — Sort order, defaults to top

### `yahoo_news_home`

- **HTTP:** `GET /yahoo-news/home`
- **What:** Yahoo News homepage story stream. Returns Yahoo News's homepage "need to know" story stream: title, destination URL, summary, source, publish time, comment count, and thumbnail images for each story. Sourced from Yahoo News's own server-rendered homepage.
- **Params:** _none_

### `yahoo_news_suggest`

- **HTTP:** `GET /yahoo-news/suggest`
- **What:** Yahoo News search autocomplete suggestions. Returns Yahoo News's own search-box autocomplete suggestions for a partial query: a flat list of suggested news search terms.
- **Params:** `count` (integer, optional) — Number of suggestions to return, default 10, clamped to 1..20; `q` (string, **required**) — Partial search query to autocomplete

## Yahoo Shopping (7)

### `yahoo_shopping_article`

- **HTTP:** `GET /yahoo-shopping/article`
- **What:** Yahoo Shopping article content. Returns a single Yahoo Shopping article's full content: title, description, author, publish/update time, section, image, keywords, original publisher, and body paragraphs. Accepts a canonical shopping.yahoo.com article URL, such as one returned by the home or category story streams.
- **Params:** `url` (string, **required**) — Canonical shopping.yahoo.com article URL

### `yahoo_shopping_category`

- **HTTP:** `GET /yahoo-shopping/category`
- **What:** Yahoo Shopping section story stream. Returns a Yahoo Shopping section's editorial story feed: title, destination URL, category, and thumbnail image for each story, with page-based pagination. Sourced from Yahoo Shopping's own server-rendered section pages.
- **Params:** `category` (string, **required**) — Yahoo Shopping section; `page` (integer, optional) — 1-based page number, defaults to 1

### `yahoo_shopping_home`

- **HTTP:** `GET /yahoo-shopping/home`
- **What:** Yahoo Shopping homepage story stream. Returns Yahoo Shopping's homepage editorial story feed: title, destination URL, category, and thumbnail image for each story. Sourced from Yahoo Shopping's own server-rendered homepage. This is Yahoo's shopping buying-guide/deals content site, not a product-search API -- shopping.yahoo.com no longer exposes a searchable product catalog.
- **Params:** _none_

### `yahoo_shopping_shopping_list`

- **HTTP:** `GET /yahoo-shopping/shopping-list`
- **What:** Yahoo Shopping curated list items. Returns one curated Yahoo Shopping list's items: product title, direct destination URL, image, seller, currency, price, and sale price for each item. Sourced from the list page's own product cards. Use GET /yahoo-shopping/shopping-lists to find a list's slug.
- **Params:** `list` (string, **required**) — List slug from GET /yahoo-shopping/shopping-lists

### `yahoo_shopping_shopping_lists`

- **HTTP:** `GET /yahoo-shopping/shopping-lists`
- **What:** Yahoo Shopping curated shopping-lists directory. Returns Yahoo Shopping's curated shopping-lists directory: a slug, title, and image for each themed list (e.g. "Cooling Essentials", "Back to School"). Use a list's slug with GET /yahoo-shopping/shopping-list to read its items.
- **Params:** _none_

### `yahoo_shopping_store`

- **HTTP:** `GET /yahoo-shopping/store`
- **What:** Yahoo Shopping retailer store deals. Returns one retailer's current deals on Yahoo Shopping: product title, direct retailer product URL, image, brand, currency, price, and sale price for each offer. Sourced from the retailer's shopping.yahoo.com store page's own structured product data -- not a keyword search, a fixed set of currently-featured deals for that retailer. Use GET /yahoo-shopping/stores to find a retailer's slug.
- **Params:** `store` (string, **required**) — Retailer slug from GET /yahoo-shopping/stores

### `yahoo_shopping_stores`

- **HTTP:** `GET /yahoo-shopping/stores`
- **What:** Yahoo Shopping retailer store directory. Returns Yahoo Shopping's retailer store directory: a slug, display name, and logo image for each retailer with a dedicated store page (e.g. Amazon, Target, Best Buy). Use a store's slug with GET /yahoo-shopping/store to read its current deals.
- **Params:** _none_

## Yahoo Sports (18)

### `yahoo_sports_game`

- **HTTP:** `GET /yahoo-sports/game`
- **What:** Yahoo Sports game boxscore. Returns one game's boxscore (matchup, line score by period, and team stat totals) from sports.yahoo.com's own server-rendered game page. The `league` enum accepts `nfl`, `nba`, `wnba`, `mlb`, `nhl`, `college-football`, `college-basketball`, `college-womens-basketball`, `mls`, `premier-league`, `la-liga`, `serie-a`, `bundesliga`, `ligue-1`, `nwsl`, `ligamx-apertura`, `ligamx-clausura`, `copa-america`, `club-world-cup`, `world-cup`, `concacaf-champions-cup`, `concacaf-gold-cup`, `concacaf-league`, and `champions-league`. Get the `game` slug from a scoreboard or team-schedule response's game `url` (the last path segment), e.g. `cleveland-guardians-detroit-tigers-460811106`.
- **Params:** `game` (string, **required**) — Yahoo Sports game slug from a scoreboard/team-schedule response's game url; `league` (string, **required**) — League key

### `yahoo_sports_golf_leaderboard`

- **HTTP:** `GET /yahoo-sports/golf-leaderboard`
- **What:** Yahoo Sports golf tournament leaderboard. Returns one golf tournament's full leaderboard (every golfer's rank, to-par score, status, holes-completed-in-current-round, per-round strokes, and a fixed stat set: earnings, eagles, birdies, pars, bogeys, double bogeys), from Yahoo Sports' own public tournament-leaderboard JSON API. Get the `tournament` id from a golf-schedule response's `id` field, e.g. `golf.e.23`.
- **Params:** `season` (integer, optional) — 4-digit season year (a tournament id is reused across years); defaults to the tournament's most recent season; `tournament` (string, **required**) — Yahoo Sports golf tournament id from a golf-schedule response's id field

### `yahoo_sports_golf_schedule`

- **HTTP:** `GET /yahoo-sports/golf-schedule`
- **What:** Yahoo Sports golf tournament schedule. Returns a golf tour's tournament schedule for a season (name, dates, status, purse, and venue), from Yahoo Sports' own public tournament-schedule JSON API. The `tour` enum accepts `pga-tour`, `pga-european-tours`, `lpga-tour`, `champions-tour`, and `european-tour`. Each tournament's `id` feeds the golf-leaderboard endpoint's `tournament` parameter.
- **Params:** `season` (integer, optional) — 4-digit season year; defaults to the tour's current season; `tour` (string, **required**) — Golf tour key

### `yahoo_sports_mma_fight_card`

- **HTTP:** `GET /yahoo-sports/mma-fight-card`
- **What:** Yahoo Sports MMA fight card. Returns the current/next UFC event's full fight card (each bout's fighters, records, rankings, weight class, and card position), from Yahoo Sports' own server-rendered MMA schedule page. This endpoint takes no parameters -- it always returns whichever event Yahoo currently features as next up, not a caller-selected one.
- **Params:** _none_

### `yahoo_sports_mma_schedule`

- **HTTP:** `GET /yahoo-sports/mma-schedule`
- **What:** Yahoo Sports MMA event schedule. Returns the known UFC event calendar (name, date, status), from Yahoo Sports' own server-rendered MMA schedule page. This endpoint is UFC-only and takes no parameters -- Yahoo's own page does not expose Bellator, PFL, ONE Championship, or other promotions from this URL.
- **Params:** _none_

### `yahoo_sports_motorsports_race`

- **HTTP:** `GET /yahoo-sports/motorsports-race`
- **What:** Yahoo Sports motorsports race results. Returns one race's full driver-by-driver results (finishing position, driver, car/team, points, laps, time), from Yahoo Sports' own server-rendered race page. The `series` enum accepts `f1` and `nascar`. Get the `race` slug from a motorsports-schedule response's race `url` (the last path segment), e.g. `australian-grand-prix-2026-2961`.
- **Params:** `race` (string, **required**) — Yahoo Sports race slug from a motorsports-schedule response's race url; `series` (string, **required**) — Motorsports series key

### `yahoo_sports_motorsports_schedule`

- **HTTP:** `GET /yahoo-sports/motorsports-schedule`
- **What:** Yahoo Sports motorsports season schedule. Returns a series' season race list (name, date, status, laps, distance, pole/race winner, venue), from Yahoo Sports' own server-rendered motorsports schedule page. The `series` enum accepts `f1` and `nascar`.
- **Params:** `season` (integer, optional) — 4-digit season year; defaults to the current season; `series` (string, **required**) — Motorsports series key

### `yahoo_sports_news`

- **HTTP:** `GET /yahoo-sports/news`
- **What:** Yahoo Sports league news. Returns recent news articles (title, summary, author, published time, and link) for a league from sports.yahoo.com's own server-rendered news page. The `league` enum accepts `nfl`, `nba`, `wnba`, `mlb`, `nhl`, `college-football`, `college-basketball`, `college-womens-basketball`, `mls`, `premier-league`, `la-liga`, `serie-a`, `bundesliga`, `ligue-1`, `nwsl`, `ligamx-apertura`, `ligamx-clausura`, `copa-america`, `club-world-cup`, `world-cup`, `concacaf-champions-cup`, `concacaf-gold-cup`, `concacaf-league`, and `champions-league`.
- **Params:** `league` (string, **required**) — League key

### `yahoo_sports_olympics_medals`

- **HTTP:** `GET /yahoo-sports/olympics-medals`
- **What:** Yahoo Sports Olympics medal count. Returns the current Olympic games' full medal count by country (gold/silver/bronze/total, ranked), from Yahoo Sports' own server-rendered Olympics medals page. This endpoint takes no parameters -- it always returns whichever Olympic games Yahoo currently has medal data for, not a caller-selected prior edition.
- **Params:** _none_

### `yahoo_sports_player`

- **HTTP:** `GET /yahoo-sports/player`
- **What:** Yahoo Sports player detail. Returns one player's bio/overview (position, jersey, status, injury, physicals, college, draft position) plus current-season stats by category, from sports.yahoo.com's own server-rendered player page. The `league` enum accepts `nfl`, `nba`, `wnba`, `mlb`, `nhl`, `college-football`, `college-basketball`, `college-womens-basketball`, `mls`, `premier-league`, `la-liga`, `serie-a`, `bundesliga`, `ligue-1`, `nwsl`, `ligamx-apertura`, `ligamx-clausura`, `copa-america`, `club-world-cup`, `world-cup`, `concacaf-champions-cup`, `concacaf-gold-cup`, `concacaf-league`, and `champions-league`. Get a numeric player id from a roster response's player `url` (the last path segment).
- **Params:** `league` (string, **required**) — League key; `player` (string, **required**) — Numeric Yahoo Sports player id

### `yahoo_sports_scoreboard`

- **HTTP:** `GET /yahoo-sports/scoreboard`
- **What:** Yahoo Sports scoreboard. Returns games (teams, score, status, venue, and broadcast info) for a league on a date, from sports.yahoo.com's own server-rendered scoreboard page. The `league` enum accepts `nfl`, `nba`, `wnba`, `mlb`, `nhl`, `college-football`, `college-basketball`, `college-womens-basketball`, `mls`, `premier-league`, `la-liga`, `serie-a`, `bundesliga`, `ligue-1`, `nwsl`, `ligamx-apertura`, `ligamx-clausura`, `copa-america`, `club-world-cup`, `world-cup`, `concacaf-champions-cup`, `concacaf-gold-cup`, `concacaf-league`, and `champions-league`.
- **Params:** `date` (string, optional) — Date as YYYY-MM-DD; defaults to Yahoo Sports' current scoreboard date; `league` (string, **required**) — League key

### `yahoo_sports_standings`

- **HTTP:** `GET /yahoo-sports/standings`
- **What:** Yahoo Sports standings. Returns league standings (record, streak, games back, and clinch status) grouped by conference/division, from sports.yahoo.com's own server-rendered standings page. The `league` enum accepts `nfl`, `nba`, `wnba`, `mlb`, `nhl`, `college-football`, `college-basketball`, `mls`, `premier-league`, `la-liga`, `serie-a`, `bundesliga`, `ligue-1`, `nwsl`, `ligamx-apertura`, `ligamx-clausura`, `world-cup`, and `champions-league` (not `college-womens-basketball`, whose standings page does not embed a full grouped table). Soccer leagues return a single ungrouped table (no conference/division) and each entry's `record.points` is populated (3 per win, 1 per draw).
- **Params:** `league` (string, **required**) — League key

### `yahoo_sports_team`

- **HTTP:** `GET /yahoo-sports/team`
- **What:** Yahoo Sports team detail. Returns one team's detail (identity, colors, conference/division, and current standing summary) from sports.yahoo.com's own server-rendered team page. The `league` enum accepts `nfl`, `nba`, `wnba`, `mlb`, `nhl`, `college-football`, `college-basketball`, `college-womens-basketball`, `mls`, `premier-league`, `la-liga`, `serie-a`, `bundesliga`, `ligue-1`, `nwsl`, `ligamx-apertura`, `ligamx-clausura`, `copa-america`, `club-world-cup`, `world-cup`, `concacaf-champions-cup`, `concacaf-gold-cup`, `concacaf-league`, and `champions-league`. Get a team slug from the scoreboard or standings response (e.g. `green-bay`, `la-lakers`).
- **Params:** `league` (string, **required**) — League key; `team` (string, **required**) — Yahoo Sports team slug

### `yahoo_sports_team_roster`

- **HTTP:** `GET /yahoo-sports/team-roster`
- **What:** Yahoo Sports team roster. Returns a team's full roster (position, jersey number, status, injury, physicals, college, and experience) from sports.yahoo.com's own server-rendered roster page. The `league` enum accepts `nfl`, `nba`, `wnba`, `mlb`, `nhl`, `college-football`, `college-basketball`, `college-womens-basketball`, `mls`, `premier-league`, `la-liga`, `serie-a`, `bundesliga`, `ligue-1`, `nwsl`, `ligamx-apertura`, `ligamx-clausura`, `copa-america`, `club-world-cup`, `world-cup`, `concacaf-champions-cup`, `concacaf-gold-cup`, `concacaf-league`, and `champions-league`. Get a team slug from the scoreboard or standings response (e.g. `green-bay`, `la-lakers`).
- **Params:** `league` (string, **required**) — League key; `team` (string, **required**) — Yahoo Sports team slug

### `yahoo_sports_team_schedule`

- **HTTP:** `GET /yahoo-sports/team-schedule`
- **What:** Yahoo Sports team schedule. Returns a team's full schedule (regular season plus any already-played/scheduled playoff games), with the same per-game fields as the scoreboard, from sports.yahoo.com's own server-rendered team schedule page. The `league` enum accepts `nfl`, `nba`, `wnba`, `mlb`, `nhl`, `college-football`, `college-basketball`, `college-womens-basketball`, `mls`, `premier-league`, `la-liga`, `serie-a`, `bundesliga`, `ligue-1`, `nwsl`, `ligamx-apertura`, `ligamx-clausura`, `copa-america`, `club-world-cup`, `world-cup`, `concacaf-champions-cup`, `concacaf-gold-cup`, `concacaf-league`, and `champions-league`. Get a team slug from the scoreboard or standings response (e.g. `green-bay`, `la-lakers`).
- **Params:** `league` (string, **required**) — League key; `team` (string, **required**) — Yahoo Sports team slug

### `yahoo_sports_tennis_rankings`

- **HTTP:** `GET /yahoo-sports/tennis-rankings`
- **What:** Yahoo Sports tennis rankings. Returns an ATP/WTA singles/doubles ranking list (rank, points, player name, country, age), from Yahoo Sports' own server-rendered rankings page. The `type` enum accepts `mens-singles`, `womens-singles`, `mens-doubles`, and `womens-doubles`. No stable player id is available in this list.
- **Params:** `type` (string, **required**) — Rankings type

### `yahoo_sports_tennis_schedule`

- **HTTP:** `GET /yahoo-sports/tennis-schedule`
- **What:** Yahoo Sports tennis tournament schedule. Returns the full season tennis tournament calendar (name, gender, match type, surface, dates, status, venue, and champion where decided), from Yahoo Sports' own server-rendered tournaments page. This endpoint takes no parameters -- it always returns Yahoo's current full-season snapshot (season/gender/match-type filtering happens client-side on Yahoo's own page, not server-side).
- **Params:** _none_

### `yahoo_sports_tennis_scoreboard`

- **HTTP:** `GET /yahoo-sports/tennis-scoreboard`
- **What:** Yahoo Sports tennis scoreboard. Returns a snapshot of current/recently-completed tennis matches across the tour (tournament, round, players, per-set scores, winner, and status), from Yahoo Sports' own server-rendered tournaments page. This endpoint takes no parameters -- it is a fixed-size "what's happening right now" snapshot, not a by-date query.
- **Params:** _none_

## Yahoo Tech (3)

### `yahoo_tech_article`

- **HTTP:** `GET /yahoo-tech/article`
- **What:** Yahoo Tech article content. Returns a single Yahoo Tech article's full content: title, description, author, publish/update time, section, image, keywords, original publisher, and body paragraphs. Accepts a canonical tech.yahoo.com article URL, such as one returned by the home or category story streams.
- **Params:** `url` (string, **required**) — Canonical tech.yahoo.com article URL

### `yahoo_tech_category`

- **HTTP:** `GET /yahoo-tech/category`
- **What:** Yahoo Tech section story stream. Returns a Yahoo Tech section's editorial story feed: title, destination URL, category, and thumbnail image for each story, with page-based pagination. Sourced from Yahoo Tech's own server-rendered section pages.
- **Params:** `category` (string, **required**) — Yahoo Tech section; `page` (integer, optional) — 1-based page number, defaults to 1

### `yahoo_tech_home`

- **HTTP:** `GET /yahoo-tech/home`
- **What:** Yahoo Tech homepage story stream. Returns Yahoo Tech's homepage editorial story feed: title, destination URL, category, and thumbnail image for each story. Sourced from Yahoo Tech's own server-rendered homepage.
- **Params:** _none_
