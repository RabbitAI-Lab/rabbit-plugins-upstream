# Changelog

## v2.0.0 (2026-09-06) — full rebuild: from hollow package to working scanner

### Why
The v1.x package (last: v1.0.8) contained no implementation:
- SKILL.md body: "Follow the skill instructions to use this skill" — zero
  instructions; every advertised capability (CVE detection, dependency
  analysis, supply-chain risk, reports) unimplemented.
- Contradictory privacy claims: SKILL.md said "fully offline, no data sent";
  README said "network access to query CVE/OSV databases". The registry's
  own skill card flagged: "privacy and network behavior are inconsistent in
  the evidence".
- Non-standard frontmatter (`name: 🔍 Agent Bom Scan`), fake 16-hex
  "verification hash", no version/license/changelog in frontmatter.

### Added
- `scripts/bom_scan.py` — stdlib-only scanner: `scan` / `bom` / `check`
  subcommands; 8 lockfile parsers; embedded-DB range matching; optional
  `--mode online` via `api.osv.dev/v1/querybatch` (name+version+ecosystem
  only); CVSS 3.1 base scores computed at runtime; key=value + JSON +
  markdown outputs; exit 0 CLEAN / 10 FINDINGS / 2 usage / 3 fatal.
- `data/advisories.yaml` — 34 advisory records, every one verified against
  the OSV.dev API on 2026-09-06 (id, ranges, aliases, CVSS vector),
  including Log4Shell (CVE-2021-44228). Declared a curated subset.
- `tools/bom_selftest.py` — 12 offline check groups incl. functional
  fixtures with expected advisory ids, CVSS 3.1 vs NVD-verified scores,
  go.sum `/go.mod` dedupe, provenance completeness, and a true-offline
  isolation test (socket layer disabled).
- `tools/bom_improve.py` — local-only feedback loop (log/learn/report) with
  a closed event vocabulary.
- `references/triage.md`, `references/online_protocol.md`,
  `references/advisories_format.md` — lazy-loaded playbooks.
- `tools/fixtures/` — vulnerable + clean test projects (npm, PyPI, Go).

### Changed
- SKILL.md rebuilt to the Agent Skills open standard: compliant frontmatter
  (lowercase name matching the slug, what+when description, version,
  license, categories, topics), machine-readable command contracts,
  progressive-disclosure load map, 178 lines (<=500 budget).
- Privacy is now honest and verifiable: offline = zero network (proven by
  test); online = explicit opt-in with a documented data-minimization list.
- README: real verification hash (TREE-SHA256-v1, 64 hex) with a
  recompute command; permissions/security sections match actual behavior.
- `skill-card.md`: risks updated to the real risk set.

### Evidence
- Deep design research distributed across cloud models (gemini design spec;
  llm7 code design) + web evidence (OSV.dev API docs incl. querybatch and
  MAL- malicious-package records; SCA tooling comparisons favoring
  ecosystem-native ranges over CPE matching).
- Advisory DB grounded via live OSV.dev queries (11 packages batched +
  targeted fetches for Log4Shell and CVE-2023-45857).
- CVSS 3.1 formula verified 5/5 against NVD API ground truth (same
  vectors, same scores) — including two formula bugs found and fixed during
  the debug stage (Roundup must stop at one decimal; the impact/exploit
  formula coefficients).
- Debug stage: local functional matrix (vulnerable/clean fixtures, exit
  codes, parsers) + multi-provider consensus model audit with byte-level
  evidence verification. Findings below.

### Debug findings (multi-model consensus + direct evidence)

Method: local functional matrix (vulnerable/clean fixtures, exit codes,
parsers, online mode) + three independent model audits (openrouter/
minimax-m3, cohere/command-a, llm7) + a two-model diff re-audit of the
changed code. Consensus rule: acted on when 2+ independent models agree or
when directly evidenced; every finding's evidence quote is byte-verified
first (findings citing unquotable or non-existent lines are rejected).

Acted on (11 fixes):
- CVSS 3.1 Roundup implemented with the wrong decimal steps — verified
  against NVD ground truth (5/5 vectors match after the fix; two formula
  bugs found, both from the roundup function, not the coefficients).
- go.sum `/go.mod` hash lines created duplicate versions — stripped.
- Forward reference bug: LOCKFILE_MAP defined before its parser functions.
- no_data_packages metric was name-based (cross-ecosystem collisions) —
  now (name, ecosystem) pair-based (openrouter + cohere).
- Online mode keyed queries by (name, version) — ecosystem collision
  possible; now (name, version, ecosystem) + chunked querybatch for >40
  packages (openrouter + cohere).
- Online result alignment: added batch/results length validation with a
  hard fail (llm7 diff re-audit).
- Empty BOM now emits an explicit "nothing scanned" warning (llm7 diff).
- package-lock.json v2/v3: skip `link: true` workspace entries; name
  extraction only strips real `node_modules/` prefixes (openrouter).
- Discovery now warns when directories beyond the depth limit are skipped
  (cohere).
- SKILL.md contract states the `--severity-floor` default (low) explicitly
  (cohere).
- Self-test gained a feedback-loop group (log/learn/report + secret
  rejection) after a cohere finding about untested coverage.

Rejected with rationale (15 of 26): two "critical" claims disproven by
direct evidence (the Roundup loop already implements the 4-decimal spec
steps — 5 NVD-verified scores are the proof; the offline claim is accurate
because the urllib import is function-local inside `osv_online`, and the
socket-isolation test passes); fabricated references ("non-existent
scripts/bom_scan.py check"); misread code (exit codes already match the
contract; the CVSS unit tests already exist; the online payload already
builds a strict dict; osv_online already returns None on error and is
already mode-gated); documented-by-design behaviors (no_vector => high is
conservative and documented in references/triage.md; requirements.txt
complex specs are excluded with an explicit warning, by design; no-retry
online policy is documented in references/online_protocol.md); and
out-of-scope enhancements (multi-module POM recursion, retry/backoff,
prerelease-range extensions) noted for future versions.

Also caught during local testing: a "clean" test fixture that was not
actually clean (requests 2.32.5 and urllib3 2.6.1 really are below
verified fixed versions — the scanner was right, the fixture was wrong),
and a wrong path in references/advisories_format.md (tools/ -> scripts/).

## v1.0.8 (2026-08-06) — README-only documentation remediation
- README regenerated from the installed SKILL.md body; tree hash added.
  No functional artifact file changed. (The functional gap itself — no
  scanner shipped — remained and is fixed in v2.0.0.)
