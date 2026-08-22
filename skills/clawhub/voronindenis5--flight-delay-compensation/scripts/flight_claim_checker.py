#!/usr/bin/env python3
"""Flight Delay Compensation checker — rule engine for EU261, UK261,
US DOT, Canada APPR, Brazil ANAC, Turkey SHY, India DGCA, plus Montreal
Convention baggage rules.

Determines eligibility, computes the cash amount, evaluates extraordinary-
circumstances defenses, tracks the claim deadline, and generates a claim
letter. Pure offline logic — the user supplies flight facts.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from pathlib import Path

# ---------------------------------------------------------------------------
# Jurisdiction rules
# ---------------------------------------------------------------------------

EU_CARRIERS_HINTS = [
    "lufthansa", "air france", "klm", "iberia", "ryanair", "easyjet",
    "vueling", "wizz", "tap", "austrian", "swiss", "brussels airlines",
    "sas", "finnair", "ita", "lot", "croatia airlines", "aegean", "tarom",
    "turkish airlines", "pegasus", "british airways", "virgin atlantic",
    "jet2", "tui", "wideroe", "norwegian", "air baltic", "eurowings",
    "sunexpress", "anadolujet", "pegasus",
]
EU_AIRPORT_PREFIX = ("EU",)  # not usable directly; we rely on --jurisdiction

UK_AIRPORT_CODES = {"LHR", "LGW", "STN", "LTN", "LCY", "MAN", "BHX", "EDI",
                    "GLA", "BRS", "NCL", "BFS", "SOU", "ABZ", "LPL", "EMA"}
EU_AIRPORT_CODES = {
    "FRA", "MUC", "BER", "HAM", "DUS", "CDG", "ORY", "NCE", "LYS", "MRS",
    "AMS", "BRU", "MAD", "BCN", "AGP", "VLC", "LIS", "OPO", "FCO", "MXP",
    "VCE", "PMO", "ATH", "SKG", "VIE", "ZRH", "GVA", "CPH", "ARN", "OSL",
    "HEL", "DUB", "WAW", "KRK", "PRG", "BUD", "OTP", "SOF", "ZAG", "DBV",
    "LJU", "RIX", "VNO", "TLL", "ARN", "AYT", "IST", "SAW", "AYT",
}  # includes Turkey (SHY mirrors EU261)


@dataclass
class Ruling:
    eligible: bool
    jurisdiction: str = ""
    regulation: str = ""
    amount: float = 0.0
    currency: str = ""
    tier_label: str = ""
    reasons: list = field(default_factory=list)
    care: list = field(default_factory=list)
    deadline: str = ""
    defense_notes: list = field(default_factory=list)
    notes: list = field(default_factory=list)


def detect_jurisdiction(origin: str, dest: str, carrier: str,
                        override: str | None) -> str:
    if override:
        o = override.upper()
        # normalize common aliases
        if o in ("EU", "EU261", "EUROPE"):
            return "EU"
        if o in ("UK", "GB", "UK261"):
            return "UK"
        if o in ("US", "USA", "DOT"):
            return "US"
        if o in ("CA", "CANADA", "APPR"):
            return "CA"
        if o in ("BR", "BRAZIL"):
            return "BR"
        if o in ("TR", "TRKEY", "TURKEY"):
            return "TR"
        if o in ("IN", "INDIA"):
            return "IN"
        return o
    car = (carrier or "").lower()
    o, d = (origin or "").upper(), (dest or "").upper()
    # Departure airport governs first: EU departure → EU261; UK departure → UK261
    if o in EU_AIRPORT_CODES:
        return "EU"
    if o in UK_AIRPORT_CODES:
        return "UK"
    if d in UK_AIRPORT_CODES or \
            any(h in car for h in ("british airways", "virgin atlantic",
                                   "jet2", "tui")):
        return "UK"
    if d in EU_AIRPORT_CODES or \
            any(h in car for h in EU_CARRIERS_HINTS):
        return "EU"
    return "US"  # default fallback reports honestly


def eu_tier_amount(distance_km: int, currency: str = "EUR") -> tuple[float, str]:
    if currency == "GBP":
        if distance_km <= 1500:
            return 220, "≤1,500 km"
        if distance_km <= 3500:
            return 350, "1,500–3,500 km"
        return 520, ">3,500 km"
    if distance_km <= 1500:
        return 250, "≤1,500 km"
    if distance_km <= 3500:
        return 400, "1,500–3,500 km"
    return 600, ">3,500 km"


EXTRAORDINARY = {
    "weather", "storm", "snow", "fog", "ice",
    "atc", "atc strike", "air traffic control",
    "security", "security threat",
    "medical", "medical emergency",
    "airport closure", "closure",
}
NOT_EXTRAORDINARY = {
    "technical", "technical fault", "mechanical", "maintenance",
    "crew", "crew shortage", "staffing", "strike (airline staff)",
    "operational", "overbooked", "late arrival (rotational)",
}


def evaluate_extraordinary(reason: str) -> tuple[bool, str]:
    r = (reason or "").lower().strip()
    for k in NOT_EXTRAORDINARY:
        if k in r:
            return False, (f"'{reason}' is NOT an extraordinary circumstance — "
                           "courts (CJEU Wallentin-Hermann, Krüsemann) hold routine "
                           "technical/crew issues are the airline's responsibility. "
                           "Push back.")
    for k in EXTRAORDINARY:
        if k in r:
            return True, (f"'{reason}' may qualify as extraordinary — compensation "
                          "unlikely unless you can disprove (ask for METAR/NOTAM "
                          "evidence).")
    return False, (f"'{reason}' is not a recognized extraordinary circumstance — "
                   "demand specifics from the airline.")


# ---------------------------------------------------------------------------
# Main evaluation
# ---------------------------------------------------------------------------


def evaluate(args) -> Ruling:
    r = Ruling(eligible=False)
    jur = detect_jurisdiction(args.origin, args.destination,
                              args.carrier, args.jurisdiction)
    r.jurisdiction = jur

    flight_date = date.fromisoformat(args.date) if args.date else None

    # which delay number matters
    if args.disruption == "cancellation":
        delay = args.reroute_delay
    else:
        delay = args.delay

    # ---------------- EU / UK / TR (shared shape) ----------------
    if jur in ("EU", "UK", "TR"):
        cur = "GBP" if jur == "UK" else "EUR"
        r.regulation = {"EU": "EC 261/2004", "UK": "UK261 (retained EU261)",
                        "TR": "SHY-Passenger"}.get(jur, "EC 261/2004")
        amount, tier = eu_tier_amount(args.distance, cur)
        r.tier_label = tier

        if args.disruption == "denied-boarding":
            r.eligible = True
            r.amount = amount
            r.currency = cur
            r.reasons.append(
                "Involuntary denied boarding: full distance-tier compensation, "
                "no extraordinary-circumstances defense applies.")
        elif args.disruption == "cancellation":
            notice = args.notice if args.notice is not None else 0
            if notice >= 14:
                r.reasons.append(
                    f"Cancelled with {notice} days notice ≥ 14 — no cash "
                    "compensation due (refund/reroute rights remain).")
                r.eligible = False
            elif delay is None or delay <= 120:
                r.reasons.append(
                    "Cancellation <14 days notice with reroute arriving "
                    "≤2h late — no cash compensation (refund/reroute "
                    "rights remain).")
                r.eligible = False
            else:
                # Art 7(2) 50% reduction if reroute delay within tier bound
                reduction_bound = (120 if args.distance <= 1500
                                   else 180 if args.distance <= 3500
                                   else 240)
                if delay <= reduction_bound:
                    r.eligible = True
                    r.amount = round(amount / 2)
                    r.currency = cur
                    r.reasons.append(
                        f"Cancelled on {notice} days notice; reroute arrived "
                        f"{delay // 60}h{delay % 60:02d}m late (within "
                        f"{reduction_bound // 60}h tier bound) → 50% of "
                        f"{tier} tier.")
                else:
                    r.eligible = True
                    r.amount = amount
                    r.currency = cur
                    r.reasons.append(
                        f"Cancelled on {notice} days notice; reroute arrived "
                        f"{delay // 60}h{delay % 60:02d}m late → full {tier} tier.")
        else:  # delay
            if delay is None or delay < 180:
                th = "2h" if args.distance <= 1500 else "3-4h"
                r.reasons.append(
                    f"Delay {delay or 0}m < 3h threshold — no cash compensation. "
                    f"Care entitlements (meals, communications) may start at {th}.")
            else:
                r.eligible = True
                r.amount = amount
                r.currency = cur
                r.reasons.append(
                    f"Delay {delay // 60}h{delay % 60:02d}m at final destination "
                    f"≥ 3h → {tier} tier compensation.")

        # extraordinary circumstances
        if args.airline_reason and r.eligible:
            is_ex, note = evaluate_extraordinary(args.airline_reason)
            r.defense_notes.append(note)
            if is_ex:
                r.eligible = False
                r.amount = 0
                r.reasons.append(
                    "Airline-cited reason may be extraordinary — claim weakened. "
                    "Request evidence; see claim-strategy.md before conceding.")

        # care entitlements
        care_hours = 2 if args.distance <= 1500 else 4
        eff = delay or 0
        if eff >= care_hours * 60:
            r.care.append(f"Meals/refreshments/2 communications due after "
                          f"{care_hours}h delay")
        if eff >= 5 * 60:
            r.care.append("5h+ delay: right to full refund instead of waiting")
        if args.overnight:
            r.care.append("Overnight: hotel + transfers due")

        # deadline
        if flight_date:
            years = {"EU": 3, "UK": 6, "TR": 2}.get(jur, 2)
            r.deadline = (flight_date + timedelta(days=365 * years)).isoformat()
            r.notes.append(f"Statute of limitations ≈ {years} years "
                           f"(jurisdiction-dependent; file early).")

    # ---------------- US ----------------
    elif jur == "US":
        r.regulation = "14 CFR 250 (DOT)"
        if args.disruption == "denied-boarding":
            r.eligible = True
            if delay is None or delay >= 120:
                r.amount = 1350  # 400% cap (inflation-adjusted)
                r.currency = "USD"
                r.tier_label = "400% of one-way fare, capped"
            elif delay >= 60:
                r.amount = 675
                r.currency = "USD"
                r.tier_label = "200% of one-way fare, capped"
            else:
                r.amount = 0
                r.reasons.append("Substitute transport arrived <1h late — "
                                 "no denied-boarding compensation.")
                r.eligible = False
            if r.eligible:
                r.reasons.append("Involuntary bump with "
                                 f"{(delay or 0) // 60}h arrival delay.")
        else:
            r.reasons.append(
                "US domestic rules: NO federal compensation for delays or "
                "cancellations. Meals/hotel depend on the airline's published "
                "customer plan (DOT dashboard). Tarmac: deplaning right at 3h "
                "domestic / 4h international.")
            if args.baggage_issue:
                r.notes.append("Baggage: Montreal Convention / DOT liability "
                               "cap (~$3,800 domestic) may apply — see "
                               "jurisdictions.md.")
    # ---------------- Canada ----------------
    elif jur == "CA":
        r.regulation = "APPR (Canada)"
        if args.disruption == "denied-boarding":
            r.eligible = True
            r.amount, r.currency = 900, "CAD"
            r.tier_label = "denied boarding, large carrier"
        elif delay is not None and delay >= 180:
            r.eligible = True
            h = delay / 60
            if h < 6:
                r.amount, r.tier_label = 400, "3-6h delay (large carrier)"
            elif h < 9:
                r.amount, r.tier_label = 700, "6-9h delay (large carrier)"
            else:
                r.amount, r.tier_label = 1000, "9h+ delay (large carrier)"
            r.currency = "CAD"
            r.reasons.append(f"Delay {delay // 60}h{delay % 60:02d}m ≥ 3h → "
                             "APPR tier.")
            if args.airline_reason:
                is_ex, note = evaluate_extraordinary(args.airline_reason)
                r.defense_notes.append(note)
                if is_ex:
                    r.eligible, r.amount = False, 0
                    r.notes.append("APPR extraordinary-circumstances exclusion "
                                   "is broader than EU261 — see jurisdictions.md.")
        else:
            r.reasons.append("Under 3h delay: standards of treatment (meals/"
                             "communications) may apply; no cash tier.")
    # ---------------- Brazil ----------------
    elif jur == "BR":
        r.regulation = "ANAC Resolução 400"
        if delay is not None and delay >= 240:
            r.eligible = True
            r.reasons.append(
                "Delay ≥4h: airline must offer rebooking, refund, or trip "
                "completion. No fixed statutory cash, but material damages are "
                "claimable under consumer law (small-claims practice).")
            r.notes.append("Document all expenses; consumer-court claims for "
                           "damages have high success rates in Brazil.")
        else:
            r.reasons.append("Under 4h: material assistance (communication, "
                             "food) after 1-4h thresholds.")
    # ---------------- India ----------------
    elif jur == "IN":
        r.regulation = "DGCA CAR Section 3, Series M"
        if delay is not None:
            if delay <= 60:
                r.amount = 5000
            elif delay <= 120:
                r.amount = 7500
            else:
                r.amount = 10000
            r.eligible = delay > 60
            r.currency = "INR"
            r.tier_label = f"{delay}m delay band"

    if args.baggage_issue:
        r.notes.append(
            f"Baggage issue ({args.baggage_issue}): Montreal Convention "
            "(~1,288 SDR ≈ $1,700) — written claim within 21 days (delayed) "
            "or 7 days (damaged).")

    return r


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------


def render(r: Ruling, args) -> str:
    out = []
    a = out.append
    a("=" * 62)
    a(" FLIGHT COMPENSATION CHECK")
    a("=" * 62)
    a(f" Route        : {args.origin or '?'} → {args.destination or '?'} "
      f"({args.distance:,} km)")
    a(f" Carrier      : {args.carrier or '?'}    Date: {args.date or '?'}")
    a(f" Disruption   : {args.disruption}"
      + (f" (arrival delay {args.delay}m)" if args.disruption == "delay" else
         (f" (reroute delay {args.reroute_delay}m, {args.notice}d notice)"
          if args.disruption == "cancellation" else "")))
    a(f" Jurisdiction : {r.jurisdiction} — {r.regulation}")
    a("")
    if r.eligible:
        a(f" ✅ ELIGIBLE — {r.currency} {r.amount:,.0f}"
          + (f"  [{r.tier_label}]" if r.tier_label else ""))
        a("    per passenger (multiply by travelers on the booking)")
    else:
        a(" ❌ NOT ELIGIBLE for cash compensation")
    a("")
    if r.reasons:
        a(" REASONING")
        for x in r.reasons:
            a(f"   • {x}")
    if r.care:
        a("")
        a(" CARE ENTITLEMENTS (separate from cash)")
        for x in r.care:
            a(f"   • {x}")
    if r.defense_notes:
        a("")
        a(" AIRLINE DEFENSE ANALYSIS")
        for x in r.defense_notes:
            a(f"   • {x}")
    if r.notes:
        a("")
        a(" NOTES")
        for x in r.notes:
            a(f"   • {x}")
    if r.deadline:
        a("")
        a(f" ⏰ Claim deadline (statute of limitations): {r.deadline}")
    a("=" * 62)
    return "\n".join(out)


LETTER_TEMPLATE = """{city}, {today}

To: Customer Relations — {carrier}
Re: Claim under {regulation} — {flight_route}, {date}
    Booking ref: {booking}, Passenger: {passenger}

Dear {carrier},

On {date} I was a passenger on your flight {flight_route} ({route_km:,} km),
which {disruption_phrase}. {delay_phrase}

Under {regulation}, I am entitled to compensation of {amount}.
I request payment of {amount} to the following account within 14 days:
IBAN: [YOUR IBAN]   Name: [ACCOUNT HOLDER]

{care_clause}
Should you contend that extraordinary circumstances apply, kindly provide the
specific evidence (maintenance records, METAR/NOTAM) you rely on, together
with proof that all reasonable measures were taken to avoid the disruption.

Absent payment or a substantiated reply within 14 days, I will escalate this
matter to the competent National Enforcement Body / ADR scheme and, if
necessary, the courts, without further notice.

Yours faithfully,
{passenger}
[Address, phone, email]
"""


def render_letter(r: Ruling, args) -> str:
    if not r.eligible:
        return ("# No claim letter generated — ruling is not eligible.\n"
                "(Care/refund claims may still be worth a letter; adapt "
                "references/claim-strategy.md templates.)")
    disruption_phrase = {
        "delay": f"arrived {args.delay // 60}h{args.delay % 60:02d}m late at "
                 "the final destination",
        "cancellation": "was cancelled",
        "denied-boarding": "denied me boarding against my will "
                           "(involuntary denied boarding)",
    }[args.disruption]
    if args.disruption == "cancellation" and args.reroute_delay:
        delay_phrase = (f"I was rerouted and arrived "
                        f"{args.reroute_delay // 60}h"
                        f"{args.reroute_delay % 60:02d}m late at the final "
                        f"destination")
    else:
        delay_phrase = ""
    return LETTER_TEMPLATE.format(
        city="[Your city]", today=date.today().isoformat(),
        carrier=args.carrier or "[Airline]",
        regulation=r.regulation,
        flight_route=f"{args.origin or 'XXX'}→{args.destination or 'XXX'}",
        route_km=args.distance,
        date=args.date or "[date]",
        booking=args.booking_ref or "[booking ref]",
        passenger=args.passenger_name or "[Your name]",
        disruption_phrase=disruption_phrase, delay_phrase=delay_phrase,
        amount=f"{r.currency} {r.amount:,.0f}",
        care_clause=("I also claim reimbursement of attached care expenses "
                     "(meals/transport/hotel) with receipts."
                     if args.overnight or args.care_reimb else ""))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Air passenger compensation checker (EU261/UK261/US DOT/"
                    "APPR/ANAC/SHY/DGCA + Montreal baggage).")
    ap.add_argument("--from", dest="origin", help="origin airport code")
    ap.add_argument("--to", dest="destination", help="destination airport code")
    ap.add_argument("--distance", type=int, required=True,
                    help="great-circle km to FINAL destination")
    ap.add_argument("--delay", type=int,
                    help="arrival delay at final destination, minutes")
    ap.add_argument("--disruption", default="delay",
                    choices=["delay", "cancellation", "denied-boarding"])
    ap.add_argument("--reroute-delay", type=int,
                    help="for cancellations: rerouted arrival delay, minutes")
    ap.add_argument("--notice", type=int,
                    help="days of cancellation notice given")
    ap.add_argument("--date", help="flight date YYYY-MM-DD")
    ap.add_argument("--carrier", help="operating carrier name")
    ap.add_argument("--jurisdiction",
                    help="force EU/UK/US/CA/BR/TR/IN (auto-detected otherwise)")
    ap.add_argument("--airline-reason", dest="airline_reason",
                    help="reason the airline cited (e.g. 'technical fault')")
    ap.add_argument("--overnight", action="store_true",
                    help="disruption included an overnight wait")
    ap.add_argument("--baggage-issue", dest="baggage_issue",
                    choices=["delayed", "lost", "damaged"],
                    help="also check baggage rules")
    ap.add_argument("--passenger-name", dest="passenger_name")
    ap.add_argument("--booking-ref", dest="booking_ref")
    ap.add_argument("--care-reimb", action="store_true",
                    help="claim care expenses with receipts")
    ap.add_argument("--letter", type=Path, help="write claim letter to file")
    ap.add_argument("--json", type=Path, help="write ruling as JSON")
    args = ap.parse_args()

    if args.disruption in ("delay", "denied-boarding") and args.delay is None:
        ap.error(f"--delay is required for --disruption {args.disruption}")
    if args.disruption == "cancellation" and args.reroute_delay is None \
            and args.notice is not None:
        pass

    r = evaluate(args)
    print(render(r, args))

    if args.json:
        args.json.write_text(json.dumps({
            "eligible": r.eligible, "jurisdiction": r.jurisdiction,
            "regulation": r.regulation, "amount": r.amount,
            "currency": r.currency, "tier": r.tier_label,
            "reasons": r.reasons, "care": r.care,
            "defense_notes": r.defense_notes, "deadline": r.deadline,
            "notes": r.notes}, indent=2))
        print(f"\nJSON ruling → {args.json}")
    if args.letter:
        args.letter.write_text(render_letter(r, args))
        print(f"Claim letter → {args.letter}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
