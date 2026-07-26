# Glyph Fidelity

**Protect letterform structure under all-caps transforms and tight tracking.**

Three specific failure modes a naive tracking/case change introduces: wrong all-caps tracking (uses a continuous formula, not a guess), ligatures collapsing under negative tracking, and inline acronyms breaking a paragraph's even visual texture.

## What it does

- **All-caps tracking formula**: `TS = max(5%, min(12%, 160/FS))`, compressed to `+3–5%` above 32px — a precise, continuously-scaled alternative to banded tracking values.
- **Small caps guard**: refuses to fake small caps by shrinking the base font; checks for the native OpenType feature first.
- **Ligature collision check**: flags when tracking below `-2%` risks colliding built-in ligatures (`fi`, `fl`, `ffi`), and disables ligatures on just that range instead of loosening the tracking.
- **Inline acronym isolation**: detects 3+ consecutive capital letters inside sentence-case prose and isolates them into a subrange (`+5%` tracking, `-1px` size) so they don't read as a dark "spot" breaking paragraph color.

## When to use

- Applying or reviewing an ALL CAPS transform.
- A heading or label where letters look like they're touching or merging.
- Prose containing acronyms (HTML, ZUS, USA) that look visually heavier than surrounding text.

## When NOT to use

- Base tracking direction/size decisions — see `text-typesetting` Step 2. This skill only refines the all-caps number and handles structural side-effects.
- Number figure styles — see `text-typesetting` Step 4.

## What's inside

```
glyph-fidelity/
├── README.md    ← this file
├── SKILL.md     ← full rules, formulas, quality checklist
└── LICENSE      ← MIT
```

## Related skills

Part of the typography/layout family in this playbook. Refines [`text-typesetting`](../text-typesetting/README.md)'s tracking output for the specific case of all-caps text and its side-effects; independent of design-tool context (applies equally to CSS output).

## License

MIT — see `LICENSE`. Author: **[Monika Zapisek](https://monikazapisek.com)**. Project: **Design Engineering Playbook**.

---

*Part of the [Design Engineering Playbook](https://github.com/monikazapisekstudio/design-engineering-playbook) — AI-assisted workflow artefacts for product designers working in agile and lean environments.*
