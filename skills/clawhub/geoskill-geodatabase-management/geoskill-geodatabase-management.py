#!/usr/bin/env python3
"""geodatabase-management — 空间数据库管理

围绕 GeoPackage（SQLite 容器）的空间数据库管理：

- **建表/导入**：把矢量要素写入 GeoPackage 图层（GDAL/fiona 保证规范合规）。
- **空间索引**：用 SQLite 内置 ``rtree`` 虚拟表为图层构建 R-tree 空间索引
  （``idx_<layer>_geom``，存每个要素的外包矩形）。
- **空间查询**：按 bbox 做索引查询（SQL）与暴力扫描，两者结果对齐。
- **信息检查**：从 ``gpkg_contents`` 列出图层与要素数、索引状态。

数据源：本地矢量文件（``--input``），或 ``--synthetic`` 模式生成随机点集
（离线）。

隐私声明 / Privacy：
- 默认完全离线运行，``--synthetic`` 模式不读取任何外部数据。
- 所有处理在本地完成，不上传用户数据。

Usage:
    python geodatabase-management.py --input cities.shp --layer cities
    python geodatabase-management.py --bbox 116 39 117 40 --synthetic --output-dir ./out

License: MIT
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import sqlite3
import sys
from typing import Any, Dict, List, Optional, Sequence, Tuple

import numpy as np

VERSION = "1.0.0"
SKILL_NAME = "geodatabase-management"

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


def _sanitize_layer(layer: str) -> str:
    """把图层名规整为合法 SQL 标识符。"""
    s = "".join(c if (c.isalnum() or c == "_") else "_" for c in layer)
    if not s or s[0].isdigit():
        s = "layer_" + s
    return s


def validate_bbox(bbox) -> List[float]:
    """校验 bbox [W, S, E, N]；不合法抛 ValidationError（exit 6）。

    同 buffer-analysis / change-detection-dl：跨 180°（W > E）静默产出负
    像元宽度错查询；超经纬度范围亦然。统一前置校验，给出可读提示。
    """
    if bbox is None:
        return None  # type: ignore[return-value]
    try:
        w, s, e, n = (float(v) for v in bbox)
    except (TypeError, ValueError) as exc:
        raise ValidationError(f"bbox values must be numeric: {bbox}") from exc
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(f"bbox longitude out of range [-180, 180]: W={w}, E={e}")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(f"bbox latitude out of range [-90, 90]: S={s}, N={n}")
    if w > e:
        raise ValidationError(
            f"bbox W ({w}) > E ({e}); antimeridian-crossing bbox is not supported — "
            "split the request into two bboxes on either side of +/-180")
    if s > n:
        raise ValidationError(f"bbox S ({s}) > N ({n})")
    return [w, s, e, n]


# ---------------------------------------------------------------------------
# 核心算法：GeoPackage 建表 / 导入 / 索引 / 查询
# ---------------------------------------------------------------------------
def create_geodatabase(path: str, gdf: Any, layer: str = "features",
                       append: bool = False) -> str:
    """把 GeoDataFrame 写入 GeoPackage 图层，返回规整后的图层名。"""
    import fiona  # noqa: F401  (确认驱动可用)
    layer = _sanitize_layer(layer)
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    mode = "a" if append and os.path.exists(path) else "w"
    gdf.to_file(path, layer=layer, driver="GPKG", mode=mode)
    return layer


def import_features(path: str, gdf: Any, layer: str = "features") -> int:
    """追加导入要素到已存在的图层，返回追加的要素数。"""
    layer = _sanitize_layer(layer)
    if not os.path.exists(path):
        raise UsageError(f"geodatabase not found: {path}", path=path)
    gdf.to_file(path, layer=layer, driver="GPKG", mode="a")
    return len(gdf)


def list_layers(path: str) -> List[Dict[str, Any]]:
    """从 gpkg_contents 读取图层清单与要素数。"""
    if not os.path.exists(path):
        raise UsageError(f"geodatabase not found: {path}", path=path)
    con = sqlite3.connect(path)
    try:
        rows = con.execute(
            "SELECT table_name, data_type FROM gpkg_contents").fetchall()
        out = []
        for table_name, data_type in rows:
            try:
                cnt = con.execute(
                    f'SELECT COUNT(*) FROM "{table_name}"').fetchone()[0]
            except sqlite3.Error:
                cnt = None
            out.append({"layer": table_name, "data_type": data_type,
                        "feature_count": cnt})
        return out
    finally:
        con.close()


def spatial_index_table(layer: str) -> str:
    return f"idx_{_sanitize_layer(layer)}_geom"


def spatial_index_exists(path: str, layer: str) -> bool:
    tbl = spatial_index_table(layer)
    con = sqlite3.connect(path)
    try:
        row = con.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
            (tbl,)).fetchone()
        return row is not None
    finally:
        con.close()


def build_spatial_index(path: str, layer: str, gdf: Optional[Any] = None) -> int:
    """为图层构建 R-tree 空间索引，返回索引要素数。

    外包矩形取自要素几何；若未提供 gdf，则从 GeoPackage 重新读取。
    """
    layer = _sanitize_layer(layer)
    if gdf is None:
        import geopandas as gpd
        gdf = gpd.read_file(path, layer=layer)

    # 取与 GeoPackage 一致的 fid（GDAL 写入为 1..N 的 INTEGER PRIMARY KEY）
    con = sqlite3.connect(path)
    try:
        fids = [r[0] for r in con.execute(
            f'SELECT fid FROM "{layer}" ORDER BY fid').fetchall()]
    except sqlite3.Error as exc:
        con.close()
        raise ValidationError(f"cannot read fid from layer '{layer}': {exc}") from exc

    if len(fids) != len(gdf):
        # 退化：按行号生成 1..N
        fids = list(range(1, len(gdf) + 1))

    tbl = spatial_index_table(layer)
    con.execute(f'DROP TABLE IF EXISTS "{tbl}"')
    con.execute(
        f'CREATE VIRTUAL TABLE "{tbl}" USING rtree(id, minx, maxx, miny, maxy)')
    rows = []
    for fid, geom in zip(fids, gdf.geometry):
        if geom is None or geom.is_empty:
            continue
        minx, miny, maxx, maxy = geom.bounds
        rows.append((int(fid), float(minx), float(maxx), float(miny), float(maxy)))
    con.executemany(f'INSERT INTO "{tbl}" VALUES (?,?,?,?,?)', rows)
    con.commit()
    con.close()
    return len(rows)


def query_bbox_indexed(path: str, layer: str, bbox: Sequence[float]) -> List[int]:
    """用 R-tree 空间索引查询与 bbox 相交的要素 fid。"""
    tbl = spatial_index_table(layer)
    w, s, e, n = bbox
    con = sqlite3.connect(path)
    try:
        rows = con.execute(
            f'SELECT id FROM "{tbl}" WHERE minx <= ? AND maxx >= ? '
            f'AND miny <= ? AND maxy >= ? ORDER BY id',
            (e, w, n, s)).fetchall()
        return [r[0] for r in rows]
    except sqlite3.OperationalError as exc:
        raise ValidationError(
            f"spatial index query failed (build it first?): {exc}") from exc
    finally:
        con.close()


def query_bbox_brute(path: str, layer: str, bbox: Sequence[float]) -> List[int]:
    """暴力扫描查询：读整个图层，按外包矩形相交过滤。"""
    import geopandas as gpd
    from shapely.geometry import box
    gdf = gpd.read_file(path, layer=layer)
    win = box(*bbox)
    fids = []
    con = sqlite3.connect(path)
    try:
        db_fids = [r[0] for r in con.execute(
            f'SELECT fid FROM "{_sanitize_layer(layer)}" ORDER BY fid').fetchall()]
    finally:
        con.close()
    if len(db_fids) != len(gdf):
        db_fids = list(range(1, len(gdf) + 1))
    for fid, geom in zip(db_fids, gdf.geometry):
        if geom is None or geom.is_empty:
            continue
        if win.intersects(geom.envelope):
            fids.append(int(fid))
    return sorted(fids)


def database_info(path: str) -> Dict[str, Any]:
    """汇总数据库信息：图层、要素数、空间索引状态。"""
    layers = list_layers(path)
    for lyr in layers:
        lyr["has_spatial_index"] = spatial_index_exists(path, lyr["layer"])
    con = sqlite3.connect(path)
    try:
        tables = [r[0] for r in con.execute(
            "SELECT name FROM sqlite_master WHERE type='table'").fetchall()]
    finally:
        con.close()
    return {"path": path, "layers": layers, "sqlite_tables": tables}


# ---------------------------------------------------------------------------
# 合成数据 / I/O
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], n: int = 200, seed: int = 42) -> Any:
    import geopandas as gpd
    from shapely.geometry import Point
    from pyproj import CRS
    rng = np.random.default_rng(seed)
    w, s, e, n_ = bbox
    xs = rng.uniform(w, e, n)
    ys = rng.uniform(s, n_, n)
    return gpd.GeoDataFrame(
        {"id": np.arange(1, n + 1),
         "value": rng.uniform(0, 100, n).round(3)},
        geometry=[Point(x, y) for x, y in zip(xs, ys)],
        crs=CRS.from_epsg(4326))


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
            "layer": getattr(args, "layer", None),
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
def process(args: argparse.Namespace) -> int:
    started_at = _utc_now()
    output_dir = args.output_dir
    os.makedirs(output_dir, exist_ok=True)
    bbox = list(args.bbox) if args.bbox else None

    if args.input and not args.synthetic:
        gdf = read_vector(args.input)
        if bbox is None and gdf.crs is not None:
            b = gdf.total_bounds
            bbox = [float(b[0]), float(b[1]), float(b[2]), float(b[3])]
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <vector>")
        bbox = validate_bbox(bbox)
        if not isinstance(args.features, int) or args.features <= 0:
            raise ValidationError(
                f"--features must be a positive integer; got {args.features!r}")
        gdf = generate_synthetic(bbox, n=args.features)
        source_note = "synthetic"

    if len(gdf) == 0:
        raise ValidationError("input vector has no features")

    gpkg_path = os.path.join(output_dir, "database.gpkg")
    if os.path.exists(gpkg_path):
        os.remove(gpkg_path)
    layer = create_geodatabase(gpkg_path, gdf, args.layer)
    indexed = build_spatial_index(gpkg_path, layer, gdf)

    # 查询窗口：优先 --bbox，否则用数据全范围；任何来源都再做一次 validate_bbox
    if bbox is None:
        b = gdf.total_bounds
        bbox = [float(b[0]), float(b[1]), float(b[2]), float(b[3])]
    bbox = validate_bbox(bbox)
    q_indexed = query_bbox_indexed(gpkg_path, layer, bbox)
    q_brute = query_bbox_brute(gpkg_path, layer, bbox)
    consistent = q_indexed == q_brute

    info = database_info(gpkg_path)
    report = {
        "skill": SKILL_NAME,
        "source": source_note,
        "layer": layer,
        "n_features": int(len(gdf)),
        "indexed_features": indexed,
        "has_spatial_index": spatial_index_exists(gpkg_path, layer),
        "query_bbox": bbox,
        "query_indexed_count": len(q_indexed),
        "query_brute_count": len(q_brute),
        "query_consistent": consistent,
        "database_info": info,
    }
    report_path = os.path.join(output_dir, "database_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2, default=str)

    qa = {
        "source": source_note,
        "layer": layer,
        "n_features": int(len(gdf)),
        "indexed_features": indexed,
        "query_indexed_count": len(q_indexed),
        "query_consistent": consistent,
    }
    outputs = [
        {"path": gpkg_path, "kind": "vector", "feature_count": int(len(gdf)),
         "crs_epsg": 4326},
        {"path": report_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] geodatabase: {gpkg_path} (layer: {layer})")
        print(f"[{SKILL_NAME}] features: {len(gdf)}  indexed: {indexed}")
        print(f"[{SKILL_NAME}] query matches: {len(q_indexed)} "
              f"(index==brute: {consistent})")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Manage a GeoPackage: create layers, build spatial index, run bbox queries.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input vector file to import")
    p.add_argument("--layer", default="features",
                   help="GeoPackage layer name (default: features)")
    p.add_argument("--features", type=int, default=200,
                   help="number of synthetic points (default: 200)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate synthetic point features (offline)")
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
