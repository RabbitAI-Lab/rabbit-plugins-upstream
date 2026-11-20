# Changelog

## [0.2.1] - 2026-08-04

### Changed
- Added a "Try it — sample prompts" section to SKILL.md and README.md with
  five concrete trigger examples (pre-publish audit by path, safe-to-publish
  check, third-party install vetting, discoverability check). Docs only; no
  behavioral change.

## [0.2.0] - 2026-08-04

### Added
- Discoverability layer: a post-publish check — tag accurately with
  `--tags` / `--categories` / `--topics`, verify with `clawhub search
  <keyword>` or `clawhub explore` that the skill shows up for keywords a real
  user would type, and record the tags used plus a screenshot of the search
  results. Reported under a new `DISCOVERABILITY` line; inaccurate or missing
  topics get a WARN.
- CLI reality notes: `--topics` drive search (max 5); `--tags` are npm-style
  dist-tags, not keywords; `--categories` requires valid taxonomy slugs.

## [0.1.0] - 2026-08-03

### Added
- Initial release: 3-layer audit procedure (code / SKILL.md / release
  metadata), verification commands, declaration-vs-behavior diff, semantic
  prompt-injection review, scoring rubric, and the full annotated checklist
  with the incident behind every item.
