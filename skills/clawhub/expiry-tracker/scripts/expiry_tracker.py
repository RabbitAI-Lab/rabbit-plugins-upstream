#!/usr/bin/env python3
"""
Expiry Tracker — Track food expiry dates, reduce waste.

Usage:
    python expiry_tracker.py add "milk" --days 7
    python expiry_tracker.py add "chicken" --expiry 2026-08-15
    python expiry_tracker.py list --days 3
    python expiry_tracker.py today
    python expiry_tracker.py inventory
    python expiry_tracker.py remove "milk"
    python expiry_tracker.py report
    python expiry_tracker.py batch "milk, eggs, bread, chicken"
"""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path

DB_PATH = Path.home() / ".expiry_tracker.json"

# Default shelf life in days by category
SHELF_LIFE = {
    "dairy": 7,
    "meat": 3,
    "produce-leafy": 4,
    "produce-root": 14,
    "produce-fruit": 7,
    "bakery": 5,
    "deli": 5,
    "eggs": 21,
    "condiments": 180,
    "tofu": 7,
    "other": 7,
}

# Keyword → category mapping
CATEGORY_KEYWORDS = {
    "dairy": ["milk", "yogurt", "yoghurt", "cheese", "cream", "butter", "kefir", "sour cream", "cottage cheese"],
    "meat": ["chicken", "beef", "pork", "fish", "turkey", "bacon", "sausage", "ham", "steak", "ground", "lamb", "duck", "shrimp", "salmon"],
    "produce-leafy": ["spinach", "lettuce", "salad", "kale", "arugula", "herbs", "cilantro", "parsley", "basil", "spring onion", "green onion"],
    "produce-root": ["carrot", "potato", "onion", "garlic", "ginger", "beet", "turnip", "radish", "sweet potato", "leek"],
    "produce-fruit": ["berry", "berries", "banana", "apple", "orange", "lemon", "lime", "grape", "mango", "pineapple", "peach", "plum", "pear", "avocado", "tomato", "strawberry", "blueberry", "raspberry"],
    "bakery": ["bread", "bagel", "tortilla", "bun", "roll", "pastry", "cake", "muffin", "croissant", "pancake", "naan", "pita"],
    "deli": ["cold cut", "salami", "prosciutto", "ham slice", "prepared salad", "coleslaw", "hummus", "tzatziki"],
    "eggs": ["egg"],
    "condiments": ["sauce", "dressing", "ketchup", "mustard", "mayo", "relish", "chutney", "jam", "jelly"],
    "tofu": ["tofu", "tempeh", "seitan"],
}

# Priority recipes for soon-to-expire items
RECIPE_HINTS = {
    "dairy": "Use in a creamy pasta sauce, smoothie, or bake into a casserole",
    "meat": "Cook tonight! Freeze if you can't use it today",
    "produce-leafy": "Make a big salad, stir-fry, or blend into a green smoothie",
    "produce-fruit": "Bake into a crumble, make a smoothie, or freeze for later",
    "bakery": "Make croutons, bread pudding, or freeze for toast",
    "eggs": "Hard-boil them (lasts 7 more days) or make a frittata",
    "deli": "Use in a sandwich or cook into a pasta dish",
    "tofu": "Stir-fry or scramble — tofu freezes well too",
}


def categorize(name: str) -> str:
    """Guess category from item name."""
    name_lower = name.lower()
    for cat, keywords in CATEGORY_KEYWORDS.items():
        for kw in keywords:
            if kw in name_lower:
                return cat
    return "other"


def load_db() -> dict:
    """Load the expiry tracker database."""
    if DB_PATH.exists():
        return json.loads(DB_PATH.read_text())
    return {"items": [], "waste_log": [], "created": datetime.now().isoformat()}


def save_db(db: dict):
    """Save the expiry tracker database."""
    db["updated"] = datetime.now().isoformat()
    DB_PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False))


def parse_date(s: str) -> datetime:
    """Parse a date string in common formats."""
    for fmt in ("%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y", "%m/%d/%Y", "%d-%m-%Y"):
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            pass
    # Try relative: "3d", "1w"
    s = s.strip().lower()
    if s.endswith("d"):
        return datetime.now() + timedelta(days=int(s[:-1]))
    if s.endswith("w"):
        return datetime.now() + timedelta(weeks=int(s[:-1]))
    raise ValueError(f"Cannot parse date: {s}")


def fmt_date(dt: datetime) -> str:
    return dt.strftime("%b %d")


def days_until(dt: datetime) -> int:
    return (dt.date() - datetime.now().date()).days


def urgency_emoji(days: int) -> str:
    if days < 0:
        return "🔴"
    elif days == 0:
        return "🟠"
    elif days <= 2:
        return "🟡"
    elif days <= 5:
        return "🟢"
    return "⚪"


def cmd_add(args):
    """Add an item to the tracker."""
    db = load_db()
    now = datetime.now()

    if args.expiry:
        exp_date = parse_date(args.expiry)
    elif args.days:
        exp_date = now + timedelta(days=args.days)
    else:
        cat = categorize(args.name)
        days = SHELF_LIFE.get(cat, 7)
        exp_date = now + timedelta(days=days)
        print(f"  (guessed category: {cat}, shelf life: {days}d)")

    item = {
        "name": args.name,
        "category": categorize(args.name),
        "added": now.strftime("%Y-%m-%d"),
        "expiry": exp_date.strftime("%Y-%m-%d"),
        "quantity": args.quantity or 1,
        "note": args.note or "",
    }

    db["items"].append(item)
    save_db(db)

    d = days_until(exp_date)
    print(f"✅ Added: {args.name} — expires {fmt_date(exp_date)} ({d}d)")


def cmd_remove(args):
    """Remove an item (consumed or tossed)."""
    db = load_db()
    name_lower = args.name.lower()

    removed = []
    keep = []
    for item in db["items"]:
        if name_lower in item["name"].lower():
            removed.append(item)
        else:
            keep.append(item)

    if not removed:
        print(f"❌ No item matching '{args.name}' found.")
        return

    db["items"] = keep

    if args.wasted:
        for item in removed:
            entry = {**item, "action": "wasted", "date": datetime.now().strftime("%Y-%m-%d")}
            db.setdefault("waste_log", []).append(entry)
        print(f"🗑️  Marked as WASTED: {', '.join(i['name'] for i in removed)}")
    else:
        for item in removed:
            entry = {**item, "action": "consumed", "date": datetime.now().strftime("%Y-%m-%d")}
            db.setdefault("waste_log", []).append(entry)
        print(f"✅ Marked as consumed: {', '.join(i['name'] for i in removed)}")

    save_db(db)


def cmd_list(args):
    """List items, optionally filtered by days until expiry."""
    db = load_db()
    if not db["items"]:
        print("📦 Inventory is empty. Add items with 'add'.")
        return

    items = []
    for item in db["items"]:
        d = days_until(datetime.strptime(item["expiry"], "%Y-%m-%d"))
        if args.days is None or d <= args.days:
            items.append((d, item))

    items.sort(key=lambda x: x[0])

    print(f"{'':3s} {'Item':<25s} {'Expires':<12s} {'Days':>5s}  Category")
    print("─" * 65)
    for d, item in items:
        emoji = urgency_emoji(d)
        status = "EXPIRED" if d < 0 else f"{d}d"
        print(f"{emoji}  {item['name']:<25s} {item['expiry']:<12s} {status:>5s}  {item['category']}")


def cmd_today(args):
    """Show what to use today — items expiring within 48h."""
    db = load_db()
    if not db["items"]:
        print("📦 Nothing in inventory.")
        return

    urgent = []
    for item in db["items"]:
        d = days_until(datetime.strptime(item["expiry"], "%Y-%m-%d"))
        if d <= 2:
            urgent.append((d, item))

    if not urgent:
        print("✅ Nothing urgent! All items have >2 days left.")
        # Show next to expire
        items = [(days_until(datetime.strptime(i["expiry"], "%Y-%m-%d")), i) for i in db["items"]]
        items.sort(key=lambda x: x[0])
        if items:
            d, item = items[0]
            print(f"📅 Next: {item['name']} — expires in {d}d ({item['expiry']})")
        return

    urgent.sort(key=lambda x: x[0])

    print("⚠️  USE THESE TODAY/TOMORROW:\n")
    for d, item in urgent:
        emoji = urgency_emoji(d)
        hint = RECIPE_HINTS.get(item["category"], "Use it soon!")
        status = "EXPIRED" if d < 0 else ("TODAY" if d == 0 else f"in {d}d")
        print(f"  {emoji} {item['name']} — {status}")
        print(f"     💡 {hint}")
        print()


def cmd_inventory(args):
    """Show full inventory sorted by expiry date."""
    db = load_db()
    if not db["items"]:
        print("📦 Inventory is empty.")
        return

    items = [(days_until(datetime.strptime(i["expiry"], "%Y-%m-%d")), i) for i in db["items"]]
    items.sort(key=lambda x: x[0])

    print(f"📦 FULL INVENTORY ({len(items)} items)\n")
    total_value = 0
    for d, item in items:
        emoji = urgency_emoji(d)
        status = "EXPIRED" if d < 0 else f"{d}d"
        qty = f" x{item['quantity']}" if item.get("quantity", 1) > 1 else ""
        note = f"  📝 {item['note']}" if item.get("note") else ""
        print(f"  {emoji} {item['name']}{qty} — {item['expiry']} ({status})  [{item['category']}]{note}")


def cmd_report(args):
    """Show waste statistics."""
    db = load_db()
    waste_log = db.get("waste_log", [])

    if not waste_log:
        print("📊 No waste data yet. Use 'remove --wasted' when food goes bad.")
        return

    consumed = [e for e in waste_log if e["action"] == "consumed"]
    wasted = [e for e in waste_log if e["action"] == "wasted"]
    total = len(waste_log)

    print("📊 WASTE REPORT\n")
    print(f"  Total items tracked: {total}")
    print(f"  ✅ Consumed: {len(consumed)} ({100*len(consumed)/total:.0f}%)")
    print(f"  🗑️  Wasted:  {len(wasted)} ({100*len(wasted)/total:.0f}%)")

    if wasted:
        print(f"\n  Wasted items:")
        for e in wasted:
            print(f"    • {e['name']} ({e.get('category', '?')}) — tossed {e['date']}")

    # Category breakdown
    cats = {}
    for e in waste_log:
        cat = e.get("category", "other")
        cats.setdefault(cat, {"consumed": 0, "wasted": 0})
        cats[cat][e["action"]] = cats[cat].get(e["action"], 0) + 1

    print(f"\n  By category:")
    for cat, counts in sorted(cats.items()):
        total_cat = counts["consumed"] + counts["wasted"]
        waste_rate = 100 * counts["wasted"] / total_cat if total_cat else 0
        print(f"    {cat:<20s} consumed={counts['consumed']:>2d}  wasted={counts['wasted']:>2d}  waste={waste_rate:.0f}%")


def cmd_batch(args):
    """Bulk add items from comma-separated text."""
    items = [s.strip() for s in args.items.split(",") if s.strip()]
    if not items:
        print("No items found. Separate with commas.")
        return

    db = load_db()
    now = datetime.now()

    for name in items:
        cat = categorize(name)
        days = SHELF_LIFE.get(cat, 7)
        exp_date = now + timedelta(days=days)

        item = {
            "name": name,
            "category": cat,
            "added": now.strftime("%Y-%m-%d"),
            "expiry": exp_date.strftime("%Y-%m-%d"),
            "quantity": 1,
            "note": f"auto: {cat}, {days}d",
        }
        db["items"].append(item)
        d = days_until(exp_date)
        print(f"✅ {name:<20s} → {cat:<15s} expires {exp_date.strftime('%b %d')} ({d}d)")

    save_db(db)
    print(f"\nAdded {len(items)} items.")


def main():
    parser = argparse.ArgumentParser(
        description="Track food expiry dates and reduce waste.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command", help="Command to run")

    # add
    p_add = sub.add_parser("add", help="Add an item to track")
    p_add.add_argument("name", help="Item name (e.g. 'milk', 'chicken breast')")
    g = p_add.add_mutually_exclusive_group()
    g.add_argument("--days", type=int, help="Days until expiry (default: auto from category)")
    g.add_argument("--expiry", help="Expiry date (YYYY-MM-DD, DD.MM.YYYY, or '3d'/'1w')")
    p_add.add_argument("--quantity", type=int, help="Quantity (default: 1)")
    p_add.add_argument("--note", help="Optional note")
    p_add.set_defaults(func=cmd_add)

    # remove
    p_rm = sub.add_parser("remove", help="Remove an item (consumed or wasted)")
    p_rm.add_argument("name", help="Item name to remove (fuzzy match)")
    p_rm.add_argument("--wasted", action="store_true", help="Mark as wasted (not consumed)")
    p_rm.set_defaults(func=cmd_remove)

    # list
    p_list = sub.add_parser("list", help="List items, optionally filtered")
    p_list.add_argument("--days", type=int, default=None, help="Only items expiring within N days")
    p_list.set_defaults(func=cmd_list)

    # today
    p_today = sub.add_parser("today", help="Show what to use today/tomorrow")
    p_today.set_defaults(func=cmd_today)

    # inventory
    p_inv = sub.add_parser("inventory", help="Show full inventory")
    p_inv.set_defaults(func=cmd_inventory)

    # report
    p_report = sub.add_parser("report", help="Show waste statistics")
    p_report.set_defaults(func=cmd_report)

    # batch
    p_batch = sub.add_parser("batch", help="Bulk add from comma-separated list")
    p_batch.add_argument("items", help='Comma-separated items, e.g. "milk, eggs, bread"')
    p_batch.set_defaults(func=cmd_batch)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(1)

    args.func(args)


if __name__ == "__main__":
    main()
