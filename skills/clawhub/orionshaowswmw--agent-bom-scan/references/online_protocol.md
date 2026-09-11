# References: Online mode protocol (load when --mode online is requested)

Online mode adds full OSV.dev coverage on top of the offline curated DB.
It is **off by default** and requires an explicit `--mode online`.

## Endpoint (only one)
- `POST https://api.osv.dev/v1/querybatch` — batched, one request for all
  packages (cap 40, 20 s timeout). Single fallback: `POST /v1/query`.

## Data minimization (what leaves the machine)
Per package, ONLY: `name`, `version`, `ecosystem`.
Never sent: file paths, lockfile contents, source code, hashes, credentials,
hostnames, report text.

## Maven coordinates
Maven package names must be `group:artifact` (e.g.
`org.apache.logging.log4j:log4j-core`). Bare artifact names will not match.

## Response handling
- `results[i].vulns[]` aligns with the query order.
- Each finding carries the OSV id as `advisory_id` and `source: osv_online`.
- `MAL-` prefixed ids are **malicious package** records (OpenSSF feed):
  severity forced to high, `malicious_package: true`.
- On network error: `online_error=<type>` on stderr, offline findings remain
  valid, exit code reflects offline results only. Log it:
  `python3 tools/bom_improve.py log --event online_error --area online --context "<type>"`

## Limits
- Max 40 package queries per scan (largest BOMs first by lockfile order).
- No retries, no other endpoints, no uploads, no telemetry.
- OSV.dev aggregates 30+ sources (GHSA, PYSEC, RustSec, Go vulndb, distro
  feeds). Ecosystem-native ranges => fewer false positives than CPE matching.
