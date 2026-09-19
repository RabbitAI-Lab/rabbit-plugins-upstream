---
name: sports-betting-research
description: Researches public sportsbook markets, event schedules, live status, and game context using DraftKings Sportsbook, ESPN, and SofaScore through the Crawlora API. Use for odds snapshots and event comparisons, not wagering, account actions, or financial advice.
---

# Sports betting research

Compare public sportsbook markets with independent event context. Keep odds,
lines, game status, and schedules timestamped and separate from predictions.

## When to use this skill

- Find upcoming or live events and their public sportsbook markets.
- Compare moneyline, spread, total, or proposition prices where published.
- Cross-check an event's teams, players, schedule, and status with ESPN or
  SofaScore before discussing a market.
- Build a time-stamped odds board for research or reporting.

## Research workflow

1. Discover leagues and events with the DraftKings league/event routes. Resolve
   the event ID before requesting event context or markets.
2. Capture sportsbook market names, selections, odds, line values, timestamps,
   and suspended/closed state exactly as returned. Do not combine markets with
   different settlement rules.
3. Use ESPN or SofaScore for schedule and score context, matching by teams,
   date, league, and start time. Similar names are not proof of identity.
4. Compare snapshots only when collection time, locale, league, and market
   type are aligned. A price movement is observed change, not an explanation.

## Examples

```sh
scripts/crawlora.sh /draftkings/sportsbook/leagues | jq '.'
scripts/crawlora.sh /draftkings/sportsbook/featured-leagues | jq '.'
scripts/crawlora.sh /draftkings/sportsbook/league-events league_id=<id> | jq '.'
scripts/crawlora.sh /draftkings/sportsbook/event-markets event_id=<id> | jq '.'
scripts/crawlora.sh /espn/scoreboard sport=football league=nfl | jq '.'
```

## Notes and limits

- Public, anonymous market snapshots only. No bets, deposits, withdrawals,
  account access, or payment actions occur.
- Sportsbook availability, prices, and legal access vary by jurisdiction and
  time. Verify material decisions with the licensed operator and local rules.
- Odds are not forecasts or guaranteed returns. Do not present a snapshot as
  advice or infer insider information from a line change.

See [`reference/endpoints.md`](reference/endpoints.md) for the complete generated endpoint list.
