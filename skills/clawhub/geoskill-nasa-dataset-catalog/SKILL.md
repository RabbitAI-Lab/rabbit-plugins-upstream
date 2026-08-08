---
name: nasa-dataset-catalog
description: 'Search, browse, and download 52K+ NASA Earth science datasets. Combines the opengeos/NASA-Earth-Data offline catalog with live CMR / LP DAAC earthdata cloud / GES DISC endpoints. Supports offline search, online granule search, single-granule download with bearer token, and --qa sidecar.'
---

# nasa-dataset-catalog

Search, browse, and download 52,126 NASA Earth science datasets. Built
on top of the offline catalog from
[opengeos/NASA-Earth-Data](https://github.com/opengeos/NASA-Earth-Data)
+ live NASA services (CMR, LP DAAC earthdata cloud, GES DISC).

## Quick start

```bash
# 0. (one-time) Put your Earthdata bearer token in ~/.geoskill/secrets.json
#    — see "Credentials" below
python scripts/nasa_dataset_catalog.py auth
#    [OK] EARTHDATA_USERNAME      source=user_secrets available=True
#    [OK] EARTHDATA_PASSWORD      source=user_secrets available=True
#    [OK] EARTHDATA_TOKEN         source=user_secrets available=True

# 1. Catalog coverage
python scripts/nasa_dataset_catalog.py stats
#    Offline catalog: .../nasa_catalog.json
#      total records       : 52,126
#      with bbox           : 47,628
#      with DOI            : 22,237
#      unique short_names  : 50,763

# 2. Search offline catalog (52K records) by keyword
python scripts/nasa_dataset_catalog.py search MOD11A1
python scripts/nasa_dataset_catalog.py search precipitation --provider GES_DISC

# 3. Search live CMR (network)
python scripts/nasa_dataset_catalog.py search MOD11A1 --live

# 4. Get detailed metadata for a short_name
python scripts/nasa_dataset_catalog.py info MOD11A1

# 5. Find granules for a time + bbox
python scripts/nasa_dataset_catalog.py granules MOD11A1 \
  --version 061 --temporal 2024-06-01,2024-06-02 \
  --bbox 115 39 117 41

# 6. Download a single granule (uses bearer token)
python scripts/nasa_dataset_catalog.py download \
  --short-name MOD11A1 --version 061 \
  --temporal 2024-06-01,2024-06-01 --bbox 115 39 117 41 \
  --output MOD11A1_day153.hdf
```

## Subcommands

| Subcommand | Purpose | Network |
|---|---|---|
| `auth` | Show current credential state (source only) | No |
| `search` | Search by keyword (offline catalog and/or live CMR) | Optional |
| `info` | Show metadata for a short_name (offline first, then live) | Optional |
| `granules` | List granules for a short_name in a temporal/bbox window | Yes |
| `download` | Download a single granule by URL or short_name+bbox+temporal | Yes |
| `stats` | Show catalog coverage stats | No |

## Common options (per subcommand)

- `--format {text,json}` — output format (default `text`; `json` for piping)
- `--qa PATH` — write a JSON run-summary sidecar to `PATH` (mirrors Phase 5 `--qa` convention)
- `--limit N` (search / granules) — max results

## Credentials

This skill authenticates with **NASA Earthdata Login** (covers all EOSDIS
data centers: LAADS, GES DISC, LP DAAC, ASF, NSIDC, CMR, AppEEARS, Worldview).

Resolution order (first non-empty wins):

1. Environment variables (`EARTHDATA_USERNAME` / `EARTHDATA_PASSWORD` /
   `EARTHDATA_TOKEN` / `FIRMS_MAP_KEY` / `OPENAI_API_KEY` / `CMA_API_KEY` /
   `EOG_USERNAME` / `EOG_PASSWORD`)
2. `~/.geoskill/secrets.json` (user-level, **not** vendored into the skill)
3. `~/.netrc` entries
4. Skill defaults (geoskill-core `_DEFAULTS`)

For a one-time setup, write to `~/.geoskill/secrets.json`:

```json
{
  "EARTHDATA_USERNAME": "ruiduobao",
  "EARTHDATA_PASSWORD": "Ruiduobao123",
  "EARTHDATA_TOKEN": "eyJ0eXAiOiJKV1Q..."
}
```

You can generate a bearer token at
<https://urs.earthdata.nasa.gov/profile> (Generate Token button). The
`EARTHDATA_TOKEN` is preferred for CMR / LP DAAC earthdata cloud / GES DISC
because it's safer than embedding username/password on the command line.

## How it works

### Offline catalog

The bundled `data/nasa_catalog.json` (42.7 MB) contains **52,126 NASA Earth
science dataset records** with metadata: short_name, entry_title, DOI,
concept-id, provider-id, s3-links, bbox, horizontal_res, start/end time,
creator, publisher, version, linkage. Sourced from
<https://github.com/opengeos/NASA-Earth-Data/blob/main/nasa_earth_data.py>
which uses `earthaccess.search_datasets(keyword="*")` (CMR).

### Live CMR

Uses the public CMR REST API (`/search/granules.json` +
`/search/collections.json`) to look up real-time granule listings and
download URLs.

### Download

Single-granule download with `requests.Session` + bearer token header.
Supports `--max-bytes` for testing/demo (download only the first N bytes).

## Why a new skill

The `opengeos/NASA-Earth-Data` repo provides the *list* of NASA datasets
but no download mechanism. The `modis-product-search` skill only searches
MODIS products. The `satellite-search` skill searches satellite parameters.
None of the existing 40 skills provides a unified 52K-catalog search +
live CMR granule lookup + token-based download.

This skill fills that gap and is intentionally small / focused (one file,
<800 LOC, 6 subcommands).

## Endpoints used

| Service | URL | Auth |
|---|---|---|
| CMR collection search | `https://cmr.earthdata.nasa.gov/search/collections.json` | optional |
| CMR granule search | `https://cmr.earthdata.nasa.gov/search/granules.json` | optional |
| LP DAAC earthdata cloud | `https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/...` | **bearer token** |
| GES DISC data | `https://data.gesdisc.earthdata.nasa.gov/data/...` | **bearer token** |
| LAADS archive (legacy) | `https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/...` | basic auth (CMR-search is preferred) |

## Examples

### Search offline catalog for GPM precipitation products
```bash
python scripts/nasa_dataset_catalog.py search GPM --provider GES_DISC --limit 10 --format json | jq
```

### Find MOD11A1 granules over Beijing on 2024-06-01
```bash
python scripts/nasa_dataset_catalog.py granules MOD11A1 \
  --version 061 --temporal 2024-06-01,2024-06-01 \
  --bbox 115 39 117 41 --list-urls beijing_mod11a1.json
```

### Download first 1 MB of a MOD11A1 tile (testing)
```bash
python scripts/nasa_dataset_catalog.py download \
  --short-name MOD11A1 --version 061 \
  --temporal 2024-06-01,2024-06-01 --bbox 115 39 117 41 \
  --output test.hdf --max-bytes 1048576
```

### Pipeline: search → info → granules → download with QA
```bash
python scripts/nasa_dataset_catalog.py search MOD11A1 --qa run.qa.json
python scripts/nasa_dataset_catalog.py info MOD11A1 --qa run.qa.json
python scripts/nasa_dataset_catalog.py granules MOD11A1 --version 061 \
  --temporal 2024-06-01 --bbox 115 39 117 41 --list-urls urls.json --qa run.qa.json
python scripts/nasa_dataset_catalog.py download --short-name MOD11A1 \
  --version 061 --temporal 2024-06-01 --bbox 115 39 117 41 \
  --output mod11a1.hdf --qa run.qa.json
```

## Exit codes

Per geoskill-core convention §2.2:
- 0 = success
- 2 = argument error
- 3 = missing dependency (e.g. `requests`)
- 4 = network / rate-limit
- 5 = no match
- 6 = data validation failure
- 7 = processing failure
- 130 = user interrupt (Ctrl-C)

## Limitations

- 52K offline catalog is a snapshot; live CMR is authoritative for new datasets
- `--max-bytes` truncates the download; full downloads need `--max-bytes 0` or omit
- LP DAAC earthdata cloud URLs require *both* bearer token and (in some
  cases) an OAuth flow with `application/x-www-form-urlencoded` redirect
  handling — `requests` follows the 302 redirect automatically
- Granule size estimates come from CMR `granule_size` field (MB) and may
  differ from actual on-disk size

## Tests

23 tests, all PASSED:

- Catalog loading + normalize_record + search_catalog (offline, no network) — 8
- Catalog stats + URL extraction — 4
- Live CMR search (MOD11A1) + Live CMR collections — 2 (skipif no token)
- Real download of first 1 MB of MOD11A1 HDF — 1 (skipif no token)
- CLI smoke tests (`auth`, `stats`, `search`, `info`, `granules`, `download`,
  `--qa` sidecar, `--help`, `--version`) — 8

```bash
cd nasa-dataset-catalog
python -m pytest --tb=short
# ============================= 23 passed in ~10s ==============================
```

## Versioning

- 0.1.0 (2026-07-27) — Phase 7.5 initial release. 6 subcommands, 23 tests,
  52K offline catalog, CMR + LP DAAC + GES DISC integration.

## License

MIT. Bundled `data/nasa_catalog.json` is from
<https://github.com/opengeos/NASA-Earth-Data> (MIT).
