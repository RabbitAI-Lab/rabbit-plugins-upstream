---
name: sports-scores-research
description: Pulls live scores, standings, rosters, and player/team stats via the Crawlora API — ESPN (most sports/leagues), SofaScore (global soccer + more), MLB's own stats API, and Strava (routes, clubs, challenges) — returning clean JSON. Use when the user wants a live scoreboard, a team or player's stats, league standings, a game's boxscore/play-by-play, head-to-head history, or an endurance-sport route/club.
---

# Sports & athletics research

Pull live scoreboards, standings, rosters, player/team stats, and endurance-
sport routes/clubs across four sports-data sources as normalized JSON from
the Crawlora API — no scraping scoreboard widgets or stat pages.

## When to use this skill

- "What's the score / status of <game> right now?"
- "Show me <team>'s roster / season stats / standing."
- "What's <player>'s stats this season?"
- "Give me the boxscore / play-by-play for <game>."
- "Head-to-head history between <team A> and <team B>."
- League news, rankings/polls, or betting-odds snapshots (where exposed).
- "Find running/biking/hiking routes in <region>" or "look up this Strava club."

## Setup (one-time)

- Get a free Crawlora API key (2,000 credits/mo, no card) at [https://crawlora.net](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills).
- `export CRAWLORA_API_KEY=sk_your_key_here`
- All requests: `x-api-key: $CRAWLORA_API_KEY` against
  `https://api.crawlora.net/api/v1`. Missing/invalid key → `401`.

## How it works

1. **ESPN (most sports/leagues)** — `/espn/scoreboard` for today's/a date's
   games (sport+league params); `/espn/teams` / `/espn/team` for team lists
   and detail; `/espn/team-roster` for rosters; `/espn/standings`;
   `/espn/athlete` for a player; `/espn/game-summary` for one game's
   matchup/odds/boxscore; `/espn/news` and `/espn/rankings` (e.g. AP Top 25)
   round it out.
2. **SofaScore (global soccer-first, many sports)** — `/sofascore/search` to
   resolve a team/player/event id; `/sofascore/live-events` for what's live
   right now; `/sofascore/event` (+ `/event-statistics`, `/event-lineups`,
   `/event-incidents`, `/event-odds`, `/event-h2h`) for one match in depth;
   `/sofascore/standings`, `/sofascore/team`, `/sofascore/team-events`,
   `/sofascore/team-players`, `/sofascore/player`.
3. **MLB** — `/mlb/schedule` for games/scores by date; `/mlb/game` (+
   `/mlb/game-boxscore`, `/mlb/game-play-by-play`) for one game's detail;
   `/mlb/standings`, `/mlb/teams`, `/mlb/team-roster`, `/mlb/team-stats`;
   `/mlb/player` + `/mlb/player-stats`; `/mlb/transactions` for
   signings/trades/IL moves; `/mlb/league-stats` for ranked league leaders.
4. **Strava** — `/strava/routes` (requires `sport` — one of `hiking`,
   `road-biking`, `mountain-biking`, `trail-running`, `gravel-biking` —
   plus `country`+`region` slugs) to browse routes; `/strava/routes/detail`
   (`path`) for one route; `/strava/clubs/{id}` for a club; `/strava/challenges`
   for current public challenges.

Full endpoint list, methods, and params: [`reference/endpoints.md`](reference/endpoints.md).

## Calling the API

```sh
# ESPN scoreboard + team:
scripts/crawlora.sh /espn/scoreboard sport=basketball league=nba | jq '.'
scripts/crawlora.sh /espn/team-roster sport=basketball league=nba team=lal | jq '.'

# SofaScore live + match detail:
scripts/crawlora.sh /sofascore/live-events sport=football | jq '.'
scripts/crawlora.sh /sofascore/event id=<event-id> | jq '.'

# MLB:
scripts/crawlora.sh /mlb/schedule date=2026-08-10 | jq '.'
scripts/crawlora.sh /mlb/player-stats id=<mlb-id> group=hitting | jq '.'

# Strava:
scripts/crawlora.sh /strava/challenges | jq '.'
scripts/crawlora.sh /strava/routes sport=hiking country=<country-slug> region=<region-slug> | jq '.'
```

Raw `curl` fallback:

```sh
curl -fsS -H "x-api-key: $CRAWLORA_API_KEY" \
  "https://api.crawlora.net/api/v1/espn/standings?sport=football&league=nfl" | jq '.'
```

## Endpoint reference

See [`reference/endpoints.md`](reference/endpoints.md) for every ESPN,
SofaScore, MLB, and Strava endpoint this skill uses.

## Examples

- **Live game tracker:** `/espn/scoreboard` or `/sofascore/live-events`
  polled on an interval to report score changes as they happen.
- **Pre-game brief:** `/sofascore/event-h2h` (history) + `/sofascore/event-odds`
  (market expectation) + both teams' `/sofascore/team-events` (recent form).
- **Season stat leaders:** `/mlb/league-stats` or `/espn/rankings` for
  top performers, then `/mlb/player-stats` / `/espn/athlete` for the detail.
- **Roster/transaction watch:** `/mlb/team-roster` + `/mlb/transactions` to
  track who's been added or dropped this week.

## Notes & limits

- **Credits / pay-on-success:** billed only on `2xx`; free tier 2,000 credits/mo.
  Key at [https://crawlora.net](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills).
- **Public data only** — public scoreboard/stats pages; odds are informational,
  not a betting service.
- **Security:** key lives in `CRAWLORA_API_KEY` only — never hardcode, query-param, or commit it.
- **ESPN and SofaScore cover many sports/leagues** via `sport`/`league`
  params — check `reference/endpoints.md` for the accepted values before
  assuming a league is supported.
- Live-score endpoints reflect the source's own update cadence — poll rather
  than assume sub-second freshness.
- **Strava's `country`/`region` are platform-specific slugs**, not free-text
  names — the exact slug format isn't in the tool schema; verify a working
  value at [crawlora.net/docs](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)
  or the [playground](https://crawlora.net/playground?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)
  if `/strava/routes` 404s — `/strava/challenges` needs no params and is a
  safe starting point.
