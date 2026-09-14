#!/usr/bin/env python3
"""
apartment_scorecard.py — compare competing apartments/houses with a weighted
scorecard instead of vibes.

Hard constraints kill listings first (budget, commute, bedrooms, pets, date),
then soft criteria score the survivors with YOUR weights, then money layers
on the true monthly cost (rent + fees + utilities + commute), and the report
ends with negotiation ammunition: the market signals that justify asking for
less.

Commands:
  criteria            interactive guide to building your weights file
  screen              score + rank listings from a JSON/CSV file
  compare             side-by-side table of 2+ listings
  budget              what you can actually afford (30% rule + debt)
  negotiate           leverage-based rent negotiation script
  example             self-contained demo on 4 sample listings

Files (override with --file): ~/.apartment-scorecard.json (weights)
                              ~/.apartments.json (listings)
Pure stdlib.
"""
import argparse
import csv
import datetime as dt
import json
import math
import os
import sys

DEFAULT_WEIGHTS = os.path.expanduser("~/.apartment-scorecard.json")
DEFAULT_LISTINGS = os.path.expanduser("~/.apartments.json")

# ---------------------------------------------------------------- criteria
# Each criterion: key, question, what 1 and 5 look like, default weight.
CRITERIA = [
    ("price", "Monthly cost vs your budget", None, 3,
     "over budget", "at/below budget"),
    ("commute", "Daily door-to-door commute (time × days)", None, 3,
     "90+ min", "under 20 min"),
    ("space", "Square meters / layout efficiency for your life", None, 2,
     "cramped", "generous"),
    ("light", "Natural light / window orientation", None, 2,
     "dark cave", "sunny all day"),
    ("noise", "Street/neighbor/traffic noise at the hours you sleep", None, 3,
     "constant", "silent"),
    ("kitchen", "Counter space, appliances, storage", None, 2,
     "can't cook", "joy to cook"),
    ("storage", "Closets, shelving, basement/attic", None, 1,
     "none", "abundant"),
    ("bathroom", "Size, condition, second bath?", None, 1,
     "grim", "spa"),
    ("building", "Building condition, elevator, upkeep", None, 2,
     "falling apart", "well managed"),
    ("neighbors", "Party walls thin? Upstairs stomper? Feel of the block", None, 2,
     "nightly bass", "peaceful"),
    ("laundry", "In-unit / in-building / laundromat distance", None, 2,
     "street trip", "in-unit"),
    ("safety", "Neighborhood safety at the hours you come home", None, 3,
     "uncomfortable", "no thought"),
    ("transit", "Transit options / walkability / parking", None, 2,
     "car mandatory", "car-free easy"),
    ("pets_ok", "Pet policy if relevant (hard constraint usually)", None, 2,
     "banned", "welcome"),
    ("flex_space", "Work-from-home nook, guest possibility", None, 1,
     "none", "dedicated room"),
    ("outdoor", "Balcony/terrace/yard/park proximity", None, 1,
     "none", "private green"),
]

# ---------------------------------------------------------------- defaults
def default_weights():
    return {
        "budget_monthly": 1800,
        "net_monthly_income": 5200,
        "debt_payments": 400,
        "max_commute_min": 45,
        "bedrooms_min": 1,
        "move_date": "2026-10-01",
        "pets": True,
        "weights": {k: wt for k, _, _, wt, _, _ in CRITERIA},
        "utilities_estimate": 140,
        "renters_insurance": 15,
        "commute_cost_per_min": 0.0,   # optional $ valuation
        "commute_mode": "transit",
    }


def load_json(path, create_with=None):
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    if create_with is not None:
        with open(path, "w") as f:
            json.dump(create_with, f, indent=2)
        return create_with
    return None


def load_listings(path):
    path = os.path.expanduser(path)
    if path.endswith(".csv"):
        rows = []
        with open(path) as f:
            for row in csv.DictReader(f):
                rows.append({k: _coerce(v) for k, v in row.items()})
        return rows
    with open(path) as f:
        return json.load(f)


def _coerce(v):
    if v is None or v == "":
        return None
    try:
        return int(v)
    except ValueError:
        pass
    try:
        return float(v)
    except ValueError:
        pass
    if v.lower() in ("true", "false"):
        return v.lower() == "true"
    return v


# ---------------------------------------------------------------- hard screen
def hard_screen(listing, w):
    """Return list of disqualifying reasons (empty = passes)."""
    fails = []
    rent = listing.get("rent", 0)
    budget = w.get("budget_monthly", 10**9)
    if rent > budget:
        fails.append(f"rent ${rent} > budget ${budget}")
    nc = w.get("max_commute_min")
    if nc is not None and listing.get("commute_min") is not None:
        if listing["commute_min"] > nc:
            fails.append(f"commute {listing['commute_min']} min > max {nc} min")
    nb = w.get("bedrooms_min")
    if nb is not None and listing.get("bedrooms") is not None:
        if listing["bedrooms"] < nb:
            fails.append(f"{listing.get('bedrooms')} bed < min {nb}")
    if w.get("pets") and listing.get("pets_ok") is False:
        fails.append("pets not allowed")
    md = w.get("move_date")
    if md and listing.get("available"):
        try:
            need = dt.date.fromisoformat(md)
            avail = dt.date.fromisoformat(str(listing["available"]))
            if avail > need:
                fails.append(f"available {avail} after move date {need}")
        except ValueError:
            pass
    return fails


# ---------------------------------------------------------------- scoring
def score(listing, w):
    """Weighted 1-5 score. Listing may carry 'scores': {criterion: 1-5}."""
    given = listing.get("scores", {})
    weights = w.get("weights", {})
    total = 0.0
    max_total = 0.0
    detail = []
    for key, _, _, _, _, _ in CRITERIA:
        wt = weights.get(key, 0)
        if wt == 0:
            continue
        val = given.get(key)
        if val is None:
            continue
        val = max(1, min(5, val))
        total += wt * val
        max_total += wt * 5
        detail.append((key, wt, val))
    pct = (total / max_total * 100) if max_total else 0.0
    return pct, detail


# ---------------------------------------------------------------- money
def true_monthly(listing, w):
    rent = listing.get("rent", 0)
    fees = (listing.get("fees_monthly", 0) or 0)
    deposit_interest_lost = ((listing.get("deposit", 0) or 0) * 0.04 / 12
                             if listing.get("deposit") else 0)
    utilities = 0 if listing.get("utilities_included") else w.get("utilities_estimate", 140)
    insurance = w.get("renters_insurance", 15)
    parking = listing.get("parking_monthly", 0) or 0
    pet_rent = listing.get("pet_rent_monthly", 0) or 0
    commute = commute_cost_monthly(listing, w)
    total = (rent + fees + utilities + insurance + parking + pet_rent
             + deposit_interest_lost + commute)
    breakdown = {
        "rent": rent, "fees": fees, "utilities": utilities,
        "insurance": insurance, "parking": parking, "pet_rent": pet_rent,
        "deposit_interest_lost": round(deposit_interest_lost, 2),
        "commute": round(commute, 2),
    }
    # amortize one-time costs over expected lease months
    months = listing.get("lease_months", 12)
    onetime = (listing.get("broker_fee", 0) or 0) + (listing.get("move_in_fees", 0) or 0)
    if onetime and months:
        total += onetime / months
        breakdown["one_time_amortized"] = round(onetime / months, 2)
    return total, breakdown


def commute_cost_monthly(listing, w):
    """Monetize commute: time at your valuation + transit/pass cost."""
    mins = listing.get("commute_min") or 0
    days = w.get("commute_days", 5)
    time_cost = mins * 2 * days * 4.33 * w.get("commute_cost_per_min", 0.0)
    fare = listing.get("transit_pass_monthly", 0) or 0
    return time_cost + fare


def income_ratio(total_monthly, w):
    income = w.get("net_monthly_income", 0)
    return (total_monthly / income) if income else None


# ---------------------------------------------------------------- report
def render_screen(listings, w, show_failed=True):
    survivors, failed = [], []
    for L in listings:
        reasons = hard_screen(L, w)
        (failed if reasons else survivors).append((L, reasons))
    print(f"Screened {len(listings)} listings "
          f"({len(survivors)} pass, {len(failed)} fail hard constraints)\n")
    if show_failed and failed:
        print("Failed hard constraints:")
        for L, reasons in failed:
            print(f"  ✗ {L.get('name', '?'):<24} {'; '.join(reasons)}")
        print()
    rows = []
    for L, _ in survivors:
        pct, detail = score(L, w)
        tm, bd = true_monthly(L, w)
        ratio = income_ratio(tm, w)
        rows.append((pct, tm, ratio, L, bd))
    rows.sort(key=lambda r: -r[0])
    print(f"{'#':<3}{'listing':<24}{'score':>7}{'true $/mo':>11}{'%income':>9}")
    for i, (pct, tm, ratio, L, _) in enumerate(rows, 1):
        r = f"{ratio * 100:.0f}%" if ratio else "-"
        print(f"{i:<3}{L.get('name', '?'):<24}{pct:>6.0f}%{tm:>10,.0f}{r:>9}")
    print()
    for i, (pct, tm, ratio, L, bd) in enumerate(rows, 1):
        print(f"#{i} {L.get('name', '?')} — {pct:.0f}% score, ${tm:,.0f}/mo all-in")
        top = sorted(bd.items(), key=lambda kv: -kv[1])[:4]
        print("   cost drivers: " + ", ".join(f"{k} ${v:,.0f}" for k, v in top if v))
        if L.get("notes"):
            print(f"   notes: {L['notes']}")
        print()
    return rows


def render_compare(listings, w):
    keys = ["rent", "sqm", "bedrooms", "commute_min", "deposit", "fees_monthly",
            "parking_monthly", "utilities_included", "pets_ok", "available",
            "floor", "lease_months"]
    names = [L.get("name", "?") for L in listings]
    print(f"{'field':<22}" + "".join(f"{n[:14]:>16}" for n in names))
    print("-" * (22 + 16 * len(names)))
    for k in keys:
        vals = []
        for L in listings:
            v = L.get(k, "-")
            if isinstance(v, bool):
                v = "yes" if v else "no"
            vals.append(str(v))
        print(f"{k:<22}" + "".join(f"{v[:14]:>16}" for v in vals))
    print()
    print(f"{'SCORE %':<22}", end="")
    scored = []
    for L in listings:
        pct, _ = score(L, w)
        scored.append(pct)
        print(f"{pct:>15.0f}%", end=" ")
    print()
    print(f"{'TRUE $/mo':<22}", end="")
    for L in listings:
        tm, _ = true_monthly(L, w)
        print(f"{tm:>15,.0f}", end=" ")
    print()
    winner = listings[scored.index(max(scored))].get("name", "?")
    cheapest = min(listings, key=lambda L: true_monthly(L, w)[0]).get("name", "?")
    print(f"\nBest score: {winner} | Cheapest all-in: {cheapest}")
    if winner != cheapest:
        for L in listings:
            if L.get("name") == winner:
                tw, _ = true_monthly(L, w)
                tc, _ = true_monthly(
                    next(x for x in listings if x.get("name") == cheapest), w)
                print(f"Premium for {winner} over {cheapest}: ${tw - tc:,.0f}/mo — "
                      f"is the quality difference worth it to you?")
    print()


# ---------------------------------------------------------------- budget
def render_budget(w):
    income = w.get("net_monthly_income", 0)
    debt = w.get("debt_payments", 0)
    print(f"Budget analysis (net income ${income:,}/mo, debt ${debt:,}/mo)")
    # classic ratios on gross-of-debt income
    avail = income - debt
    r30 = avail * 0.30
    r33 = avail * 0.33
    r50 = avail * 0.50
    print(f"  30% rule (conservative):  ${r30:,.0f}/mo rent")
    print(f"  33% (typical approvals):  ${r33:,.0f}/mo rent")
    print(f"  50% (danger line):        ${r50:,.0f}/mo — do not cross all-in")
    print()
    print("  Remember TRUE cost: rent + fees + utilities (~$140) + insurance (~$15)"
          " + parking + pet rent + commute.")
    print("  Landlords typically require gross income ≥ 3× rent (or 2.75× with"
          " good credit); if yours is below, prepare guarantor or extra deposit.")
    print("  Front costs: deposit + first (+ last) + broker/move-in fees —"
          " budget 2.5-3.5× monthly rent accessible on signing day.")
    return r30


# ---------------------------------------------------------------- negotiate
NEGOTIATION_PLAYS = {
    "vacant_days": "Unit sitting empty: every vacant month costs the landlord "
                   "≈ 8.3% of annual rent. Day-35 vacancy beats a 5% discount.",
    "lease_length": "Offering 18-24 months (or signing in the off-season "
                    "Nov-Feb) is worth real money to them: turnover costs "
                    "$2-4k (paint, cleaning, vacancy, leasing).",
    "move_in_speed": "Can you sign NOW and move in 3 days? Certainty is the "
                     "cheapest thing you can offer.",
    "winter_timing": "Winter leases (Nov-Feb) renew into winter next year — "
                     "landlords hate winter turnover; use this.",
    "comparables": "Same building/same layout listed lower is the single "
                   "strongest lever. Bring printouts.",
    "renewal_history": "If they mention turnover, ask what the last tenant "
                       "paid and why they left — answer guides your ask.",
    "fix_credit_story": "Income below 3×? Offer bigger deposit, guarantor, or "
                        "auto-pay enrollment instead of accepting a bump.",
    "amenity_fallback": "Can't move rent? Ask for: parking, storage unit, "
                        "in-unit washer, new paint, late-fee waiver — these "
                        "cost the landlord less than $50/mo each.",
}


def render_negotiate(listing, w, facts):
    """facts: dict of market signals (vacant_days, comparables, etc.).
    Returns the printed text (for tests)."""
    import io
    import contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        _negotiate_text(listing, w, facts)
    text = buf.getvalue()
    print(text, end="")
    return text


def _negotiate_text(listing, w, facts):
    rent = listing.get("rent", 0)
    print(f"Negotiation plan — {listing.get('name', '?')} at ${rent:,}/mo\n")
    levers = []
    for fact, present in facts.items():
        if present and fact in NEGOTIATION_PLAYS:
            levers.append(NEGOTIATION_PLAYS[fact])
    if not levers:
        levers = [NEGOTIATION_PLAYS["comparables"],
                  NEGOTIATION_PLAYS["lease_length"]]
    print("Your leverage:")
    for i, l in enumerate(levers, 1):
        print(f"  {i}. {l}")
    target_low = rent * 0.93
    target_high = rent * 0.97
    print(f"\nAsk: ${target_low:,.0f}/mo (7% under ask)")
    print(f"Walk-away deal: ${target_high:,.0f}/mo (3% under ask)")
    print(f"Value of holding firm: ${(rent - target_high) * 12:,.0f}/year")
    print(f"Value of full win:    ${(rent - target_low) * 12:,.0f}/year")
    print()
    print("Script opener:")
    print(f"  \"We love the unit and are ready to sign a "
          f"{facts.get('lease_offer', 18)}-month lease")
    print(f"   this week at ${target_low:,.0f}. Given [comparable/reason],")
    print("   can you make that work?\"")
    print("\nRules:")
    print("  • Anchor FIRST with a specific number — it sets the range.")
    print("  • Silence after your number. Do not fill it.")
    print("  • Trade, never beg: long lease / fast move-in / auto-pay for $.")
    print("  • Get any concession in writing on the lease, not verbal.")
    print("  • Fees (amenity, admin, 'technology') are softer than rent — "
          "always attack those second.")
    print()


# ---------------------------------------------------------------- sample
def sample_listings():
    return [
        {
            "name": "Maple St 2BR", "rent": 1850, "sqm": 68, "bedrooms": 2,
            "commute_min": 32, "deposit": 1850, "fees_monthly": 40,
            "parking_monthly": 100, "utilities_included": False,
            "pets_ok": True, "available": "2026-09-15", "floor": 3,
            "lease_months": 12, "broker_fee": 0,
            "notes": "top floor, corner unit, faces park",
            "scores": {"price": 3, "commute": 4, "space": 4, "light": 5,
                       "noise": 4, "kitchen": 3, "storage": 3, "bathroom": 3,
                       "building": 4, "neighbors": 4, "laundry": 5,
                       "safety": 4, "transit": 5, "pets_ok": 5,
                       "flex_space": 4, "outdoor": 3},
        },
        {
            "name": "Gallery Loft", "rent": 2100, "sqm": 55, "bedrooms": 1,
            "commute_min": 15, "deposit": 2100, "fees_monthly": 75,
            "parking_monthly": 0, "utilities_included": True,
            "pets_ok": True, "available": "2026-09-01", "floor": 8,
            "lease_months": 12, "broker_fee": 1500,
            "notes": "doorman building, gym, rooftop; thin walls rumored",
            "scores": {"price": 2, "commute": 5, "space": 2, "light": 5,
                       "noise": 2, "kitchen": 4, "storage": 2, "bathroom": 4,
                       "building": 5, "neighbors": 2, "laundry": 5,
                       "safety": 5, "transit": 5, "pets_ok": 3,
                       "flex_space": 2, "outdoor": 4},
        },
        {
            "name": "Oak Rd Garden", "rent": 1690, "sqm": 74, "bedrooms": 2,
            "commute_min": 52, "deposit": 1690, "fees_monthly": 0,
            "parking_monthly": 0, "utilities_included": False,
            "pets_ok": True, "available": "2026-10-01", "floor": 1,
            "lease_months": 12, "broker_fee": 0,
            "notes": "huge, quiet street, dated kitchen, needs car",
            "scores": {"price": 4, "commute": 2, "space": 5, "light": 3,
                       "noise": 5, "kitchen": 2, "storage": 5, "bathroom": 2,
                       "building": 2, "neighbors": 5, "laundry": 2,
                       "safety": 3, "transit": 1, "pets_ok": 5,
                       "flex_space": 3, "outdoor": 5},
        },
        {
            "name": "Vue Tower 1BR", "rent": 1780, "sqm": 48, "bedrooms": 1,
            "commute_min": 28, "deposit": 1780, "fees_monthly": 120,
            "parking_monthly": 150, "utilities_included": False,
            "pets_ok": False, "available": "2026-09-01", "floor": 12,
            "lease_months": 12, "broker_fee": 0,
            "notes": "fees are brutal; cat would be a dealbreaker",
            "scores": {"price": 4, "commute": 4, "space": 2, "light": 4,
                       "noise": 3, "kitchen": 3, "storage": 2, "bathroom": 3,
                       "building": 4, "neighbors": 3, "laundry": 4,
                       "safety": 4, "transit": 4, "pets_ok": 1,
                       "flex_space": 2, "outdoor": 2},
        },
    ]


def sample_weights():
    w = default_weights()
    w.update({"budget_monthly": 1900, "net_monthly_income": 6800,
              "debt_payments": 400, "max_commute_min": 55,
              "bedrooms_min": 1, "pets": True, "move_date": "2026-10-01"})
    return w


# ---------------------------------------------------------------- commands
def cmd_criteria(args):
    print("Build your weights file — answer for YOUR life (1 = don't care, "
          "5 = dealbreaker-ish):\n")
    w = default_weights()
    print(f"Current defaults written to {DEFAULT_WEIGHTS} — edit there, or:")
    print("  python3 apartment_scorecard.py criteria   # this guide\n")
    print(f"{'criterion':<14}{'default wt':>10}   1 looks like → 5 looks like")
    print("-" * 72)
    for key, q, _, wt, lo, hi in CRITERIA:
        print(f"{key:<14}{wt:>10}   {lo} → {hi}")
    print()
    print("Hard constraints (in weights file): budget_monthly, "
          "max_commute_min, bedrooms_min, pets, move_date")
    print("Money assumptions: utilities_estimate, renters_insurance, "
          "commute_cost_per_min (try 0.3-0.8 $/min), commute_days")


def cmd_screen(args):
    w = load_json(args.weights, create_with=default_weights())
    listings = load_listings(args.file)
    if not listings:
        print(f"No listings in {args.file}")
        sys.exit(1)
    render_screen(listings, w)


def cmd_compare(args):
    w = load_json(args.weights, create_with=default_weights())
    listings = load_listings(args.file)
    chosen = [L for L in listings if L.get("name") in args.names]
    if len(chosen) < 2:
        print(f"Need 2+ known names from {args.file}; have "
              f"{[L.get('name') for L in listings]}")
        sys.exit(1)
    render_compare(chosen, w)


def cmd_budget(args):
    w = load_json(args.weights, create_with=default_weights())
    render_budget(w)


def cmd_negotiate(args):
    w = load_json(args.weights, create_with=default_weights())
    listings = load_listings(args.file)
    L = next((x for x in listings if x.get("name") == args.name), None)
    if L is None:
        print(f"Listing '{args.name}' not in {args.file}")
        sys.exit(1)
    facts = {}
    for f in (args.facts or []):
        facts[f] = True
    if args.vacant_days:
        facts["vacant_days"] = args.vacant_days >= 21
    if args.lease_offer:
        facts["lease_length"] = args.lease_offer >= 18
    render_negotiate(L, w, facts)


def cmd_example(args):
    w = sample_weights()
    listings = sample_listings()
    print("=== EXAMPLE: hunting a 2BR with a cat, Oct 1 move, $1,900 budget ===\n")
    print("  (sample hunter nets $6,800/mo; a $1,850 ask needs the true-cost view)\n")
    print("--- Budget reality check ---\n")
    render_budget(w)
    print("\n--- Screen & rank 4 listings ---\n")
    rows = render_screen(listings, w)
    print("\n--- Head-to-head: top two ---\n")
    top_names = [rows[0][3].get("name"), rows[1][3].get("name")]
    render_compare([L for L in listings if L.get("name") in top_names], w)
    print("\n--- Negotiate the winner ---\n")
    render_negotiate(rows[0][3], w,
                     {"vacant_days": True, "lease_length": True,
                      "comparables": True, "move_in_speed": True})


def main():
    ap = argparse.ArgumentParser(
        prog="apartment_scorecard.py",
        description="Weighted apartment comparison with hard screening, true-cost "
                    "math, and negotiation prep. Pure stdlib.")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("criteria", help="guide to your weights file")
    sub.add_parser("example", help="self-contained demo")
    sub.add_parser("budget", help="affordability analysis")

    p = sub.add_parser("screen", help="score and rank listings")
    p.add_argument("--file", default=DEFAULT_LISTINGS)
    p.add_argument("--weights", default=DEFAULT_WEIGHTS)

    p = sub.add_parser("compare", help="side-by-side of named listings")
    p.add_argument("--file", default=DEFAULT_LISTINGS)
    p.add_argument("--weights", default=DEFAULT_WEIGHTS)
    p.add_argument("names", nargs="+")

    p = sub.add_parser("negotiate", help="negotiation plan for one listing")
    p.add_argument("--file", default=DEFAULT_LISTINGS)
    p.add_argument("--weights", default=DEFAULT_WEIGHTS)
    p.add_argument("name")
    p.add_argument("--facts", nargs="*", choices=list(NEGOTIATION_PLAYS),
                   help="market signals you know")
    p.add_argument("--vacant-days", type=int, help="how long unit is empty")
    p.add_argument("--lease-offer", type=int, help="lease length you'd sign")

    args = ap.parse_args()
    {"criteria": cmd_criteria, "screen": cmd_screen, "compare": cmd_compare,
     "budget": cmd_budget, "negotiate": cmd_negotiate,
     "example": cmd_example}[args.cmd](args)


if __name__ == "__main__":
    main()
