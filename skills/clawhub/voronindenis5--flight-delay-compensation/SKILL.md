---
name: flight-delay-compensation
description: "Check if a delayed, cancelled, or overbooked flight qualifies for cash compensation under EU261, UK261, US DOT, Canada APPR, Brazil ANAC, Turkey SHY, or India DGCA rules. Calculates exact amounts by distance tier, evaluates airline extraordinary-circumstances defenses, tracks claim deadlines, and generates ready-to-send claim letters. Use when a flight disruption occurred and the user wants to know their rights or file a claim."
version: 1.0.0
author: Denis Voronin
license: MIT
tags: [travel, flights, compensation, eu261, passenger-rights, claims, airlines]
---
# Flight Delay Compensation ✈️

Check whether a delayed, cancelled, or overbooked flight qualifies for cash compensation (EU261, UK261, US DOT rules, Brazil ANAC, Canada APPR, Turkey SHY), calculate the exact amount, and auto-generate a ready-to-send claim letter — including connecting-flight logic, extraordinary-circumstances defenses, and deadline tracking.

## Overview

Billions in airline compensation goes unclaimed every year because passengers don't know their rights, airlines deflect with vouchers, and claim processes feel opaque. This skill closes that gap:

- **`flight_claim_checker.py`** — rule engine implementing EU261/UK261 distance tiers, delay thresholds, cancellation/denied-boarding rules, extraordinary circumstances exclusions, connecting itinerary logic (final-destination arrival delay is what counts), and statute-of-limitations tracking. Outputs eligibility, amount (EUR/GBP/CAD/USD), and a formatted claim letter.
- **`references/jurisdictions.md`** — full rule tables per jurisdiction including care entitlements (meals, hotel) and baggage rules.
- **`references/claim-strategy.md`** — how to actually get paid: where to file, escalation to NEB/A DR, airline delay tactics, and when agencies are worth their 35% cut.

Works offline; no flight-status APIs needed — the user provides the flight facts (the agent can look them up if tools allow).

## When to Use

- "My flight was delayed 4 hours / cancelled / I was bumped — am I owed money?"
- User provides an itinerary + disruption and wants eligibility + amount + letter
- Airline offered vouchers — check what cash they're legally owed instead
- Follow-up: "they rejected my claim citing weather — is that valid?"
- Connecting flights where a delay on leg 1 caused a missed leg 2
- Baggage delayed/lost/damaged on an international flight (Montreal Convention)

**Don't use for:** suing airlines in court (final escalation beyond NEB complaint), class actions, or US domestic delay claims (US rules only cover tarmac delays and denied boarding — no general delay compensation exists there; the tool will say so honestly).

## Quick Start

```bash
# EU flight, 5-hour delay, 1450 km
python3 scripts/flight_claim_checker.py --from MUC --to LHR \
  --distance 1450 --delay 300 --date 2026-07-14 --carrier "Lufthansa"

# Cancelled flight with rerouting arriving 3h late (EU)
python3 scripts/flight_claim_checker.py --from BCN --to FCO --distance 850 \
  --disruption cancellation --reroute-delay 180 --date 2026-06-01 \
  --carrier "Vueling" --notice 2

# US domestic delay (expect: no federal compensation — but get the truth)
python3 scripts/flight_claim_checker.py --from JFK --to LAX --distance 3970 \
  --delay 420 --jurisdiction US --carrier "Delta"

# Denied boarding (any jurisdiction with rules)
python3 scripts/flight_claim_checker.py --from FRA --to JFK --distance 6200 \
  --disruption denied-boarding --jurisdiction EU --carrier "United"

# Generate the claim letter too
python3 scripts/flight_claim_checker.py --from CDG --to TXL --distance 880 \
  --delay 400 --date 2026-05-20 --carrier "Air France" \
  --passenger-name "Jane Doe" --booking-ref ABC123 --letter claim.txt
```

## Rule Summary (built into the engine)

| Jurisdiction | Delay threshold | Amounts | Extraordinary circumstances |
|---|---|---|---|
| EU261 | 3h at final destination | €250 (≤1500km) / €400 (1500-3500) / €600 (>3500 or EU>3500) | Weather, ATC strikes, security, medical |
| UK261 | 3h | £220 / £350 / £520 | Same as EU |
| US DOT | none for delays | Denied boarding up to 400% of fare capped \$2150 (bump) | Weather |
| Canada APPR | 3h | CAD 400-1000 (large airlines) | Weather, safety |
| Brazil ANAC | 4h | Rebooking/refund + material damages | Weather, technical-fault exceptions disputed |
| Turkey SHY | 3h | €250/€400/€600 (mirrors EU) | Mirrors EU |

Care entitlements (meals/hotel) start at **2-4h delay** depending on distance and jurisdiction — the engine reports these even when cash compensation doesn't apply.

## Common Pitfalls

1. **Accepting vouchers on the spot.** Vouchers often waive your cash rights in the fine print. EU261 cash is a legal right; vouchers are optional and should exceed cash value if you take them.
2. **Missing connecting-flight logic.** A 90-minute delay on leg 1 that makes you arrive 4h late at your final destination still qualifies under EU261 — arrival delay at final destination is the test. The engine handles this via `--delay` = final arrival delay.
3. **Believing "technical fault = extraordinary circumstance."** Courts (incl. CJEU) have repeatedly ruled routine technical faults are the airline's responsibility. The engine flags weak defenses and tells the user to push back.
4. **Claiming against the wrong airline.** The claim goes to the **operating carrier**, not the codeshare seller or travel agency.
5. **Waiting too long.** Statutes of limitations run 1 year (e.g., some EU states) to 6 years (UK). The engine computes the deadline from the flight date and jurisdiction.
6. **Ignoring partial-reroute compensation.** If you accepted rerouting and still arrived 3h+ late, you're owed compensation (may be halved under EU rules for short-notice rerouting — engine applies this).

## Verification Checklist

- [ ] Jurisdiction auto-detected correctly (EU if departure or EU carrier arrival; UK variants; etc.)
- [ ] Distance tier checked against a real route distance (agent can verify via web)
- [ ] Arrival delay at **final destination** used for connecting itineraries
- [ ] Extraordinary-circumstances defense evaluated — if airline claims weather, verify with historical METAR/NOTAM before conceding
- [ ] Deadline computed and letter generated with booking reference + flight number

## References

- `references/jurisdictions.md` — complete rule tables + care entitlements + baggage (Montreal Convention)
- `references/claim-strategy.md` — filing channels, escalation, agency fee math, template follow-ups
