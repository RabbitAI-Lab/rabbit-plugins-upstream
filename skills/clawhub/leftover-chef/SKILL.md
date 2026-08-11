---
name: leftover-chef
description: >
  Suggests recipes based on leftover ingredients you already have. Takes a list of
  ingredients (from photo description, text, or voice) and generates recipes ranked
  by how completely they use what's available. Includes a 50+ recipe database and a
  Python matcher that flags missing ingredients.
version: 1.0.0
author: Denis Voronin
license: MIT
tags:
  - cooking
  - recipes
  - food-waste
  - sustainability
  - meal-planning
---

# Leftover Chef

Turn random leftover ingredients into meals you can actually cook tonight.

## When to use

- The user lists ingredients they have (e.g. "I have eggs, rice, and soy sauce").
- The user describes a fridge photo or voice inventory.
- The user wants to reduce food waste by cooking with what's on hand.

## How it works

1. Collect the user's available ingredients as a simple list (comma or space separated).
2. Run `scripts/leftover_chef.py` with the ingredients as arguments.
3. The script matches against a built-in database of 50+ recipes (JSON, stdlib only).
4. Recipes are ranked by **usage ratio**: how many of your ingredients the recipe uses
   vs. how many the recipe needs that you don't have.
5. Each result shows the recipe, which ingredients you have, which are missing, and a
   usage percentage.

## Usage

### From the command line

```bash
python3 scripts/leftover_chef.py eggs rice soy sauce
python3 scripts/leftover_chef.py --list-ingredients
python3 scripts/leftover_chef.py chicken potato --json
python3 scripts/leftover_chef.py tomato onion garlic --limit 3
```

### Options

| Flag | Description |
|------|-------------|
| `--json` | Output results as JSON |
| `--limit N` | Show top N matches (default 10) |
| `--threshold P` | Minimum usage percent to show (default 0) |
| `--list-ingredients` | Print all known ingredients |
| `--list-recipes` | Print all recipe names |

### Interpreting results

- **Usage 100%**: you have every ingredient. Cook it now.
- **Usage 70–99%**: you're missing 1–2 items — easy substitution or quick store run.
- **Usage 40–69%**: partial match, listed for inspiration.
- **Missing** items are printed with a warning so the agent can suggest substitutions.

## Agent workflow

1. Ask for or receive the ingredient list.
2. Run the script and read the ranked output.
3. Present the top 3–5 matches to the user with a short pitch for each.
4. Offer substitution suggestions for any missing ingredients.
5. Optionally read a full recipe from `references/recipes.md` for details.

## Files

- `scripts/leftover_chef.py` — main matcher script (Python 3, stdlib only)
- `scripts/recipes_db.json` — embedded recipe database (50+ recipes)
- `references/recipes.md` — detailed cooking notes for featured recipes
- `references/substitutions.md` — common ingredient substitutions
