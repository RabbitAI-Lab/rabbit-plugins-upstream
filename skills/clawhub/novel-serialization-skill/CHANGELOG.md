# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- `.gitignore` and `.editorconfig` (were missing from the generated project)
- `LICENSES/CC-BY-NC-SA-4.0.txt` with the official Creative Commons license text
- `README_FOR_AI_Audit_Report.md` recording the post-generation compliance audit
- `CONTRIBUTING.md`: Recognition Policy section (required by spec Section 7.6)
- `references/method-patterns.md`: Style Consistency Rules row in the split index
- `README_FOR_AI_Audit_Report_Round2.md`: content-level re-audit (12 further defects)
- `CONTRIBUTING.md`: Review Process and Markdown linting rules (required by spec Section 7.6)
- `.github/workflows/novel-release.yml`: the licence gate now inspects chapter content for the
  CC BY-NC-SA 4.0 header, and the continuity gate now fails when the module or required
  `state/` files are missing
- `references/method-patterns-publishing.md`: documented the frontmatter-vs-CC-header ordering
- `references/examples/example-chapter-draft.md`: added the mandatory YAML frontmatter
- `README_FOR_AI_Audit_Report_Round3.md`: cross-document consistency audit (6 further defects)

### Changed
- `modules/` restructured to `modules/<name>/SKILL.md` per spec Sections 1 and 5.2
- `references/examples/` created and the three worked examples moved into it
- `.github/ISSUE TEMPLATE` renamed to `.github/ISSUE_TEMPLATE` so GitHub detects the forms
- `.gitattributes` now enforces `eol=lf`, matching `.editorconfig`
- All files normalized to LF line endings with a trailing newline
- Version fields aligned to 1.1.2 (all seven SKILL.md files and the README badge)
- `CODE_OF_CONDUCT.md` / `SECURITY.md`: fabricated contact addresses replaced with the
  spec-mandated placeholders
- `.github/workflows/novel-release.yml`: the chapter-format gate can now actually fail, and
  no longer errors when `chapters/` is absent
- The CC BY-NC-SA 4.0 license header ordering rule (frontmatter at byte 0, then the header,
  then narrative) is now stated identically in all 11 files that state it, instead of only in
  `references/method-patterns-publishing.md`. This closes a contradiction introduced by the
  ordering fix itself: `prompts/02-robustness-checks.md` previously instructed reviewers to
  reject compliant chapter files
- Root `SKILL.md` no longer calls chapter frontmatter optional while the publishing template
  makes it mandatory
- World-building and character sheet paths in the two modules now match the root `SKILL.md`
  conventions instead of contradicting them
- `state/location-states.md` added to the root state inventory, which the continuity-tracker
  module already required
- Chapter filename examples zero-padded to 3 digits everywhere, so lexical sort equals numeric
  sort
- Continuity reports now go to `state/continuity-reports/` instead of the Git-ignored `drafts/`
- Root `SKILL.md` Continuity State table: state-file ownership realigned to the continuity tracker
- All six module SKILL.md files: sibling modules relabelled from "Sub-Skills"/"branch skills"
  to "Related Modules" (peers), and the path column converted to resolving relative links
- `README.md`: architecture diagram rebuilt on a uniform 68-column grid
- `CONTRIBUTING.md`: dual-mode wording corrected so it no longer contradicts itself

### Fixed
- Broken internal links in `references/method-patterns.md` (raw space + wrong anchor)
  and `prompts/01-implement-method.md` (pointed at the wrong README)
- Three module SKILL.md files referencing example files that do not exist in the spec tree
- `CHANGELOG.md` compare links, which were missing the owner path segment
- Headings rendered as literal text in five files (no preceding blank line)
- `CONTRIBUTING.md`: branch prefix unified to `feat/`, missing TOC entry added
- `CONTRIBUTING.md` no longer tells contributors to run `validate.py` or `tests/` (neither exists)
- `CONTRIBUTING.md`: leftover `feature/` branch prefix unified to `feat/`
- `references/method-patterns-publishing.md`: malformed `poV:` frontmatter key corrected to `pov:`
- `modules/chapter-writing/SKILL.md`: the undefined "continuity state header" term now points at
  the concrete frontmatter defined in the publishing template
- `SECURITY.md`: GitHub's template boilerplate sentence replaced with real content
- `README.md`: directory tree was missing `.gitattributes` and the audit reports
- `references/examples/example-chapter-draft.md`: word-count claim no longer states 4,500 words
  of prose that the file does not contain

## [1.1.2] - 2026-09-14

### Changed
- Updated README FOR AI.md metadata version to 1.1.2
- Updated license policy documentation for clarity
- Improved runtime output language specification

### Fixed
- Corrected file naming convention note in README
- Fixed license header references in prompt templates

## [1.1.1] - 2026-09-10

### Changed
- Refactored module structure for improved modularity
- Updated SKILL.md frontmatter with dual license declarations
- Improved glossary definitions in references/

### Fixed
- Fixed broken cross-references in method-patterns.md
- Corrected module trigger descriptions

## [1.1.0] - 2026-09-05

### Added
- Added `continuity-tracker` module for state tracking and memory persistence
- Added `method-patterns-continuity.md` split module
- Added `example-chapter-draft.md` worked example
- Added GitHub Actions release workflow template
- Added dependabot configuration
- Added FUNDING.yml for community support

### Changed
- Split `method-patterns.md` into sub-modules per the 500-line rule
- Updated project directory structure documentation
- Improved prompt templates with output language instructions

### Fixed
- Fixed continuity state tracking inconsistencies
- Corrected version numbering in YAML frontmatter

## [1.0.0] - 2026-08-28

### Added
- Initial release of GitHub Novel Serialization Skill
- Core SKILL.md index and quick-reference
- `references/method-patterns.md` master template file
- `prompts/` dual-mode prompt templates (implement-method, robustness-checks)
- Functional modules:
  - `worldbuilding/` — World-building sub-skill
  - `character-design/` — Character design sub-skill
  - `chapter-writing/` — Chapter writing sub-skill
  - `continuity-check/` — Continuity & consistency verification sub-skill
  - `publishing-workflow/` — GitHub publishing & release sub-skill
- Example files: worldbuilding, character sheet, chapter draft
- GitHub community health files (ISSUE_TEMPLATE, PULL_REQUEST_TEMPLATE)
- .gitignore and .editorconfig
- Dual licensing: GPL-3.0 + CC BY-NC-SA 4.0
- CODE_OF_CONDUCT.md, CONTRIBUTING.md, SECURITY.md, CHANGELOG.md

---

[Unreleased]: https://github.com/[OWNER]/[REPO]/compare/v1.1.2...HEAD
[1.1.2]: https://github.com/[OWNER]/[REPO]/compare/v1.1.1...v1.1.2
[1.1.1]: https://github.com/[OWNER]/[REPO]/compare/v1.1.0...v1.1.1
[1.1.0]: https://github.com/[OWNER]/[REPO]/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/[OWNER]/[REPO]/releases/tag/v1.0.0
