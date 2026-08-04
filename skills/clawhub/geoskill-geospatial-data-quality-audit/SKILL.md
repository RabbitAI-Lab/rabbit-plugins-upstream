---
name: geospatial-data-quality-audit
description: >
  Unified geospatial data quality audit for GIS data packages. Checks raster,
  vector, table, NetCDF, and directory structure. Outputs JSON/HTML reports,
  issue layers, checksums, and machine-readable exit codes. Use when the user
  wants to validate data packages, check delivery quality, find CRS/nodata/
  geometry issues, or generate QA reports.
---

## Prerequisites / 先准备 X 文件

> ⚠️ **必读** — 本 skill 不属于即用型，需要先准备特定文件才能跑。

本 skill 不下载数据，只审计你给的 **本地数据目录**。

👉 完整教程见仓库根目录 `PREREQUISITES.md` 2.3 节。

**先准备 X 文件**：随便指一个 GIS 数据目录就能跑。

快速试跑命令：

```bash
python geospatial_data_quality_audit.py /path/to/your/data --html --issues-geojson
```


# Geospatial Data Quality Audit

> ⚠️ **本 skill 不下载数据**。它只审计本地 `input_dir` 下的文件。
> `--bbox` / `--aoi-file` 接口仅为上下文记录 (写到 `output-manifest.json`)，不会触发任何下载。

Unified QA tool for GIS data packages. Recursively discovers geospatial files, runs per-file and cross-file checks, and produces structured reports.

## Trigger

Use when the user wants to:
- Check/validate a directory of spatial data
- Find CRS, nodata, geometry, encoding issues
- Generate QA reports (JSON/HTML) for data delivery
- Verify cross-file consistency (CRS, extent, resolution)
- Produce checksums or issue layers

## Boundaries

- Read-only by default (`--fix-safe` not implemented in this version)
- Does not modify source data
- Does not download external data
- Compliance/certification conclusions require human review

## CLI Usage

```bash
# Basic audit
python scripts/geospatial_data_quality_audit.py /path/to/data

# With HTML report and issues GeoJSON
python scripts/geospatial_data_quality_audit.py /path/to/data --html --issues-geojson

# Custom rules
python scripts/geospatial_data_quality_audit.py /path/to/data --rules rules.json

# Fail on warnings too
python scripts/geospatial_data_quality_audit.py /path/to/data --fail-on warning

# Non-recursive with checksums
python scripts/geospatial_data_quality_audit.py /path/to/data --no-recursive --checksums
```

## Arguments

| Argument | Description |
|---|---|
| `input_dir` | Directory to audit (required) |
| `--output-dir, -o` | Output directory (default: `<input>/qa-output`) |
| `--rules` | Custom rules JSON file |
| `--no-recursive` | Don't recurse into subdirectories |
| `--html` | Generate HTML report |
| `--issues-geojson` | Generate spatial issues GeoJSON |
| `--checksums` | Generate MD5 checksums file |
| `--fail-on` | Fail on `error` (default) or `warning` |
| `--sample-size` | Max files to check (0=all) |

## Output

| File | Description |
|---|---|
| `qa-report.json` | Full JSON report with all findings |
| `qa-report.html` | Human-readable HTML report (with `--html`) |
| `qa.json` | Summary: score, error/warning counts |
| `spatial_issues.geojson` | Point layer of spatial issues (with `--issues-geojson`) |
| `checksums.txt` | MD5 checksums (with `--checksums`) |
| `output-manifest.json` | Machine-readable manifest |

## Exit Codes

| Code | Meaning |
|---|---|
| 0 | All checks pass (or only warnings) |
| 2 | Argument error |
| 3 | Dependency missing |
| 6 | Data validation failure (errors found) |
| 7 | Processing failure |

## QA Score

`score = max(0, 100 - errors * 10 - warnings * 2)`

## Supported Formats

- **Raster**: GeoTIFF, IMG, ASC, GRD
- **Vector**: Shapefile, GeoJSON, KML, GML, GPKG, GPX
- **Table**: CSV, TSV, Parquet, Excel
- **NetCDF**: NC, NC4, HDF, HDF5
- **LAS**: LAS, LAZ (basic checks)
- **Document**: DOCX, PDF, MD (basic checks)

## Rule Engine

Built-in rules cover file readability, CRS presence, nodata, geometry validity, encoding, companion files, and cross-file consistency. Custom rules via JSON config extend with size limits, required CRS, and forbidden extensions.

See `references/rules.md` for full rule catalog.

## Workflow

1. Recursively discover geospatial files (skip hidden/cache dirs)
2. Detect file type from extension + content sniff
3. Run per-file checks (type-specific)
4. Run cross-file consistency checks
5. Apply rule engine (built-in + custom)
6. Generate reports and exit with appropriate code

## Dependencies

- Pure Python stdlib for basic checks
- `rasterio` (optional) for deep raster checks
- `fiona` (optional) for deep vector checks
- `netCDF4` (optional) for deep NetCDF checks
- Missing optional deps produce warnings, not errors
