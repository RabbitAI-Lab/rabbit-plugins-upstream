#!/usr/bin/env python3
"""
Tax Doc Collector — track deductible expenses year-round with IRS categorization,
real-time tax savings estimates, audit risk flags, and tax-ready export.
Pure Python stdlib. JSON file database.

Usage:
    python3 tax_docs.py setup --bracket <percent>
    python3 tax_docs.py add --amount <N> --category <cat> --merchant <name> [--note text] [--date YYYY-MM-DD]
    python3 tax_docs.py add-mileage --miles <N> --purpose <text> [--date YYYY-MM-DD]
    python3 tax_docs.py add-home-office --sqft <N>
    python3 tax_docs.py summary [--year YYYY]
    python3 tax_docs.py by-category <category> [--year YYYY]
    python3 tax_docs.py audit-risk [--year YYYY]
    python3 tax_docs.py export schedule-c [--year YYYY]
    python3 tax_docs.py export schedule-a [--year YYYY]
    python3 tax_docs.py export csv [--year YYYY]
    python3 tax_docs.py categories
    python3 tax_docs.py mileage-rate [--year YYYY]
    python3 tax_docs.py list [--year YYYY] [--category cat]
    python3 tax_docs.py delete <id>

Examples:
    python3 tax_docs.py setup --bracket 24
    python3 tax_docs.py add --amount 45.99 --category "office supplies" --merchant "Staples"
    python3 tax_docs.py add --amount 120.00 --category "meals" --merchant "Olive Garden" --note "client lunch"
    python3 tax_docs.py add-mileage --miles 45 --purpose "client visit"
    python3 tax_docs.py summary
    python3 tax_docs.py export schedule-c
"""

import json
import os
import sys
import uuid
from datetime import datetime, date

DB_PATH = os.path.expanduser("~/.tax_docs.json")

# IRS Mileage rates
MILEAGE_RATES = {
    2024: {"business": 0.67, "medical": 0.21, "charity": 0.14},
    2025: {"business": 0.70, "medical": 0.21, "charity": 0.14},
    2026: {"business": 0.70, "medical": 0.22, "charity": 0.14},
}

# Schedule C categories
SCHEDULE_C = {
    "advertising": {"line": "8", "label": "Advertising", "deductible": 1.0},
    "car truck": {"line": "9", "label": "Car and truck expenses", "deductible": 1.0},
    "car": {"line": "9", "label": "Car and truck expenses", "deductible": 1.0},
    "commissions": {"line": "10", "label": "Commissions and fees", "deductible": 1.0},
    "contract labor": {"line": "11", "label": "Contract labor", "deductible": 1.0},
    "depreciation": {"line": "13", "label": "Depreciation", "deductible": 1.0},
    "employee benefits": {"line": "14", "label": "Employee benefit programs", "deductible": 1.0},
    "insurance": {"line": "15", "label": "Insurance (other than health)", "deductible": 1.0},
    "interest mortgage": {"line": "16a", "label": "Interest: mortgage", "deductible": 1.0},
    "interest other": {"line": "16b", "label": "Interest: other", "deductible": 1.0},
    "legal professional": {"line": "17", "label": "Legal and professional services", "deductible": 1.0},
    "office expense": {"line": "18", "label": "Office expense", "deductible": 1.0},
    "office supplies": {"line": "18", "label": "Office expense", "deductible": 1.0},
    "office": {"line": "18", "label": "Office expense", "deductible": 1.0},
    "pension": {"line": "19", "label": "Pension and profit-sharing", "deductible": 1.0},
    "rent vehicle": {"line": "20a", "label": "Rent/lease: vehicles", "deductible": 1.0},
    "rent property": {"line": "20b", "label": "Rent/lease: business property", "deductible": 1.0},
    "rent": {"line": "20b", "label": "Rent/lease: business property", "deductible": 1.0},
    "repairs": {"line": "21", "label": "Repairs and maintenance", "deductible": 1.0},
    "supplies": {"line": "22", "label": "Supplies", "deductible": 1.0},
    "taxes licenses": {"line": "23", "label": "Taxes and licenses", "deductible": 1.0},
    "travel": {"line": "24a", "label": "Travel", "deductible": 1.0},
    "meals": {"line": "24b", "label": "Deductible meals", "deductible": 0.5},
    "utilities": {"line": "25", "label": "Utilities", "deductible": 1.0},
    "wages": {"line": "26", "label": "Wages (less employment credits)", "deductible": 1.0},
    "software": {"line": "27a", "label": "Other: software/subscriptions", "deductible": 1.0},
    "dues": {"line": "27a", "label": "Other: dues/subscriptions", "deductible": 1.0},
    "professional development": {"line": "27a", "label": "Other: education/training", "deductible": 1.0},
    "bank fees": {"line": "27a", "label": "Other: bank/merchant fees", "deductible": 1.0},
    "other": {"line": "27a", "label": "Other expenses", "deductible": 1.0},
}

# Schedule A categories
SCHEDULE_A = {
    "medical": {"label": "Medical and dental", "schedule": "A", "floor": 0.075},
    "medical dental": {"label": "Medical and dental", "schedule": "A", "floor": 0.075},
    "state local tax": {"label": "State and local taxes", "schedule": "A", "floor": 0},
    "property tax": {"label": "Property tax", "schedule": "A", "floor": 0},
    "mortgage interest": {"label": "Mortgage interest", "schedule": "A", "floor": 0},
    "charity": {"label": "Charity (cash)", "schedule": "A", "floor": 0},
    "charity cash": {"label": "Charity (cash)", "schedule": "A", "floor": 0},
    "charity noncash": {"label": "Charity (non-cash)", "schedule": "A", "floor": 0},
    "casualty loss": {"label": "Casualty/theft loss", "schedule": "A", "floor": 0.10},
}

ALL_CATEGORIES = {**SCHEDULE_C, **SCHEDULE_A}


# --- Database ---

def load_db():
    if os.path.exists(DB_PATH):
        with open(DB_PATH, "r") as f:
            return json.load(f)
    return {
        "bracket": 22,
        "expenses": [],
        "mileage": [],
        "home_office": None,
    }

def save_db(db):
    with open(DB_PATH, "w") as f:
        json.dump(db, f, indent=2, default=str)


# --- Parsing ---

def parse_flags(args):
    positional = []
    flags = {}
    i = 0
    while i < len(args):
        if args[i].startswith("--"):
            key = args[i][2:]
            if i + 1 < len(args) and not args[i + 1].startswith("--"):
                flags[key] = args[i + 1]
                i += 2
            else:
                flags[key] = True
                i += 1
        else:
            positional.append(args[i])
            i += 1
    return positional, flags


def lookup_category(user_cat):
    """Match user input to an IRS category (case insensitive, fuzzy)."""
    user_lower = user_cat.lower().strip()
    if user_lower in ALL_CATEGORIES:
        return user_lower, ALL_CATEGORIES[user_lower]
    # Try partial matches
    for key, val in ALL_CATEGORIES.items():
        if user_lower in key or key in user_lower:
            return key, val
    # Unknown → put in "other"
    return "other", ALL_CATEGORIES["other"]


# --- Commands ---

def cmd_setup(db, args):
    _, flags = parse_flags(args)
    bracket_str = flags.get("bracket")
    if bracket_str:
        try:
            bracket = float(bracket_str)
        except ValueError:
            print("Error: bracket must be a number (e.g. 24 for 24%)")
            return
        db["bracket"] = bracket
        save_db(db)
        print(f"✓ Tax bracket set to {bracket}%")
    else:
        print(f"Current bracket: {db.get('bracket', 22)}%")


def cmd_add(db, args):
    _, flags = parse_flags(args)
    amount_str = flags.get("amount")
    category_str = flags.get("category", "other")
    merchant = flags.get("merchant", "Unknown")
    note = flags.get("note", "")
    exp_date = flags.get("date", date.today().isoformat())

    if not amount_str:
        print("Error: --amount is required")
        return

    try:
        amount = float(amount_str)
    except ValueError:
        print(f"Error: amount must be a number, got '{amount_str}'")
        return

    cat_key, cat_info = lookup_category(category_str)
    deductible_rate = cat_info.get("deductible", 1.0)
    deductible_amount = amount * deductible_rate
    savings = deductible_amount * (db.get("bracket", 22) / 100)

    expense = {
        "id": str(uuid.uuid4())[:8],
        "date": exp_date,
        "amount": amount,
        "deductible_amount": round(deductible_amount, 2),
        "category": category_str,
        "category_key": cat_key,
        "schedule": "C" if cat_key in SCHEDULE_C else "A",
        "merchant": merchant,
        "note": note,
        "savings": round(savings, 2),
    }
    db["expenses"].append(expense)
    save_db(db)

    print(f"✓ Logged expense #{expense['id']}")
    print(f"   ${amount:.2f} at {merchant} ({exp_date})")
    print(f"   Category: {cat_info['label']} (Schedule {expense['schedule']})")
    if deductible_rate < 1.0:
        print(f"   Deductible portion: ${deductible_amount:.2f} ({deductible_rate*100:.0f}%)")
    print(f"   💰 Est. tax savings: ${savings:.2f} (at {db.get('bracket', 22)}% bracket)")


def cmd_add_mileage(db, args):
    _, flags = parse_flags(args)
    miles_str = flags.get("miles")
    purpose = flags.get("purpose", "Business")
    exp_date = flags.get("date", date.today().isoformat())

    if not miles_str:
        print("Error: --miles is required")
        return

    try:
        miles = float(miles_str)
    except ValueError:
        print(f"Error: miles must be a number")
        return

    year = int(exp_date[:4]) if len(exp_date) >= 4 else date.today().year
    rate = MILEAGE_RATES.get(year, MILEAGE_RATES[2026])
    rate_val = rate["business"]
    deduction = miles * rate_val
    savings = deduction * (db.get("bracket", 22) / 100)

    entry = {
        "id": str(uuid.uuid4())[:8],
        "date": exp_date,
        "miles": miles,
        "purpose": purpose,
        "rate": rate_val,
        "deduction": round(deduction, 2),
        "savings": round(savings, 2),
    }
    db["mileage"].append(entry)
    save_db(db)

    print(f"✓ Logged mileage #{entry['id']}")
    print(f"   {miles:.0f} miles — {purpose} ({exp_date})")
    print(f"   Rate: ${rate_val:.2f}/mile ({year} IRS standard)")
    print(f"   Deduction: ${deduction:.2f}")
    print(f"   💰 Est. tax savings: ${savings:.2f}")


def cmd_add_home_office(db, args):
    _, flags = parse_flags(args)
    sqft_str = flags.get("sqft")
    if not sqft_str:
        print("Error: --sqft is required")
        return
    try:
        sqft = int(sqft_str)
    except ValueError:
        print("Error: sqft must be a number")
        return
    if sqft > 300:
        print("⚠ Simplified method caps at 300 sqft. Using 300.")
        sqft = 300
    deduction = sqft * 5  # $5 per sqft
    savings = deduction * (db.get("bracket", 22) / 100)
    db["home_office"] = {
        "sqft": sqft,
        "method": "simplified",
        "deduction": deduction,
        "savings": round(savings, 2),
    }
    save_db(db)
    print(f"✓ Home office deduction (simplified method)")
    print(f"   {sqft} sqft × $5 = ${deduction:.2f}")
    print(f"   💰 Est. tax savings: ${savings:.2f}")


def cmd_summary(db, args):
    _, flags = parse_flags(args)
    year = int(flags.get("year", date.today().year))

    year_expenses = [e for e in db["expenses"] if e["date"].startswith(str(year))]
    year_mileage = [m for m in db.get("mileage", []) if m["date"].startswith(str(year))]

    total_expense = sum(e["deductible_amount"] for e in year_expenses)
    total_mileage_deduction = sum(m["deduction"] for m in year_mileage)
    home_office = db.get("home_office", {})
    if home_office and str(year) == date.today().strftime("%Y"):
        ho_deduction = home_office.get("deduction", 0)
    else:
        ho_deduction = 0

    total_deductions = total_expense + total_mileage_deduction + ho_deduction
    bracket = db.get("bracket", 22)
    total_savings = total_deductions * (bracket / 100)

    print(f"📊 Tax Year {year} Summary")
    print(f"{'═' * 55}")
    print(f"   Marginal bracket: {bracket}%")
    print(f"{'─' * 55}")
    print(f"   Expense deductions:  ${total_expense:>10,.2f}")
    print(f"   Mileage deductions:  ${total_mileage_deduction:>10,.2f}")
    if ho_deduction:
        print(f"   Home office:         ${ho_deduction:>10,.2f}")
    print(f"{'─' * 55}")
    print(f"   Total deductions:    ${total_deductions:>10,.2f}")
    print(f"   💰 Est. tax savings:  ${total_savings:>10,.2f}")
    print(f"{'═' * 55}")

    # Breakdown by category
    print(f"\n   By Category:")
    cat_totals = {}
    for e in year_expenses:
        cat = e.get("category_key", "other")
        label = ALL_CATEGORIES.get(cat, {}).get("label", cat)
        cat_totals[label] = cat_totals.get(label, 0) + e["deductible_amount"]
    for cat, total in sorted(cat_totals.items(), key=lambda x: x[1], reverse=True):
        bar_len = min(int(total / 50), 30)
        bar = "█" * bar_len
        print(f"   {cat:<35s} ${total:>8,.2f} {bar}")
    if year_mileage:
        total_miles = sum(m["miles"] for m in year_mileage)
        print(f"   {'Mileage (' + str(int(total_miles)) + ' miles)':<35s} ${total_mileage_deduction:>8,.2f}")


def cmd_by_category(db, args):
    if len(args) < 1:
        print("Usage: by-category <category> [--year YYYY]")
        return
    cat_input = args[0]
    _, flags = parse_flags(args)
    year = int(flags.get("year", date.today().year))
    cat_key, cat_info = lookup_category(cat_input)

    matching = [e for e in db["expenses"]
                if e.get("category_key") == cat_key and e["date"].startswith(str(year))]

    print(f"📂 {cat_info['label']} — {len(matching)} entries ({year})")
    print(f"{'─' * 60}")
    total = 0
    for e in sorted(matching, key=lambda x: x["date"]):
        total += e["deductible_amount"]
        print(f"   {e['date']} {e['merchant'][:25]:<25s} ${e['amount']:>8.2f} (deduct ${e['deductible_amount']:.2f})")
        if e.get("note"):
            print(f"              📝 {e['note']}")
    print(f"{'─' * 60}")
    print(f"   Total deductible: ${total:.2f}")
    print(f"   Tax savings: ${total * db.get('bracket', 22) / 100:.2f}")


def cmd_audit_risk(db, args):
    _, flags = parse_flags(args)
    year = int(flags.get("year", date.today().year))
    year_expenses = [e for e in db["expenses"] if e["date"].startswith(str(year))]

    risk_points = 0
    warnings = []

    # Check meals
    meals_total = sum(e["deductible_amount"] for e in year_expenses if e.get("category_key") == "meals")
    all_total = sum(e["deductible_amount"] for e in year_expenses)
    if all_total > 0 and meals_total / all_total > 0.03:
        risk_points += 3
        warnings.append(f"Meals are {meals_total/all_total*100:.1f}% of total deductions (>3% is high risk)")

    # Round numbers
    round_count = sum(1 for e in year_expenses if e["amount"] == int(e["amount"]) and e["amount"] > 100)
    if round_count:
        risk_points += round_count
        warnings.append(f"{round_count} round-number expenses over $100 (looks estimated)")

    # Cash expenses
    cash_count = sum(1 for e in year_expenses if "cash" in e.get("note", "").lower())
    if cash_count > 3:
        risk_points += 1
        warnings.append(f"{cash_count} cash transactions noted")

    # Charity
    charity_total = sum(e["deductible_amount"] for e in year_expenses if "charity" in e.get("category_key", ""))
    if charity_total > 5000:
        risk_points += 2
        warnings.append(f"Charitable contributions of ${charity_total:.2f} — ensure written acknowledgment for gifts ≥$250")

    # "Other" category
    other_count = sum(1 for e in year_expenses if e.get("category_key") == "other")
    if other_count > 5:
        risk_points += 2
        warnings.append(f"{other_count} expenses in 'other' — categorize more specifically")

    # Mileage without purpose
    no_purpose = sum(1 for m in db.get("mileage", []) if not m.get("purpose") or m["purpose"] == "Business")
    if no_purpose > 3:
        risk_points += 2
        warnings.append(f"{no_purpose} mileage entries without specific purpose")

    level = "🟢 LOW" if risk_points <= 3 else ("🟡 MODERATE" if risk_points <= 7 else "🔴 HIGH")
    print(f"⚠️  Audit Risk Assessment — Tax Year {year}")
    print(f"{'═' * 55}")
    print(f"   Risk Level: {level} ({risk_points} points)")
    if warnings:
        print(f"\n   ⚠️  Risk Factors:")
        for w in warnings:
            print(f"      • {w}")
    else:
        print(f"\n   ✅ No significant risk factors detected")
    print(f"\n{'═' * 55}")
    print(f"   Note: This is general guidance, not tax advice.")
    print(f"   Consult a CPA for your specific situation.")


def cmd_export(db, args):
    if not args:
        print("Usage: export <schedule-c|schedule-a|csv> [--year YYYY]")
        return
    fmt = args[0]
    _, flags = parse_flags(args[1:])
    year = int(flags.get("year", date.today().year))

    year_expenses = [e for e in db["expenses"] if e["date"].startswith(str(year))]
    year_mileage = [m for m in db.get("mileage", []) if m["date"].startswith(str(year))]

    if fmt == "schedule-c":
        print(f"📋 Schedule C Export — Tax Year {year}")
        print(f"{'═' * 60}")
        sc_cats = {}
        for e in year_expenses:
            if e.get("schedule") == "C":
                key = e.get("category_key", "other")
                info = SCHEDULE_C.get(key, SCHEDULE_C["other"])
                line = info["line"]
                sc_cats.setdefault(line, {"label": info["label"], "amount": 0, "count": 0})
                sc_cats[line]["amount"] += e["deductible_amount"]
                sc_cats[line]["count"] += 1
        # Add mileage to car/truck
        if year_mileage:
            total_mileage_ded = sum(m["deduction"] for m in year_mileage)
            sc_cats.setdefault("9", {"label": "Car and truck expenses", "amount": 0, "count": 0})
            sc_cats["9"]["amount"] += total_mileage_ded
            sc_cats["9"]["count"] += len(year_mileage)
        # Home office
        ho = db.get("home_office", {})
        if ho and str(year) == str(date.today().year):
            sc_cats.setdefault("30", {"label": "Home office (simplified)", "amount": 0, "count": 0})
            sc_cats["30"]["amount"] += ho.get("deduction", 0)
            sc_cats["30"]["count"] = 1

        print(f"\n   Line  Category{' '*22}Amount")
        print(f"   {'─' * 55}")
        total = 0
        for line in sorted(sc_cats.keys(), key=lambda x: (len(x), x)):
            entry = sc_cats[line]
            print(f"   {line:>5s}  {entry['label']:<35s} ${entry['amount']:>10,.2f}  ({entry['count']} entries)")
            total += entry["amount"]
        print(f"   {'─' * 55}")
        print(f"   {'TOTAL':>5s}  {'':<35s} ${total:>10,.2f}")
        bracket = db.get("bracket", 22)
        print(f"\n   💰 Estimated tax savings: ${total * bracket / 100:,.2f}")
        print(f"{'═' * 60}")

    elif fmt == "schedule-a":
        print(f"📋 Schedule A Export — Tax Year {year}")
        print(f"{'═' * 60}")
        sa_cats = {}
        for e in year_expenses:
            if e.get("schedule") == "A":
                key = e.get("category_key", "other")
                info = SCHEDULE_A.get(key, {"label": key})
                label = info.get("label", key)
                sa_cats.setdefault(label, 0)
                sa_cats[label] += e["deductible_amount"]
        total = 0
        for label, amount in sorted(sa_cats.items()):
            print(f"   {label:<35s} ${amount:>10,.2f}")
            total += amount
        print(f"   {'─' * 55}")
        print(f"   {'TOTAL':<35s} ${total:>10,.2f}")
        bracket = db.get("bracket", 22)
        print(f"\n   💰 Estimated tax savings: ${total * bracket / 100:,.2f}")
        print(f"   Note: Subject to AGI floors (medical: 7.5%, SALT cap: $10k)")
        print(f"{'═' * 60}")

    elif fmt == "csv":
        print("date,amount,deductible,category,merchant,note,schedule")
        for e in year_expenses:
            print(f"{e['date']},{e['amount']:.2f},{e['deductible_amount']:.2f},{e['category']},\"{e['merchant']}\",\"{e.get('note', '')}\",{e['schedule']}")
        for m in year_mileage:
            print(f"{m['date']},{m['miles']:.1f},{m['deduction']:.2f},mileage,\"{m['purpose']}\",\"{m['miles']:.0f} miles @ ${m['rate']:.2f}\",C")
        print(f"\n# Exported {len(year_expenses)} expenses + {len(year_mileage)} mileage entries")
    else:
        print(f"Unknown format: {fmt}. Use: schedule-c, schedule-a, or csv")


def cmd_categories(db, args):
    print(f"🏷️  IRS Tax Categories")
    print(f"{'═' * 55}")
    print(f"\n  Schedule C (Business):")
    for key, info in SCHEDULE_C.items():
        ded = f" ({int(info['deductible']*100)}% ded)" if info["deductible"] < 1.0 else ""
        print(f"    Line {info['line']:>4s}  {info['label']}{ded}")
    print(f"\n  Schedule A (Personal):")
    for key, info in SCHEDULE_A.items():
        floor = f" ({info['floor']*100:.1f}% AGI floor)" if info.get("floor") else ""
        print(f"    {info['label']}{floor}")


def cmd_mileage_rate(db, args):
    _, flags = parse_flags(args)
    year = int(flags.get("year", date.today().year))
    rate = MILEAGE_RATES.get(year, MILEAGE_RATES[2026])
    print(f"🚗 IRS Standard Mileage Rates — {year}")
    print(f"{'─' * 40}")
    print(f"   Business:  ${rate['business']:.2f}/mile")
    print(f"   Medical:   ${rate['medical']:.2f}/mile")
    print(f"   Charity:   ${rate['charity']:.2f}/mile")


def cmd_list(db, args):
    _, flags = parse_flags(args)
    year = int(flags.get("year", date.today().year))
    cat_filter = flags.get("category")

    expenses = [e for e in db["expenses"] if e["date"].startswith(str(year))]
    if cat_filter:
        cat_key, _ = lookup_category(cat_filter)
        expenses = [e for e in expenses if e.get("category_key") == cat_key]

    print(f"📋 Expenses — {year} ({len(expenses)} entries)")
    print(f"{'─' * 65}")
    for e in sorted(expenses, key=lambda x: x["date"], reverse=True):
        cat_label = ALL_CATEGORIES.get(e.get("category_key"), {}).get("label", e["category"])
        print(f"   {e['date']} {e['id']}  ${e['amount']:>8.2f}  {e['merchant'][:20]:<20s} {cat_label[:25]}")
    print(f"{'─' * 65}")


def cmd_delete(db, args):
    if len(args) < 1:
        print("Usage: delete <id>")
        return
    exp_id = args[0]
    before = len(db["expenses"])
    db["expenses"] = [e for e in db["expenses"] if e["id"] != exp_id]
    if len(db["expenses"]) < before:
        save_db(db)
        print(f"✓ Deleted expense #{exp_id}")
    else:
        print(f"Not found: #{exp_id}")


# --- Main ---

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    command = sys.argv[1]
    args = sys.argv[2:]
    db = load_db()
    commands = {
        "setup": cmd_setup,
        "add": cmd_add,
        "add-mileage": cmd_add_mileage,
        "add-home-office": cmd_add_home_office,
        "summary": cmd_summary,
        "by-category": cmd_by_category,
        "audit-risk": cmd_audit_risk,
        "export": cmd_export,
        "categories": cmd_categories,
        "mileage-rate": cmd_mileage_rate,
        "list": cmd_list,
        "delete": cmd_delete,
    }
    if command not in commands:
        print(f"Unknown command: {command}")
        print(f"Available: {', '.join(commands.keys())}")
        return
    commands[command](db, args)


if __name__ == "__main__":
    main()
