#!/usr/bin/env python3
"""
Subscription Slayer — track subscriptions, detect waste, generate cancellations.

Usage:
    python3 subscription_tracker.py analyze subs.json
    python3 subscription_tracker.py analyze subs.json --json
    python3 subscription_tracker.py analyze subs.json --threshold 50
    python3 subscription_tracker.py cancel subs.json --name "Netflix"
    python3 subscription_tracker.py cancel subs.json --threshold 70
    python3 subscription_tracker.py demo

Stdlib only. No external dependencies.
"""

import argparse
import json
import os
import sys
from datetime import date, datetime

# ---------------------------------------------------------------------------
# Cost normalisation
# ---------------------------------------------------------------------------

CYCLE_TO_MONTHS = {
    "weekly": 12.0 / 52.0,
    "biweekly": 12.0 / 26.0,
    "monthly": 1.0,
    "bimonthly": 1.0 / 2.0,
    "quarterly": 1.0 / 3.0,
    "semiannual": 1.0 / 6.0,
    "yearly": 1.0 / 12.0,
    "annual": 1.0 / 12.0,
}


def monthly_cost(cost: float, cycle: str) -> float:
    """Convert a per-cycle cost to monthly cost."""
    months = CYCLE_TO_MONTHS.get(cycle.lower(), 1.0)
    return round(cost * months, 2)


def annual_cost(cost: float, cycle: str) -> float:
    """Convert a per-cycle cost to annual cost."""
    return round(monthly_cost(cost, cycle) * 12, 2)


# ---------------------------------------------------------------------------
# Waste detection
# ---------------------------------------------------------------------------

# Categories that are commonly forgotten / underutilised
HIGH_WASTE_CATEGORIES = {
    "news", "magazine", "newsletter",
    "cloud storage", "backup",
    "app", "software",
}
MEDIUM_WASTE_CATEGORIES = {
    "music", "entertainment", "streaming", "video",
    "fitness", "gym", "health",
    "productivity", "education",
}


def parse_date_safe(s: str | None) -> date | None:
    """Parse an ISO date string safely."""
    if not s:
        return None
    try:
        return datetime.strptime(s[:10], "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return None


def days_between(d1: date, d2: date) -> int:
    """Return the number of days between two dates."""
    return abs((d2 - d1).days)


def compute_waste_score(sub: dict, reference_date: date | None = None) -> int:
    """
    Compute a waste probability score (0–100).

    Factors:
      - Days since last use (40 pts max)
      - Cost efficiency (25 pts max) — high cost + low usage = waste
      - Subscription age (15 pts max)
      - Auto-renew (10 pts)
      - Category tendency (10 pts)
    """
    if reference_date is None:
        reference_date = date.today()

    score = 0

    # --- Factor 1: Days since last use (40 pts) ---
    last_used = parse_date_safe(sub.get("last_used"))
    if last_used:
        days_unused = days_between(last_used, reference_date)
        if days_unused >= 180:
            score += 40
        elif days_unused >= 90:
            score += 35
        elif days_unused >= 60:
            score += 28
        elif days_unused >= 30:
            score += 20
        elif days_unused >= 14:
            score += 10
        elif days_unused >= 7:
            score += 5
    else:
        # No last_used data — slight uncertainty penalty
        score += 5

    # --- Factor 2: Cost vs. usage (25 pts) ---
    monthly = monthly_cost(sub.get("cost", 0), sub.get("billing_cycle", "monthly"))
    if last_used:
        days_unused = days_between(last_used, reference_date)
        if days_unused >= 30 and monthly >= 10:
            score += 25
        elif days_unused >= 30 and monthly >= 5:
            score += 18
        elif days_unused >= 30:
            score += 10
        elif days_unused >= 14 and monthly >= 15:
            score += 15
    else:
        if monthly >= 20:
            score += 15
        elif monthly >= 10:
            score += 8

    # --- Factor 3: Subscription age (15 pts) ---
    start_date = parse_date_safe(sub.get("start_date"))
    if start_date:
        age_days = days_between(start_date, reference_date)
        if age_days >= 730:  # 2+ years
            score += 15
        elif age_days >= 365:  # 1+ year
            score += 10
        elif age_days >= 180:
            score += 5

    # --- Factor 4: Auto-renew (10 pts) ---
    auto_renew = sub.get("auto_renew", True)
    if auto_renew:
        score += 10

    # --- Factor 5: Category tendency (10 pts) ---
    category = (sub.get("category") or "").lower()
    if category in HIGH_WASTE_CATEGORIES:
        score += 10
    elif category in MEDIUM_WASTE_CATEGORIES:
        score += 5

    return min(score, 100)


def waste_label(score: int) -> str:
    """Return a human-readable waste label."""
    if score >= 80:
        return "🔴 Critical — almost certainly wasting money"
    elif score >= 60:
        return "🟠 High — likely unused"
    elif score >= 40:
        return "🟡 Moderate — possibly underutilised"
    else:
        return "🟢 Low — probably in use"


# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------


def analyze_subscriptions(subs: list, reference_date: date | None = None) -> dict:
    """
    Analyze a list of subscriptions.

    Returns dict with totals, per-subscription details ranked by waste, and
    category breakdowns.
    """
    if reference_date is None:
        reference_date = date.today()

    details = []
    total_monthly = 0.0
    total_annual = 0.0

    for sub in subs:
        m_cost = monthly_cost(sub.get("cost", 0), sub.get("billing_cycle", "monthly"))
        a_cost = annual_cost(sub.get("cost", 0), sub.get("billing_cycle", "monthly"))
        total_monthly += m_cost
        total_annual += a_cost

        score = compute_waste_score(sub, reference_date)
        last_used = parse_date_safe(sub.get("last_used"))
        days_unused = (
            days_between(last_used, reference_date) if last_used else None
        )

        details.append(
            {
                "name": sub.get("name", "Unknown"),
                "cost": sub.get("cost", 0),
                "billing_cycle": sub.get("billing_cycle", "monthly"),
                "monthly_cost": m_cost,
                "annual_cost": a_cost,
                "category": sub.get("category", "uncategorized"),
                "last_used": sub.get("last_used", ""),
                "days_unused": days_unused,
                "auto_renew": sub.get("auto_renew", True),
                "cancel_url": sub.get("cancel_url", ""),
                "waste_score": score,
                "waste_label": waste_label(score),
            }
        )

    # Sort by waste score descending
    details.sort(key=lambda x: x["waste_score"], reverse=True)

    # Category breakdown
    category_costs = {}
    for d in details:
        cat = d["category"]
        if cat not in category_costs:
            category_costs[cat] = {"monthly": 0, "annual": 0, "count": 0}
        category_costs[cat]["monthly"] += d["monthly_cost"]
        category_costs[cat]["annual"] += d["annual_cost"]
        category_costs[cat]["count"] += 1

    return {
        "reference_date": reference_date.isoformat(),
        "total_monthly": round(total_monthly, 2),
        "total_annual": round(total_annual, 2),
        "subscription_count": len(subs),
        "details": details,
        "category_breakdown": category_costs,
        "high_waste": [d for d in details if d["waste_score"] >= 60],
        "potential_monthly_savings": round(
            sum(d["monthly_cost"] for d in details if d["waste_score"] >= 60), 2
        ),
        "potential_annual_savings": round(
            sum(d["annual_cost"] for d in details if d["waste_score"] >= 60), 2
        ),
    }


# ---------------------------------------------------------------------------
# Cancellation email generation
# ---------------------------------------------------------------------------

EMAIL_TEMPLATE = """To: {email}
Subject: {subject}

Dear {company} Customer Support,

I am writing to formally request the cancellation of my {name} subscription, effective immediately.

Account details:
  - Service: {name}
  - Account email: [YOUR EMAIL]
  - Account/Member ID: [YOUR ACCOUNT ID]
  - Name on account: [YOUR NAME]

Please process this cancellation and confirm via email that:
1. My subscription has been cancelled and will not be renewed.
2. No further charges will be made to my payment method.
3. Any applicable pro-rated refund for the unused portion of my billing cycle is processed.

If you require any additional information to process this request, please contact me at [YOUR EMAIL].

I expect written confirmation of the cancellation within 5 business days, as required by consumer protection regulations.

Thank you for your prompt attention to this matter.

Sincerely,
[YOUR NAME]
[YOUR EMAIL]
"""


def generate_cancellation_email(sub: dict) -> str:
    """Generate a cancellation email for a subscription."""
    name = sub.get("name", "the service")
    # Guess email and company from name
    company = name.split()[0] if name else "the company"
    domain = company.lower().replace(" ", "") + ".com"
    email = f"support@{domain}"
    subject = f"Cancellation Request — {name} Subscription (Account #[YOUR ACCOUNT ID])"

    return EMAIL_TEMPLATE.format(
        email=email, subject=subject, company=company, name=name
    )


def generate_cancellations(subs: list, threshold: int = 60, name_filter: str | None = None) -> list:
    """Generate cancellation emails for subscriptions matching criteria."""
    reference_date = date.today()
    results = []

    for sub in subs:
        score = compute_waste_score(sub, reference_date)
        sub_name = sub.get("name", "")

        if name_filter:
            if name_filter.lower() not in sub_name.lower():
                continue
        else:
            if score < threshold:
                continue

        results.append(
            {
                "name": sub_name,
                "waste_score": score,
                "waste_label": waste_label(score),
                "cancel_url": sub.get("cancel_url", ""),
                "email": generate_cancellation_email(sub),
            }
        )

    return results


# ---------------------------------------------------------------------------
# Output formatting
# ---------------------------------------------------------------------------


def format_analysis_text(analysis: dict) -> str:
    """Format analysis as readable text."""
    lines = []
    lines.append("=" * 60)
    lines.append("  ⚔️  SUBSCRIPTION SLAYER")
    lines.append("=" * 60)
    lines.append("")

    # Summary
    lines.append(f"  Total monthly cost:   ${analysis['total_monthly']:.2f}/mo")
    lines.append(f"  Total annual cost:    ${analysis['total_annual']:.2f}/yr")
    lines.append(f"  Active subscriptions: {analysis['subscription_count']}")
    lines.append("")

    if analysis["potential_annual_savings"] > 0:
        lines.append(f"  💸 Potential annual savings: ${analysis['potential_annual_savings']:.2f}")
        lines.append(f"     (by cancelling {len(analysis['high_waste'])} high-waste subscriptions)")
        lines.append("")

    # Per-subscription ranking
    lines.append("  📊 SUBSCRIPTIONS RANKED BY WASTE")
    lines.append("  " + "-" * 56)
    for i, d in enumerate(analysis["details"], 1):
        bar_len = d["waste_score"] // 5
        bar = "█" * bar_len + "░" * (20 - bar_len)
        days_str = f"{d['days_unused']}d unused" if d["days_unused"] is not None else "no data"
        lines.append(f"  {i:>2}. {d['name']}")
        lines.append(f"      {d['waste_label']}")
        lines.append(f"      Waste: [{bar}] {d['waste_score']}/100")
        lines.append(f"      ${d['monthly_cost']:.2f}/mo  (${d['annual_cost']:.2f}/yr)  "
                     f"Category: {d['category']}  {days_str}")
        if d["cancel_url"]:
            lines.append(f"      Cancel: {d['cancel_url']}")
        lines.append("")

    # Category breakdown
    lines.append("  🏷️  COST BY CATEGORY")
    lines.append("  " + "-" * 56)
    for cat, info in sorted(analysis["category_breakdown"].items(), key=lambda x: x[1]["monthly"], reverse=True):
        pct = info["monthly"] / analysis["total_monthly"] * 100 if analysis["total_monthly"] else 0
        lines.append(f"     {cat:<20} ${info['monthly']:>7.2f}/mo  "
                     f"(${info['annual']:>8.2f}/yr)  {info['count']} sub(s)  ({pct:.0f}%)")
    lines.append("")

    # Recommendations
    if analysis["high_waste"]:
        lines.append("  ⚔️  RECOMMENDATION: Cancel these now")
        lines.append("  " + "-" * 56)
        for d in analysis["high_waste"]:
            lines.append(f"     • {d['name']}  —  save ${d['annual_cost']:.2f}/yr")
        lines.append("")

    lines.append("=" * 60)
    return "\n".join(lines)


def format_cancellations_text(cancellations: list) -> str:
    """Format cancellation emails as readable text."""
    lines = []
    lines.append("=" * 60)
    lines.append("  📧 CANCELLATION EMAILS")
    lines.append("=" * 60)

    for c in cancellations:
        lines.append("")
        lines.append(f"  ── {c['name']} ({c['waste_score']}/100) ──")
        if c["cancel_url"]:
            lines.append(f"  Cancel URL: {c['cancel_url']}")
        lines.append("")
        # Indent the email body
        for email_line in c["email"].split("\n"):
            lines.append(f"  {email_line}")
        lines.append("")
        lines.append("  " + "-" * 56)

    lines.append("")
    lines.append("  ⚠️  Replace [YOUR EMAIL], [YOUR ACCOUNT ID], and [YOUR NAME]")
    lines.append("     with your actual details before sending.")
    lines.append("=" * 60)
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Sample data for demo
# ---------------------------------------------------------------------------

SAMPLE_SUBS = [
    {
        "name": "Netflix",
        "cost": 15.49,
        "billing_cycle": "monthly",
        "category": "streaming",
        "last_used": "2024-01-15",
        "start_date": "2022-03-01",
        "auto_renew": True,
        "cancel_url": "https://www.netflix.com/cancelplan",
    },
    {
        "name": "Adobe Creative Cloud",
        "cost": 54.99,
        "billing_cycle": "monthly",
        "category": "software",
        "last_used": "2023-06-01",
        "start_date": "2021-01-15",
        "auto_renew": True,
        "cancel_url": "https://account.adobe.com/plans",
    },
    {
        "name": "Spotify Premium",
        "cost": 10.99,
        "billing_cycle": "monthly",
        "category": "music",
        "last_used": "2026-07-28",
        "start_date": "2020-05-10",
        "auto_renew": True,
        "cancel_url": "https://www.spotify.com/account/subscription/",
    },
    {
        "name": "NYT Digital",
        "cost": 17.0,
        "billing_cycle": "monthly",
        "category": "news",
        "last_used": "2023-11-01",
        "start_date": "2019-08-20",
        "auto_renew": True,
        "cancel_url": "https://www.nytimes.com/account",
    },
    {
        "name": "iCloud Storage 200GB",
        "cost": 2.99,
        "billing_cycle": "monthly",
        "category": "cloud storage",
        "last_used": "2026-08-01",
        "start_date": "2018-11-01",
        "auto_renew": True,
        "cancel_url": "https://support.apple.com/billing",
    },
    {
        "name": "Peloton App",
        "cost": 12.99,
        "billing_cycle": "monthly",
        "category": "fitness",
        "last_used": "2024-02-14",
        "start_date": "2022-01-01",
        "auto_renew": True,
        "cancel_url": "https://members.onepeloton.com/preferences",
    },
    {
        "name": "LinkedIn Premium",
        "cost": 39.99,
        "billing_cycle": "monthly",
        "category": "productivity",
        "last_used": "2026-07-15",
        "start_date": "2023-09-01",
        "auto_renew": True,
        "cancel_url": "https://www.linkedin.com/premium/manage",
    },
    {
        "name": "Amazon Prime",
        "cost": 139.0,
        "billing_cycle": "yearly",
        "category": "shopping",
        "last_used": "2026-07-30",
        "start_date": "2017-06-01",
        "auto_renew": True,
        "cancel_url": "https://www.amazon.com/mc/yourmembership",
    },
    {
        "name": "Dropbox Plus",
        "cost": 11.99,
        "billing_cycle": "monthly",
        "category": "cloud storage",
        "last_used": "2023-03-10",
        "start_date": "2020-02-15",
        "auto_renew": True,
        "cancel_url": "https://www.dropbox.com/account/plan",
    },
    {
        "name": "Headspace",
        "cost": 69.99,
        "billing_cycle": "yearly",
        "category": "health",
        "last_used": "2024-09-01",
        "start_date": "2021-04-01",
        "auto_renew": True,
        "cancel_url": "https://account.headspace.com/manage-subscription",
    },
]


def run_demo():
    """Run analysis on sample subscription data."""
    print("=" * 60)
    print("  ⚔️  SUBSCRIPTION SLAYER — Demo Mode")
    print("  Analyzing 10 sample subscriptions...\n")

    analysis = analyze_subscriptions(SAMPLE_SUBS)
    print(format_analysis_text(analysis))

    print("\n\nGenerating cancellation emails for high-waste subscriptions...\n")
    cancellations = generate_cancellations(SAMPLE_SUBS, threshold=60)
    print(format_cancellations_text(cancellations))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Subscription Slayer — track and cancel subscriptions."
    )
    sub = parser.add_subparsers(dest="command", help="Sub-command")

    # Analyze
    p_analyze = sub.add_parser("analyze", help="Analyze subscriptions")
    p_analyze.add_argument("file", type=str, help="JSON file with subscriptions")
    p_analyze.add_argument("--json", action="store_true", help="Output JSON")
    p_analyze.add_argument(
        "--threshold", type=int, default=0, help="Min waste score to show (default 0)"
    )

    # Cancel
    p_cancel = sub.add_parser("cancel", help="Generate cancellation emails")
    p_cancel.add_argument("file", type=str, help="JSON file with subscriptions")
    p_cancel.add_argument("--name", type=str, help="Cancel a specific subscription by name")
    p_cancel.add_argument(
        "--threshold", type=int, default=60, help="Waste score threshold (default 60)"
    )
    p_cancel.add_argument("--json", action="store_true", help="Output JSON")

    # Demo
    sub.add_parser("demo", help="Run demo with sample data")

    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "demo":
        run_demo()
        return 0

    if args.command == "analyze":
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                subs = json.load(f)
        except FileNotFoundError:
            print(f"Error: File not found: {args.file}", file=sys.stderr)
            return 1
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON: {e}", file=sys.stderr)
            return 1

        analysis = analyze_subscriptions(subs)

        if args.threshold > 0:
            analysis["details"] = [
                d for d in analysis["details"] if d["waste_score"] >= args.threshold
            ]

        if args.json:
            print(json.dumps(analysis, indent=2, ensure_ascii=False, default=str))
        else:
            print(format_analysis_text(analysis))
        return 0

    if args.command == "cancel":
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                subs = json.load(f)
        except FileNotFoundError:
            print(f"Error: File not found: {args.file}", file=sys.stderr)
            return 1
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON: {e}", file=sys.stderr)
            return 1

        cancellations = generate_cancellations(
            subs, threshold=args.threshold, name_filter=args.name
        )

        if not cancellations:
            print("No subscriptions matched the criteria.")
            return 0

        if args.json:
            print(json.dumps(cancellations, indent=2, ensure_ascii=False))
        else:
            print(format_cancellations_text(cancellations))
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
