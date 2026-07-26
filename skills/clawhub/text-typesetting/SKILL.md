---
name: text-typesetting
description: Use when setting or reviewing line-height, letter-spacing (tracking), and vertical-trim/leading-trim for a text style — computing the geometric relationship between font size and these values for body text, headings, UI labels, or captions.
triggers:
  use_when:
    - user asks to configure a text style or type token
    - user asks "what line-height should this be"
    - user asks to compute tracking / letter-spacing
    - user is setting up h1-h6 / body / label / caption text styles
    - agent has Figma access and user asks to fix/inspect a selected text layer's spacing
  do_not_use_for:
    - generating a full type scale across sizes (see type-scale-generator)
    - vertical rhythm between blocks/components (see vertical-spacing)
    - column width / measure (see line-length-optimizer)
metadata:
  author: Monika Zapisek
  project: Design Engineering Playbook
  version: 1.0
  status: accepted
---

# Text Typesetting

## Purpose

Compute a coherent `line-height` and `letter-spacing` for a given `font-size` and text role, and correctly account for vertical-trim (CSS `leading-trim` / Figma `textLeadingTrim`) when it changes what "line-height" visually means.

## When To Use

- Setting up a new text style/token (body, heading, label, caption).
- Reviewing an existing style where line-height or tracking look off.
- Inspecting a selected Figma text layer and proposing corrected values.
- Not for generating an entire scale of sizes at once, and not for spacing *between* elements (that's vertical rhythm, a different skill).

## Inputs

- `font-size` (px or rem).
- `font-family-category`: sans-serif / serif / display / monospace (serifs generally need more line-height breathing room than sans at the same size).
- `text-role`: body / heading / UI label / caption.
- `text-case`: original (sentence/title case) or uppercase/small-caps — this is the primary driver of letter-spacing direction, see Workflow step 2.
- `x-height`: high / low, if known for the specific typeface (see Workflow step 2b) — optional refinement, not required to produce a baseline recommendation.
- `font-weight`: numeric (100–900) if known — scales the tracking magnitude from step 2/2b, see Workflow step 2c.
- `variable-font-axes`: if the font is variable, the actual `wght` value and whether an `opsz` (optical size) axis exists and is bound to size — see Workflow step 2d.
- If available: `textLeadingTrim` / vertical-trim state (see Figma Node Integration) — this changes the recommended line-height, not just its visual effect.

## Outputs

- `line-height` value (unitless ratio preferred for body text, so it scales with font-size).
- `letter-spacing` value (in `em`, since tracking should scale with font-size, not be a fixed px).
- CSS/token snippet, plus a one-line rationale per value.

## Workflow

1. **Base line-height by role and family:**
   - Body text: `1.4`–`1.65`. Serif → upper half of range (more breathing room); sans-serif → lower half.
   - Headings: tighter, `1.1`–`1.3` — large text needs proportionally less line-height.
   - UI labels / captions: `1.2`–`1.4`, biased by legibility needs at small size rather than by family.

1b. **Measure compensation ("Typography Triangle") — only when the column is wider than ideal:** if `line-length-optimizer` reports (or the input states) a measure wider than the ~65-character ideal — the eye has more trouble tracking back to the start of the next line the wider the column gets — compensate by *increasing* line-height beyond the step-1 base:

   ```
   LH_new = LH_base + ((characters_per_line − 65) / 100) × 0.1
   ```

   E.g. at 85 characters per line, line-height grows from `1.5` to `1.7`. Only apply this when measure is confirmed wider than ~65–75 characters (i.e. already outside `line-length-optimizer`'s comfortable range) — don't apply a correction for a column that's merely at the high end of normal. This is a compensation for a business constraint that's forcing an over-wide container, not a substitute for fixing the width via `line-length-optimizer` when that's actually available.

2. **Letter-spacing (tracking) — driven first by case, then by size.** `text-case` is the primary branch — check it before applying any size-based rule:

   **Branch A — uppercase or small-caps** (`textCase: UPPERCASE` / `SMALL_CAPS`, or CSS `text-transform: uppercase`): default font spacing is tuned for mixed-case letterforms, which lose their shape variety when flattened to all-caps — the eye can't recognize word-shapes anymore, only a dense block of equal-height letters. Always add positive tracking, scaled inversely with size (small caps text needs proportionally more room than large):
   - `font-size ≤ 12px` → `letter-spacing: +10%` (`+0.10em`)
   - `12px < font-size ≤ 18px` → `letter-spacing: +6%` (`+0.06em`)
   - `font-size > 18px` → `letter-spacing: +2%` (`+0.02em`)

   **Branch B — sentence/title case** (`textCase: ORIGINAL`): lowercase letters carry their own internal/external counters that already aid legibility — no tracking adjustment needed at body/reading sizes. Only tighten at larger sizes, where letter-spacing optically opens up and headings start to look "broken apart":
   - `font-size < 24px` → `letter-spacing: 0` (`normal`) — don't touch it.
   - `24px ≤ font-size < 36px`, sans-serif → `letter-spacing: -1.5%` (`-0.015em`).
   - `font-size ≥ 36px`, sans-serif → `letter-spacing: -2%` (`-0.02em`).
   - Serif/display faces: apply roughly half the sans-serif tightening — serifs already have less open counters, so the same negative value over-tightens.

2b. **x-height refinement (optional, only if the specific typeface's x-height is known):**
   - **High x-height** (e.g. Inter, Roboto, San Francisco — most UI-oriented sans faces): open, wide counters at small sizes aid legibility, but the letters occupy more vertical space and tolerate — sometimes need — very slightly looser tracking at small sizes to avoid letters visually merging. Bias toward the upper end of the Branch A/B ranges above.
   - **Low x-height** (classic serif and elegant display faces, e.g. Georgia-style proportions): small letters are compact relative to cap-height, leaving more natural vertical air already. Keep tracking closer to zero — loosening it further makes low-x-height letters visually drift apart and the word loses cohesion. Bias toward the lower end of the ranges above, or don't adjust at all if already near zero.
   - If x-height is unknown, skip this refinement — the Branch A/B base values are safe defaults without it.

2c. **Font-weight modifier (apply after Branch A/B + x-height, as a final scaling pass on whatever tracking value step 2/2b produced):**
   - Heavier weights (Bold/700, Black/900) carry thicker strokes, which already reduce the white space inside and between letters — the same *numeric* tracking value reads as looser on a Black weight than on a Regular weight, because there's less counter-space for the extra room to sit in. Reduce the computed tracking magnitude (keep the sign from Branch A/B, scale the number down):
     - Weight ≥ 700 (Bold/Black/Heavy): multiply the Branch A/B result by roughly `×0.7`.
     - Weight ≤ 300 (Light/Thin): multiply by roughly `×1.15` — thin strokes leave more open counters already, and default spacing can look slightly cramped without a small boost.
     - Weight 400–500 (Regular/Medium): no modifier, use the Branch A/B value as-is.
   - This applies in both branches: an uppercase Black-weight label still gets positive tracking (Branch A), just proportionally less than the same label in Regular weight.
   - If weight is unknown, skip this modifier — Branch A/B values already assume Regular/Medium as the default case.

2d. **Variable fonts — read the actual axis value, don't assume a named instance:**
   - A variable font's weight is a continuous value (e.g. `wght: 550`), not a fixed Regular/Bold step. Apply the font-weight modifier (step 2c) by interpolating between the anchor points (400→×1, 700→×0.7, 300→×1.15) rather than snapping to the nearest named instance — a `wght: 550` gets a modifier roughly halfway between ×1 and ×0.7.
   - If the font exposes an **optical size axis** (`opsz`), check it before manually adjusting tracking at all: `opsz` is specifically designed to auto-adjust spacing, stroke contrast, and x-height proportions for the rendering size, which is much of what steps 2/2b/2c are compensating for manually. When `opsz` is bound to `font-size` (CSS `font-optical-sizing: auto` — the default in modern browsers — or the Figma equivalent), treat the manual tracking correction as a smaller supplementary nudge, not the full computed value, and say so in the output rather than silently stacking both corrections.
   - If no variation axis data is available (static font, or Figma reports only a named instance), fall back to the discrete Regular/Bold treatment in steps 2c and don't guess at intermediate values.

3. **Vertical-trim / leading-trim guard (critical — check before finalizing line-height):**
   - Default behavior (trim off): the font's built-in leading (space above cap-height and below baseline) is included in the line box. The `line-height` values above assume this default.
   - If vertical-trim / `leading-trim` is **on** (CSS `leading-trim: both` / `text-box-trim`, or Figma `textLeadingTrim: CAP_HEIGHT` or equivalent): the line box is cropped to cap-height/baseline, removing the font's built-in air. In this state, the same numeric `line-height` reads as visually tighter — recompute upward (roughly +10–15%) if trim is on and the target visual density should stay the same as the untrimmed baseline. State explicitly whether the recommended value assumes trim on or off — never hand over a bare number without saying which.
   - If unknown (plain CSS with no Figma/plugin context, no way to check), state the assumption ("assuming default leading, trim off") rather than silently picking one.
   - **Property name:** this skill uses `textNode.textLeadingTrim` (values `"CAP_HEIGHT"` / `"NONE"`), matching current Figma Plugin API. The shorter `leadingTrim` is a colloquial/CSS-adjacent shorthand (CSS itself uses `leading-trim`) — not the actual Figma API property name. Use `textLeadingTrim` when writing to a node.

4. **OpenType number styles — pick by content role, not by default.** Digits aren't one glyph set; the font exposes up to four figure styles along two independent axes (form × spacing), and picking wrong is a common, avoidable error:

   | Content role | Figure form | Spacing | CSS | Figma `fontFeatures` |
   |---|---|---|---|---|
   | Running prose (articles, body copy) | Oldstyle (varying heights, ascenders/descenders — blends into lowercase text instead of forming bright "spikes") | Proportional | `font-variant-numeric: oldstyle-nums proportional-nums;` | `{ onum: 1 }` |
   | Headings / display / UI counters (prices, single stats, non-tabular labels) | Lining (uniform cap-height) | Proportional (natural rhythm — a `1` shouldn't occupy the same width as an `8`) | `font-variant-numeric: lining-nums proportional-nums;` | `{ lnum: 1 }` |
   | Tables, financial statements, any column of stacked numbers | Lining | Tabular (fixed-width per digit, so units/tens/hundreds columns align vertically) | `font-variant-numeric: lining-nums tabular-nums;` | `{ lnum: 1, tnum: 1 }` |

   - Default to the prose row for body text and the heading row for display/UI unless the user specifies otherwise — don't leave figures at the font's raw default, which is often lining+proportional regardless of role and will look wrong in a paragraph of running text.
   - **Kerning interacts differently per spacing mode** (ties into step 5): proportional figures (prose and heading rows) need `fontKerning: "METRIC"` active — pairs like `11` or `74` produce visible gaps without it. Tabular figures have kerning intentionally suppressed by the font itself to preserve fixed-width column alignment — **do not** force `fontKerning` changes on a tabular-figure node to "fix" spacing; that's the font working as designed, not a bug.
   - **Residual pair collisions in display headings:** even with `fontKerning: METRIC` active, a font with a sparse OpenType kerning table can still leave specific proportional-figure pairs too tight (`11` — the two vertical strokes nearly touch) or too loose (`74` — the diagonal and the crossbar leave a visible gap) at large display sizes, where the flaw becomes visible. If a display heading contains one of these known-risky pairs, apply a local `setRangeLetterSpacing` on just that pair, `±2%`, rather than adjusting the whole node's tracking. Don't apply this pre-emptively — only when the specific pair is present and the size is large enough to make it visible (roughly ≥32px).
   - **Currency and fractional amounts** (e.g. `99.90 zł`, `$4.99`): the cents/grosze portion is a common candidate for the OpenType `Numerator`/superscript feature (`sups` or a fraction feature `frac`) to visually subordinate it to the whole-number part, matching classic price-tag typesetting. Only apply when the content is genuinely a price/currency amount, not a generic decimal (`3.14`, a percentage) — those stay as plain lining figures. Also check the decimal separator (`.`/`,`) isn't visually colliding with a preceding `0` — a rare kerning gap in some fonts — and apply the same local range-tracking fix as above if it is.
   - Small caps (`font-variant: small-caps` / Figma `letterCase: SMALL_CAPS`) only when explicitly requested — it's a stylistic choice, not a default correction.

5. **Kerning/tracking integrity guard (hard rule, not a recommendation):**
   - **Kerning** (per-pair optical correction baked into the font's OpenType tables, e.g. `AV`, `Ta`, `We`) and **tracking**/`letter-spacing` (a uniform global offset applied to every letter) are complementary, not substitutes. Adjusting tracking in steps 2/2b/2c/2d must never disable or bypass the font's native kerning table.
   - CSS: leave `font-kerning: normal` (the default) — never set `font-kerning: none` as a side effect of a tracking change.
   - Figma: `textNode.fontKerning` should stay `"METRIC"` (or `"AUTO"` if that's the file's existing convention) whenever tracking is modified. Do **not** set it to `"NONE"` — that discards the type designer's kerning pairs entirely, which is almost never the actual intent even when a user asks for "tighter spacing." If a request sounds like it wants kerning disabled, confirm rather than assume, since it's a rare, usually-unwanted operation.
   - The larger the tracking value or font-size, the more visible a missing kerning table becomes (mismatched pairs stand out more at heading sizes) — so this guard matters most exactly where steps 2/2c apply the largest adjustments, not just as a blanket rule.
   - Report `fontKerning` state in the output whenever letter-spacing is changed, so a disabled kerning table isn't silently inherited from the node's prior state.

6. **Dash rendering in Figma (which character/spacing to use is `microtypography` Rule 1c — this step is only the rendering layer on top of that decision):**
   - Whenever a text node contains `-`, `–`, or `—`, `fontKerning` must be `"METRIC"`/`"AUTO"` (per step 5) so the font's OpenType pair tables can prevent collisions with adjacent outward-leaning letterforms (`V—`, `—A`, `1–9`) — this is the same guard as step 5, just called out explicitly because dash collisions are the most visible failure case.
   - **Display-size / all-caps em dash:** at large sizes or inside an all-caps run (Branch A from step 2), an unspaced em dash can visually crowd its neighbors even with correct kerning. Prefer a small *local* tracking nudge over inserting an actual space — a real space would reopen the "should this have spaces" question Rule 1c already answered, and would break word-count/line-wrap assumptions elsewhere. Apply `+3%` `setRangeLetterSpacing` across the em dash **and the single character immediately on each side of it**, not the dash alone — tracking just the dash glyph itself doesn't change its distance to its neighbors (letter-spacing is applied between characters, not as padding on one glyph), so the range must include at least one adjacent character per side to actually open the gap.
   - **Numeric ranges with en dash in display headings** (e.g. a large "1995–2026"): verify the digits aren't visually touching the dash's arms. If they are (common in cheaper fonts lacking digit-to-dash kerning pairs), apply the same local range-tracking nudge rather than falling back to a spaced dash, since a numeric range must stay unspaced per `microtypography` Rule 1c.
   - **Hyphen height in all-caps (`case`-sensitive forms):** a default hyphen is vertically centered for lowercase text; in an all-caps run it can visually hang too low relative to the capital letters. Check whether the font's OpenType `case` feature (case-sensitive forms — raises hyphens, dashes, parentheses, and similar punctuation to align with cap-height) is available and enable it (Figma `fontFeatures: { case: 1 }`) for all-caps/small-caps nodes rather than leaving the punctuation optically low. Skip if the font doesn't expose the feature — don't fake it with manual vertical offsets.

7. **Hanging punctuation in Figma (handles the case `microtypography` Rule 4 flags — this is the computation step, that skill only detects it):**
   - Trigger: a display heading (≥24px) whose first character is an opening quote (`„`, `"`, `«`) or, less commonly, a dash/parenthesis, where leaving it inside the block makes the following letter's left edge look indented relative to body copy below it.
   - Figma has no native global hanging-punctuation toggle, so simulate it: apply a negative `paragraphIndent` sized to the visual width of the leading punctuation mark. Starting formula: `Indent = -0.45 × fontSize` — a closer default than a flat `-0.5em`, since most quote glyphs (`„`, `"`, `«`) render narrower than a full em. Treat `0.45` as the typical case and adjust per-typeface if the font's specific quote glyph is notably wider or narrower; verify visually that the letter after the mark now aligns with the column edge, not the mark itself.
   - If a negative `paragraphIndent` isn't available or reliable for the node's configuration, the fallback is splitting the punctuation mark into its own text container positioned to overhang the block — more precise but heavier to set up; prefer the `paragraphIndent` approach first.
   - Only applies to the node(s) `microtypography` flagged — don't scan for this independently, since it's a display-heading-only concern and this skill isn't the one parsing body copy.

## Figma Node Integration

When running with Figma access:

- **Read:** `textNode.fontSize`, `textNode.lineHeight`, `textNode.letterSpacing`, `textNode.fontName.family`, `textNode.textLeadingTrim`, `textNode.textCase`, `textNode.fontWeight`, `textNode.fontKerning`.
- **Variable fonts:** if `textNode.fontName` resolves to a variable font instance, read the bound `wght` axis value via `textNode.boundVariables` / `textNode.fontVariations` (API surface depends on Figma version) instead of trusting only the named style string — a variable instance named "Regular" can still be bound to a custom `wght` like 435. Also check for an `opsz` axis per Workflow step 2d before stacking a manual tracking correction on top of it.
- **`textCase` check is the mandatory first branch for letter-spacing** (Workflow step 2): `UPPERCASE`/`SMALL_CAPS` → Branch A; `ORIGINAL` → Branch B. Read this before computing any tracking value — the two branches produce opposite-sign results, so skipping this check risks recommending negative tracking on all-caps text (actively harmful, not just suboptimal).
- **Vertical-trim check is mandatory first step for line-height:** always read `textLeadingTrim` before recommending a `line-height` value — see Workflow step 3. If it's off and the layer sits inside an Auto Layout frame with a tight `itemSpacing`, flag the interaction with `vertical-spacing` (optical gap will read smaller than the set gap value).
- **`fontKerning` guard (hard rule, see Workflow step 5):** whenever `letterSpacing` is written, read the current `fontKerning` value first and preserve it — write `letterSpacing` alone, never bundle in a `fontKerning: "NONE"` change. If the node already has `fontKerning: "NONE"` from a prior edit, flag it as likely unintentional rather than silently leaving or silently fixing it.
- **Action back to Figma:** if asked to apply the fix directly, set `lineHeight`, `letterSpacing`, and (if requested) `fontFeatures`/`letterCase` on the node via the plugin API. Report the values first; only write to the node when the user asks for a direct application, not as a silent default.
- **Hanging punctuation:** only computed when `microtypography` (or the user directly) flags an eligible display heading — see Workflow step 7. Apply `paragraphIndent` (or the split-container fallback) only on explicit request, same as every other direct Figma write in this skill.

## Quality Checklist

- [ ] Line-height and family/role pairing both stated with rationale, not just a bare number.
- [ ] `text-case` checked first; Branch A (uppercase/small-caps) always positive, Branch B (sentence/title case) only negative above 24px — never the reverse sign.
- [ ] Font-weight modifier applied after the base tracking value, not before (sign comes from Branch A/B, magnitude scaled by weight) — heavier weight scales tracking down, lighter weight scales it up.
- [ ] Variable font `wght` read as a continuous value and interpolated, not snapped to the nearest named instance; `opsz` axis checked before stacking a full manual correction on top of it.
- [ ] x-height refinement applied only when the specific typeface's x-height is actually known, not guessed.
- [ ] Vertical-trim state is explicitly checked (Figma) or explicitly assumed (plain CSS) — never silently ignored.
- [ ] `fontKerning` never set to `NONE` as a side effect of a tracking change; existing `NONE` state flagged, not silently kept or silently changed.
- [ ] Number-figure style (oldstyle/lining × proportional/tabular) matches content role per the Step 4 table — not left at font default.
- [ ] `fontKerning` never force-changed on tabular-figure nodes — suppressed kerning there is correct, not a bug.
- [ ] Dash rendering (step 6) only adjusts local range-tracking or `case` feature — never overrides the character/spacing choice already made by `microtypography` Rule 1c.
- [ ] Hanging-punctuation indent only computed for nodes actually flagged as eligible, verified visually rather than trusting the `-0.5em` starting estimate blindly.
- [ ] `case` OpenType feature checked (not assumed) before claiming a font can raise punctuation to cap-height; skipped cleanly if unsupported.
- [ ] If a Figma node was modified, changes were applied only on explicit request, not silently.
- [ ] Cross-reference to `vertical-spacing` noted when trim state affects Auto Layout gap perception.

## References

- Bringhurst, R. (2012). *The Elements of Typographic Style* (4th ed.). Hartley & Marks — inverse relationship between type size and tracking (larger size → tighter letter-spacing) for sentence-case text; em dash as the unspaced default parenthetical mark.
- Felici, J. (2003). *The Complete Manual of Typography*. Adobe Press — how x-height and glyph width should drive line-height and tracking selection per typeface.
- Butterick, M. *Practical Typography*. — all-caps text needs added letter-spacing (5–12%) because default font spacing is tuned for mixed-case letterforms; heavier weights carry proportionally less need for it since strokes already fill more of the counter.
- Wathan, A., Schoger, S. (2018). *Refactoring UI*. — practical uppercase/small-caps tracking values by size band, and UI text minimum-size floor.
- Hunt, R. — spaced en dash as a lighter-weight alternative to the em dash for sentence-level parenthetical breaks, when a house style prefers it.
- OpenType `case` feature (case-sensitive forms) — raises punctuation (hyphens, dashes, parentheses) to align with cap-height in all-caps/small-caps text.
- Felici, J. (2003). *The Complete Manual of Typography*. Adobe Press — oldstyle vs. lining figures, and their correct role split between running prose and tabular/display contexts.
- Latin, M. (2017). *Better Web Typography for a Better Web*. — tabular vs. proportional number spacing for UI/data contexts.
- OpenType number-style registered features: `onum` (oldstyle), `lnum` (lining), `pnum` (proportional), `tnum` (tabular).
- Bringhurst, R. (2012). *The Elements of Typographic Style* (4th ed.). Hartley & Marks — hanging punctuation as optical margin alignment.
- Related skill: [`microtypography`](../microtypography/README.md) Rule 1c — decides which dash character and spacing to use in prose; this skill only handles Figma-rendering-layer kerning/tracking on top of that choice.
- OpenType Font Variations spec (`wght`, `opsz` registered axes) — variable fonts expose weight as a continuous value and, when present, an optical-size axis designed to auto-adjust spacing/contrast per rendering size.
- OpenType `kern` feature / GPOS pair-positioning tables — per-pair optical correction (e.g. `AV`, `Ta`, `We`) baked into the font by its designer, complementary to (not replaced by) a uniform tracking value.
- CSS Working Group Draft: `leading-trim` / `text-box-trim` — crops the line box to cap-height/baseline, removing font-internal leading.
- Figma Plugin API Docs: `TextNode.textLeadingTrim`, `TextNode.letterSpacing`, `TextNode.fontFeatures`, `TextNode.letterCase`.
- Related skills: [`line-length-optimizer`](../line-length-optimizer/SKILL.md) (column width), [`microtypography`](../microtypography/SKILL.md) (character-level fixes) — apply after typesetting values are set, since column width and rag risk depend on the chosen font-size/line-height.
