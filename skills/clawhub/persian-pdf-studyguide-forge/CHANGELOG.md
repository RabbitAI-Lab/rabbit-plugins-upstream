# Changelog

## 1.3.2 (2026-08-25)

### Added
- `examples/01_sleep_eating_review.html` — golden reference output (5.4 MB,
  fully self-contained Persian RTL exam-review guide produced by this
  pipeline): agents can diff their built guide against it to confirm
  structure, RTL shell, enrichment contracts, and offline self-containment.
- SKILL.md now points agents to the example as the "what good looks like"
  reference.
- Package hygiene: stale `scripts/__pycache__/*.pyc` artifacts (inherited from
  the original upload, regenerated at runtime) are no longer shipped.



## 1.3.1 (2026-08-25)

Token-optimization release: SKILL.md input tokens cut 24% (1,564 -> 1,185,
o200k_base) with zero behavioral change — verified by independent multi-model
semantic-diff audits (verdict: PRESERVED).

### Changed
- Removed the 21-bullet capability brochure (features are embodied by the
  scripts; a one-line "Built-in" summary remains) and the 19-line file
  inventory (replaced by `ls scripts/ templates/`).
- Fixed the stale "v1.2.2" title; description shortened without losing
  discovery keywords.
- Merged duplicate guardrails; strengthened phrasing (publish/distribute
  without permission, inspect and validate medical education).
- All 10 pipeline commands, flags, evidence-layer rules, and QA/definition-of-
  done criteria are unchanged.

### Added
- Model-routing guidance: strong model for primary correction and flashcard
  verification; cheap model for the reviewer pass and bulk enrichment.



## 1.3.0 (2026-08-21)

Field fixes from a full production run that converted a 48-page Persian
psychology lecture PDF into a study guide and then maximised its six enrichment
sections across multiple free-tier providers.

### Fixed

- `reasoning_team_enrich.validate()` no longer crashes on Persian page
  references («صفحهٔ ۳»), Persian/Arabic answer labels («الف/ب/ج/د», ۱–۴), bare
  JSON arrays, or partial-but-valid batches — these are now coerced into the
  strict contract instead of discarding otherwise-valid content (new shared
  helpers in `common.py`: `coerce_ref`, `coerce_answer`, `is_bare_answer`,
  `strip_option_prefix`).
- Enrichment no longer fails a whole session when a provider returns fewer
  items than requested; well-formed subsets are accepted.
- Multiple-choice-style flashcards no longer keep a bare letter ("A") as their
  answer: such cards are dropped, and the new QA gate `flash-no-bare-answer`
  fails the build if any remain.
- Quiz/bank options no longer duplicate the shell's A–D labels with their own
  «الف) » prefixes (stripped at validation and in the HTML builder; new QA gate
  `quiz-options-no-letter-prefix`).
- The combined `--maximum` schema could be truncated by a smaller provider and
  return empty quiz/scenario sections; enrichment now retries those sections
  with a focused pass.

### Added

- `scripts/verify_flashcards.py`: independent post-hoc verification that
  confirms or corrects each flashcard answer against its source page and drops
  undeterminable ones instead of inventing content.
- New QA gates: `flash-no-bare-answer`, `quiz-options-no-letter-prefix`.

## 1.2.2

Base release used for the production run. See `SKILL.md` for capabilities.
