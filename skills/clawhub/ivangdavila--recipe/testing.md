# Testing — Cooking It, Recording It, Promoting What Works

A collection becomes a repertoire only through this file. The make log is what separates recipes that work from recipes that were saved.

**Read `~/Clawic/data/recipe/made/<year>.md` before rating anything, before promoting a variation, and before answering "what should we cook".** Three rows about the same dish say more than any rating, and a change that already failed once should not be proposed again.

## The Make-Log Row

Written after the meal, not during. Columns and the file's shape are in `memory-template.md`.

- `Date`, `Recipe`, `For` (people by name; the person lives in the shared contacts box), `Scale`, `Rating` 1-5, `What changed`, `Fix next time`.
- **`Fix next time` is the field that makes the row worth writing.** A row without it is a diary entry. If nothing needs fixing, write `nothing — as written`, which is itself a strong signal.
- Log the failures. A log of successes cannot answer "why did we stop making this", and the second failure of the same dish is what triggers a retirement (`library.md`).
- One row per cook, including repeats of the same recipe. The repeats are the data.

## Rating That Survives Six Months

| Rating | Means |
|---|---|
| 5 | Cook again as written, would serve to guests |
| 4 | Cook again with the recorded fix |
| 3 | Fine; there is a better version of this dish somewhere |
| 2 | Something is wrong with the recipe, not the cook — vet it (`vetting.md`) |
| 1 | Retire it |

Rate the recipe, not the evening. A dish rated 2 because the cook was rushed teaches nothing next year. If the failure was execution, write that in `What changed` and leave the rating from the last good cook.

## Promotion — When a Change Becomes the Recipe

The rule: **two cooks, same change, same verdict → promote.**

1. First cook with the change: the change lives in `## Variations`, dated, marked `untested`.
2. Second cook with the change, verdict holds: move it into `## Ingredients` or `## Method`, and move the *previous* line into `## Variations` labelled `superseded <date>`.
3. The old version is never deleted. The day the promoted version disappoints, the only way back is that line.
4. Update `rating`, `made`, `last_made` in the recipe frontmatter and the matching cells in `index.md`, in the same turn.

One cook is not enough because a single good result confounds the change with everything else that varied that night: the pan, the heat, the ingredient batch, the hunger. Two cooks with the change and one without is the cheapest experiment a kitchen can run.

## Testing Deliberately

When the user wants to *find* the right version rather than stumble into it:

- **Change one variable per cook.** Two changes and a better result teaches nothing about which one mattered.
- **Order the variables by leverage**: salt level, then cooking time or temperature, then fat, then the fiddly aromatics. Most dishes are fixed by the first two.
- **Split the batch where the recipe allows it** — two trays, two pans, half the dough — and taste them side by side. Sequential tasting a week apart is unreliable; simultaneous tasting is not.
- **Write the hypothesis before cooking**: "less cream will taste more tomato-forward". Recording the prediction is what stops the result being rationalised afterwards.
- **Blind the taster where it is easy.** Household opinion about a dish they know you changed is not evidence.
- Three to five cooks is the realistic ceiling for a home test. Past that, the variation between batches of the same ingredients exceeds the effect being chased.

## Diagnosing From the Log

| Pattern in the log | Reading |
|---|---|
| Same recipe, several 4s, always the same fix | The fix is the recipe. Promote it and stop rewriting it every time |
| Rating drops over successive cooks | Something drifted — an ingredient brand, the oven, the scale factor. Check `## Kitchen` |
| High rating, never cooked again | Effort exceeded the payoff. Tag it `project` so it stops appearing in weeknight suggestions |
| Two failures traced to the written recipe | The source is the problem, not the dish. Update `## Sources` and find the dish elsewhere (`vetting.md`) |
| Long gaps between cooks of everything | The collection is not matched to how they actually eat; check the effort tags and the weeknight ceiling in `## Household` |

## Failure Triage, Fast

Before assuming the recipe is wrong: was the oven verified against the measured offset in `## Kitchen`, was the salt the brand the recipe assumes, was the tin the size it specifies, and was it scaled? Those four account for most "the recipe is bad" verdicts. Stove-side diagnosis of a dish that went wrong — split sauce, tough meat, flat bread — is `cooking`'s job; this file's job is to make sure the finding lands in the file.

**Write after every cook, in the same turn as the meal is discussed**: a row in `~/Clawic/data/recipe/made/<year>.md`; `made`, `last_made` and `rating` bumped in the recipe file and in its `index.md` row; and any change recorded in `## Variations` with `untested` or its verdict. A promotion edits `## Ingredients`/`## Method` and demotes the old line to `## Variations` as `superseded`. Formats: `memory-template.md`.
