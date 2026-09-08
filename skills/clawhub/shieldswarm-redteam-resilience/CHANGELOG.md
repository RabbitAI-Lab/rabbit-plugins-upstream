# Changelog

## v2.1.1 (2026-09-06) — hygiene patch

- Removed `improvement_report.md` (a build/test artifact) from the shipped
  bundle: in a security skill, pre-existing log/report content that the
  operator did not generate is a trust issue.
- Verification-hash scope made explicit and stable: all package files except
  `README.md` and server-managed files (`.clawhub/`, `_meta.json`).

## v2.1.0 (2026-09-06) — "everything works" release

Resolves the v2.0.1 known issue (four referenced scripts missing from the
published package) and makes the whole package machine-readable,
self-verifying, and self-improving.

### Added
- `scripts/mode_selector.sh` — deterministic mode + first-action selection
  (key=value output, exit 0/2).
- `scripts/shieldswarm_validate.sh` — fail-closed command validator
  (offensive patterns, secret exposure, red-team ROE gate, length limit).
- `scripts/approval_gate.sh` — append-only JSONL approval log with atomic
  writes and separation of duties (high risk: approver ≠ rollback owner and
  ≠ operator).
- `scripts/quality_floor_check.sh` — model quality-floor gate with a hard
  `cloud_only` policy (local/gguf/ollama/llama.cpp/onnx always FAIL).
- `templates/quality_floor_matrix.yaml` — flat, machine-readable matrix,
  tier membership grounded in the operator's live 751-model cloud fleet.
- `references/modes.md`, `references/incident.md`,
  `references/model_resilience.md`, `references/promotion.md`,
  `references/self_improvement.md` — progressive-disclosure detail files.
- `tools/self_improve.py` — durable feedback loop (log/learn/report/reset;
  local `feedback.jsonl`, never uploaded; secret-rejecting).

### Changed
- `SKILL.md` rewritten: explicit command-contract table (flags → output
  keys → exit codes), progressive-disclosure load map, references only
  files that exist. Body kept well under the 500-line open-standard budget.
- `tools/shieldswarm_selftest.py` rewritten for v2.1: 12 check groups incl.
  functional smoke tests of all four scripts (PASS and FAIL paths), matrix
  semantics, and reference integrity. (The v2.0.1 self-test was written for
  the v1.x package and failed against it.)
- Quality-floor guidance: removed "local Qwen" fallbacks and all local-model
  references; cloud-only policy now enforced by the script, not by prose.
- `skill-card.md`: the "referenced helper scripts not present" risk is
  resolved (scripts shipped + smoke-tested).
- `README.md` synced to v2.1.0.

### Fixed
- D1 — SKILL.md referenced 4 scripts that did not exist: all four now ship
  and are smoke-tested by the self-test.
- D2 — SKILL.md referenced 7+ templates that did not exist: references now
  point only at existing files (self-test enforces).
- D3 — shipped self-test failed on the shipped package: self-test v2.1
  passes on v2.1.
- D4 — quality floor was prose with local-model fallbacks: now a flat YAML
  matrix + deterministic gate.

### Evidence
- Deep improvement research distributed across cloud models (gemini design
  review; llm7 script design) plus web evidence from the Anthropic Agent
  Skills open standard (≤500-line SKILL.md body, three-tier progressive
  disclosure, description-as-trigger, scripts run without loading code).
- Debug stage: full local static + functional pass, then a multi-provider
  consensus audit (finding fixed when 2+ independent models agree, or when
  directly evidenced). Findings appended below.

### Debug findings (multi-model consensus + direct evidence)

Method: five independent model audits (openrouter/minimax-m3, llm7,
gemini-3.1-flash-lite, cohere/command-a, plus a two-model diff re-audit of
the ROE gate) + exhaustive local functional tests. Consensus rule: a finding
is acted on when 2+ independent models agree **or** when directly evidenced
against the source; every finding's quoted evidence is byte-verified first
(findings citing non-existent files or unquotable lines are rejected as
hallucinations — this is how 14 of 19 model findings were rejected).

Acted on (4 fixes):
- self-test's dangerous-pattern scan was tripping on its own blocklist
  literal → scan scoped to docs/config; executables covered by functional
  smoke tests instead (direct evidence).
- ROE gate only checked file existence → now requires structural keys
  (uncommented, line-anchored `scope:`, `abort_conditions:`,
  `rollback_owner:`, `authorized_by:`) plus non-empty `exercise_name` /
  `authorized_by` / `rollback_owner`; an untouched template, a
  whitespace-only value, or a commented-out key is rejected (cohere +
  direct evidence; smoke-tested both directions).
- whitespace-only quoted values no longer count as filled; field values are
  trimmed before the emptiness check (cohere + direct evidence).
- all new gate behavior is covered by self-test smoke cases (PASS and FAIL
  paths), keeping the package self-verifying.

Rejected with rationale (14 of 19): fabricated file references
(gemini-3.1-flash-lite: 4/5 findings cited files that do not exist in the
package), claims disproven by functional tests (llm7 round 1: 5/5 — e.g.
"--max-len not implemented" while the flag exists and is exercised),
coherent-but-wrong design suggestions (audit-grade work already needs the
strongest models; see references/model_resilience.md), and portability
non-issues (`stat -c%s` is GNU-only; `:` needs no ERE escaping).

Provider notes (environmental, not skill defects): groq free tier returns
413 for large audit payloads and one empty HTTP-200; huggingface key was in
quota cooling; zai timed out; mistral was rate-limited during the audit
window. Recorded per the skill's own feedback protocol.

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
