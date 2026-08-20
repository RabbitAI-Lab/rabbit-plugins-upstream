#!/usr/bin/env python3
"""
Utility Bill Analyzer — detect anomalies, compare usage, and suggest savings.
Pure Python stdlib only. JSON file as database.

Usage:
  python3 bill_analyzer.py add --type electricity --date 2025-01-15 --usage 450 --cost 67.50
  python3 bill_analyzer.py history
  python3 bill_analyzer.py compare --month 01
  python3 bill_analyzer.py anomaly
  python3 bill_analyzer.py forecast
  python3 bill_analyzer.py report
"""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta
from statistics import mean

# ---------------------------------------------------------------------------
# Database helpers
# ---------------------------------------------------------------------------

DEFAULT_DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bills.json")

SEASON_MAP = {
    12: "winter", 1: "winter", 2: "winter",
    3: "spring", 4: "spring", 5: "spring",
    6: "summer", 7: "summer", 8: "summer",
    9: "autumn", 10: "autumn", 11: "autumn",
}


def load_db(db_path):
    """Load the bill database from JSON file."""
    if not os.path.exists(db_path):
        return []
    with open(db_path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_db(bills, db_path):
    """Save the bill database to JSON file."""
    with open(db_path, "w", encoding="utf-8") as f:
        json.dump(bills, f, indent=2, sort_keys=True)


# ---------------------------------------------------------------------------
# Core domain logic
# ---------------------------------------------------------------------------

def get_season(month_int):
    """Return season name for a month integer (1-12)."""
    return SEASON_MAP.get(month_int, "unknown")


def cost_per_unit(usage, cost):
    """Calculate cost per unit of usage."""
    if usage <= 0:
        return 0.0
    return round(cost / usage, 4)


def sort_bills(bills):
    """Return bills sorted by date ascending."""
    return sorted(bills, key=lambda b: b["date"])


def filter_by_type(bills, util_type):
    """Filter bills by utility type."""
    if not util_type:
        return bills
    return [b for b in bills if b["type"].lower() == util_type.lower()]


def rolling_average(bills, index, window=3):
    """Calculate rolling average of usage for a window of prior bills."""
    start = max(0, index - window)
    window_bills = bills[start:index]
    if not window_bills:
        return 0.0
    return mean(b["usage"] for b in window_bills)


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_add(args):
    """Record a new utility bill."""
    bills = load_db(args.db)

    # Parse date
    try:
        dt = datetime.strptime(args.date, "%Y-%m-%d")
    except ValueError:
        print(f"Error: Invalid date '{args.date}'. Use YYYY-MM-DD format.")
        return 1

    if args.usage <= 0:
        print("Error: Usage must be positive.")
        return 1
    if args.cost <= 0:
        print("Error: Cost must be positive.")
        return 1

    bill = {
        "type": args.type.lower(),
        "date": args.date,
        "month": dt.month,
        "year": dt.year,
        "usage": args.usage,
        "cost": round(args.cost, 2),
        "cpu": cost_per_unit(args.usage, args.cost),
        "season": get_season(dt.month),
    }

    bills.append(bill)
    bills = sort_bills(bills)
    save_db(bills, args.db)

    print(f"✓ Added {bill['type']} bill for {bill['date']}: "
          f"{bill['usage']} units, ${bill['cost']:.2f} "
          f"(${bill['cpu']:.4f}/unit)")
    return 0


def cmd_history(args):
    """Show usage and cost trend."""
    bills = load_db(args.db)
    bills = filter_by_type(bills, args.type)
    if not bills:
        print("No bills recorded.")
        return 1

    bills = sort_bills(bills)
    print(f"\n{'Date':<12} {'Type':<12} {'Usage':>8} {'Cost':>9} {'$/unit':>8} {'Season':<8} Bar")
    print("-" * 78)

    max_usage = max(b["usage"] for b in bills)
    for b in bills:
        bar_len = int((b["usage"] / max_usage) * 40) if max_usage > 0 else 0
        bar = "█" * bar_len
        print(f"{b['date']:<12} {b['type']:<12} {b['usage']:>8} "
              f"{b['cost']:>8.2f} {b['cpu']:>8.4f} {b['season']:<8} {bar}")

    print(f"\nTotal: {len(bills)} bills, "
          f"{sum(b['usage'] for b in bills)} units, "
          f"${sum(b['cost'] for b in bills):.2f}")
    return 0


def cmd_compare(args):
    """Compare a month's usage to the same month in the prior year."""
    bills = load_db(args.db)
    bills = filter_by_type(bills, args.type)
    if not bills:
        print("No bills recorded.")
        return 1

    month = int(args.month)
    years = sorted(set(b["year"] for b in bills))

    if len(years) < 2:
        print(f"Need at least 2 years of data to compare. Found {len(years)}.")
        return 1

    latest_year = years[-1]
    prior_year = years[-2]

    latest = [b for b in bills if b["year"] == latest_year and b["month"] == month]
    prior = [b for b in bills if b["year"] == prior_year and b["month"] == month]

    if not latest:
        print(f"No bill found for month {month:02d}/{latest_year}.")
        return 1
    if not prior:
        print(f"No bill found for month {month:02d}/{prior_year}.")
        return 1

    print(f"\n=== Month {month:02d} Comparison: {prior_year} → {latest_year} ===\n")
    for utype in sorted(set(b["type"] for b in latest + prior)):
        l = [b for b in latest if b["type"] == utype]
        p = [b for b in prior if b["type"] == utype]
        if not l or not p:
            continue
        lb, pb = l[0], p[0]
        usage_diff = lb["usage"] - pb["usage"]
        usage_pct = (usage_diff / pb["usage"] * 100) if pb["usage"] else 0
        cost_diff = lb["cost"] - pb["cost"]
        cost_pct = (cost_diff / pb["cost"] * 100) if pb["cost"] else 0
        cpu_diff = lb["cpu"] - pb["cpu"]
        cpu_pct = (cpu_diff / pb["cpu"] * 100) if pb["cpu"] else 0

        print(f"  [{utype.upper()}]")
        print(f"    Usage:     {pb['usage']:g} → {lb['usage']:g}  ({usage_diff:+.1f}, {usage_pct:+.1f}%)")
        print(f"    Cost:      ${pb['cost']:.2f} → ${lb['cost']:.2f}  ({cost_diff:+.2f}, {cost_pct:+.1f}%)")
        print(f"    $/unit:    ${pb['cpu']:.4f} → ${lb['cpu']:.4f}  ({cpu_diff:+.4f}, {cpu_pct:+.1f}%)")

        if usage_pct > 15:
            print(f"    ⚠ Usage up {usage_pct:.1f}% — check for leaks, appliance issues, or behavior change.")
        elif usage_pct < -15:
            print(f"    ✓ Usage down {abs(usage_pct):.1f}% — great improvement!")
        if cpu_pct > 10:
            print(f"    ⚠ Rate increased {cpu_pct:.1f}% — consider switching plans or providers.")
    return 0


def cmd_anomaly(args):
    """Detect bills with usage >1.5× the rolling average."""
    bills = load_db(args.db)
    bills = filter_by_type(bills, args.type)
    if not bills:
        print("No bills recorded.")
        return 1

    bills = sort_bills(bills)
    anomalies = []

    for i, b in enumerate(bills):
        avg = rolling_average(bills, i, window=3)
        if avg > 0 and b["usage"] > avg * 1.5:
            ratio = b["usage"] / avg if avg else 0
            anomalies.append((b, avg, ratio))

    if not anomalies:
        print("No anomalies detected. All bills within 1.5× rolling average.")
        return 0

    print(f"\n⚠ {len(anomalies)} ANOMALY(IES) DETECTED:\n")
    for b, avg, ratio in anomalies:
        print(f"  {b['date']} [{b['type']}] Usage: {b['usage']} "
              f"(avg was {avg:.0f}, {ratio:.1f}× normal)")
        if b["season"] == "winter":
            print(f"    → Winter spike — heating load? Check insulation, thermostat settings.")
        elif b["season"] == "summer":
            print(f"    → Summer spike — AC load? Check cooling efficiency, seals.")
        else:
            print(f"    → Check for leaks, faulty appliances, or billing errors.")
    return 0


def cmd_forecast(args):
    """Predict next bill based on seasonal averages and recent trend."""
    bills = load_db(args.db)
    bills = filter_by_type(bills, args.type)
    if not bills:
        print("No bills recorded.")
        return 1

    bills = sort_bills(bills)
    last = bills[-1]
    next_month = last["month"] % 12 + 1
    if last["month"] == 12:
        next_year = last["year"] + 1
    else:
        next_year = last["year"]

    next_season = get_season(next_month)

    # Gather same-month historical data per type
    print(f"\n=== Forecast for {next_year}-{next_month:02d} ({next_season}) ===\n")
    utypes = sorted(set(b["type"] for b in bills))
    for utype in utypes:
        tbills = [b for b in bills if b["type"] == utype]
        same_month = [b for b in tbills if b["month"] == next_month]
        recent = tbills[-3:] if len(tbills) >= 3 else tbills

        if same_month:
            pred_usage = mean(b["usage"] for b in same_month)
            pred_cpu = mean(b["cpu"] for b in same_month)
            method = f"avg of {len(same_month)} historical {next_month:02d}-month bills"
        else:
            pred_usage = mean(b["usage"] for b in recent)
            pred_cpu = mean(b["cpu"] for b in recent)
            method = f"avg of last {len(recent)} bills (no same-month data)"

        pred_cost = pred_usage * pred_cpu
        print(f"  [{utype.upper()}]")
        print(f"    Predicted usage: {pred_usage:.0f} units")
        print(f"    Predicted cost:  ${pred_cost:.2f}")
        print(f"    Est. rate:       ${pred_cpu:.4f}/unit")
        print(f"    Method: {method}\n")
    return 0


def cmd_report(args):
    """Generate annual summary with savings suggestions."""
    bills = load_db(args.db)
    bills = filter_by_type(bills, args.type)
    if not bills:
        print("No bills recorded.")
        return 1

    bills = sort_bills(bills)
    years = sorted(set(b["year"] for b in bills))
    latest_year = years[-1]
    year_bills = [b for b in bills if b["year"] == latest_year]

    print(f"\n{'='*60}")
    print(f"  ANNUAL REPORT — {latest_year}")
    print(f"{'='*60}\n")

    for utype in sorted(set(b["type"] for b in year_bills)):
        ubills = [b for b in year_bills if b["type"] == utype]
        total_usage = sum(b["usage"] for b in ubills)
        total_cost = sum(b["cost"] for b in ubills)
        avg_cpu = total_cost / total_usage if total_usage else 0
        avg_usage = mean(b["usage"] for b in ubills)
        max_bill = max(ubills, key=lambda b: b["usage"])
        min_bill = min(ubills, key=lambda b: b["usage"])

        print(f"  [{utype.upper()}]")
        print(f"    Bills this year:   {len(ubills)}")
        print(f"    Total usage:       {total_usage} units")
        print(f"    Total cost:        ${total_cost:.2f}")
        print(f"    Average usage:     {avg_usage:.0f} units/bill")
        print(f"    Average rate:      ${avg_cpu:.4f}/unit")
        print(f"    Peak month:        {max_bill['date']} ({max_bill['usage']} units, {max_bill['season']})")
        print(f"    Low month:         {min_bill['date']} ({min_bill['usage']} units, {min_bill['season']})")

        # Seasonal breakdown
        seasons = {}
        for b in ubills:
            seasons.setdefault(b["season"], []).append(b["usage"])
        print(f"    Seasonal avg:")
        for s in ["winter", "spring", "summer", "autumn"]:
            if s in seasons:
                print(f"      {s:<8}: {mean(seasons[s]):.0f} units")
        print()

    # Savings suggestions
    print(f"{'='*60}")
    print("  SAVINGS SUGGESTIONS")
    print(f"{'='*60}\n")
    suggestions = generate_suggestions(bills)
    for i, s in enumerate(suggestions, 1):
        print(f"  {i}. {s}")

    # Year-over-year comparison
    if len(years) >= 2:
        prior_year = years[-2]
        print(f"\n{'='*60}")
        print(f"  YEAR-OVER-YEAR: {prior_year} → {latest_year}")
        print(f"{'='*60}\n")
        for utype in sorted(set(b["type"] for b in bills)):
            curr = [b for b in bills if b["year"] == latest_year and b["type"] == utype]
            prev = [b for b in bills if b["year"] == prior_year and b["type"] == utype]
            if not curr or not prev:
                continue
            cu, pu = sum(b["usage"] for b in curr), sum(b["usage"] for b in prev)
            cc, pc = sum(b["cost"] for b in curr), sum(b["cost"] for b in prev)
            print(f"  [{utype.upper()}]")
            print(f"    Usage: {pu:g} → {cu:g} ({cu-pu:+.1f}, {((cu-pu)/pu*100) if pu else 0:+.1f}%)")
            print(f"    Cost:  ${pc:.2f} → ${cc:.2f} ({cc-pc:+.2f})")
            print()
    return 0


# ---------------------------------------------------------------------------
# Savings suggestion engine
# ---------------------------------------------------------------------------

def generate_suggestions(bills):
    """Generate savings suggestions based on usage patterns."""
    suggestions = []
    bills = sort_bills(bills)

    # Group by type
    by_type = {}
    for b in bills:
        by_type.setdefault(b["type"], []).append(b)

    for utype, tbills in by_type.items():
        total_cost = sum(b["cost"] for b in tbills)
        avg_usage = mean(b["usage"] for b in tbills)
        max_bill = max(tbills, key=lambda b: b["usage"])

        # Check for anomalies
        for i, b in enumerate(tbills):
            avg = rolling_average(tbills, i)
            if avg > 0 and b["usage"] > avg * 1.5:
                suggestions.append(
                    f"[{utype}] Investigate {b['date']} spike "
                    f"({b['usage']} units vs {avg:.0f} avg) — possible leak or malfunction."
                )

        # Seasonal analysis
        winter = [b for b in tbills if b["season"] == "winter"]
        summer = [b for b in tbills if b["season"] == "summer"]

        if utype == "electricity":
            if winter and mean(b["usage"] for b in winter) > avg_usage * 1.2:
                suggestions.append(
                    "[electricity] Winter usage is high — consider: "
                    "programmable thermostat (lower when away/sleeping), "
                    "seal drafty windows/doors, add insulation, "
                    "use LED bulbs, service heating system annually."
                )
            if summer and mean(b["usage"] for b in summer) > avg_usage * 1.2:
                suggestions.append(
                    "[electricity] Summer AC usage is high — consider: "
                    "set AC to 24-26°C, use ceiling fans, "
                    "close blinds during peak sun, service AC unit, "
                    "seal ducts, use a smart thermostat."
                )
            suggestions.append(
                "[electricity] Switch to LED bulbs (75% less energy than incandescent)."
            )
            suggestions.append(
                "[electricity] Unplug vampire electronics or use smart power strips."
            )

        elif utype == "gas":
            if winter and mean(b["usage"] for b in winter) > avg_usage * 1.2:
                suggestions.append(
                    "[gas] Winter heating is the biggest cost — consider: "
                    "lower thermostat 1-2°C, insulate hot water pipes, "
                    "service furnace, weatherstrip doors, add attic insulation."
                )
            suggestions.append(
                "[gas] Lower water heater temperature to 50°C (120°F) to save 4-22% annually."
            )

        elif utype == "water":
            suggestions.append(
                "[water] Fix dripping faucets — a drip/sec wastes 1,300+ gallons/year."
            )
            suggestions.append(
                "[water] Install low-flow showerheads and faucet aerators."
            )
            suggestions.append(
                "[water] Run dishwasher and washing machine only with full loads."
            )

        # Rate trend analysis
        if len(tbills) >= 4:
            recent_cpu = mean(b["cpu"] for b in tbills[-3:])
            older_cpu = mean(b["cpu"] for b in tbills[:3])
            if recent_cpu > older_cpu * 1.1:
                pct = (recent_cpu - older_cpu) / older_cpu * 100
                suggestions.append(
                    f"[{utype}] Rate increased {pct:.1f}% — compare plans from "
                    f"competing providers; consider fixed-rate or off-peak plans."
                )
            elif recent_cpu < older_cpu * 0.9:
                suggestions.append(
                    f"[{utype}] Rate decreased — your current plan is competitive."
                )

    if not suggestions:
        suggestions.append("Your usage is stable and within normal ranges. Keep it up!")
        suggestions.append("Review the utility-savings-checklist.md for more optimization tips.")

    return suggestions


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Utility Bill Analyzer — detect anomalies, compare usage, suggest savings.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Example:\n"
               "  python3 bill_analyzer.py add --type electricity --date 2025-01-15 --usage 450 --cost 67.50\n"
               "  python3 bill_analyzer.py history\n"
               "  python3 bill_analyzer.py report\n",
    )
    parser.add_argument("--db", default=DEFAULT_DB, help="Path to bills JSON database (default: bills.json next to script)")
    sub = parser.add_subparsers(dest="command", required=True)

    # add
    p_add = sub.add_parser("add", help="Record a new bill")
    p_add.add_argument("--type", required=True, choices=["electricity", "water", "gas"],
                       help="Utility type")
    p_add.add_argument("--date", required=True, help="Bill date YYYY-MM-DD")
    p_add.add_argument("--usage", required=True, type=float,
                       help="Usage in kWh (electricity) or m³ (water/gas)")
    p_add.add_argument("--cost", required=True, type=float, help="Total cost")

    # history
    p_hist = sub.add_parser("history", help="Show usage/cost trend with ASCII bar chart")
    p_hist.add_argument("--type", choices=["electricity", "water", "gas"], default=None, help="Filter by utility type")

    # compare
    p_cmp = sub.add_parser("compare", help="Compare same month across years")
    p_cmp.add_argument("--month", required=True, help="Month number 01-12")
    p_cmp.add_argument("--type", choices=["electricity", "water", "gas"], default=None, help="Filter by utility type")

    # anomaly
    p_anom = sub.add_parser("anomaly", help="Detect bills >1.5× rolling average")
    p_anom.add_argument("--type", choices=["electricity", "water", "gas"], default=None, help="Filter by utility type")

    # forecast
    p_fc = sub.add_parser("forecast", help="Predict next bill based on seasonal patterns")
    p_fc.add_argument("--type", choices=["electricity", "water", "gas"], default=None, help="Filter by utility type")

    # report
    p_rep = sub.add_parser("report", help="Annual summary with savings suggestions")
    p_rep.add_argument("--type", choices=["electricity", "water", "gas"], default=None, help="Filter by utility type")

    args = parser.parse_args()

    commands = {
        "add": cmd_add,
        "history": cmd_history,
        "compare": cmd_compare,
        "anomaly": cmd_anomaly,
        "forecast": cmd_forecast,
        "report": cmd_report,
    }

    return commands[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
