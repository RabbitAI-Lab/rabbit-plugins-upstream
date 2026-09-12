---
name: commute-time-optimizer
description: "Use when comparing where to live based on commute, evaluating a hybrid work schedule, deciding if a new job's longer commute is worth it, calculating the true annual cost of driving to work, or planning which weekdays to go into the office — computes rush-hour travel times by weekday, prices every commute mode (car, transit, bike, walk, WFH) in hours and dollars, optimizes hybrid office-day schedules to minimize time in traffic, and shows the lifespan/multi-year cost of location choices."
version: 1.0.0
author: Denis Voronin
license: MIT
tags: [commute, relocation, hybrid-work, time-value, cost-of-driving, housing]
---

# Commute Time Optimizer

## Overview

The average one-way commute in the US is ~27 minutes — about 250 hours a year per worker, or six working weeks spent in a car or train. Yet people weigh a $200/month rent difference carefully while treating a "10 extra minutes each way" as trivia. Ten minutes each way is 83 hours a year — two full work weeks — plus fuel, depreciation, and crash-risk exposure. Housing and job decisions systematically misprice commute time because the cost is paid in small daily installments.

This skill makes the full cost visible and comparable. Feed it route facts you already know (off-peak time, typical rush multiplier, distance, mode options) and it produces:

- **Rush-hour times per weekday** — Monday is not Friday; traffic peaks mid-week.
- **True cost per mode** — hours/year, $/year at your hourly rate, vehicle costs (IRS-style per-mile), transit fares, and the WFH baseline.
- **Hybrid schedule optimization** — for N required office days, which weekdays minimize time in traffic, with the penalty vs. the theoretical best picked explicitly.
- **Relocation/job comparisons** — home A vs. home B vs. job C, multi-year totals, and the "commune-time equivalent rent" — how much more rent is justified by a shorter commute.
- **Lifespan math** — what 10 years of each option costs in hours (life expectancy terms: 500 hours = 31 waking days) and dollars.

Numbers default to US DOT/FHWA and AAA-style averages and are all editable.

## When to Use

- Comparing two apartments/homes or two job offers with different commutes
- Deciding which days to go into the office on a hybrid schedule
- "Is moving closer to work worth the higher rent?"
- "What does my commute actually cost me per year?"
- Evaluating transit vs. driving vs. cycling for a specific route
- Don't use for: one-off trip routing (use a maps tool), freight/logistics, or precise real-time traffic prediction — this is a decision-support model built from your observed typical times.

## Inputs You Provide

| Input | Default | Where to get it |
|---|---|---|
| off-peak one-way minutes | required | maps tool at 10am on Sunday |
| rush multiplier (peak/off-peak) | 1.4 car, 1.1 transit | your own observed typical times |
| distance miles | required | maps |
| days/week commuting | 5 | your schedule |
| annual weeks | 48 (4 wks PTO+hol) | |
| your hourly rate ($, after-tax) | 30 | salary ÷ 2080 |
| mode params | IRS-style defaults | `params` command |

## Commands

```bash
# Editable assumptions (AAA-style vehicle cost, transit fare, bike speed...)
python3 scripts/commute_opt.py params

# Weekday rush profile for one route (Mon-vs-Fri traffic differs)
python3 scripts/commute_opt.py profile --offpeak 25 --mode car

# Full cost of one commute setup
python3 scripts/commute_opt.py cost --offpeak 25 --distance 15 --mode car \
    --rate 35 --days 5

# Compare modes for the same route
python3 scripts/commute_opt.py compare --offpeak 25 --distance 15 --rate 35

# Hybrid: which 3 office days minimize traffic? (5 = all weekdays)
python3 scripts/commute_opt.py hybrid --offpeak 30 --mode car --office-days 3

# Relocation decision: two homes vs. one job (or more)
python3 scripts/commute_opt.py decide \
    --option "Apartment A,offpeak=25,distance=12,mode=car,extra_rent=0" \
    --option "House B,offpeak=42,distance=26,mode=car,extra_rent=-450" \
    --option "Condo C + transit,offpeak=40,distance=18,mode=transit,extra_rent=-200" \
    --rate 40 --years 5

# Everything as JSON for further analysis
python3 scripts/commute_opt.py cost --offpeak 25 --distance 15 --json
```

## How It Works

**Weekday profile.** Peak congestion is mid-week: multipliers `Mon 1.28, Tue 1.38, Wed 1.42, Thu 1.36, Fri 1.22` (FHWA-style patterns; commute peak 7–9am/4–6pm). Rush time = off-peak × weekday multiplier × mode rush factor (car 1.0 relative, transit 1.1 on its own scale, bike/walk unaffected).

**Mode costs.** Per round trip:
```
car:     miles × 2 × ($0.30 fuel+maint + $0.37 depreciation+ownership amortized)   [AAA/IRS-style, editable]
transit: fare × 2  (monthly-pass logic in references)
bike:    $0.08/mile
walk:    $0
WFH:     $0, 0 min
```
Time is priced at your after-tax hourly rate — the honest way to value unpaid commute time (WFH Research findings: workers value commuting time lost at ~full wage).

**Annualization.** `trips/year = days × weeks; hours = minutes × 2 × trips / 60`.

**Hybrid optimizer.** Brute-force all C(5, N) weekday subsets, sum rush-time across chosen days, pick min; report penalty vs. best-possible and vs. Mon–Fri.

**Equivalent rent.** For the `decide` command: `Δ$ = (time$ + direct$) difference vs. baseline option`, then `breakeven_rent = −Δ$/12` — how much extra monthly rent the faster commute justifies.

**Lifespan framing.** Hours/decade converted to waking days (16h/day) — the number that actually changes housing decisions.

## Reading the Output

```
=== 5-YEAR DECISION ===
Option                       hrs/yr   $/yr(time)  $/yr(total)  5-yr total   vs. best
Apartment A (car, 12mi)       96.7      3,481       5,611       28,055    baseline
House B (car, 26mi)          162.3      6,487      11,082       55,412   +27,357
Condo C (transit, 18mi)      154.0      6,163       8,063       40,317   +12,262
House B pays −$450/mo rent … net: A wins unless rent gap > $456/mo
```

## Common Pitfalls

1. **Valuing commute time at $0.** Unpaid time is still your life; WFH-research valuation ≈ full after-tax wage. Set `--rate 0` only for genuinely neutral time (napping on a train you'd take anyway).
2. **Using map ETA as the commute.** Map ETAs are often off-peak or smoothed. Enter your *observed* typical door-to-door time; the tool applies weekday multipliers.
3. **Forgetting both directions.** All outputs are round-trip. Don't double-count manually.
4. **Ignoring hybrid-day choice.** Mon/Wed/Fri office weeks pay a Wednesday penalty; with the default profile Mon/Thu/Fri is fastest for car commuters and Tue/Wed/Thu (stacking all three peaks) is the worst choice.
5. **Amortized car costs feel "sunk."** Depreciation and maintenance scale with miles even on a car you own anyway; the per-mile model is the standard honest approximation.
6. **Comparing rent gaps without annualization.** Always run `decide` over your realistic tenure (3–7 years), not 1 year.

## Verification Checklist

- [ ] Off-peak time is your observed time, not map-estimated
- [ ] Hourly rate is after-tax (salary ÷ 2080 × 0.75 approx)
- [ ] Compared options use identical days/week and weeks/year
- [ ] For hybrid: confirmed which days the office actually requires vs. allows
- [ ] `decide` includes the rent/housing gap for each option
