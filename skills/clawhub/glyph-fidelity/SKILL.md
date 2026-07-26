---
name: glyph-fidelity
description: Use when checking that letterform-level detail survives a transform — all-caps tracking by a continuous formula, ligature collisions under negative tracking, and inline acronyms needing their own subrange treatment to keep paragraph color even.
triggers:
  use_when:
    - user applies or reviews an ALL CAPS text transform
    - user asks about ligatures breaking under tight tracking
    - user asks how to handle an acronym (HTML, ZUS, USA) inside running prose
    - user asks why a heading "looks wrong" after transforming to uppercase
  do_not_use_for:
    - the base tracking direction/size rules for a text style (see text-typesetting Step 2 — this skill refines edge cases on top of it)
    - number figure styles (see text-typesetting Step 4)
    - hanging punctuation / dash rendering (see microtypography Rule 1c/4, text-typesetting Step 6/7)
metadata:
  author: Monika Zapisek
  project: Design Engineering Playbook
  version: 1.0
  status: accepted
---

# Glyph Fidelity

## Purpose

Protect letterform structure from three specific failure modes that a naive tracking/case transform introduces: under- or over-tracked all-caps text, ligatures that collapse into illegible blobs under negative tracking, and inline acronyms that break the paragraph's even visual "color" (texture).

## When To Use

- Any time text is transformed to `UPPERCASE`/`ALL CAPS`, to compute the correct tracking rather than a guessed round number.
- Reviewing a heading or label where letters look like they're touching or merging.
- Text containing acronyms (3+ consecutive capital letters) inside otherwise sentence-case prose.

## When NOT to use

- This isn't the primary tracking-direction logic — `text-typesetting` Step 2 (Branch A/B) already decides *whether* tracking is positive or negative and by roughly how much. This skill only refines the number for all-caps specifically and covers structural side-effects (ligatures, acronym color) that Step 2 doesn't address.

## Inputs

- `font-size` (px).
- The text content itself (to detect ligature-prone letter pairs and inline acronyms).
- Current tracking value, if reviewing an existing style.

## Outputs

- A precise tracking percentage for all-caps runs (continuous formula, not a banded guess).
- Flags for any ligature collision risk, with the fix (disable standard ligatures for that range).
- Flags for inline acronyms, with the subrange fix (own tracking + size adjustment).

## Workflow

### Rule 1 — All-caps tracking (continuous formula)

For any text-run transformed to `UPPERCASE`, tracking (`TS`) is a function of font-size (`FS`), not a fixed band:

```
TS = max(5%, min(12%, 160 / FS))
```

This produces roughly: 12% at very small sizes (10px), ~8% at 20px, tapering toward the floor as size grows. For large display headings (`FS > 32px`), compress further to a `+3%` to `+5%` range — the formula above starts overshooting once letterforms are large enough that spacing reads proportionally looser even at low percentages.

This refines, but does not replace, `text-typesetting` Step 2 Branch A's banded values (`≤12px → +10%`, `12–18px → +6%`, `>18px → +2%`) — use this formula when a precise, continuously-scaled value is needed (e.g. a fluid type scale); use the bands when a simpler discrete system is preferred. Don't apply both to the same node.

### Rule 2 — Small caps: never fake it

If `Small Caps` styling is required, never simulate it by shrinking the base font (`fontSize × 0.8`) and capitalizing — this produces thin, spindly letterforms with the wrong stroke weight relative to true small caps, which are drawn by the type designer at the correct weight. Check for and use the native OpenType feature instead:

- CSS: `font-variant-caps: small-caps;` (or `all-small-caps` if lowercase-context is needed too).
- Figma: `textNode.textCase = "SMALL_CAPS"`.
- If the font doesn't expose small caps at all, say so explicitly and let the user decide between a real (but imperfect) simulation and dropping the request — don't silently fake it either way.

### Rule 3 — Ligature collision under negative tracking

Negative tracking (`TS < -2%`, per `text-typesetting` Step 2 Branch B at large sizes) pulls letters closer together. Built-in ligatures (`fi`, `fl`, `ffi`, `ffl`) are pre-drawn as fused glyphs — at sufficiently negative tracking, the already-fused shape can start visually colliding with its neighbors, reading as a blob rather than two/three distinct letters.

- Trigger: tracking value more negative than `-2%` on a text containing ligature-prone pairs.
- Fix: disable standard ligatures for that specific range rather than reducing the tracking further (reducing tracking would undo the heading-tightening `text-typesetting` was asked to do).
  - CSS: `font-variant-ligatures: no-common-ligatures;` on the affected range.
  - Figma: `textNode.setRangeFontFeatures(start, end, { liga: 0 })` (or `textNode.opentypeFlags` depending on API version — verify against the installed Figma API version rather than assuming).
- Only disable ligatures on the specific range that triggered the check — don't disable ligatures globally across a node that also contains normally-tracked text.

### Rule 4 — Inline acronyms break paragraph color

A run of 3+ consecutive capital letters (`HTML`, `ZUS`, `USA`) inside otherwise sentence-case prose reads visually heavier and denser than the surrounding lowercase text — it creates a dark "spot" that breaks the paragraph's even visual texture (what Bringhurst calls color).

- Trigger: any inline run of ≥3 consecutive uppercase letters within sentence-case body text.
- Fix: isolate the acronym into its own subrange and apply:
  - Tracking: `+5%` on that subrange only.
  - Font-size: reduce by `1px` relative to the surrounding body text (a small optical correction — full-size acronyms read as shouting relative to the lowercase around them).
- Don't apply this to acronyms already styled as small caps or already in an all-caps heading (Rule 1 already governs those) — this rule is specifically for inline mixed-case contexts.

## Quality Checklist

- [ ] All-caps tracking computed from the formula (or the Step 2 bands, not both) and stated with the input `font-size` shown.
- [ ] Small caps verified as a native OpenType feature before use; simulated small caps only used with explicit user awareness.
- [ ] Ligature collision checked whenever tracking is more negative than `-2%`; fix disables ligatures on the affected range only, doesn't further reduce tracking.
- [ ] Inline acronyms (3+ caps) in sentence-case prose isolated into a subrange with `+5%` tracking and `-1px` size, not left at body-text default.
- [ ] Figma writes (if any) only applied on explicit request.

## References

- Bringhurst, R. (2012). *The Elements of Typographic Style* (4th ed.). Hartley & Marks — even paragraph "color" (visual texture) as a compositor's goal; acronyms and all-caps runs as color-breaking outliers requiring correction.
- Felici, J. (2003). *The Complete Manual of Typography*. Adobe Press — ligature behavior under tight tracking; true small caps vs. faked/scaled capitals.
- OpenType registered features: `liga` (standard ligatures), `smcp`/`c2sc` (small caps).
- Related skills: [`text-typesetting`](../text-typesetting/README.md) (base tracking direction/size — this skill refines edge cases on top of it), [`microtypography`](../microtypography/README.md) (character-level text rules independent of a design tool).
