#!/usr/bin/env python3
"""spatial-data-validation — 空间数据质量验证

对矢量数据执行多维度质量验证：

- **几何有效性**：用 shapely 判定每个要素几何是否有效（self-intersection、
  ring 自交、空几何、null 几何），并给出原因。
- **拓扑检查**：检测重复几何与多边形之间的重叠（overlap）。
- **属性完整性**：统计每个必填字段的空值/缺失比例。
- **CRS 一致性**：判断数据坐标参考系是否与期望 EPSG 一致。

最终给出 0-1 的综合质量评分与等级（A/B/C/D/F）。

数据源：本地矢量文件（``--input``，任意 OGR 支持格式），或 ``--synthetic``
模式在本地生成含刻意缺陷（bowtie、null 几何、缺失属性）的测试要素。

隐私声明 / Privacy：
- 默认完全离线运行，``--synthetic`` 模式不读取任何外部数据。
- 所有处理在本地完成，不上传用户数据。

Usage:
    python spatial-data-validation.py --input parcels.gpkg --crs EPSG:4326
    python spatial-data-validation.py --bbox 116 39 117 40 --synthetic --output-dir ./out

License: MIT
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import sys
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

VERSION = "1.0.0"
SKILL_NAME = "spatial-data-validation"

DEFAULT_REQUIRED_FIELDS = ["id", "name", "class"]

# ---- 共享核心库（本地 vendored，随脚本目录一起分发）----
try:
    from _geoskill_core.errors import (
        GeoSkillError, UsageError, ValidationError, ProcessError, to_exit_code,
    )
    from _geoskill_core.manifest import OutputManifest, OutputFile
except ImportError:  # pragma: no cover - fallback minimal definitions
    class GeoSkillError(Exception):
        def __init__(self, message: str, code: int = 7, kind: str = "EGeo", **kw):
            super().__init__(message)
            self.message, self.code, self.kind = message, code, kind

    class UsageError(GeoSkillError):
        def __init__(self, m, **k): super().__init__(m, code=2, kind="EUsage", **k)

    class ValidationError(GeoSkillError):
        def __init__(self, m, **k): super().__init__(m, code=6, kind="EValidate", **k)

    class ProcessError(GeoSkillError):
        def __init__(self, m, **k): super().__init__(m, code=7, kind="EProcess", **k)

    def to_exit_code(exc):
        return getattr(exc, "code", 7)

    OutputManifest = None
    OutputFile = None


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


def validate_bbox(bbox: List[float]) -> None:
    """校验用户传入 bbox：W<E、S<N、经纬度在合法范围、非零面积；跨 180° 明确提示。"""
    if bbox is None:
        raise UsageError("provide --bbox (synthetic mode) or --input <vector>")
    if len(bbox) != 4:
        raise ValidationError(f"bbox must have exactly 4 numbers, got {len(bbox)}")
    w, s, e, n = [float(x) for x in bbox]
    if w > e:
        raise ValidationError(
            f"bbox minLon ({w}) > maxLon ({e}): crossing the 180° antimeridian is not "
            "supported, please split the region into two bboxes")
    if s > n:
        raise ValidationError(f"bbox minLat ({s}) > maxLat ({n}): S must be <= N")
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(f"bbox longitudes out of range [-180, 180]: {w}, {e}")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(f"bbox latitudes out of range [-90, 90]: {s}, {n}")
    if w == e or s == n:
        raise ValidationError("bbox has zero area")


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def geometry_validity(geom: Any) -> Tuple[bool, str]:
    """判定单个几何是否有效，返回 (is_valid, reason)。"""
    import shapely
    if geom is None:
        return False, "null geometry"
    try:
        is_empty = bool(geom.is_empty)
    except Exception:  # noqa: BLE001
        is_empty = False
    if is_empty and geom.geom_type != "GeometryCollection":
        return False, "empty geometry"
    try:
        if shapely.is_valid(geom):
            return True, "valid"
        return False, shapely.is_valid_reason(geom)
    except Exception as exc:  # noqa: BLE001
        return False, f"error: {exc}"


def check_geometry(gdf: Any) -> List[Dict[str, Any]]:
    """逐要素几何有效性检查。"""
    results = []
    for i, geom in enumerate(gdf.geometry):
        ok, reason = geometry_validity(geom)
        results.append({"index": int(i), "valid": bool(ok), "reason": reason})
    return results


def check_topology(gdf: Any, overlap_tol: float = 1e-9) -> Dict[str, Any]:
    """拓扑检查：重复几何与多边形重叠。"""
    geoms = list(gdf.geometry)
    n = len(geoms)
    duplicates = 0
    seen_wkt = set()
    for g in geoms:
        if g is None:
            continue
        wkt = g.wkt
        if wkt in seen_wkt:
            duplicates += 1
        seen_wkt.add(wkt)

    overlaps: List[Dict[str, Any]] = []
    for i in range(n):
        gi = geoms[i]
        if gi is None or not gi.is_valid or gi.is_empty:
            continue
        for j in range(i + 1, n):
            gj = geoms[j]
            if gj is None or not gj.is_valid or gj.is_empty:
                continue
            try:
                inter = gi.intersection(gj)
            except Exception:  # noqa: BLE001
                continue
            area = getattr(inter, "area", 0.0)
            if area is not None and area > overlap_tol:
                overlaps.append({"pair": [int(i), int(j)], "overlap_area": float(area)})
    return {
        "duplicate_geometries": int(duplicates),
        "overlapping_pairs": overlaps,
        "n_overlaps": len(overlaps),
    }


def check_attributes(gdf: Any, required_fields: List[str]) -> Dict[str, Any]:
    """属性完整性：逐字段统计空值。"""
    cols = set(gdf.columns)
    per_field = {}
    n = len(gdf)
    for f in required_fields:
        if f not in cols:
            per_field[f] = {"present": False, "null_count": n, "null_fraction": 1.0}
            continue
        series = gdf[f]
        null_count = int(series.isna().sum())
        # 视空字符串为缺失
        try:
            empty_str = int((series.astype(str).str.strip() == "").sum())
        except Exception:  # noqa: BLE001
            empty_str = 0
        missing = max(null_count, empty_str)
        per_field[f] = {
            "present": True,
            "null_count": missing,
            "null_fraction": round(missing / n, 4) if n else 0.0,
        }
    fractions = [v["null_fraction"] for v in per_field.values()]
    mean_completeness = (1.0 - (sum(fractions) / len(fractions))) if fractions else 1.0
    return {
        "n_features": int(n),
        "fields": per_field,
        "attribute_completeness": round(float(mean_completeness), 4),
    }


def check_crs(gdf: Any, expected_epsg: int) -> Dict[str, Any]:
    """CRS 一致性检查。"""
    crs = getattr(gdf, "crs", None)
    actual_epsg = None
    if crs is not None:
        try:
            actual_epsg = crs.to_epsg()
        except Exception:  # noqa: BLE001
            actual_epsg = None
    consistent = actual_epsg == expected_epsg
    return {
        "expected_epsg": int(expected_epsg),
        "actual_epsg": actual_epsg,
        "crs_string": (crs.to_string() if crs is not None else None),
        "consistent": bool(consistent),
    }


def grade_from_score(score: float) -> str:
    if score >= 0.95:
        return "A"
    if score >= 0.85:
        return "B"
    if score >= 0.70:
        return "C"
    if score >= 0.50:
        return "D"
    return "F"


def validate_vector(
    gdf: Any,
    required_fields: List[str],
    expected_epsg: int = 4326,
) -> Dict[str, Any]:
    """聚合所有检查，返回综合质量报告。"""
    geom = check_geometry(gdf)
    topo = check_topology(gdf)
    attr = check_attributes(gdf, required_fields)
    crs = check_crs(gdf, expected_epsg)

    n = len(geom)
    n_valid = sum(1 for g in geom if g["valid"])
    geom_score = (n_valid / n) if n else 1.0
    topo_score = 1.0
    if n:
        issues = topo["duplicate_geometries"] + topo["n_overlaps"]
        topo_score = max(0.0, 1.0 - issues / n)
    attr_score = attr["attribute_completeness"]
    crs_score = 1.0 if crs["consistent"] else 0.0

    overall = round(0.40 * geom_score + 0.20 * topo_score
                    + 0.25 * attr_score + 0.15 * crs_score, 4)
    return {
        "n_features": int(n),
        "geometry": {
            "valid_count": int(n_valid),
            "invalid_count": int(n - n_valid),
            "score": round(geom_score, 4),
            "details": geom,
        },
        "topology": {**topo, "score": round(topo_score, 4)},
        "attributes": {**attr, "score": round(attr_score, 4)},
        "crs": {**crs, "score": crs_score},
        "overall_score": overall,
        "grade": grade_from_score(overall),
    }


# ---------------------------------------------------------------------------
# 合成数据：含刻意缺陷的矢量要素
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    n: int = 6,
    required_fields: Optional[List[str]] = None,
    seed: int = 42,
) -> Any:
    """在 bbox 内生成 n 个多边形要素，其中包含 bowtie / null 几何与缺失属性。"""
    import geopandas as gpd
    from shapely.geometry import Polygon
    from pyproj import CRS

    if required_fields is None:
        required_fields = list(DEFAULT_REQUIRED_FIELDS)
    rng = np.random.default_rng(seed)
    w, s, e, n_ = bbox
    cols = max(3, int(np.ceil(np.sqrt(n))))
    rows = max(1, int(np.ceil(n / cols)))
    dx = (e - w) / cols
    dy = (n_ - s) / rows

    geoms, attrs = [], {f: [] for f in required_fields}
    idx = 0
    for r in range(rows):
        for c in range(cols):
            if idx >= n:
                break
            x0 = w + c * dx
            y0 = s + r * dy
            x1, y1 = x0 + dx * 0.8, y0 + dy * 0.8
            if idx == 0:
                # bowtie（自相交）→ 无效几何
                geom = Polygon([(x0, y0), (x1, y1), (x1, y0), (x0, y1), (x0, y0)])
            elif idx == 1:
                geom = None  # null 几何
            else:
                geom = Polygon([(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)])
            geoms.append(geom)
            for f in required_fields:
                if idx == 2 and f == "name":
                    attrs[f].append(None)  # 制造一个属性缺失
                elif f == "id":
                    attrs[f].append(idx + 1)
                elif f == "class":
                    attrs[f].append(rng.choice(["urban", "veg", "water"]))
                else:
                    attrs[f].append(f"feat_{idx}")
            idx += 1

    data = {f: attrs[f] for f in required_fields}
    gdf = gpd.GeoDataFrame(data, geometry=geoms, crs=CRS.from_epsg(4326))
    return gdf


def write_geojson(path: str, gdf: Any) -> None:
    """写 GeoJSON，兼容空 GeoDataFrame。"""
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    if len(gdf) == 0:
        with open(path, "w", encoding="utf-8") as f:
            json.dump({"type": "FeatureCollection", "features": []}, f)
        return
    gdf.to_file(path, driver="GeoJSON")


def read_vector(path: str) -> Any:
    import geopandas as gpd
    if not os.path.exists(path):
        raise UsageError(f"input vector not found: {path}", path=path)
    try:
        return gpd.read_file(path)
    except Exception as exc:  # noqa: BLE001
        raise ValidationError(f"failed to read vector '{path}': {exc}") from exc


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------
def write_manifest(
    output_dir: str,
    args: argparse.Namespace,
    outputs: List[Dict[str, Any]],
    qa: Dict[str, Any],
    started_at: str,
    exit_code: int,
    bbox: Optional[List[float]],
) -> Optional[str]:
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME,
        skill_version=VERSION,
        command=cmd,
        started_at=started_at,
        finished_at=_utc_now(),
        exit_code=exit_code,
        inputs={
            "input": getattr(args, "input", None),
            "crs": getattr(args, "crs", None),
            "synthetic": bool(getattr(args, "synthetic", False)),
            "bbox": bbox,
        },
        outputs=[OutputFile(**o) for o in outputs],
        qa=qa,
        software={"python": sys.version.split()[0], "skill": SKILL_NAME},
    )
    path = os.path.join(output_dir, "output-manifest.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(man.to_dict(), f, ensure_ascii=False, indent=2, default=str)
    return path


# ---------------------------------------------------------------------------
# 主流程
# ---------------------------------------------------------------------------
def _parse_epsg(text: str) -> int:
    t = str(text).upper().replace("EPSG:", "").strip()
    try:
        return int(t)
    except ValueError as exc:
        raise UsageError(f"invalid --crs '{text}', expected EPSG:<code>") from exc


def process(args: argparse.Namespace) -> int:
    started_at = _utc_now()
    output_dir = args.output_dir
    if args.bbox is not None:
        validate_bbox(list(args.bbox))
    bbox = list(args.bbox) if args.bbox else None
    expected_epsg = _parse_epsg(args.crs)
    required_fields = [f.strip() for f in args.fields.split(",") if f.strip()]

    if args.input and not args.synthetic:
        gdf = read_vector(args.input)
        if bbox is None and gdf.crs is not None:
            try:
                b = gdf.total_bounds
                bbox = [float(b[0]), float(b[1]), float(b[2]), float(b[3])]
            except Exception:  # noqa: BLE001
                bbox = None
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <vector>")
        gdf = generate_synthetic(bbox, required_fields=required_fields)
        source_note = "synthetic"

    if len(gdf) == 0:
        raise ValidationError("input vector has no features")

    report = validate_vector(gdf, required_fields, expected_epsg)
    report["source"] = source_note

    os.makedirs(output_dir, exist_ok=True)
    report_path = os.path.join(output_dir, "validation_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2, default=str)

    # 导出无效几何要素
    invalid_idx = [g["index"] for g in report["geometry"]["details"] if not g["valid"]]
    invalid_gdf = gdf.iloc[invalid_idx] if invalid_idx else gdf.iloc[0:0]
    invalid_path = os.path.join(output_dir, "invalid_geometries.geojson")
    write_geojson(invalid_path, invalid_gdf)

    qa = {
        "source": source_note,
        "n_features": report["n_features"],
        "invalid_geometries": report["geometry"]["invalid_count"],
        "attribute_completeness": report["attributes"]["attribute_completeness"],
        "crs_consistent": report["crs"]["consistent"],
        "overall_score": report["overall_score"],
        "grade": report["grade"],
    }
    outputs = [
        {"path": report_path, "kind": "json"},
        {"path": invalid_path, "kind": "vector", "crs_epsg": 4326,
         "feature_count": int(len(invalid_gdf))},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] features: {report['n_features']}")
        print(f"[{SKILL_NAME}] invalid geometries: {report['geometry']['invalid_count']}")
        print(f"[{SKILL_NAME}] attribute completeness: {qa['attribute_completeness']:.4f}")
        print(f"[{SKILL_NAME}] CRS consistent: {qa['crs_consistent']}")
        print(f"[{SKILL_NAME}] overall score: {qa['overall_score']:.4f} (grade {qa['grade']})")
        print(f"[{SKILL_NAME}] report: {report_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Validate vector geometry, topology, attributes and CRS consistency.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input vector file (any OGR format)")
    p.add_argument("--crs", default="EPSG:4326",
                   help="expected CRS as EPSG:<code> (default: EPSG:4326)")
    p.add_argument("--fields", default=",".join(DEFAULT_REQUIRED_FIELDS),
                   help="comma-separated required attribute fields")
    p.add_argument("--synthetic", action="store_true",
                   help="generate synthetic vector data with defects (offline)")
    p.add_argument("--output-dir", default="./output", help="output directory")
    p.add_argument("--quiet", action="store_true", help="suppress console output")
    p.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    return p


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return process(args)
    except GeoSkillError as exc:
        print(f"[{SKILL_NAME}] ERROR [{exc.kind}] {exc.message}", file=sys.stderr)
        return exc.code
    except KeyboardInterrupt:
        return 130
    except Exception as exc:  # noqa: BLE001
        print(f"[{SKILL_NAME}] ERROR {exc}", file=sys.stderr)
        return to_exit_code(exc)


if __name__ == "__main__":
    sys.exit(main())
