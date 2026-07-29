# Scaling — Batch, Pan, and the Terms That Refuse

`factor = target ÷ base`. Multiply the masses, then walk the non-linear terms in SKILL.md (What Does Not Scale) and everything below. A scaled recipe that only changed the numbers is wrong in the pan, the timing, or the seasoning.

**Read `## Kitchen` in `~/Clawic/data/recipe/memory.md` before quoting a scale factor.** The largest pot, the mixer bowl, the oven shelf and the tin sizes are hard ceilings: a ×3 that does not fit in a 5 L pot is not a recipe, it is three cooks.

## The Procedure

1. Convert to weight first (`conversion.md`). Scaling volumes multiplies the volume error along with the quantity.
2. `factor = target_servings ÷ base_servings`, kept as a decimal, not rounded to a "nice" number.
3. Multiply every bulk mass. Round to what a scale can read: 1 g under 100 g, 5 g above.
4. Recompute the vessel by **area** (below), not by capacity.
5. Correct the non-linear terms: seasoning, aromatics, leavener, yeast, evaporation.
6. Restate every time as an internal temperature or an observable cue (SKILL.md Rule 5).
7. Check the ceilings from `## Kitchen`, and say which one binds if any does.
8. Write the result into `## Variations` marked `untested`, or into a new recipe file if it is a permanent change.

## Pan and Tin Geometry

Batter and braise depth is what cooks; area is what carries the batch.

- Round: `area = π × (diameter ÷ 2)²`. Square/rectangular: `L × W`.
- Target: `new_area = old_area × factor`, keeping depth the same.
- Common tins: 15 cm round = 177 cm² · 18 cm = 254 · 20 cm = 314 · 23 cm = 415 · 25 cm = 491 · 20×20 cm square = 400 · 23×33 cm rect = 759 · half-sheet 33×45 cm = 1485 · 900 g loaf ≈ 21×11 cm = 231.
- Worked: doubling a 20 cm round cake (314 cm²) needs 628 cm² — that is a 23×33 cm rectangle (759, 20% loose, bake ~5 min less) or two 20 cm tins. It is *not* a 25 cm round (491 — 22% short, so the batter is 28% deeper and the centre stays raw).
- Depth changes time far more than area does. If the depth rises more than ~20%, drop the temperature 10-15 °C and extend, or the outside sets first.
- Filling level: cake batter to ⅔ of the tin, bread dough to ½, braises to ⅔ with liquid ⅓-⅔ up the solids. Above those, it goes over the side.

## Time Under Scale

- **Roasts and whole birds**: for the same shape, `thickness ∝ mass^(1/3)` and `time ∝ thickness²`, so `time_factor ≈ mass_factor^(2/3)`. Doubling adds ~60%; tripling adds ~110%. Always finish on internal temperature.
- **A doubled tray of anything thin** — cookies, roasted vegetables, sheet-pan dinners — is two trays at the same time, rotated at the halfway point, not one crowded tray. Crowding switches roasting to steaming; the observable is that liquid pools instead of evaporating.
- **Pot dishes**: the cook time barely moves; the *heat-up* and the *reduction* both grow (below).
- **Baked goods in the right-sized tin**: time is close to unchanged. Start checking at the original time.
- Under a pressure cooker, time does not scale with quantity at all — only the come-to-pressure time does (`equipment.md`).

## Evaporation and Reduction

Evaporation rate tracks exposed surface area, not volume.

- Same pan, double the sauce → roughly double the reduction time.
- To hold the time, double the surface area: a 24 cm pan (452 cm²) becomes a 34 cm pan (908 cm²), or two pans.
- This is the single most common failure of a scaled braise or ragù: the recipe says "reduce for 20 minutes", the tripled batch needs an hour, and the cook stops on the clock and serves it thin.
- The observable cue that replaces the clock: a spoon drawn across the base leaves a track that closes slowly, or the volume has dropped to the level marked before the reduction started.

## Seasoning Under Scale

- Salt in a pot dish: scale it, then add 80% and correct at the end. You can add salt; you cannot remove it.
- Chili, garlic, raw alliums, strong spice, alcohol: start at 75% of the scaled amount at `factor` ≥ 2, then taste. Also gated by `spice_level`.
- Salt in a dough or a cure is a percentage of flour or of meat weight and scales exactly (`vetting.md` bands).
- Acid (vinegar, citrus) scales linearly but is the easiest correction at the end — hold 20% back with the salt.

## Fractional and Awkward Quantities

- **Eggs**: whisk one and weigh. US large = 50 g out of shell, white 30 g, yolk 20 g. Half an egg is 25 g of whisked whole egg. Never round a half egg up in a batter — it is 6% of the liquid in a two-egg cake.
- **Half a tin, half a packet**: use the whole one and scale the rest of the recipe to it, or record the leftover on the plan's carry-over line so it becomes next week's recipe (`planning.md`).
- **Spices under 1 g**: a kitchen scale that reads to 1 g cannot measure 0.4 g of cinnamon. Use the spoon measure for anything below ~2 g and accept it.
- **Yeast under 1 g** in a small overnight dough: measure by making a slurry — dissolve 5 g in 50 ml of water and use a tenth of it.

## Scaling Down

Halving is not the safe direction; it fails differently.

- Surface-to-volume rises, so evaporation and browning run faster: reduce the heat or the time, and check earlier.
- A halved batter in a halved tin is fine; a halved batter in the original tin is a thin, dry disc.
- Aromatics that were "1 onion" become "half an onion", and the pan is now too big — step down one pan size or the fond burns.
- Below ~½ of the original, a bread dough is hard to knead and a custard is hard to temper. At that point, make the full batch and freeze half.

## Baker's Percentage

For anything where flour is the backbone, percentages make scaling trivial and cross-recipe comparison possible.

- Flour = 100%. Every other ingredient is a percentage of total flour weight.
- `ingredient_g = flour_g × percentage`. To hit a target dough weight: `flour_g = target_total ÷ sum_of_all_percentages`.
- Worked: a 70% hydration, 2% salt, 0.6% instant yeast dough for a 900 g loaf → percentages total 172.6% → flour = 900 ÷ 1.726 = 521 g, water 365 g, salt 10 g, yeast 3 g.
- Bands to stay inside are in `vetting.md`. Percentages are also what let two bread recipes be compared at a glance, which mass never does.

**Write when a scale is produced**: the scaled version into the recipe's `## Variations` with its factor, the tin or pot used, and `untested` until it has been cooked (SKILL.md Rule 8). If a ceiling bound the scale — pot volume, mixer bowl, oven shelf — that ceiling belongs as one line in `## Kitchen` of `~/Clawic/data/recipe/memory.md`, because it will bind again. After the scaled version is cooked, `testing.md` decides whether it is promoted (`memory-template.md`).
