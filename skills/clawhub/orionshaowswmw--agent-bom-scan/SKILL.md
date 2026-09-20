---
name: agent-bom-scan
version: 2.0.0
author: orionshaowswmw
license: MIT-0
categories: [security]
topics: [security, sbom, dependency-scanning, cve, supply-chain]
metadata: {"openclaw":{"emoji":"🔍"}}
description: BOM (bill of materials) vulnerability scanner that parses 8 lockfile formats, matches versions against an OSV-verified advisory database, and emits provenance-stamped findings. Use when auditing dependencies of an authorized project for CVEs, building an SBOM, assessing supply-chain risk, or generating a machine-readable security report. Offline by default; explicit online mode queries api.osv.dev with name+version only.
---

# Agent BOM Vulnerability Scanner v2.0.0

A deterministic BOM scanner. The script does the work; the model only
orchestrates and interprets. Every finding is provenance-stamped; nothing is
invented.

## 0. Command contracts (read this first)

| Command | Purpose | Output (stdout) | Exit |
|---|---|---|---|
| `python3 scripts/bom_scan.py scan <path> [--mode offline\|online] [--severity-floor low\|medium\|high\|critical (default: low)] [--out DIR]` | build BOM + match advisories | `mode=` `lockfiles=` `bom_packages=` `findings=` `critical=` `high=` `medium=` `low=` `actionable=` `no_data_packages=` `db_hash=sha256:...` `db_version=` `out=` `verdict=CLEAN\|FINDINGS\|ERROR` | 0 CLEAN · 10 FINDINGS · 2 usage · 3 fatal |
| `python3 scripts/bom_scan.py bom <path> [--out FILE]` | BOM only (no matching, no network) | JSON + `bom_packages=` `lockfiles=` | 0 ok · 3 fatal |
| `python3 scripts/bom_scan.py check [--db FILE]` | self-check (db parses, hash, parser sanity) | `db_hash=` `records=` `verdict=PASS\|FAIL` | 0 PASS · 3 FAIL |
| `python3 tools/bom_improve.py log --event E [--area A] [--context C]` | append one feedback event | `logged=<event>` | 0 ok · 2 usage |
| `python3 tools/bom_improve.py learn [--area A] [--limit N]` | read recent feedback | `ts= area= event= context=` lines | 0 ok |
| `python3 tools/bom_improve.py report [--out F]` | render improvement report | `report=<file> events=<n>` | 0 ok |
| `python3 tools/bom_selftest.py` | full offline package test | `PASS:` lines, ends `ALL CHECKS PASSED` | 0 pass · 1 fail |

Python 3.8+ stdlib only. No pip packages. Deterministic, sorted outputs.
Supported lockfiles: `package-lock.json` (v1+v2/v3), `requirements.txt`,
`Pipfile.lock`, `go.sum`, `Cargo.lock`, `Gemfile.lock`, `composer.json`,
`pom.xml`.

Scan output files (in `<path>/bom_scan_out/` or `--out DIR`):
`bom.json` (full BOM + warnings), `findings.json` (machine-readable findings),
`bom_report.md` (human report).

## 1. Usage (one pass)

1. Verify you are authorized to assess the project. Scope: dependency files
   only; never read source for secrets.
2. Run the scan:

```bash
python3 scripts/bom_scan.py scan /path/to/project --severity-floor high
```

3. Read the `key=value` summary. Then, and only if needed, read
   `bom_report.md` / `findings.json` from `out=`.
4. Interpret per `references/triage.md`. Cite advisory ids; never re-severity
   or invent findings.
5. Full coverage: `--mode online` (see the privacy contract in section 2
   before enabling it; protocol in `references/online_protocol.md`).

## 2. Privacy contract (honest, verifiable)

- **Offline mode (default): zero network.** The scanner does not import the
  socket layer at all in offline mode; the self-test proves a scan completes
  with the socket disabled.
- **Online mode (explicit opt-in):** sends ONLY `name`, `version`,
  `ecosystem` per package to `api.osv.dev` (batch endpoint). Never sent:
  paths, lockfile contents, source code, hashes, credentials, hostnames.
- "Local-first" means the offline curated DB (`data/advisories.yaml`,
  34 OSV-verified records). It is a **curated subset, not a full CVE
  database** — a clean offline result is *no data*, not *no vulnerabilities*.

## 3. Hard rules (hallucination guard)

- **Zero-assumption:** a finding exists only when a verified range matched.
  No match => `no_data` (unknown), never "safe".
- Every finding carries provenance: `advisory_id`, `aliases`,
  `introduced`/`fixed`, `cvss_vector` (score computed at runtime from the
  vector, CVSS 3.1, NVD-verified), `source` (`offline_db` + `db_hash`, or
  `osv_online`).
- The model must not add, remove, rename, or re-severity findings. It may
  interpret, cite, and escalate.
- CVSS scores are computed, not recalled. Never quote a score from memory.
- Malicious-package records (`MAL-` ids, online only) are flagged
  `malicious_package: true` and treated as supply-chain compromise.

## 4. Self-improvement loop (durable skill memory)

Feedback lives in local `feedback.jsonl` (never uploaded). Event vocabulary:
`false_positive · missed_vuln · db_gap · parser_gap · perf_issue ·
doc_stale · user_confusion · online_error`.

```bash
python3 tools/bom_improve.py log --event false_positive --area db --context "advisory=GHSA-... pkg=x@1.2.3 reason=range overlap"
python3 tools/bom_improve.py learn --area db
python3 tools/bom_improve.py report        # at the end of a review job
```

DB changes follow `references/advisories_format.md` (verify against OSV.dev
first, bump `db_version`, cite evidence in CHANGELOG.md). The changelog is
the long-term memory; `db_hash` in reports is the chain of custody.

## 5. Load map (progressive disclosure — read only what the task needs)

| Load when | File |
|---|---|
| always (this file) | `SKILL.md` |
| interpreting findings | `references/triage.md` |
| enabling `--mode online` | `references/online_protocol.md` |
| extending the advisory DB | `references/advisories_format.md` |
| the data itself | `data/advisories.yaml` (34 records) |
| verification | `python3 tools/bom_selftest.py` |
| test fixtures (expected results) | `tools/fixtures/` |

## 6. Verification

```bash
python3 tools/bom_selftest.py    # 12 offline check groups, ends ALL CHECKS PASSED
python3 scripts/bom_scan.py check
```

The self-test covers: hygiene, frontmatter compliance, reference integrity,
advisory-DB semantics, functional scans of vulnerable/clean fixtures with
expected advisory ids, go.sum dedupe, CVSS 3.1 against NVD-verified scores,
provenance completeness, true offline isolation (socket disabled), honest
claims, secrets, and version/hash consistency.

## 7. Versioning

`CHANGELOG.md` is authoritative. v2.0.0 is a full rebuild of the v1.x
hollow package (v1 advertised capabilities it did not implement). Registry
versions below 2.0.0 contain no working scanner — do not trust them.
