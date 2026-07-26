#!/usr/bin/env python3
"""Compute a target freelance hourly/project rate from desired take-home income and real costs."""

import argparse
import json


def compute_rate(
    target_annual_income,
    work_weeks_per_year=48,
    billable_hours_per_week=25,
    business_expenses_annual=0.0,
    tax_rate_pct=25.0,
    profit_margin_pct=10.0,
):
    """
    target_annual_income: desired take-home (post-tax) income in USD
    work_weeks_per_year: weeks actually worked (accounts for vacation/holidays)
    billable_hours_per_week: hours you can realistically bill, not total hours worked
                              (unbillable time: admin, sales, learning is excluded here)
    business_expenses_annual: software, insurance, equipment, etc.
    tax_rate_pct: effective tax rate to gross up for (self-employment + income tax)
    profit_margin_pct: buffer/reinvestment margin on top of break-even
    """
    if billable_hours_per_week <= 0 or work_weeks_per_year <= 0:
        raise ValueError("billable_hours_per_week and work_weeks_per_year must be > 0")

    # Gross up post-tax target to pre-tax revenue needed
    pre_tax_income_needed = target_annual_income / (1 - tax_rate_pct / 100.0)
    revenue_needed = pre_tax_income_needed + business_expenses_annual
    revenue_needed_with_margin = revenue_needed * (1 + profit_margin_pct / 100.0)

    total_billable_hours = work_weeks_per_year * billable_hours_per_week
    hourly_rate = revenue_needed_with_margin / total_billable_hours

    return {
        "inputs": {
            "target_annual_income": target_annual_income,
            "work_weeks_per_year": work_weeks_per_year,
            "billable_hours_per_week": billable_hours_per_week,
            "business_expenses_annual": business_expenses_annual,
            "tax_rate_pct": tax_rate_pct,
            "profit_margin_pct": profit_margin_pct,
        },
        "total_billable_hours_per_year": total_billable_hours,
        "pre_tax_revenue_needed": round(revenue_needed_with_margin, 2),
        "recommended_hourly_rate": round(hourly_rate, 2),
        "day_rate_8h": round(hourly_rate * 8, 2),
        "week_rate_at_billable_hours": round(hourly_rate * billable_hours_per_week, 2),
        "monthly_target_revenue": round(revenue_needed_with_margin / 12, 2),
    }


def project_rate(hourly_rate, estimated_hours, risk_buffer_pct=15.0):
    """Convert an hourly rate + hour estimate into a fixed project quote with a risk buffer."""
    base = hourly_rate * estimated_hours
    with_buffer = base * (1 + risk_buffer_pct / 100.0)
    return {
        "hourly_rate": hourly_rate,
        "estimated_hours": estimated_hours,
        "risk_buffer_pct": risk_buffer_pct,
        "base_project_price": round(base, 2),
        "recommended_project_price": round(with_buffer, 2),
    }


def main():
    ap = argparse.ArgumentParser(description="Freelance rate calculator: target income -> hourly/day/project rate")
    sub = ap.add_subparsers(dest="cmd", required=True)

    rate_p = sub.add_parser("rate", help="Compute hourly/day rate from target annual income")
    rate_p.add_argument("--target-income", type=float, required=True, help="Desired take-home (post-tax) annual income, USD")
    rate_p.add_argument("--work-weeks", type=float, default=48, help="Weeks worked per year (default 48, i.e. 4 weeks off)")
    rate_p.add_argument("--billable-hours", type=float, default=25, help="Realistically billable hours per week (default 25; most freelancers bill 50-60%% of a 40-50h week)")
    rate_p.add_argument("--expenses", type=float, default=0.0, help="Annual business expenses (software, insurance, equipment), USD")
    rate_p.add_argument("--tax-rate", type=float, default=25.0, help="Effective tax rate percent to gross up for (default 25)")
    rate_p.add_argument("--margin", type=float, default=10.0, help="Profit/reinvestment margin percent on top of break-even (default 10)")
    rate_p.add_argument("--json", action="store_true")

    proj_p = sub.add_parser("project", help="Convert hourly rate + hour estimate into a project quote")
    proj_p.add_argument("--hourly-rate", type=float, required=True)
    proj_p.add_argument("--hours", type=float, required=True, help="Estimated hours for the project")
    proj_p.add_argument("--buffer", type=float, default=15.0, help="Risk buffer percent for scope creep/underestimation (default 15)")
    proj_p.add_argument("--json", action="store_true")

    args = ap.parse_args()

    if args.cmd == "rate":
        result = compute_rate(
            args.target_income, args.work_weeks, args.billable_hours,
            args.expenses, args.tax_rate, args.margin,
        )
        if args.json:
            print(json.dumps(result, indent=2))
            return
        print(f"Target take-home income:     ${args.target_income:,.2f}/yr")
        print(f"Billable hours/year:         {result['total_billable_hours_per_year']:,.0f}")
        print(f"Pre-tax revenue needed:      ${result['pre_tax_revenue_needed']:,.2f}/yr")
        print("-" * 44)
        print(f"Recommended hourly rate:     ${result['recommended_hourly_rate']:,.2f}/hr")
        print(f"Recommended day rate (8h):   ${result['day_rate_8h']:,.2f}/day")
        print(f"Weekly target (at billable): ${result['week_rate_at_billable_hours']:,.2f}/wk")
        print(f"Monthly target revenue:      ${result['monthly_target_revenue']:,.2f}/mo")
    else:
        result = project_rate(args.hourly_rate, args.hours, args.buffer)
        if args.json:
            print(json.dumps(result, indent=2))
            return
        print(f"Base price ({args.hours}h @ ${args.hourly_rate}/hr): ${result['base_project_price']:,.2f}")
        print(f"With {args.buffer}% risk buffer:              ${result['recommended_project_price']:,.2f}")


if __name__ == "__main__":
    main()
