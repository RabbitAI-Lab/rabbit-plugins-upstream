#!/usr/bin/env python3
"""
salary-negotiator — structured salary negotiation preparation.

Subcommands: offer | floor | compare | raise | demo

Runs offline; the user supplies market data (the output tells them which
sources to use). All figures are annual USD unless stated.
"""
import argparse
import json
import sys

# Die quietly on SIGPIPE when users pipe to head/less (e.g. `... | head`)
try:
    import signal
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
except (AttributeError, ValueError):
    pass  # non-POSIX platform

# Risk weights for variable comp components (documented assumptions)
P_BONUS_PAYOUT = 0.85      # target bonuses rarely pay 100%
RSU_RETENTION = 0.90       # ~10% of grants vesting are forfeited (leave early)
OPTION_VALUE_FACTOR = 0.15 # expected realized value of startup options vs paper value
BENEFIT_401K = "cash"      # 401k match counts as cash


def money(x):
    return f"${x:,.0f}"


# ── Market anchor ────────────────────────────────────────────────────────────
def build_anchor(market_min, market_med, market_max, leverage="medium"):
    """leverage: strong (competing offer / scarce skills) | medium | developing"""
    mult = {"strong": 1.07, "medium": 1.00, "developing": 0.93}[leverage]
    target = round(market_med * mult, -2)
    stretch = round(market_med + 0.65 * (market_max - market_med), -2)
    return {
        "market": (market_min, market_med, market_max),
        "target": target,
        "stretch": stretch,
        "rationale": {
            "strong": "competing offer / scarce-skill evidence justifies above-median",
            "medium": "at-median target keeps you credible and negotiable",
            "developing": "career-switcher positioning: at-market entry, renegotiate at 12mo",
        }[leverage],
    }


# ── Total comp EV ────────────────────────────────────────────────────────────
def comp_ev(base=0, bonus_pct=0, bonus_payout=P_BONUS_PAYOUT, signon=0,
            signon_years=3, rsu_annual=0, rsu_retention=RSU_RETENTION,
            match_pct=0, match_cap=0, options=0):
    """Expected annual value of a comp package."""
    parts = {"base": base}
    if bonus_pct:
        parts["bonus"] = round(base * bonus_pct / 100.0 * bonus_payout)
    if signon:
        parts["signon_amortized"] = round(signon / max(1, signon_years))
    if rsu_annual:
        parts["rsu"] = round(rsu_annual * rsu_retention)
    if match_pct:
        cap = match_cap if match_cap else base * match_pct / 100.0
        parts["401k_match"] = round(min(base * match_pct / 100.0, cap))
    if options:
        parts["options_risk_adjusted"] = round(options * OPTION_VALUE_FACTOR)
    total = sum(parts.values())
    return {"components": parts, "total_ev": total}


# ── Floor ────────────────────────────────────────────────────────────────────
def walk_away_floor(monthly_costs, runway_months, other_income=0, benefit_gap=0):
    """The salary below which the answer is no."""
    annual_costs = (monthly_costs + benefit_gap - other_income) * 12
    # gross up for ~22% effective tax+withholding (rough, US single filer)
    gross = annual_costs / 0.78
    return {
        "annual_costs": round(annual_costs),
        "gross_floor": round(gross, -2),
        "monthly_runway_note": f"6-month emergency cushion ≈ {money(monthly_costs * runway_months / 0.78)} gross",
    }


# ── Compare two packages ─────────────────────────────────────────────────────
def parse_pkg(spec):
    """Parse package descriptions like:
    'base 150k, bonus 15%, rsu 60k/yr, match 4%, signon 20k, options 80k'
    'startup: base 130k, options 0.5%, strike 1.50, valuation 60M'
    Returns kwargs for comp_ev().
    """
    import re
    s = spec.lower()

    def num_after(kword):
        """Value immediately after kword; '150k'/'60m' suffixes scale it."""
        m = re.search(rf"{kword}\s*\$?\s*([0-9]+(?:\.[0-9]+)?)\s*(k|m)?\b", s)
        if not m:
            return None
        v = float(m.group(1))
        if m.group(2) == "k":
            v *= 1_000
        elif m.group(2) == "m":
            v *= 1_000_000
        return v

    base = num_after("base") or 0
    bonus = num_after("bonus") or 0
    signon = num_after("signon") or 0
    rsu = num_after("rsu") or 0
    match = num_after("match") or 0

    # bonus/match given as small numbers are percentages of base
    bonus_pct = bonus if 0 < bonus < 100 else (bonus / base * 100 if base and bonus else 0)
    match_pct = match if 0 < match < 100 else 0

    # options: either a paper value ('options 80k') or a stake
    # ('options 0.5%, valuation 60M' -> pct * valuation / 4yr vest)
    options = num_after("options") or 0
    if 0 < options < 100:  # looks like a percentage stake, not dollars
        val = num_after("valuation") or 0
        if val:
            strike_note = num_after("strike") or 0
            shares_value = options / 100.0 * val
            # subtract strike cost if both strike and valuation given (per-share × implied shares)
            options = max(0.0, shares_value / 4.0)  # annualized over 4-year vest
        else:
            options = 0  # percent without valuation is unquantifiable
    else:
        options = options / 4.0 if options else 0  # paper/yr from total grant

    return {"base": base, "bonus_pct": bonus_pct, "signon": signon,
            "rsu_annual": rsu, "match_pct": match_pct, "options": options}


def compare_packages(a, b, years=3):
    eva = comp_ev(**a)
    evb = comp_ev(**b)
    rows = []
    keys = sorted(set(eva["components"]) | set(evb["components"]))
    rows.append(("component", "A", "B"))
    for k in keys:
        rows.append((k, money(eva["components"].get(k, 0)), money(evb["components"].get(k, 0))))
    # year-1 cash (base + bonus + signon) vs later years
    def y1_cash(pkg, ev):
        bonus = ev["components"].get("bonus", 0)
        return pkg["base"] + bonus + pkg.get("signon", 0)
    def yn_cash(pkg, ev):
        return pkg["base"] + ev["components"].get("bonus", 0)
    a1, b1 = y1_cash(a, eva), y1_cash(b, evb)
    an, bn = yn_cash(a, eva), yn_cash(b, evb)
    multi_a = a1 + yn_cash(a, eva) * (years - 1)
    multi_b = b1 + yn_cash(b, evb) * (years - 1)
    return {
        "a_ev": eva["total_ev"], "b_ev": evb["total_ev"],
        "a_y1_cash": a1, "b_y1_cash": b1,
        f"a_{years}yr_cash": multi_a, f"b_{years}yr_cash": multi_b,
        "ev_delta": eva["total_ev"] - evb["total_ev"],
        "cash_y1_delta": a1 - b1,
        "components_a": eva["components"], "components_b": evb["components"],
    }


# ── Scripts ─────────────────────────────────────────────────────────────────
def offer_script(role, target, stretch, tone="collaborative-firm"):
    if tone == "collaborative-firm":
        return f"""SCRIPT — {role} offer, round 1 ({tone})
1. Thank genuinely, buy time:
   "Thank you — I'm genuinely excited about this role and the team.
    I'd like a day to review the full package properly."
2. The counter (next call — enthusiasm, then ONE number, then SILENCE):
   "I've done my research on this scope for [location/level]: market
    medians run around [market median]. Given [your specific qualification
    — metric, scale, or scarce skill], I was targeting {money(target)}.
    Is there flexibility to get there?"
   ▸ Say the number. Stop talking. Let the silence work.
3. If "that's above the band":
   "I understand bands are real. If base is capped, I'm open to solving it
    with [sign-on / an equity refresh / a 6-month review with criteria] —
    which of those has the most room?"
4. If they move to {money(stretch)} or near it:
   "That works. Can you send the updated package in writing today?"
5. Never:
   × give a range (they hear the low end)
   × apologize for the number ("I know it's a lot but...")
   × accept verbally on the first call
"""
    return "tone not implemented — use collaborative-firm"


def raise_script(current, market_med, ask, impact):
    pct = round((ask / current - 1) * 100)
    return f"""SCRIPT — raise conversation (from {money(current)} → ask {money(ask)}, +{pct}%)
1. Frame (schedule a dedicated meeting, not a hallway):
   "I'd like to talk about my compensation. I've taken on significantly
    expanded scope this year, and I want to walk through it."
2. Evidence (2 minutes max, metrics not adjectives):
   "{impact}"
   "Market data for this scope puts the median around {money(market_med)};
    I'm currently at {money(current)}."
3. The ask (one number):
   "Based on that, I'm asking for {money(ask)}."
   ▸ Then silence. Do not fill it.
4. If "budget is fixed this cycle":
   "I hear that. Can we agree in writing to [review on DATE] with
    [explicit criteria], plus [title change / equity refresh] now?
    I want a path, not a maybe."
5. If "you need to develop more":
   "That's fair feedback — can we make it concrete? What specifically
    would justify {money(ask)}, and by when?"
6. Follow up in writing same day:
   "Summarizing our conversation: [ask] / [criteria] / [date]..."
"""


def pushback_qa(target, levers):
    return f"""PUSHBACK Q&A (rehearse out loud)
Q: "The band for this level caps at [X]."
A: "Understood — then let's solve it across the package: sign-on,
   an equity refresh, or a performance bonus with explicit criteria.
   Which has the most room?" (levers: {levers})

Q: "We need you at this level first; revisit in a year."
A: "Happy to — can we set the criteria and date in writing now?
   What does the next level look like, concretely?"

Q: "Others on the team are at this level too."
A: "My ask reflects [specific scope/metric] and market medians —
   not comparisons. Is {money(target)} within policy for the
   scope I've described?"

Q: "This is our final offer."
A: (real final vs. bluff) "I appreciate you pushing on it. If it's truly
   final, I'll decide within [24-48h]." — then actually be ready to
   accept or walk per your floor.
"""


# ── Subcommands ─────────────────────────────────────────────────────────────
def cmd_offer(args):
    anchor = build_anchor(args.market_min, args.market_med, args.market_max, args.leverage)
    ev = comp_ev(base=args.offer_base, bonus_pct=args.offer_bonus or 0,
                 signon=args.offer_signon or 0, rsu_annual=args.offer_rsu or 0,
                 match_pct=args.offer_match or 0)
    t, s = anchor["target"], anchor["stretch"]
    m0, m1, m2 = anchor["market"]
    base_vs_med = (args.offer_base / m1 - 1) * 100 if m1 else 0
    print(f"NEGOTIATION STRATEGY — {args.role}" + (f" ({args.location})" if args.location else ""))
    print("=" * 64)
    print("MARKET ANCHOR")
    print(f"  Market: {money(m0)} — {money(m1)} — {money(m2)} (min/med/max)")
    print(f"  Target:  {money(t)}   ({anchor['rationale']})")
    print(f"  Stretch: {money(s)}   (p75-ish; justify with specific leverage)")
    if args.floor:
        print(f"  Floor:   {money(args.floor)}   (your walk-away — never go below)")
    print()
    print("OFFER EVALUATION (expected value, risk-weighted)")
    for k, v in ev["components"].items():
        print(f"  {k:<18} {money(v)}")
    print(f"  {'TOTAL COMP EV':<18} {money(ev['total_ev'])}")
    verdict = "BELOW your target" if ev["total_ev"] < t else "at/ABOVE your target"
    print(f"  vs target {money(t)}: {verdict}")
    if abs(base_vs_med) >= 5:
        direction = "below" if base_vs_med < 0 else "above"
        print(f"  ⚠ Base is {abs(base_vs_med):.0f}% {direction} market median → negotiate BASE specifically.")
    print()
    print(offer_script(args.role, t, s))
    levers = "sign-on, equity refresh, review-in-6mo with criteria, PTO, title, remote stipend"
    print(pushback_qa(t, levers))
    print("Market sources to verify: levels.fyi (tech), Glassdoor, LinkedIn Salary,")
    print("Payscale, and — best — two recruiters in the niche. Use >=3 sources.")
    return 0


def cmd_floor(args):
    f = walk_away_floor(args.monthly_costs, args.runway_months, args.other_income, args.benefit_gap)
    print("WALK-AWAY FLOOR")
    print("=" * 64)
    print(f"  Annual net needs (costs + benefit gap - other income): {money(f['annual_costs'])}")
    print(f"  Grossed up (~22% effective tax): {money(f['gross_floor'])}  ← YOUR FLOOR")
    print(f"  {f['monthly_runway_note']}")
    print()
    print("  Usage: below this number, the answer is no — regardless of how")
    print("  nice the team is. Knowing it converts 'no' from an argument to a fact.")
    return 0


def cmd_compare(args):
    a = parse_pkg(args.a)
    b = parse_pkg(args.b)
    c = compare_packages(a, b)
    print("PACKAGE COMPARISON (risk-weighted EV)")
    print("=" * 64)
    print(f"{'component':<22}{'A':>14}{'B':>14}")
    keys = sorted(set(c["components_a"]) | set(c["components_b"]))
    for k in keys:
        print(f"  {k:<20}{money(c['components_a'].get(k, 0)):>14}{money(c['components_b'].get(k, 0)):>14}")
    print(f"  {'TOTAL EV':<20}{money(c['a_ev']):>14}{money(c['b_ev']):>14}")
    print(f"  {'Year-1 cash':<20}{money(c['a_y1_cash']):>14}{money(c['b_y1_cash']):>14}")
    print(f"  {'3-year cash':<20}{money(c['a_3yr_cash']):>14}{money(c['b_3yr_cash']):>14}")
    winner = "A" if c["a_ev"] > c["b_ev"] else "B"
    print()
    print(f"  EV winner: {winner} by {money(abs(c['ev_delta']))}/yr")
    print(f"  Year-1 cash winner: {'A' if c['cash_y1_delta'] > 0 else 'B'} by {money(abs(c['cash_y1_delta']))}")
    print()
    print("  Notes: options are discounted to 15% of paper value (most startups'")
    print("  options expire worthless); RSUs at 90% (forfeiture risk); bonuses at")
    print("  85% payout. Adjust if you have better information about THIS company.")
    return 0


def cmd_raise(args):
    pct = (args.ask / args.current - 1) * 100
    print(raise_script(args.current, args.market_med, args.ask, args.impact))
    print(f"Ask: {money(args.ask)} (+{pct:.0f}% from {money(args.current)}; market median {money(args.market_med)})")
    return 0


def cmd_demo(args):
    print("=== DEMO 1: offer strategy ===")
    cmd_offer(argparse.Namespace(
        role="Senior Backend Engineer", location="Remote US", leverage="strong",
        offer_base=145000, offer_bonus=10, offer_signon=15000, offer_rsu=40000,
        offer_match=0, market_min=130000, market_med=160000, market_max=210000,
        floor=151000))
    print()
    print("=== DEMO 2: walk-away floor ===")
    cmd_floor(argparse.Namespace(monthly_costs=4200, runway_months=6,
                                 other_income=0, benefit_gap=500))
    print()
    print("=== DEMO 3: two offers, different shapes ===")
    cmd_compare(argparse.Namespace(
        a="BigCo: base 150k, bonus 15%, rsu 60k, match 4%",
        b="Startup: base 130k, options 80k"))
    print()
    print("=== DEMO 4: raise script ===")
    cmd_raise(argparse.Namespace(current=95000, market_med=115000,
                                 impact="shipped X (+12% activation), led Y migration solo",
                                 ask=108000))


def main():
    p = argparse.ArgumentParser(description="salary-negotiator: structured negotiation prep")
    sub = p.add_subparsers(dest="cmd")
    o = sub.add_parser("offer", help="full strategy for a job offer")
    o.add_argument("--role", required=True)
    o.add_argument("--location")
    o.add_argument("--leverage", default="medium", choices=["strong", "medium", "developing"])
    o.add_argument("--offer-base", type=float, required=True)
    o.add_argument("--offer-bonus", type=float, help="percent")
    o.add_argument("--offer-signon", type=float)
    o.add_argument("--offer-rsu", type=float, help="annual grant value")
    o.add_argument("--offer-match", type=float, help="401k match percent")
    o.add_argument("--market-min", type=float, required=True)
    o.add_argument("--market-med", type=float, required=True)
    o.add_argument("--market-max", type=float, required=True)
    o.add_argument("--floor", type=float, help="your walk-away from the floor command")
    f = sub.add_parser("floor", help="walk-away floor from personal finances")
    f.add_argument("--monthly-costs", type=float, required=True)
    f.add_argument("--runway-months", type=int, default=6)
    f.add_argument("--other-income", type=float, default=0)
    f.add_argument("--benefit-gap", type=float, default=0, help="monthly value of benefits you'd lose/gain")
    c = sub.add_parser("compare", help="compare two packages")
    c.add_argument("--a", required=True, help="'base 150k, bonus 15%, rsu 60k, match 4%, signon 20k, options 80k'")
    c.add_argument("--b", required=True)
    r = sub.add_parser("raise", help="raise conversation script")
    r.add_argument("--current", type=float, required=True)
    r.add_argument("--market-med", type=float, required=True)
    r.add_argument("--impact", required=True)
    r.add_argument("--ask", type=float, required=True)
    sub.add_parser("demo")
    args = p.parse_args()
    if args.cmd == "offer":
        return cmd_offer(args)
    if args.cmd == "floor":
        return cmd_floor(args)
    if args.cmd == "compare":
        return cmd_compare(args)
    if args.cmd == "raise":
        return cmd_raise(args)
    if args.cmd == "demo":
        return cmd_demo(args)
    p.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
