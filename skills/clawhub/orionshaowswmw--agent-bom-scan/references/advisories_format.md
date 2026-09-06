# References: Advisory DB format & extension (load when extending data/advisories.yaml)

The embedded DB is a **curated subset** — every record is verified against
OSV.dev before it enters the file. It is the skill's long-term memory:
versioned, hash-stamped, and cited in every offline finding.

## Format (parsed by scripts/bom_scan.py, no external deps)
One record per block. `#` lines are comments. Header keys:
`schema`, `db_version`, `record_count`, `source`.

```
=== <advisory_id>
package: <registry name; Maven = group:artifact>
ecosystem: npm | PyPI | Maven | Go | Cargo | RubyGems | Packagist
range_type: semver | ecosystem
introduced: <version | 0 | *>
fixed: <version | *>
aliases: CVE-...,GHSA-...     (comma list, or -)
cvss_vector: CVSS:3.1/...     (or NONE -> severity defaults to high, flagged)
summary: <one line, max 140 chars>
```

Semantics: affected = `introduced <= version < fixed`. `introduced: 0` or `*`
= from the beginning. `fixed: *` = never fixed (still vulnerable).

## Adding a record (protocol)
1. Verify FIRST via OSV.dev:
   `POST https://api.osv.dev/v1/query {"package":{"name":...,"ecosystem":...},"version":<suspected>}`
   Take the id, aliases, ranges (first affected[].ranges[0].events), and the
   CVSS_V3 vector from the response. **Never write an advisory from memory.**
2. Cross-check the vector's score against the CVSS 3.1 formula (the scanner
   computes it; NVD is the tie-breaker reference).
3. Append the block, bump `db_version` (date), update `record_count`.
4. Re-run `python3 scripts/bom_scan.py check` and the self-test.
5. Record the change in CHANGELOG.md with the OSV evidence (id + date).

## Rules
- Never delete a record without annotation (withdrawn records keep their
  block with `summary: WITHDRAWN ...`).
- No secrets, no internal URLs, no package data beyond the advisory fields.
- The DB hash (sha256) travels with every offline finding — that is the
  chain of custody.
