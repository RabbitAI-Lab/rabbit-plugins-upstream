#!/usr/bin/env python3
"""
Home Inventory Manager
======================
Manage a JSON database of household items for insurance, moving, or estate planning.

Commands: add, list, search, by-room, total-value, export-csv,
          insurance-report, depreciation-report, assign-box, box-manifest

Python 3.8+ stdlib only — no external dependencies.
"""

import argparse
import csv
import json
import os
import sys
from datetime import date, datetime

# ---------------------------------------------------------------------------
# Depreciation configuration
#   rate > 0  => value decreases (depreciation)
#   rate < 0  => value increases (appreciation)
#   "rate" is annual, applied linearly up to max_age years, then held flat.
# ---------------------------------------------------------------------------

DEPRECIATION_RATES = {
    # category: (annual_rate, typical_lifespan_years)
    "electronics":      (0.25, 5),
    "appliances":       (0.12, 10),
    "furniture":        (0.08, 15),
    "clothing":         (0.20, 5),
    "tools":            (0.10, 12),
    "sports":           (0.12, 8),
    "books":            (0.10, 20),
    "jewelry":          (-0.03, 100),   # appreciates ~3%/yr
    "art":              (-0.05, 100),   # appreciates ~5%/yr
    "collectibles":     (-0.04, 100),
    "vehicles":         (0.15, 12),
    "musical":          (0.06, 25),
    "other":            (0.10, 10),
}

DEFAULT_DB = "inventory.json"

HIGH_VALUE_THRESHOLD = 1000.00


# ---------------------------------------------------------------------------
# Database helpers
# ---------------------------------------------------------------------------

def load_db(path):
    if not os.path.exists(path):
        return {"items": [], "next_id": 1}
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if "items" not in data:
        data["items"] = []
    if "next_id" not in data:
        data["next_id"] = max((i["id"] for i in data["items"]), default=0) + 1
    return data


def save_db(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def find_item(data, item_id):
    for item in data["items"]:
        if item["id"] == item_id:
            return item
    return None


# ---------------------------------------------------------------------------
# Item creation
# ---------------------------------------------------------------------------

def add_item(data, args):
    item = {
        "id": data["next_id"],
        "name": args.name,
        "category": (args.category or "other").lower(),
        "room": (args.room or "unassigned").lower(),
        "purchase_date": args.purchase_date or "",
        "estimated_value": float(args.value or 0),
        "brand_model": args.brand_model or "",
        "serial_number": args.serial or "",
        "photo_path": args.photo or "",
        "qr_label_id": args.qr or "",
        "box_id": "",
        "notes": args.notes or "",
    }
    data["items"].append(item)
    data["next_id"] += 1
    return item


# ---------------------------------------------------------------------------
# Depreciation calculation
# ---------------------------------------------------------------------------

def years_since(purchase_date_str):
    """Return years since purchase_date_str (ISO YYYY-MM-DD). 0 if unparseable."""
    if not purchase_date_str:
        return 0
    try:
        pd = datetime.strptime(purchase_date_str, "%Y-%m-%d").date()
    except ValueError:
        return 0
    delta = date.today() - pd
    return max(delta.days / 365.25, 0)


def depreciated_value(item):
    """Return (current_value, annual_rate, lifespan) for an item."""
    cat = item.get("category", "other")
    rate, lifespan = DEPRECIATION_RATES.get(cat, DEPRECIATION_RATES["other"])
    yrs = years_since(item.get("purchase_date", ""))
    effective_yrs = min(yrs, lifespan)
    original = item.get("estimated_value", 0)
    if rate < 0:
        # appreciation — no cap
        current = original * (1 + abs(rate) * yrs)
    else:
        current = original * max(1 - rate * effective_yrs, 0)
    return round(current, 2), rate, lifespan


# ---------------------------------------------------------------------------
# Formatting helpers
# ---------------------------------------------------------------------------

def fmt_money(v):
    return f"${v:,.2f}"


def print_item(item, show_depreciation=False):
    print(f"  [{item['id']}] {item['name']}  "
          f"({item['category']}, {item['room']})  "
          f"{fmt_money(item.get('estimated_value', 0))}")
    details = []
    if item.get("brand_model"):
        details.append(f"brand/model: {item['brand_model']}")
    if item.get("serial_number"):
        details.append(f"serial: {item['serial_number']}")
    if item.get("purchase_date"):
        details.append(f"purchased: {item['purchase_date']}")
    if item.get("qr_label_id"):
        details.append(f"QR: {item['qr_label_id']}")
    if item.get("box_id"):
        details.append(f"box: {item['box_id']}")
    if item.get("notes"):
        details.append(f"notes: {item['notes']}")
    if details:
        print(f"       " + " | ".join(details))
    if show_depreciation:
        cv, rate, lifespan = depreciated_value(item)
        direction = "appreciates" if rate < 0 else "depreciates"
        print(f"       current value: {fmt_money(cv)} "
              f"({direction} {abs(rate)*100:.0f}%/yr, {lifespan}yr lifespan)")


def print_items_table(items, show_depreciation=False):
    if not items:
        print("  (no items)")
        return
    for item in items:
        print_item(item, show_depreciation)


# ---------------------------------------------------------------------------
# Command handlers
# ---------------------------------------------------------------------------

def cmd_add(args, data, db_path):
    item = add_item(data, args)
    save_db(db_path, data)
    print(f"Added item #{item['id']}: {item['name']}")


def cmd_list(args, data, db_path):
    items = data["items"]
    print(f"\n{'='*60}")
    print(f"  HOME INVENTORY — {len(items)} item(s)")
    print(f"{'='*60}")
    print_items_table(items, show_depreciation=args.with_depreciation)
    print()


def cmd_search(args, data, db_path):
    q = args.query.lower()
    results = []
    for item in data["items"]:
        haystack = " ".join(str(v) for v in item.values()).lower()
        if q in haystack:
            results.append(item)
    print(f"\nSearch results for '{args.query}' — {len(results)} match(es):\n")
    print_items_table(results)
    print()


def cmd_by_room(args, data, db_path):
    room = args.room.lower()
    results = [i for i in data["items"] if i.get("room", "").lower() == room]
    total = sum(i.get("estimated_value", 0) for i in results)
    print(f"\nRoom '{room}' — {len(results)} item(s), total {fmt_money(total)}:\n")
    print_items_table(results)
    print()


def cmd_total_value(args, data, db_path):
    items = data["items"]
    replacement = sum(i.get("estimated_value", 0) for i in items)
    depreciated = sum(depreciated_value(i)[0] for i in items)
    print(f"\n{'='*50}")
    print(f"  TOTAL INVENTORY VALUE")
    print(f"{'='*50}")
    print(f"  Items:              {len(items)}")
    print(f"  Replacement cost:   {fmt_money(replacement)}")
    print(f"  Depreciated value:  {fmt_money(depreciated)}")
    print(f"  Difference:         {fmt_money(depreciated - replacement)}")
    print()


def cmd_export_csv(args, data, db_path):
    output = args.output or "inventory_export.csv"
    fields = [
        "id", "name", "category", "room", "purchase_date",
        "estimated_value", "brand_model", "serial_number",
        "photo_path", "qr_label_id", "box_id", "notes",
    ]
    with open(output, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for item in data["items"]:
            writer.writerow(item)
    print(f"Exported {len(data['items'])} item(s) to {output}")


def cmd_insurance_report(args, data, db_path):
    items = data["items"]
    if not items:
        print("No items in inventory.")
        return

    total_replacement = sum(i.get("estimated_value", 0) for i in items)
    total_depreciated = sum(depreciated_value(i)[0] for i in items)

    # By room
    rooms = {}
    for item in items:
        room = item.get("room", "unassigned")
        rooms.setdefault(room, []).append(item)

    # By category
    categories = {}
    for item in items:
        cat = item.get("category", "other")
        categories.setdefault(cat, []).append(item)

    high_value = [i for i in items if i.get("estimated_value", 0) >= HIGH_VALUE_THRESHOLD]

    print(f"\n{'#'*60}")
    print(f"#  INSURANCE REPORT — {date.today().isoformat()}")
    print(f"{'#'*60}")
    print(f"\nSUMMARY")
    print(f"  Total items:           {len(items)}")
    print(f"  Total replacement cost: {fmt_money(total_replacement)}")
    print(f"  Total depreciated value:{fmt_money(total_depreciated)}")
    print(f"  High-value items (≥{fmt_money(HIGH_VALUE_THRESHOLD)}): {len(high_value)}")

    print(f"\n{'—'*50}")
    print("BY ROOM")
    for room in sorted(rooms):
        room_items = rooms[room]
        room_total = sum(i.get("estimated_value", 0) for i in room_items)
        print(f"\n  {room.upper()} — {len(room_items)} item(s) — {fmt_money(room_total)}")
        for item in room_items:
            flag = " ⚠" if item.get("estimated_value", 0) >= HIGH_VALUE_THRESHOLD else ""
            print(f"    [{item['id']}] {item['name']} — {fmt_money(item.get('estimated_value', 0))}{flag}")

    print(f"\n{'—'*50}")
    print("BY CATEGORY")
    for cat in sorted(categories):
        cat_items = categories[cat]
        cat_total = sum(i.get("estimated_value", 0) for i in cat_items)
        cat_dep = sum(depreciated_value(i)[0] for i in cat_items)
        print(f"  {cat:20s}  {len(cat_items):3d} items  "
              f"replacement {fmt_money(cat_total):>12s}  "
              f"depreciated {fmt_money(cat_dep):>12s}")

    print(f"\n{'—'*50}")
    print("HIGH-VALUE ITEMS")
    if high_value:
        for item in sorted(high_value, key=lambda i: i.get("estimated_value", 0), reverse=True):
            print(f"  [{item['id']}] {item['name']}  "
                  f"({item['category']}, {item['room']})  "
                  f"{fmt_money(item['estimated_value'])}")
    else:
        print("  (none)")

    print(f"\n{'#'*60}")
    print()


def cmd_depreciation_report(args, data, db_path):
    items = data["items"]
    if not items:
        print("No items in inventory.")
        return

    print(f"\n{'#'*60}")
    print(f"#  DEPRECIATION REPORT — {date.today().isoformat()}")
    print(f"{'#'*60}")

    # Group by category
    categories = {}
    for item in items:
        cat = item.get("category", "other")
        categories.setdefault(cat, []).append(item)

    print(f"\n{'Category':20s} {'Items':>5s}  {'Original':>12s}  "
          f"{'Current':>12s}  {'Change':>12s}  {'Rate/yr':>8s}")
    print(f"{'—'*75}")

    grand_orig = 0
    grand_curr = 0

    for cat in sorted(categories):
        cat_items = categories[cat]
        orig = sum(i.get("estimated_value", 0) for i in cat_items)
        curr = sum(depreciated_value(i)[0] for i in cat_items)
        rate = DEPRECIATION_RATES.get(cat, DEPRECIATION_RATES["other"])[0]
        direction = "-" if rate > 0 else "+"
        change = curr - orig
        grand_orig += orig
        grand_curr += curr
        print(f"{cat:20s} {len(cat_items):5d}  {fmt_money(orig):>12s}  "
              f"{fmt_money(curr):>12s}  {fmt_money(change):>12s}  "
              f"{direction}{abs(rate)*100:.0f}%")

    print(f"{'—'*75}")
    change = grand_curr - grand_orig
    print(f"{'TOTAL':20s} {len(items):5d}  {fmt_money(grand_orig):>12s}  "
          f"{fmt_money(grand_curr):>12s}  {fmt_money(change):>12s}")

    print(f"\nPer-item detail:\n")
    for item in sorted(items, key=lambda i: i.get("estimated_value", 0), reverse=True):
        cv, rate, lifespan = depreciated_value(item)
        yrs = years_since(item.get("purchase_date", ""))
        print(f"  [{item['id']}] {item['name']:30s}  "
              f"{item['category']:14s}  "
              f"orig {fmt_money(item.get('estimated_value',0)):>10s}  "
              f"now {fmt_money(cv):>10s}  "
              f"({yrs:.1f} yrs)")
    print()


def cmd_assign_box(args, data, db_path):
    item = find_item(data, args.item_id)
    if not item:
        print(f"Error: item #{args.item_id} not found.")
        sys.exit(1)
    item["box_id"] = args.box
    save_db(db_path, data)
    print(f"Assigned item #{item['id']} ({item['name']}) to box {args.box}")


def cmd_box_manifest(args, data, db_path):
    box_id = args.box
    box_items = [i for i in data["items"] if i.get("box_id", "").upper() == box_id.upper()]
    if not box_items:
        print(f"No items assigned to box {box_id}.")
        return

    total = sum(i.get("estimated_value", 0) for i in box_items)

    print(f"\n{'='*50}")
    print(f"  BOX MANIFEST — {box_id}")
    print(f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"  Items: {len(box_items)}")
    print(f"  Total value: {fmt_money(total)}")
    print(f"{'='*50}")
    for i, item in enumerate(box_items, 1):
        print(f"  {i}. {item['name']}  ({item['category']}, {item['room']})")
        if item.get("brand_model"):
            print(f"     brand/model: {item['brand_model']}")
    print(f"{'='*50}")

    # QR-friendly compact summary (single line, pipe-delimited)
    names = "|".join(i["name"] for i in box_items)
    qr_data = f"BOX:{box_id}|N:{len(box_items)}|V:{total:.0f}|{names}"
    print(f"\nQR data (compact):")
    print(f"  {qr_data}")
    print(f"\n  Tip: pipe this string into any QR code generator:")
    print(f"  echo '{qr_data}' | qrencode -o {box_id}.png")
    print()


# ---------------------------------------------------------------------------
# Argument parsing
# ---------------------------------------------------------------------------

def build_parser():
    parser = argparse.ArgumentParser(
        description="Home Inventory Manager — track items for insurance, moving, estate planning.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--db", default=DEFAULT_DB, help=f"Path to JSON database (default: {DEFAULT_DB})")
    sub = parser.add_subparsers(dest="command", required=True)

    # add
    p_add = sub.add_parser("add", help="Add a new item")
    p_add.add_argument("--name", required=True)
    p_add.add_argument("--category", default=None)
    p_add.add_argument("--room", default=None)
    p_add.add_argument("--value", type=float, default=0, help="Estimated replacement value")
    p_add.add_argument("--brand-model", dest="brand_model", default=None)
    p_add.add_argument("--serial", default=None, help="Serial number")
    p_add.add_argument("--purchase-date", default=None, help="YYYY-MM-DD")
    p_add.add_argument("--photo", default=None, help="Path to photo file")
    p_add.add_argument("--qr", default=None, help="QR label ID")
    p_add.add_argument("--notes", default=None)
    p_add.set_defaults(func=cmd_add)

    # list
    p_list = sub.add_parser("list", help="List all items")
    p_list.add_argument("--with-depreciation", action="store_true", help="Show current depreciated value")
    p_list.set_defaults(func=cmd_list)

    # search
    p_search = sub.add_parser("search", help="Search by keyword")
    p_search.add_argument("query")
    p_search.set_defaults(func=cmd_search)

    # by-room
    p_room = sub.add_parser("by-room", help="List items in a room")
    p_room.add_argument("room")
    p_room.set_defaults(func=cmd_by_room)

    # total-value
    p_tv = sub.add_parser("total-value", help="Total value summary")
    p_tv.set_defaults(func=cmd_total_value)

    # export-csv
    p_csv = sub.add_parser("export-csv", help="Export to CSV")
    p_csv.add_argument("--output", "-o", default=None)
    p_csv.set_defaults(func=cmd_export_csv)

    # insurance-report
    p_ins = sub.add_parser("insurance-report", help="Generate insurance report")
    p_ins.set_defaults(func=cmd_insurance_report)

    # depreciation-report
    p_dep = sub.add_parser("depreciation-report", help="Depreciation by category")
    p_dep.set_defaults(func=cmd_depreciation_report)

    # assign-box
    p_box = sub.add_parser("assign-box", help="Assign an item to a moving box")
    p_box.add_argument("--item-id", type=int, required=True)
    p_box.add_argument("--box", required=True, help="Box ID (e.g. BOX-001)")
    p_box.set_defaults(func=cmd_assign_box)

    # box-manifest
    p_manifest = sub.add_parser("box-manifest", help="Generate a box manifest")
    p_manifest.add_argument("box", help="Box ID")
    p_manifest.set_defaults(func=cmd_box_manifest)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    db_path = args.db
    data = load_db(db_path)
    args.func(args, data, db_path)


if __name__ == "__main__":
    main()
