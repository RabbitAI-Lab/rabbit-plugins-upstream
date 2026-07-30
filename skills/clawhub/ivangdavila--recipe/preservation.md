# Preservation — Family Recipes, Handwriting, and Cooks Who Never Wrote Anything Down

The failure mode here is not losing the recipe; it is *improving* it into something nobody recognises. Preserve the artifact, then build the cookable version beside it. Both survive.

## Order of Operations

1. **Capture the original as an image first**, before any transcription. Flat, even light, the whole card including the stains and the marginalia — the pencilled "add more butter" in someone else's hand is part of the record.
2. **Store the image beside the recipe file** with the same stem: `recipes/grandma-rosa-sunday-sauce.jpg` next to `recipes/grandma-rosa-sunday-sauce.md`, linked from `## Original`.
3. **Transcribe verbatim into `## Original`**, including the odd measures, the misspellings, and the missing steps. This section is never edited afterwards (SKILL.md Rule 2).
4. **Record the provenance line**: who, from whom before them, roughly when, and where they cooked it. "Grandma Rosa, from her mother, Puglia, circa 1955" is the part that cannot be reconstructed later.
5. **Then** build `## Ingredients` and `## Method` as the tested modern version, and log the cooks that got you there (`testing.md`).

## Decoding Old Measures

| Written | Usually means | How to pin it down |
|---|---|---|
| "A coffee cup of flour" | 150-200 ml, and it means *that* cup | Find the cup if it still exists and measure it; otherwise assume 175 ml and mark it derived |
| "A teacup" | ~200-240 ml | Same |
| "A glass" | 200-250 ml, often of wine or water in that kitchen | Same |
| "A knob of butter" | 15-25 g | Cook it and settle on the figure that works, then record it as derived |
| "A pinch" / "as much as you can hold" | 0.3-0.5 g for a pinch; a three-finger pinch ~1 g | Weigh your own pinch once |
| "Enough flour to make a soft dough" | A hydration, not a mass | Work backwards: fix the liquid, add flour to the described texture, weigh the total, convert to baker's percentage (`scaling.md`) |
| "A moderate oven" | 180 °C / 350 °F conventional | "Slow" ≈ 150, "hot" ≈ 220, "very hot" ≈ 240 |
| "Gas mark 4" | 180 °C | Full table in `conversion.md` |
| "1 lb" in a pre-metric British recipe | 453.6 g | But a pint is 568 ml, not 473 |
| "Butter the size of an egg" | ~50-55 g | — |
| "Cook until done" | The cook knew; the card does not | Reconstruct from the dish type and record the internal temperature you settled on, marked `added` |

The general method for any unmeasurable instruction: fix everything you *can* measure, cook it, adjust the unknown until it matches the remembered result, then write the number down as `derived <date>`.

## Interviewing a Cook Who Works By Eye

- **Cook it with them, and weigh as they go.** Ask for permission to put a bowl on a scale; do not interrupt the flow with questions. This produces a better record in one afternoon than a year of asking.
- If cooking together is impossible: ask them to walk through it while you write, then read it back as instructions and let them correct you. People cannot list ingredients accurately but they can always spot a wrong step.
- **Ask about the failures**, not the successes: "what goes wrong when it doesn't work?" gets you the cue, the temperature and the timing that the recipe depends on. It is the highest-yield question in the interview.
- **Ask what changed over the years** — the recipe as cooked in 2026 is often not the one from 1955, and both are worth recording.
- Record the audio if they agree. Transcribe the numbers; keep the phrasing in `## Original`.
- Ask early. This work has a deadline nobody sets.

## Ingredients That No Longer Exist

Old recipes assume old products. When the modern version fails, suspect these before the method:

- **Flour**: protein content has drifted and varies by country. A 1950s British "plain flour" is not today's; if a dough is slack, the flour is the first suspect.
- **Eggs** are larger now. "3 eggs" in an old cake may be closer to 2½ modern large ones — weigh (`scaling.md`).
- **Cream and milk** fat percentages are standardised differently by country and era; "double cream" has no US equivalent at the same fat level.
- **Yeast**: fresh yeast was the default; instant needs a third of the weight (`substitutions.md`).
- **Tinned tomatoes, stock cubes and shortening** have all changed in salt and water content. Taste before salting an old recipe to its written amount.
- **Local varieties** — a specific tomato, a regional cheese, a wheat that is no longer grown. Name what it was, name your substitute, and mark the version `adapted`.

## What Not To Do

- Do not clean up the original text. The misspelling and the crossed-out line are evidence.
- Do not merge two family versions into one "correct" file. Two files, two names, each with its provenance, and a note in each pointing at the other — the disagreement between them is the family history.
- Do not discard the physical card after digitising. Photograph it and say so; whether the paper is kept is the family's decision, not a filing decision.
- Do not publish a family recipe outside the family without asking (`authoring.md`).

## The Family Cookbook

When the goal is a book rather than a collection: gather first, cook second, write third. Choose recipes by who is still around to explain them, not by which sound best. Every recipe gets its provenance line and, where it exists, the scan of the original facing the tested version — that pairing is what makes the book worth having rather than another recipe file.

**Write as the preservation happens**: the recipe file at `~/Clawic/data/recipe/recipes/<kebab-title>.md` with `## Original` verbatim, the provenance line, and the image stored beside it with the same stem; the index row in the same turn. Each derived measure is written back into `## Original` as `derived <date>`, never over the source's own words. A cookbook draft, a scan inventory, or an interview transcript is a long text read whole and goes to `~/Clawic/data/recipe/artifacts/<kebab-name>.md` with its `## Boxes` line. The relative the recipe came from goes in `~/Clawic/data/contacts/contacts.md` — name, key and one line of context — and is referenced here by name only (`memory-template.md`).
