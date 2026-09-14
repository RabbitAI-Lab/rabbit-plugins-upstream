# Commute Cost Model — Assumptions, Sources, and Math

This reference documents every number `scripts/commute_opt.py` uses, why, and how to override it.

## 1. Time is the dominant cost

US Census / DOT figures: average one-way commute ≈ 27–28 minutes; ~10% of workers exceed 60 minutes each way. At 250 commuting days/year, the average worker spends **~230 hours/year** commuting — roughly six 40-hour work weeks. Long-commute (>1h each way) correlates in happiness research (e.g., Kahneman & Krueger day-reconstruction studies) with among the lowest rated daily activities, and longitudinal studies link long commutes to higher stress, back pain, and worse sleep — effects that do NOT fully adapt over time, unlike income gains.

**Valuation:** WFH Research (Barrero, Bloom, Davis) finds workers on average value eliminated commute time at close to their full gross wage (their estimate: ~8% of pay willingness-to-trade for full-remote). This tool defaults to pricing time at your **after-tax hourly rate** (`--rate`), a slightly conservative choice. If your commute time is genuinely usable (reading on a train, not driving), discount it — the `decide` output shows time and money separately so you can reweight.

## 2. Weekday traffic profile

Congestion peaks **mid-week**. Default multipliers applied to off-peak time (car peak direction 7–9am / 4–6pm):

| Weekday | Multiplier | Note |
|---|---|---|
| Mon | 1.28 | lighter Friday-adjacent spillover |
| Tue | 1.38 | peak |
| Wed | 1.42 | peak |
| Thu | 1.36 | near peak |
| Fri | 1.22 | lighter PM peak; but longer off-peak spread |

These are stylized from FHWA Urban Mobility Report congestion patterns and typical peer-reviewed urban profiles (Tue–Thu worst, Friday lightest peak). They're EDITABLE assumptions — if your city behaves differently (e.g., Friday worst in tourist towns), pass `--profile "1.30,1.40,1.45,1.40,1.35"`.

Transit rush factor: 1.10 (crowding, headway changes) — transit time is far more stable than car time; reliability is a big part of its value. Bike/walk: no rush multiplier; add your own weather-abandonment rate (default: bike usable 60% of days, editable — see params).

## 3. Vehicle cost per mile

Blended AAA "Your Driving Costs" + IRS business-rate structure, split into mileage-variable and ownership components:

| Component | Default $/mile | Nature |
|---|---|---|
| fuel + electricity | 0.14 | variable |
| maintenance + tires | 0.10 | variable |
| depreciation | 0.13 | variable-ish (mileage-driven) |
| insurance + registration + finance | 0.10 | ownership, amortized per-mile |

**Total default: $0.47/mile.** The strict marginal cost of an extra trip is lower (≈$0.24–0.30: fuel + maintenance + some depreciation), but commutes drive total mileage, which drives vehicle choice, insurance tiers, and replacement frequency — so the fully-loaded per-mile figure is the honest planning number. The tool prints both `marginal` and `fully-loaded` annual costs. Parking and tolls: add via `--parking` ($/day) and `--tolls` ($/day).

**Transit:** default fare $2.75/trip, monthly cap logic $130 (beyond which a pass is cheaper — the tool switches automatically at 2×cap/month). **Bike:** $0.08/mile (chain, tires, brake wear). **Walk:** $0.

## 4. Annualization

`trips_per_year = commute_days_per_week × weeks_per_year` — defaults 5 × 48 (assumes ~4 weeks of PTO/holidays/remote mix). All time and money figures are ROUND TRIP. Hours/year = one-way minutes × 2 × trips ÷ 60.

## 5. Hybrid schedule optimizer

For N office days out of 5 weekdays, evaluate all C(5,N) subsets: total weekly commute = Σ chosen-day rush minutes. Report the best subset, the worst, and Mon–Wed–Fri (the cultural default) with its penalty vs. best. With the default profile, **Mon/Thu/Fri wins for 3-day car commuters** (skips the Tue/Wed peak stack, uses light-Friday), **Tue/Wed/Thu is the worst 3-day choice**, and for 2 days the optimizer avoids Wednesday. If your office requires anchor days, just compare those subsets — the optimizer output makes the forced-vs-free penalty visible.

## 6. Equivalent-rent framing (the `decide` command)

For each option: `annual_total_$ = time_$ + direct_$ (vehicle/fare/parking/tolls)`. Versus the baseline (first) option, an option is justified when:

```
extra_annual_cost ≤ 12 × (monthly_rent_savings)
→ breakeven_extra_rent = −(Δ annual total cost) / 12
```

I.e., if House B costs $450/month less but adds $5,470/year in commute, it still wins by $5,470 − $5,400 = $70… the tool prints exactly this arithmetic and the verdict. The `extra_rent` field in options is monthly, positive = costs MORE than baseline (then commute savings must beat it).

## 7. Lifespan framing

`waking_days = hours / 16`. A 10-minute-each-way increase = 83 h/yr ≈ 5.2 waking days/yr ≈ **52 waking days per decade**. Presenting commute deltas in days-per-decade is the single most effective reframing in housing-decision research literature; the tool surfaces it for every option.

## 8. Known limitations

- Point estimates, not distributions: no variance modeling. Rush-hour variance is real; transit's lower variance is captured only qualitatively.
- No carpool/HOV modeling (halve the time value if you genuinely enjoy company, or use transit logic).
- No relocation of *other* trips (groceries, school run) — moving changes those too; treat results as commute-only.
- Cyclical congestion feedback (everyone optimizing the same days) is obviously not modeled — office policies, not this tool, set reality.

## 9. Quick sanity table (defaults, 48 wks/yr)

| One-way | Days/wk | Hours/yr | Car $/yr @15mi (loaded) | Days/decade |
|---|---|---|---|---|
| 15 min | 5 | 120 | $6,768 | 75 |
| 25 min | 5 | 200 | $8,460 | 125 |
| 40 min | 5 | 320 | $10,152 | 200 |
| 60 min | 5 | 480 | $11,844 | 300 |
| 25 min | 3 (hybrid) | 120 | $5,076 | 75 |
