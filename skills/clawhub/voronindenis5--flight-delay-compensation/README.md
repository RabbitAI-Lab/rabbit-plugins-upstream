# flight-delay-compensation ✈️

**Know exactly what the airline owes you — and get it.**

A 5-hour delay on a Munich→New York flight legally entitles each passenger to
€600 under EU261. Most never claim it. Airlines reject half of all first
claims with boilerplate like "technical difficulties are beyond our control" —
which courts have repeatedly ruled is not a valid defense. This skill is a
compensation rule engine + claim-letter generator that closes the gap between
what passengers are owed and what they actually collect.

## The real-world problem

- An estimated **€8-10 billion in EU compensation goes unclaimed annually**
- Passengers don't know which law applies (EU261? UK? APPR? DOT?) or the amount tiers
- Airlines deflect with vouchers (which waive cash rights) and pseudo-legal
  "extraordinary circumstances" claims
- Claim agencies take 25-50% cuts for what is often one well-worded letter

## What it does

`flight_claim_checker.py` is an offline rule engine:

- **Eligibility** — delay (≥3h at *final destination*, so connecting flights
  work), cancellation (14-day notice rules + reroute timing with the 50%
  reduction bands), denied boarding
- **Amounts** — EU261 €250/€400/€600 · UK261 £220/£350/£520 · US denied
  boarding 200%/400% caps · Canada APPR CAD 400-1000 · India DGCA bands ·
  Brazil ANAC guidance
- **Defense analysis** — airline says "technical fault"? The engine cites
  CJEU case law (Wallentin-Hermann, Krüsemann) and tells you to push back.
  Says "weather"? It tells you to demand METAR evidence.
- **Care entitlements** — meals/hotel/transport thresholds, separate from cash
- **Baggage** — Montreal Convention deadlines (21/7 days) and SDR caps
- **Deadlines** — statute of limitations per jurisdiction
- **Claim letter** — generates the full 14-day-ultimatum letter with booking
  details filled in

## Quick start

```bash
# EU flight delayed 5h, 1450 km route
python3 scripts/flight_claim_checker.py --from MUC --to LHR --distance 1450 \
  --delay 300 --date 2026-07-14 --carrier "Lufthansa"

# Airline rejected you citing "technical fault"? Check the defense:
python3 scripts/flight_claim_checker.py --from FRA --to JFK --distance 6200 \
  --delay 400 --airline-reason "technical fault" --carrier "Lufthansa"

# Generate the claim letter
python3 scripts/flight_claim_checker.py --from CDG --to TXL --distance 880 \
  --delay 400 --date 2026-05-20 --carrier "Air France" \
  --passenger-name "Jane Doe" --booking-ref ABC123 --letter claim.txt

# US domestic — get the honest answer (no federal delay compensation)
python3 scripts/flight_claim_checker.py --from JFK --to LAX --distance 3970 \
  --delay 420 --jurisdiction US --carrier "Delta"
```

## Example

```
✅ ELIGIBLE — EUR 600  [>3,500 km]
   per passenger (multiply by travelers on the booking)

REASONING
  • Delay 6h40m at final destination ≥ 3h → >3,500 km tier compensation.

AIRLINE DEFENSE ANALYSIS
  • 'technical fault' is NOT an extraordinary circumstance — courts
    (CJEU Wallentin-Hermann, Krüsemann) hold routine technical/crew issues
    are the airline's responsibility. Push back.

⏰ Claim deadline (statute of limitations): 2029-06-15
```

## License

MIT © Denis Voronin
