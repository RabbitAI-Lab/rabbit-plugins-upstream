# Prediction Framework

## Evidence Weighting

Use these weights as a guide, then explain deviations.

Keep all forecasts informational. Odds, betting markets, and exchange prices are analysis inputs only; never frame a prediction as guaranteed, betting advice, financial advice, or an instruction to wager.

| Dimension | Weight | What to inspect |
|---|---:|---|
| Team/style matchup | 25% | chance creation, chance prevention, press resistance, transition defense, set pieces |
| Player availability/state | 25% | starters, injuries, suspensions, illness, role fitness, ratings |
| Current data | 20% | xG, big chances, shots on target, saves, chance locations, momentum |
| Market baseline | 15% | Polymarket, Stake, books, liquidity, line movement |
| Match-state/context/environment | 15% | group standings or knockout bracket, draw value, advancement path, host boost, heat, travel, governance and continuity signals |

Raise player availability above 25% when a team depends on one or two key roles: a build-up organizer, main ball progressor, primary chance creator, defensive organizer, goalkeeper, set-piece specialist, or main finisher. Use named players only as verified, tournament-specific examples; do not treat them as permanent rules. Availability means role fitness, expected minutes, and replacement quality, not just whether the player appears in the squad.

For knockout matches, raise the style-matchup weight when a favorite has not proven it can create high-quality chances against compact blocks. Paper strength, ranking, and possession become weaker inputs if the team lacks a clear box-occupation plan, reliable striker profile, second-ball pressure, or a bench route to change the rhythm after 70 minutes.

## Source Tiers

| Tier | Sources | Use |
|---|---|---|
| A | official lineups, FIFA match centre, federation injury updates | facts and availability |
| B1 | Sofascore, FotMob, Flashscore, FIFA match centre stats, user-supplied screenshots from these sources | immediate performance, lineups, player ratings, saves, big chances, shot xG when visible |
| B2 | WhoScored, Sofascore event maps, shot maps, heatmaps, Opta-style event data | event-level and tactical diagnosis when directly readable |
| B3 | FBref, StatsBomb free data, Understat | delayed review, historical validation, model calibration, and deep context rather than live matchday reads |
| C | Polymarket public pages, Stake public odds pages, major books | market baseline and consensus |
| D | Guardian/BBC/ESPN/local beat reports | narrative, context, quotes, style and matchup hints |
| E | social clips/forums | hypothesis only; verify elsewhere |

Mark uncertain facts clearly: confirmed, reported, inferred, or user-supplied.

Access discipline matters as much as source quality. If a site returns 403, requires heavy JavaScript, blocks automated access, or only appears through a user screenshot, say exactly that. Do not promote a source into "used" unless the relevant match page, API output, or screenshot was actually read.

For each non-trivial forecast, create a compact evidence snapshot before the prediction: exact fixture, scheduled kickoff and time zone when known, information cutoff time, source/page actually read, relevant market type, and whether each fact is confirmed, reported, inferred, or user-supplied. A source name alone is not enough for time-sensitive odds, lineups, or live statistics. Do not imply that a page was current when its timestamp, fixture identity, or market type was unclear.

If the user says relevant match pages are already open, or the task concerns live data, technical stats, lineups, odds, substitutions, or post-match review from likely open pages, first enumerate or inspect the available pages/tabs and confirm the exact match/event page. Use the already-open DOM or screenshot when it is readable; choose a new page, web search, API call, or script only after confirming the page is unavailable, incomplete, or too noisy. Do not guess event URLs or write a scraper before checking what the user has already opened. If browser automation opens temporary pages, preserve user-opened pages and clean up only the temporary pages where the tool supports it.

Predicted lineups from Sofascore, FotMob, other apps, or user screenshots can inform the pre-match personnel layer, but label them as predicted, not official. After reading a predicted lineup, list the specific lineup triggers that would change the forecast: main finisher starts or sits, defensive organizer returns, ball-progressor fitness, goalkeeper change, or whether a key player is fit for 60-70 minutes.

Distinguish a confirmed starting XI, a warm-up late replacement, and an in-match injury substitution. For a late pre-kickoff replacement, reassess the lost role, replacement fit, and changed route to goal or defensive control; do not assume it uses a normal match substitution or changes the remaining-substitution budget unless the competition rules and event record confirm it.

Screenshots are fallback or supplemental evidence, not a hard gate. Do not ask for or wait on screenshots if public pages, credible reports, or enough other source layers support a forecast. If a screenshot would improve a specific claim, mark that claim provisional or missing and continue with lower confidence.

For live matches, keep source types separate: confirmed page data, user-observed broadcast details, and tactical inference. Do not present a broadcast observation or inference as page-confirmed data.

For substitutions, use the player names in a readable event log or lineup as the authority. Do not identify a player from a shirt number or memory when that named source is available.

## Market Reading

- Prefer public web pages for market baselines: Polymarket event/market pages, Stake public odds pages, and major books. Use screenshots only when live page access is unavailable.
- For World Cup fixtures, start from dedicated aggregation pages before generic search:
  - Polymarket World Cup games: `https://polymarket.com/zh/sports/world-cup/games`
  - Stake World Cup soccer page: `https://stake.com/zh/sports/soccer/international/world-cup`
  If these dedicated pages do not expose the fixture odds, then use major public books, odds aggregators, or user-supplied screenshots as supplemental market input.
- Do not treat a failed generic search, a team-name-only Polymarket Gamma API search, or an unrelated API result as proof that odds do not exist. The public sport/game aggregation page can expose fixtures that API search misses.
- For Polymarket public pages, read visible market text first: moneyline, draw, spreads, totals, BTTS, first-team-to-score, displayed volume, and any visible probability/cent price. Clean duplicated or concatenated page text before using it.
- For Stake public pages, use the direct World Cup soccer URL first. If it blocks access, requires heavy JavaScript, redirects away, or shows no normal 1X2 fixture odds, record Stake as unavailable for that match and move on. Do not keep retrying Stake, do not infer that the whole market layer is unavailable, and do not invent odds.
- If Stake's generic soccer page redirects to casino/home, do not mark Stake unavailable until the direct World Cup URL `https://stake.com/zh/sports/soccer/international/world-cup` has been tried.
- If Stake's `/world-cup/all` variant shows no results or an incomplete list, retry the base World Cup URL before marking Stake unavailable. Record the exact page state: empty list, redirected, blocked, stale fixtures, or readable fixture rows.
- On Stake, record the active market selector. Use `获胜盘` or normal win/draw/win for 90-minute 1X2; use `让分盘` only for handicap reads, `总分盘` for totals, and `晋级` or equivalent markets only for advancement. Do not mix these markets in one probability line.
- On Stake, distinguish the complete fixture row from top-page "large bet" or promoted cards. Large-bet cards can repeat the same fixture and expose only one side of the price; use the fixture list row that shows all three normal 90-minute 1X2 decimal prices before setting the market baseline.
- Separate normal 1X2 decimal odds from signup offers, free bets, odds boosts, and acquisition promos. Promotional prices are not a market baseline.
- Do not claim Polymarket orderbook depth, bid/ask spread, midpoint, or token-level detail unless an API/orderbook source was actually read. Public page text is enough for baseline probability, not precise execution quality.
- Convert odds/prices into rough probabilities, but avoid false precision when using screenshots or noisy page text.
- Compare 1X2 with handicap and totals.
- Favorite with weak handicap support often means small win, not blowout.
- Heavy favorite plus deep handicap support plus group net-goal incentive supports multi-goal predictions in group matches.
- Low total with strong favorite supports 1-0 or 2-0 rather than 3-1.
- Polymarket low liquidity, low volume, stale visible prices, or very wide spread should be weak reference only.

## Data Reading

Prefer tournament data over friendlies, but still inspect the recent five friendlies/pre-tournament matches when available. Use them for role continuity, minutes, opponent quality, and player state; use current tournament data for the stronger read on actual chance quality.

Immediate performance sources:

- Use FotMob, Sofascore, Flashscore, FIFA match centre, or user screenshots for live scores, lineups, substitutions, shots, shots on target, big chances, saves, ratings, and visible xG. If screenshots are absent, continue with readable public data and mark screenshot-only details as missing.
- Use Sofascore shot xG, player ratings, heatmaps, and event views when available; they are especially useful for distinguishing real pressure from low-value shot volume.
- Use momentum charts only as pressure context. They should not override xG, big chances, shots on target, xGOT, shot locations, forced saves, or visible substitution effects on chance quality.
- Use WhoScored or Opta-style event data for tactical questions such as ball progression, repeated turnovers, zone occupation, and whether a midfield disconnect is structural.
- Do not treat unavailable xG, big chances, shot-quality views, or official lineups as a blocker by itself. For pre-match forecasts, current-fixture xG and big chances do not exist, and official lineups may be unavailable until close to kickoff. Use recent tournament stats, official match-centre basics, credible team news, expected lineup reports, and role/style evidence as fallback.
- For post-match reviews, try the advanced data sources first. If they are unavailable, still review with the best readable evidence: score timeline, shots, shots on target, possession, cards, substitutions, official match reports, reliable recaps, and market expectation. Mark the missing advanced data and lower confidence in fine-grained chance-quality claims.

Delayed review sources:

- Use FBref for next-day or later validation of aggregate and advanced stats. Do not treat it as a real-time source.
- Use StatsBomb free data for historical learning, event-data practice, and model calibration; do not assume current World Cup coverage.
- Use Understat as an xG reference mainly for covered club competitions; verify coverage before using it for national-team matches.

For the previous match, ask:

- Was the score supported by xG and big chances?
- Did xG and xGOT tell the same story, or did finishing/shot placement change the result?
- Did a goalkeeper produce an outlier performance?
- Were red cards, early goals, penalties, or game-plan collapses decisive?
- Did the team create box entries and high-quality shots, or only low-value volume?
- Which players had high ratings for repeatable actions: saves, key passes, duels, progressive carries, defensive actions?
- Did the team look structurally stable under the opponent it faced, or did loose passing, weak rest defense, repeated turnovers, or soft defensive pressure let an inferior opponent generate too many shots or shots on target?

For lineups and availability, separate bench, rotation, managed minutes, and true absence. Do not infer injury from a star starting on the bench unless credible injury/availability reporting confirms it.

## Fast-Pass And Lineup Revision

When the user explicitly asks for an immediate first pass, whole-round forecast, or rough prediction, do not over-invest in full verification before answering. Produce a compact provisional read, then state what is missing.

- Label it clearly as a rough or provisional pre-match forecast.
- For knockout batches, still split 90-minute score, advancement lean, and extra-time or penalty risk.
- If cards are requested and referee or comparable discipline data is available, give a main card count plus range. Otherwise give a qualitative discipline-risk read, name the missing referee data, and do not invent a precise card count.
- Preserve the source-layer structure: market, data, news, context, and style. Mark unchecked layers rather than pretending they were read.
- Name the triggers for a later update: official lineup, key role starting or sitting, market move, injury/suspension report, referee assignment, weather, or venue shift.
- If a later lineup, odds screenshot, or live page update arrives, update the affected layer first. Do not rerun every layer unless the stale layer could change the conclusion.
- A missing star, creator, or transition partner lowers that route's weight but does not erase the team's scoring path. Recheck set pieces, secondary runners, defender targets, long shots, second balls, goalkeeper variance, penalties, and bench routes before moving to a clean-sheet forecast.

Pattern examples:

- A 0-0 with high shot volume and many goalkeeper saves can show real pressure, but finishing variance or a goalkeeper outlier may break market expectation.
- A possession-dominant 0-1 loss does not prove poor team quality by itself; inspect whether possession became high-quality chances.
- A reputation-heavy favorite can underperform when the actual team sheet removes key chance creation, progression, defensive control, or finishing roles.
- A favorite with consecutive low-efficiency attacking games should not be treated as due for automatic rebound. Upgrade only if the lineup, roles, or previous-match chance quality show a real route to repair.
- Split inefficient favorites into low-quality volume and high-quality under-conversion. Keep margin capped for low-quality volume, but allow a rebound scoreline when prior matches show strong xG, big chances, shots on target, repeated box entries, or an opponent with weaker defensive personnel.
- In knockout matches, high-quality under-conversion by a favorite raises both comeback potential and accident risk. If a team has clear xG, big chances, box touches, and forced saves but fails to score early, keep its chance-creation rating high while raising the risk of a counterattack goal, set-piece goal, extra time, or late chaos.
- Split chance creation from finishing execution. xG, big chances, box entries, and cutbacks describe chance creation; xGOT, shot placement, finishing record, and goalkeeper-forcing shots describe conversion quality. Do not downgrade a team only for ordinary buildup if it has a repeatable route to a top finisher or consistent high-xGOT shots.
- Apply a finishing-edge modifier in knockout matches. A low-volume or average-possession team with an elite finisher, strong shot placement, or high xGOT conversion can keep a stronger advancement path than its buildup quality alone suggests, especially when the opponent must open up after conceding.
- Separate pressure volume from pressure quality. Corners, crosses, box touches, possession, and total shots are not real domination unless paired with cross completion, shots on target, big chances, xG, xGOT, second-ball recovery, or forced saves.
- Separate sterile possession from real dominance. Upgrade possession teams when xG, big chances, shots on target, corners, box touches, and opponent shots on target all support the same story; do not call it real dominance from possession alone.
- Separate statistical superiority from team state. A favorite can win the xG battle and still be in poor form if role players are misfiring, passing is careless, rest defense is loose, or a much weaker opponent produces repeated shots on target and transition entries.
- Separate black-horse status from geography and historical brand. A non-traditional power that has repeated major-tournament knockout success, won a continental title, or shown multi-cycle defensive and transition stability should be treated as an established strong team until current form says otherwise.
- For a reputation-heavy knockout favorite, ask whether its recent possession became clear chances against set defenses. If not, move a regulation draw, extra time, and penalties into the central forecast instead of leaving them as a remote failure mode.
- An underdog that creates repeatable scoring routes across matches should be upgraded from "can frustrate" to "has a stable goal path." Track set pieces, direct play, crosses to a target forward, transition carries, long shots, and second balls.
- Separate underdog resistance from underdog scoring. A compact low block, goalkeeper form, or defensive stamina can keep the score close without supporting BTTS. Upgrade underdog goals only when there is a repeatable route: target-forward outlet, set-piece taker, transition carrier, second-ball structure, or opponent-specific defensive gap.
- Do not reduce an underdog's goal path to one star pairing. If the main transition carrier or partner is absent, still check set pieces, defender runs, secondary wide outlets, rebounds, penalty-box chaos, late bench speed, and opponent concentration errors.
- In chaotic knockout scores, separate the pre-match process from key-event variance. Early goals, saved penalties, disallowed goals, goalkeeper outliers, and stoppage-time winners can make a sound xG or chance-quality read produce the wrong exact score.

## Knockout Preparation Review

Before knockout forecasts, run a compact tournament-to-date review instead of sorting teams by name value or power ranking alone.

- Separate external media evaluation from your own read. Media consensus is calibration, not the conclusion.
- Review actual match content: chance quality, opponent quality, game-state effects, defensive concessions, set pieces, transition exposure, and whether scorelines flattered or hid the team.
- Review team status in the current cycle. Do not use "black horse" as shorthand for countries outside the classic elite if recent World Cup, continental tournament, and qualifying evidence shows repeatable high-level performance.
- Review bench and integration: whether substitutes changed the game, protected a lead, restored chance creation, or kept defensive structure after 70 minutes.
- Review core state: whether the main finisher, creator, ball progressor, defensive organizer, and goalkeeper look fit enough for knockout tempo and potential extra time.
- Review opponent strength already faced. Do not grant a favorite a contender-level ceiling until it has either handled a credible high-pressure opponent or shown stable ball security, defensive concentration, and chance creation against the opponents it has faced.
- Review knockout-specific risk: extra-time stamina, penalty profile, yellow-card suspension pressure, referee/card exposure, and whether the team has a plan B when its main route is blocked.

## Calibration Discipline

- Calibration is context-bound. Reuse only an explicit post-match review or calibration ledger supplied in the current context or by the user; never claim an unstated cross-session memory, record, or model update.
- For iterative tracking, keep a compact record with the match, forecast timestamp, 90-minute lean, exact-score confidence, result confidence, market baseline, source completeness, regulation outcome, final/advancement outcome, process verdict, and error category. If normalized 1X2 probabilities were explicitly produced, record them and calculate a Brier score or comparable metric; do not manufacture probabilities solely to score a past forecast.
- A complete forecast cannot be market-only or context-only. After a market page has been read, preserve that market baseline and move on to recent performance/data, player availability/news, match-state incentives, and style matchup. Do not re-read the same market source unless the captured price is ambiguous, stale, or incomplete.
- If Sofascore/FotMob/Flashscore/xG, lineup, or injury data cannot be read, say exactly which layer is missing. Missing advanced event data mostly caps confidence in exact score, margin, and chance-quality claims; missing key availability or lineup facts can cap confidence in the winner lean. Do not silently replace missing data with market prices.
- Carry forward explicit lessons from recent post-match reviews before making a new forecast.
- After a run of draws, raise draw awareness but do not apply blanket draw protection.
- After noticing overconservatism, do not swing back to paper-strength favorites without rechecking key role fitness, starters, and recent chance quality.
- After a paper-strength favorite fails because it could not break a compact block, do not correct only the specific team. Generalize the rule: reputation, ranking, and market price need proof of chance quality, box occupation, set pieces, bench impact, or transition control before supporting a confident regulation win.
- After a favored team has failed to score from open play or produced repeated low-quality volume, cap its margin and raise draw risk until there is concrete evidence of chance-creation repair.
- After a favorite advances while looking disjointed, downgrade future regulation-win confidence even if aggregate xG was strong. Treat loose passing, poor defensive concentration, misfiring key roles, and too many opponent shots on target as form warnings, especially if the opponent has not been an elite stress test.
- When a narrow score is driven by an outstanding goalkeeper performance against clear xG, big chances, and shots-on-target dominance, record it as finishing or goalkeeper variance rather than an attacking-process failure.
- In low-score reviews, distinguish a balanced low-event match from one-sided suppression hidden by poor finishing or an exceptional goalkeeper. A correct low-total or exact-score call is only a partial process hit when the predicted game shape was cautious or balanced but the actual chance creation was heavily one-sided.
- Reconcile cross-source counting differences before grading the forecast. When shots on target, saves, goals, cards, or xG disagree, keep one provider's internally consistent totals or name each provider and counting rule; do not combine incompatible totals into a synthetic match record.
- After post-match reviews show that corners, box touches, or territorial pressure did not create goals, reduce the weight of pressure-only indicators until they are paired with xG, big chances, shots on target, xGOT, or forced saves.
- After a favorite controls possession or wins xG but advances narrowly through a penalty, goalkeeper performance, or poor finishing from open play, keep the favorite's advancement quality separate from its regulation-margin quality. Do not automatically upgrade the next forecast to a comfortable win.
- Do not let historical baggage, past-round narratives, or national-team stereotypes outweigh current execution. Treat them as psychological modifiers only, and reweight quickly after early pressing success, first-goal match-state change, crowd momentum, or visible duel advantage.
- After a smaller team shows real scoring routes in consecutive tournament matches, give that route independent weight even if market price, reputation, or possession profile still favors the opponent.
- After a team sustains success across a World Cup run, continental title, and current knockout performance, move it from "black horse" framing into the stable-team bucket unless player availability or recent execution clearly regresses.
- Strong teams with healthy elite creators/finishers should not be flattened into default draws by climate or opening-round caution alone.
- Structural or role gaps should usually cap margin first, then raise draw risk; they should not automatically flip the match to an upset.
- Public criticism from core players about rushed federation rebuilds, leaks, squad discontinuity, or instability is a high-weight cohesion signal, not ordinary post-match venting. Downgrade team cohesion, tactical continuity, defensive coordination, and late-game resilience. Keep unverified corruption, payment, or internal-politics claims separate until sourced.
- If final lineups are unavailable, label the forecast provisional and name the specific lineup triggers that would move the score or winner lean.
- A doubtful player who starts is not automatically fit for a full match. Keep a minutes/role-fitness branch after lineup confirmation; if the player leaves at half-time or early, record managed minutes or fitness uncertainty unless a reliable source confirms the reason. Do not retrospectively label the predicted XI simply right or wrong.
- In post-match review, classify key-event variance separately from model error: early red card, goalkeeper error, VAR reversal, penalty save, injury substitution, or extreme finishing. Explain whether the pre-match read was wrong before the event, or whether the event changed the match state.
- Before attributing dominance or the result to a red card, compare the pre-card score, shots, shots on target, xG, territory, and chance pattern with the post-card phase. Treat the dismissal as an amplifier rather than the root cause when the match was already structurally one-sided.
- Separate a high-total distribution miss from extreme finishing variance. If the pre-match matchup, rotation, and incentives supported an open game but the forecast stayed in a normal low-to-moderate scoring range, record a total-baseline or tail-risk miss even when the final score also ran far above xG or xGOT. Raise the expected total and widen the score distribution only as far as the repeatable evidence supports; do not calibrate all the way to one outlier scoreline.
- In knockout reviews, score the 90-minute forecast before judging the final extra-time or shootout result. Treat extra-time goals, a red card that changes the late opportunity set, and post-90-minute VAR decisions as separate branches; they can validate an advancement lean without proving the regulation-margin call.
- Grade exact scores by phase. If the final score after extra time matches the forecast but the 90-minute score does not, record a final-score hit and a regulation exact-score miss rather than a full exact-score hit.
- When a favorite generates strong xG, big chances, shots on target, and territorial pressure but concedes through low-frequency routes, keep the chance-creation process mostly intact while updating the conceded-goal routes. The correction may be "underdog scoring route was underweighted," not "favorite was overrated."

## Live Update Rules

- At halftime or any requested live checkpoint, reconcile a compact event ledger before interpreting the technical statistics: current score and scorers, cards, penalties or VAR decisions, injuries, substitutions, and stoppage time. Cross-check a readable event log against the lineup when possible, label user-observed events as user-supplied, and state when the reason for a substitution is unknown. Do not describe a change as tactical when the event record marks an injury substitution.
- After an early underdog goal, do not overreact to score alone. Check whether the favorite is creating real chances or only territorial pressure, and whether the underdog still has a second-goal route.
- At halftime, update from xG, big chances, shots on target, substitution needs, and whether the favorite has obvious bench fixes. Do not anchor to pre-match market strength if current chance quality contradicts it.
- Around 60 minutes, substitutions become a major model signal. Upgrade or downgrade only when they change chance quality: crossing quality, one-v-one threat, central occupation, pressing, second-ball recovery, or rest-defense exposure.
- Interpret substitutions structurally, not as a player list. Identify who now progresses the ball, who occupies the box, who protects second balls, who supplies width, and what counterattack or rest-defense risk the change creates.
- Do not treat a defender-for-attacker substitution by a leading team as an automatic defensive upgrade. Reassess ball retention, pressure-release passes, transition outlets, counterthreat, box-entry suppression, and second-ball coverage. Adding defenders while removing multiple progressors or outlets can invite repeated attacks and increase late-concession risk.
- Do not name a formation change from substitutions alone. Confirm it from visible positions, heatmaps, build-up structure, or repeated defensive shape; otherwise describe the likely role and risk change as an inference.
- Treat an 80th-minute-or-later attacking substitution as an immediate chance-quality signal, not automatically as preparation for extra time. Reassess the next few attacks, especially set pieces, box occupation, and second-ball coverage, before assigning its main purpose.
- After a goalkeeper replacement, increase short-term variance around shot-stopping, rebound control, crosses, and defensive communication. Do not label the change an injury, or infer its exact effect, unless the event record or reliable reporting confirms it.
- When a favorite removes multiple central creators or progressors while chasing, expect more direct play, wide attacks, crosses, and second balls. This can increase goal probability through box numbers while lowering midfield control and raising late transition risk.
- After an equalizer, reset from the new score and remaining time, then reassess both sides' risk appetite and substitution optionality. Check whether the former leading team has already removed progressors, creators, or transition outlets and whether its remaining personnel can reopen the game; do not carry forward its pre-equalizer protection confidence.
- Do not make large live probability jumps from substitution labels or defender count alone. Anchor numeric changes to the score-and-time baseline, current xG, big chances, shots on target, recent pressure, on-field roles, and remaining outlets. If no live model or readable market supports a number, prefer calibrated qualitative confidence to unsupported precision.
- After a favorite takes a late lead, the main danger often shifts from open-play control to set pieces, second balls, direct play, chaotic box entries, and transition exposure.
- After late stoppage-time goals or VAR reviews, distinguish process from outcome. A disallowed equalizer may still reveal a real weakness in box control, aerial defense, second-ball coverage, or late-game decision-making.

## VAR And Offside Review

For controversial goals, explain the decision as a rules chain rather than only accepting or rejecting the outcome.

- Separate physical fact from rules judgment: who touched the ball, when the touch occurred, where players were positioned, whether an offside-position player became involved, and whether a defender's touch was a deliberate play or a deflection/rebound/save.
- For offside, identify the last attacking teammate touch that resets the offside line. A slight attacking touch confirmed by connected-ball technology, audio, or video can create a new offside moment even if it is difficult to see on broadcast.
- A defender's touch does not automatically reset offside. Reset only when the defender deliberately plays the ball with enough control, sight, time, and body coordination. Passive deflections, instinctive blocks, rebounds, and saves do not "clean" an attacker who was already in an offside position.
- If a player appears to run back onside before receiving or playing the ball, still evaluate the position at the teammate's last touch, not only the later receiving moment.
- Treat social clips as hypotheses. Verify the rule chain with official event logs, credible recaps, IFAB Law 11, and available technology explanations. Mark which facts are confirmed by technology, which are visible on video, and which are referee interpretation.

## Referee Controversy And Social Reaction

When asked about post-match referee discourse, social-media complaints, or claims of bias, separate evidence levels before concluding.

- Event-log confirmed: goals, cards, fouls, penalties, VAR checks, substitutions, injury time, and official disciplinary records.
- Video-visible but judgment-dependent: contact intensity, holding, obstruction, advantage, off-ball blocking, simulation, dissent, and whether a defender had control.
- Rule-chain claims: offside phase, deliberate play versus deflection, handball position, penalty-area contact, DOGSO or SPA threshold, and VAR clear-and-obvious reviewability.
- Sentiment and allegation: fan outrage, coach/player quotes, federation statements, conspiracy claims, or "FIFA bias" narratives. Treat these as context or hypotheses unless a credible report substantiates them.
- In the output, name the disputed incidents and state whether each is confirmed fact, visible interpretation, or unsupported allegation. Do not convert social-media volume into proof of referee intent.

## Cards And Referee Risk

Use a range, not false precision. A card forecast should include a main count, a reasonable range, and the main red-card trigger.

- State the counting convention before forecasting or reviewing cards. Separate single-yellow player totals, every yellow-card event, second-yellow dismissals, straight red cards, and technical-area cards; providers may display a player sent off for two cautions under red cards while excluding those cautions from the yellow total.
- Start with referee profile when available: yellow-card average, red-card frequency, penalty frequency, tolerance for dissent, tactical fouls, and advantage play.
- Separate tournament-wide referee environment from single-match referee behavior. Compare multiple matches before saying the tournament is loose or strict: contact tolerance, dissent tolerance, dangerous-tackle enforcement, VAR intervention, foul volume, yellow-card volume, red-card triggers, and whether cards skew toward the trailing or protesting team.
- Adjust for knockout intensity, rivalry, elimination pressure, and whether one team is likely to defend long stretches or make repeated transition-stopping fouls.
- Identify team-specific foul points: fullbacks isolated against wingers, midfielders chasing faster carriers, aerial duel mismatches, late recovery tackles, and repeated tactical fouls after turnovers.
- Account for match state: early goal, trailing favorite, protecting a lead, extra-time fatigue, and late desperation can move cards above the baseline.
- Do not equate foul volume with yellow-card volume. A referee who tolerates contact, dissent, or off-ball disruption can produce a match that is more fragmented and physical but still below the card-count model.
- During live review, lower the remaining-card forecast if the referee has allowed repeated non-dangerous fouls without cards through roughly 55-65 minutes. Keep a high-card branch only when dissent, repeated transition stops, dangerous tackles, or late chasing-state escalation appears.
- For teams that rely on high-contact disruption, tactical fouls, or small off-ball actions, raise the foul/control-risk read first. Raise the card forecast only when the referee profile, early threshold, rivalry pressure, or repeated transition stops support it.
- Distinguish total-card forecast from team-card distribution. A tolerant referee can allow many fouls with a low total, while dissent, chasing state, or repeated transition stops can skew cards toward one team even when total cards stay near the expected range.
- When post-match comments claim a team "committed many small fouls but avoided cards," treat that as a contact-threshold signal, not automatic proof of bias. Verify foul counts, advantage calls, repeated infringement warnings, dissent cards, tactical stops, and whether the opponent's cards came from protests or chasing-state fouls.
- For South American teams, use a style modifier rather than a stereotype. Upgrade foul/control-risk when the current team shows high-contact duels, tactical fouls, off-ball blocks, set-piece wrestling, game-management delays, or referee-pressure behavior. Do not automatically upgrade yellow cards unless the referee profile and early threshold punish that behavior.
- If a high-contact team gains from a permissive referee, reflect it in the match model: more broken rhythm, more opponent frustration, higher protest-card risk for the opponent, and lower clean-possession quality. This can matter even when the total-card forecast stays moderate.
- Keep suspension and prior red-card history separate from moral judgment. Use it only when it affects player behavior, referee attention, or lineup risk.
- Output example: "cards main 5, reasonable range 4-6; red-card risk medium if Team B's fullback is repeatedly isolated."

## Venue And Host Modifiers

Do not treat a regional or co-host venue as full home advantage by default.

- Split host effect into geography/travel, crowd mix, time zone, climate, stadium surface, familiarity, media pressure, and referee atmosphere.
- Split altitude into stadium familiarity, crowd pressure, and physiological adaptation. A host at altitude gets less unique edge when the opponent routinely plays, trains, or qualifies at comparable or higher altitude. In those cases, keep the host modifier mostly to crowd/stadium familiarity rather than stamina.
- A co-host playing in another co-host country, neutral NFL-style venue, or mixed-crowd city usually gets a small modifier unless evidence shows a clear crowd or travel edge.
- Host pressure can help intensity but also increase finishing tension, disciplinary risk, or over-aggression. Treat it as directional context, not a decisive input.

## Style Matchup Diagnostics

Do not force every team into a preferred formation, build-up shape, or possession model. Evaluate whether the team's actual approach creates and prevents high-quality chances.

When a possession team counterpresses effectively after losing the ball, evaluate its defensive value through the transition chances it removes from the opponent, not only through its own possession share or attacking output. Check whether the opponent can find a first and second forward pass, whether midfield receivers can turn, and whether recoveries lead to progression or immediate turnovers and back-passes. If a transition-dependent team repeatedly loses its progression outlets and cannot launch its preferred attacks, treat that as a structural style neutralization rather than reducing the diagnosis to an individual attacker having a poor game.

### Positive indicators

- The team creates repeatable high-quality chances, not just territory or shot volume.
- The team has a credible plan B when central combinations fail: target-forward outlet, wide crossing with box numbers, set-piece threat, second-ball counterpress, or substitution pattern that has already changed games.
- Ball progression remains functional under pressure.
- Defensive spacing limits the opponent's best chance creation route.
- Set pieces, transitions, wide play, central combinations, or direct play fit the available players.
- Game state changes do not immediately remove the team's main route to goal.
- Substitutes preserve or improve intensity after 70 minutes, especially chance creation, defensive control, and transition protection.

### Warning indicators

- Possession or pressure produces few clear chances.
- A favorite's main edge is mostly reputation, ranking, or possession, while recent matches show few big chances, weak box occupation, or low-quality shot volume.
- A favorite has not faced a strong opponent yet but already shows careless passing, loose rest defense, weak defensive pressure, or dependence on one or two players to rescue poor team structure.
- Key creators occupy the same zones and reduce each other's influence.
- Injuries or role changes remove the team's main progression, creation, or finishing route.
- Recent coaching change, abrupt youth rebuild, public leaks, or player-confirmed lack of shared playing time undermines coordinated pressing, defensive spacing, set-piece assignments, and late-game resilience.
- Aggressive attacking choices leave repeated high-value counterattacks.
- Heavy favorite pressure can weaken rest defense. Adding attackers may increase comeback probability and concession risk at the same time.
- The team needs to chase but lacks tools to create better chances.
- The team is starter-dependent and its bench cannot protect leads, change attacking rhythm, or handle extra-time intensity.

## Match-State Incentives

### Group Stage

- Team on 3 points may accept draw if it nearly secures qualification.
- Team on 1 point against weak opponent may chase net goal difference.
- Team on 0 points in match two usually cannot accept a draw, but may still lack tools to chase.
- Third-place qualification pressure can raise draw probability, but it does not automatically imply a low-total match. Separate draw incentive from low-scoring incentive. If either side has strong transition attackers, set-piece threats, or an early-goal path, keep 2-2 or 3-3 draw states alive.
- A team that is safe with a draw may still chase second place, bracket position, host momentum, or internal selection credibility. Do not treat "draw is enough" as "draw is preferred" unless team news, coach quotes, lineup choices, and market totals support it.
- Rotation impact must be evaluated for both teams. If the underdog or near-peer removes its main finisher, progression hub, goalkeeper, or defensive organizer, upgrade the favorite's margin even if the favorite is also qualified.
- Already qualified is not enough to downgrade a favorite. Check whether the opponent is rotating core roles, whether the favorite's replacements preserve chance creation, and whether goal difference, group position, or momentum still matters.
- Team already eliminated may either rotate, collapse, or play freer. Do not assume a pride rebound unless lineup intent, player buy-in, coaching stability, and cohesion signals support it.
- Path incentives matter only if teams can realistically control placement; do not overweight speculative bracket choices early.

### Third-Place Playoff

- Do not equate reduced title or elimination pressure with low intensity or a low total. Check whether both teams can play more freely, whether an early concession has little downside beyond the placement result, and whether either side still has selection, individual-award, or tournament-record incentives.
- When both teams retain elite creators, finishers, or transition outlets but rotation removes goalkeepers, central defenders, midfield screens, press leaders, or defensive organizers, raise both the expected goal total and the high-scoring tail. Individual attacking quality can survive rotation more easily than coordinated defensive spacing and communication.
- Weight rotation by role and spine continuity, not by headcount. Compare the remaining goalkeeper-center-back-midfield protection chain with the available creators, finishers, transition runners, set-piece threats, and attacking bench; treat asymmetric damage to one defensive spine as a margin signal as well as a total-goals signal.
- After an early goal, reassess for a feedback loop: the trailing side may open up sooner, while a leading side with credible transition outlets can keep creating high-value chances. In this setup, do not merely move a conservative scoreline up by one goal; widen the distribution and keep a clearly labeled high-total branch while lowering exact-score confidence.
- Do not force an open-game adjustment when key attackers are rested, fatigue or weather suppresses tempo, both coaches preserve compact structures, or recent data and market totals show weak chance creation. Third-place status is a conditional modifier, not a standalone over-goals rule.

### Knockout Stage

- Separate 90-minute prediction from advancement prediction. A team can be more likely to advance without being clearly likely to win in regulation.
- Keep decision-stage probabilities unambiguous: `reach extra time` includes matches later settled in extra time or on penalties, while `decided in extra time` and `reach penalties` are separate branches. If outputting mutually exclusive stages, label them as `90-minute decision / extra-time decision / shootout decision`.
- For finals, use recent final-specific extra-time frequency only as a bounded context prior alongside current 90-minute draw prices, styles, goalkeeper quality, and attacking intent. Do not let a small historical sample override the current matchup, but do not apply a generic knockout-stage prior without checking the final-specific pattern.
- Do not apply group-stage third-place, goal-difference, or "draw is enough" logic to knockout matches. A draw after 90 minutes means extra time and possibly penalties, not a final table outcome.
- Weak or near-peer teams may rationally aim to reach extra time or penalties if their open-play chance creation is limited but their goalkeeper, penalty takers, defensive block, or fatigue profile is competitive.
- Favorites may avoid high-risk chasing while level, especially early, but should become more aggressive if extra time hurts them more than the opponent or if their bench can change chance creation.
- Leading teams may protect game state earlier than in group matches; trailing underdogs may open up later, raising late-goal, counterattack, and extra-time variance.
- Reassess the whole game shape after the first goal. A team with a credible counterattacking finisher or high-quality transition outlet can see its advantage grow nonlinearly once the opponent has to chase.
- Evaluate extra time separately: bench quality, injury load, recent minutes, age profile, heat, travel, pressing style, and late-game control can move the advancement lean even if the 90-minute score lean stays level.
- Starter-dependent teams should carry explicit extra-time risk if substitutions have not preserved intensity or chance creation after 70 minutes.
- Evaluate penalty shootouts explicitly when the match is close: goalkeeper penalty record, penalty-taker availability, set-piece/finisher substitutions, captain/leader presence, fatigue, and recent pressure-game history affect confidence.
- Treat the shootout as its own matchup. A slight 90-minute or open-play edge does not automatically become a penalty edge; goalkeeper penalty profile, taker depth, late substitutions, captain/leader presence, fatigue, and recent pressure history can flip advancement confidence.
- When the favorite's open-play chance creation is unproven, do not write "favorite advances" without a regulation draw branch. Use formulations such as "1-1 after 90; favorite slight edge in extra time" or "favorite stronger on paper, but penalty path is a major live branch."
- When market data is available, distinguish 90-minute 1X2, to-advance markets, extra-time/penalty props, and totals. Do not mix a regulation draw price with an advancement probability.
- Treat low 90-minute draw odds as a main knockout signal, not a footnote. If the 1X2 market prices the draw close to one or both teams, move extra time and penalties into the central forecast even when one team remains the better advancement lean.
- Output knockout forecasts as regulation score plus advancement lean, for example: "1-1 after 90; Team A advances after extra time" or "0-0 after 90; Team B advances on penalties."

## Confidence Labels

| Confidence | Use when |
|---|---|
| High | market, data, personnel, and motivation align; low missing-data risk |
| Medium | favorite clear but one key uncertainty exists |
| Low | signals conflict, key lineups unknown, or team styles create high variance |

Separate confidence in result from confidence in exact score. Exact score is usually lower confidence.

For knockout matches, separate confidence in regulation result from confidence in advancement. Penalty-shootout outcomes are usually low-confidence unless there is strong goalkeeper, taker, or fatigue evidence.

Use numeric probabilities only when the evidence and calculation support them. Otherwise use the labels above and do not imply quantitative calibration.

## Standard Answer Template

```markdown
| Match | Evidence cutoff | Sources used | Market | Data/personnel correction | Prediction | Result / score confidence |
|---|---|---|---|---|---|---|
| A vs B | 12:00 UTC; lineups pending | Market, news, matchup | A small favorite | B has strong low block; A missing creator | A 1-0 | Medium / Low |

**A vs B**
Evidence snapshot: exact fixture and kickoff; information cutoff; named market page and market type; team news report; style-matchup notes. Data layer unavailable.
Calibration: Prior review showed overcorrecting to draws is risky, but this remains provisional because final lineups are unavailable.
Prediction: A 1-0; backup 1-1.
Confidence: result medium; exact score low; if applicable, advancement medium.
Knockout note: if applicable, 90-minute score; advancement lean and confidence; extra-time or penalty-shootout risk.
Cards note: if requested and referee data is sufficient, main card count; reasonable range; red-card trigger. Otherwise, qualitative discipline risk and missing data.
Why: [market], [data], [availability], [style matchup].
Failure mode: A cannot turn possession into box chances, or B scores first from transition/set piece.
Missing data: Sofascore unavailable / lineup not confirmed / weather not checked.
Disclaimer: Informational football analysis only; not betting or financial advice.
```

## Post-Match Review Template

```markdown
| Match | Prediction | Result | Verdict |
|---|---:|---:|---|

What was right:
- ...

What was wrong:
- ...

Verdict category:
- Result and process both right / result right but process partly wrong / result wrong but process defensible.

Model update:
- Increase/decrease weight for ...
- Note whether this was a paper-strength error, over-draw-protection error, lineup/fitness miss, market miss, or finishing-variance miss.

Calibration record: match; forecast timestamp; 90-minute lean; regulation exact-score verdict; final/advancement verdict; decision-stage verdict; result/exact-score confidence; market baseline; source completeness; process verdict; error category. Add 1X2 probabilities and Brier score only if probabilities were explicitly forecast.
```

Review against process and chance quality, not only score. If a prediction loses to an extreme goalkeeper performance or red card, record it differently from a wrong style-matchup read.
