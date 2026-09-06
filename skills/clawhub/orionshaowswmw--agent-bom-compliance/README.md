# agent-bom-compliance v2.0.1

**Offline SBOM + verifiable compliance scanner for agent projects.** One
python3 stdlib script (`scripts/bomscan.py`), zero network, zero install.

| Capability | v1.0.10 (old) | v2.0.0 (this) |
|---|---|---|
| SBOM generation | claimed, not implemented | ✅ CycloneDX 1.5 JSON from npm/pip/pyproject/go manifests; deduped unique bom-refs; PEP-508 env-markers stripped |
| Compliance checks | claimed 7 frameworks, no code | ✅ 6-rule curated engine, cited to OWASP LLM 2025 / Agentic / NIST SSDF / CISA |
| Secret detection | — | ✅ pattern scan, **zero-character redaction** (`[REDACTED len=N sha256:TAG]`) |
| Policy gating | — | ✅ `--fail-severity` → exit-code contract (0/1/2/3/4) |
| Auditability | README self-hash ritual only | ✅ hash-chained JSONL audit (O_NOFOLLOW, atomic 0600, `seq` gap-spotting) + `audit --verify` |
| Self-improvement | — | ✅ `trend` diff vs previous audited run (REGRESSED → rc 1) |
| Anti-hallucination | fake verification_hash | ✅ control refs limited to static registry; engine hard-fails otherwise |
| Network/telemetry | — (nothing ran at all) | ✅ none, enforced by stdlib-only import guard in selftest |

## Quickstart

    python3 scripts/bomscan.py doctor                 # env + ruleset + control registry
    python3 scripts/bomscan.py sbom  . -o sbom.json   # full CycloneDX 1.5 document
    python3 scripts/bomscan.py scan  .                # findings JSON (rc 4 on FAIL@HIGH)
    python3 scripts/bomscan.py report . -o rep.json   # verdict + audit-chain entry
    python3 scripts/bomscan.py trend  .               # IMPROVED/UNCHANGED/REGRESSED
    python3 scripts/bomscan.py audit  . --verify      # tamper-evident chain proof
    bash    scripts/selftest.sh                       # 34 offline checks

## Exit codes (the machine contract)

| rc | meaning |
|---|---|
| 0 | ok / policy pass (PASS or WARN below fail-severity) |
| 1 | `trend` REGRESSED |
| 2 | usage error (includes ruleset registry self-check trip) |
| 3 | target/environment error |
| 4 | policy FAIL (verdict FAIL at `--fail-severity`) or audit chain broken |

## Verdict ladder

`FAIL` = any finding at/above `--fail-severity` (default HIGH) · `WARN` = any
MEDIUM+ below it · `PASS` = clean.

## Honest scope

This skill produces a **verifiable-compliance signal**. It does **not**
certify SOC 2, ISO 27001, or CMMC — those require accredited auditors, and
v1's claims to the contrary were removed. OWASP LLM citations use the **2025
Top 10** numbering (stable); a renumbered 2026 edition exists — see
`docs/evidence.md`.

## Layout

- `SKILL.md` — agent operating rules
- `scripts/bomscan.py` — the engine
- `scripts/selftest.sh` — 26 offline regression checks
- `manifest.json` — entrypoints, contracts, exit codes, policy
- `docs/operations.md` — command reference + recipes
- `docs/evidence.md` — standards research table + scope honesty
- `docs/integration.md` — agent/CI wiring
- `CHANGELOG.md` — history

License: MIT-0.
