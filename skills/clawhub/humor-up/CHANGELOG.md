# Changelog

## [0.1.0] - 2026-08-02

### Added
- Initial release: 7 humor jobs (punch-up, occasion writer, witty daily brief,
  joke on demand, icebreakers, caption-this, joke doctor & scorer).
- Five craft laws for every humorous line, in English and 中文.
- 14-pattern bilingual pattern library (`patterns.md`) with build steps and
  failure modes per pattern.
- 4-dimension scoring rubric with calibration examples.
- Anti-cringe contract: explicit rules for when NOT to be funny.

### Security
- Pure-prompt skill: no scripts, no environment variables, no CLI dependencies,
  no network access. Nothing to declare in `metadata.openclaw.requires` — and
  that's the honest declaration.
