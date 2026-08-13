# Common Pitfalls in Design Token Extraction

These are the five most common mistakes when extracting design tokens from existing UI. Understanding them saves more time than any extraction technique.

---

## Pitfall 1: Treating Frequency as Design Intent

**The mistake:** Counting occurrences — "this value appears 47 times, it must be a token."

**Why it's wrong:**
- A value appearing 50 times may just be early copy-paste code replicated across the codebase
- A value appearing once (e.g., brand title font, maximum page width, top-layer modal shadow) may be the most important design decision in the entire system
- Frequency indicates "where to look," not "what matters"

**The fix:**
For each candidate value, ask:
1. Does it express a stable design role (not an accident of history)?
2. Would changing it break the design coherence?
3. Should it change together with other instances?
4. Does it need to vary by theme?

A value that scores yes on 1-2 of these is a strong candidate. A value that scores yes on all four is a mandatory token.

---

## Pitfall 2: Force-Merging Near-Duplicates

**The mistake:** Seeing 15px, 16px, 17px and averaging them to 16px to get a "clean 4px scale."

**Why it's wrong:**
- 15px may be a button height constrained by the font's x-height
- 16px may be a text size set by the design system's base unit
- 17px may be a table row height with a 1px border compensation
- Differences from font metrics, component sizing constraints, responsive scaling, or intentional optical adjustments are NOT drift — they serve a purpose

**The fix:**
1. List all "near-duplicate" values with their locations
2. For each, determine whether the difference is intentional (font metrics, component identity, responsive) or accidental (copy-paste drift)
3. Only merge values confirmed to be accidental drift
4. For intentional differences, either keep separate tokens OR document as a known exception
5. Never let "looks nicer on a 4px grid" override functional intent

---

## Pitfall 3: Skipping Browser Rendering

**The mistake:** Running a global regex search for hex codes and pixel values, cataloging everything found in source files.

**Why it's wrong:**
- CSS specificity can override values declared in theme files
- Theme scopes (`.dark`, `[data-brand="x"]`) can remap variables at runtime
- Third-party component libraries may inject their own styles that override yours
- Media queries can change values at different viewports
- Some CSS variables may reference other variables that resolve differently at runtime
- Deprecated code may still exist in files but has no effect

**The fix:**
If the project can run:
1. Open key pages in a browser
2. Inspect actual computed styles on real elements
3. Check `getComputedStyle()` for final resolved values
4. Note which theme variables are actually being consumed
5. Flag values that exist in source but are overridden at runtime

If the project cannot run:
1. Flag ALL values as grade I (inferred) or A (assumed)
2. Document that browser verification was not possible
3. Recommend the user spot-check a few values in their browser

---

## Pitfall 4: Renaming Without Aliasing

**The mistake:** Replacing `#165DFF` with `--color-blue-500` and calling it done.

**Why it's wrong:**
- This is a rename, not a token extraction. The real value is not "blue-500" — it's "this is the color that means primary action."
- If the brand color changes from blue to purple next year, every component referencing `--color-blue-500` by name is now semantically wrong
- The name `color-blue-500` tells you only the current value, not what design decision it represents

**The fix:**
1. Primitive tokens get descriptive names: `color.blue.500`
2. Semantic tokens get role-based names: `color.action.primary`
3. Components reference semantic tokens, not primitives
4. When the brand color changes, only the semantic→primitive mapping changes — component code stays untouched

**The alias relationship is the core value of token extraction.** Without it, you've just created a CSS variable dictionary. With it, you've created a design system.

---

## Pitfall 5: Mass-Replacing the Entire Codebase

**The mistake:** Generating tokens, then doing a find-and-replace across all files.

**Why it's wrong:**
- You can't verify all states (hover, focus, active, disabled, loading, error, empty) at once
- Naming disagreements surface as you replace — you'll find yourself arguing about whether a gray is "secondary" or "tertiary" while 47 new bugs appear
- Some values are genuinely local and should NOT have been turned into tokens
- Visual changes, naming debates, and historical exceptions all blend into one unmanageable diff

**The fix:**
1. Pick ONE representative page or component group
2. Migrate it to tokens and verify ALL states (at least: default, hover, focus, active, disabled, empty, error, loading)
3. Run visual regression — screenshot before and after
4. If the page is stable, expand to the next batch
5. Keep old variable → new token mappings so you can trace back any breakage
6. Stop at any sign of unexpected visual change and investigate before continuing

**Schedule:**
- Batch 1: One representative page (proves the tokens work)
- Batch 2: Foundation components (buttons, inputs, cards, navigation)
- Batch 3: Remaining pages
- Batch 4: Special cases and intentionally local exceptions

---

## Quick Self-Check Before Finalizing

Ask these five questions before presenting extraction results:

| # | Question | If No... |
|---|----------|----------|
| 1 | Are same-value tokens with different semantics separated? | You'll break theme switching |
| 2 | Do semantic tokens reference primitives (not copy values)? | You've just renamed, not tokenized |
| 3 | Are all assumed values (grade A) explicitly flagged? | You're presenting guesses as facts |
| 4 | Could a new developer build a page using only semantic tokens? | Your semantic layer is incomplete |
| 5 | Would theme switching change the right things and leave the rest alone? | Your semantic mappings are wrong |

If you can't answer yes to all five, go back and fix the extraction before packaging.
