# Changelog

## 2.0.1 (2026-09-06)

- `scripts/selftest.sh` — the version-sync check now tolerates `skill-card.md`
  being absent from the **installed** payload (ClawHub consumes the card for
  the registry page and does not ship it in the install archive); the check
  still enforces it when present in a source checkout. Discovered by running
  the 34-check suite against the registry-installed artifact: 34/34 both in
  source layout and installed layout.

## 2.0.0 (2026-09-06) — full functional rewrite

v1 (1.0.x) shipped **zero functional content**: a 1.6 KB SKILL.md whose entire
instruction was "Follow the skill instructions to use this skill", a README
padding a TREE-SHA256 self-hash ritual, no scripts at all — while claiming
OWASP/NIST/SOC2/ISO27001/CMMC/EU-AI-Act "compliance" and "SBOM generation".
v2.0.0 replaces the shell with a real, offline, verifiable engine.

**Added**
- `scripts/bomscan.py` — stdlib-only python3 (no pip, no network, no telemetry).
- `sbom` — CycloneDX 1.5 JSON (ECMA-424 shape: bomFormat/specVersion/version/
  serialNumber urn:uuid/metadata.component/components[] with purls/dependencies
  graph) from `package.json` (+`package-lock.json` locked versions),
  `requirements.txt` (env-markers stripped so purls stay valid), PEP-621 +
  Poetry `pyproject.toml`, and `go.mod` (require lines & blocks). bom-refs are
  deduped across manifests (CycloneDX uniqueness) with a collision-safe
  `root:name@version` root ref; output-write failures exit 3 honestly.
- `scan` — curated rule engine:
  - `SEC-01` committed-secret patterns (OpenAI/GitHub/Slack/AWS/GCP/private-key
    blocks); **zero-character redaction** — findings carry only
    `[REDACTED len=N sha256:TAG]`, never any character of the match.
  - `DEP-01` unpinned dependencies: npm exact-`x.y.z`-only pinning (ranges,
    `*`, tags, `git:`/`file:`/workspace all unpinned), pip lines without `==`
    (PEP-508 env-markers handled), and PEP-621/Poetry pyproject deps via the
    SBOM parser itself (single source of truth).
  - `NET-01` declared-vs-actual egress drift (schemes http/https/ftp/sftp/ssh/
    git/ws/wss **plus IP-literal URLs** vs SKILL.md
    `metadata.network.outbound`; boundary-safe host match
    `u==h or u.endswith("."+h)` — a declared `example.com` never blesses
    `badexample.com`; `outbound:[*]` collapses to "nothing declared").
  - `MODEL-01` model artifacts (.gguf/.safetensors/.bin/.pt/.ckpt/.onnx/.h5)
    without declared provenance.
  - `LIC-01` LICENSE presence (incl. licence/COPYING variants).
  - `GO-01` go.mod `replace`/`retract` directives (local-path forks =
    supply-chain redirect).
- Findings carry `control_refs` into a **static CONTROL_REGISTRY** (OWASP LLM
  Top 10 **2025 edition**, OWASP Agentic AI AG04/AG07, NIST SSDF SP 800-218
  PW.4/PS.3, CISA minimum SBOM elements). The engine **hard-fails (rc 2)** if
  any emitted ref is not in the registry — hallucinated control citations are
  impossible by construction; the selftest asserts it end-to-end.
- `report` — combined verdict (`PASS/WARN/FAIL`), `--fail-severity` policy gate
  (rc 4 on FAIL), `report_sha256`, sidecar full SBOM, and a **hash-chained
  audit JSONL** append per run: created with `O_NOFOLLOW` (no symlink swaps),
  mode 0600 set atomically via `fchmod` at create (no looser-perm window), and
  a monotonic `seq` per record for forensic gap-spotting. Keyless-chain limits
  (append/truncate under full local compromise) are documented, not hidden.
- `trend` — deltas vs the previous audited run for the same target:
  IMPROVED / UNCHANGED / REGRESSED (rc 1) — the self-improving feedback signal.
- `audit --verify` — recomputes the chain, rc 4 + `bad_lines[]` on tamper.
- `doctor` — environment + ruleset + full control-registry dump as JSON.
- JSON contracts `agent_bom.{doctor,sbom,scan,report,trend,audit}.v1`;
  exit-code map in `manifest.json`.
- `scripts/selftest.sh` — 34 offline checks (schema shape, bom-ref uniqueness,
  env-marker stripping, severity counts, zero-char redaction incl. 8-char
  window scan, NET-01 boundary + IP-literal + host/IP split, policy
  downgrade/INFO trip, remediation→PASS, trend IMPROVED/REGRESSED, chain
  tamper detection with surgical JSON edit, seq monotonicity, rc3 coverage on
  missing dir/unwritable outputs, binary/zero-byte robustness,
  stdlib/no-network import guard, version sync). 34/34 PASS.
- Post-implementation **distributed multi-provider review** (4 expert lenses):
  13 findings adopted (see `docs/evidence.md` adjudication ledger), 8 rejected
  with reasons.
- Docs: `docs/operations.md` (command reference + recipes),
  `docs/evidence.md` (standards research table + honest scope),
  `docs/integration.md` (agent/CI wiring against contracts).

**Removed**
- v1's TREE-SHA256 self-verification ritual, fake `verification_hash`
  frontmatter, emoji-in-`name` frontmatter, and every certification-grade claim.

**Honest scope**: this is a *verifiable-compliance signal*, not SOC2/ISO27001/
CMMC certification. OWASP LLM citations follow the **2025** Top 10 numbering;
a 2026 renumbered edition exists (see `docs/evidence.md`).

## 1.0.10
- Pre-rewrite marketing shell; no executable content. Kept for history only.
