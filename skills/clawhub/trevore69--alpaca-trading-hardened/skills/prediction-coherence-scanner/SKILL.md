---
name: prediction-coherence-scanner
description: Scan mutually exclusive outcome groups for price coherence gaps, with completeness gates that reject the phantom arbitrage caused by missing legs.
license: MIT
compatibility: Requires Python 3.9+, the simmer-sdk package, and network access to the Simmer API.
metadata:
  author: "Clawedassistant"
  version: "1.0.0"
  displayName: "Coherence Scanner"
  difficulty: "intermediate"
---

# Coherence Scanner

Identify outcome groups whose prices are internally inconsistent. In a set of
outcomes where exactly one can be true, the YES prices must sum to 1.00. When
they sum to less than that net of costs, buying every leg pays 1.00 for less
than 1.00. No forecast is involved, which is the appeal, and also why the
opportunity is rare.

> 🚨 **Framework, not a production trading system.** Read [DISCLAIMER.md](DISCLAIMER.md)
> before connecting a wallet with real funds. Defaults: $10 max per set, 5 sets
> per run, dry-run unless `--live`, paper `sim` venue unless you change it.

> **This is a template.** The default signal is price coherence within an event
> group. The skill handles the plumbing: grouping, completeness proof, cost
> accounting, and execution safety. Swap in your own quote feed or grouping
> source. Your agent provides the alpha.

## The thing this skill is actually for

Most of this code says no. That is the point.

The naive version of this strategy is four lines: group markets by event, sum
the prices, buy everything when the sum is under 1.00. That version loses money,
and it loses it in a specific and avoidable way.

While building this, a live scan returned 27 legs of the 2028 Democratic nominee
event summing to **0.308**. Read naively, that is a 69% risk-free return.
Re-querying the same event properly returned the **full 37 legs summing to
1.0015**. The missing 10 legs held the other 0.69. There was no edge. Acting on
the first view would have bought an incomplete book and held a plain directional
bet while believing it was hedged.

That produces the rule at the centre of this skill, and it is backwards from
intuition:

> **The larger the apparent edge, the more likely your data is broken.**

A real coherence gap in a liquid market is worth one or two percent. A 69% one
means you are missing legs. So the scanner refuses any group whose prices sum
below 0.90, and calls it "suspected missing legs" rather than a trade. It gives
up hypothetical deep arbitrage on purpose, because every deep candidate observed
in live data was an artifact.

## Gates

Each gate exists because of a measurement in [references/METHOD.md](references/METHOD.md).
Order matters: completeness is proven before any edge is believed.

| Gate | Rejects |
| --- | --- |
| Structural partition proof | Groups with no venue-level guarantee of exclusivity |
| Truncated window | Any capped result set, which silently drops legs |
| Completeness floor | Sums below 0.90, treated as missing legs, not profit |
| Exclusivity ceiling | Sums above 1.25, meaning legs can all be true at once |
| Executable quotes | Groups missing a real ask on any leg |
| Quote freshness | Quotes older than 120 seconds |
| Cost survival | Edges that vanish once asks and fees are paid |

Two findings drive most abstentions:

- **`event_id` does not mean mutually exclusive.** The "Spain vs. Argentina,
  More Markets" event bundles 23 unrelated props (over/unders, spreads, both
  teams to score) and sums to 5.44. Those can all be true at once. Exclusivity
  must come from structure, such as Polymarket's negative-risk flag, never from
  the price sum. Using the sum to decide a group is a partition and then trading
  that same sum is circular reasoning, and it is how a broken group gets traded.
- **Midpoints are not tradeable.** Of 698 markets pooled from the list endpoint,
  zero carried an executable ask. You buy at the ask, so a group whose midpoints
  sum to 0.995 often costs more than 1.00 to actually buy. The scanner abstains
  rather than substituting a midpoint, because doing so understates cost and
  produces precisely the trades you do not want.

## Honest expectations

**Expect this skill to abstain, nearly always.** Every leg set that could be
proven complete was efficiently priced, between 0.9950 and 1.0195. On the data
measured on 17/07/2026 it found no executable edge, because the quote depth
needed to confirm one is not exposed by this API surface.

That is a real result, not a failure to try. A scanner that accurately reports
"there is nothing here" is worth more than one that hallucinates edge from
truncated data. If this fires constantly, suspect the completeness gate before
celebrating.

## Setup

```bash
python3 -m venv .venv
.venv/bin/pip install simmer-sdk
export SIMMER_API_KEY="your-key"   # from simmer.markets/dashboard
```

A venv is the reliable path. Many hosts ship Python without `pip` on PATH, and
Debian-based ones refuse system-wide installs anyway. Run the scanner with
`.venv/bin/python` so it sees the SDK.

If you already keep the key in `~/.simmer/credentials.json`, export it from
there rather than pasting it:

```bash
export SIMMER_API_KEY=$(python3 -c "import json,os;print(json.load(open(os.path.expanduser('~/.simmer/credentials.json')))['api_key'])")
```

## Use

```bash
# Dry run against paper markets. Always start here.
python3 coherence_scanner.py --query "Golden Boot"

# Show why each group was rejected. This is the useful mode.
python3 coherence_scanner.py --query "Exact Score" --show-abstains

# Machine readable
python3 coherence_scanner.py --query "World Cup" --json

# Real orders. Only after you have wired in a quote feed and read DISCLAIMER.md.
python3 coherence_scanner.py --query "Golden Boot" --venue polymarket --live
```

`--query` is mandatory. Unfiltered discovery is capped at 1,000 markets and
silently drops legs, which is the exact input that manufactures fake edge.
Filters are applied server side before that cap, so they reach the whole
catalogue.

Check what the skill has done, without placing orders:

```bash
python3 scripts/status.py
```

## Tests

```bash
python3 tests/test_coherence.py
```

Twenty two gate tests, built from real market fixtures including the 27-leg
phantom arbitrage. No network or API key needed.

## Remixing

The plumbing is structural. The swappable parts:

- **`executable_price(leg)`** is the highest-value change. Wire in a real order
  book (Polymarket CLOB, Kalshi orderbook) with depth. Until you do, the cost
  gate cannot confirm an edge and the scanner will abstain. This is the main
  blocker between this skill and a live edge.
- **`detect_partition_family(legs)`** is where you prove exclusivity. Add your
  own families, ideally from authoritative venue event membership rather than
  name matching.
- **`MIN_PLAUSIBLE_SUM`** is the completeness floor. Loosening it toward 0
  re-enables the phantom arbitrage this skill exists to prevent. Do not, unless
  you have proven completeness some other way.
- **Sizing.** The current split is naive and equal across legs. Real dutch book
  sizing should weight by price and available depth.

## Limits

- Buy-side only. The over-round case (sum above 1.00, sell every leg) needs
  short access or NO legs and is not implemented.
- Partial fills break the guarantee. Owning 8 of 10 legs is an unhedged bet you
  did not intend. Execution stops on the first failed leg and reports exposure
  rather than building a broken book.
- No latency edge. Coherence gaps in liquid books close fast, so a periodic scan
  mostly finds gaps that are already gone.
