---
name: nasa-dataset-download
description: 'Download any NASA Earth observation dataset (HDF / NetCDF / GeoTIFF) end-to-end. Wraps the official earthaccess library to authenticate with NASA Earthdata Login and bulk-download granules from MODIS, VIIRS, GPM, Sentinel, SMAP, ASTER, etc. Supports BBox + temporal window filtering and QA sidecars. Default credentials are loaded from ~/.geoskill/secrets.json (NASA Earthdata bearer token). 0.2.0: alias map (description → short_name), multi-word search, --dry-run, proper exit codes (5 on 0 results), accurate --max-files, fixed granule display.'
---

# nasa-dataset-download

End-to-end download of any NASA Earth observation dataset. Built on top
of [`earthaccess`](https://github.com/nsidc/earthaccess) (NSIDC's
official Python SDK) so it handles **MODIS**, **VIIRS**, **GPM**,
**Sentinel-1**, **SMAP**, **ASTER**, **MERRA-2**, and thousands of
other NASA datasets through a uniform CLI.

## Quick start

```bash
# 0. one-time: put your Earthdata bearer token in ~/.geoskill/secrets.json
#    (or set $EARTHDATA_TOKEN in your env)
python scripts/nasa_dataset_download.py login
#    [OK] EARTHDATA_USERNAME      source=user_secrets available=True
#    [OK] EARTHDATA_TOKEN         source=user_secrets available=True
#    Attempting live login with earthaccess.login()...
#    OK: earthaccess.authenticated=True

# 1. browse the 52K offline catalog for inspiration
python scripts/nasa_dataset_download.py known MOD11A1

# 2. list available granules
python scripts/nasa_dataset_download.py search MOD11A1 \
  --version 061 --temporal-start 2024-06-01 --temporal-end 2024-06-01 \
  --bbox 115 39 117 41

# 3. download 2 granules (defaults to ./output/<short_name>/)
python scripts/nasa_dataset_download.py download MOD11A1 \
  --version 061 --temporal-start 2024-06-01 --temporal-end 2024-06-01 \
  --bbox 115 39 117 41 --max-files 2

# 4. print URLs only (no download)
python scripts/nasa_dataset_download.py urls MOD11A1 \
  --version 061 --temporal-start 2024-06-01 --temporal-end 2024-06-01 \
  --bbox 115 39 117 41 --out urls.json
```

## Subcommands

| Subcommand | Network | Purpose |
|---|---|---|
| `login` | Yes | Authenticate with Earthdata; show credential state |
| `known` | No | Browse the bundled 52K offline catalog **+ alias map** (multi-word AND search) |
| `search` | Yes | List granules for a dataset in BBox + time window. Description-style names ("land surface temperature") print an alias hint suggesting canonical short_name(s). |
| `download` | Yes | Bulk-download granules to a local directory. `--dry-run` previews; `--max-files` actually limits downloads. |
| `urls` | Yes | Print granule URLs (no download); also writes a structured JSON sidecar via `--out`. |

## Alias map (description → short_name)

`data/aliases.json` (50 entries) maps natural-language descriptions to
canonical short_names. Lets users search by what they know, not by what
they've memorized:

```bash
# user types a description, skill suggests the right short_name
python scripts/nasa_dataset_download.py known "land surface temperature"
# -> alias match: 'land surface temperature' -> MOD11A1, MOD11A2, MOD11B, MOD11_L2, ...
#    and 10 catalog records like MOD11A1 | MODIS/Terra LST/Emissivity Daily L3

# search with description also gets the hint
python scripts/nasa_dataset_download.py search "land surface temperature" --temporal-start 2024-06-01 --bbox 115 39 117 41
# stderr: hint: 'land surface temperature' matched the alias map; try the canonical short_name(s): MOD11A1, ...

# disable hinting per-invocation
python scripts/nasa_dataset_download.py search "MOD11A1" --no-alias-resolve
```

Other entries: `MODIS LST`, `surface reflectance`, `land cover`,
`vegetation index`, `NDVI`, `snow cover`, `sea ice`, `precipitation`,
`IMERG`, `GPM`, `rainfall`, `soil moisture`, `SMAP`, `SST`, `ocean color`,
`active fire`, `evapotranspiration`, `Sentinel-1`, `Landsat`, `DEM`, `ASTER`,
`LAI`, `GPP`, `ET`.

## Common options (per subcommand)

- `--format {text,json}` — output format
- `--qa PATH` — write a JSON run-summary sidecar to `PATH` (mirrors Phase 5 convention)
- `--bbox W S E N` — geographic bounding box in WGS84
- `--temporal-start YYYY-MM-DD` / `--temporal-end YYYY-MM-DD` — date range (inclusive)
- `--count N` — max results
- `--max-files N` (download only) — **actually limits downloads** (was buggy in v0.1.0)
- `--dry-run` (download only) — print what would be downloaded; no files written
- `--no-alias-resolve` (search only) — skip the alias-map hint when `short_name` looks like a description

## 0-result handling

Per geoskill-core §2.2, search returns **exit 5** when 0 granules match
(v0.1.0 silently exited 0). The error output now lists possible causes
and suggests a fix:

```
$ python scripts/nasa_dataset_download.py search NOTAREAL --temporal-start 2024-06-01 --temporal-end 2024-06-01
  no granules found. Possible causes:
    - 'NOTAREAL' may be a description, not a short_name
    - the date 2024-06-01 may be out of range for this dataset
    - try `nasa-dataset-download known "NOTAREAL"` to find a similar short_name
    - or check spelling: e.g. MOD11A1 (not MOD11A-1), GPM_3IMERGHH (not IMERG)
$ echo $?
5
```

## Credentials

This skill authenticates with **NASA Earthdata Login** (covers all
EOSDIS data centers: LAADS, GES DISC, LP DAAC, ASF, NSIDC, CMR,
AppEEARS, Worldview). Resolution order:

1. `EARTHDATA_USERNAME` / `EARTHDATA_PASSWORD` / `EARTHDATA_TOKEN` env vars
2. `~/.geoskill/secrets.json` (user-level, **not** vendored)
3. `~/.netrc` entries (`machine urs.earthdata.nasa.gov`)
4. Skill defaults

**Bearer token is preferred** for CMR / LP DAAC earthdata cloud / GES DISC
since it works with both modern (CMR-driven) and legacy endpoints.

```json
// C:\Users\<you>\.geoskill\secrets.json
{
  "EARTHDATA_USERNAME": "ruiduobao",
  "EARTHDATA_PASSWORD": "Ruiduobao123",
  "EARTHDATA_TOKEN": "eyJ0eXAiOiJKV1Q..."
}
```

Generate a bearer token at <https://urs.earthdata.nasa.gov/profile>.

## Endpoints used

| Service | URL | Auth | Datasets |
|---|---|---|---|
| CMR | `https://cmr.earthdata.nasa.gov/search/` | optional | All NASA |
| LP DAAC earthdata cloud | `https://data.lpdaac.earthdatacloud.nasa.gov/` | **bearer** | MODIS Land / SRTM / ASTER |
| GES DISC | `https://data.gesdisc.earthdata.nasa.gov/data/` | **bearer** | GPM / MERRA-2 / TRMM |
| LAADS archive (legacy) | `https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/` | basic | MODIS L1 / atmosphere |

## Validation: 10 real downloads

Verified on 2026-07-27 (Beijing BBox, 2024-06-01) — all 10 datasets
downloaded successfully via Earthdata bearer token:

| # | Dataset | Provider | Size | Format |
|---|---|---|---|---|
| 1 | MOD11A1 v061 | LP DAAC | 3.95 MB | HDF4 |
| 2 | MOD09GA v061 | LP DAAC | 173.6 MB | HDF4 |
| 3 | GPM_3IMERGHH v07 | GES DISC | 16.1 MB | HDF5 |
| 4 | MOD11A2 v061 | LP DAAC | 13.6 MB | HDF4 |
| 5 | MOD10A1 v61 | NSIDC | 17.0 MB | HDF4 |
| 6 | MOD13Q1 v061 | LP DAAC | 235.2 MB | HDF4 |
| 7 | MOD09A1 v061 | LP DAAC | 130.4 MB | HDF4 |
| 8 | GPM_3IMERGDF v07 | GES DISC | 31.95 MB | HDF5 |
| 9 | MOD14A1 v061 | LP DAAC | 0.9 MB | HDF4 |
| 10 | MOD21A1D v061 | LP DAAC | 2.6 MB | HDF4 |

**Total: 16 files, 625 MB, 148 seconds** via VPN 7897.

## Tests

23 tests (all PASSED on 2026-07-27):
- 6 catalog (offline, no network) — `test_catalog_exists`, `test_load_catalog`, `test_search_catalog_*`, `test_search_catalog_multiword*`
- 4 alias (offline) — `test_alias_map_loaded`, `test_resolve_alias_*`
- 1 granule_info (offline) — `test_granule_info_keys`
- 6 CLI smoke (no network) — `test_cli_help`, `test_cli_version`, `test_cli_login_shows_creds`, `test_cli_known_search`, `test_cli_known_qa_sidecar`, `test_cli_known_multikeyword`
- 3 CLI live (no network — pure error/hint paths) — `test_cli_search_no_match_exit5`, `test_cli_download_dry_run`
- 3 live (skipif no token) — `test_live_login`, `test_live_search_mod11a1`, `test_live_search_gpm`, `test_live_search_mod09ga`

Plus a **20-question end-to-end regression** (`.user-test/regression_test.py`)
that runs every realistic user question and asserts the expected outcome
(20/20 PASS in ~70s wall clock).

```bash
cd nasa-dataset-download
python -m pytest --tb=short
# ============================= 23 passed in ~24s =============================

python .user-test/regression_test.py
# 20/20 questions PASSED
```

## Why a new skill

The existing `modis-lst-download`, `gpm-download`, and `download-dem`
each target one product line. `nasa-dataset-catalog` searches 52K
datasets but doesn't handle bulk download well. This skill fills
both gaps:

- **Bulk download** any of the 52K NASA datasets in one command
- Uses the **official `earthaccess` SDK** (NSIDC's maintained library)
- Defaults to `~/.geoskill/secrets.json` for credentials (single place
  for all 40+ skills)

## Exit codes

Per geoskill-core §2.2: 0=success, 2=arg, 3=missing dep, 4=network,
5=no match, 6=data validation, 7=processing, 130=interrupt.

## Limitations

- AWS S3 cloud-hosted datasets (`earthaccess.search_data(cloud_hosted=True)`)
  not exposed as a separate subcommand yet — use the Python API for those
- GES DISC older URLs (`gpm1.gesdisc.eosdis.nasa.gov/opendap/`) not
  supported; use the new `data.gesdisc.earthdata.nasa.gov/data/` path
- Granule listing is hard-capped at `--count`; raise if you need more
- No retry / resume / multipart — if download fails midway, re-run
  (skips already-downloaded files via earthaccess internal cache)
- Alias map (`data/aliases.json`) has 50 entries; the offline catalog has
  52K. For unmapped descriptions, `known` falls back to multi-word AND
  search across the offline catalog and may surface false positives
  (e.g. "Sentinel-1" hits ESA Greenland records that mention sentinel in
  the title). When in doubt, the alias hint suggests canonical short_names.

## Versioning

- **0.2.0** (2026-07-27) — Phase 7.7. Alias map (50 entries) + multi-word
  AND search; fixed `search` output (`g.title` / `g.size_in_mb` /
  `g.get_umm()` were broken in earthaccess 0.18); `--max-files` now
  actually limits downloads (was reporting-only in v0.1.0); `--dry-run`
  on download; 0-result search returns exit 5 with hint; suppressed
  FutureWarning noise; JSON output now includes granule_id, size, day/night,
  production_dt, temporal range, data_links, cloud_hosted flag. 23 tests +
  20-question regression. 0 fail, 0 skip-with-fail.
- 0.1.0 (2026-07-27) — Phase 7.6 initial release. 5 subcommands, 13 tests,
  10 real-download integration tests (PASS 10/10, 625 MB across 6
  different NASA data centers).

## License

MIT. `earthaccess` is Apache-2.0. Bundled `data/nasa_catalog.json`
from <https://github.com/opengeos/NASA-Earth-Data> (MIT).
