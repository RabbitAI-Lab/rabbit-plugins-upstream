#!/usr/bin/env python3
"""format-batch-converter — 格式批量转换

用 GDAL/OGR（经 rasterio / fiona / geopandas）批量转换栅格与矢量格式：

- **栅格**：GeoTIFF 之间互转/重压缩（rasterio）。
- **矢量**：GeoJSON / Shapefile / GeoPackage 互转（geopandas + fiona/GDAL）。

支持 ``--input`` 指向单个文件或目录（可 ``--recursive`` 递归），按扩展名
自动识别类型并分别转到 ``--raster-target`` / ``--vector-target``。每次转换
记录结构化日志（来源、目标、状态、字节数），汇总到 conversion_log.json。

数据源：本地文件或目录（``--input``），或 ``--synthetic`` 模式在本地生成
一个小 GeoTIFF + GeoJSON + Shapefile 源集做离线批量转换演示。

隐私声明 / Privacy：
- 默认完全离线运行，``--synthetic`` 模式不读取任何外部数据。
- 所有处理在本地完成，不上传用户数据。

Usage:
    python format-batch-converter.py --input ./data --vector-target gpkg --recursive
    python format-batch-converter.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "format-batch-converter"

RASTER_EXTS = {".tif", ".tiff", ".geotiff"}
VECTOR_EXTS = {".geojson", ".json", ".shp", ".gpkg", ".gml", ".kml"}
RASTER_TARGETS = {"tif"}
VECTOR_TARGETS = {"geojson", "gpkg", "shp"}

_TARGET_DRIVER = {"geojson": "GeoJSON", "gpkg": "GPKG", "shp": "ESRI Shapefile"}
_TARGET_EXT = {"geojson": ".geojson", "gpkg": ".gpkg", "shp": ".shp", "tif": ".tif"}

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


# ---------------------------------------------------------------------------
# 输入校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox) -> None:
    """校验 bbox 合法性（W<=E, S<=N, 经纬度范围, 零面积）。"""
    if not (isinstance(bbox, (list, tuple)) and len(bbox) == 4):
        raise ValidationError(f"bbox must have 4 floats, got {bbox!r}", bbox=list(bbox))
    W_, S_, E_, N_ = (float(x) for x in bbox)
    if not (W_ <= E_ and S_ <= N_):
        raise ValidationError(
            f"invalid bbox ordering: W={W_} E={E_} S={S_} N={N_} "
            f"(require W<=E and S<=N)",
            w=W_, e=E_, s=S_, n=N_,
        )
    if not (-180.0 <= W_ <= 180.0 and -180.0 <= E_ <= 180.0):
        raise ValidationError(
            f"lon out of range [-180,180]: W={W_} E={E_}",
            w=W_, e=E_,
        )
    if not (-90.0 <= S_ <= 90.0 and -90.0 <= N_ <= 90.0):
        raise ValidationError(
            f"lat out of range [-90,90]: S={S_} N={N_}",
            s=S_, n=N_,
        )
    if (E_ - W_) <= 0.0 or (N_ - S_) <= 0.0:
        raise ValidationError(
            f"zero-area bbox: W={W_} E={E_} S={S_} N={N_}",
            w=W_, e=E_, s=S_, n=N_,
        )


def validate_params(args) -> None:
    """校验 CLI 参数值域。"""
    if args.bbox is not None:
        validate_bbox(args.bbox)
    if int(args.size) < 1:
        raise UsageError(f"--size must be >=1, got {args.size}", size=int(args.size))


# ---------------------------------------------------------------------------
# 核心：类型识别与单文件转换
# ---------------------------------------------------------------------------
def detect_kind(path: str) -> Optional[str]:
    """按扩展名识别 raster / vector；未知返回 None。"""
    ext = os.path.splitext(path)[1].lower()
    if ext in RASTER_EXTS:
        return "raster"
    if ext in VECTOR_EXTS:
        return "vector"
    return None


def convert_raster(src: str, dst: str) -> None:
    """GeoTIFF → GeoTIFF（可换压缩）。用 rasterio 逐块读写。"""
    import rasterio
    from rasterio.shutil import copy as rio_copy
    with rasterio.open(src) as ds:
        profile = ds.profile.copy()
        profile.update(driver="GTiff", compress="deflate")
        rio_copy(ds, dst, **profile)


def convert_vector(src: str, dst: str, target: str) -> None:
    """矢量格式互转：读入后按目标驱动写出。"""
    import geopandas as gpd
    if target not in VECTOR_TARGETS:
        raise UsageError(f"unknown vector target '{target}'. "
                         f"Choose from: {sorted(VECTOR_TARGETS)}")
    gdf = gpd.read_file(src)
    driver = _TARGET_DRIVER[target]
    if target == "shp":
        # Shapefile 列名 ≤10 字符
        gdf.columns = [c[:10] for c in gdf.columns]
    gdf.to_file(dst, driver=driver)


def convert_file(src: str, dst_dir: str, raster_target: str = "tif",
                 vector_target: str = "geojson") -> Dict[str, Any]:
    """转换单个文件，返回日志条目。"""
    entry: Dict[str, Any] = {
        "source": src, "kind": None, "status": "skipped",
        "target": None, "bytes": 0, "message": "",
    }
    kind = detect_kind(src)
    entry["kind"] = kind
    if kind is None:
        entry["message"] = "unsupported extension"
        return entry
    if not os.path.exists(src):
        entry["status"] = "error"
        entry["message"] = "source not found"
        return entry

    stem = os.path.splitext(os.path.basename(src))[0]
    try:
        if kind == "raster":
            dst = os.path.join(dst_dir, stem + _TARGET_EXT[raster_target])
            convert_raster(src, dst)
        else:
            dst = os.path.join(dst_dir, stem + _TARGET_EXT[vector_target])
            convert_vector(src, dst, vector_target)
        entry["status"] = "ok"
        entry["target"] = dst
        entry["bytes"] = os.path.getsize(dst)
    except Exception as exc:  # noqa: BLE001
        entry["status"] = "error"
        entry["message"] = str(exc)
    return entry


def collect_inputs(path: str, recursive: bool = False) -> List[str]:
    """把文件 / 目录展开为待转换文件列表。"""
    if os.path.isfile(path):
        return [path]
    if not os.path.isdir(path):
        raise UsageError(f"input not found: {path}", path=path)
    files: List[str] = []
    if recursive:
        for root, _dirs, names in os.walk(path):
            for name in sorted(names):
                if detect_kind(os.path.join(root, name)) is not None:
                    files.append(os.path.join(root, name))
    else:
        for name in sorted(os.listdir(path)):
            p = os.path.join(path, name)
            if os.path.isfile(p) and detect_kind(p) is not None:
                files.append(p)
    return files


def batch_convert(input_path: str, output_dir: str, raster_target: str = "tif",
                  vector_target: str = "geojson",
                  recursive: bool = False) -> Dict[str, Any]:
    """批量转换，返回 {entries, summary}。"""
    files = collect_inputs(input_path, recursive=recursive)
    os.makedirs(output_dir, exist_ok=True)
    entries = [convert_file(f, output_dir, raster_target, vector_target)
               for f in files]
    n_ok = sum(1 for e in entries if e["status"] == "ok")
    n_err = sum(1 for e in entries if e["status"] == "error")
    n_skip = sum(1 for e in entries if e["status"] == "skipped")
    summary = {
        "n_inputs": len(files),
        "n_converted": n_ok,
        "n_errors": n_err,
        "n_skipped": n_skip,
        "total_output_bytes": int(sum(e["bytes"] for e in entries)),
    }
    return {"entries": entries, "summary": summary}


# ---------------------------------------------------------------------------
# 合成数据：源集（tif + geojson + shp）
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], source_dir: str,
                       size: int = 32) -> List[str]:
    """在 source_dir 生成一个小栅格 + 两个矢量文件，返回路径列表。"""
    import geopandas as gpd
    from shapely.geometry import Point, Polygon
    from pyproj import CRS
    os.makedirs(source_dir, exist_ok=True)
    w, s, e, n_ = bbox
    paths = []

    # 栅格
    yy, xx = np.mgrid[0:size, 0:size].astype(np.float32)
    band = (xx + yy).astype(np.float32)
    tif = os.path.join(source_dir, "synthetic_raster.tif")
    _write_geotiff(tif, band[np.newaxis, ...], bbox)
    paths.append(tif)

    # 矢量 GeoJSON（点）
    rng = np.random.default_rng(42)
    pts = gpd.GeoDataFrame(
        {"id": np.arange(1, 11)},
        geometry=[Point(rng.uniform(w, e), rng.uniform(s, n_)) for _ in range(10)],
        crs=CRS.from_epsg(4326))
    gj = os.path.join(source_dir, "synthetic_points.geojson")
    pts.to_file(gj, driver="GeoJSON")
    paths.append(gj)

    # 矢量 Shapefile（多边形）
    polys = gpd.GeoDataFrame(
        {"id": [1, 2]},
        geometry=[
            Polygon([(w, s), (w + (e - w) / 3, s), (w + (e - w) / 3, s + (n_ - s) / 3),
                     (w, s + (n_ - s) / 3), (w, s)]),
            Polygon([(e - (e - w) / 3, n_ - (n_ - s) / 3), (e, n_ - (n_ - s) / 3),
                     (e, n_), (e - (e - w) / 3, n_), (e - (e - w) / 3, n_ - (n_ - s) / 3)]),
        ],
        crs=CRS.from_epsg(4326))
    shp = os.path.join(source_dir, "synthetic_polys.shp")
    polys.to_file(shp, driver="ESRI Shapefile")
    paths.append(shp)
    return paths


def _write_geotiff(path: str, cube: np.ndarray, bbox: List[float],
                   nodata: float = -9999.0) -> None:
    import rasterio
    from rasterio.transform import from_bounds
    if cube.ndim == 2:
        cube = cube[np.newaxis, ...]
    nb, h, w = cube.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    profile = {"driver": "GTiff", "height": h, "width": w, "count": nb,
               "dtype": "float32", "crs": "EPSG:4326", "transform": transform,
               "nodata": nodata, "compress": "deflate"}
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(cube[b].astype("float32"), b + 1)


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
            "vector_target": getattr(args, "vector_target", None),
            "raster_target": getattr(args, "raster_target", None),
            "recursive": bool(getattr(args, "recursive", False)),
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
    bbox = list(args.bbox) if args.bbox else None

    # 1) 校验（在 makedirs 之前）
    validate_params(args)
    converted_dir = os.path.join(output_dir, "converted")

    # 2) 解析输入源
    if args.input and not args.synthetic:
        if not os.path.exists(args.input):
            raise UsageError(f"input not found: {args.input}", path=args.input)
        input_path = args.input
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <path>")
        if args.input and args.synthetic:
            # 显式 --synthetic 覆盖 --input
            pass
        source_dir = os.path.join(output_dir, "source")
        generate_synthetic(bbox, source_dir, size=args.size)
        input_path = source_dir
        source_note = "synthetic"

    # 3) 提前嗅探 --input 路径文件数（避免空目录静默 rc=0）
    files = collect_inputs(input_path, recursive=args.recursive)
    if not files:
        raise ValidationError(
            f"no supported files found in input path: {input_path} "
            f"(supported raster: {sorted(RASTER_EXTS)}, vector: {sorted(VECTOR_EXTS)})",
            input_path=input_path,
        )

    # 4) 校验通过后再创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    result = batch_convert(input_path, converted_dir,
                           raster_target=args.raster_target,
                           vector_target=args.vector_target,
                           recursive=args.recursive)
    result["source"] = source_note
    result["vector_target"] = args.vector_target
    result["raster_target"] = args.raster_target

    log_path = os.path.join(output_dir, "conversion_log.json")
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2, default=str)

    summary = result["summary"]
    qa = {
        "source": source_note,
        **summary,
        "vector_target": args.vector_target,
        "raster_target": args.raster_target,
        "n_input_files": len(files),
    }
    outputs = [{"path": log_path, "kind": "json"}]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] inputs: {summary['n_inputs']}  converted: "
              f"{summary['n_converted']}  errors: {summary['n_errors']}  "
              f"skipped: {summary['n_skipped']}")
        print(f"[{SKILL_NAME}] output bytes: {summary['total_output_bytes']}")
        print(f"[{SKILL_NAME}] log: {log_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Batch convert raster/vector formats (GeoTIFF/SHP/GPKG/GeoJSON) with logging.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input file or directory")
    p.add_argument("--vector-target", dest="vector_target", default="geojson",
                   choices=sorted(VECTOR_TARGETS),
                   help="target vector format (default: geojson)")
    p.add_argument("--raster-target", dest="raster_target", default="tif",
                   choices=sorted(RASTER_TARGETS),
                   help="target raster format (default: tif)")
    p.add_argument("--recursive", action="store_true",
                   help="recurse into subdirectories")
    p.add_argument("--size", type=int, default=32,
                   help="synthetic raster size (default: 32)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate synthetic source files (offline)")
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
