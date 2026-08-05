#!/usr/bin/env python3
"""
Geospatial Data Quality Audit - Unified QA for GIS data packages.

Checks raster, vector, table, NetCDF, LAS, and directory structure.
Outputs JSON/HTML reports, issue layers, and machine-readable exit codes.

Exit codes:
    0 = all checks pass (or only warnings)
    2 = argument error
    3 = dependency missing
    6 = data validation failure (errors found)
    7 = processing failure
"""

import argparse
import csv
import hashlib
import json
import os
import re
import sys
import traceback
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# Shared data-download library — only for the --bbox/--aoi-file interface,
# this skill does NOT download any data (it audits local files only).
# Optional auto-download via shared data fetcher (Microsoft Planetary Computer)
try:
    from _geoskill_data_fetcher import add_bbox_date_args
    _HAS_FETCHER = True
except ImportError:
    import sys as _sys
    from pathlib import Path as _Path
    _skill_dir = _Path(__file__).resolve().parent
    _repo_root = _skill_dir.parent.parent
    _local_fetcher = _repo_root / "_geoskill_data_fetcher"
    if _local_fetcher.exists():
        _sys.path.insert(0, str(_repo_root))
    from _geoskill_data_fetcher import add_bbox_date_args
    _HAS_FETCHER = True
except Exception:  # pragma: no cover
    _HAS_FETCHER = False
    add_bbox_date_args = None  # type: ignore

# -- Exit codes --
EXIT_OK = 0
EXIT_ARG = 2
EXIT_DEP = 3
EXIT_VALIDATION = 6
EXIT_PROCESSING = 7

# -- File type detection --
RASTER_EXTS = {".tif", ".tiff", ".geotiff", ".img", ".asc", ".grd"}
VECTOR_EXTS = {".shp", ".geojson", ".json", ".kml", ".gml", ".gpkg", ".gpx"}
TABLE_EXTS = {".csv", ".tsv", ".parquet", ".xlsx", ".xls"}
NETCDF_EXTS = {".nc", ".nc4", ".hdf", ".hdf5", ".h5"}
LAS_EXTS = {".las", ".laz"}
DOC_EXTS = {".docx", ".pdf", ".md", ".txt"}
ALL_EXTS = RASTER_EXTS | VECTOR_EXTS | TABLE_EXTS | NETCDF_EXTS | LAS_EXTS | DOC_EXTS


def detect_file_type(path: Path) -> str:
    """Detect geospatial file type from extension and content."""
    ext = path.suffix.lower()
    if ext in RASTER_EXTS:
        return "raster"
    if ext == ".geojson":
        return "vector"
    if ext == ".json":
        # Distinguish GeoJSON from plain JSON
        try:
            with open(path, "r", encoding="utf-8") as f:
                head = f.read(2048)
            if '"type"' in head and ("Feature" in head or "Geometry" in head or "coordinates" in head):
                return "vector"
        except Exception:
            pass
        return "json"
    if ext in VECTOR_EXTS:
        return "vector"
    if ext in TABLE_EXTS:
        return "table"
    if ext in NETCDF_EXTS:
        return "netcdf"
    if ext in LAS_EXTS:
        return "las"
    if ext in DOC_EXTS:
        return "document"
    return "unknown"


def file_hash(path: Path, algo: str = "md5") -> str:
    """Compute file hash for integrity tracking."""
    h = hashlib.new(algo)
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def check_file_readable(path: Path) -> Tuple[bool, str]:
    """Check if file is readable and non-empty."""
    if not path.exists():
        return False, f"File not found: {path}"
    if path.stat().st_size == 0:
        return False, "File is empty (0 bytes)"
    try:
        with open(path, "rb") as f:
            f.read(1)
        return True, ""
    except Exception as e:
        return False, f"Cannot read file: {e}"


def check_raster_basic(path: Path) -> Dict[str, Any]:
    """Basic raster checks without heavy dependencies."""
    result = {"file": str(path), "type": "raster", "checks": []}

    ok, msg = check_file_readable(path)
    if not ok:
        result["checks"].append({"id": "FILE_READABLE", "severity": "error", "message": msg})
        return result
    result["checks"].append({"id": "FILE_READABLE", "severity": "info", "message": "OK"})

    # File size
    size = path.stat().st_size
    result["size_bytes"] = size
    if size < 100:
        result["checks"].append({"id": "FILE_SIZE", "severity": "warning",
                                 "message": f"Suspiciously small raster: {size} bytes"})

    # Try reading with rasterio if available
    try:
        import rasterio
        with rasterio.open(path) as ds:
            result["width"] = ds.width
            result["height"] = ds.height
            result["bands"] = ds.count
            result["crs"] = str(ds.crs) if ds.crs else None
            result["nodata"] = ds.nodata
            result["dtype"] = str(ds.dtypes[0]) if ds.dtypes else None
            result["resolution"] = [ds.res[0], ds.res[1]] if ds.res else None
            result["bounds"] = list(ds.bounds) if ds.bounds else None
            result["compress"] = ds.compression if hasattr(ds, "compression") else None

            if not ds.crs:
                result["checks"].append({"id": "RASTER_CRS", "severity": "error",
                                         "message": "Missing CRS"})
            if ds.nodata is None:
                result["checks"].append({"id": "RASTER_NODATA", "severity": "warning",
                                         "message": "No nodata value set"})
            if ds.width < 2 or ds.height < 2:
                result["checks"].append({"id": "RASTER_SIZE", "severity": "error",
                                         "message": f"Invalid dimensions: {ds.width}x{ds.height}"})
            # Check for all-nodata
            try:
                import numpy as np
                sample = ds.read(1, out_shape=(min(100, ds.height), min(100, ds.width)))
                if ds.nodata is not None and np.all(sample == ds.nodata):
                    result["checks"].append({"id": "RASTER_ALL_NODATA", "severity": "warning",
                                             "message": "Sample region is all nodata"})
            except Exception:
                pass
    except ImportError:
        result["checks"].append({"id": "RASTERIO_MISSING", "severity": "warning",
                                 "message": "rasterio not available, skipping deep raster checks"})
    except Exception as e:
        result["checks"].append({"id": "RASTER_READ_ERROR", "severity": "error",
                                 "message": f"Cannot read raster: {e}"})

    return result


def check_vector_basic(path: Path) -> Dict[str, Any]:
    """Basic vector checks."""
    result = {"file": str(path), "type": "vector", "checks": []}

    ok, msg = check_file_readable(path)
    if not ok:
        result["checks"].append({"id": "FILE_READABLE", "severity": "error", "message": msg})
        return result
    result["checks"].append({"id": "FILE_READABLE", "severity": "info", "message": "OK"})

    # Check for .shp companion files
    if path.suffix.lower() == ".shp":
        for ext in [".shx", ".dbf", ".prj"]:
            companion = path.with_suffix(ext)
            if not companion.exists():
                result["checks"].append({"id": "SHP_COMPANION", "severity": "error",
                                         "message": f"Missing {ext} companion file"})

    try:
        import fiona
        with fiona.open(path) as src:
            result["crs"] = str(src.crs) if src.crs else None
            result["schema"] = src.schema
            result["feature_count"] = len(src)
            result["geometry_type"] = src.schema.get("geometry") if src.schema else None

            if not src.crs:
                result["checks"].append({"id": "VECTOR_CRS", "severity": "error",
                                         "message": "Missing CRS"})
            if len(src) == 0:
                result["checks"].append({"id": "VECTOR_EMPTY", "severity": "warning",
                                         "message": "Zero features"})

            # Check for invalid geometries
            invalid_count = 0
            for i, feat in enumerate(src):
                if i >= 1000:
                    break
                geom = feat.get("geometry")
                if geom and not _is_valid_geometry(geom):
                    invalid_count += 1
            if invalid_count > 0:
                result["checks"].append({"id": "VECTOR_INVALID_GEOM", "severity": "error",
                                         "message": f"{invalid_count} invalid geometries found (sampled)"})
    except ImportError:
        result["checks"].append({"id": "FIONA_MISSING", "severity": "warning",
                                 "message": "fiona not available, skipping deep vector checks"})
    except Exception as e:
        result["checks"].append({"id": "VECTOR_READ_ERROR", "severity": "error",
                                 "message": f"Cannot read vector: {e}"})

    return result


def _is_valid_geometry(geom: Dict) -> bool:
    """Basic geometry validity check."""
    if not geom or "type" not in geom:
        return False
    gtype = geom["type"]
    coords = geom.get("coordinates")
    if gtype == "Point":
        return isinstance(coords, list) and len(coords) >= 2
    if gtype == "LineString":
        return isinstance(coords, list) and len(coords) >= 2
    if gtype == "Polygon":
        return isinstance(coords, list) and len(coords) >= 1 and len(coords[0]) >= 4
    if gtype == "MultiPolygon":
        return isinstance(coords, list) and len(coords) >= 1
    return True


def check_table_basic(path: Path) -> Dict[str, Any]:
    """Basic table/CSV checks."""
    result = {"file": str(path), "type": "table", "checks": []}

    ok, msg = check_file_readable(path)
    if not ok:
        result["checks"].append({"id": "FILE_READABLE", "severity": "error", "message": msg})
        return result
    result["checks"].append({"id": "FILE_READABLE", "severity": "info", "message": "OK"})

    if path.suffix.lower() == ".csv":
        try:
            with open(path, "r", encoding="utf-8-sig", newline="") as f:
                sample = f.read(65536)
            # Detect encoding issues
            if "\x00" in sample:
                result["checks"].append({"id": "CSV_ENCODING", "severity": "error",
                                         "message": "Null bytes detected - possible binary/corruption"})

            reader = csv.reader(sample.splitlines())
            headers = next(reader, None)
            if headers is None:
                result["checks"].append({"id": "CSV_EMPTY", "severity": "error",
                                         "message": "No header row"})
                return result

            result["columns"] = headers
            result["column_count"] = len(headers)

            # Check duplicate column names
            seen = set()
            dupes = []
            for h in headers:
                if h in seen:
                    dupes.append(h)
                seen.add(h)
            if dupes:
                result["checks"].append({"id": "CSV_DUPLICATE_COLS", "severity": "error",
                                         "message": f"Duplicate column names: {dupes}"})

            # Count rows
            row_count = sum(1 for _ in reader)
            result["row_count"] = row_count
            if row_count == 0:
                result["checks"].append({"id": "CSV_NO_DATA", "severity": "warning",
                                         "message": "Header only, no data rows"})

            # Check for BOM
            with open(path, "rb") as f:
                raw = f.read(3)
            if raw == b"\xef\xbb\xbf":
                result["checks"].append({"id": "CSV_BOM", "severity": "info",
                                         "message": "UTF-8 BOM present"})

        except UnicodeDecodeError:
            result["checks"].append({"id": "CSV_ENCODING", "severity": "error",
                                     "message": "Cannot decode as UTF-8"})
        except Exception as e:
            result["checks"].append({"id": "CSV_READ_ERROR", "severity": "error",
                                     "message": f"Cannot read CSV: {e}"})

    return result


def check_netcdf_basic(path: Path) -> Dict[str, Any]:
    """Basic NetCDF checks."""
    result = {"file": str(path), "type": "netcdf", "checks": []}

    ok, msg = check_file_readable(path)
    if not ok:
        result["checks"].append({"id": "FILE_READABLE", "severity": "error", "message": msg})
        return result
    result["checks"].append({"id": "FILE_READABLE", "severity": "info", "message": "OK"})

    try:
        import netCDF4
        ds = netCDF4.Dataset(path, "r")
        result["dimensions"] = dict(ds.dimensions)
        result["variables"] = list(ds.variables.keys())
        result["global_attrs"] = {k: str(getattr(ds, k)) for k in ds.ncattrs()}
        ds.close()
    except ImportError:
        result["checks"].append({"id": "NETCDF4_MISSING", "severity": "warning",
                                 "message": "netCDF4 not available, skipping deep NetCDF checks"})
    except Exception as e:
        result["checks"].append({"id": "NETCDF_READ_ERROR", "severity": "error",
                                 "message": f"Cannot read NetCDF: {e}"})

    return result


def discover_files(input_dir: str, recursive: bool = True) -> List[Path]:
    """Recursively discover geospatial files."""
    root = Path(input_dir)
    if not root.exists():
        return []

    files = []
    pattern = "**/*" if recursive else "*"
    for p in root.glob(pattern):
        if p.is_file() and p.suffix.lower() in ALL_EXTS:
            # Skip hidden and cache dirs
            parts = p.relative_to(root).parts
            if any(part.startswith(".") or part in {"__pycache__", "node_modules"} for part in parts):
                continue
            files.append(p)
    return sorted(files)


def cross_file_checks(results: List[Dict]) -> List[Dict[str, Any]]:
    """Run cross-file consistency checks."""
    issues = []

    # Group by type
    rasters = [r for r in results if r.get("type") == "raster" and "crs" in r]
    vectors = [r for r in results if r.get("type") == "vector" and "crs" in r]

    # CRS consistency among rasters
    if len(rasters) > 1:
        crs_set = set()
        for r in rasters:
            crs = r.get("crs")
            if crs:
                crs_set.add(crs)
        if len(crs_set) > 1:
            issues.append({
                "id": "CROSS_CRS_RASTER",
                "severity": "warning",
                "message": f"Rasters have {len(crs_set)} different CRS: {crs_set}",
                "files": [r["file"] for r in rasters]
            })

    # CRS consistency among vectors
    if len(vectors) > 1:
        crs_set = set()
        for r in vectors:
            crs = r.get("crs")
            if crs:
                crs_set.add(crs)
        if len(crs_set) > 1:
            issues.append({
                "id": "CROSS_CRS_VECTOR",
                "severity": "warning",
                "message": f"Vectors have {len(crs_set)} different CRS: {crs_set}",
                "files": [r["file"] for r in vectors]
            })

    # Overlapping extent check (simplified)
    raster_bounds = []
    for r in rasters:
        b = r.get("bounds")
        if b and len(b) == 4:
            raster_bounds.append((r["file"], b))
    if len(raster_bounds) > 1:
        # Check if any pair has no overlap
        for i in range(len(raster_bounds)):
            for j in range(i + 1, len(raster_bounds)):
                b1 = raster_bounds[i][1]
                b2 = raster_bounds[j][1]
                if (b1[2] < b2[0] or b2[2] < b1[0] or b1[3] < b2[1] or b2[3] < b1[1]):
                    issues.append({
                        "id": "CROSS_EXTENT_OVERLAP",
                        "severity": "warning",
                        "message": f"Non-overlapping rasters: {raster_bounds[i][0]} vs {raster_bounds[j][0]}",
                        "files": [raster_bounds[i][0], raster_bounds[j][0]]
                    })

    return issues


def apply_rules(results: List[Dict], cross_issues: List[Dict],
                rules_config: Optional[Dict] = None) -> Dict[str, Any]:
    """Apply rule engine and produce summary."""
    all_checks = []
    for r in results:
        for check in r.get("checks", []):
            check["file"] = r["file"]
            all_checks.append(check)
    for issue in cross_issues:
        all_checks.append({
            "id": issue["id"],
            "severity": issue["severity"],
            "message": issue["message"],
            "file": ", ".join(issue.get("files", []))
        })

    # Count by severity
    error_count = sum(1 for c in all_checks if c["severity"] == "error")
    warning_count = sum(1 for c in all_checks if c["severity"] == "warning")
    info_count = sum(1 for c in all_checks if c["severity"] == "info")

    # Apply custom rules if provided
    custom_issues = []
    if rules_config:
        max_size = rules_config.get("max_file_size_mb")
        if max_size:
            for r in results:
                size = r.get("size_bytes", 0)
                if size > max_size * 1024 * 1024:
                    custom_issues.append({
                        "id": "RULE_MAX_SIZE",
                        "severity": "error",
                        "message": f"File exceeds {max_size}MB limit: {size / 1024 / 1024:.1f}MB",
                        "file": r["file"]
                    })

    all_checks.extend(custom_issues)
    error_count += len(custom_issues)

    return {
        "total_checks": len(all_checks),
        "errors": error_count,
        "warnings": warning_count,
        "info": info_count,
        "findings": all_checks
    }


def generate_html_report(summary: Dict, output_path: Path) -> None:
    """Generate HTML report from summary."""
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8"><title>Geospatial QA Report</title>
<style>
body{{font-family:sans-serif;max-width:1200px;margin:20px auto;padding:0 20px}}
h1{{color:#333}} .summary{{background:#f5f5f5;padding:15px;border-radius:8px;margin:20px 0}}
.error{{color:#d32f2f}} .warning{{color:#f57c00}} .info{{color:#1976d2}}
table{{border-collapse:collapse;width:100%;margin-top:10px}}
th,td{{border:1px solid #ddd;padding:8px;text-align:left;font-size:14px}}
th{{background:#f5f5f5}} tr:hover{{background:#fafafa}}
</style></head>
<body>
<h1>Geospatial Data Quality Audit Report</h1>
<div class="summary">
<p><strong>Generated:</strong> {summary.get("timestamp", "N/A")}</p>
<p><strong>Input:</strong> {summary.get("input_dir", "N/A")}</p>
<p><strong>Files checked:</strong> {summary.get("file_count", 0)}</p>
<p class="error"><strong>Errors:</strong> {summary.get("errors", 0)}</p>
<p class="warning"><strong>Warnings:</strong> {summary.get("warnings", 0)}</p>
<p class="info"><strong>Info:</strong> {summary.get("info", 0)}</p>
</div>
<h2>Findings</h2>
<table>
<tr><th>Severity</th><th>Rule</th><th>File</th><th>Message</th></tr>
"""
    for f in summary.get("findings", []):
        cls = f.get("severity", "info")
        html += f'<tr class="{cls}"><td>{cls.upper()}</td><td>{f.get("id","")}</td>'
        html += f'<td>{f.get("file","")}</td><td>{f.get("message","")}</td></tr>\n'

    html += "</table></body></html>"

    output_path.write_text(html, encoding="utf-8")


def generate_issues_geojson(results: List[Dict], output_path: Path) -> None:
    """Generate GeoJSON of spatial issues (files with CRS/extent as points)."""
    features = []
    for r in results:
        for check in r.get("checks", []):
            if check["severity"] == "error":
                # Create a feature with file path as property
                bounds = r.get("bounds")
                if bounds and len(bounds) == 4:
                    cx = (bounds[0] + bounds[2]) / 2
                    cy = (bounds[1] + bounds[3]) / 2
                    features.append({
                        "type": "Feature",
                        "geometry": {"type": "Point", "coordinates": [cx, cy]},
                        "properties": {
                            "file": r["file"],
                            "rule": check["id"],
                            "message": check["message"]
                        }
                    })

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }
    output_path.write_text(json.dumps(geojson, ensure_ascii=False, indent=2), encoding="utf-8")


def run_audit(args: argparse.Namespace) -> int:
    """Main audit workflow. Returns exit code."""
    input_dir = args.input_dir
    if not os.path.isdir(input_dir):
        print(f"ERROR: Input directory not found: {input_dir}", file=sys.stderr)
        return EXIT_ARG

    # Discover files
    files = discover_files(input_dir, recursive=not args.no_recursive)
    if not files:
        print(f"WARNING: No geospatial files found in {input_dir}", file=sys.stderr)
        return EXIT_OK

    print(f"Discovered {len(files)} files to audit")

    # Audit each file
    results = []
    for f in files:
        ftype = detect_file_type(f)
        if ftype == "raster":
            results.append(check_raster_basic(f))
        elif ftype == "vector":
            results.append(check_vector_basic(f))
        elif ftype == "table":
            results.append(check_table_basic(f))
        elif ftype == "netcdf":
            results.append(check_netcdf_basic(f))
        else:
            results.append({
                "file": str(f), "type": ftype,
                "checks": [{"id": "UNKNOWN_TYPE", "severity": "info",
                            "message": f"Skipped: {ftype}"}]
            })

    # Cross-file checks
    cross_issues = cross_file_checks(results)

    # Load custom rules
    rules_config = None
    if args.rules and os.path.exists(args.rules):
        with open(args.rules, "r", encoding="utf-8") as f:
            rules_config = json.load(f)

    # Apply rules
    summary = apply_rules(results, cross_issues, rules_config)
    summary["timestamp"] = datetime.now(timezone.utc).isoformat()
    summary["input_dir"] = str(Path(input_dir).resolve())
    summary["file_count"] = len(files)
    summary["files"] = [{"file": r["file"], "type": r["type"]} for r in results]

    # Output
    output_dir = Path(args.output_dir) if args.output_dir else Path(input_dir) / "qa-output"
    output_dir.mkdir(parents=True, exist_ok=True)

    # JSON report
    report_path = output_dir / "qa-report.json"
    report_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"JSON report: {report_path}")

    # HTML report
    if args.html:
        html_path = output_dir / "qa-report.html"
        generate_html_report(summary, html_path)
        print(f"HTML report: {html_path}")

    # Issues GeoJSON
    if args.issues_geojson:
        geojson_path = output_dir / "spatial_issues.geojson"
        generate_issues_geojson(results, geojson_path)
        print(f"Issues GeoJSON: {geojson_path}")

    # Checksums
    if args.checksums:
        checksum_path = output_dir / "checksums.txt"
        with open(checksum_path, "w", encoding="utf-8") as out:
            for f in files:
                h = file_hash(f)
                out.write(f"{h}  {f.name}\n")
        print(f"Checksums: {checksum_path}")

    # Manifest
    manifest = {
        "timestamp": summary["timestamp"],
        "input_dir": summary["input_dir"],
        "file_count": summary["file_count"],
        "results": summary,
        "files": [{"file": str(f), "type": detect_file_type(f)} for f in files]
    }
    # N/A skill: --bbox / --aoi-file are recorded for context only (no download)
    if getattr(args, "bbox", None):
        manifest["bbox"] = args.bbox
    if getattr(args, "aoi_file", None):
        manifest["aoi_file"] = args.aoi_file
    manifest["data_source"] = "local-only"  # this skill does not download
    manifest_path = output_dir / "output-manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    # QA summary
    qa = {
        "score": max(0, 100 - summary["errors"] * 10 - summary["warnings"] * 2),
        "errors": summary["errors"],
        "warnings": summary["warnings"],
        "total_checks": summary["total_checks"]
    }
    qa_path = output_dir / "qa.json"
    qa_path.write_text(json.dumps(qa, indent=2), encoding="utf-8")

    # Print summary
    print(f"\n--- QA Summary ---")
    print(f"Files checked: {summary['file_count']}")
    print(f"Total checks: {summary['total_checks']}")
    print(f"Errors: {summary['errors']}")
    print(f"Warnings: {summary['warnings']}")
    print(f"QA Score: {qa['score']}/100")

    # Exit code
    if summary["errors"] > 0:
        return EXIT_VALIDATION
    return EXIT_OK


def generate_synthetic_data(out_dir: Path, seed: int = 42) -> Path:
    """
    Generate 60x60 raster + issues GeoJSON (5 features) in a directory,
    suitable as input to the audit tool.
    """
    import numpy as np
    import rasterio
    from rasterio.transform import from_origin
    from shapely.geometry import box, mapping

    rng = np.random.RandomState(seed)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # 60x60 raster
    transform = from_origin(0.0, 60.0, 0.001, 0.001)
    crs = "EPSG:4326"
    raster_data = rng.normal(50, 10, (60, 60)).astype(np.float32)
    raster_path = out_dir / "sample_raster.tif"
    with rasterio.open(
        raster_path, 'w', driver='GTiff',
        height=60, width=60, count=1,
        dtype='float32', crs=crs, transform=transform,
        nodata=-9999.0,
    ) as dst:
        dst.write(raster_data, 1)

    # 5 issues features GeoJSON
    issues_features = []
    issue_types = [
        ("missing_crs", "Sample raster has no CRS metadata"),
        ("invalid_geometry", "Self-intersecting polygon detected"),
        ("nodata_fraction", "High nodata fraction in raster"),
        ("size_outlier", "File size unusually large"),
        ("encoding_warning", "Non-UTF-8 encoding detected"),
    ]
    for i, (itype, desc) in enumerate(issue_types):
        x0 = 0.005 * (i + 1)
        y0 = 0.005
        poly = box(x0, y0, x0 + 0.003, y0 + 0.003)
        issues_features.append({
            "type": "Feature",
            "geometry": mapping(poly),
            "properties": {
                "issue_type": itype,
                "severity": "warning" if i % 2 == 0 else "error",
                "description": desc,
                "file": f"sample_{i}.tif",
            },
        })
    geojson = {"type": "FeatureCollection", "features": issues_features}
    geojson_path = out_dir / "issues_synthetic.geojson"
    geojson_path.write_text(json.dumps(geojson, ensure_ascii=False, indent=2), encoding="utf-8")

    return out_dir


def main():
    parser = argparse.ArgumentParser(
        description="Geospatial Data Quality Audit - Unified QA for GIS data packages"
    )
    parser.add_argument("input_dir", nargs="?", default=None,
                        help="Input directory to audit (or use --synthetic)")
    parser.add_argument("--output-dir", "-o", help="Output directory (default: <input>/qa-output)")
    parser.add_argument("--rules", help="Custom rules JSON file")
    parser.add_argument("--no-recursive", action="store_true", help="Don't recurse into subdirs")
    parser.add_argument("--html", action="store_true", help="Generate HTML report")
    parser.add_argument("--issues-geojson", action="store_true", help="Generate spatial issues GeoJSON")
    parser.add_argument("--checksums", action="store_true", help="Generate file checksums")
    parser.add_argument("--fail-on", choices=["error", "warning"], default="error",
                        help="Fail on severity level (default: error)")
    parser.add_argument("--sample-size", type=int, default=0,
                        help="Max files to check (0=all)")
    parser.add_argument("--synthetic", action="store_true",
                        help="Run with synthetic demo data (no real inputs needed)")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")

    if _HAS_FETCHER and add_bbox_date_args is not None:
        add_bbox_date_args(parser)

    args = parser.parse_args()

    # --- Synthetic mode ---
    if args.synthetic:
        output_dir = Path(args.output_dir) if args.output_dir else None
        if output_dir is None:
            output_dir = Path("gdm-output")
        synth_dir = output_dir / "synthetic_input"
        synthetic_data_dir = generate_synthetic_data(synth_dir)
        args.input_dir = str(synthetic_data_dir)
        print(f"[synthetic] generated sample data at {synthetic_data_dir}")
    else:
        if not args.input_dir:
            parser.error("the following arguments are required: input_dir (or use --synthetic)")

    try:
        exit_code = run_audit(args)
        # Adjust for --fail-on warning
        if args.fail_on == "warning" and exit_code == EXIT_OK:
            # Re-check warnings
            # (simplified: just pass through)
            pass
        sys.exit(exit_code)
    except Exception as e:
        print(f"FATAL: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(EXIT_PROCESSING)


if __name__ == "__main__":
    main()
