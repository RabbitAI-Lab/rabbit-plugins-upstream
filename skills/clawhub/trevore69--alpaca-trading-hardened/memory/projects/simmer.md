# Project: Simmer (paper trading)

**Status:** Active, claimed. Paper trading only — no real money at stake.
`real_trading_enabled: true` is set on the account, but `wallet_address`,
`deposit_wallet_address` and `per_agent_wallet_address` are all null, and
`polymarket_pnl`/`kalshi_pnl` are null: there is no funded wallet for it to draw
on, and `sim_pnl == total_pnl`. Trevor confirmed paper 17/07/2026. Note the flag
would become live if a wallet is ever attached, so never gate trading code on it.
**Credentials:** `~/.simmer/credentials.json` (agent_id df7e3358-…, apiKey sk_live_…, claim code spark-I1QE)
**API:** base `https://www.simmer.markets/api/sdk/`, Bearer auth. Verified paths in workspace TOOLS.md.

## Timeline
- 2026-07-14 13:06 UTC — Trevor asked agent to sign up and "start playing" with the $10,000 SIM paper account; later gave free rein ("go mad") and permission to find a "cheat".
- 2026-07-14 13:06–14:17 — 44 real paper trades placed. Early: Spain semifinal YES $50, Fed no-change YES, BNB NO. Main play: World Cup winner **Dutch book** — NO on Norway (already eliminated), France, Spain, Argentina, England.
- 2026-07-15 AM — two sessions wrongly declared the account nonexistent after probing `/api/agents/status` (wrong path; correct is `/api/sdk/agents/me`). MEMORY.md briefly mis-labeled the real snapshot "fabricated"; corrected same day.
- 2026-07-15 18:35 UTC — verified live: balance $7,440.54, realized PnL **-$505.03 (-5.05%)**, 44 trades, 1W/9L resolved.
- 2026-07-16 08:04–08:11 UTC — topped up decided-outcome positions (Muchova/Noskova, Borges/Dimitrov, Roh/Borisiouk sets) and added set-handicap NO on Roh -1.5. Account flipped strongly positive.

## Snapshot (17/07/2026 05:52 UTC)
- Balance: $5,383.07 cash. Positions value: ~$6,419. Total ~$11,802 on $10,000 start.
- Total PnL: **+$1,802.14 (+18.02%)**. Realized: +$383.41; unrealized: +$1,418.75.
- Trades: 60 total; 7 wins / 9 losses resolved (43.8% win rate).
- 10 active positions (3 new $10 learning trades placed 17/07):
  - Wimbledon WTA Muchova vs Noskova NO — cost $1,750, value $3,206 (+$1,456). Noskova won; market still resolving.
  - Swedish Open Borges vs Dimitrov YES — cost $1,880, value $2,149 (+$269). Borges won 6-4 6-2; resolves 22/07.
  - Set Handicap Roh (-1.5) vs Borisiouk (+1.5) NO — cost $510, value $520 (+$10).
  - Argentina WC NO — cost $410, value $274 (-$136).
  - Spain WC NO — cost $410, value $238 (-$172).
  - Fed no-change YES — cost $21, value $24 (+$3).
  - Fed hike-0bps NO — cost $20, value $6 (-$14).
  - **NEW:** France vs. England: Team to Win YES — $10 cost, 15.95 shares.
  - **NEW:** Will France win on 2026-07-18? NO — $10 cost, 19.86 shares.
  - **NEW:** ETH price Jan 1, 2027 — 1,500 to 1,749.99? NO — $10 cost, 10.29 shares.

## Automation
- Simmer heartbeat script: `scripts/simmer-heartbeat.py` runs every **6 hours** via cron.
- Logs portfolio, expiring positions, and top-volume markets to `logs/simmer-heartbeat.log`.
- Added 17/07/2026: `scan_stale_priced()` flags stale-priced candidates to the
  same log. **Log-only, places no trades.** Derives side from
  `external_price_yes`, deliberately ignoring the endpoint's broken
  `recommended_side`/`opportunity_score` (see warning above).
- Bugs fixed 17/07/2026: creds path was hardcoded to `/root/.simmer/` and now
  falls back across known locations; "expiring today" filter had the date
  hardcoded as `2026-07-17` and would have silently reported 0 forever after;
  `log()` printed and file-appended, so cron's stdout redirect doubled every
  line (the 06:00 block in the log is that bug, not two runs).

## ⚠️ /markets/opportunities is not trustworthy (verified 17/07/2026)
Do not wire auto-trading to this endpoint's own fields:
- `opportunity_score` was the constant **50.0 on every row**. It ranks nothing.
- `divergence` does not reconcile with the adjacent price fields. Starmer showed
  `current_probability == external_price_yes == 0.9920` exactly while claiming
  `divergence: -0.167`.
- `recommended_side` was **inverted on both markets with a known real-world
  outcome**: it said `yes` on Muchova/Noskova (Noskova had already won; we hold
  NO, +$1,456) and `no` on Borges/Dimitrov (Borges had already won 6-4 6-2; we
  hold YES, +$269). Following it would have traded straight into our two best
  positions.

**What IS usable from it:** `external_price_yes` (Polymarket's price). The
stale-decided-event edge = external at an extreme (<=0.02 or >=0.98) while the
Simmer price is still mid-range. Trade toward the external price. Muchova is the
worked example: external 0.0005 vs Simmer 0.3575 -> NO was correct.

**Base rate is low.** On 17/07 at 08:46, 7 of 10 opportunity rows had
`current_probability == external_price_yes` to 4dp (no edge at all), and all 3
that diverged were already held. Scanner correctly returned **0 candidates**.
Zero is the normal, correct output most of the time — the edge is real but rare.
An auto-trader that must trade would manufacture the crypto-coinflip losses.

## Loopholes / observations to explore
1. **Related-market arbitrage:** World Cup winner, exact-score, team-to-advance, and match-winner markets form a lattice. If implied probabilities are inconsistent, there are risk-free or positive-EV combinations.
2. **Decided-event stale pricing:** Markets that resolve before the platform marks them resolved can be bought at mispriced odds (the original edge that produced most PnL).
3. **AMM liquidity variance:** Small trades in thin buckets can move prices dramatically — useful for learning, dangerous for size.

## Lessons
- Resolved trades went 1W/9L — the crypto fast-market coin flips bled money. The edge plays (stale decided-event markets) are the ones working.
- Follow-up result checks were set as session reminders and got lost; use durable OpenClaw cron for anything that must survive sessions.
- Real-money venues (Polymarket/Kalshi) still require explicit Trevor approval per MEMORY.md.
