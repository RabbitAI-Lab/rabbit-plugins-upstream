# HTTrack Integration Guide

HTTrack is the **primary fetching engine** for the entire system. Every website
fetch goes through the `httrack` CLI, wrapped by
`src/crawler/httrack_engine.py`.

## Why HTTrack

HTTrack is a free, GPL-3 open-source web crawler and offline browser by Xavier
Roche. It mirrors websites to local disk, can update existing mirrors, resume
interrupted downloads, and emit change reports.

| Layer | HTTrack role |
|---|---|
| Supplier discovery | mirrors B2B directory pages locally; link analyzer walks local files |
| Website fetching | `httrack <url> -O <path>` initial full mirror |
| Live updates | `httrack --update` downloads only changed pages |
| Change detection | `hts-changes.json` lists new/changed/unchanged/removed |
| Parsing | parser reads only local files — never the network |
| Discontinued products | files reported "removed" → products marked discontinued |
| JS fallback | Playwright renders JS pages into the same mirror directory |
| Scheduling | Celery Beat triggers `httrack --update` on 6h/24h/72h intervals |
| Docker | `apt install httrack` in the Dockerfile; persistent mirror volume |
| Rate limiting | `--connection-per-second` (fractions allowed, e.g. 0.1 = 1/10s) |

## Command reference

```bash
# initial mirror (polite, catalog-focused)
httrack "https://supplier.ir/catalog/" \
  -O "/var/lib/iran_chem_db/mirrors/supplier_name" \
  --depth=5 --ext-depth=0 --stay-on-same-domain \
  --connection-per-second=2 --sockets=4 \
  +*.html +*.htm +*.php +*.asp +*.pdf +*.xlsx +*.csv \
  -*.jpg -*.png -*.gif -*.mp4 -*.zip \
  --assume asp=text/html,php=text/html

# incremental update (only changed pages)
httrack --update -O "/var/lib/iran_chem_db/mirrors/supplier" -%X

# multiple URLs from a list file
httrack -%L urls.txt -O outdir --depth=3 --stay-on-same-domain
```

## Change detection

After an update, HTTrack writes `hts-changes.json` — the quick way to see what
an update actually did. `ChangeDetector` parses it and the parser only
re-processes "new"/"modified" files, and marks products from "removed" files as
discontinued.

## Profiles

`src/crawler/httrack_profiles.py` provides pre-built profiles: standard catalog,
PDF catalog, large database, sensitive (ultra-polite), login-required, and
`.ir` domain (UTF-8 charset).
