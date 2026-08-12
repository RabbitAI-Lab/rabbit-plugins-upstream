#!/usr/bin/env python3
"""spatial-etl-pipeline — 空间ETL流水线

配置驱动的 Extract-Transform-Load 流水线：

- **Extract**：从合成数据或本地矢量文件提取 GeoDataFrame。
- **Transform**：按配置顺序执行可组合的算子——bbox 过滤、属性过滤、
  重投影、加字段（面积/周长/派生列）、字段重命名、缓冲。
- **Load**：写出 GeoJSON / GeoPackage。

每个步骤记录结构化日志（名称、耗时、输入/输出要素数、消息），流水线结束
后汇总质量报告（要素增减、空值比例、CRS）。配置可用 ``--config`` 提供 JSON。

数据源：``--input`` 矢量文件，或 ``--synthetic`` 模式生成随机多边形（离线）。

隐私声明 / Privacy：
- 默认完全离线运行，``--synthetic`` 模式不读取任何外部数据。
- 所有处理在本地完成，不上传用户数据。

Usage:
    python spatial-etl-pipeline.py --input raw.shp --config pipeline.json
    python spatial-etl-pipeline.py --bbox 116 39 117 40 --synthetic --output-dir ./out

License: MIT
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import sys
import time
import warnings
from typing import Any, Callable, Dict, List, Optional, Tuple

import numpy as np

VERSION = "1.0.0"
SKILL_NAME = "spatial-etl-pipeline"

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


def validate_bbox(b: List[float], ctx: str = "bbox") -> None:
    """校验地理范围 [W, S, E, N]，不合法时抛 ValidationError (rc=6)。"""
    if b is None or len(b) != 4:
        raise ValidationError(f"{ctx} must be [minLon minLat maxLon maxLat]")
    w, s, e, n = (float(v) for v in b)
    if w > e:
        raise ValidationError(
            f"{ctx} invalid: minLon {w} > maxLon {e} "
            "(note: crossing the 180/-180 antimeridian is not supported)")
    if s > n:
        raise ValidationError(f"{ctx} invalid: minLat {s} > maxLat {n}")
    if not (-180.0 <= w <= 180.0) or not (-180.0 <= e <= 180.0):
        raise ValidationError(f"{ctx} longitude out of range [-180, 180]")
    if not (-90.0 <= s <= 90.0) or not (-90.0 <= n <= 90.0):
        raise ValidationError(f"{ctx} latitude out of range [-90, 90]")


def validate_step_params(op: str, step: Dict[str, Any]) -> None:
    """校验单步算子所需参数，缺参/类型错误抛 ValidationError (rc=6)。"""
    if op == "filter_bbox":
        bbox = step.get("bbox")
        if bbox is None:
            raise ValidationError("filter_bbox step missing required parameter 'bbox'")
        validate_bbox(bbox, ctx="filter_bbox bbox")
    elif op == "filter_attribute":
        for key in ("field", "value"):
            if key not in step:
                raise ValidationError(
                    f"filter_attribute step missing required parameter '{key}'")
    elif op == "reproject":
        if "to_crs" not in step:
            raise ValidationError("reproject step missing required parameter 'to_crs'")
    elif op == "add_field":
        if "name" not in step:
            raise ValidationError("add_field step missing required parameter 'name'")
    elif op == "rename":
        if not isinstance(step.get("mapping"), dict):
            raise ValidationError(
                "rename step missing required parameter 'mapping' (JSON object)")
    elif op == "buffer":
        try:
            d = float(step["distance"])
        except (KeyError, TypeError, ValueError):
            raise ValidationError(
                "buffer step missing/invalid numeric parameter 'distance'")
        if not np.isfinite(d):
            raise ValidationError("buffer step 'distance' must be finite")


# ---------------------------------------------------------------------------
# 核心：流水线上下文与算子注册表
# ---------------------------------------------------------------------------
class PipelineContext:
    """承载数据与逐步日志的上下文。"""

    def __init__(self) -> None:
        self.gdf = None
        self.logs: List[Dict[str, Any]] = []
        self.initial_count = 0

    def log(self, step: str, op: str, n_in: int, n_out: int,
            status: str, message: str = "", elapsed_ms: float = 0.0) -> None:
        self.logs.append({
            "step": step, "op": op, "status": status,
            "features_in": int(n_in), "features_out": int(n_out),
            "elapsed_ms": round(float(elapsed_ms), 3),
            "message": message,
        })


# ---- Transform 算子：fn(gdf, params) -> gdf ----
def op_filter_bbox(gdf: Any, params: Dict[str, Any]) -> Any:
    from shapely.geometry import box
    bbox = params["bbox"]
    win = box(*bbox)
    mask = gdf.geometry.apply(lambda g: bool(g is not None and win.intersects(g)))
    return gdf[mask].reset_index(drop=True)


_ATTR_OPS: Dict[str, Callable[[Any, Any], Any]] = {
    ">": lambda a, b: a > b,
    ">=": lambda a, b: a >= b,
    "<": lambda a, b: a < b,
    "<=": lambda a, b: a <= b,
    "==": lambda a, b: a == b,
    "!=": lambda a, b: a != b,
}


def op_filter_attribute(gdf: Any, params: Dict[str, Any]) -> Any:
    field = params["field"]
    cmp = params.get("cmp", ">")
    value = params["value"]
    if field not in gdf.columns:
        raise ValidationError(f"filter field '{field}' not in attributes")
    if cmp not in _ATTR_OPS:
        raise UsageError(f"unknown comparator '{cmp}'. Choose from: {sorted(_ATTR_OPS)}")
    mask = _ATTR_OPS[cmp](gdf[field], value)
    return gdf[mask].reset_index(drop=True)


def op_reproject(gdf: Any, params: Dict[str, Any]) -> Any:
    to_crs = params["to_crs"]
    try:
        return gdf.to_crs(to_crs)
    except Exception as exc:  # noqa: BLE001
        raise ValidationError(f"reproject to {to_crs} failed: {exc}") from exc


def op_add_field(gdf: Any, params: Dict[str, Any]) -> Any:
    name = params["name"]
    source = params.get("source", "area")
    out = gdf.copy()
    # 地理 CRS 下计算面积/质心仅作派生字段，抑制 geopandas 的提示性警告
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        if source == "area":
            out[name] = out.geometry.area.round(8)
        elif source == "length":
            out[name] = out.geometry.length.round(8)
        elif source == "centroid_x":
            out[name] = out.geometry.centroid.x.round(8)
        elif source == "centroid_y":
            out[name] = out.geometry.centroid.y.round(8)
        elif source == "index":
            out[name] = np.arange(1, len(out) + 1)
        else:
            raise UsageError(f"unknown add_field source '{source}'")
    return out


def op_rename(gdf: Any, params: Dict[str, Any]) -> Any:
    mapping = params["mapping"]
    return gdf.rename(columns=mapping)


def op_buffer(gdf: Any, params: Dict[str, Any]) -> Any:
    distance = float(params["distance"])
    out = gdf.copy()
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        out["geometry"] = out.geometry.buffer(distance)
    return out


TRANSFORM_OPS: Dict[str, Callable[[Any, Dict[str, Any]], Any]] = {
    "filter_bbox": op_filter_bbox,
    "filter_attribute": op_filter_attribute,
    "reproject": op_reproject,
    "add_field": op_add_field,
    "rename": op_rename,
    "buffer": op_buffer,
}


# ---------------------------------------------------------------------------
# Extract / Load
# ---------------------------------------------------------------------------
def extract_synthetic(bbox: List[float], n: int = 40, seed: int = 42) -> Any:
    import geopandas as gpd
    from shapely.geometry import Polygon
    from pyproj import CRS
    rng = np.random.default_rng(seed)
    w, s, e, n_ = bbox
    geoms, vals = [], []
    for _ in range(n):
        x = rng.uniform(w, e)
        y = rng.uniform(s, n_)
        d = (e - w) * rng.uniform(0.01, 0.04)
        geoms.append(Polygon([(x, y), (x + d, y), (x + d, y + d), (x, y + d), (x, y)]))
        vals.append(float(rng.uniform(0, 100)))
    return gpd.GeoDataFrame(
        {"id": np.arange(1, n + 1), "value": np.round(vals, 3)},
        geometry=geoms, crs=CRS.from_epsg(4326))


def extract_file(path: str) -> Any:
    import geopandas as gpd
    if not os.path.exists(path):
        raise UsageError(f"input vector not found: {path}", path=path)
    try:
        return gpd.read_file(path)
    except Exception as exc:  # noqa: BLE001
        raise ValidationError(f"failed to read '{path}': {exc}") from exc


def load_vector(gdf: Any, path: str, fmt: str) -> str:
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    fmt = fmt.lower()
    if fmt == "geojson":
        if len(gdf) == 0:
            with open(path, "w", encoding="utf-8") as f:
                json.dump({"type": "FeatureCollection", "features": []}, f)
        else:
            gdf.to_file(path, driver="GeoJSON")
    elif fmt in ("gpkg", "geopackage"):
        if os.path.exists(path):
            os.remove(path)
        gdf.to_file(path, layer="etl_output", driver="GPKG")
    else:
        raise UsageError(f"unknown load format '{fmt}'. Choose geojson / gpkg")
    return path


# ---------------------------------------------------------------------------
# 流水线执行与质量报告
# ---------------------------------------------------------------------------
def run_pipeline(config: Dict[str, Any], ctx: PipelineContext) -> PipelineContext:
    """按配置执行 ETL 流水线，逐步记录日志。"""
    # Extract
    t0 = time.perf_counter()
    src = config.get("source", {})
    stype = src.get("type", "synthetic")
    if stype == "file":
        if "path" not in src:
            raise ValidationError("source.type 'file' requires 'path'")
        ctx.gdf = extract_file(src["path"])
        note = f"file:{src['path']}"
    elif stype == "synthetic":
        if "bbox" not in src:
            raise ValidationError("synthetic source requires 'bbox'")
        validate_bbox(src["bbox"], ctx="source bbox")
        ctx.gdf = extract_synthetic(src["bbox"], n=src.get("n", 40))
        note = "synthetic"
    else:
        raise ValidationError(f"unknown source type '{stype}'")
    ctx.initial_count = len(ctx.gdf)
    ctx.log("extract", "extract", 0, len(ctx.gdf), "ok",
            message=note, elapsed_ms=(time.perf_counter() - t0) * 1000)

    # Transform
    for i, step in enumerate(config.get("steps", []), start=1):
        op = step.get("op")
        if op not in TRANSFORM_OPS:
            raise UsageError(f"unknown transform op '{op}'. "
                             f"Choose from: {sorted(TRANSFORM_OPS)}")
        validate_step_params(op, step)
        n_in = len(ctx.gdf)
        t0 = time.perf_counter()
        try:
            ctx.gdf = TRANSFORM_OPS[op](ctx.gdf, step)
            ctx.log(f"t{i}", op, n_in, len(ctx.gdf), "ok",
                    elapsed_ms=(time.perf_counter() - t0) * 1000)
        except GeoSkillError:
            raise
        except Exception as exc:  # noqa: BLE001
            ctx.log(f"t{i}", op, n_in, n_in, "error", message=str(exc),
                    elapsed_ms=(time.perf_counter() - t0) * 1000)
            raise ProcessError(f"transform step {op} failed: {exc}") from exc

    # Load
    load_cfg = config.get("load")
    if load_cfg:
        t0 = time.perf_counter()
        n_in = len(ctx.gdf)
        path = load_vector(ctx.gdf, load_cfg["path"], load_cfg.get("format", "geojson"))
        ctx.log("load", "load", n_in, len(ctx.gdf), "ok",
                message=f"{load_cfg.get('format', 'geojson')}:{path}",
                elapsed_ms=(time.perf_counter() - t0) * 1000)
    return ctx


def quality_report(ctx: PipelineContext) -> Dict[str, Any]:
    """汇总质量报告：要素增减、空值比例、CRS。"""
    gdf = ctx.gdf
    final_count = len(gdf)
    dropped = ctx.initial_count - final_count
    attr_cols = [c for c in gdf.columns if c != "geometry"]
    nulls = {}
    for c in attr_cols:
        n = int(gdf[c].isna().sum())
        nulls[c] = round(n / final_count, 4) if final_count else 0.0
    invalid_geom = int(sum(1 for g in gdf.geometry if g is None or not g.is_valid))
    return {
        "initial_features": int(ctx.initial_count),
        "final_features": int(final_count),
        "dropped_features": int(dropped),
        "retention": round(final_count / ctx.initial_count, 4) if ctx.initial_count else 0.0,
        "null_fractions": nulls,
        "invalid_geometries": invalid_geom,
        "crs": (gdf.crs.to_string() if gdf.crs is not None else None),
        "n_steps": len(ctx.logs),
    }


def default_config(bbox: List[float], output_dir: str, n: int = 40) -> Dict[str, Any]:
    return {
        "source": {"type": "synthetic", "bbox": bbox, "n": n},
        "steps": [
            {"op": "add_field", "name": "area", "source": "area"},
            {"op": "add_field", "name": "cx", "source": "centroid_x"},
            {"op": "filter_attribute", "field": "value", "cmp": ">", "value": 20},
            {"op": "rename", "mapping": {"id": "feature_id"}},
        ],
        "load": {"format": "geojson",
                 "path": os.path.join(output_dir, "etl_output.geojson")},
    }


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
            "config": getattr(args, "config", None),
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

    if args.config:
        if not os.path.exists(args.config):
            raise UsageError(f"config file not found: {args.config}", path=args.config)
        try:
            with open(args.config, encoding="utf-8") as f:
                config = json.load(f)
        except (OSError, ValueError) as exc:
            raise ValidationError(
                f"failed to parse config '{args.config}': {exc}") from exc
        if not isinstance(config, dict):
            raise ValidationError(f"config '{args.config}' must be a JSON object")
    elif args.input and not args.synthetic:
        config = {
            "source": {"type": "file", "path": args.input},
            "steps": [{"op": "add_field", "name": "area", "source": "area"}],
            "load": {"format": "geojson",
                     "path": os.path.join(output_dir, "etl_output.geojson")},
        }
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic), --input, or --config")
        if args.features < 1:
            raise ValidationError(f"--features must be >= 1 (got {args.features})")
        validate_bbox(bbox)
        config = default_config(bbox, output_dir, n=args.features)

    ctx = PipelineContext()
    run_pipeline(config, ctx)
    report = quality_report(ctx)

    os.makedirs(output_dir, exist_ok=True)
    etl_report = {
        "skill": SKILL_NAME,
        "quality": report,
        "steps": ctx.logs,
        "config": config,
    }
    report_path = os.path.join(output_dir, "etl_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(etl_report, f, ensure_ascii=False, indent=2, default=str)

    outputs = [{"path": report_path, "kind": "json"}]
    if config.get("load"):
        outputs.insert(0, {"path": config["load"]["path"], "kind": "vector",
                           "feature_count": report["final_features"]})
    man_path = write_manifest(output_dir, args, outputs, report, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] steps executed: {len(ctx.logs)}")
        for log in ctx.logs:
            print(f"[{SKILL_NAME}]   {log['step']:>8} {log['op']:<18} "
                  f"{log['features_in']} -> {log['features_out']} [{log['status']}]")
        print(f"[{SKILL_NAME}] features: {report['initial_features']} -> "
              f"{report['final_features']}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Config-driven spatial ETL pipeline with per-step logging and QA.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input vector file (extract source)")
    p.add_argument("--config", help="pipeline config JSON file")
    p.add_argument("--features", type=int, default=40,
                   help="number of synthetic features (default: 40)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate synthetic polygon features (offline)")
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
