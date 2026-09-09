# Changelog

All notable changes to this skill are documented here.
Format based on [Keep a Changelog](https://keepachangelog.com/), adheres to [Semantic Versioning](https://semver.org/).

## [0.1.3] - 2026-09-09

### Changed
- Republished fresh after deleting the ClawHub slug (registry retained the 0.1.2 version number, so this clean release carries 0.1.3). Content identical to 0.1.2: fully fictionalized worked example, no confidential case references anywhere in the package or its history.

## [0.1.2] - 2026-09-09

### Changed
- Worked example fully fictionalized: the demo no longer references any real company or filing (compliance — the original case reference is confidential). Example files renamed to `format-demo-ir-detector*.md`; all identifiers replaced with fictional placeholders.
- Public repository history rewritten to a single clean commit; pre-0.1.2 tags removed, so the confidential case reference does not remain in public git history.
- ClawHub slug deleted and republished fresh, clearing the immutable pre-0.1.2 registry versions that still contained the original example.

## [0.1.1] - 2026-09-09

### Changed
- SKILL.md now opens with an English overview (positioning, pointer to `en/SKILL.md`) so the ClawHub/GitHub landing view leads bilingual instead of Chinese-only. Runtime workflow unchanged.

## [0.1.0] - 2026-09-09

### Added
- Six-phase workflow: acquire → structured extraction → gaming review → cross-validation → inference → ledger booking
- Field credibility grading table (v1 prior): capacity / product mix / emissions = high risk; equipment count / physical info = low risk, used as trust anchors; threshold-hugging signature checklist; three interest-review questions
- Cross-validation recipes: capacity (cycle-time / material / energy methods), yield back-calculation from material balance (material-balance method), emission back-calculation, product-mix inference from hazardous-waste fingerprints; external source list (discharge permit platform, hazwaste manifests, penalty records, prospectuses, customs)
- Minimal ontology ledger schema v0.1: 8 entities, 8 relations (incl. gaming_trace), JSONL format with provenance (file + page + verbatim quote), game_risk and status tags per fact, failed-query-driven schema evolution
- Process→equipment mapping seed for semiconductor / IR detector / nanoimprint tracks (~22 rows, uncertain entries marked 【to verify】)
- Bilingual documentation (Chinese primary, full English mirror under `en/`)
- Worked format demo using a fictionalized IR-detector case (all numbers explicitly marked illustrative)
