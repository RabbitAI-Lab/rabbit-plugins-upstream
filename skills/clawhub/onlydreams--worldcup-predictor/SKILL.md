---
name: worldcup-predictor
description: Use when analyzing or predicting World Cup or international football matches, especially when the user asks for match forecasts, score predictions, betting-market comparison, card or discipline forecasts, group qualification scenarios, knockout-stage scenarios, style matchup, player availability, post-match review, or iterative model corrections.
---

# World Cup Predictor

## Core Principle

Predict matches by combining market baseline, verified data, team news, style matchup, and match-state incentives. Do not let one signal dominate: odds can overprice favorites, scorelines can hide chance quality, and possession can hide low chance quality.

## Disclaimer

Use this skill for informational football analysis only. Predictions are uncertain and can be wrong; do not present them as guaranteed outcomes, betting advice, financial advice, or an instruction to wager. When betting markets, odds, or platforms such as Polymarket or Stake are discussed, state that they are evidence inputs for analysis rather than recommendations to bet.

## Task Routing

Classify the request before collecting evidence. Use only the route that fits the user request, and label a limited-evidence answer as provisional.

| Request type | Required focus | Reference section |
|---|---|---|
| Full pre-match forecast | all five source layers, score, failure mode | Forecast Workflow |
| Quick first pass | compact lean, unchecked layers, update triggers | `Fast-Pass And Lineup Revision` |
| Live update | current match state, named events, substitutions, chance quality | `Live Update Rules` |
| Post-match review | result, process, key-event variance, model record | `Post-Match Review Template` |
| Rules, VAR, or referee controversy | event facts, rule chain, evidence level | `VAR And Offside Review` / `Referee Controversy And Social Reaction` |

Detailed routes and templates live in `references/prediction-framework.md`.

## Required Source Discipline

Before forecasting, state which source layers were actually used:

| Layer | Examples | Rule |
|---|---|---|
| Market | Polymarket public market pages, Stake public odds pages, major books, screenshots only as fallback | Use as baseline, not verdict |
| Data | Sofascore, FotMob, Flashscore, WhoScored, FBref, match centre stats | Prefer for xG, big chances, saves, ratings, momentum |
| News | FIFA, federations, Guardian, BBC, ESPN, local beat reports | Use for injuries, suspensions, lineup clues, travel/weather |
| Context | group table, knockout bracket, path, schedule, venue, weather, governance and continuity signals | Use for motivation, risk appetite, and team stability |
| Style matchup | pressing, buildup routes, chance creation patterns, transition risk, set pieces | Use to explain how chances are created or denied |

If a layer is missing, say so and reduce confidence. Never claim Sofascore, FotMob, Flashscore, WhoScored, FBref, Stake, Polymarket, or lineup data was used unless it was directly read from a public page/API or supplied by the user. Treat FBref as a delayed review and validation source, not a real-time matchday source, unless current-match data is verified.

Start every non-trivial fixture-specific forecast, live update, or post-match review with an evidence snapshot: exact fixture, match start time/time zone when known, information cutoff time, and the source layers actually read. For time-sensitive sources, state the page state or timestamp rather than implying it is current. A general rules explanation needs this snapshot only when it analyzes a specific match event.

If the user mentions currently open match pages, browser tabs, live match pages, Sofascore, FotMob, Flashscore, Stake, Polymarket, lineups, odds, technical stats, or post-match review, first inspect available pages/tabs when the runtime provides browser state and identify the exact match/event page. Do this before opening new pages, guessing URLs, searching the web, writing a scraper, or using an API. Choose DOM reading, screenshot reading, or API/script access only after confirming what is already available. If browser automation opens temporary pages, preserve user-opened pages and clean up only the temporary pages where the tool supports it.

For a full match prediction, do not stop after reading only market odds or only schedule/context. Before producing the final forecast, make a visible attempt to check market baseline, recent performance/data, player availability/news, match-state incentives, and style matchup.

Treat advanced match data as high value but not always available. In pre-match forecasts, official lineups often appear only close to kickoff, and current-fixture xG or big chances do not exist yet; use recent match data, official match centre stats, credible news, and style/context checks instead. In post-match reviews, prefer xG, big chances, shot quality, and lineups when readable, but if Sofascore/FotMob/Flashscore are unavailable, use FIFA match centre, official reports, reliable recaps, and visible basic stats as fallback. Keep missing layers in the output and reduce confidence in the exact score or fine-grained tactical claim, not necessarily the whole winner lean.

User screenshots are fallback or supplemental inputs, not required inputs. Do not block a forecast waiting for screenshots when public pages, credible reports, or enough layer evidence are available; mark screenshot-dependent details as missing or provisional instead.

If the user explicitly asks for a quick first pass, "one round" forecast, or rough forecast before deeper verification, answer immediately with a clearly provisional forecast instead of blocking on full source collection. Still label missing layers and name the lineup, market, or news triggers that would change the prediction.

## Market Lookup Routing

For World Cup match odds, check dedicated market pages before generic search:

1. Open the Polymarket World Cup games page, such as `https://polymarket.com/zh/sports/world-cup/games`, and read visible moneyline/draw prices for the relevant fixtures.
2. Open the Stake World Cup soccer page directly: `https://stake.com/zh/sports/soccer/international/world-cup`, and read normal 1X2 decimal odds when the fixture is visible. Confirm the active market is normal win/draw/win, not handicap, totals, advancement, or a top-page large-bet card.
3. If Polymarket and Stake both lack readable fixture odds, use major public books, odds aggregators, or user-supplied screenshots as supplemental market input.

For another international competition, start from a public page for that exact competition or fixture, then use a second public book or odds aggregator if the first source is incomplete. Do not force a non-World-Cup fixture through World Cup URLs. Record which competition page and market type were actually read.

Do not conclude that market odds are unavailable from generic web search alone. Do not rely on Polymarket Gamma API team-name search as the first pass; it can return unrelated markets or miss sport/game aggregation pages. If Stake blocks access, requires heavy JavaScript, redirects away, or shows no normal 1X2 fixture odds after trying the direct World Cup page, mark Stake unavailable for that match and move on instead of retrying repeatedly. Ignore signup promos, free-bet boosts, and "50/1" style acquisition offers when setting a normal market baseline.

## Forecast Workflow

1. **Check calibration state**: only carry forward an explicit review or calibration record supplied in the current context or by the user. Do not imply access to an unstated cross-session record. Do not let a recent draw cluster cause blanket draw protection, and do not overcorrect back to paper favorites while ignoring injuries, starters, or role gaps.
2. **Identify match state**: date/time, group or knockout round, standings or bracket path, qualification/advancement incentives, and whether draw, extra time, or penalties change each team's risk appetite.
3. **Set market baseline**: follow the market lookup routing above, then convert visible prices/odds into rough favorite, draw, and total-goals expectations. Note liquidity, volume, wide spreads, stale pages, missing markets, or pages that only load earlier fixtures. Use Polymarket API only when public page text cannot expose the needed market or when orderbook/bid-ask detail is specifically required.
4. **Verify recent performance**: prefer last tournament match data over friendlies, but also inspect recent five friendlies/pre-tournament matches when available. For immediate matchday reads, prefer verified Sofascore/FotMob/Flashscore data or user-supplied screenshots; use WhoScored/Sofascore event or shot-level data when available; use FBref, StatsBomb free data, and Understat mainly for delayed review, model calibration, or historical context. Check opponent quality, xG/chance quality, shots on target, big chances, saves, player ratings, minutes, and whether the scoreline was misleading.
5. **Check player availability**: injuries, suspensions, illness, rotation, expected starters, whether key players are truly fit enough to execute their role for 60-70 minutes, and whether replacements preserve or change the team's main route to goal.
6. **Analyze style matchup**: test how each team creates chances, prevents chances, handles pressure, progresses the ball, defends transitions, uses set pieces, and changes structure through substitutions without forcing a preferred shape or formation.
7. **Stress-test paper favorites**: before backing a reputation-heavy or market-heavy favorite, require evidence that it can turn territory into high-quality box chances against this opponent. If recent matches show low-quality volume, weak striker/box occupation, overlapping creators, loose passing, weak rest defense, or limited second-ball pressure, cap the margin and raise draw, extra-time, and penalty branches instead of assuming automatic repair.
8. **Account for context**: heat/humidity, travel, home/host boost, kickoff time, venue surface, altitude, referee/discipline risk, and governance or continuity signals if known. Treat climate and host effects as modifiers, not master variables. For altitude, separate stadium familiarity and crowd pressure from physiological adaptation; do not give a large altitude edge to a host if the opponent routinely plays or trains at comparable or higher altitude.
9. **Produce prediction**: give winner/draw lean, exact score, backup score, separate result and exact-score confidence, and the single most important failure mode. For knockout matches, also separate 90-minute score, advancement lean, and advancement confidence. If odds or betting markets were used, include a brief disclaimer that the analysis is not betting or financial advice.
10. **Post-match review**: compare prediction with score, xG/chances, ratings, key events, substitutions, late-game control, and update the model. Do not overgeneralize from one matchday.

Do not repeat a completed layer while required layers remain unchecked. For example, once market prices have been read, move to data, news, context, and style instead of re-reading the same market page unless the market data is ambiguous or stale.

## Style Matchup Checks

Analyze team style without privileging a specific formation, build-up shape, or possession structure.

- Strong favorite is safer when it repeatedly creates high-quality chances and limits the opponent's most dangerous route to goal.
- Reputation-heavy favorites are unsafe when their advantage is mostly possession, names, or market price. Upgrade them only when lineup roles, recent chance quality, set pieces, bench impact, or opponent weaknesses show a repeatable route to clear chances.
- Be skeptical when possession, shot count, or territorial pressure does not translate into clear chances.
- Separate chance creation from finishing execution. A team can have ordinary buildup but remain dangerous if it has a reliable high-quality finisher, strong shot placement, or repeated xGOT overperformance from real chances.
- Distinguish **pressure** from **chance quality**. A team can have 70% possession, 20+ shots, and still mostly create low-value attempts.
- Extra man is not automatic advantage. Ask whether the team can turn numbers into clear chances, second-ball recovery, and defensive control.
- Big first-match wins can be false signals when the opponent collapsed, received red cards, or conceded unusually easy chances.

## Output Format

Use a compact table first:

| Match | Evidence cutoff | Sources used | Market baseline | Prediction | Result / score confidence |
|---|---|---|---|---|---|

Then add short match notes:

- **Evidence snapshot**: exact fixture, information cutoff time, and source layers actually used.
- **Calibration**: prior post-match lessons applied, and whether this is provisional or final based on lineup availability.
- **Prediction**: score and backup score.
- **Confidence**: separate result confidence from exact-score confidence; for knockout matches, add advancement confidence.
- **Knockout note**: for knockout matches, separate 90-minute result from advancement lean, extra-time risk, and penalty-shootout risk.
- **Cards note**: when referee or discipline evidence is sufficient, give a main card count, reasonable range, and main red-card trigger; otherwise give a qualitative discipline-risk read and state what is missing.
- **Why**: 2-4 strongest reasons.
- **Failure mode**: the most likely way the prediction breaks.
- **Missing data**: important unavailable source layers.
- **Disclaimer**: if odds or betting markets were used, state that the analysis is informational only and not betting or financial advice.

## Common Mistakes

Do not equate market price, reputation, possession, pressure-only data, or one scoreline with superior chance creation. Do not treat predicted lineups as official, infer an injury from a benching, stereotype a team or confederation, or apply group-stage incentives to a knockout match. For the detailed safeguards, use `references/prediction-framework.md`.

For detailed weighting, confidence rules, and review templates, read `references/prediction-framework.md`.
