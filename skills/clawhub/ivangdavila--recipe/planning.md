# Planning — A Week From the Collection, and One Shopping List

Two deliverables: a plan whose recipes overlap on purpose, and a single aggregated list. Both come from the collection, not from imagination.

**Read `~/Clawic/data/recipe/index.md`, `## Household` in `memory.md`, `~/Clawic/data/health/profile.md`, and `plans/<year>.md`** (or whatever `## Boxes` points to) before proposing a week. The last one carries the previous week's leftovers and what was already eaten twice this month — planning without it repeats dishes and re-buys what is in the fridge.

## Building the Week

1. **Count the actual meals.** Nights out, leftovers nights, and a night where nobody cooks. A seven-recipe week for a household that eats out twice is two wasted shops.
2. **Anchor with one project and fill with weeknights.** Effort tags do this: at most one `project` or `weekend` recipe per week unless the user says otherwise; the rest at or under the weeknight ceiling in `## Household` (default 35 min active).
3. **Chain the perishables.** The bunch of coriander, the tub of yoghurt, the half tin of coconut milk: pick the second recipe to finish what the first one opens. This is the single largest waste reduction available and it is a scheduling decision, not a cooking one.
4. **Cook once, eat twice, deliberately.** Mark which dinners are scaled to produce lunches and put the scale factor in the plan row, not in the recipe.
5. **Vary the shape, not just the cuisine.** Three tomato-based braises in a week feel repetitive even across three cuisines. Alternate the dominant technique and the dominant acid.
6. **Front-load the fragile.** Fish and leafy greens in the first two days after a shop; roots, pulses, frozen and pantry dishes later in the week.
7. **Include one never-made recipe** when the week has capacity — this is where the untried third of the collection gets used (`library.md`).

## Prep-Ahead Ordering

For a cook-ahead day, order the work by what blocks what, not by recipe:

- Anything with a long unattended phase first: doughs, stocks, brines, marinades, soaked pulses. Their clock runs while you do everything else.
- Then oven work, grouped by temperature — an oven at one temperature can carry several trays; two temperatures is two sessions.
- Then hob work, then cold assembly.
- Wash-up choke point: one pan used by three recipes serialises them. Either wash between or pick a different recipe.
- Store components, not assembled dishes. A dressed salad, a sauced pasta and a soaked crumble all degrade; their parts do not.

## Shopping List Aggregation

The arithmetic is the point. Doing this by hand per recipe is how the same onion gets bought three times.

1. **Normalise every line to one unit per ingredient** — grams for solids, millilitres for liquids, count only for genuinely countable items (eggs, lemons, tins).
2. **Sum across the plan**, applying each recipe's scale factor first.
3. **Subtract `pantry_staples`** from `config.yaml`, and anything the user says is already in the house.
4. **Round up to a purchasable package size** and record the leftover: `750 g needed → 1 kg bag, 250 g over`. That leftover is next week's chaining input.
5. **Group by where it is bought** — produce, meat/fish, dairy, dry goods, frozen, other — in the order of the shop, not alphabetically.
6. **Flag the substitutions in advance**: for each ingredient with a known-good swap, put it in brackets so the decision is made in the aisle, not abandoned.
7. **Keep the recipe attribution on the line** where two recipes want different forms of the same thing: `onion 500 g (2 for the ragù diced, 1 for the dal sliced)`. Without it, the prep is guesswork.

Store-level pantry management, stock levels and household quantities are `grocery`'s job; this file's job ends at a correct, aggregated, rounded list generated from the plan.

## Waste Arithmetic

- The list is right when the fridge is empty on shopping day. Record it once in the carry-over line of that week's section in `~/Clawic/data/recipe/plans/<year>.md`: what got thrown away and which recipe bought it. Two cycles of that is enough to fix the pattern.
- Herb bunches, cream, and fresh cheese are the three biggest single-purchase wastes in a domestic kitchen because recipes call for a fraction of the smallest pack. Plan them as chains or buy the frozen/long-life form.
- A recipe that requires one ingredient bought only for it, unused elsewhere, and costing more than the rest of the dish, is a `project` recipe — tag it and stop putting it in weeknight plans.

## Events and Guests

- Read the guests' rows in `~/Clawic/data/contacts/contacts.md` for restrictions before choosing anything. Ask nothing that is already recorded there.
- Build the menu around what can be finished ahead: for a table of 8+, at most one dish should need active work in the last 30 minutes.
- Check the oven and hob contention explicitly — two dishes needing 200 °C and the same shelf at the same time is the failure that shows up at the table, not on the page.
- A menu with timings is an artifact, not a plan row: `artifacts/menu-<name>.md`, with a run-sheet counting backwards from service (T−48h, T−24h, T−4h, T−45min, plate). The plan row points at it.
- Quantities for a crowd: 150-200 g protein per adult before trim, 60-80 g dry pasta or rice, 300-400 g vegetables in total. Scale by heads, then apply the pot ceilings from `## Kitchen` (`scaling.md`).

**Write when a plan is made or a week ends**: the plan section in `~/Clawic/data/recipe/plans/<year>.md`, including the generated-list date and the carry-over line of what was bought and not used — the carry-over is what picks next week's recipes. An event menu with timings goes to `artifacts/menu-<name>.md` with its `## Boxes` line in the same turn. A guest's restriction learned while planning goes into their `Context` in `~/Clawic/data/contacts/contacts.md` (`memory-template.md`).
