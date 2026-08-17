#!/usr/bin/env python3
"""
packing_pro.py — Smart packing list generator.

Generates a categorized, weighted packing checklist based on destination,
trip duration, season/weather, activities, and transport type.

Usage:
    python3 packing_pro.py
    python3 packing_pro.py --destination "Tokyo" --duration 7 --season winter \
        --activities hiking photography --transport flight
    python3 packing_pro.py --destination "Bali" --duration 10 --season summer \
        --temp-c 30 --activities swimming --output trip.json

Standard library only. Python 3.8+.
"""

import argparse
import json
import math
import sys

# ---------------------------------------------------------------------------
# Item Database — (name, weight_g, category, note)
# ---------------------------------------------------------------------------
# Each entry: name, weight in grams, category, optional note.
ITEMS = {
    # --- Critical / Documents ---
    "passport": (30, "documents", "Check expiry >6 months before travel"),
    "id_card": (30, "documents", "National ID or driver's license"),
    "travel_tickets": (10, "documents", "Printed backup of e-tickets"),
    "credit_cards": (10, "documents", "Notify bank of travel dates"),
    "cash": (50, "documents", "Local currency, small bills"),
    "phone": (180, "electronics", ""),
    "phone_charger": (60, "electronics", ""),
    "usb_cable": (30, "electronics", ""),
    "medications": (50, "documents", "In original containers; bring extra"),
    "glasses": (100, "documents", "Plus case"),
    "emergency_contacts": (10, "documents", "Printed list"),
    "insurance_docs": (20, "documents", "Travel insurance card/policy"),

    # --- Clothing: Base Layer ---
    "underwear": (50, "clothing", ""),
    "socks": (50, "clothing", ""),
    "thermal_socks": (90, "clothing", "Cold weather"),
    "tshirt": (150, "clothing", ""),
    "thermal_top": (200, "clothing", "Cold weather base layer"),
    "thermal_bottom": (300, "clothing", "Cold weather base layer"),

    # --- Clothing: Mid Layer ---
    "long_sleeve_shirt": (250, "clothing", ""),
    "sweater": (450, "clothing", ""),
    "fleece": (400, "clothing", ""),
    "hoodie": (500, "clothing", ""),
    "polo_shirt": (200, "clothing", "Business casual"),
    "dress_shirt": (250, "clothing", "Business/formal"),

    # --- Clothing: Outer Layer ---
    "light_jacket": (350, "clothing", "Windbreaker"),
    "rain_jacket": (400, "clothing", "Waterproof"),
    "winter_coat": (1200, "clothing", "Heavy coat"),
    "down_jacket": (600, "clothing", "Packable, warm"),
    "blazer": (700, "clothing", "Business"),
    "suit": (1500, "clothing", "Formal"),

    # --- Clothing: Lower Body ---
    "jeans": (700, "clothing", ""),
    "trousers": (400, "clothing", "Slacks / chinos"),
    "shorts": (250, "clothing", ""),
    "skirt": (300, "clothing", ""),
    "swimwear": (200, "clothing", "Swimsuit / trunks"),

    # --- Clothing: Sleep ---
    "pajamas": (400, "clothing", ""),
    "robe": (600, "clothing", "Optional"),

    # --- Footwear ---
    "sneakers": (600, "footwear", "Wear on travel day"),
    "dress_shoes": (700, "footwear", "Business/formal"),
    "sandals": (300, "footwear", "Beach/warm weather"),
    "hiking_boots": (1100, "footwear", "Hiking"),
    "slippers": (200, "footwear", "Optional"),

    # --- Accessories ---
    "belt": (100, "accessories", ""),
    "tie": (50, "accessories", "Formal"),
    "sun_hat": (80, "accessories", "Sun protection"),
    "beanie": (100, "accessories", "Cold weather"),
    "scarf": (150, "accessories", ""),
    "gloves": (100, "accessories", "Cold weather"),
    "mittens": (150, "accessories", "Very cold"),
    "sunglasses": (50, "accessories", ""),

    # --- Toiletries ---
    "toothbrush": (20, "toiletries", ""),
    "toothpaste": (100, "toiletries", "Travel size for carry-on"),
    "dental_floss": (10, "toiletries", ""),
    "deodorant": (100, "toiletries", ""),
    "shampoo": (200, "toiletries", "Travel size for carry-on"),
    "body_wash": (100, "toiletries", "Travel size"),
    "razor": (50, "toiletries", ""),
    "hairbrush": (80, "toiletries", ""),
    "sunscreen": (200, "toiletries", "SPF 50+"),
    "lip_balm": (15, "toiletries", ""),
    "moisturizer": (100, "toiletries", ""),
    "first_aid_kit": (300, "toiletries", "Bandages, antiseptic, pain reliever"),
    "contact_solution": (200, "toiletries", "If wearing contacts"),
    "insect_repellent": (100, "toiletries", ""),
    "motion_sickness_meds": (30, "toiletries", ""),

    # --- Electronics ---
    "power_bank": (250, "electronics", ""),
    "laptop": (1500, "electronics", ""),
    "laptop_charger": (300, "electronics", ""),
    "tablet": (400, "electronics", ""),
    "headphones": (100, "electronics", ""),
    "camera": (500, "electronics", ""),
    "camera_batteries": (60, "electronics", "Spare battery"),
    "memory_cards": (10, "electronics", ""),
    "universal_adapter": (150, "electronics", "International travel"),
    "portable_speaker": (300, "electronics", "Optional"),

    # --- Activity: Hiking ---
    "daypack": (500, "activity_gear", "Hiking day pack"),
    "water_bottle": (200, "activity_gear", "Reusable, empty for flight"),
    "trail_map": (100, "activity_gear", "Or GPS device"),

    # --- Activity: Beach ---
    "beach_towel": (400, "activity_gear", ""),
    "snorkel_gear": (800, "activity_gear", "Optional"),
    "beach_bag": (200, "activity_gear", ""),
    "waterproof_phone_case": (50, "activity_gear", ""),

    # --- Activity: Skiing ---
    "ski_gloves": (200, "activity_gear", ""),
    "ski_goggles": (150, "activity_gear", ""),
    "neck_gaiter": (100, "activity_gear", "Balaclava"),
    "hand_warmers": (50, "activity_gear", ""),

    # --- Activity: Business ---
    "business_cards": (50, "activity_gear", ""),
    "notebook": (250, "activity_gear", ""),
    "pen": (20, "activity_gear", ""),

    # --- Activity: Photography ---
    "tripod": (1000, "activity_gear", "Optional"),
    "lens_cleaning_kit": (100, "activity_gear", ""),

    # --- Activity: Camping ---
    "tent": (2000, "activity_gear", "Or check if provided at site"),
    "sleeping_bag": (1500, "activity_gear", ""),
    "headlamp": (100, "activity_gear", ""),
    "multi_tool": (150, "activity_gear", ""),
    "fire_starter": (30, "activity_gear", "Matches / lighter"),

    # --- Misc ---
    "travel_pillow": (300, "misc", ""),
    "eye_mask": (30, "misc", ""),
    "earplugs": (10, "misc", ""),
    "laundry_bag": (50, "misc", ""),
    "umbrella": (300, "misc", "Travel-sized"),
    "book": (350, "misc", ""),
    "snacks": (200, "misc", ""),
    "reusable_bag": (50, "misc", "Shopping bag"),
    "padlock": (50, "misc", "For hostels/gym lockers"),
    "sewing_kit": (30, "misc", ""),
    "drivers_license": (30, "documents", "Required for car rental"),
    "car_charger": (80, "misc", "Phone charger for car"),
    "phone_mount": (100, "misc", "Car phone mount"),
    "roadside_kit": (800, "misc", "Jumper cables, triangle, first aid"),
    "cooler": (1000, "misc", "For road trips"),
}


# ---------------------------------------------------------------------------
# Climate / Weather Logic
# ---------------------------------------------------------------------------
SEASON_DEFAULTS = {
    "winter": -2,
    "spring": 14,
    "autumn": 12,
    "summer": 27,
}


def get_climate(season, temp_c=None):
    """Determine climate category from season and optional temperature."""
    if temp_c is None:
        temp_c = SEASON_DEFAULTS.get(season.lower(), 15)
    if temp_c <= 0:
        return "freezing"
    elif temp_c <= 10:
        return "cold"
    elif temp_c <= 20:
        return "mild"
    elif temp_c <= 30:
        return "warm"
    return "hot"


# ---------------------------------------------------------------------------
# Packing List Builder
# ---------------------------------------------------------------------------
def build_packing_list(destination, duration, season, temp_c, activities, transport):
    """Build a complete categorized packing list."""
    climate = get_climate(season, temp_c)
    activities = [a.lower().strip() for a in activities] if activities else []
    transport = (transport or "flight").lower().strip()

    categories = {
        "clothing": [],
        "footwear": [],
        "accessories": [],
        "toiletries": [],
        "electronics": [],
        "activity_gear": [],
        "misc": [],
        "documents": [],
    }

    # -- Critical items (always included) --
    critical_items = build_critical_items(transport, destination)

    # -- Clothing based on climate --
    build_clothing(categories, climate, duration)

    # -- Toiletries (base set for everyone) --
    build_base_toiletries(categories)

    # -- Electronics (base set) --
    build_base_electronics(categories, transport)

    # -- Activity gear --
    for activity in activities:
        build_activity_gear(categories, activity, climate)

    # -- Transport-specific items --
    build_transport_items(categories, transport)

    # -- Season extras --
    build_season_extras(categories, season)

    # -- Misc comfort items --
    build_misc(categories, transport, duration)

    # -- Calculate total weight --
    total_weight = 0
    for cat_items in categories.values():
        for item in cat_items:
            total_weight += item["weight_g"] * item.get("quantity", 1)
    for item in critical_items:
        total_weight += item["weight_g"]

    result = {
        "destination": destination,
        "duration_days": duration,
        "season": season,
        "climate": climate,
        "temperature_c": temp_c,
        "transport": transport,
        "activities": activities,
        "estimated_total_weight_g": total_weight,
        "estimated_total_weight_kg": round(total_weight / 1000, 1),
        "critical_items": critical_items,
        "categories": {k: v for k, v in categories.items() if v},
        "notes": build_notes(duration, transport, activities),
    }
    return result


def build_critical_items(transport, destination):
    """Items that should never be forgotten."""
    critical = []
    for key, note in [
        ("passport", "Check expiry >6 months (international travel)"),
        ("id_card", "Secondary ID"),
        ("credit_cards", "Notify bank of travel dates"),
        ("cash", "Local currency, small bills for tips/transit"),
        ("phone", "With international plan or eSIM"),
        ("phone_charger", ""),
        ("medications", "In original containers; bring extra supply"),
        ("emergency_contacts", "Printed backup list"),
        ("insurance_docs", "Travel insurance card/policy number"),
    ]:
        weight, cat, default_note = ITEMS[key]
        critical.append({
            "item": key.replace("_", " ").title(),
            "category": cat,
            "weight_g": weight,
            "note": note or default_note,
        })
    if transport == "car":
        critical.append({
            "item": "Driver's License",
            "category": "documents",
            "weight_g": 30,
            "note": "Plus vehicle registration",
        })
    return critical


def add_item(categories, key, quantity=1, note=None):
    """Add an item to its category."""
    if key not in ITEMS:
        return
    weight, cat, default_note = ITEMS[key]
    categories[cat].append({
        "item": key.replace("_", " ").title(),
        "quantity": quantity,
        "weight_g": weight,
        "note": note or default_note,
    })


def build_clothing(categories, climate, duration):
    """Add clothing based on climate and duration."""
    # Base (all climates)
    add_item(categories, "underwear", duration + 1)
    add_item(categories, "belt", 1)

    if climate in ("freezing", "cold"):
        add_item(categories, "thermal_top", math.ceil(duration / 2))
        add_item(categories, "thermal_bottom", math.ceil(duration / 2))
        add_item(categories, "thermal_socks", min(duration + 1, 5))
        add_item(categories, "long_sleeve_shirt", min(math.ceil(duration / 2) + 1, 6))
        add_item(categories, "sweater", 2)
        add_item(categories, "fleece", 1)
        add_item(categories, "jeans", min(math.ceil(duration / 3), 3))
        add_item(categories, "trousers", min(math.ceil(duration / 4), 2))
        if climate == "freezing":
            add_item(categories, "winter_coat", 1, "Wear on travel day")
            add_item(categories, "mittens", 1)
        else:
            add_item(categories, "down_jacket", 1, "Wear on travel day")
            add_item(categories, "gloves", 1)
        add_item(categories, "beanie", 1)
        add_item(categories, "scarf", 1)
        add_item(categories, "socks", min(duration + 1, 5))
        add_item(categories, "pajamas", 2 if duration > 7 else 1)
        add_item(categories, "sneakers", 1, "Wear on travel day")

    elif climate == "mild":
        add_item(categories, "tshirt", min(math.ceil(duration / 2) + 1, 7))
        add_item(categories, "long_sleeve_shirt", min(math.ceil(duration / 3), 3))
        add_item(categories, "socks", min(duration + 1, 6))
        add_item(categories, "jeans", min(math.ceil(duration / 3), 3))
        add_item(categories, "trousers", min(math.ceil(duration / 4), 2))
        add_item(categories, "light_jacket", 1)
        add_item(categories, "hoodie", 1)
        add_item(categories, "pajamas", 2 if duration > 7 else 1)
        add_item(categories, "sneakers", 1, "Wear on travel day")

    else:  # warm or hot
        add_item(categories, "tshirt", min(duration + 1, 8))
        add_item(categories, "shorts", min(math.ceil(duration / 2), 4))
        add_item(categories, "socks", min(math.ceil(duration / 2), 4))
        add_item(categories, "underwear", duration + 1)
        add_item(categories, "jeans", 1, "For evenings / travel day")
        add_item(categories, "light_jacket", 1, "For air conditioning / evenings")
        add_item(categories, "pajamas", 1)
        add_item(categories, "sneakers", 1, "Wear on travel day")
        add_item(categories, "sandals", 1)
        add_item(categories, "sunglasses", 1)
        add_item(categories, "sun_hat", 1)


def build_base_toiletries(categories):
    """Base toiletries everyone needs."""
    for key in [
        "toothbrush", "toothpaste", "dental_floss", "deodorant",
        "shampoo", "body_wash", "razor", "hairbrush", "lip_balm",
        "first_aid_kit",
    ]:
        add_item(categories, key, 1)


def build_base_electronics(categories, transport):
    """Base electronics."""
    add_item(categories, "usb_cable", 1)
    add_item(categories, "power_bank", 1)
    add_item(categories, "headphones", 1)
    if transport == "flight":
        add_item(categories, "universal_adapter", 1, "For international flights")


def build_activity_gear(categories, activity, climate):
    """Add gear specific to an activity."""
    if activity in ("hiking", "trekking"):
        add_item(categories, "hiking_boots", 1, "Break in before trip")
        add_item(categories, "daypack", 1)
        add_item(categories, "water_bottle", 1)
        add_item(categories, "trail_map", 1)
        add_item(categories, "first_aid_kit", 1, "Trail-specific")
    elif activity in ("swimming", "beach", "surfing"):
        add_item(categories, "swimwear", 2)
        add_item(categories, "beach_towel", 1)
        add_item(categories, "sandals", 1)
        add_item(categories, "sunscreen", 1, "SPF 50+ — reapply frequently")
        add_item(categories, "waterproof_phone_case", 1)
    elif activity == "business":
        add_item(categories, "laptop", 1)
        add_item(categories, "laptop_charger", 1)
        add_item(categories, "business_cards", 1)
        add_item(categories, "notebook", 1)
        add_item(categories, "pen", 1)
        add_item(categories, "dress_shirt", min(3, 5))
        add_item(categories, "dress_shoes", 1)
        add_item(categories, "polo_shirt", 2)
        add_item(categories, "trousers", 2, "Business slacks")
        add_item(categories, "blazer", 1)
    elif activity in ("skiing", "snow"):
        add_item(categories, "ski_gloves", 1)
        add_item(categories, "ski_goggles", 1)
        add_item(categories, "neck_gaiter", 1)
        add_item(categories, "hand_warmers", 5, "Several packs")
        add_item(categories, "thermal_top", 2, "Ski base layer")
        add_item(categories, "thermal_bottom", 2, "Ski base layer")
    elif activity == "photography":
        add_item(categories, "camera", 1)
        add_item(categories, "camera_batteries", 2, "Spare batteries")
        add_item(categories, "memory_cards", 2)
        add_item(categories, "lens_cleaning_kit", 1)
        add_item(categories, "tripod", 1, "Optional — check weight")
    elif activity == "formal":
        add_item(categories, "suit", 1)
        add_item(categories, "dress_shoes", 1)
        add_item(categories, "tie", 1)
        add_item(categories, "dress_shirt", 1)
    elif activity == "camping":
        add_item(categories, "tent", 1, "Or verify site provides shelter")
        add_item(categories, "sleeping_bag", 1)
        add_item(categories, "headlamp", 1)
        add_item(categories, "multi_tool", 1)
        add_item(categories, "fire_starter", 1)
        add_item(categories, "insect_repellent", 1)


def build_transport_items(categories, transport):
    """Items specific to transport type."""
    if transport == "flight":
        add_item(categories, "travel_pillow", 1)
    elif transport == "car":
        add_item(categories, "car_charger", 1)
        add_item(categories, "phone_mount", 1)
        add_item(categories, "roadside_kit", 1)
        add_item(categories, "sunglasses", 1, "Driving")
        add_item(categories, "cooler", 1, "Optional for road trips")
    elif transport == "train":
        add_item(categories, "travel_pillow", 1)
        add_item(categories, "book", 1, "Or downloaded media")
    elif transport == "bus":
        add_item(categories, "book", 1, "Or downloaded media")
        add_item(categories, "motion_sickness_meds", 1)


def build_season_extras(categories, season):
    """Season-specific additions."""
    if season.lower() == "summer":
        add_item(categories, "sunscreen", 1, "SPF 50+")
        add_item(categories, "sunglasses", 1)
        add_item(categories, "insect_repellent", 1)
    elif season.lower() == "winter":
        add_item(categories, "moisturizer", 1, "Cold dry air")
        add_item(categories, "lip_balm", 1, "Extra — cold weather")
    elif season.lower() in ("spring", "autumn"):
        add_item(categories, "rain_jacket", 1)
        add_item(categories, "umbrella", 1)


def build_misc(categories, transport, duration):
    """Comfort and utility items."""
    add_item(categories, "laundry_bag", 1)
    add_item(categories, "reusable_bag", 1)
    add_item(categories, "snacks", 1, "For travel day")
    add_item(categories, "sewing_kit", 1)
    if duration > 5:
        add_item(categories, "earplugs", 1)
        add_item(categories, "eye_mask", 1)
    if transport == "flight":
        add_item(categories, "padlock", 1, "For luggage / lockers")


def build_notes(duration, transport, activities):
    """Generate helpful packing notes."""
    notes = []
    if duration > 7:
        notes.append(
            f"Long trip ({duration} days): Plan a laundry day around day 5-6. "
            "Pack quick-dry fabrics."
        )
    if transport == "flight":
        notes.append(
            "Flight: Keep all liquids ≤100 ml in a 1 L clear bag for carry-on. "
            "Put sharp items and large liquids in checked baggage."
        )
    if transport == "car":
        notes.append("Road trip: Download offline maps and playlists before departure.")
    if "business" in (activities or []):
        notes.append("Business trip: Check dress code in advance; steam/iron clothes upon arrival.")
    if "skiing" in (activities or []) or "snow" in (activities or []):
        notes.append("Ski trip: Check if you can rent bulky gear (skis, boots, helmet) at the resort.")
    if "camping" in (activities or []):
        notes.append("Camping: Verify campsite amenities — some provide tents/cooking gear.")
    if not notes:
        notes.append("Pack versatile items that mix and match to save space.")
    return notes


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Smart packing list generator."
    )
    parser.add_argument("--destination", "-d", required=True,
                        help="Trip destination")
    parser.add_argument("--duration", type=int, required=True,
                        help="Trip duration in days")
    parser.add_argument("--season", "-s", required=True,
                        choices=["summer", "winter", "spring", "autumn"],
                        help="Season of travel")
    parser.add_argument("--temp-c", type=int, default=None,
                        help="Average temperature in °C (overrides season default)")
    parser.add_argument("--activities", "-a", nargs="*", default=[],
                        help="Activities: hiking, swimming, beach, business, "
                             "skiing, snow, photography, formal, camping")
    parser.add_argument("--transport", "-t", default="flight",
                        choices=["flight", "train", "car", "bus"],
                        help="Primary transport type (default: flight)")
    parser.add_argument("--output", "-o", default=None,
                        help="Output file path (default: stdout)")

    args = parser.parse_args()

    result = build_packing_list(
        destination=args.destination,
        duration=args.duration,
        season=args.season,
        temp_c=args.temp_c,
        activities=args.activities,
        transport=args.transport,
    )

    output = json.dumps(result, indent=2)
    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Packing list saved to {args.output}", file=sys.stderr)
        print(f"Total estimated weight: {result['estimated_total_weight_kg']} kg "
              f"({result['estimated_total_weight_g']} g)", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
