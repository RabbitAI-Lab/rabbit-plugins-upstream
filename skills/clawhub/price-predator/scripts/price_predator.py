#!/usr/bin/env python3
"""
Price Predator — Track product prices, get alerts, predict the best time to buy.

Pure Python stdlib. No external dependencies.

Usage:
    python3 price_predator.py track --name "Sony WH-1000XM5" --price 350.00 --category electronics
    python3 price_predator.py track --url "https://example.com/product/123"
    python3 price_predator.py update <product-id> --price 299.99
    python3 price_predator.py history <product-id>
    python3 price_predator.py alert [product-id]
    python3 price_predator.py best-time --category electronics
    python3 price_predator.py report
    python3 price_predator.py list
    python3 price_predator.py remove <product-id>
    python3 price_predator.py info <product-id>

Database is a JSON file stored at ~/.price_predator_db.json by default.
Override with --db /path/to/db.json.
"""

import argparse
import json
import os
import statistics
import sys
import uuid
from datetime import datetime, timedelta
from pathlib import Path

DEFAULT_DB = Path.home() / ".price_predator_db.json"

# ── Seasonal buying calendar ────────────────────────────────────────────────
# Maps category → {month_num: short description} of best times to buy.
SEASONAL_CALENDAR = {
    "electronics": {
        "best_months": [11, 12],
        "note": "Black Friday (Nov) and Cyber Monday/December holiday sales offer the deepest discounts on TVs, laptops, headphones, and gadgets.",
        "secondary_months": [(7, "Amazon Prime Day"), (8, "Back-to-school sales on laptops")],
    },
    "mattresses": {
        "best_months": [5],
        "note": "May (Memorial Day sales) is prime mattress season. Presidents' Day (Feb) is a secondary window.",
        "secondary_months": [(2, "Presidents' Day sales"), (9, "Labor Day sales")],
    },
    "appliances": {
        "best_months": [9, 5],
        "note": "September (Labor Day) and May (Memorial Day) bring major appliance clearance events.",
        "secondary_months": [(11, "Black Friday"), (1, "New Year clearance")],
    },
    "clothing": {
        "best_months": [1, 7],
        "note": "End-of-season clearance: January (winter clothes), July (summer clothes).",
        "secondary_months": [(8, "Back-to-school"), (12, "Post-holiday clearance")],
    },
    "furniture": {
        "best_months": [1, 7],
        "note": "Furniture dealers clear inventory in January and July to make room for new lines.",
        "secondary_months": [(11, "Black Friday"), (5, "Memorial Day")],
    },
    "toys": {
        "best_months": [11, 12],
        "note": "November–December holiday shopping season; deepest toy discounts in early December.",
        "secondary_months": [(1, "Post-holiday clearance"), (7, "Summer toy clearance")],
    },
    "tv": {
        "best_months": [11, 1],
        "note": "Black Friday (Nov) is the biggest TV discount event. January brings Super Bowl promos.",
        "secondary_months": [(11, "Black Friday"), (1, "Super Bowl sales")],
    },
    "laptops": {
        "best_months": [11, 8],
        "note": "Black Friday / Cyber Monday (Nov) and back-to-school (Aug) are best for laptops.",
        "secondary_months": [(7, "Amazon Prime Day"), (4, "Spring refresh cycle")],
    },
    "smartphones": {
        "best_months": [9, 11],
        "note": "New iPhones/Androids launch Sep–Oct; prior models drop. Black Friday adds more discounts.",
        "secondary_months": [(3, "Spring launch events"), (11, "Black Friday")],
    },
    "cameras": {
        "best_months": [11, 4],
        "note": "Black Friday (Nov) and April (spring rebate season) offer camera deals.",
        "secondary_months": [(1, "CES clearance"), (9, "Photokina season")],
    },
    "video-games": {
        "best_months": [11, 12],
        "note": "Black Friday (Nov) and holiday (Dec) sales on games and consoles.",
        "secondary_months": [(6, "E3 / Summer Game Fest promos"), (1, "Steam Winter Sale end")],
    },
    "tools": {
        "best_months": [6, 12],
        "note": "Father's Day (June) and holiday/December sales for power tools and hardware.",
        "secondary_months": [(11, "Black Friday"), (5, "Spring DIY promos")],
    },
    "fitness": {
        "best_months": [1, 12],
        "note": "January (New Year resolutions) and December holiday sales on fitness equipment.",
        "secondary_months": [(9, "End of outdoor fitness season clearance"), (5, "Memorial Day")],
    },
    "outdoor": {
        "best_months": [9, 8],
        "note": "End-of-summer clearance (Aug–Sep) is best for grills, patio furniture, and camping gear.",
        "secondary_months": [(5, "Memorial Day"), (11, "Black Friday")],
    },
    "jewelry": {
        "best_months": [1, 7],
        "note": "Post-holiday (Jan) and mid-summer (Jul) are slower jewelry periods with better prices.",
        "secondary_months": [(2, "Valentine's clearance"), (11, "Black Friday")],
    },
    "generic": {
        "best_months": [11],
        "note": "November (Black Friday / Cyber Monday) is the broadest discount window across categories.",
        "secondary_months": [(7, "Amazon Prime Day"), (1, "New Year clearance")],
    },
}

# Default depreciation pattern: expected year-over-year price decline as a fraction.
# Used for prediction when there isn't enough history.
DEPRECIATION_RATES = {
    "electronics": 0.15,
    "smartphones": 0.25,
    "laptops": 0.18,
    "tv": 0.20,
    "cameras": 0.15,
    "video-games": 0.12,
    "mattresses": 0.05,
    "appliances": 0.05,
    "furniture": 0.04,
    "clothing": 0.10,
    "toys": 0.08,
    "tools": 0.06,
    "fitness": 0.08,
    "outdoor": 0.06,
    "jewelry": 0.03,
    "generic": 0.08,
}

MONTH_NAMES = [
    "", "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]

# ── Database helpers ────────────────────────────────────────────────────────

def load_db(db_path: Path) -> dict:
    if db_path.exists() and db_path.stat().st_size > 0:
        with open(db_path, "r") as f:
            return json.load(f)
    return {"products": {}}

def save_db(db_path: Path, db: dict):
    db_path.parent.mkdir(parents=True, exist_ok=True)
    with open(db_path, "w") as f:
        json.dump(db, f, indent=2)


# ── Commands ────────────────────────────────────────────────────────────────

def cmd_track(args, db):
    """Add a product to track."""
    pid = args.id or uuid.uuid4().hex[:8]
    now = datetime.now().isoformat(timespec="seconds")

    if pid in db["products"]:
        print(f"Error: Product '{pid}' already exists. Use 'update' to add a price observation.")
        sys.exit(1)

    if not args.name and args.url:
        args.name = args.url  # default name to URL if not provided

    product = {
        "id": pid,
        "name": args.name or "Unnamed Product",
        "url": args.url or "",
        "category": args.category or "generic",
        "target_price": args.target,
        "alert_threshold": args.threshold if args.threshold is not None else 0.10,
        "created_at": now,
        "price_history": [],
    }

    if args.price is not None:
        product["price_history"].append({
            "price": round(args.price, 2),
            "timestamp": now,
            "source": args.source or "manual",
        })

    db["products"][pid] = product
    save_db(Path(args.db), db)
    print(f"✅ Tracking product '{product['name']}' (id: {pid})")
    if args.price is not None:
        print(f"   Initial price: ${args.price:.2f}")
    print(f"   Category: {product['category']}")


def cmd_update(args, db):
    """Record a new price observation for a tracked product."""
    pid = args.product_id
    if pid not in db["products"]:
        print(f"Error: Product '{pid}' not found.")
        sys.exit(1)

    now = datetime.now().isoformat(timespec="seconds")
    entry = {
        "price": round(args.price, 2),
        "timestamp": now,
        "source": args.source or "manual",
    }
    db["products"][pid]["price_history"].append(entry)
    save_db(Path(args.db), db)

    history = db["products"][pid]["price_history"]
    prev = history[-2]["price"] if len(history) >= 2 else None
    print(f"✅ Updated '{db['products'][pid]['name']}' → ${args.price:.2f}")
    if prev is not None:
        diff = args.price - prev
        pct = (diff / prev) * 100 if prev else 0
        arrow = "↓" if diff < 0 else ("↑" if diff > 0 else "=")
        print(f"   {arrow} {abs(diff):+.2f} ({pct:+.1f}%) from previous ${prev:.2f}")


def cmd_history(args, db):
    """Show price history with ASCII sparkline chart."""
    pid = args.product_id
    if pid not in db["products"]:
        print(f"Error: Product '{pid}' not found.")
        sys.exit(1)

    product = db["products"][pid]
    history = product["price_history"]
    if not history:
        print(f"No price history for '{product['name']}'.")
        return

    print(f"\n📊 Price History: {product['name']} (id: {pid})")
    print(f"   Category: {product['category']}")
    print(f"   Observations: {len(history)}")
    prices = [h["price"] for h in history]
    print(f"   Low: ${min(prices):.2f}  High: ${max(prices):.2f}  "
          f"Median: ${statistics.median(prices):.2f}  Latest: ${prices[-1]:.2f}\n")

    sparkline = sparkline_chart(prices)
    print(f"   Sparkline: {sparkline}")
    print(f"   {min(prices):.0f}" + " " * (len(sparkline) - 4) + f"{max(prices):.0f}\n")

    print("   Date                     Price     Source")
    print("   " + "-" * 55)
    for h in history:
        print(f"   {h['timestamp'][:19]:24s} ${h['price']:8.2f}  {h['source']}")


def cmd_alert(args, db):
    """Check for price drops exceeding the alert threshold."""
    pids = [args.product_id] if args.product_id else list(db["products"].keys())
    if not pids:
        print("No products being tracked.")
        return

    any_alert = False
    for pid in pids:
        if pid not in db["products"]:
            print(f"⚠️  Product '{pid}' not found.")
            continue
        product = db["products"][pid]
        history = product["price_history"]
        if len(history) < 2:
            continue

        prices = [h["price"] for h in history]
        median = statistics.median(prices)
        latest = prices[-1]
        threshold = product.get("alert_threshold", 0.10)

        if median > 0:
            drop_pct = (median - latest) / median
        else:
            drop_pct = 0

        if drop_pct >= threshold:
            any_alert = True
            print(f"🔔 ALERT: '{product['name']}' (id: {pid})")
            print(f"   Latest: ${latest:.2f} | Median: ${median:.2f}")
            print(f"   Drop: {drop_pct*100:.1f}% below median (threshold: {threshold*100:.0f}%)")
            if product.get("target_price") and latest <= product["target_price"]:
                print(f"   🎯 Target price ${product['target_price']:.2f} REACHED!")
            print()

    if not any_alert:
        print("✅ No price drop alerts. All prices are within normal range.")


def cmd_best_time(args, db):
    """Predict best time to buy based on category seasonal patterns."""
    category = args.category.lower().strip()
    info = SEASONAL_CALENDAR.get(category)
    if not info:
        info = SEASONAL_CALENDAR["generic"]
        category = "generic"

    now = datetime.now()
    current_month = now.month

    print(f"\n📅 Best Time to Buy: {category.upper()}")
    print(f"   {info['note']}")
    print(f"   Best months: {', '.join(MONTH_NAMES[m] for m in info['best_months'])}")
    if info.get("secondary_months"):
        sec = ", ".join(f"{MONTH_NAMES[m]} ({desc})" for m, desc in info["secondary_months"])
        print(f"   Also good: {sec}")

    # Months until next best month
    best = info["best_months"]
    months_until = []
    for m in best:
        diff = (m - current_month) % 12
        months_until.append((diff, m))
    months_until.sort()
    nearest_gap, nearest_month = months_until[0]

    if nearest_gap == 0:
        print(f"   🟢 NOW is a great time to buy {category}!")
    elif nearest_gap == 1:
        print(f"   🟡 Next best window: next month ({MONTH_NAMES[nearest_month]})")
    else:
        print(f"   🔴 Next best window: {MONTH_NAMES[nearest_month]} ({nearest_gap} months away)")

    # If tracking products in this category, show depreciation expectation
    dep_rate = DEPRECIATION_RATES.get(category, DEPRECIATION_RATES["generic"])
    print(f"   Expected annual depreciation: ~{dep_rate*100:.0f}%")

    # Show matching tracked products
    matching = [p for p in db["products"].values() if p.get("category", "generic").lower() == category]
    if matching:
        print(f"\n   Tracked {category} products:")
        for p in matching:
            history = p["price_history"]
            latest = history[-1]["price"] if history else None
            print(f"     • {p['name']} (id: {p['id']}) — Latest: ${latest:.2f}" if latest
                  else f"     • {p['name']} (id: {p['id']}) — No prices yet")


def cmd_report(args, db):
    """Show a summary report of all tracked products."""
    if not db["products"]:
        print("No products tracked yet. Use 'track' to add one.")
        return

    print(f"\n{'='*70}")
    print(f"  PRICE PREDATOR REPORT — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"  {len(db['products'])} product(s) tracked")
    print(f"{'='*70}\n")

    for pid, product in db["products"].items():
        history = product["price_history"]
        name = product["name"]
        category = product.get("category", "generic")
        print(f"  📦 {name}  (id: {pid})")
        print(f"     Category: {category}")
        if product.get("url"):
            print(f"     URL: {product['url']}")

        if not history:
            print("     No price data yet.\n")
            continue

        prices = [h["price"] for h in history]
        low, high = min(prices), max(prices)
        median = statistics.median(prices)
        latest = prices[-1]
        first = prices[0]

        overall = ((latest - first) / first * 100) if first else 0
        print(f"     Prices: low ${low:.2f} | high ${high:.2f} | median ${median:.2f} | latest ${latest:.2f}")
        print(f"     Trend: {overall:+.1f}% since first observation")

        spark = sparkline_chart(prices)
        print(f"     Sparkline: {spark}")

        if len(prices) >= 2:
            threshold = product.get("alert_threshold", 0.10)
            drop = (median - latest) / median if median else 0
            if drop >= threshold:
                print(f"     🔔 BELOW median by {drop*100:.1f}% — potential buy!")
            elif latest <= low * 1.02:
                print(f"     🟢 Near all-time low!")

        if product.get("target_price"):
            if latest <= product["target_price"]:
                print(f"     🎯 Target ${product['target_price']:.2f} reached!")
            else:
                gap = (latest - product["target_price"]) / latest * 100
                print(f"     🎯 Target ${product['target_price']:.2f} ({gap:.0f}% above)")

        # Best time recommendation
        info = SEASONAL_CALENDAR.get(category, SEASONAL_CALENDAR["generic"])
        print(f"     📅 Best buy months: {', '.join(MONTH_NAMES[m] for m in info['best_months'])}")
        print()


def cmd_list(args, db):
    """List all tracked products."""
    if not db["products"]:
        print("No products tracked yet.")
        return
    print(f"\n{'ID':10s} {'Name':40s} {'Category':16s} {'Latest':>10s} {'Obs':>4s}")
    print("-" * 85)
    for pid, product in db["products"].items():
        history = product["price_history"]
        latest = f"${history[-1]['price']:.2f}" if history else "—"
        print(f"{pid:10s} {product['name'][:40]:40s} {product.get('category','generic')[:16]:16s} {latest:>10s} {len(history):4d}")


def cmd_remove(args, db):
    """Remove a tracked product."""
    pid = args.product_id
    if pid not in db["products"]:
        print(f"Error: Product '{pid}' not found.")
        sys.exit(1)
    name = db["products"][pid]["name"]
    del db["products"][pid]
    save_db(Path(args.db), db)
    print(f"✅ Removed '{name}' (id: {pid})")


def cmd_info(args, db):
    """Show detailed info about a single product."""
    pid = args.product_id
    if pid not in db["products"]:
        print(f"Error: Product '{pid}' not found.")
        sys.exit(1)
    product = db["products"][pid]
    print(f"\n📦 {product['name']}")
    print(f"   ID: {pid}")
    print(f"   Category: {product.get('category', 'generic')}")
    if product.get("url"):
        print(f"   URL: {product['url']}")
    print(f"   Target Price: {product.get('target_price') or 'Not set'}")
    print(f"   Alert Threshold: {product.get('alert_threshold', 0.10)*100:.0f}% below median")
    print(f"   Created: {product.get('created_at', 'unknown')}")
    print(f"   Observations: {len(product['price_history'])}")


# ── ASCII Sparkline ─────────────────────────────────────────────────────────

SPARK_CHARS = "▁▂▃▄▅▆▇█"

def sparkline_chart(prices: list) -> str:
    """Generate a compact Unicode sparkline from a list of prices."""
    if not prices:
        return ""
    if len(prices) == 1:
        return SPARK_CHARS[3]
    lo, hi = min(prices), max(prices)
    if hi == lo:
        return SPARK_CHARS[3] * len(prices)
    scale = len(SPARK_CHARS) - 1
    chars = []
    for p in prices:
        idx = int((p - lo) / (hi - lo) * scale)
        idx = max(0, min(scale, idx))
        chars.append(SPARK_CHARS[idx])
    return "".join(chars)


# ── Prediction helper ───────────────────────────────────────────────────────

def predict_future_price(current_price: float, category: str, months_ahead: int) -> float:
    """Predict price after N months based on category depreciation rate."""
    annual_rate = DEPRECIATION_RATES.get(category, DEPRECIATION_RATES["generic"])
    monthly_rate = annual_rate / 12
    return current_price * ((1 - monthly_rate) ** months_ahead)


# ── CLI ─────────────────────────────────────────────────────────────────────

def build_parser():
    parser = argparse.ArgumentParser(
        prog="price_predator",
        description="🦈 Price Predator — Track prices, get alerts, predict the best time to buy.",
    )
    parser.add_argument("--db", default=str(DEFAULT_DB), help="Path to JSON database file")
    sub = parser.add_subparsers(dest="command", required=True)

    # track
    p_track = sub.add_parser("track", help="Add a product to track")
    p_track.add_argument("--name", help="Product name")
    p_track.add_argument("--url", help="Product URL")
    p_track.add_argument("--price", type=float, help="Initial/current price")
    p_track.add_argument("--category", default="generic", help="Product category (e.g. electronics)")
    p_track.add_argument("--target", type=float, help="Target buy price")
    p_track.add_argument("--threshold", type=float, help="Alert threshold as fraction (default 0.10 = 10%%)")
    p_track.add_argument("--source", help="Price source label (e.g. amazon)")
    p_track.add_argument("--id", help="Custom product ID (default: auto-generated)")

    # update
    p_update = sub.add_parser("update", help="Record a new price observation")
    p_update.add_argument("product_id", help="Product ID")
    p_update.add_argument("--price", type=float, required=True, help="New price")
    p_update.add_argument("--source", help="Price source label")

    # history
    p_history = sub.add_parser("history", help="Show price history with ASCII chart")
    p_history.add_argument("product_id", help="Product ID")

    # alert
    p_alert = sub.add_parser("alert", help="Check for price drops")
    p_alert.add_argument("product_id", nargs="?", default=None, help="Product ID (default: check all)")

    # best-time
    p_best = sub.add_parser("best-time", help="Predict best time to buy by category")
    p_best.add_argument("--category", required=True, help="Product category")

    # report
    sub.add_parser("report", help="Full summary report of all tracked products")

    # list
    sub.add_parser("list", help="List all tracked products")

    # remove
    p_remove = sub.add_parser("remove", help="Remove a tracked product")
    p_remove.add_argument("product_id", help="Product ID")

    # info
    p_info = sub.add_parser("info", help="Show detailed info about a product")
    p_info.add_argument("product_id", help="Product ID")

    return parser


COMMAND_MAP = {
    "track": cmd_track,
    "update": cmd_update,
    "history": cmd_history,
    "alert": cmd_alert,
    "best-time": cmd_best_time,
    "report": cmd_report,
    "list": cmd_list,
    "remove": cmd_remove,
    "info": cmd_info,
}


def main():
    parser = build_parser()
    args = parser.parse_args()
    db = load_db(Path(args.db))
    COMMAND_MAP[args.command](args, db)


if __name__ == "__main__":
    main()
