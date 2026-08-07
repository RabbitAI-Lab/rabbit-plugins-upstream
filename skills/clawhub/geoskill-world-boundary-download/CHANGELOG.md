# Changelog

All notable changes to the `world-boundry-download` skill are documented here.

## [0.1.1] - 2026-07-21

### Fixed
- Default output filename for `region` subcommand no longer contains the
  duplicated `_clipped` suffix (e.g. `CHN_ADM1_clipped.geojson` instead of
  `CHN_ADM1_clipped_clipped.geojson`).
- Default output filename for `multi` subcommand no longer contains the
  duplicated ISO list (e.g. `multi_ADM0_CHN-JPN-KOR.geojson` instead of
  `multi_ADM0_CHN-JPN-KOR_CHN-JPN-KOR.geojson`).
- Default output filename now embeds the data source when it is not the
  default `geoboundaries` (e.g. `CHN_ADM0_natural_earth.zip`,
  `CHN_ADM1_gadm.zip`). This prevents silent overwrites when the same
  ISO/level is downloaded from different data sources in one session.
- `format.read_input` no longer crashes on directory inputs (e.g. the
  extracted SHP set from GADM). It now finds the `.shp` inside.
- `format._looks_like_zip` no longer fails on directory paths.
- GADM URL pattern corrected: per-level URLs (`gadm41_{ISO}_{N}.zip`) do
  not exist; GADM 4.1 distributes one country-wide zip with all levels,
  so we download it once and extract the requested level.
- Natural Earth URL corrected: requires a `cultural` sub-directory.
- Natural Earth now filters its global basemap to the requested country
  before writing output.

### Tests
- 67/67 unit + integration tests pass (16 offline + 11 geoBoundaries
  network + 5 network + 35 cache/format/geometry/iso).
- 20/20 end-to-end CLI stress test passes (multi-country, multi-level,
  multi-format, multi-source, bbox clip, simplified, all-levels,
  metadata).

## [0.1.0] - 2026-07-21

### Added
- Initial release.
- CLI with subcommands: `search`, `resolve-iso`, `list-sources`,
  `levels`, `info`, `bbox`, `country`, `region`, `multi`, `all-levels`,
  `cache-info`, `cache-clear`.
- Three data sources: `geoboundaries` (default, CC BY 4.0), `gadm`
  (non-commercial), `natural_earth` (public domain). Automatic
  fallback chain when the user does not pin a source.
- Four output formats: Shapefile (zip), GeoJSON, GeoPackage, TopoJSON.
- Country name resolution: English, Chinese aliases, ISO 2/3-letter
  codes. Fuzzy fallback via `pycountry` + alias table.
- Bbox clipping for the `region` subcommand.
- Multi-country merge for the `multi` subcommand.
- On-disk HTTP cache at `~/.cache/world-boundry-download/`.
- 67 unit + integration tests.
