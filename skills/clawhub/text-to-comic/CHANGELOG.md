# Changelog

## 2.1.0

Iteration based on real-world diary-to-comic results (climbing diary and polar ocean park diary).

### Added

- Real finished comic examples:
  - `examples/climbing-diary-final.jpg` — 6-panel diary comic (2x3)
  - `examples/ocean-park-diary-final.jpg` — 10-panel diary comic (2x5)
  - `examples/webtoon-demo.json` — vertical scroll (webtoon) panel-plan example
- `scripts/assemble_page.py` — assemble rendered panels into a final page/canvas with optional Chinese caption overlay
- New validation fields in `schemas/render-task.schema.json`:
  - `no_numbering` — catches embedded page/panel numbering (e.g. "4/6") that image models sometimes add
  - `no_watermark` — catches baked-in AI watermark/signature in the corner

### Changed

- Unified version number across README / skill-card / CHANGELOG to `2.1.0`
- README now showcases real finished comics and a "reuse your protagonist across diaries" section
- SKILL.md validation section now requires `no_numbering` and `no_watermark` checks per panel
- compile_prompt.py now warns when a panel has a non-empty `text_budget` so text stays readable

### Insights from real usage

- Image models sometimes add panel numbering or a corner watermark despite the clean-image suffix — these need dedicated validation, not just a prompt suffix.
- Reusing one character bible across multiple diary entries keeps a personal comic "series" coherent (same protagonist, season-appropriate outfit).
- Long caption blocks under each panel are more reliable than forcing in-image text.

### Compatibility notes

- Slug remains `text-to-comic`
- Frontmatter remains compatible with the current OpenClaw metadata expectations
- Existing v2.0.0 / v2.0.1 panel plans and render tasks remain valid

---

## 2.0.0

This release upgrades the installed ClawHub release `1.0.0` into a publish-ready, structured v2 package.

### Added

- Structured `style preset` registry in `presets/styles.json`
- Structured `panel plan` schema in `schemas/panel-plan.schema.json`
- Structured `render task` schema in `schemas/render-task.schema.json`
- Example payloads in:
  - `examples/four-panel-demo.json`
  - `examples/infographic-demo.json`
- GitHub/ClawHub-oriented bilingual `README.md`
- Updated publishable `skill-card.md`
- `RELEASE_NOTES_2.0.0.md`
- `.gitignore` for local install artifacts
- Helper scripts:
  - `scripts/compile_prompt.py`
  - `scripts/validate_panel_plan.py`

### Changed

- Reframed the skill from a mainly prose-driven visual-director prompt into a staged workflow:
  - analyze
  - plan
  - style compile
  - render
  - validate
  - retry
  - assemble
- Preserved the original broad scope across comics, picture books, infographics, and hybrid outputs
- Preserved the original emphasis on:
  - content-type judgment
  - storyboarding
  - character consistency
  - scene continuity
  - clean-image composition
- Converted legacy style names into stable `style_id` values for repeatable behavior

### Compatibility notes

- Slug remains `text-to-comic`
- Frontmatter remains compatible with the current OpenClaw metadata expectations
- Simple natural-language requests still work without requiring users to provide JSON
- Structured JSON artifacts are additive, not mandatory for end users

### Expected benefits

- More stable output across retries
- Easier single-panel regeneration
- Better publishing review because intermediate artifacts are inspectable
- Less style drift because presets are explicit and reusable
- Easier future split into multiple specialized skills
