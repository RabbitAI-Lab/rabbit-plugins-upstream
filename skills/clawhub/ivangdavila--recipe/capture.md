# Capture — Getting a Recipe In From Anywhere

The job is always the same: extract yield, ingredients with quantities, method with cues, times and temperatures, and the source — then write one file and one index row. Everything else is optional.

**Before saving, read `~/Clawic/data/recipe/index.md`** and check for the same dish under another name or from another source. A duplicate saved as a second file splits the make count, the ratings, and the variations across two files that then diverge (`library.md`).

## Source Ladder — What Each One Gives You

| Source | What you get | What is missing, and how to fill it |
|---|---|---|
| Recipe site with structured data | Everything, cleanly — most food sites publish schema.org `Recipe` JSON-LD in the page head | Salt brand, tin size, whether the temperature is fan. Ask nothing; record the gap in `## Original` |
| Recipe site without it | Prose plus a printable card | The card is usually the accurate one; the prose sometimes carries the technique note |
| Screenshot or photo of a screen | The text | Anything below the fold. If the ingredient list is cut, say so rather than inferring |
| Photo of a cookbook page | Text plus the book's conventions | Which cup, which egg size, whether the oven is fan — the front matter of a cookbook states these once and applies them everywhere. Record the book's convention, not just the page |
| Handwritten card | The original, and the family's own units | Method steps are usually compressed or absent (`preservation.md`) |
| Video | Ingredients on screen, technique in the demonstration | Exact quantities and yield are often never stated. Capture what is shown, mark the rest `unstated` |
| Dictation or memory | What they actually do | Quantities ("a good glug"). Convert to a range with a unit, and keep their phrase in `## Original` |
| An app export file | Everything, in that app's field names | Field mapping and duplicate handling (`migration.md`) |

## Extraction Order

1. **Yield first.** Every other number depends on it. If the source gives no yield, derive one from the protein or the tin ("serves 4" from 700 g of thigh) and mark it `derived`.
2. **Ingredients in method order**, not in shelf order, and grouped by component when the method uses them separately ("Marinade", "Sauce").
3. **Quantities with their unit**, verbatim, into `## Original`. Convert into the user's `units` for `## Ingredients` (`conversion.md`).
4. **Method as one action per step**, each with the cue that ends it. A step with a time but no cue ("cook 8 minutes") gets the cue added if the source states it anywhere; if it does not, that is a vetting finding, not something to invent.
5. **Times and temperatures** with the oven type. A source that does not say gets `conventional, unstated by source`.
6. **Source line**: URL plus capture date, or book plus edition and page, or person plus year (Rule 7).
7. **Tags** from the vocabulary already in use in `index.md` — never a new tag when an existing one fits (`library.md`).

## What To Drop and What To Keep

- Drop: the childhood story, the SEO paragraph, the "why you'll love this" list, nutrition estimates from an automated calculator, affiliate equipment lists, the comment section.
- Keep, always: any sentence that changes what you do — "do not stir after this point", "the dough should be tacky, not sticky", "this fails with pre-ground spice". These are usually in the prose, never in the card, and they are the reason the recipe works.
- Keep, condensed: a warning about a step that commonly fails, and any make-ahead or freezing note.
- One recipe per file, even when the source publishes three variations of it. The variations go in `## Variations` of the one file (`format.md`).

## Reading Structured Data

Sites that publish schema.org `Recipe` give you `recipeYield`, `recipeIngredient[]`, `recipeInstructions[]`, `prepTime`/`cookTime`/`totalTime` as ISO-8601 durations (`PT1H15M` = 75 min), `recipeCategory`, `recipeCuisine`, and `aggregateRating`. Map them straight into the frontmatter (`format.md`). Two traps: `recipeYield` is often a bare number with no unit — decide whether it means servings or pieces from the method, and write which; and `recipeInstructions` is sometimes one blob rather than a list, which has to be split into steps by hand.

## Paywalls, Copyright, and Attribution

- A recipe's *list of ingredients* is not protected in most jurisdictions; the *written expression* — headnotes, step prose, photographs — is. For a personal collection this rarely matters; for anything shared or published it does (`authoring.md`).
- Practical line: store the recipe in your own words with the source credited. Store a verbatim copy only for a family original or a book you own, and keep it in `## Original` where it is clearly marked as someone else's text.
- Never log in, bypass a paywall, or store site credentials to fetch a recipe. If a page is paywalled, ask the user to paste the text.
- Attribution outlives the link. A URL alone is worthless when the site is gone: keep the site name, the author if given, the recipe title as published, and the capture date.

## Ambiguity Handling

| The source says | Write |
|---|---|
| "salt to taste" | Leave it, and add a starting quantity in grams as a bracketed suggestion |
| "1 tbsp salt" with no brand | Convert at the user's salt from `## Kitchen`, and note the assumption in `## Original` |
| "1 medium onion" | Grams with the count in parentheses: `170 g onion (1 medium)` |
| "a can of tomatoes" | The gram weight, with the tin size as published: `400 g tinned tomato (1 × 400 g tin)` |
| "cook until done" | Keep the phrase, add the internal temperature or the observable cue from the dish type; mark it `added` |
| "350 °F" with no oven type | Convert, and append `(conventional, unstated by source)` |
| A quantity that is obviously wrong | Do not silently fix it. Capture it, then run `vetting.md` and record the finding in `## Notes` |

## Batch Capture

When the user drops five links or a folder of photos at once: extract all of them, then write all of them, then write the index rows in one pass — and report a single line of what landed and what was skipped. Stop and ask only if two of them are the same dish, which is the one decision the user has to make (merge or keep both).

**Write at the end of every capture**: the recipe file at `~/Clawic/data/recipe/recipes/<kebab-title>.md` **and** its row in `~/Clawic/data/recipe/index.md`, in the same turn (SKILL.md Rule 1 and 9). If the capture revealed a source worth trusting or distrusting, add its row to `## Sources` in `~/Clawic/data/recipe/memory.md`. Formats and thresholds: `memory-template.md`.
