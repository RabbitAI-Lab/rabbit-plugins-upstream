#!/usr/bin/env python3
"""
freelance-rate-calculator — compute a sustainable freelance/contract hourly rate.

Subcommands: rate | compare | project | plan | demo

The core idea: freelancers systematically underprice because they anchor on
salaried hourly equivalents (salary / 2080) and forget that freelancers:
  * only bill a fraction of hours (sales, admin, learning are unpaid)
  * pay both halves of payroll taxes + benefits out of pocket
  * must fund their own vacation, sick days, and retirement
  * need bench cushion for gaps between contracts

Runs offline, stdlib only. All monetary figures are annual unless stated.
"""
import argparse
import json
import sys

# Die quietly on SIGPIPE when users pipe to head/less
try:
    import signal
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
except (AttributeError, ValueError):
    pass

# ── Defaults (documented assumptions; every one is overridable) ─────────────
DEFAULTS = {
    "billable_ratio": 0.60,      # 60% of working hours are billable (industry norm 50-70%)
    "workweeks": 46,             # 52 - 4 vacation - 7 holidays - 1 sick (round)
    "hours_per_week": 40,        # total working hours (billable + unpaid)
    "self_emp_tax_rate": 0.153,  # SECA: both halves of FICA (US)
    "income_tax_rate": 0.18,     # effective federal/state marginal (rough, US)
    "months_bench": 1.0,         # expected gap months/year between contracts
    "bench_loaded": True,        # fold bench months into the required rate
    "overhead": 0,               # $/yr: software, hardware amortization, insurance, CPA...
    "benefits_load": 0,          # $/yr: health insurance, retirement match you self-fund
    "target_net": 0,             # $/yr take-home you want to hit
}


def money(x):
    return f"${x:,.0f}"


# ── Core math ────────────────────────────────────────────────────────────────
def compute_rate(target_net, overhead=0, benefits_load=0,
                 billable_ratio=DEFAULTS["billable_ratio"],
                 workweeks=DEFAULTS["workweeks"],
                 hours_per_week=DEFAULTS["hours_per_week"],
                 self_emp_tax_rate=DEFAULTS["self_emp_tax_rate"],
                 income_tax_rate=DEFAULTS["income_tax_rate"],
                 months_bench=DEFAULTS["months_bench"],
                 bench_loaded=True):
    """Return full rate breakdown from a desired net (take-home) income.

    Logic:
      1. Gross-up net for income tax + self-employment tax → revenue needed.
      2. Add overhead + benefits → operating revenue needed.
      3. Billable hours = workweeks × hours/week × billable_ratio
         (bench months already carved out of workweeks; if bench_loaded,
          also shrink billable hours by months_bench/12 as extra cushion).
      4. rate = operating revenue / billable hours.
    """
    net = float(target_net)
    overhead = float(overhead)
    benefits = float(benefits_load)

    # 1. tax gross-up: net = gross × (1 - income_tax) - gross × se_tax
    #    (SE tax applies to 92.35% of net earnings; folded into rate for simplicity)
    se_base_factor = 0.9235
    keep_ratio = 1 - income_tax_rate - self_emp_tax_rate * se_base_factor
    gross_needed = net / keep_ratio

    # 2. operating revenue
    revenue_needed = gross_needed + overhead + benefits

    # 3. billable hours
    total_hours = workweeks * hours_per_week
    billable = total_hours * billable_ratio
    if bench_loaded and months_bench > 0:
        billable *= (12 - months_bench) / 12.0

    rate = revenue_needed / max(1.0, billable)

    return {
        "target_net": net,
        "gross_needed": round(gross_needed),
        "revenue_needed": round(revenue_needed),
        "keep_ratio": round(keep_ratio, 4),
        "total_hours": total_hours,
        "billable_hours": round(billable),
        "hourly_rate": round(rate, 2),
        "day_rate": round(rate * 8, 2),
        "weekly_rate": round(rate * hours_per_week * billable_ratio, 2),
        "assumptions": {
            "billable_ratio": billable_ratio,
            "workweeks": workweeks,
            "hours_per_week": hours_per_week,
            "income_tax_rate": income_tax_rate,
            "self_emp_tax_rate": self_emp_tax_rate,
            "months_bench": months_bench,
            "bench_loaded": bench_loaded,
            "overhead": overhead,
            "benefits_load": benefits,
        },
    }


def rate_for_salary(salary, overhead=0, benefits_load=0, **kw):
    """What rate replaces a given salaried job? (net ≈ salary after tax at job)"""
    # Salaried employee keeps ~78% after income+payroll(employee half)
    job_keep = 0.78
    net_equivalent = salary * job_keep
    return compute_rate(net_equivalent, overhead=overhead,
                        benefits_load=benefits_load, **kw)


def check_rate(hourly_rate, **kw):
    """Inverse: what net income does an offered rate actually produce?"""
    # normalize CLI-friendly names to compute_rate's signature
    if "se_tax" in kw:
        kw["self_emp_tax_rate"] = kw.pop("se_tax")
    r = float(hourly_rate)
    b = compute_rate(1, **kw)  # get assumptions/billable from a probe call
    billable = b["billable_hours"]
    revenue = r * billable
    se_base_factor = 0.9235
    keep_ratio = b["keep_ratio"]
    # overhead/benefits come out of revenue before personal net
    overhead_total = kw.get("overhead", 0) or 0
    benefits_total = kw.get("benefits_load", 0) or 0
    net = (revenue - overhead_total - benefits_total) * keep_ratio
    return {
        "hourly_rate": r,
        "billable_hours": billable,
        "annual_revenue": round(revenue),
        "annual_net": round(net),
        "monthly_net": round(net / 12),
        "equivalent_salary": round(net / job_keep_default()),
    }


def job_keep_default():
    return 0.78


# ── Project pricing ──────────────────────────────────────────────────────────
def price_project(hours_estimate, hourly_rate, risk_buffer=0.15,
                  value_price_cap=None, rush=False):
    """Turn an hours estimate into a fixed-price quote with buffer."""
    buffered = hours_estimate * (1 + risk_buffer)
    if rush:
        buffered *= 1.25
    price = buffered * hourly_rate
    q = {
        "hours_estimate": hours_estimate,
        "buffered_hours": round(buffered, 1),
        "hourly_rate": hourly_rate,
        "fixed_price": round(price, -1),
        "price_per_hour_effective": round(price / max(1, hours_estimate), 2),
    }
    if value_price_cap is not None and price > value_price_cap:
        q["capped_at"] = value_price_cap
        q["fixed_price"] = value_price_cap
        q["note"] = "capped by client value ceiling"
    return q


# ── Scenario helpers ─────────────────────────────────────────────────────────
def run_rate(args):
    r = compute_rate(args.target_net, overhead=args.overhead,
                     benefits_load=args.benefits,
                     billable_ratio=args.billable_ratio,
                     workweeks=args.workweeks,
                     hours_per_week=args.hours,
                     months_bench=args.bench_months,
                     bench_loaded=not args.no_bench_load,
                     income_tax_rate=args.income_tax,
                     self_emp_tax_rate=args.se_tax)
    print("FREELANCE RATE CALCULATOR")
    print("=" * 66)
    print(f"  Target take-home:        {money(r['target_net'])}/yr")
    print(f"  Tax keep-ratio:          {r['keep_ratio']:.1%} of revenue is yours")
    print(f"  Gross needed (taxes):    {money(r['gross_needed'])}")
    print(f"  Overhead + benefits:     {money(args.overhead + args.benefits)}/yr")
    print(f"  Revenue needed:          {money(r['revenue_needed'])}")
    print()
    print(f"  Working year:            {args.workweeks}w × {args.hours}h = {r['total_hours']:,}h total")
    print(f"  Billable ratio:          {args.billable_ratio:.0%} → {r['billable_hours']:,}h billable")
    if args.bench_months:
        print(f"  Bench cushion:           {args.bench_months} months folded in")
    print()
    print(f"  ══ HOURLY RATE: ${r['hourly_rate']:,.2f}/h ══")
    print(f"  Day rate (8h):  {money(r['day_rate'])}")
    print(f"  Weekly rate:    {money(r['weekly_rate'])}")
    print()
    print(f"  ⚠ Quote it. Don't explain it. The naive 'net ÷ 2080' would be "
          f"${args.target_net/2080:,.0f}/h;")
    print(f"    the true rate is {r['hourly_rate']/(args.target_net/2080):.1f}× that —"
          " the gap is taxes,")
    print("    bench time, and unpaid admin. Underquoting it is why freelancers")
    print("    go broke busy.")
    return r


def run_salary(args):
    r = rate_for_salary(args.salary, overhead=args.overhead,
                        benefits_load=args.benefits,
                        billable_ratio=args.billable_ratio,
                        months_bench=args.bench_months)
    print("RATE TO REPLACE A SALARY")
    print("=" * 66)
    print(f"  Salaried job:            {money(args.salary)}/yr")
    print(f"  Your take-home there:    ~{money(args.salary * 0.78)} (≈22% tax/payroll)")
    print(f"  Same net as freelance:   needs rate below — plus you cover your")
    print(f"                           own health insurance & retirement ({money(args.benefits)}/yr if funded)")
    print()
    print(f"  Revenue needed:          {money(r['revenue_needed'])}")
    print(f"  Billable hours:          {r['billable_hours']:,}h")
    print(f"  ══ HOURLY RATE: ${r['hourly_rate']:,.2f}/h ══")
    print()
    print("  Rule of thumb check: salaried hourly = salary/2080 =", end=" ")
    print(f"${args.salary/2080:,.2f}/h — that's the trap that bankrupts you.")
    print(f"  True rate is {r['hourly_rate'] / (args.salary/2080):.2f}× the naive one.")
    return r


def run_check(args):
    c = check_rate(args.rate, overhead=args.overhead, benefits_load=args.benefits,
                   billable_ratio=args.billable_ratio, workweeks=args.workweeks,
                   hours_per_week=args.hours, months_bench=args.bench_months,
                   income_tax_rate=args.income_tax, se_tax=args.se_tax)
    print("WHAT DOES THIS RATE ACTUALLY PAY?")
    print("=" * 66)
    print(f"  Rate:                    ${args.rate:,.2f}/h")
    print(f"  × {c['billable_hours']:,} billable hours = {money(c['annual_revenue'])} revenue")
    print(f"  − overhead/benefits − taxes → {money(c['annual_net'])} net")
    print(f"  Monthly take-home:       {money(c['monthly_net'])}")
    print(f"  ≈ equivalent salary:     {money(c['equivalent_salary'])} (pre-tax job)")
    if args.min_net and c["annual_net"] < args.min_net:
        deficit = args.min_net - c["annual_net"]
        print()
        print(f"  ⚠ {money(deficit)}/yr SHORT of your {money(args.min_net)} minimum.")
        need = compute_rate(args.min_net, overhead=args.overhead,
                            benefits_load=args.benefits, billable_ratio=args.billable_ratio,
                            months_bench=args.bench_months)
        print(f"    You need ${need['hourly_rate']:,.2f}/h instead.")
    return c


def run_project(args):
    base = compute_rate(args.target_net, overhead=args.overhead,
                        benefits_load=args.benefits, billable_ratio=args.billable_ratio,
                        months_bench=args.bench_months)
    rate = args.rate or base["hourly_rate"]
    q = price_project(args.hours, rate, risk_buffer=args.buffer,
                      value_price_cap=args.value_cap, rush=args.rush)
    print("FIXED-PRICE PROJECT QUOTE")
    print("=" * 66)
    print(f"  Your hours estimate:     {args.hours}h")
    print(f"  Risk buffer:             +{args.buffer:.0%} → {q['buffered_hours']}h")
    if args.rush:
        print(f"  Rush premium:            +25%")
    print(f"  Rate basis:              ${rate:,.2f}/h")
    print(f"  ══ QUOTE: {money(q['fixed_price'])} ══")
    print(f"  Effective rate if on-estimate: ${q['price_per_hour_effective']:,.2f}/h")
    if "note" in q:
        print(f"  ({q['note']}; effective rate ${q['fixed_price']/max(1,args.hours):,.2f}/h)")
    print()
    print("  Scope-creep guard: 'That's outside our agreed scope — happy to")
    print("  quote it as a change order at the same rate.'")
    return q


def run_demo(args):
    print("=== DEMO 1: $70k target net, full costs ===")
    r = compute_rate(70000, overhead=4000, benefits_load=9600)
    print(f"  $70k net + $4k software/insurance + $9.6k health → "
          f"${r['hourly_rate']:,.2f}/h over {r['billable_hours']:,} billable hours")
    print()
    print("=== DEMO 2: naive vs true (the $95k trap) ===")
    r2 = rate_for_salary(95000, benefits_load=9600)
    print(f"  Leaving a $95k job? salary/2080 = $45.67/h (the trap)")
    print(f"  True replacement rate:    ${r2['hourly_rate']:,.2f}/h")
    print(f"  Underpricing at $45/h nets you ≈ "
          f"{money(check_rate(45, benefits_load=9600)['annual_net'])}/yr")
    print()
    print("=== DEMO 3: project quote ===")
    q = price_project(60, r2["hourly_rate"], risk_buffer=0.15)
    print(f"  60h estimate at ${r2['hourly_rate']:,.2f}/h + 15% buffer → quote {money(q['fixed_price'])}")
    return 0


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd")

    def common(sp):
        sp.add_argument("--overhead", type=float, default=0,
                        help="$/yr software, hardware, insurance, CPA (default 0)")
        sp.add_argument("--benefits", type=float, default=0,
                        help="$/yr health/retirement you self-fund (default 0)")
        sp.add_argument("--billable-ratio", type=float, default=0.60,
                        help="billable share of working hours (default 0.60)")
        sp.add_argument("--workweeks", type=int, default=46)
        sp.add_argument("--hours", type=int, default=40, help="working h/week")
        sp.add_argument("--bench-months", type=float, default=1.0)
        sp.add_argument("--income-tax", type=float, default=0.18)
        sp.add_argument("--se-tax", type=float, default=0.153)
        sp.add_argument("--no-bench-load", action="store_true")

    rate_p = sub.add_parser("rate", help="rate from target take-home")
    rate_p.add_argument("--target-net", type=float, required=True)
    common(rate_p)

    sal_p = sub.add_parser("salary", help="rate to replace a salaried job")
    sal_p.add_argument("--salary", type=float, required=True)
    common(sal_p)

    chk = sub.add_parser("check", help="what net does rate X produce?")
    chk.add_argument("--rate", type=float, required=True)
    chk.add_argument("--min-net", type=float, default=0)
    common(chk)

    prj = sub.add_parser("project", help="fixed-price quote from hours")
    prj.add_argument("--hours", type=float, required=True)
    prj.add_argument("--rate", type=float, default=0, help="use this rate (default: computed)")
    prj.add_argument("--target-net", type=float, default=70000)
    prj.add_argument("--buffer", type=float, default=0.15)
    prj.add_argument("--value-cap", type=float, default=None)
    prj.add_argument("--rush", action="store_true")
    prj.add_argument("--overhead", type=float, default=0)
    prj.add_argument("--benefits", type=float, default=0)
    prj.add_argument("--billable-ratio", type=float, default=0.60)
    prj.add_argument("--bench-months", type=float, default=1.0)
    prj.add_argument("--workweeks", type=int, default=46)

    sub.add_parser("demo")

    args = p.parse_args()
    handlers = {"rate": run_rate, "salary": run_salary, "check": run_check,
                "project": run_project, "demo": run_demo}
    if args.cmd in handlers:
        handlers[args.cmd](args)
        return 0
    p.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
