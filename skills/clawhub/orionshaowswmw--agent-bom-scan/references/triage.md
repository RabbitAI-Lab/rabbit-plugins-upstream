# References: Triage & interpretation (load when reading scan output)

## The zero-assumption rule
- A finding = a version fell inside a verified advisory range. Each carries
  advisory_id, aliases, introduced/fixed, cvss_vector, source, db_hash.
- No match = `no_data` (unknown), **never** "safe". The offline DB is a
  curated subset: a clean offline verdict is NOT a clean security verdict.
  For a real clearance use `--mode online`.
- Models using this skill must not add, remove, rename, or re-severity
  findings. Interpret, cite, escalate — do not invent.

## Severity handling
- Scores are computed at runtime from the CVSS 3.1 vector (NVD-verified
  formula). Bucket: >=9 critical, >=7 high, >=4 medium, else low.
- `no_vector: true` records default to high (conservative) and are flagged.
- `malicious_package: true` (online, MAL- ids) = supply-chain compromise,
  treat as critical response regardless of score.

## Working findings
1. Sort by score (report already does). Critical/high first.
2. Reachability: is the vulnerable code path actually used? (The scanner
   does not do reachability analysis — that is a human/model judgment; mark
   it as such, never as a scanner fact.)
3. Upgrade to `fixed` (or the next safe release) when possible; record the
   change.
4. Below `--severity-floor` findings are listed with `below_floor: true` —
   never silently dropped.

## False positives & feedback
Suspected false positive? Do not edit the DB ad hoc:
`python3 tools/bom_improve.py log --event false_positive --area db --context "advisory=<id> pkg=<p>@<v> reason=..."`
then verify against OSV.dev per references/advisories_format.md before any
DB change. Missed vulnerabilities: `--event missed_vuln --area db`.

## Never
- Never claim a version is vulnerable without a range match.
- Never claim a project is secure from a clean scan.
- Never downgrade a risky task to a weaker model silently (model-resilience
  policy of the host workspace applies).
