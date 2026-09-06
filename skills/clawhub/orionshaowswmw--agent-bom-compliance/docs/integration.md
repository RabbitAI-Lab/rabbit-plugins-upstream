# Integration — wiring bomscan into agents & CI

Everything is stdout-JSON + exit codes: no config files, no daemons.

## Contracts (stable `schema` field on every payload)

| Schema | Producer | Key fields |
|---|---|---|
| `agent_bom.doctor.v1` | doctor | spec, ruleset, controls, supported_manifests |
| `agent_bom.sbom.v1` | sbom -o | out path, component count |
| `agent_bom.scan.v1` | scan | summary, verdict, fail_severity, findings[] |
| `agent_bom.report.v1` | report | verdict, summary, sbom synopsis, report_sha256 |
| `agent_bom.trend.v1` | trend | open_prev/now, net, direction, verdicts |
| `agent_bom.audit.v1` | audit | entries or chain_ok/bad_lines |

Parse rule: **trust `schema`, read documented fields only**, and branch on
exit codes, not message text.

## Exit-code matrix (branch on these)

| rc | scan/report | trend | audit --verify | sbom/doctor |
|---|---|---|---|---|
| 0 | pass (PASS/WARN) | improved/unchanged/insufficient-history | chain ok | ok |
| 1 | — | **REGRESSED** | — | — |
| 2 | usage / registry trip | usage | usage | usage |
| 3 | DIR/env error | DIR/env error | DIR/env error | DIR/env error |
| 4 | **verdict FAIL** (or chain break) | — | **chain broken** | — |

## Agent recipes

**Pre-commit posture check for a skills repo**

    python3 scripts/bomscan.py scan . --fail-severity MEDIUM && echo gate-passed

**Self-improving loop signal** (the pattern the owning agent uses):

    python3 scripts/bomscan.py report .  >/dev/null   # findings → fix
    # ... apply remediations ...
    python3 scripts/bomscan.py report .  >/dev/null
    python3 scripts/bomscan.py trend  .               # expect direction: IMPROVED

If `direction != IMPROVED` after a remediation round, re-emit `scan` JSON and
let the agent re-plan from the new finding set — `report` history guarantees
the agent compares against a tamper-evident baseline, not its own memory.

**SBOM hand-off to CVE scanners (offline → online boundary)**

    python3 scripts/bomscan.py sbom . -o sbom.json
    # elsewhere / later / on a machine with network:
    #   trivy sbom sbom.json   ·   grype sbom:sbom.json   ·   osv-scanner --sbom=sbom.json

The skill deliberately ends at generation; vulnerability matching is an
online concern outside its network-free policy.

## Environment variables

| Var | Default | Purpose |
|---|---|---|
| `AGENT_BOM_AUDIT` | `<DIR>/.agent_bom_audit.jsonl` | relocate the audit ledger (e.g. central compliance dir; keep mode 0600) |

## Consuming secrets-rule output safely

SEC-01 evidence carries **zero characters** of the match — title shows only
`[REDACTED len=N sha256:TAG]` (TAG correlates identical finds across files)
plus `evidence.file`/`evidence.line`. Routing a finding to a ticket with those
fields is safe; never open the file and quote the raw line into chat.

## Audit-progress integration

`audit --verify` proves existing ledger records are unmodified/unreordered.
The chain is **keyless**: a fully local attacker can truncate the tail or
append consistent forgeries — to close that, snapshot the head hash
(`tail -1 ledger | sha256sum`) into CI artifacts after each gate. Ledger
records carry a monotonic `seq` for gap-spotting. `AGENT_BOM_AUDIT` relocates
the ledger; point it only at paths you own.

## Multi-model / distributed review note

This v2 was reviewed by multiple AI providers before publish (4 expert lenses;
adopt/reject ledger in `docs/evidence.md`). The suite
(`bash scripts/selftest.sh`, 34 checks) is the arbiter: **code beats prose** —
any model's suggested change is merged only if all 34 checks stay green.

## Multi-model / distributed review note

This v2 was reviewed by multiple AI providers before publish. The suite
(`bash scripts/selftest.sh`, 26 checks) is the arbiter: **code beats prose** —
any model's suggested change is merged only if all 26 checks stay green.
