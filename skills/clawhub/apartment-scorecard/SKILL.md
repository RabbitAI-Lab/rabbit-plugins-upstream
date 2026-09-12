---
name: apartment-scorecard
description: "Use when comparing apartments or rental homes and torn between options, when deciding if a listing is actually affordable, when touring rentals and needing to score them consistently instead of by vibes, when the advertised rent hides fees/parking/pet rent/utilities/commute, when preparing to negotiate rent or lease terms, or when defining what you actually need (bedrooms, pets, commute ceiling) before searching — applies hard constraints first (budget, commute, bedrooms, pets, move date) to kill unqualified listings, scores survivors on 16 weighted criteria YOU prioritize, computes the true all-in monthly cost with every fee amortized, runs affordability analysis (30/33/50% rules, 3x-income approval math), compares finalists side-by-side with the quality-vs-cost premium quantified, and generates a leverage-based negotiation script with anchoring targets."
version: 1.0.0
author: Denis Voronin
license: MIT
tags: [apartment, rental, housing, moving, comparison, budgeting, negotiation, decision-making]
---

# Apartment Scorecard — Compare Rentals Like an Analyst

## Overview

Apartment hunting corrupts judgment: you tour five places in a day, the one with the nice lobby light wins, and six months later you're paying $120/month in "amenity fees" for a gym you never use with a 50-minute commute you didn't count. The listing price is marketing; your actual cost and quality are computable.

This skill enforces the process your rational self would use: **hard constraints first** (no point scoring a place you can't afford, can't bring the cat to, or can't move into on time), then **weighted scoring on 16 criteria** with weights that reflect YOUR priorities (a remote worker weights light and noise; a commuter weights transit), then **true monthly cost** — every fee, amortized broker fee, parking, pet rent, utilities, insurance, deposit interest, and optionally your commute time valued in money — and finally **negotiation prep**: the market signals that justify asking for less, with anchoring numbers and a script.

## When to Use

- Comparing 2+ listings you've toured (or are about to) → `screen`, then `compare` the finalists
- "Can I afford this rent?" → `budget` (the 30/33/50 rules + landlord 3×-income math)
- Touring today: score each place on the 1-5 criteria sheet right after leaving (memory decays in hours)
- About to sign: `negotiate` with the facts you gathered (days vacant, comparables, lease flexibility)
- Defining the search itself: hard constraints (max commute, pets, budget) before you waste tours
- Don't use for: buying property (mortgage/tax math differs — see `job-offer-comparator` style skills for offers), roommate conflict mediation, or short-term vacation rentals.

## The 16 Criteria

| Criterion | Default weight | 1 looks like | 5 looks like |
|---|---|---|---|
| price | 3 | over budget | at/below budget |
| commute | 3 | 90+ min | under 20 min |
| noise | 3 | constant | silent |
| safety | 3 | uncomfortable | no thought |
| space | 2 | cramped | generous |
| light | 2 | dark cave | sunny all day |
| kitchen | 2 | can't cook | joy to cook |
| building | 2 | falling apart | well managed |
| neighbors | 2 | nightly bass | peaceful |
| laundry | 2 | street trip | in-unit |
| transit | 2 | car mandatory | car-free easy |
| pets_ok | 2 | banned | welcome |
| storage | 1 | none | abundant |
| bathroom | 1 | grim | spa |
| flex_space | 1 | none | dedicated room |
| outdoor | 1 | none | private green |

Edit weights in `~/.apartment-scorecard.json` — set to 0 anything you don't care about. Score each listing 1-5 per criterion during/immediately after the tour; `criteria` prints this table.

## Commands

```bash
# Affordability: 30/33/50% rules, 3×-income approval math, front costs
python3 scripts/apartment_scorecard.py budget

# See criteria + defaults
python3 scripts/apartment_scorecard.py criteria

# Screen & rank: hard constraints kill, survivors score, true cost ranks
python3 scripts/apartment_scorecard.py screen --file apartments.json

# Side-by-side of finalists + quality-vs-cost premium
python3 scripts/apartment_scorecard.py compare "Maple St 2BR" "Oak Rd Garden"

# Negotiation plan with your leverage facts
python3 scripts/apartment_scorecard.py negotiate "Maple St 2BR" \
    --vacant-days 30 --lease-offer 18 \
    --facts comparables move_in_speed

# Full demo: budget → screen → compare → negotiate
python3 scripts/apartment_scorecard.py example
```

Listings: JSON list (or CSV) — `name`, `rent`, `bedrooms`, `commute_min`, `deposit`, `fees_monthly`, `parking_monthly`, `pet_rent_monthly`, `broker_fee`, `utilities_included`, `pets_ok`, `available` (YYYY-MM-DD), `lease_months`, plus your 1-5 `scores` per criterion. See `references/listing-format.md`.

## True Cost Model

```
true_monthly = rent + monthly fees + utilities (if not included)
             + renters insurance + parking + pet rent
             + deposit × 4% / 12        (interest your money loses)
             + (broker + move-in fees) / lease months
             + commute_min × 2 × days × 4.33 × $/min (optional, try 0.3-0.8)
```

The commute term is the sleeper: at $0.50/min, a place 20 minutes further costs ~$433/month — often more than the rent difference people agonize over. Report also shows `%income` so the 50% danger line is visible at a glance.

## Workflow

1. `budget` → know your real ceiling BEFORE touring (all-in, not rent).
2. Set hard constraints in the weights file; don't tour what fails them.
3. Tour with the criteria sheet; score 1-5 within an hour of each visit.
4. `screen` → ranking with hard fails listed; `compare` the top 2 → the premium line asks the right question ("is $300/mo worth 9 score points?").
5. `negotiate` the chosen one with real facts → anchor first, trade lease length/speed for dollars, get it in writing.

## Common Pitfalls

1. **Comparing rent instead of true cost.** A $1,690 place with no fees and included utilities can be cheaper than a $1,580 place with $150/month of parking + amenity + pet fees. The screen table's `true $/mo` column exists to prevent this.
2. **Scoring during the tour by vibes, then writing numbers later.** Score within the hour; bring the criteria list; photograph everything (the photos double as deposit-dispute evidence later).
3. **Ignoring the commute because "it's fine."** Value your time honestly (the $/min setting); 30 extra minutes daily is ~22 hours/month.
4. **Hard constraints as soft preferences.** If pets are non-negotiable, they're a constraint, not a weight — mixed-up categories is how people end up heartbroken at lease signing.
5. **Negotiating by asking "is the rent flexible?"** That invites a no. Anchor with a specific number and a trade (longer lease, fast move-in, auto-pay); `negotiate` prints the script.
6. **Forgetting front costs.** Deposit + first + last + broker = 2.5-3.5× monthly rent due on signing day; budget it before you fall in love.
7. **Weighting everything 3.** If everything matters, nothing does. Force yourself to 0-out at least five criteria.

## Verification Checklist

- [ ] `python3 scripts/test_apartment_scorecard.py` → ALL TESTS PASSED (29 assertions)
- [ ] `python3 scripts/apartment_scorecard.py example` runs the full pipeline
- [ ] Weights file edited to YOUR priorities (not defaults)
- [ ] Every toured listing scored within an hour of the visit
- [ ] Decision made on true $/mo + score, not advertised rent + vibes
