# Costing — What a Recipe Actually Costs Per Serving

`cost_per_serving = Σ (quantity_used ÷ edible_yield × unit_price) ÷ servings`, every amount carrying its currency.

**Read `## Prices` in `~/Clawic/data/recipe/memory.md`** (or `prices.md` if `## Boxes` points there) before quoting any cost. A price older than ~6 months is an estimate and the answer says so. Currency comes from `currency` in `config.yaml`, falling back to `~/Clawic/profile.yaml`.

## The Calculation

1. **Unit price from a package price**: `unit_price = package_price ÷ package_quantity`. A 1.2 kg tray at 7.70 EUR is 6.42 EUR/kg — recipes are costed per kilogram and per litre, never per package.
2. **Correct for edible yield** where the recipe's quantity is *after* trimming but the purchase is *before*: `purchase_quantity = recipe_quantity ÷ yield_factor`.
3. **Sum the lines**, then divide by `servings` from the recipe frontmatter.
4. **Round to the nearest sensible unit** and state the date and the shop the prices came from. A cost per serving with no date is a number that will be wrong within a year.

Worked, at 4 servings: 700 g chicken thigh at 6.42 EUR/kg with a 0.75 bone-in yield → 933 g purchased → 5.99 EUR. 400 g tinned tomato at 1.60 EUR/kg → 0.64. 200 g yoghurt at 2.40 EUR/kg → 0.48. Aromatics and spice, estimated → 0.80. Total 7.91 EUR → **1.98 EUR per serving** (prices as of 2026-07-12, local supermarket).

## Edible Yield Factors

Typical ranges — weigh once in the user's own kitchen and record the real figure, because knife skill and trim standards move these by 10 points.

| Ingredient | Yield after trim/prep | Note |
|---|---|---|
| Onion | 0.88-0.92 | Skin and ends only |
| Carrot, peeled | 0.80-0.85 | Unpeeled is ~0.95 |
| Broccoli → florets | 0.60-0.65 | The stalk is edible; using it moves this to ~0.90 |
| Cauliflower → florets | 0.55-0.65 | Same |
| Leafy greens, stemmed | 0.60-0.75 | Spinach lower, chard higher |
| Whole chicken → raw meat | 0.50-0.55 | The carcass makes stock, which is why whole birds cost less per gram of meat |
| Bone-in thigh → meat | 0.70-0.78 | — |
| Whole round fish → fillet | 0.40-0.50 | Flat fish lower still |
| Prawns, shell-on | 0.50-0.60 | — |
| Dried pulses → cooked | 2.2-2.5× (gain) | 100 g dry ≈ 230 g cooked; this is why dry beans undercut tins by a factor of three |
| Rice, dry → cooked | 2.5-3× (gain) | — |
| Hard cheese, rind on | 0.90-0.95 | Rind goes into stock |

## The Lines People Forget

- **Spices and aromatics.** Individually trivial, collectively 5-15% of a home-cooked dish. Either cost them properly per gram from the jar price, or add a flat estimate line and label it — never silently omit them, which is what makes home-cooking-versus-takeaway comparisons dishonest.
- **Oil and fat used for cooking**, not just the fat in the ingredient list.
- **Energy**, when comparing methods: a 3-hour oven braise costs real money and an air fryer or pressure cooker for the same dish costs a fraction of it. Only include it when the question is a method comparison; otherwise note it and leave it out.
- **Waste**, when the recipe uses part of a pack that will not be used elsewhere. That is a cost of *this* recipe, and it is the number that makes "cheap" recipes with one exotic ingredient look expensive — correctly.
- Salt, pepper and water from `pantry_staples` are excluded by convention. Say so once.

## Comparisons Worth Making

| Question | How to answer honestly |
|---|---|
| Cheaper than the takeaway? | Include spices, oil, and the unused fraction of packs. Exclude labour unless the user asks for it, and say that you did |
| Which of these two recipes is cheaper per serving? | Only comparable if both yields are real and both use the same price date |
| Is batch cooking cheaper? | Compare cost per serving at ×1 and at the batch factor, including any larger package price break — the saving is usually the package break, not the cooking |
| Where is the money going in this dish? | Sort the lines descending; one ingredient is typically over half. That line is the substitution lever (`substitutions.md`) |
| Did the weekly food spend go up? | That is a household budget question — the shared finances box, not this skill. Cost per serving is what this file owns |

## Keeping Prices Usable

- Record `unit price with currency in the value` (`6.42 EUR/kg`), the package it came from, the shop, and the date read. Without the date the row is worthless within a season.
- Refresh from a receipt on the `price_refresh` cadence rather than item by item — a receipt updates twenty rows in one pass.
- Keep the package size the shop actually sells alongside the unit price: it is what the shopping list has to round to (`planning.md`).
- Record only ingredients that recur. Costing a one-off dish uses a stated estimate and writes nothing.

**Write after any costing pass**: each unit price read from a receipt, shelf, or order into `## Prices` of `~/Clawic/data/recipe/memory.md` with its currency, package size, shop and date — and the shop's package sizes alongside them, because the shopping list rounds to those. Past ~15 ingredients the section splits to `prices.md` with the same heading plus `## Package Sizes`. A measured edible yield from this kitchen goes in the same row's notes rather than being re-derived (`memory-template.md`).
