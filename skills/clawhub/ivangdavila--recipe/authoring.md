# Authoring — Writing an Original Recipe for Other People

A recipe you wrote for yourself can rely on your kitchen, your salt, and your hands. A recipe written for other people cannot rely on any of them. That difference is the whole craft.

**Read `## Kitchen` in `~/Clawic/data/recipe/memory.md` before writing for publication**: every assumption in it — the oven offset, the salt brand, the tin sizes, the largest pot — is a thing your reader does not share and that has to be stated or designed out.

## The Test Cycle

| Round | Purpose | What changes |
|---|---|---|
| 1 | Does it work at all | Everything; write down what you actually did, not what you planned |
| 2 | Fix the ratio | One variable (`testing.md`), and weigh everything, including what you measured by eye |
| 3 | Fix the method | Step order, timing ranges, cues. Cook from your own written draft and follow it literally — every place you improvise is a missing instruction |
| 4 | Blind test | Someone else cooks it from the text with no verbal help. Their questions are the defects list |
| 5 | Confirm | Cook the corrected text once more, unchanged |

Round 4 is the one people skip and the one that finds the real errors. A recipe that has never been cooked by a stranger is a draft.

## Writing for a Kitchen That Is Not Yours

- **Give weights**, and volumes in parentheses if the audience expects them. A cup is a range (`conversion.md`).
- **Name the salt** and give grams. Diamond Crystal to table salt by volume is roughly a doubling.
- **State the oven type** with every temperature, and give a doneness cue that does not depend on the oven at all.
- **Give tin dimensions**, not "a medium tin", and say what happens with a different size.
- **Give a time range plus the cue that ends it**, always in that order. Ranges are honest; single numbers are a promise no kitchen can keep.
- **Say what it should look, smell and sound like** at the two or three moments where it can go wrong. Sound is the most under-used and the most reliable: a pan that has stopped hissing has stopped browning.
- **Name the failure modes** where they are likely: "if it splits, take it off the heat and whisk in a spoonful of cold cream".
- **Assume no specialist equipment** unless it is in the `equipment` field, and give the manual alternative where one exists.

## Ingredient List Discipline

- Method order, grouped by component, prep after the comma (`format.md`).
- Every item in the list appears in a step, and every item in a step is in the list. This one check catches most published errors (`vetting.md`).
- Divided ingredients state the split explicitly.
- Give a substitution only where you have tested it. An untested substitution in a published recipe is a defect you handed to a stranger.
- Give the state you need: `250 g butter, cold, cubed` and `250 g butter, softened` are different recipes.

## The Headnote

Three jobs, in one to three sentences: what the dish is, why this version differs from the obvious one, and the one thing that will go wrong if the reader is careless. Everything else — the trip, the grandmother, the season — belongs somewhere that is not the recipe. If the headnote does not change what the reader does, cut it.

## Yield, and Why It Has To Be Real

- Countable where possible: `12 muffins`, `1 × 900 g loaf`, `4 servings × ~350 g`.
- Measure the finished yield on the confirm round and write the actual figure. A yield copied from the recipe you adapted is the most common lie in published recipes, and it breaks every reader's scaling, costing and shopping.
- State the serving assumption when it is arguable: "4 as a main, 6 as a starter".

## Attribution and Adaptation

- "Adapted from X" is required when the ratio and the method came from a specific source; it is honest and it is also what protects you. A list of ingredients is generally not protectable, but the written expression is (`capture.md`).
- Adaptation means you changed something that matters and tested it. Retyping someone's recipe with metric conversions is not adaptation.
- A family recipe published outside the family gets the family's permission and the provenance line (`preservation.md`).
- Keep your test notes where the rounds already live — each round dated in the recipe's `## Variations`, its verdict in `~/Clawic/data/recipe/made/<year>.md`. When a reader reports a failure, those notes are the only way to tell whether it is their kitchen or your recipe.

## Collections and Cookbooks

- Declare the conventions once, at the front, and hold them everywhere: which cup, which egg size, which salt, conventional or fan, weight or volume first. A cookbook whose conventions drift between chapters generates a support burden per reader.
- Order by how people cook, not by how you developed them.
- Cross-reference components (a stock, a dough, a sauce) to one canonical recipe rather than repeating them — and give each component recipe a yield that the recipes calling for it actually use.
- Budget for the boring pages: an index by main ingredient, and a page of the substitutions you tested. Those are the pages people photograph.

**Write throughout an authoring project**: the recipe under development lives in `~/Clawic/data/recipe/recipes/<kebab-title>.md` like any other, with each test round as a dated entry in `## Variations` and the round's verdict in `made/<year>.md` — that log *is* the development record. The draft of a collection, a style-conventions page, or a print layout is a long text read whole and goes to `~/Clawic/data/recipe/artifacts/<kebab-name>.md` with its `## Boxes` line in the same turn. If the cookbook is tracked as a project, its one-line status also goes to the shared `~/Clawic/data/projects/<project>.md`, with the draft staying here (`memory-template.md`).
