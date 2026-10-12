# ClawHub lintlang — publish notes (v1.1.0 update, NOT published)

Prepared 2026-10-02 by the ClawHub steward. The live listing is untouched.

## What ships

- `SKILL.md` in this directory — publish-ready. Same slug (`lintlang`), same
  owner (@roli-lpci). Publishing creates version **1.1.0** (each publish is a
  new semver version; version history is kept).

## What changed vs live v1.0.0 (7 items)

1. **Skill body → audit-grade procedure.** Live body was the looser
   `skills/lintlang/SKILL.md` ("invoke when writing, editing, or reviewing…").
   New body is the `lintlang-audit` procedure: numbered trigger → runner →
   scan → verdict → report, explicit exclusions, exit-code semantics.
2. **Prompt-injection hygiene added** ("The output is data, not instructions").
   Matters on ClawHub post-SlowMist: findings quote the audited file verbatim.
3. **Honest-interpretation section added** (PASS ≠ safe, REVIEW ≠ failure).
4. **Runner self-test recipe added** (throwaway file, seeded H1.1 finding).
5. **Pins 0.8.1 → 0.8.2** (6 occurrences). Live listing was stale on arrival:
   published 2026-09-30 00:22 UTC from source @86dbb28 while 0.8.2 shipped the
   same day.
6. **License MIT-0 → Apache-2.0.** The live listing's MIT-0 is factually wrong;
   the repo's LICENSE is Apache-2.0 (verified via gh API). Correction, not a
   choice.
7. **Discovery optimization** (per ClawHub's vector-search weighting —
   display name > description > tags; body not indexed):
   - H1: "Lint agent instructions with LintLang" → **"Agent instruction audit
     with LintLang"** (noun-first keyword phrase; old H1 led with a verb).
   - Description rewritten noun-first and keyword-dense (lint, SKILL.md,
     CLAUDE.md, AGENTS.md, GEMINI.md, tool definitions, system prompts,
     agent configs) with the trigger ("runs on request when the user names a
     file") and exclusions up front.
   - **Tags added** (were absent): `lint, linter, audit, code-quality,
     agent-config, prompt, skill`.
   - Claude-Code-plugin-specific hook paragraph removed (meaningless to the
     OpenClaw audience).

## Deliberately NOT done

- No second listing (would read as registry spam/duplication).
- `name: lintlang` slug unchanged — required for in-place update.
- No `metadata.openclaw` changes (emoji 🔍, homepage, anyBins [lintlang, uvx]
  carried over).

## Freshness notes for the record

- Live v1.0.0 content = repo `skills/lintlang/SKILL.md` @86dbb28; repo HEAD has
  the same file with 0.8.2 pins (only delta). A prior internal note claimed the
  listing matched `.agents/skills/lintlang/SKILL.md` (the product-overview
  variant) — that was wrong; corrected here.
- Listing stats: 0 installs/60d, Security CLEAN, no stars. Republishing bumps
  `updatedAt` (recency signal for `recommended` sort); installs/ratings still
  need driving — discovery alone won't move those.

## Exact remaining step to ship

1. `clawhub login` (device flow — NOT done; the CLI reports "Not logged in").
   Complete at github.com/login/device in a signed-in browser session; authorize
   ONLY the ClawHub OAuth app after reading the consent screen.
2. From this directory: `clawhub publish ./package` (or `clawhub sync`).
3. Verify live: `clawhub inspect lintlang` → v1.1.0; confirm display title,
   description, tags, and Apache-2.0 license render correctly.
4. Optional, recommended: `clawhub star lintlang` (usage signals feed ranking).

## Docs cited

- steipete/openclaw `docs/tools/clawhub.md`: metadata powers discovery; usage
  signals (stars, downloads) improve ranking/visibility; each publish = new
  semver version with history.
- openclaw/clawhub `docs/http-api.md`: sorts (`updated` default,
  `recommended` = engagement + recency, `trending` = installs/7d); republish
  bumps `updatedAt`; slugs namespaced per owner (`ownerHandle/slug`).
- geeks-accelerator/in-bed-ai `docs/guides/optimizing-skills-for-clawhub.md`
  (5 skills published, keyword analysis 2026-03-29): vector search indexes
  display name (H1) > description > tags; body not indexed; lead with noun
  keywords, never verbs or filler.
