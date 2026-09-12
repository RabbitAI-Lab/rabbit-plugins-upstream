#!/usr/bin/env python3
"""
commute_opt.py — true cost of commuting: time, money, hybrid schedules, housing decisions.

Modes: car / transit / bike / walk / wfh. Pure stdlib. -h for usage.
"""
import argparse
import datetime as dt
import itertools
import json
import sys

# --------------------------- editable assumptions --------------------------
PARAMS = {
    # weekday rush multipliers (applied to off-peak time), Mon..Fri
    "profile": [1.28, 1.38, 1.42, 1.36, 1.22],
    "mode_rush": {"car": 1.40, "transit": 1.10, "bike": 1.00, "walk": 1.00, "wfh": 0.0},
    # vehicle $/mile
    "fuel_maint_per_mile": 0.24,     # fuel/electricity + maintenance + tires
    "ownership_per_mile": 0.23,      # depreciation + insurance/reg amortized
    "transit_fare": 2.75,            # per trip
    "transit_monthly_cap": 130.0,    # monthly pass price (auto-switch threshold)
    "bike_per_mile": 0.08,
    "weeks_per_year": 48,
    "default_hourly_rate": 30.0,     # after-tax $/h for time valuation
    "waking_hours_per_day": 16,
}
WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri"]

MODES = ["car", "transit", "bike", "walk", "wfh"]


def err(msg):
    sys.exit("error: " + msg)


def roundtrip_minutes(one_way_min, multiplier, mode):
    return one_way_min * multiplier * 2


def mode_cost_per_trip(mode, distance):
    """Return ($ per one-way trip, note)."""
    if mode == "car":
        per_mile = PARAMS["fuel_maint_per_mile"] + PARAMS["ownership_per_mile"]
        return distance * per_mile, f"car @ ${per_mile:.2f}/mi fully loaded"
    if mode == "transit":
        return PARAMS["transit_fare"], f"fare ${PARAMS['transit_fare']:.2f}"
    if mode == "bike":
        return distance * PARAMS["bike_per_mile"], "bike wear $0.08/mi"
    if mode == "walk":
        return 0.0, "walking"
    return 0.0, "WFH"


def annual_transit_fare(trips):
    """Monthly-cap logic: if 2x monthly cap is cheaper than pay-per-ride, use passes."""
    monthly_trips = trips / 12.0
    per_ride = monthly_trips * PARAMS["transit_fare"]
    cap = PARAMS["transit_monthly_cap"]
    if per_ride > 2 * cap:  # heuristic: heavy users should be on a pass
        return 12 * cap, "monthly pass"
    return trips * PARAMS["transit_fare"], "pay-per-ride"


def evaluate(offpeak, distance, mode, days, rate,
             parking_day=0.0, tolls_day=0.0, profile=None):
    """Full annual evaluation of one commute setup. Returns dict."""
    if mode not in MODES:
        err(f"mode '{mode}' not in {MODES}")
    profile = profile or PARAMS["profile"]
    weeks = PARAMS["weeks_per_year"]
    trips = days * weeks

    # per-weekday rush minutes (one-way) across the commuting week
    day_minutes = [offpeak * m * PARAMS["mode_rush"][mode] if i < days else 0.0
                   for i, m in enumerate(profile)]
    if mode == "wfh":
        day_minutes = [0.0] * 5
    avg_one_way = (sum(day_minutes) / days) if days else 0.0
    hours_yr = avg_one_way * 2 * trips / 60.0

    if mode == "transit":
        direct_yr, fare_note = annual_transit_fare(trips)
    else:
        per_trip, fare_note = mode_cost_per_trip(mode, distance)
        direct_yr = per_trip * 2 * trips
    direct_yr += (parking_day + tolls_day) * days * weeks

    time_yr = hours_yr * rate
    marginal = None
    if mode == "car":
        marginal = distance * 2 * trips * PARAMS["fuel_maint_per_mile"] \
            + (parking_day + tolls_day) * days * weeks
    waking_days_decade = hours_yr * 10 / PARAMS["waking_hours_per_day"]
    return dict(
        mode=mode, distance_mi=distance, days_per_week=days,
        trips_per_year=trips,
        avg_one_way_min=round(avg_one_way, 1),
        avg_roundtrip_min=round(avg_one_way * 2, 1),
        weekday_one_way_min={WEEKDAYS[i]: round(m, 1) for i, m in enumerate(day_minutes)},
        hours_per_year=round(hours_yr, 1),
        time_cost_per_year=round(time_yr, 0),
        direct_cost_per_year=round(direct_yr, 0),
        car_marginal_cost_per_year=None if marginal is None else round(marginal, 0),
        total_per_year=round(time_yr + direct_yr, 0),
        waking_days_per_decade=round(waking_days_decade, 1),
        fare_basis=fare_note,
    )


# --------------------------- subcommands -----------------------------------
def cmd_params(a):
    print("Editable assumptions (edit PARAMS in commute_opt.py):")
    for k, v in PARAMS.items():
        print(f"  {k:28} {v}")
    print("\nModes:", ", ".join(MODES))
    print("Weekday rush multipliers Mon..Fri:", PARAMS["profile"])


def cmd_profile(a):
    prof = parse_profile(a.profile) or PARAMS["profile"]
    print(f"RUSH PROFILE — {a.mode}, off-peak {a.offpeak} min one-way\n")
    print(f"{'DAY':<6}{'RUSH (one-way)':>16}{'ROUND TRIP':>12}")
    for i, dname in enumerate(WEEKDAYS):
        one = a.offpeak * prof[i] * PARAMS["mode_rush"][a.mode]
        print(f"{dname:<6}{one:>14.0f} min{one*2:>10.0f} min")
    print("\nMid-week peaks; Friday lightest PM peak (default FHWA-style pattern).")


def parse_profile(s):
    if not s:
        return None
    try:
        vals = [float(x) for x in s.split(",")]
        if len(vals) != 5:
            raise ValueError
        return vals
    except ValueError:
        err("--profile needs 5 comma-separated multipliers, e.g. 1.28,1.38,1.42,1.36,1.22")


def cmd_cost(a):
    r = evaluate(a.offpeak, a.distance, a.mode, a.days, a.rate,
                 a.parking, a.tolls, parse_profile(a.profile))
    if a.json:
        print(json.dumps(r, indent=2))
        return
    print(f"COMMUTE COST — {a.mode}, {a.offpeak:.0f} min off-peak, {a.distance} mi, "
          f"{a.days} d/wk @ ${a.rate:.0f}/h\n")
    print(f"  avg one-way (rush)      {r['avg_one_way_min']:.0f} min")
    print(f"  avg round trip          {r['avg_roundtrip_min']:.0f} min")
    print(f"  trips/year              {r['trips_per_year']}")
    print(f"  TIME                    {r['hours_per_year']:.0f} h/yr "
          f"(={r['waking_days_per_decade']:.0f} waking days/decade)")
    print(f"  time value              ${r['time_cost_per_year']:,.0f}/yr")
    print(f"  direct cost             ${r['direct_cost_per_year']:,.0f}/yr  [{r['fare_basis']}]")
    if r["car_marginal_cost_per_year"] is not None:
        print(f"    (car marginal-only   ${r['car_marginal_cost_per_year']:,.0f}/yr "
              f"— fuel+maint, no ownership)")
    print(f"  TOTAL                   ${r['total_per_year']:,.0f}/yr")


def cmd_compare(a):
    rows = []
    for m in MODES:
        ev = evaluate(a.offpeak, a.distance, m, a.days, a.rate,
                      a.parking, a.tolls, parse_profile(a.profile))
        rows.append((ev["total_per_year"], ev))
    rows.sort(key=lambda x: x[0])
    print(f"MODE COMPARISON — {a.distance} mi, off-peak {a.offpeak:.0f} min, "
          f"{a.days} d/wk @ ${a.rate:.0f}/h\n")
    print(f"{'MODE':<10}{'1-WAY':>7}{'HRS/YR':>8}{'TIME $':>10}{'DIRECT $':>10}{'TOTAL $':>10}")
    for _, r in rows:
        print(f"{r['mode']:<10}{r['avg_one_way_min']:>6.0f}m{r['hours_per_year']:>8.0f}"
              f"{r['time_cost_per_year']:>10,.0f}{r['direct_cost_per_year']:>10,.0f}"
              f"{r['total_per_year']:>10,.0f}")
    print("\nWFH assumes 0 min / $0 — the baseline every mode is judged against.")


def cmd_hybrid(a):
    if not 1 <= a.office_days <= 5:
        err("--office-days must be 1..5")
    prof = parse_profile(a.profile) or PARAMS["profile"]
    base = a.offpeak * PARAMS["mode_rush"][a.mode]
    subsets = list(itertools.combinations(range(5), a.office_days))
    scored = []
    for s in subsets:
        tot = sum(base * prof[i] for i in s)
        scored.append((tot, s))
    scored.sort()
    best_tot, best = scored[0]
    worst_tot, worst = scored[-1]
    mwf = tuple(i for i in (0, 2, 4) if i in range(5))[:a.office_days]
    if len(mwf) < a.office_days:
        mwf = tuple(sorted(set(list(mwf) + list(range(5))))[:a.office_days])
    mwf_tot = sum(base * prof[i] for i in mwf)
    names = lambda s: "/".join(WEEKDAYS[i] for i in s)
    print(f"HYBRID SCHEDULE — {a.office_days} office days, {a.mode}, "
          f"off-peak {a.offpeak:.0f} min\n")
    print(f"  best   {names(best):<12} {best_tot*2:>6.0f} min/wk round trip")
    print(f"  MWF    {names(mwf):<12} {mwf_tot*2:>6.0f} min/wk "
          f"(+{(mwf_tot-best_tot)*2:.0f} vs best)")
    print(f"  worst  {names(worst):<12} {worst_tot*2:>6.0f} min/wk "
          f"(+{(worst_tot-best_tot)*2:.0f} vs best)")
    print(f"\n  all {len(subsets)} subsets ranked:")
    for tot, s in scored:
        mark = " ← best" if s == best else (" ← MWF" if s == mwf else "")
        print(f"    {names(s):<12} {tot*2:>6.0f} min/wk{mark}")
    weekly_hr = best_tot * 2 / 60.0
    print(f"\n  best schedule over a year: {weekly_hr*PARAMS['weeks_per_year']:.0f} h/yr "
          f"commuting ({a.office_days}d/wk × {PARAMS['weeks_per_year']} wks)")


def parse_option(spec):
    parts = spec.split(",")
    if len(parts) < 2:
        err(f"bad option '{spec}' — need name,offpeak=MIN[,key=val...]")
    name = parts[0].strip()
    kv = dict(p.split("=", 1) for p in parts[1:] if "=" in p)
    try:
        return dict(
            name=name,
            offpeak=float(kv.get("offpeak", parts[1])),
            distance=float(kv.get("distance", 10)),
            mode=kv.get("mode", "car"),
            days=float(kv.get("days", 5)),
            extra_rent=float(kv.get("extra_rent", 0)),
            parking=float(kv.get("parking", 0)),
            tolls=float(kv.get("tolls", 0)),
        )
    except ValueError:
        err(f"bad numeric field in option '{spec}'")


def cmd_decide(a):
    if len(a.option) < 2:
        err("need at least 2 --option entries")
    opts = [parse_option(o) for o in a.option]
    results = []
    for o in opts:
        ev = evaluate(o["offpeak"], o["distance"], o["mode"], o["days"], a.rate,
                      o["parking"], o["tolls"])
        rent_yr = o["extra_rent"] * 12
        net_yr = ev["total_per_year"] + rent_yr
        results.append(dict(opt=o, ev=ev, rent_yr=rent_yr, net_yr=net_yr))
    base = results[0]["net_yr"]
    results.sort(key=lambda r: r["net_yr"])
    print(f"COMMUTE DECISION — {a.years} year horizon, ${a.rate:.0f}/h\n")
    print(f"{'OPTION':<28}{'HRS/YR':>8}{'$/YR TOTAL':>12}{'RENT Δ$/YR':>12}"
          f"{'NET $/YR':>10}{'vs BEST':>10}")
    for r in results:
        vs = r["net_yr"] - results[0]["net_yr"]
        print(f"{r['opt']['name'][:27]:<28}{r['ev']['hours_per_year']:>8.0f}"
              f"{r['ev']['total_per_year']:>12,.0f}{r['rent_yr']:>12,.0f}"
              f"{r['net_yr']:>10,.0f}{vs:>10,.0f}")
    print()
    for r in results[1:]:
        delta = r["net_yr"] - results[0]["net_yr"]
        o = r["opt"]
        if delta > 0:
            justify = -delta / 12.0
            print(f"  {o['name']}: needs ≥ ${justify:,.0f}/mo MORE rent savings "
                  f"to break even (currently ${o['extra_rent']:,.0f}/mo)")
        else:
            print(f"  {o['name']}: WINS by ${-delta:,.0f}/yr "
                  f"(${-delta*a.years:,.0f} over {a.years} yrs)")
    print(f"\n  lifespan view ({a.years} yrs):")
    for r in results:
        hrs = r["ev"]["hours_per_year"] * a.years
        print(f"    {r['opt']['name'][:27]:<28} {hrs:>7,.0f} h "
              f"(= {hrs/PARAMS['waking_hours_per_day']:.0f} waking days)")


# --------------------------- cli -------------------------------------------
def main():
    p = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("params").set_defaults(fn=cmd_params)

    sp = sub.add_parser("profile", help="weekday rush times")
    sp.add_argument("--offpeak", type=float, required=True)
    sp.add_argument("--mode", default="car", choices=MODES)
    sp.add_argument("--profile", help="5 comma multipliers Mon..Fri")
    sp.set_defaults(fn=cmd_profile)

    sp = sub.add_parser("cost", help="annual cost of one setup")
    sp.add_argument("--offpeak", type=float, required=True, help="off-peak one-way minutes")
    sp.add_argument("--distance", type=float, required=True, help="one-way miles")
    sp.add_argument("--mode", default="car", choices=MODES)
    sp.add_argument("--days", type=int, default=5)
    sp.add_argument("--rate", type=float, default=PARAMS["default_hourly_rate"])
    sp.add_argument("--parking", type=float, default=0.0, help="$ per day")
    sp.add_argument("--tolls", type=float, default=0.0, help="$ per day")
    sp.add_argument("--profile")
    sp.add_argument("--json", action="store_true")
    sp.set_defaults(fn=cmd_cost)

    sp = sub.add_parser("compare", help="all modes for one route")
    sp.add_argument("--offpeak", type=float, required=True)
    sp.add_argument("--distance", type=float, required=True)
    sp.add_argument("--days", type=int, default=5)
    sp.add_argument("--rate", type=float, default=PARAMS["default_hourly_rate"])
    sp.add_argument("--parking", type=float, default=0.0)
    sp.add_argument("--tolls", type=float, default=0.0)
    sp.add_argument("--profile")
    sp.set_defaults(fn=cmd_compare)

    sp = sub.add_parser("hybrid", help="best office weekdays")
    sp.add_argument("--offpeak", type=float, required=True)
    sp.add_argument("--mode", default="car", choices=MODES)
    sp.add_argument("--office-days", type=int, required=True)
    sp.add_argument("--profile")
    sp.set_defaults(fn=cmd_hybrid)

    sp = sub.add_parser("decide", help="compare housing/job options")
    sp.add_argument("--option", action="append", required=True,
                    help='"Name,offpeak=25,distance=12,mode=car,extra_rent=-450"')
    sp.add_argument("--rate", type=float, default=PARAMS["default_hourly_rate"])
    sp.add_argument("--years", type=int, default=5)
    sp.set_defaults(fn=cmd_decide)

    a = p.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
