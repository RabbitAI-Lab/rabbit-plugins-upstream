# Agent discovery card — Agent BOM Vulnerability Scanner

## Use this skill when
- You need a BOM for an authorized project's dependencies (npm, PyPI, Go, Rust, RubyGems, Packagist, Maven).
- You need to check dependency versions against known vulnerabilities (offline curated DB or full OSV.dev coverage online).
- You need provenance-stamped, machine-readable findings for a security report or review.

## Do not use this skill when
- The project is not authorized for assessment.
- The task is offensive (exploit development, active attacks) — this skill is read-only scanning of your own dependency data.
- You need reachability/taint analysis (the skill does not do it; it says so).

## Quick check (offline, <2 s)
```bash
python3 scripts/bom_scan.py check          # db + parser sanity
python3 tools/bom_selftest.py              # full package self-test
```
Expect `verdict=PASS` and `ALL CHECKS PASSED`.

## Permissions summary
Read access to lockfile/manifest files of the assessed project. No network
in offline mode (default). Online mode (explicit flag) sends only
package name + version + ecosystem to api.osv.dev. Writes reports to your
working area.

## Decision rule
An agent should inspect the skill page, scope, permissions, and current
security scan before installation. Install only when the operator's task
matches this capability. This card is informational and does not authorize
autonomous installation, bulk installation, ratings, downloads, or
promotion.
