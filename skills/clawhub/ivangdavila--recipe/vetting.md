# Vetting — Will This Recipe Work Before You Cook It

A recipe can be checked against its own ratios in about a minute. Most failures are visible on the page: a leavener out of band, a hydration that cannot produce the pictured crumb, a braise with no liquid, a yield that does not match the tin.

**Read `## Sources` in `~/Clawic/data/recipe/memory.md` first** (or `sources.md` if `## Boxes` points there): a source already marked `untrusted` earns a closer read, and one marked `reliable` earns the benefit of the doubt on an odd-looking number.

## The Ratio Checks

Convert to grams first (`conversion.md`), then compare against the band. Outside the band is not automatically wrong — it is a question the recipe has to answer.

| Ratio | Band | Formula | Out of band means |
|---|---|---|---|
| Bread hydration | 60-70% standard, 75-85% ciabatta/focaccia, 100%+ only for batters | water ÷ flour, by weight | Below 55%: a stiff dough that will not open up. Above 85% with no folds or shaping instruction: the method is missing |
| Salt in bread | 1.8-2.2% | salt ÷ flour | Above 3% slows the yeast measurably; 0% is a technique choice, not an omission, and the recipe should say so |
| Instant yeast | 0.5-1% same-day, 0.1-0.3% overnight cold | yeast ÷ flour | 2% with a 12-hour rise over-ferments; 0.2% with a 2-hour rise never rises |
| Chemical leavener | 1-1¼ tsp baking powder (4-5 g) per 120 g flour | powder ÷ flour | Double the band tastes metallic and collapses; half never lifts. **Exception**: self-raising flour is manufactured at ~6 g per 120 g, so a recipe using it — or converted from it (`substitutions.md`) — reads high by design and is in band |
| Baking soda without acid | Needs buttermilk, yoghurt, brown sugar, cocoa (natural, not Dutched), citrus, or vinegar | — | Soda with no acid in the list is either a typo for powder or a soapy cake |
| Cake fat-to-flour | 50-100% for a butter cake | fat ÷ flour | Under 30% with no other tenderizer reads dry; over 120% is a shortbread |
| Custard | 1 large egg (50 g) sets ~120-150 ml dairy | dairy ÷ egg | Far above: it will not set. Far below: it is scrambled |
| Brine | 5-8% salt for a wet brine; 1-1.5% of meat weight for a dry brine/cure | salt ÷ water, or salt ÷ meat | A 15% brine over 12 hours is inedible; the recipe means a shorter time or a lower figure |
| Braise liquid | Liquid reaching ⅓ to ⅔ up the meat | — | Fully submerged is a boil; a dry pot with a 3-hour time is a burn |
| Pickle vinegar | ≥5% acetic acid vinegar for shelf-stable, ≥1:1 with water | — | A refrigerator pickle can go weaker; a canned one cannot, and the recipe must distinguish |

## Structural Red Flags

| Flag | Why it predicts failure |
|---|---|
| No yield, or a yield with no unit | Nothing can be scaled, costed, or shopped for; often means the recipe was never tested at a fixed size |
| Ingredient in the list that never appears in a step | Either a step is missing or the list is from a different version of the recipe |
| Ingredient in a step that is not in the list | Same problem, worse — you will discover it mid-cook |
| Times with no cues, throughout | "Cook 8 minutes" travels badly between hobs, pans and quantities; a tested recipe states what it should look like |
| Only one temperature for a two-stage bake | Breads and roasts that need a sear then a drop will say so; one number often means untested |
| "Bake until golden brown" as the only doneness cue on something with a food-safety floor | Poultry, pork, eggs, and reheated rice have internal temperatures; colour is not one of them |
| A photograph that cannot come from the method | Charred edges with no broiler step; an open crumb at 58% hydration; a glaze with no reduction |
| Volume measures for a yeasted dough or a laminated pastry | The ratio matters to a few percent and cups cannot deliver that |
| Comment section full of "I made these changes and it worked" | The published version is not the one that works; read the changes before cooking |

## Food-Safety Floors

These are not preferences and no vetting pass waves them through. Internal temperature, at the thickest point, held for the time given.

| Food | Floor | Note |
|---|---|---|
| Poultry, whole or pieces | 74 °C / 165 °F instant | Lower with a held time is a professional pasteurization table, not a home shortcut |
| Ground meat (beef, pork, lamb) | 71 °C / 160 °F | Grinding moves surface bacteria through the mass |
| Whole-muscle beef and lamb | 52-63 °C / 125-145 °F by preference | Surface-only contamination; a seared exterior is the control |
| Pork, whole cuts | 63 °C / 145 °F plus 3 min rest | The old 71 °C figure was retired; a recipe still using it will be dry |
| Fish | 52-63 °C / 125-145 °F | Raw service depends on the supply chain and freezing history, not on the recipe |
| Eggs, dishes with runny yolk | 71 °C / 160 °F for the safe version | Pasteurized eggs are the escape hatch for a raw preparation |
| Leftovers, reheated | 74 °C / 165 °F throughout | Cooked rice held warm is the classic *Bacillus cereus* case: cool fast, refrigerate within 1 hour, reheat once |
| Home canning, low-acid foods | Pressure canning only | A boiling-water bath cannot reach the temperature botulinum spores need. A recipe that says otherwise is discarded, not adapted |

Anything in this table suspends the recipe: fix the recipe to meet the floor, or do not cook it. If the user reports an illness after a meal, that is a clinician's question, not a recipe question.

## Verdicts

- **Cook it** — ratios in band, steps complete, cues present.
- **Cook it with these three corrections** — name each one and where the number came from. Write the corrected version into the recipe's `## Ingredients` and keep the source's numbers in `## Original`.
- **Do not cook it** — a safety floor is violated, or two or more structural flags stack. Say which, and offer to find the same dish from a source marked `reliable`.

**Write after any vetting pass that changed something**: corrections into the recipe file's `## Ingredients` with the source's numbers left intact in `## Original`, and the finding as one line in `## Notes`. A source that caused a real failure, or that has now been vindicated twice, gets its row updated in `## Sources` of `~/Clawic/data/recipe/memory.md` — two traced failures is what turns a source `untrusted` (`memory-template.md`).
