# Publication status & evidence - `appstore-api` package

Status: **NOT PUBLISHED** to any registry or marketplace. This repository ships
the package files together with their local verification evidence; no external
listing exists, and none is created by this repository.

Canonical package source for the prepaid-credit release; external publication is gated on a live package-mode capability response.

## Evidence bundle

| Item | Location |
| --- | --- |
| Package manifest with per-file sizes and SHA-256 digests | `manifest.json` |
| `sha256sum`-style checksums | `CHECKSUMS.txt` |
| Machine-readable facts and prohibited-claims policy | `evidence/publication-evidence.json` |

Digests are deterministic SHA-256 values over the committed bytes; regenerating
twice produces byte-identical trees (enforced by `../check_appstore.sh`).

## Local verification (must pass before any distribution decision)

```sh
bash services/social-data-skills/contracts/validate.sh
bash services/social-data-skills/catalog/check.sh
bash services/social-data-skills/catalog/package_check.sh
bash services/social-data-skills/catalog/check_appstore.sh
bash services/social-data-skills/catalog/package_check_appstore.sh
```

## What this package does not claim

- No registry or marketplace listing, download statistics, ratings, or community metrics exist for it.
- No live availability, latency, uptime, or success-rate figures are asserted anywhere; example payloads are illustrative fixtures, not captured responses.
- No official platform partnership, endorsement, license grant, or data-sharing arrangement is claimed.
- No purchase, review-submission, account, login, or other write/authenticated capability exists or is advertised; the surface is GET-only public reads.
- Route paths in this package are stable capability identifiers; public gateway exposure for this platform is issued to your workspace at onboarding.

## If publication is ever approved

1. Re-run all five validators above and attach their outputs to the approval record.
2. Regenerate the package from `catalog/catalog_appstore.json`; never edit generated files by hand.
3. Flip the status flags in `evidence/publication-evidence.json` only via regeneration, and only once a real publication event exists.
4. Keep all public statements within the verified facts recorded here; anything beyond them remains prohibited.
