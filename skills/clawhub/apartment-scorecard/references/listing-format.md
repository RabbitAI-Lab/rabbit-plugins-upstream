# Listing Format & Tour Protocol

## Full listing JSON

```json
{
  "name": "Maple St 2BR",
  "rent": 1850,
  "sqm": 68,
  "bedrooms": 2,
  "bathrooms": 1,
  "commute_min": 32,
  "transit_pass_monthly": 90,
  "deposit": 1850,
  "fees_monthly": 40,
  "parking_monthly": 100,
  "pet_rent_monthly": 25,
  "broker_fee": 0,
  "move_in_fees": 200,
  "utilities_included": false,
  "pets_ok": true,
  "available": "2026-09-15",
  "floor": 3,
  "lease_months": 12,
  "notes": "top floor, corner unit, faces park",
  "scores": {
    "price": 3, "commute": 4, "space": 4, "light": 5, "noise": 4,
    "kitchen": 3, "storage": 3, "bathroom": 3, "building": 4,
    "neighbors": 4, "laundry": 5, "safety": 4, "transit": 5,
    "pets_ok": 5, "flex_space": 4, "outdoor": 3
  }
}
```

### Field notes

- `rent`: advertised monthly rent.
- `commute_min`: door-to-door ONE way, at the hour you'd actually travel.
  Test it, don't estimate from the map.
- `transit_pass_monthly`: if you'd need a pass ONLY for this location
  (otherwise leave 0).
- `deposit`, `broker_fee`, `move_in_fees`: one-time money; broker+move-in
  amortize over `lease_months`, deposit counts as 4%/year lost interest
  (it comes back, but its earning power doesn't).
- `fees_monthly`: amenity/tech/admin/"resident benefits" garbage fees —
  always ask "what's the ALL-IN monthly?" on the tour.
- `scores`: your 1-5 per criterion, filled within an hour of touring.
  Missing criteria are simply skipped (weight doesn't count for or against).

### CSV minimal format

`name,rent,bedrooms,commute_min,pets_ok,available` is enough for
screening; add columns as you collect them. Values auto-coerce
("true"/"false", numbers).

## Weights file (~/.apartment-scorecard.json)

```json
{
  "budget_monthly": 1900,
  "net_monthly_income": 6800,
  "debt_payments": 400,
  "max_commute_min": 55,
  "bedrooms_min": 1,
  "move_date": "2026-10-01",
  "pets": true,
  "utilities_estimate": 140,
  "renters_insurance": 15,
  "commute_cost_per_min": 0.5,
  "commute_days": 5,
  "weights": { "price": 3, "commute": 3, "light": 4, "noise": 3,
               "gym": 0, "...": "all 16 keys" }
}
```

- Hard constraints: `budget_monthly`, `max_commute_min`, `bedrooms_min`,
  `pets`, `move_date`. Set `null` to disable any of them.
- `commute_cost_per_min`: what an hour of your life costs you. If you
  earn $30/h net, 0.5 is a fair self-price. 0 disables the term.
- Weights 0-5; 0 removes the criterion from scoring entirely.

## The 30-minute tour protocol

Bring: phone (photos + this checklist), tape measure, earbuds.

1. **Outside first:** noise at the hour you'd sleep (visit at that hour
   if possible), street lighting, where you'd park, the commute test.
2. **Photos on entering:** every wall, every fixture, every existing
   scratch — timestamped. These are your deposit-dispute evidence.
3. **Run water** (pressure, drainage, hot water lag), **flush**, **open
   every window** (does it open? street noise?), **check cell signal**
   in the corner you'd work from, **note outlet count** where the desk
   would go.
4. **Ask:** all-in monthly with every fee? Average utilities last year?
   Why did the last tenant leave? How long has it been vacant? Deposit
   return policy and timeline? Those last two are negotiation facts.
5. **Score 1-5 on all 16 criteria in the stairwell** before the next
   tour. Your memory of "cozy" decays to "small" by tomorrow.

## Negotiation fact-finding

The levers in `negotiate` need facts; gather them cheaply:

- **Vacancy duration** — ask, or check listing history ("reduced price"
  and old photos = sitting empty). Every vacant month ≈ 8.3% of annual
  rent; landlords discount rationally.
- **Comparables** — same building listed lower, or same layout across
  the street. Printouts beat adjectives.
- **Season** — Nov-Feb signings are gold; landlords hate winter turnover
  and deep-clean costs.
- **Your tradables** — 18/24-month lease, move-in this week, auto-pay,
  or a longer notice period. Never trade something they didn't value.

Ask anchors 7% under list, walk-away deal at 3% under; on a $1,850 unit
that's a $666-$1,554/year swing for one uncomfortable conversation.
