# Claim Strategy: How to Actually Get Paid

Airlines reject ~50% of first claims — most rejections don't survive a well-worded reply. This is the playbook.

## Step 1 — Collect evidence immediately (at the airport)

- Photo of the departure board showing the delay/cancellation
- Boarding passes (yours and any rerouted ones)
- The reason the airline staff gave, in writing if possible (ask gate agents to note it)
- Receipts for meals, transport, hotel, toiletries (care expenses are separately reimbursable)
- Names of staff you spoke with; timeline notes

Airlines love claiming "extraordinary circumstances" after the fact; contemporaneous evidence beats their boilerplate.

## Step 2 — File directly with the operating carrier

Find the airline's EU261/APPR complaints web form or complaints email (usually buried in "legal" or "feedback" pages — the agent can locate it). Include:

1. Booking reference, flight number, date, route
2. Scheduled vs actual arrival times (final destination!)
3. The regulation you're claiming under (EU261 Art. 6/7, APPR, etc.)
4. Amount claimed and bank details (IBAN)
5. 14-day ultimatum: "please pay within 14 days or I will escalate to [NEB/CTA/DOT] and pursue ADR"

Use the generated letter from `flight_claim_checker.py` as the body.

**Operating carrier, not codeshare seller.** If Lufthansa marketed a flight operated by Air Dolomiti, the claim goes to Air Dolomiti.

## Step 3 — Decode the rejection

Common rejection templates and rebuttals:

| Airline says | Reality | Your reply |
|---|---|---|
| "Technical fault = extraordinary circumstance" | CJEU (Wallentin-Hermann, van der Lans) says routine faults are inherent to operations | Cite case law; request the maintenance record specifics they rely on |
| "Weather at origin" | Often only ATC *flow restrictions* triggered by distant weather — courts split; ask for METARs | Request specific METAR/NOTAM evidence for your airport and timestamp |
| "ATC strike" | Only airport-wide/EU-wide strikes qualify; the airline's *own staff* striking does not | Ask which entity struck and when |
| "Crew shortage" | Airline's planning problem = not extraordinary (CJEU Krüsemann) | Cite Krüsemann (2018) |
| Voucher offered as final | Cash is your right; vouchers optional | "I do not accept vouchers; payment under Art. 7 to IBAN …" |

## Step 4 — Escalate (free, and it works)

- **EU:** complain to the National Enforcement Body of the departure country (or arrival, if EU carrier). List maintained by the European Commission. NEB pressure settles many cases.
- **ADR schemes:** aviationADR (UK), SOeP or Söp (Germany), SGK/Conciliator (other). Binding-ish on the airline if it's a member — check membership; low-cost carriers often aren't.
- **UK:** CAA escalation + MCOL small claims (cheap, high success on documented 3h+ delays).
- **Canada:** Canadian Transportation Agency complaint (free).
- **US:** DOT complaint (denied boarding/tarmac), DOT consumer complaint for plan violations.
- **Courts:** small-claims track in the country of departure or airline HQ. Costs are low; airlines frequently settle on receipt of the summons.

## Step 5 — When a claims agency makes sense

Agencies (AirHelp, Flightright, etc.) take 25-50% + success fees, but they have legal teams and the airline's fear of court. Consider an agency when:

- Your case is >6 months old with stonewalling
- The airline's extraordinary-circumstances claim needs METAR/NOTAM forensics
- You'd rather not file small-claims abroad

For clean 4h+ delays with documentation, DIY letters convert at high rates — don't give away 35% of €600 without trying one letter first.

## Money details

- Compensation is per **passenger** — families multiply (3 passengers on a €600 tier = €1,800).
- Paid in cash/bank transfer; refuse "travel credit only" responses (illegal under EU261 Art. 7(3)).
- Business or economy — same amounts.
- Taxes: generally tax-free as compensation for loss, but jurisdiction-dependent; not the airline's business anyway.

## Template follow-up (rejection reply)

> Dear [Airline],
>
> You rejected my claim of [date] citing [reason]. Under [regulation], the burden of proving extraordinary circumstances rests with the carrier, and per [CJEU case], [reason] does not qualify. I request the specific evidence supporting your position within 14 days. Absent payment of [amount] by [date], I will file with [NEB/ADR/court] without further notice.
>
> [Name, booking ref, flight, IBAN]

## Record-keeping

Track: flight details → claim sent date → responses received → deadline (statute of limitations). The checker outputs the deadline; put a calendar reminder at deadline-minus-3-months.
