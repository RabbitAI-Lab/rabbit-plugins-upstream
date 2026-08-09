#!/usr/bin/env python3
"""
Leftover Chef — match available ingredients to recipes, ranked by usage.

Usage:
    python3 leftover_chef.py egg rice soy sauce
    python3 leftover_chef.py --list-ingredients
    python3 leftover_chef.py --list-recipes
    python3 leftover_chef.py chicken potato --json
    python3 leftover_chef.py tomato onion garlic --limit 3
    python3 leftover_chef.py pasta garlic --threshold 50

Stdlib only. No external dependencies.
"""

import argparse
import json
import os
import sys
from difflib import SequenceMatcher

# ---------------------------------------------------------------------------
# Load recipe database
# ---------------------------------------------------------------------------

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "recipes_db.json")


def load_recipes(path: str = DB_PATH) -> list:
    """Load the recipe database from JSON."""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("recipes", [])


# ---------------------------------------------------------------------------
# Ingredient normalisation & fuzzy matching
# ---------------------------------------------------------------------------

# Common synonyms / plurals mapped to canonical names
SYNONYMS = {
    "eggs": "egg",
    "tomatoes": "tomato",
    "potatoes": "potato",
    "onions": "onion",
    "carrots": "carrot",
    "garlics": "garlic",
    "garlic clove": "garlic",
    "bell peppers": "bell pepper",
    "peppers": "bell pepper",
    "pepper": "bell pepper",  # ambiguous: could be black pepper; we handle below
    "chickpeas": "chickpea",
    "chick peas": "chickpea",
    "chicken breast": "chicken",
    "chicken thigh": "chicken",
    "chicken thighs": "chicken",
    "ground beef": "ground beef",
    "minced beef": "ground beef",
    "beef mince": "ground beef",
    "soy": "soy sauce",
    "soya sauce": "soy sauce",
    "olive oil": "olive oil",
    "veg oil": "oil",
    "vegetable oil": "oil",
    "canola oil": "oil",
    "white wine": "white wine",
    "rice noodles": "rice noodle",
    "bean sprouts": "bean sprout",
    "beans": "bean",
    "green beans": "bean",
    "green bean": "bean",
    "spring onion": "scallion",
    "green onion": "scallion",
    "pinenuts": "pine nut",
    "pine nuts": "pine nut",
    "corn flour": "flour",
    "plain flour": "flour",
    "all-purpose flour": "flour",
    "ap flour": "flour",
    "spuds": "potato",
    "spud": "potato",
    "taters": "potato",
    "scallions": "scallion",
    "shrimp": "shrimp",
    "prawns": "shrimp",
    "prawn": "shrimp",
    "salmon fillet": "salmon",
    "beef stew meat": "beef",
    "stewing beef": "beef",
    "chicken broth": "chicken broth",
    "stock": "chicken broth",
    "chicken stock": "chicken broth",
    "cabbage": "cabbage",
    "red cabbage": "cabbage",
    "avocados": "avocado",
    "limes": "lime",
    "lemons": "lemon",
    "berries": "berry",
    "blueberries": "berry",
    "strawberries": "berry",
    "grapes": "grape",
    "bananas": "banana",
    "apples": "apple",
    "cucumbers": "cucumber",
    "mozzarella cheese": "mozzarella",
    "parmesan cheese": "parmesan",
    "feta cheese": "feta",
    "cheddar": "cheese",
    "cheddar cheese": "cheese",
    "baking soda": "baking soda",
    "bicarbonate of soda": "baking soda",
    "cilantro": "cilantro",
    "coriander leaf": "cilantro",
    "fresh coriander": "cilantro",
}

# Tokens that should map to "black pepper" rather than bell pepper
PEPPER_BLACK = {"black pepper", "blackpepper", "ground pepper"}


def normalise(raw: str) -> str:
    """Normalise a single ingredient token to canonical form."""
    s = raw.strip().lower()
    if s in PEPPER_BLACK:
        return "black pepper"
    # direct synonym lookup
    if s in SYNONYMS:
        return SYNONYMS[s]
    # try singular of simple plurals
    if s.endswith("es") and len(s) > 3:
        candidate = s[:-2]
        if candidate in SYNONYMS:
            return SYNONYMS[candidate]
    if s.endswith("s") and len(s) > 2:
        candidate = s[:-1]
        if candidate in SYNONYMS:
            return SYNONYMS[candidate]
    return s


def fuzzy_match(have: str, need: str, threshold: float = 0.82) -> bool:
    """Return True if `have` and `need` are similar enough."""
    if have == need:
        return True
    # containment handles "garlic clove" vs "garlic"
    if have in need or need in have:
        return True
    ratio = SequenceMatcher(None, have, need).ratio()
    return ratio >= threshold


def have_ingredient(needed: str, available: set) -> bool:
    """Check if a needed ingredient is available (with fuzzy matching)."""
    for avail in available:
        if fuzzy_match(avail, needed):
            return True
    return False


# ---------------------------------------------------------------------------
# Matching engine
# ---------------------------------------------------------------------------


def match_recipes(available_raw: list, recipes: list) -> list:
    """
    Score every recipe against available ingredients.

    Returns list of dicts:
      recipe, ingredients_have, ingredients_missing, usage_pct,
      missing_count, total_ingredients
    Sorted by usage_pct desc, then missing_count asc.
    """
    available = {normalise(x) for x in available_raw}
    results = []

    for r in recipes:
        needed = r.get("ingredients", [])
        have_list = []
        missing_list = []
        for ing in needed:
            ing_n = normalise(ing)
            if have_ingredient(ing_n, available):
                have_list.append(ing)
            else:
                missing_list.append(ing)
        total = len(needed)
        have_count = len(have_list)
        usage_pct = round(100 * have_count / total, 1) if total else 0
        results.append(
            {
                "recipe": r,
                "ingredients_have": have_list,
                "ingredients_missing": missing_list,
                "usage_pct": usage_pct,
                "have_count": have_count,
                "missing_count": len(missing_list),
                "total_ingredients": total,
            }
        )

    # Sort: highest usage first; on tie, fewer missing items
    results.sort(key=lambda x: (x["usage_pct"], -x["missing_count"]), reverse=True)
    return results


# ---------------------------------------------------------------------------
# Output formatting
# ---------------------------------------------------------------------------

USAGE_BAR_WIDTH = 20


def format_bar(pct: float, width: int = USAGE_BAR_WIDTH) -> str:
    filled = int(pct / 100 * width)
    return "█" * filled + "░" * (width - filled)


def format_result_text(idx: int, r: dict) -> str:
    recipe = r["recipe"]
    lines = []
    lines.append(
        f"  {idx}. {recipe['name']}  —  {r['usage_pct']}% ingredients "
        f"({r['have_count']}/{r['total_ingredients']})"
    )
    lines.append(f"     {format_bar(r['usage_pct'])}")
    lines.append(f"     Time: {recipe.get('time_min', '?')} min  "
                 f"Difficulty: {recipe.get('difficulty', '?')}  "
                 f"Cuisine: {recipe.get('cuisine', 'any')}")
    if r["ingredients_have"]:
        lines.append(f"     ✓ Have: {', '.join(r['ingredients_have'])}")
    if r["ingredients_missing"]:
        lines.append(f"     ✗ Missing: {', '.join(r['ingredients_missing'])}")
    return "\n".join(lines)


def format_results_text(results: list, available_raw: list) -> str:
    lines = []
    lines.append("=" * 60)
    lines.append("  🍳 LEFTOVER CHEF")
    lines.append(f"  Ingredients: {', '.join(available_raw)}")
    lines.append(f"  Matches found: {len(results)}")
    lines.append("=" * 60)
    lines.append("")

    perfect = [r for r in results if r["missing_count"] == 0]
    partial = [r for r in results if 0 < r["missing_count"] <= 2 and r["usage_pct"] >= 50]

    if perfect:
        lines.append("  ★ You have everything for these — cook now!")
        for i, r in enumerate(perfect, 1):
            lines.append(format_result_text(i, r))
            lines.append("")
    if partial:
        lines.append("  ◐ Almost there — missing 1–2 items:")
        for i, r in enumerate(partial, len(perfect) + 1):
            lines.append(format_result_text(i, r))
            lines.append("")
    if not perfect and not partial:
        lines.append("  No strong matches. Best partial matches:")
        for i, r in enumerate(results[:5], 1):
            lines.append(format_result_text(i, r))
            lines.append("")
    return "\n".join(lines)


def format_results_json(results: list) -> str:
    """Format results as compact JSON."""
    out = []
    for r in results:
        out.append(
            {
                "name": r["recipe"]["name"],
                "usage_pct": r["usage_pct"],
                "have_count": r["have_count"],
                "missing_count": r["missing_count"],
                "total_ingredients": r["total_ingredients"],
                "ingredients_have": r["ingredients_have"],
                "ingredients_missing": r["ingredients_missing"],
                "time_min": r["recipe"].get("time_min"),
                "difficulty": r["recipe"].get("difficulty"),
                "cuisine": r["recipe"].get("cuisine"),
                "instructions": r["recipe"].get("instructions", ""),
                "servings": r["recipe"].get("servings"),
            }
        )
    return json.dumps(out, indent=2, ensure_ascii=False)


def list_all_ingredients(recipes: list) -> str:
    """Print every unique ingredient in the database."""
    seen = set()
    for r in recipes:
        for ing in r.get("ingredients", []):
            seen.add(ing)
    lines = [f"All {len(seen)} known ingredients:\n"]
    for ing in sorted(seen):
        lines.append(f"  • {ing}")
    return "\n".join(lines)


def list_all_recipes(recipes: list) -> str:
    """Print every recipe name."""
    lines = [f"All {len(recipes)} recipes:\n"]
    for i, r in enumerate(recipes, 1):
        lines.append(f"  {i}. {r['name']} ({r.get('cuisine', '?')}, {r.get('time_min', '?')} min)")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Match leftover ingredients to recipes."
    )
    p.add_argument(
        "ingredients",
        nargs="*",
        help="Ingredients you have (space or comma separated).",
    )
    p.add_argument("--json", action="store_true", help="Output JSON.")
    p.add_argument("--limit", type=int, default=10, help="Max results to show.")
    p.add_argument(
        "--threshold",
        type=int,
        default=0,
        help="Minimum usage %% to display (default 0).",
    )
    p.add_argument(
        "--list-ingredients", action="store_true", help="List all known ingredients."
    )
    p.add_argument(
        "--list-recipes", action="store_true", help="List all recipe names."
    )
    return p


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    recipes = load_recipes()

    if args.list_ingredients:
        print(list_all_ingredients(recipes))
        return 0
    if args.list_recipes:
        print(list_all_recipes(recipes))
        return 0

    # Flatten comma-separated input
    raw_input = []
    for item in args.ingredients:
        for part in item.split(","):
            part = part.strip()
            if part:
                raw_input.append(part)

    if not raw_input:
        parser.print_help()
        return 1

    results = match_recipes(raw_input, recipes)

    # Apply threshold
    results = [r for r in results if r["usage_pct"] >= args.threshold]

    # Apply limit
    results = results[: args.limit]

    if not results:
        print("No matching recipes found. Try different or fewer ingredients.")
        return 0

    if args.json:
        print(format_results_json(results))
    else:
        print(format_results_text(results, raw_input))

    return 0


if __name__ == "__main__":
    sys.exit(main())
