---
name: agent-bom-compliance
description: >
  Offline SBOM + verifiable compliance scanner for agent projects: generates a
  CycloneDX 1.5 JSON SBOM from npm/pip/go manifests, audits the tree with a
  curated rule engine (committed-secret detection with redacted evidence,
  unpinned-dependency supply-chain check, declared-vs-actual network egress
  drift, model-artifact provenance, license presence), emits findings mapped to
  EXPLICIT control refs (OWASP LLM Top 10 2025, OWASP Agentic AI, NIST SSDF
  SP 800-218, CISA minimum SBOM elements), filters policy by severity, keeps a
  hash-chained tamper-evident audit trail, and trends findings across runs for
  self-improving posture. 100% stdlib python3. NO network, NO telemetry.
version: 2.0.1
category: security
topics: [sbom, compliance, cyclonedx, owasp, supply-chain, audit, security]
metadata:
  openclaw:
    emoji: "🏛️"
    requires:
      bins: ["python3"]
    network:
      outbound: []
---

# 🏛️ Agent BOM Compliance v2.0.1 — SBOM + verifiable rule engine

Honest replacement for v1's marketing shell (which shipped zero functional
content). Now: a real CycloneDX 1.5 generator, a real rule engine, real
control citations, a real audit chain. Ops detail: `docs/operations.md`.
Standards evidence/scope honesty: `docs/evidence.md`. Agent wiring:
`docs/integration.md`.

## Hard rules for the agent

1. Everything runs through `scripts/bomscan.py` (python3 stdlib only, offline):
   `doctor` · `sbom DIR` · `scan DIR` · `report DIR` · `trend DIR` ·
   `audit DIR [--verify]`. All output is JSON with `schema: agent_bom.*.v1`.
2. Exit codes are the contract: **0** ok/pass · **2** usage · **3** target/env
   error · **4** policy FAIL (verdict FAIL or broken audit chain). `trend`
   returns **1** on REGRESSED — use it in CI gates.
3. This is a **verifiable-compliance signal, not a certification**. Never tell
   a user this skill "makes them SOC2/ISO27001/CMMC compliant". Findings cite
   control refs that exist in the static registry (`doctor` lists them); the
   engine hard-fails on a hallucinated ref. Do the same: cite only refs you saw.
4. Secret findings are **redacted by construction** — zero characters of the
   matched value in output; only `[REDACTED len=N sha256:TAG]` (TAG lets you
   correlate identical finds across files). Never echo a matched secret found
   in raw file bytes back into the transcript.
5. `report` appends a hash-chained audit entry (`0600`, created with
   O_NOFOLLOW, `${AGENT_BOM_AUDIT:-DIR/.agent_bom_audit.jsonl}`).
   `audit --verify` proves existing records are unmodified/unreordered;
   rc 4 = tampered. The chain is keyless: present `tail -1` hashes out-of-band
   if you must also exclude append/truncate by a fully local attacker.
   Run `report` twice to unlock `trend`.
6. Policy is tunable: `--fail-severity` (INFO..CRITICAL, default HIGH) decides
   which severity trips rc 4. Verdict ladder: PASS / WARN / FAIL.

## Quickstart

    python3 scripts/bomscan.py sbom  . -o sbom.json     # CycloneDX 1.5 doc
    python3 scripts/bomscan.py scan  . --fail-severity HIGH
    python3 scripts/bomscan.py report . -o report.json  # + report.json.sbom.json
    python3 scripts/bomscan.py report .                 # second run feeds trend
    python3 scripts/bomscan.py trend  .                 # IMPROVED/REGRESSED/UNCHANGED
    python3 scripts/bomscan.py audit  . --verify        # chain_ok proof
    bash    scripts/selftest.sh                         # 34 offline checks

Full command reference, recipes, and the standards evidence table are in
`docs/`. Entry points + contracts: `manifest.json`.
