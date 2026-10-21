# Library — Search, Tags, Duplicates, and Pruning

The index is the collection; `recipes/` is only storage. Every question about what exists is answered from `~/Clawic/data/recipe/index.md`, never by listing the folder — a directory listing gives filenames, and filenames cannot answer "vegetarian, under 30 minutes, uses up the yoghurt".

**Read `index.md` before every search, suggestion, save, or retirement.** Its shape, columns and scale cut are in `memory-template.md`.

## Answering "What Can I Make?"

The question is never really about the whole collection. Resolve it in this order:

1. **Constraint first**: time available, people, and any restriction from `~/Clawic/data/health/profile.md` plus `diet` in `config.yaml`.
2. **Filter the index** on those, then on the ingredient if one was named.
3. **Rank by `Made`, descending**, then by `Rating`. A recipe cooked seven times is a better suggestion than an unmade 5-star, because the rating of an unmade recipe is the source's opinion, not theirs.
4. **Offer three, not thirty**: one they cook often, one they rated well but have not made recently, and one never-made recipe that fits — that last slot is what stops the collection ossifying into six dishes.
5. If nothing fits, say what the gap is ("nothing under 30 minutes without dairy") — that sentence is what `## Collection` in `memory.md` records as a gap worth filling.

## Search Patterns

| Query | How to answer it |
|---|---|
| "Recipes with chickpeas" | Index tags first, then grep the ingredient lines of the recipe files — the index cannot hold every ingredient |
| "Something quick" | `Total min` ≤ the weeknight ceiling in `## Household`, default 35 |
| "What uses up the yoghurt?" | Ingredient search, then rank by how much of it the recipe uses — a recipe using 200 g beats one using a spoonful |
| "Something like the tikka but not Indian" | Match on technique and texture tags, not cuisine |
| "What did we eat last month?" | `made/<year>.md`, not the index |
| "What have we never made?" | `Made = 0` rows; this is the query that drives the quarterly review |
| Anything else | Filter the index on the closest columns, say what you filtered on, and offer to add a tag if the query has no column |

## Tag Vocabulary

Tags are a controlled vocabulary or they are noise. Five axes, and no sixth without a reason recorded in `## Collection`:

- **course** — starter, main, side, dessert, breakfast, snack, sauce, basic
- **cuisine** — one word, the tradition the dish belongs to
- **effort** — `weeknight` (≤35 min active), `weekend`, `project` (multi-day or >2 h active)
- **season** — spring, summer, autumn, winter; only when the dish genuinely depends on it
- **diet** — vegan, vegetarian, gluten-free, dairy-free, and the allergens present

Rules: reuse before inventing — check the tags already in `index.md` first. Singular, lowercase, kebab-cased. A tag used once is a note, not a tag; fold it into `## Notes` of the recipe. `freezer`, `make-ahead`, `one-pan`, `uses-leftovers` earn their place because they are how people actually search under pressure.

## Duplicates

Check before every save (`capture.md`). Three cases:

| Case | Action |
|---|---|
| Same dish, same source, already saved | Do not save. Update the existing file if the source has changed since capture |
| Same dish, different source | Merge into the existing file: add the second source under `## Original`, put the differing quantities in `## Variations`. One file, one index row, one make count |
| Similar dish, genuinely different | Two files, two distinct names, and a line in each `## Notes` pointing at the other |

Splitting a dish across two files is the expensive mistake: the make count, the rating and the fixes divide between them, and neither file is ever the good one.

## Pruning

A collection is judged by what it does not contain. On the `never_made_review` cadence (`## Due`):

1. Pull every row with `Made = 0`, oldest capture first.
2. For each: schedule it into a week (`planning.md`), or retire it.
3. Retire by moving the row to `## Retired` in `index.md` with the date and a one-line reason. Keep the file unless the user says otherwise — a retired recipe that is re-encountered next year is instantly recognisable, which is the whole point of the reason line.
4. Also retire: anything rated 1, anything with two logged failures traced to the recipe, and anything whose required equipment the user no longer owns.

The healthy shape is roughly a third cooked repeatedly, a third cooked once, a third waiting. When the waiting third passes half the collection, capture is outrunning cooking and the review cadence should shorten.

## Keeping the Index Honest

- Every recipe file has exactly one index row; every index row points at a file that exists. A row without a file is the worse failure — it makes the whole index untrustworthy.
- Any frontmatter field that also appears as a column is updated in both places in the same turn (`format.md`).
- The header line carries the counts (`84 recipes, 31 never made`) and is refreshed whenever a row is added or retired. That single line is the answer to most "how is the collection doing" questions.
- Past ~150 rows, split along `index_grouping` into `index-<group>.md`; `recipes/` stays flat forever (`memory-template.md`).

**Write after any library operation**: the index row for a save, a merge, a rating change or a retirement, in the same turn as the change. A gap the collection keeps hitting, a tag vocabulary decision, or a shift in what they actually cook goes as one line into `## Collection` of `~/Clawic/data/recipe/memory.md`, and a completed review updates its row in `## Due` (`memory-template.md`).
