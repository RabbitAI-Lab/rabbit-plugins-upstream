---
name: salary-negotiator
description: "Prepare salary negotiations with a structured toolkit: market-rate anchoring math, walk-away floor calculation, total-compensation evaluation (equity, bonuses, benefits), negotiation scripts for offers, raises, and counter-offers, and BATNA analysis. Use when the user has a job offer, is preparing a raise conversation, wants to know if their pay is competitive, or needs scripts and a strategy for negotiating compensation."
version: 1.0.0
author: Denis Voronin
license: MIT
tags: [career, salary, negotiation, compensation, job-offers, raises]
---

# Salary Negotiator

The 10 minutes of a compensation conversation move more money per minute than anything else in a career — yet most people walk in unprepared, accept the first number, and leave 10-30% on the table. This skill does the preparation: market anchoring, walk-away math, total-comp evaluation (equity! bonuses! benefits!), and the actual scripts to say.

## Overview

`scripts/salary_negotiator.py` runs the numbers that matter before any negotiation:

- **Market anchor builder** — turn salary-band data (levels.fyi / Glassdoor / recruiter info) into a defensible anchor: target, acceptable, and stretch numbers with rationale you can say out loud
- **Walk-away floor calculator** — personal financial floor (monthly costs × runway, debt, savings goals) → the number below which the offer is a no regardless of charm
- **Total compensation evaluator** — normalize offers with different shapes: base + bonus % + RSUs + options + 401k match + sign-on into an **annualized expected value** with risk weighting (startup options are lottery tickets; price them like one)
- **Raise conversation planner** — build the case from impact bullets, market deltas, and commitment signaling; includes the "no budget" counter-moves
- **BATNA analyzer** — best-alternative analysis: what you do if this fails, and how strong that makes your position
- **Script generator** — annotated negotiation scripts: acknowledging-then-countering, anchoring, silence technique, and the graceful multi-round dance

Everything runs offline with explicit assumptions; the user brings market data (the tool tells them exactly which sources to check).

## When to Use

- A job offer arrived (or is coming) and the user wants to negotiate it
- Preparing an annual review / raise ask
- "Am I underpaid?" — evaluating current comp against market data
- Comparing two offers with different structures (big-base vs equity-heavy)
- Deciding whether to counter, and by how much

**Don't use for:** contract/freelance rate-setting (that's `freelance-rate-calculator` territory), executive-level comp with accelerators/cliffs beyond RSU basics, or legal review of equity agreements (recommend an employment attorney for non-competes and option terms).

## How It Works

1. **Inputs:** current comp (or none), offer details, market data points (min/median/max for the role+level+location), personal floor inputs (monthly costs, runway needs).
2. **Anchor math**: target = market median × experience factor (if you have leverage evidence, above-median; if career-switcher, at-median). Stretch = market p75-p90. Floor = personal financial floor, never below.
3. **Total comp EV**: base + (bonus % × base × probability-of-payout) + RSU annualized value × vesting-risk factor + options × (strike-adjusted probability-weighted value) + benefits delta (401k match is cash; insurance differences priced roughly).
4. **Scripts**: pick the scenario (new offer, counter round 2, raise ask) and the tone (collaborative/firm); generate the script with fill-in numbers from the computed anchor.
5. **Practice Q&A**: likely pushbacks ("budget is fixed", "this is our standard band") and the counters.

## Quick Start

```bash
# Build the negotiation strategy for an offer
python3 scripts/salary_negotiator.py offer \
  --role "Senior Backend Engineer" --location "Remote US" \
  --offer-base 145000 --offer-bonus 10 --offer-signon 15000 \
  --offer-rsu-annual 40000 --market-min 130000 --market-med 160000 --market-max 210000

# What's my walk-away number?
python3 scripts/salary_negotiator.py floor --monthly-costs 4200 --runway-months 6 \
  --other-income 0 --benefit-gap 500

# Compare two differently-shaped offers
python3 scripts/salary_negotiator.py compare \
  --a "BigCo: base 150k, bonus 15%, RSU 60k/yr, 401k match 4%" \
  --b "Startup: base 130k, options 0.5%, strike 1.50, valuation 60M"

# Script for the raise conversation
python3 scripts/salary_negotiator.py raise --current 120000 --market-med 145000 \
  --impact "led payments migration, -38% infra cost" --ask 138000

# Full walkthrough
python3 scripts/salary_negotiator.py demo
```

## Steps (Agent Workflow)

1. Gather: role, level, location, offer components, market data (point the user to levels.fyi / Glassdoor / LinkedIn / recruiters — insist on ≥3 sources), and their financial floor.
2. Run `floor` first — knowing the walk-away changes everything downstream.
3. Run `offer` (or `compare` if multiple offers) to get anchor numbers and total-comp EV.
4. Generate the script (`offer` includes it; `raise` for internal conversations).
5. Rehearse the pushback Q&A with the user — have them say the counter number OUT LOUD.
6. Remind: get it in writing; never resign on a verbal; silence after their number is a tool, not rudeness.

## Output Shape

```
NEGOTIATION STRATEGY — Senior Backend Engineer (Remote US)
═════════════════════════════════════════════════════════
MARKET ANCHOR
  Market: $130k — $160k — $210k (min/med/max)
  Your target: $172,000  (median +7%: strong skills evidence, competitive offer)
  Your stretch: $189,000  (p75; justifiable with the RSU haircut argument)
  Your floor:  $151,000  (personal financial floor — see floor calc)

OFFER EVALUATION
  Base $145,000 + bonus 10% ($14,500 × 85% payout = $12,325)
  + sign-on $15,000 /3yr = $5,000 + RSU $40,000 × 90% retention = $36,000
  TOTAL COMP EV: $198,325/yr   vs your target $172k → offer is ABOVE target
  Base alone: $145k is 9% below market median — negotiate BASE, not RSUs.

SCRIPT (collaborative-firm, round 1)
  "Thank you — I'm genuinely excited about this role and the team.
   [pause] Based on my research for this scope in [location], market
   medians run around $160k base, and given [specific qualification],
   I was targeting $172k. Is there flexibility to get closer to that?"
  ▸ If "band is fixed": pivot to sign-on/RSU/equity refresh/PTO — see Q&A sheet.
```

## Common Pitfalls

1. **Negotiating total comp when cash is the constraint.** RSUs and bonuses are risk-weighted; base is (nearly) certain. If the base is 15% below market, a bigger option pool does not fix it — evaluate EV, then negotiate the *component* that's mispriced.
2. **Anchoring with a range.** "I'm looking for 150-170" → they hear 150. Always one number, always your target, always with rationale.
3. **Not having a floor.** Without a walk-away number, "no" sounds like an argument; with one, it's a fact. Compute it before anything else.
4. **Accepting on the call.** Enthusiasm is fine; commitment is premature. "I'd like 48 hours to review the full package" is standard and loses nothing.
5. **Countering the day the offer arrives without reading the shape.** A weak base with a giant sign-on may beat a strong base after year 1 — do the multi-year math (`compare` does 1/2/3-year views).
6. **Negotiating against yourself.** State the number. Then stop talking. The next person to speak loses money — make sure it's them.
7. **Ignoring the "no budget" counters.** There are always other levers: sign-on, equity refresh, start-date bonus, PTO, remote stipend, title, review-in-6-months-with-criteria. The Q&A sheet enumerates them.

## Verification Checklist

- [ ] Market data from ≥3 sources, role+level+location matched
- [ ] Personal floor computed BEFORE strategy
- [ ] Total comp evaluated as EV, with risk weighting on variable components
- [ ] One target number chosen (never a range)
- [ ] Script rehearsed out loud, including the number
- [ ] Pushback Q&A reviewed
- [ ] All agreements to be confirmed in writing

## One-Shot Recipes

**"They offered 115k, recruiter says band tops at 125k, I wanted 130k"**
```bash
python3 scripts/salary_negotiator.py offer --role "PM" --offer-base 115000 \
  --market-min 105000 --market-med 125000 --market-max 140000
# → anchor at 128-130 with rationale script; levers if base is truly capped
```

**"Raise review in 2 weeks; I make 95k, market is 115k, I shipped X and Y"**
```bash
python3 scripts/salary_negotiator.py raise --current 95000 --market-med 115000 \
  --impact "shipped X (+12% activation), led Y migration" --ask 108000
# → script + the 'budget lands next cycle' counters (criteria + date in writing)
```

## References

- [`references/comp-structures.md`](references/comp-structures.md) — equity types, vesting, bonus shapes, benefit valuation
- [`references/scripts.md`](references/scripts.md) — full script library: offers, counters, raises, rescission-safe exits
