---
name: microtypography
description: |
  Polish body text before publishing — Polish or English — by fixing hanging single-letter conjunctions/prepositions, adding orphan guards, flagging widow risks, and handling ragged-edge risks without rewriting copy.
triggers:
  use_when:
    - user asks for microtypography
    - user asks to fix hanging conjunctions or hanging prepositions
    - user asks for sieroty i wdowy
    - user asks for a publishing/typesetting pass on markdown, HTML, or plain text
    - user pastes long-form body copy and asks for typography polish
  do_not_use_for:
    - code
    - tables
    - short UI labels
    - copywriting or wording rewrites
    - layout work that requires rendered page inspection
license: MIT
model: Claude Sonnet 4.5
compatibility: |
  Designed for Claude Code, Codex, VS Code, OpenCode, Cursor, and GitHub Copilot.
  No external dependencies, no MCP required, no network access at runtime.
metadata:
  author: Monika Zapisek
  project: Design Engineering Playbook
  version: 1.0
  created: 2026-07-08
  updated: 2026-07-08
  status: accepted
---

# Microtypography

## Purpose

Clean up a block of text at the sentence/paragraph level so it reads well when typeset — no single-letter words stranded at line end, no single-word "orphan" lines left dangling, no unreported widow risk at a column/page break, and no unmanaged ragged-edge risk.

## When To Use

- Before publishing a blog post, landing page copy, case study, or any long-form markdown/HTML content.
- When the user asks to "fix hanging conjunctions", "sieroty i wdowy", "clean up typesetting", "polish this text", or pastes a paragraph and asks for a typography pass.
- Not for code, tables, short UI strings, or single-line labels — there's no line-wrap to protect.

## Inputs

- The text to fix (markdown, HTML, or plain text).
- Target language: Polish, English, or mixed (detect per-paragraph if mixed).
- Output format: same as input by default; ask if ambiguous (e.g. plain text pasted but destined for HTML).

## Outputs

- The corrected text in the same format as the input, with non-breaking spaces inserted and any widow/orphan fixes applied.
- A short change log: what was changed and why (grouped by rule), so the edit is auditable — do not silently rewrite wording.
- For ragged-edge handling: either a direct rewrap for hard-wrapped text, or a non-destructive set of soft-hyphen insertions and CSS/review flags for reflowing text (see Rule 3).
- For hanging punctuation: a CSS suggestion for reflowing output, or a flag (not a computed value) for Figma display headings (see Rule 4).

## Workflow

### Rule 1 — Hanging single-letter conjunctions/prepositions (non-breaking space)

Insert a non-breaking space between a single-letter (or otherwise "small") conjunction/preposition and the word that follows it, so it can never be the last character on a line.

**Polish** — single-letter words that must never end a line: `i, a, o, u, w, z, k` (and their capitalized sentence-start forms). Also treat short two-letter forms as strong candidates when local style guides require it: `by, że, aż, iż, ze, we, do, na, od, po, ku` — apply these only if the project's style guide asks for it; the single-letter rule is non-negotiable, the two-letter rule is a style choice.

**English** — single-letter words: `a, I`. English typesetting is generally more lenient than Polish (no hard rule against "a" or "I" ending a line), so treat this as optional polish, not a hard fix, unless the user asks for strict typesetting.

**Mechanics per format:**
- Plain text / markdown: replace the space after the conjunction with ` ` (non-breaking space, renders as ` ` visually but blocks the line break). In markdown source this is the literal NBSP character, not an HTML entity, unless the target is HTML.
- HTML: use `&nbsp;` between the word and what follows.
- Do not insert NBSP inside code spans, URLs, or already-escaped content.

### Rule 1b — Numbers, units, and dimensions

- **Multiplication sign in dimensions:** in a dimension pattern (`<number> x <number>`, e.g. `1920x1080`, `3 x 4 m`), replace the `x`/`X`/`*` with the proper multiplication sign `×`. Don't touch a bare `x` that isn't between two numbers (variable names, "x-axis", "Grade x").
- **NBSP between number and unit/currency:** bind a numeric value to its unit or currency symbol with NBSP so they can't split across a line: `100 PLN`, `50 m`, `16 px`, `3 kg`. Applies to abbreviated units and currency codes/symbols, not to spelled-out words ("100 dolarów" already reads fine without a hard rule).
- Skip both inside code spans, URLs, and literal code (CSS values like `1920x1080` in a config file are not prose).

### Rule 1c — Smart punctuation

**Dashes — three different characters, three different spacing rules. Don't collapse them into one "make it fancy" transform:**

- **Em dash `—`** (parenthetical break, EN default per Bringhurst): no surrounding spaces — `word—word`. Replace a double hyphen `--` used this way with a bare em dash, not a spaced one.
- **En dash `–`** as a sentence-level parenthetical break (PL convention, and the Hunt-recommended EN alternative when a house style prefers a lighter mark than the em dash): surrounded by spaces — `word – word` — and those spaces should be NBSP if the dash sits near a line-wrap-risky position (short word before/after), otherwise a regular space is fine.
- **En dash `–` in a numeric/date range** (`10-15kg`, `2020-2023`): **no spaces at all** — `10–15 kg`, `2020–2023`. This is a different use of the same character from the sentence-dash case above; don't apply spacing rules meant for prose to a range. Add the NBSP-before-unit fix from Rule 1b where a unit follows (`10–15 kg`).
- **Hyphen `-`**: never surrounded by spaces, in any context (compound words, prefixes). Don't touch hyphens that aren't standing in for an em/en dash — most hyphens in normal text are correct as-is.
- Confirm which EN house style applies (unspaced em dash vs. spaced en dash) if the input doesn't already show a consistent pattern — don't silently pick one.

**Quotation marks:** detect the paragraph's language and convert straight quotes `"..."` to the typographically correct pair: Polish `„...”`, English `“...”`. Only convert quotes that wrap actual quoted/spoken text — leave straight quotes inside code, JSON, or attribute values untouched.

Both are opt-in-by-default in code-adjacent contexts (README snippets, inline code) — never touch quotes or dashes inside a code span, fenced block, or URL.

**Design-tool context:** if the dash/range sits inside a Figma text node (not markdown/HTML prose), the character choice above still applies, but kerning and per-range tracking around the dash are handled by [`text-typesetting`](../text-typesetting/README.md) Rule 6, not here — this skill decides *which character and spacing*, that skill decides *how it renders*.

### Rule 2 — Widows and orphans

- **Orphan** (in typesetting terms as used here: a single word, or a very short line, left alone at the *end* of a paragraph, wrapping to its own line): reflow by tightening wording (rare) or, more practically, by inserting an NBSP between the last two words of the paragraph so they can't be split — the standard cheap fix.
- **Widow** (a short line — often one word — left alone at the *top* of a new column/page after a page break): flag it; fixing it requires knowing the actual line breaks at render time, which this skill can't see from raw text. Note it in the output as "widow risk — verify after layout" rather than guessing a fix.
- Prefer the same NBSP-between-last-two-words technique proactively at the end of every paragraph as a low-cost orphan guard, not just when one is spotted.

### Rule 3 — Ragged edges

Split by whether the text has hard line breaks or reflows.

**Case A — hard-wrapped text** (terminal output, poetry, plain-text captions, README manually wrapped to N columns): this is fixable directly only when the hard line breaks are part of body prose, not code or tables. Recompute the wrap with a best-fit / minimal-raggedness algorithm (minimize the variance of line-end positions across the paragraph — a lightweight Knuth-Plass-style pass, not naive greedy wrap, since greedy wrap maximizes rag). Apply the fix; note the target column width used in the change log.

**Quantified rag threshold** (applies to both cases, but especially narrow containers — mobile, UI cards): measure the longest and shortest line in the paragraph. If `(longest − shortest) / container_width > 20%`, the rag is bad enough to act on, not just cosmetically uneven — this is the trigger point, not a vague "looks ragged" judgment call. Below 20%, leave it; natural word-length variation produces some rag and over-correcting flattens it artificially.

**Case B — reflowing text** (normal markdown/HTML rendered by a browser/CMS): the source doesn't control where lines actually break, so there's nothing to rewrap. Two things are still legitimate to do here, both non-destructive to wording:

1. **Soft hyphens (`&shy;` in HTML, soft-hyphen char `­` in markdown/plain text)** on long, unbreakable words (long Polish compounds, CamelCase, long tokens) so *if* the renderer needs to break there, it hyphenates cleanly instead of overflowing or forcing an ugly gap. Insert at defensible syllable or morpheme boundaries only. If you cannot identify safe break points, do not guess; flag the word for manual review instead.
2. **CSS recommendation** (report, don't silently edit a stylesheet unless asked): `hyphens: auto;` and `text-wrap: pretty;` on body copy, `text-wrap: balance;` on headings. This is the correct fix location for rag in reflowing text — flag it as a suggested CSS change alongside the text output.

Do not reword sentences to control line length in Case B — that changes content, not typesetting, and violates the "don't alter wording" rule. If reflow genuinely looks bad only after rewording could fix it, offer it as an explicit **opt-in suggestion** the user must accept separately, never auto-applied.

### Rule 4 — Hanging punctuation

A punctuation mark sitting at the very start or end of a line of text (an opening quote, dash, bullet, or parenthesis) reads as breaking the column's optical edge, even though it's technically inside the margin — the eye aligns to the letterforms, not the punctuation. Hanging punctuation pushes that mark slightly outside the block so the *letters* line up cleanly.

- **Reflowing HTML/markdown (Case B territory):** recommend the CSS property `hanging-punctuation: first last;` on the paragraph/block — this is the correct, native fix and needs no text-level change. Report it as a suggestion alongside other CSS recommendations (Rule 3 Case B), don't silently add it to a stylesheet.
- **Plain text/markdown source:** nothing to do — hanging punctuation is a rendering-layer property, not something the source text encodes. Don't attempt a manual workaround (extra spaces, etc.) here.
- **Design-tool context (Figma):** Figma has no native global hanging-punctuation toggle. For a display heading (≥24px) that opens with a quotation mark, this becomes [`text-typesetting`](../text-typesetting/README.md)'s job — it has the paragraph-indent / separate-container tools to pull the mark outside the block. This skill only flags *that* a heading opens with hanging-punctuation-eligible characters (`„`, `"`, `«`, dashes, parentheses); it doesn't compute the indent value itself.
- Only applies to headings/display text and the first/last line of justified or visually-prominent blocks — not worth flagging for ordinary body paragraphs where the effect is negligible.

### Steps

1. Detect language per paragraph (or ask if ambiguous).
2. Apply Rule 1 across the whole text.
3. Apply Rule 1b (dimensions, number+unit NBSP) and Rule 1c (smart dashes and quotes), skipping code/URLs.
4. Apply Rule 2 at the end of every paragraph, plus flag any widow risk near page/column breaks if such breaks are indicated in the input.
5. Apply Rule 3: if the input has hard line breaks, rewrap using the minimal-raggedness pass (Case A); otherwise insert soft hyphens on long unbreakable words and report a CSS suggestion (Case B) — never skip silently.
6. Apply Rule 4: recommend `hanging-punctuation: first last;` for reflowing HTML/CSS output; flag (don't compute) hanging-punctuation-eligible display headings for Figma contexts.
7. Return corrected text + change log + any manual-review flags.

## Quality Checklist

- [ ] No single-letter PL conjunction/preposition (`i, a, o, u, w, z, k`) ends a line — verify by checking each occurrence got an NBSP, not just a regex pass.
- [ ] EN `a`/`I` handled per requested strictness (default: leave as-is unless asked for strict mode).
- [ ] Dimension `x` correctly converted to `×` only between two numbers, never touching variable/axis names.
- [ ] Numbers bound to units/currency with NBSP; numeric ranges use en dash + NBSP-before-unit.
- [ ] Dashes and quotes converted per detected language, and only in prose — not inside code, URLs, or attribute values.
- [ ] No paragraph ends in a single stranded word (orphan) — last two words of every paragraph joined with NBSP.
- [ ] NBSP not inserted inside code, URLs, or markup attributes.
- [ ] Output format matches input format (or the explicitly requested one).
- [ ] Change log lists every rule applied, not just a diff.
- [ ] Ragged-edge: Case A (hard-wrapped) shows before/after rewrap; Case B (reflowing) lists soft-hyphen insertions and the CSS suggestion, not left blank.
- [ ] Wording itself was not altered beyond what's needed for orphan-joining — this is a typesetting pass, not a copy edit. Any reword-for-rag suggestion is clearly marked opt-in, separate from applied changes.
- [ ] Rule 1/Rule 2 overlap checked: if the paragraph's last word pair already got an NBSP from Rule 1 (e.g. ends in "... w trakcie."), don't apply a second, redundant NBSP for the orphan guard — note the overlap instead of double-binding.
- [ ] Hanging punctuation: CSS suggestion given for reflowing output; Figma display headings flagged (not computed) and handed off to `text-typesetting`.

## References

- Felici, J. (2003). *The Complete Manual of Typography*. Adobe Press — widow/orphan control and paragraph-level polish as core typesetting hygiene, distinct from page-level (macrotypography) concerns.
- Mittelbach, F. & Goossens, M. et al. — LaTeX `microtype` package documentation — the term of art *microtypography*: character/word-level spacing and hyphenation control, as distinct from macrotypography (grid, columns, page layout).
- Polska norma redakcyjna (Wolański, A. (2008). *Edycja tekstów. Praktyczny poradnik*. PWN) — niełamliwa spacja po spójnikach i przyimkach jednoliterowych jako standard redakcyjny; odzwierciedlona w regułach autokorekty InDesign "Polish rules".
- Bringhurst, R. (2012). *The Elements of Typographic Style* (4th ed.). Hartley & Marks — hanging punctuation: optical margin alignment for quotes, dashes, and other marks at line/column edges.
- CSS Working Group: `hanging-punctuation` property (`first`, `last`, `force-end` values) — native browser implementation of the same principle.
- Related skill: [`text-typesetting`](../text-typesetting/README.md) — computes the actual Figma paragraph-indent/container workaround for hanging punctuation on display headings; this skill only detects and flags the condition.
