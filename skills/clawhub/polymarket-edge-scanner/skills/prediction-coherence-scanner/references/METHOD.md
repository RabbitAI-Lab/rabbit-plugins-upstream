# Method and measurements

Every gate in `coherence_scanner.py` exists because of a specific measurement.
This file records those measurements so you can re-check them rather than trust
them. All figures were taken from the live Simmer SDK API on 17/07/2026 across
698 pooled unique markets.

## The relationship being traded

In a set of outcomes that is mutually exclusive (at most one is true) and
exhaustive (at least one is true), exactly one leg resolves YES and pays 1.00.
The executable YES prices must therefore sum to 1.00. If you can buy every leg
for a total of 0.96, you are paying 0.96 for a certain 1.00.

This needs no forecast. You are not claiming to know who wins. That is the
appeal, and it is also why the strategy is crowded and rarely available.

## Finding 1: event_id does not mean mutually exclusive

Markets carry an `event_id`. It is a grouping hint, not a guarantee.

| Event | Legs | Midpoint sum |
| --- | --- | --- |
| Spain vs. Argentina, More Markets | 23 | 5.4410 |
| France vs. England, More Markets | 21 | 7.4240 |
| Spain vs. Argentina, Exact Score | 17 | 1.0195 |

"More Markets" bundles over/unders, spreads and both-teams-to-score under one
event id. Those legs can all be true at once. A sum of 5.44 is meaningless, not
a signal. "Exact Score" enumerates disjoint scorelines and sums to about 1.00.

Consequence: the scanner requires structural evidence of exclusivity
(`polymarket_neg_risk` on every leg, or a recognised partition family) before it
trusts any arithmetic. `detect_partition_family` explicitly rejects
"More Markets".

## Finding 2: incomplete leg sets manufacture fake arbitrage

This is the finding that shapes the whole skill.

Scanning a capped discovery window returned 27 legs of the 2028 Democratic
nominee event, summing to **0.308**. Read naively that is a 69 percent risk-free
return: buy all 27 legs for 0.31, collect 1.00.

It is not. Re-querying that single event with a filtered search returned the
**full 37 legs, summing to 1.0015**. The missing 10 legs held the other 0.69.
There was never any edge. A scanner that acted on the 27-leg view would have
bought an incomplete book and held an ordinary directional bet while believing
it was hedged.

The same pattern appeared elsewhere:

| Event | Legs seen | Sum | Reality |
| --- | --- | --- | --- |
| Democratic Presidential Nominee 2028 | 27 | 0.3080 | truncated, full set is 37 legs at 1.0015 |
| Republican Presidential Nominee 2028 | 5 | 0.0310 | truncated, most legs absent |

**The rule this produces is counterintuitive: the larger the apparent edge, the
more likely the data is broken.** A real dutch book in a liquid market is worth
one or two percent. A 69 percent one means you are missing legs.

Hence `MIN_PLAUSIBLE_SUM = 0.90`. A midpoint sum below 0.90 triggers abstention
with "suspected missing legs" rather than a trade. This deliberately gives up any
genuine deep arbitrage, because in live data every deep candidate was an
artifact, and being wrong here costs the whole position.

Related gates: any response with `truncated` or `capped_at_limit` set forces
abstention, and `fetch_event_legs` refuses to run unfiltered queries, because
filters are applied server side before the 1,000 market cap and so reach the
whole catalogue.

## Finding 3: complete partitions are efficiently priced

Every leg set that could be proven complete sat within 0.5 to 2 percent of 1.00:

| Event | Legs | Midpoint sum | Overround |
| --- | --- | --- | --- |
| Democratic nominee 2028 (full) | 37 | 1.0015 | +0.15% |
| France vs. England, Exact Score | 17 | 0.9950 | -0.50% |
| World Cup Golden Boot Winner | 10 | 0.9955 | -0.45% |
| World Cup Golden Ball Winner | 8 | 1.0080 | +0.80% |
| Elon Musk tweet count bucket | 5 | 1.0070 | +0.70% |
| Spain vs. Argentina, Exact Score | 17 | 1.0195 | +1.95% |

Two of these sit slightly below 1.00 at the midpoint. That is not free money
either, because midpoints are not executable (Finding 4).

Expect this skill to abstain almost always. That is the honest result, not a
bug. If it fires constantly, suspect the completeness gate before celebrating.

## Finding 4: midpoints are not tradeable, and asks are often absent

Of 698 pooled markets, **0 carried `best_ask`** on the list endpoint. Both
venues returned midpoint pricing only.

| Source | Markets | With best_ask |
| --- | --- | --- |
| polymarket | 496 | 0 |
| kalshi | 202 | 0 |

The per-market `/context` endpoint returned `slippage: None` and `spread: None`
for the market checked, so depth was not recoverable there either.

You buy at the ask, not the midpoint. A group whose midpoints sum to 0.995 will
routinely cost more than 1.00 to actually buy once spread is crossed, which
turns a "0.5 percent edge" into a loss. Substituting a midpoint where an ask is
missing systematically understates cost and produces exactly the trades you do
not want.

Hence `executable_price` returns None when there is no ask, and the scanner
abstains rather than guessing. In practice this means the strategy is not
executable on the list endpoint alone. You need a venue quote feed
(Polymarket CLOB books, Kalshi orderbook) wired into `executable_price` before
this trades anything real. That is the main remix point.

## Finding 5: the edge endpoint echoes your own input

Calling `/context` with `my_probability=0.2` on a market priced at 0.001
returned `user_edge: 0.199`, `recommended_side: "yes"`, `recommendation: "TRADE"`.

That is arithmetic on the number you supplied, not independent validation. It
will endorse any probability you invent. Do not read it as confirmation. This
skill does not use it as a signal.

## Execution risk: partial fills break the guarantee

The arbitrage exists only if you own every leg. Owning 8 legs of a 10 leg book is
an unhedged directional bet that you did not intend to place. `execute` stops on
the first failed leg and reports open exposure rather than continuing to build a
broken book. Legs are bought with limit orders at the quoted ask, because a
market order can slip past the point where the edge existed.

## What would make this profitable

Honestly, on the data measured, nothing in this file constitutes a live edge.
The plumbing is sound and the gates are correct, but the executable quote data
needed to confirm an edge was not available through this API surface. To get
there you would need, in rough order of importance:

1. A real order book feed per leg, including depth, so cost is known before
   committing rather than assumed.
2. Authoritative event membership from the venue (the neg-risk event id or the
   Kalshi event ticker) so completeness is proven rather than inferred from a
   price sum.
3. Latency good enough to matter. Coherence gaps in liquid books are closed by
   faster participants, so a 15 minute cron will mostly find gaps that are
   already gone.

Points 1 and 2 are the honest blockers. Until they are solved this skill is a
correct scanner that will tell you, accurately, that there is nothing to do.
