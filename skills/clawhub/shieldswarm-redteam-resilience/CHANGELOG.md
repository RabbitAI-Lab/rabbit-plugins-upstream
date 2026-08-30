# Changelog

## v2.0.1 (2026-08-25) — token-optimization release

SKILL.md input tokens cut 32% (2,571 -> 1,758, o200k_base) with zero behavioral
change — verified by independent multi-model semantic-diff audits (verdict:
PRESERVED on every round). Registry note: v1.0.12 serves the v2.x content;
frontmatter lineage continues at 2.0.1 (publish with explicit --version).

### Changed
- Removed "What's New v2.0.0" + "Changelog v2.0.0" duplication (same items
  twice) and filler sections; de-duplicated approval/ROE/redaction rules to one
  occurrence each; "same as v1" meta-references dropped (file is self-contained).
- Frontmatter now declares categories [security, operations, agents] + topics
  (previously only set as publish-time flags).
- Template list replaced with `ls templates/` (package ships 31, list had 8).
- README "Complete Skill Reference" synced to the current SKILL.md.

### Added
- tools/shieldswarm_selftest.py documented (the shipped self-test).

### Known issue (pre-existing, not introduced here)
- SKILL.md references scripts/mode_selector.sh, scripts/shieldswarm_validate.sh,
  scripts/approval_gate.sh, scripts/quality_floor_check.sh — these files are not
  in the published package. Owner should add them or adjust the references.
