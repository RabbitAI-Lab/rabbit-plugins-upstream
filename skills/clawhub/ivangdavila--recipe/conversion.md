# Conversion — Units, Temperatures, Altitude

Volume-to-weight is per ingredient, never a single factor. Everything else here is a fixed table or a formula.

**Read `## Kitchen` in `~/Clawic/data/recipe/memory.md` before converting a temperature or a salt quantity**: the oven's measured offset and the salt brand in use are the two facts that make a correct conversion wrong in that specific kitchen.

## Volume to Weight

Per 1 US cup (236.6 ml), rounded to the nearest 5 g. Use the ingredient's own row.

| Ingredient | g/cup | Note |
|---|---|---|
| Water, milk, stock | 235 | Cream 240, buttermilk 245 |
| Plain / all-purpose flour | 120 | Spoon-and-level (King Arthur standard). Dip-and-sweep gives ~142 — an 18% difference |
| Bread flour | 120 | Whole wheat 113, rye 100, cake flour 115 |
| Granulated sugar | 200 | Caster 200, brown packed 213, icing/powdered 120 |
| Butter | 227 | 1 US stick = 113 g = 8 tbsp |
| Oil | 218 | Olive, neutral — within a few grams of each other |
| Honey, golden syrup, molasses | 340 | Weigh these; a wet cup measure loses 10-15% to the sides |
| Yoghurt, sour cream | 245 | Greek-style 250 |
| Cocoa powder | 85 | Compresses badly; the volume error here is the worst in the list |
| Rolled oats | 90 | Steel-cut 180 |
| Rice, long grain raw | 185 | Arborio 200 |
| Table salt | 290 | ~6 g/tsp |
| Kosher salt, Diamond Crystal | 135 | ~2.8 g/tsp |
| Kosher salt, Morton | 230 | ~4.8 g/tsp |
| Grated parmesan | 100 | Wildly dependent on the grater — weigh |
| Chopped nuts | 120 | Whole 140 |
| Anything not listed | Weigh it once and add the row | Then it is in `## Prices`/`## Kitchen` territory only if it recurs; otherwise just state the measured figure |

The formula for anything absent: `grams = ml × density`. Water is 1.00 g/ml, oil ~0.92, honey ~1.42, flour as packed ~0.51.

## Cup, Spoon, and Ounce

| Unit | Millilitres | Trap |
|---|---|---|
| US cup | 236.6 | Often written as 240 on labels; the difference is under 2% and rarely matters |
| Metric cup (AU, NZ) | 250 | 6% more than a US cup — compounding across 4 cups of flour is half a cup |
| Japanese cup (合 gō-adjacent usage) | 200 | Japanese rice cookers use 180 ml for rice specifically |
| UK legacy cup | 284 | Half an imperial pint. Only in older British books |
| Tablespoon | 15 | **Australia: 20 ml.** An Australian recipe's tbsp of baking powder is a third more leavener |
| Teaspoon | 5 | Consistent worldwide |
| Fluid ounce (US) | 29.6 | Imperial fl oz is 28.4 — a 4% gap that matters over a pint |
| Pint | US 473 / imperial 568 | 20% apart. British and American recipes are not interchangeable on pints |
| Ounce (weight) | 28.35 g | `oz` and `fl oz` are different things and recipes drop the `fl` |
| Pound | 453.6 g | — |
| Stone | 6.35 kg | Only in old British game and preserving recipes |

## Oven Temperatures

| °C conventional | °F | Gas mark | Fan / convection °C |
|---|---|---|---|
| 140 | 275 | 1 | 120 |
| 150 | 300 | 2 | 130 |
| 170 | 325 | 3 | 150 |
| 180 | 350 | 4 | 160 |
| 190 | 375 | 5 | 170 |
| 200 | 400 | 6 | 180 |
| 220 | 425 | 7 | 200 |
| 230 | 450 | 8 | 210 |
| 240 | 475 | 9 | 220 |

- Exact conversion: `°C = (°F − 32) × 5 ÷ 9`. Round oven figures to the nearest 5 °C; a dial cannot do better.
- **Fan correction: subtract 20 °C (35 °F), or cut the time by ~25% — one, never both.** Doing both is how a cake comes out raw.
- Apply the kitchen's measured offset *after* the fan correction, and state the final dial number: a 180 conventional recipe, in a fan oven that runs 15 °C hot, is set to 145.
- Fan is wrong for anything that needs a still, humid environment: custards, soufflés, delicate cakes, and most breads that want spring before crust. Turn it off and use the conventional column.

## Altitude

Above ~1000 m the corrections start; above ~2000 m they stack. Driven by `altitude_m`.

- **Boiling point**: `°C ≈ 100 − (altitude_m ÷ 300)`. At 2000 m water boils at ~93 °C, so anything simmered or boiled — pasta, pulses, eggs, stocks, sugar syrups — takes measurably longer and never gets hotter.
- **Chemical leavener**: reduce by roughly ¼ per 1000 m above 1000 m (a 5 g dose becomes ~3.75 g at 2000 m). Lower pressure lets gas expand faster and the structure sets after the collapse.
- **Liquid**: add 15-30 ml per 240 ml above 1000 m; evaporation is faster.
- **Sugar**: reduce ~12 g per 200 g above 1500 m; concentrated sugar weakens the set.
- **Oven**: raise 8-14 °C and shorten the time slightly, so the structure sets before the over-expansion.
- **Sugar syrups and candy**: every target temperature drops by the same amount as the boiling point. A hard-crack recipe calling for 149 °C at sea level wants ~142 °C at 2000 m.
- Deep frying, roasting, and searing are essentially unaffected — they are not pressure-limited.

## Ingredient Name Translation

Same thing, different word. Applied per the `locale` preference area.

`coriander (leaf) = cilantro` · `aubergine = eggplant` · `courgette = zucchini` · `rocket = arugula` · `plain flour = all-purpose` · `strong/bread flour = bread flour` · `caster sugar ≈ superfine` · `icing sugar = powdered/confectioners'` · `double cream ≈ heavy cream (double is ~48% fat, heavy ~36% — double whips stiffer and splits less)` · `single cream ≈ light cream` · `bicarbonate of soda = baking soda` · `cornflour (UK) = cornstarch (US)`, but `corn flour (US) = fine cornmeal` — this pair is the one that ruins a sauce · `treacle ≈ molasses` · `swede = rutabaga` · `mince = ground meat` · `prawns ≈ shrimp` · `capsicum = bell pepper` · `passata = strained tomato purée`, but `tomato purée (UK) = tomato paste (US)` — the second pair that ruins a sauce.

**Write when a conversion produced a durable fact**: a measured oven offset, a salt brand, a tin's true dimensions, or the altitude — one line each in `## Kitchen` of `~/Clawic/data/recipe/memory.md`. The converted quantities go into the recipe's `## Ingredients` with the source's originals preserved in `## Original` (`memory-template.md`). A one-off conversion the user asked about in passing is not durable and is not written.
