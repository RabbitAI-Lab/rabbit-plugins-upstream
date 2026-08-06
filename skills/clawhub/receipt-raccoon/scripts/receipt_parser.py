#!/usr/bin/env python3
"""
Receipt Raccoon — parse receipt text into structured data and generate reports.

Usage:
    python3 receipt_parser.py parse --text "receipt text..."
    python3 receipt_parser.py parse --file receipt.txt
    echo "receipt text" | python3 receipt_parser.py parse
    python3 receipt_parser.py parse --file r.txt --append receipts.jsonl
    python3 receipt_parser.py report --ledger receipts.jsonl
    python3 receipt_parser.py report --ledger receipts.jsonl --month 2024-01
    python3 receipt_parser.py demo

Stdlib only. No external dependencies.
"""

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime

# ---------------------------------------------------------------------------
# Category keyword database
# ---------------------------------------------------------------------------

CATEGORIES = {
    "groceries": [
        "milk", "bread", "eggs", "egg", "cheese", "butter", "yogurt", "cream",
        "chicken", "beef", "pork", "bacon", "turkey", "fish", "salmon", "shrimp",
        "rice", "pasta", "flour", "sugar", "oil", "salt", "pepper", "spice",
        "onion", "garlic", "potato", "tomato", "carrot", "lettuce", "spinach",
        "broccoli", "apple", "banana", "orange", "lemon", "lime", "berry",
        "avocado", "cucumber", "pepper", "celery", "mushroom", "corn",
        "juice", "water", "tea", "coffee beans", "cereal", "oats", "granola",
        "jam", "honey", "peanut butter", "nut", "almond", "walnut",
        "tofu", "tempeh", "lentil", "bean", "chickpea", "soup", "sauce",
        "ketchup", "mustard", "mayo", "vinegar", "soy", "noodle", "tortilla",
        "bun", "roll", "bagel", "pita", "cracker", "cookie", "chocolate",
        "candy", "gum", "chip", "pretzel", "popcorn", "crisps", "biscuit",
        "wine", "beer", "whisky", "vodka", "rum", "gin", "tequila", "liqueur",
        "frozen", "ice cream", "yogurt", "pizza", "dough", "crust", "pie",
        "deli", "ham", "salami", "sausage", "hot dog", "bacon strip",
        "organic", "gluten", "kale", "arugula", "fennel", "leek", "shallot",
        "parsley", "cilantro", "basil", "mint", "thyme", "rosemary", "sage",
        "dill", "chive", "scallion", "zucchini", "squash", "eggplant",
        "pepper", "radish", "beet", "turnip", "parsnip", "rutabaga",
        "cauliflower", "brussels", "artichoke", "asparagus", "green bean",
        "pea", "okra", "cabbage", "bok choy", "watercress", "endive",
        "radicchio", "fennel", "chard", "collard", "mustard green",
        "grape", "melon", "cantaloupe", "honeydew", "pineapple", "mango",
        "papaya", "kiwi", "peach", "pear", "plum", "cherry", "fig",
        "pomegranate", "coconut", "plantain", "date", "raisin", "cranberry",
        "tangerine", "nectarine", "apricot", "prune",
    ],
    "dining": [
        "burger", "pizza", "sandwich", "taco", "burrito", "quesadilla",
        "sushi", "ramen", "noodle bowl", "curry", "stir fry", "fried rice",
        "pasta dish", "risotto", "lasagna", "salad bar", "soup bowl",
        "coffee", "espresso", "latte", "cappuccino", "americano", "mocha",
        "tea", "matcha", "chai", "smoothie", "juice bar", "acai",
        "beer", "draft", "wine glass", "cocktail", "margarita", "mojito",
        "martini", "sangria", "mimosa", "bloody mary",
        "appetizer", "wings", "nachos", "fries", "onion ring", "mozzarella stick",
        "brunch", "breakfast", "pancake", "waffle", "omelette", " Benedict",
        "steak", "ribeye", "sirloin", "filet", "porterhouse", "brisket",
        "lobster", "crab", "oyster", "clam", "mussel", "scallop",
        "dessert", "cake", "tiramisu", "cheesecake", "gelato", "sorbet",
        "restaurant", "cafe", "diner", "bistro", "grill", "barbecue",
        "bbq", "kitchen", "eatery", "tavern", "pub", "brewery",
        "takeout", "delivery", "doordash", "uber eats", "grubhub",
        "gratuity", "tip",
    ],
    "electronics": [
        "cable", "charger", "usb", "hdmi", "adapter", "battery", "cord",
        "phone", "laptop", "tablet", "monitor", "keyboard", "mouse",
        "headphone", "earbud", "speaker", "webcam", "microphone", "router",
        "ssd", "hard drive", "memory", "ram", "graphics card", "gpu",
        "motherboard", "cpu", "processor", "power supply", "case fan",
        "screen protector", "phone case", "stand", "mount", "dock",
        "smartwatch", "fitness tracker", "drone", "camera", "lens",
        "tripod", "flashlight", "led", "power bank", "surge protector",
        "extension cord", "light bulb", "thermostat", "smart plug",
    ],
    "clothing": [
        "shirt", "t-shirt", "tee", "blouse", "polo", "tank top",
        "pants", "jeans", "trouser", "short", "skirt", "legging",
        "dress", "gown", "jumpsuit", "suit", "blazer", "vest",
        "jacket", "coat", "parka", "windbreaker", "cardigan", "sweater",
        "hoodie", "pullover", "fleece",
        "shoe", "sneaker", "boot", "sandal", "heel", "flat", "loafer",
        "flip flop", "slipper", "cleat",
        "sock", "underwear", "bra", "undershirt", "tight", "pantyhose",
        "hat", "cap", "beanie", "glove", "scarf", "mitten",
        "tie", "bowtie", "belt", "suspenders", "wallet", "purse",
        "handbag", "backpack", "messenger bag", "tote", "duffel",
        "watch", "ring", "necklace", "bracelet", "earring", "pendant",
    ],
    "health": [
        "pharmacy", "drug", "medicine", "medication", "prescription",
        "vitamin", "supplement", "aspirin", "ibuprofen", "acetaminophen",
        "tylenol", "advil", "motrin", "aleve", "benadryl", "claritin",
        "zyrtec", "mucinex", "sudafed", "cough", "syrup", "lozenge",
        "bandage", "band-aid", "gauze", "antiseptic", "ointment",
        "thermometer", "blood pressure", "pulse oximeter", "cane",
        "toothbrush", "toothpaste", "floss", "mouthwash", "deodorant",
        "shampoo", "conditioner", "soap", "body wash", "lotion",
        "sunscreen", "tissue", "cotton", "swab", "razor", "blade",
        "shaving", "contact", "contact lens", "solution", "eye drop",
        "first aid", "cold pack", "heating pad",
    ],
    "household": [
        "detergent", "fabric softener", "bleach", "stain remover",
        "dish soap", "dishwasher", "sponge", "scrub", "brush",
        "paper towel", "toilet paper", "tissue", "napkin",
        "trash bag", "garbage", "bin liner", "ziploc", "bag",
        "cleaning", "spray", "windex", "lysol", "clorox", "pledge",
        "mop", "broom", "vacuum", "duster", "bucket",
        "candle", "air freshener", "diffuser", "incense",
        "laundry", "dryer sheet", "starch", "iron",
        "light bulb", "battery", "filter", "water filter",
        "aluminum foil", "plastic wrap", "parchment", "freezer bag",
        "tupperware", "container", "mason jar",
        "plate", "bowl", "cup", "mug", "glass", "silverware",
        "fork", "knife", "spoon", "spatula", "whisk", "tong",
        "pan", "pot", "skillet", "baking sheet", "cutting board",
    ],
    "transport": [
        "gas", "fuel", "diesel", "unleaded", "premium", "regular",
        "octane", "ethanol", "propane",
        "uber", "lyft", "taxi", "cab", "rideshare",
        "bus", "train", "metro", "subway", "transit", "fare",
        "parking", "meter", "garage", "valet",
        "toll", "bridge", "turnpike", "express lane",
        "oil change", "tire", "rotation", "alignment", "brake",
        "wiper", "battery", "spark plug", "air filter", "antifreeze",
        "car wash", "detail",
        "bike", "bicycle", "scooter", "skateboard",
        "flight", "airline", "boarding", "luggage",
    ],
    "entertainment": [
        "movie", "cinema", "theater", "film", "ticket",
        "concert", "show", "gig", "festival", "performance",
        "game", "video game", "steam", "playstation", "xbox", "nintendo",
        "dlc", "expansion", "in-game", "microtransaction",
        "book", "magazine", "comic", "novel", "ebook",
        "streaming", "netflix", "spotify", "hulu", "disney", "hbo",
        "puzzle", "board game", "card game", "dice", "miniature",
        "museum", "gallery", "exhibition", "zoo", "aquarium",
        "amusement", "theme park", "rollercoaster", "arcade",
        "bowling", "mini golf", "escape room", "karaoke",
        "sport", "ticket", "jersey", "merchandise",
        "lottery", "scratch", "raffle",
    ],
    "office": [
        "pen", "pencil", "marker", "highlighter", "sharpie",
        "paper", "notebook", "binder", "folder", "divider",
        "stapler", "staple", "clip", "paperclip", "rubber band",
        "tape", "glue", "scissors", "ruler", "calculator",
        "printer", "ink", "toner", "cartridge", "paper ream",
        "envelope", "stamp", "mailing", "shipping",
        "desk", "chair", "lamp", "organizer", "shelf",
        "calendar", "planner", "sticky note", "index card",
        "whiteboard", "marker", "eraser",
    ],
}


def categorise_item(name: str) -> str:
    """Categorise an item name using keyword matching."""
    name_lower = name.lower()
    best_category = "other"
    best_score = 0
    for category, keywords in CATEGORIES.items():
        score = 0
        for kw in keywords:
            if kw in name_lower:
                # Longer keyword matches are weighted higher
                score += len(kw)
        if score > best_score:
            best_score = score
            best_category = category
    return best_category


# ---------------------------------------------------------------------------
# Date parsing
# ---------------------------------------------------------------------------

DATE_PATTERNS = [
    # ISO format: 2024-01-15
    (r"\b(\d{4})-(\d{1,2})-(\d{1,2})\b", "ymd_dash"),
    # US format: 01/15/2024 or 1/15/24
    (r"\b(\d{1,2})/(\d{1,2})/(\d{2,4})\b", "us_slash"),
    # EU format: 15/01/2024 or 15.01.2024
    (r"\b(\d{1,2})\.(\d{1,2})\.(\d{2,4})\b", "eu_dot"),
    # Written: Jan 15, 2024 or January 15 2024
    (r"\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+(\d{1,2}),?\s+(\d{4})\b", "written"),
    # Written day first: 15 Jan 2024
    (r"\b(\d{1,2})\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+(\d{4})\b", "written_day_first"),
]

MONTH_MAP = {
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
    "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12,
}


def parse_date(text: str) -> str:
    """Extract a date from text and return ISO format (YYYY-MM-DD)."""
    for pattern, fmt in DATE_PATTERNS:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            groups = match.groups()
            try:
                if fmt == "ymd_dash":
                    y, m, d = int(groups[0]), int(groups[1]), int(groups[2])
                elif fmt == "us_slash":
                    m, d, y = int(groups[0]), int(groups[1]), int(groups[2])
                    if y < 100:
                        y += 2000
                elif fmt == "eu_dot":
                    d, m, y = int(groups[0]), int(groups[1]), int(groups[2])
                    if y < 100:
                        y += 2000
                elif fmt == "written":
                    m = MONTH_MAP[groups[0].lower()[:3]]
                    d = int(groups[1])
                    y = int(groups[2])
                elif fmt == "written_day_first":
                    d = int(groups[0])
                    m = MONTH_MAP[groups[1].lower()[:3]]
                    y = int(groups[2])
                else:
                    continue
                return f"{y:04d}-{m:02d}-{d:02d}"
            except (ValueError, KeyError):
                continue
    return ""


# ---------------------------------------------------------------------------
# Receipt parsing
# ---------------------------------------------------------------------------

# Price pattern: captures a monetary amount at end of line
PRICE_PATTERN = re.compile(r"(-?\$?\s*[\d,]+\.\d{2})\s*$")
# Alternative price pattern: price... somewhere in the line
PRICE_ANYWHERE = re.compile(r"\$?\s*([\d,]+\.\d{2})")

# Known non-item line indicators
SKIP_KEYWORDS = [
    "subtotal", "sub total", "sub-total", "total", "balance", "amount",
    "tax", "vat", "gst", "hst", "pst", "tip", "gratuity", "cash",
    "change", "credit", "debit", "visa", "mastercard", "amex",
    "thank", "welcome", "phone", "tel", "fax", "www", "http",
    "order", "receipt", "invoice", "store", "#", "qty", "quantity",
    "cashier", "register", "terminal", "transaction", "auth",
    "approval", "ref", "card", "account", "awa", "loyalty",
    "points", "reward", "coupon", "discount", "savings", "markdown",
    "promo", "sale", " clearance", "boss", "store number", "addr",
    "street", "avenue", "ave", "blvd", "road", "rd", "drive",
    "suite", "unit", "zip", "postal", "clerk",
]

# Keywords for identifying summary lines
SUMMARY_KEYWORDS = {
    "subtotal": ["subtotal", "sub total", "sub-total"],
    "tax": ["tax", "vat", "gst", "hst", "pst", "sales tax"],
    "total": ["total", "balance due", "amount due", "grand total"],
    "tip": ["tip", "gratuity"],
}


def is_summary_line(line: str) -> str:
    """Check if a line is a summary line (subtotal/tax/total/tip). Return type or empty."""
    line_lower = line.lower()
    for key, keywords in SUMMARY_KEYWORDS.items():
        for kw in keywords:
            if kw in line_lower:
                return key
    return ""


def extract_price(line: str) -> float | None:
    """Extract the last monetary value from a line."""
    # Try end-of-line price first
    match = PRICE_PATTERN.search(line)
    if match:
        return parse_money(match.group(1))
    # Fallback: any price in the line
    matches = PRICE_ANYWHERE.findall(line)
    if matches:
        return parse_money(matches[-1])
    return None


def parse_money(s: str) -> float:
    """Parse a money string like '$1,234.56' into a float."""
    cleaned = re.sub(r"[^\d.\-]", "", s)
    try:
        return round(float(cleaned), 2)
    except ValueError:
        return 0.0


def extract_merchant(lines: list) -> str:
    """
    Extract merchant name from receipt text.
    Usually the first non-empty line that isn't a date or time.
    """
    for line in lines[:5]:
        stripped = line.strip()
        if not stripped:
            continue
        # Skip lines that are just dates, times, or numbers
        if re.match(r"^[\d/:.\-\s]+$", stripped):
            continue
        # Skip very short lines
        if len(stripped) < 2:
            continue
        # Skip lines with phone numbers
        if re.search(r"\d{3}[-.]?\d{3}[-.]?\d{4}", stripped):
            continue
        return stripped
    return "Unknown Merchant"


def parse_receipt(text: str) -> dict:
    """
    Parse raw receipt text into structured data.

    Returns dict with: merchant, date, items, subtotal, tax, total, currency.
    """
    lines = text.strip().split("\n")
    lines = [l.rstrip() for l in lines]

    merchant = extract_merchant(lines)
    date = parse_date(text)

    items = []
    subtotal = None
    tax = None
    total = None
    tip = None

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue

        # Check if this is a summary line
        summary_type = is_summary_line(stripped)
        if summary_type:
            price = extract_price(stripped)
            if price is not None:
                if summary_type == "subtotal":
                    subtotal = price
                elif summary_type == "tax":
                    tax = price
                elif summary_type == "total":
                    total = price
                elif summary_type == "tip":
                    tip = price
            continue

        # Try to parse as an item line (must have a price)
        price = extract_price(stripped)
        if price is not None and price > 0:
            # Check if we should skip this line
            line_lower = stripped.lower()
            should_skip = False
            for kw in SKIP_KEYWORDS:
                if kw in line_lower:
                    should_skip = True
                    break
            if should_skip:
                continue

            # Extract item name (everything before the price)
            name = PRICE_PATTERN.sub("", stripped).strip()
            name = PRICE_ANYWHERE.sub("", name).strip() if not name else name
            # Clean up the name
            name = re.sub(r"\s{2,}", " ", name).strip()
            name = re.sub(r"^\d+\s+", "", name)  # Remove leading item numbers
            name = re.sub(r"\s+\d+\s*$", "", name)  # Remove trailing quantities
            name = name.strip(" -|*")

            if name and len(name) >= 2:
                category = categorise_item(name)
                items.append(
                    {
                        "name": name,
                        "price": price,
                        "category": category,
                    }
                )

    # If subtotal wasn't found, calculate from items
    if subtotal is None and items:
        subtotal = round(sum(i["price"] for i in items), 2)

    # If total wasn't found, use subtotal + tax
    if total is None:
        total = round((subtotal or 0) + (tax or 0), 2)

    return {
        "merchant": merchant,
        "date": date,
        "items": items,
        "subtotal": subtotal,
        "tax": tax,
        "tip": tip,
        "total": total,
        "currency": "USD",
        "parsed_at": datetime.now().isoformat(),
    }


# ---------------------------------------------------------------------------
# Ledger (JSONL storage)
# ---------------------------------------------------------------------------


def append_to_ledger(receipt: dict, ledger_path: str) -> None:
    """Append a parsed receipt to a JSONL ledger file."""
    with open(ledger_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(receipt, ensure_ascii=False) + "\n")


def load_ledger(ledger_path: str) -> list:
    """Load all receipts from a JSONL ledger file."""
    receipts = []
    with open(ledger_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    receipts.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    return receipts


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------


def generate_report(receipts: list, month_filter: str | None = None) -> dict:
    """
    Generate spending report from a list of receipts.

    Args:
        receipts: list of parsed receipt dicts
        month_filter: optional "YYYY-MM" to filter by

    Returns dict with totals, top_merchants, category_breakdown, monthly.
    """
    if month_filter:
        receipts = [r for r in receipts if r.get("date", "").startswith(month_filter)]

    if not receipts:
        return {
            "total_spend": 0,
            "receipt_count": 0,
            "average_receipt": 0,
            "top_merchants": [],
            "category_breakdown": [],
            "monthly": [],
            "total_tax": 0,
        }

    total_spend = round(sum(r.get("total", 0) or 0 for r in receipts), 2)
    total_tax = round(sum(r.get("tax", 0) or 0 for r in receipts), 2)
    receipt_count = len(receipts)
    average_receipt = round(total_spend / receipt_count, 2) if receipt_count else 0

    # Top merchants
    merchant_totals = defaultdict(float)
    merchant_counts = defaultdict(int)
    for r in receipts:
        merchant = r.get("merchant", "Unknown")
        merchant_totals[merchant] += r.get("total", 0) or 0
        merchant_counts[merchant] += 1
    top_merchants = sorted(
        [{"merchant": m, "total": round(t, 2), "visits": merchant_counts[m]}
         for m, t in merchant_totals.items()],
        key=lambda x: x["total"],
        reverse=True,
    )

    # Category breakdown
    category_totals = defaultdict(float)
    category_counts = defaultdict(int)
    for r in receipts:
        for item in r.get("items", []):
            cat = item.get("category", "other")
            category_totals[cat] += item.get("price", 0)
            category_counts[cat] += 1
    category_breakdown = sorted(
        [
            {
                "category": c,
                "total": round(t, 2),
                "items": category_counts[c],
                "percentage": round(t / total_spend * 100, 1) if total_spend else 0,
            }
            for c, t in category_totals.items()
        ],
        key=lambda x: x["total"],
        reverse=True,
    )

    # Monthly breakdown
    monthly = defaultdict(lambda: {"total": 0, "count": 0})
    for r in receipts:
        date = r.get("date", "")
        if date:
            month = date[:7]  # YYYY-MM
            monthly[month]["total"] += r.get("total", 0) or 0
            monthly[month]["count"] += 1
    monthly_list = sorted(
        [
            {"month": m, "total": round(v["total"], 2), "count": v["count"]}
            for m, v in monthly.items()
        ],
        key=lambda x: x["month"],
    )

    return {
        "total_spend": total_spend,
        "receipt_count": receipt_count,
        "average_receipt": average_receipt,
        "total_tax": total_tax,
        "top_merchants": top_merchants[:10],
        "category_breakdown": category_breakdown,
        "monthly": monthly_list,
        "month_filter": month_filter,
    }


def format_report_text(report: dict) -> str:
    """Format report as readable text."""
    lines = []
    lines.append("=" * 60)
    lines.append("  🦝 RECEIPT RACCOON — Spending Report")
    if report.get("month_filter"):
        lines.append(f"  Month: {report['month_filter']}")
    lines.append("=" * 60)
    lines.append("")
    lines.append(f"  Total spend:      ${report['total_spend']:.2f}")
    lines.append(f"  Receipts:         {report['receipt_count']}")
    lines.append(f"  Average/receipt:  ${report['average_receipt']:.2f}")
    lines.append(f"  Total tax:        ${report['total_tax']:.2f}")
    lines.append("")

    if report["top_merchants"]:
        lines.append("  📊 TOP MERCHANTS")
        for i, m in enumerate(report["top_merchants"], 1):
            lines.append(f"     {i}. {m['merchant']}  —  ${m['total']:.2f}  ({m['visits']} visits)")
        lines.append("")

    if report["category_breakdown"]:
        lines.append("  🏷️  CATEGORY BREAKDOWN")
        for c in report["category_breakdown"]:
            bar = "█" * int(c["percentage"] / 5)
            lines.append(f"     {c['category']:<15} ${c['total']:>8.2f}  "
                         f"({c['percentage']:>5.1f}%)  {bar}  [{c['items']} items]")
        lines.append("")

    if report["monthly"]:
        lines.append("  📅 MONTHLY TREND")
        for m in report["monthly"]:
            lines.append(f"     {m['month']}  —  ${m['total']:.2f}  ({m['count']} receipts)")
        lines.append("")

    lines.append("=" * 60)
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Sample receipts for demo
# ---------------------------------------------------------------------------

SAMPLE_RECEIPTS = [
    """WHOLE FOODS MARKET #12345
123 Organic Street, Portland, OR 97201
01/15/2024  14:32

ORGANIC BANANAS       2.99
ALMOND MILK           3.49
FREE RANGE EGGS       5.99
SOURDOUGH BREAD       4.50
CHEDDAR CHEESE        6.99
CHICKEN BREAST        12.99
BABY SPINACH          3.99
OLIVE OIL             8.99

SUBTOTAL             49.93
TAX                   4.00
TOTAL                53.93

VISA ****1234
Thank you for shopping!
""",
    """STARBUCKS COFFEE #04567
456 Main Street, Seattle, WA 98101
01/16/2024  08:15

GRANDE LATTE         5.25
BLUEBERRY MUFFIN     3.75
TIP                   1.00

SUBTOTAL              9.00
TAX                   0.80
TOTAL                 9.80

Thank you!
""",
    """BEST BUY #09999
789 Electronics Way, Austin, TX 78701
01/20/2024  13:00

USB-C CABLE          19.99
PHONE CASE           24.99
SCREEN PROTECTOR     9.99

SUBTOTAL             54.97
TAX                   4.40
TOTAL                59.37

Visa ****5678
""",
    """TARGET #00321
321 Retail Blvd, Denver, CO 80202
02/03/2024  16:45

MEN'S T-SHIRT       12.99
PAPER TOWELS         7.99
DISH SOAP            3.49
BANANA CHIP          2.99
FROZEN PIZZA         5.49

SUBTOTAL             32.95
TAX                   2.64
TOTAL                35.59

RedCard ****9012
""",
    """TRADER JOE'S #444
777 Grocery Lane, San Francisco, CA 94110
02/05/2024  10:30

MANDARIN CHICKEN     5.99
ORGANIC SALAD        4.49
OLIVE OIL            5.99
DARK CHOCOLATE       2.99
GREEK YOGURT         1.99
TOMATO BASIL SOUP    3.99

SUBTOTAL             25.44
TAX                   2.03
TOTAL                27.47

Thank you!
""",
]


def run_demo():
    """Parse sample receipts and generate a report."""
    print("=" * 60)
    print("  🦝 RECEIPT RACCOON — Demo Mode")
    print("  Parsing 5 sample receipts...\n")
    receipts = []
    for i, text in enumerate(SAMPLE_RECEIPTS, 1):
        parsed = parse_receipt(text)
        receipts.append(parsed)
        print(f"  Receipt {i}: {parsed['merchant']}")
        print(f"    Date: {parsed['date']}  Items: {len(parsed['items'])}  Total: ${parsed['total']:.2f}")
    print()
    report = generate_report(receipts)
    print(format_report_text(report))
    return report


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Receipt Raccoon — parse receipts and generate reports."
    )
    sub = parser.add_subparsers(dest="command", help="Sub-command")

    # Parse command
    p_parse = sub.add_parser("parse", help="Parse a receipt")
    p_parse.add_argument("--text", type=str, help="Receipt text to parse")
    p_parse.add_argument("--file", type=str, help="File containing receipt text")
    p_parse.add_argument(
        "--append", type=str, help="Append parsed receipt to this JSONL ledger"
    )

    # Report command
    p_report = sub.add_parser("report", help="Generate spending report")
    p_report.add_argument("--ledger", type=str, required=True, help="JSONL ledger file")
    p_report.add_argument("--month", type=str, help="Filter by month (YYYY-MM)")
    p_report.add_argument("--json", action="store_true", help="Output JSON")

    # Demo command
    sub.add_parser("demo", help="Run demo with sample receipts")

    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "demo":
        run_demo()
        return 0

    if args.command == "parse":
        # Get text from argument, file, or stdin
        text = None
        if args.text:
            text = args.text
        elif args.file:
            with open(args.file, "r", encoding="utf-8") as f:
                text = f.read()
        else:
            text = sys.stdin.read()

        if not text or not text.strip():
            print("Error: No receipt text provided.", file=sys.stderr)
            return 1

        receipt = parse_receipt(text)
        print(json.dumps(receipt, indent=2, ensure_ascii=False))

        if args.append:
            append_to_ledger(receipt, args.append)
            print(f"\nAppended to ledger: {args.append}", file=sys.stderr)

        return 0

    if args.command == "report":
        try:
            receipts = load_ledger(args.ledger)
        except FileNotFoundError:
            print(f"Error: Ledger file not found: {args.ledger}", file=sys.stderr)
            return 1

        report = generate_report(receipts, month_filter=args.month)

        if args.json:
            print(json.dumps(report, indent=2, ensure_ascii=False))
        else:
            print(format_report_text(report))
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
