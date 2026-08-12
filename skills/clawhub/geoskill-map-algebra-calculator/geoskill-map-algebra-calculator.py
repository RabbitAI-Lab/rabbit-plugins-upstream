#!/usr/bin/env python3
"""map-algebra-calculator — 地图代数计算器

对多波段栅格做地图代数运算。用一个基于 Python ``ast`` 的**安全表达式求值器**
支持波段引用（b1..bN）、四则运算、幂、常用数学函数与常量，内置 NDVI / NDWI /
SAVI 等预设指数。表达式经白名单校验，拒绝任何属性访问、导入或非白名单调用。

数据源：本地多波段 GeoTIFF，或 ``--synthetic`` 生成 4 波段（蓝/绿/红/近红外）
含植被-土壤-水体的模拟影像用于离线测试。

隐私声明 / Privacy：完全离线；所有处理本地完成，不上传用户数据。

Usage:
    python map-algebra-calculator.py --input scene.tif --expr "(b4-b3)/(b4+b3)"
    python map-algebra-calculator.py --bbox 116 39 117 40 --synthetic --preset ndvi

License: MIT
"""
from __future__ import annotations

import argparse
import ast
import datetime as _dt
import json
import os
import sys
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

VERSION = "1.0.0"
SKILL_NAME = "map-algebra-calculator"

try:
    from _geoskill_core.errors import (
        GeoSkillError, UsageError, ValidationError, ProcessError, to_exit_code,
    )
    from _geoskill_core.manifest import OutputManifest, OutputFile
except ImportError:  # pragma: no cover
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


# 预设指数（{red}/{nir}/{green}/{blue} 会被替换为 bN 波段引用）
PRESETS: Dict[str, str] = {
    "ndvi": "({nir} - {red}) / ({nir} + {red})",
    "ndwi": "({green} - {nir}) / ({green} + {nir})",
    "savi": "(({nir} - {red}) / ({nir} + {red} + 0.5)) * 1.5",
    "brightness": "({red} + {green} + {blue}) / 3.0",
    "evi": "2.5 * (({nir} - {red}) / ({nir} + 6.0 * {red} - 7.5 * {blue} + 1.0))",
}

# 白名单函数
_FUNCS = {
    "sqrt": np.sqrt, "abs": np.abs, "exp": np.exp,
    "log": np.log, "log10": np.log10, "log2": np.log2,
    "sin": np.sin, "cos": np.cos, "tan": np.tan,
    "minimum": np.minimum, "maximum": np.maximum, "clip": np.clip,
    "square": np.square, "sign": np.sign,
}
_CONSTS = {"pi": float(np.pi), "e": float(np.e)}


def validate_bbox(bbox) -> None:
    """校验 bbox 是 W<E、S<N、lon∈[-180,180]、lat∈[-90,90]、非零面积。
    跨 180° 经线必须拆成两个子 bbox。"""
    if bbox is None:
        raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
    w, s, e, n = [float(v) for v in bbox]
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"bbox longitude out of range [-180, 180]: W={w}, E={e}",
            bbox=list(bbox),
        )
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"bbox latitude out of range [-90, 90]: S={s}, N={n}",
            bbox=list(bbox),
        )
    if w >= e:
        if w == e:
            raise ValidationError(
                f"bbox has zero width: W==E=={w} (degenerate AOI)",
                bbox=list(bbox),
            )
        raise ValidationError(
            f"bbox is reversed (W={w} >= E={e}); need W < E. "
            f"For datelines that cross 180° (e.g. 179.5 -> -179.5), "
            f"split into two sub-bboxes and run the skill on each separately.",
            bbox=list(bbox),
        )
    if s >= n:
        raise ValidationError(
            f"bbox is reversed (S={s} >= N={n}); need S < N",
            bbox=list(bbox),
        )


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# 核心算法：安全表达式求值（ast 白名单）
# ---------------------------------------------------------------------------
def _safe_div(a: Any, b: Any) -> Any:
    """逐像元除法，分母为 0 处结果为 0（避免 inf/nan）。"""
    a = np.asarray(a, dtype=np.float32)
    b = np.asarray(b, dtype=np.float32)
    shape = np.broadcast_shapes(a.shape, b.shape)
    out = np.zeros(shape, dtype=np.float32)
    return np.divide(a, b, out=out, where=(b != 0))


def _eval_node(node: ast.AST, bands: Dict[str, np.ndarray]) -> Any:
    if isinstance(node, ast.Expression):
        return _eval_node(node.body, bands)
    if isinstance(node, ast.BinOp):
        left = _eval_node(node.left, bands)
        right = _eval_node(node.right, bands)
        op = type(node.op)
        if op is ast.Add:
            return np.add(left, right)
        if op is ast.Sub:
            return np.subtract(left, right)
        if op is ast.Mult:
            return np.multiply(left, right)
        if op is ast.Div:
            return _safe_div(left, right)
        if op is ast.Pow:
            return np.power(np.asarray(left, dtype=np.float32), right)
        if op is ast.Mod:
            return np.mod(np.asarray(left, dtype=np.float32), right)
        raise UsageError(f"unsupported operator: {op.__name__}")
    if isinstance(node, ast.UnaryOp):
        val = _eval_node(node.operand, bands)
        if isinstance(node.op, ast.USub):
            return -np.asarray(val, dtype=np.float32)
        if isinstance(node.op, ast.UAdd):
            return +np.asarray(val, dtype=np.float32)
        raise UsageError(f"unsupported unary operator: {type(node.op).__name__}")
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return float(node.value)
        raise UsageError(f"unsupported constant type: {type(node.value).__name__}")
    if isinstance(node, ast.Name):
        name = node.id
        if name in bands:
            return bands[name]
        if name in _CONSTS:
            return _CONSTS[name]
        raise UsageError(f"unknown variable '{name}'", variable=name)
    if isinstance(node, ast.Call):
        if not isinstance(node.func, ast.Name):
            raise UsageError("only direct whitelisted function calls are allowed")
        fname = node.func.id
        if fname not in _FUNCS:
            raise UsageError(f"function '{fname}' not allowed", function=fname)
        if node.keywords:
            raise UsageError("keyword arguments are not allowed")
        args = [_eval_node(a, bands) for a in node.args]
        return _FUNCS[fname](*args)
    raise UsageError(f"unsupported expression element: {type(node).__name__}")


def evaluate_expression(expr: str, bands: Dict[str, np.ndarray]) -> np.ndarray:
    """安全求值地图代数表达式，返回 2D float32 数组。

    仅允许数字常量、波段名 (b1..bN)、pi/e、白名单函数与基本运算符。
    属性访问、下标、导入、lambda、比较等均被拒绝。
    """
    if not expr or not expr.strip():
        raise UsageError("empty expression")
    try:
        tree = ast.parse(expr, mode="eval")
    except SyntaxError as exc:
        raise UsageError(f"invalid expression syntax: {exc}", expr=expr)
    result = _eval_node(tree, bands)
    result = np.asarray(result, dtype=np.float32)
    if result.ndim == 0:
        raise ValidationError("expression did not produce a raster (scalar result)")
    result = np.nan_to_num(result, nan=0.0, posinf=0.0, neginf=0.0)
    return result.astype(np.float32)


def build_preset_expression(
    preset: str, red: int = 3, nir: int = 4, green: int = 2, blue: int = 1
) -> str:
    """把预设指数模板中的 {red}/{nir}/... 替换为 bN 波段引用。"""
    if preset not in PRESETS:
        raise UsageError(f"unknown preset '{preset}'. Choose: {sorted(PRESETS)}", preset=preset)
    repl = {"red": f"b{red}", "nir": f"b{nir}", "green": f"b{green}", "blue": f"b{blue}"}
    tmpl = PRESETS[preset]
    for k, v in repl.items():
        tmpl = tmpl.replace("{" + k + "}", v)
    return tmpl


# ---------------------------------------------------------------------------
# 合成数据：4 波段（蓝/绿/红/近红外）植被-土壤-水体影像
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float], width: int = 64, height: int = 64, seed: int = 42
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """返回 (4, H, W) 反射率式影像。左=水体，中=土壤，右=植被。"""
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    xx = xx / max(width - 1, 1)
    # 分区：xx<0.33 水，0.33..0.66 土壤，>0.66 植被
    water = (xx < 0.33).astype(np.float32)
    veg = (xx > 0.66).astype(np.float32)
    soil = np.clip(1.0 - water - veg, 0.0, 1.0)
    # 各波段反射率真值（蓝 绿 红 近红外）
    truth = {
        "blue": water * 0.06 + soil * 0.10 + veg * 0.03,
        "green": water * 0.05 + soil * 0.14 + veg * 0.09,
        "red": water * 0.03 + soil * 0.18 + veg * 0.04,
        "nir": water * 0.01 + soil * 0.22 + veg * 0.45,
    }
    order = ["blue", "green", "red", "nir"]
    cube = np.zeros((4, height, width), dtype=np.float32)
    for i, name in enumerate(order):
        noise = rng.normal(0, 0.004, size=(height, width)).astype(np.float32)
        cube[i] = np.clip(truth[name] + noise, 0.0, 1.0)
    info = {"bbox": bbox, "width": width, "height": height,
            "bands": order, "kind": "synthetic-multispectral",
            "zones": ["water(x<0.33)", "soil(0.33-0.66)", "vegetation(x>0.66)"]}
    return cube, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(path, cube, bbox, nodata=-9999.0):
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


def read_geotiff(path):
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return cube, bbox


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------
def write_manifest(output_dir, args, outputs, qa, started_at, exit_code, bbox):
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME, skill_version=VERSION, command=cmd,
        started_at=started_at, finished_at=_utc_now(), exit_code=exit_code,
        inputs={"input": getattr(args, "input", None),
                "expr": getattr(args, "expr", None),
                "preset": getattr(args, "preset", None),
                "synthetic": bool(getattr(args, "synthetic", False))},
        outputs=[OutputFile(**o) for o in outputs], qa=qa,
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

    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        validate_bbox(bbox)
        source_note = args.input
    else:
        validate_bbox(bbox)
        cube, synth_info = generate_synthetic(bbox)
        source_note = "synthetic"

    if cube.size == 0:
        raise ValidationError("input raster is empty")
    if bbox is None:
        raise UsageError("could not determine bbox")
    if cube.ndim == 2:
        cube = cube[np.newaxis, ...]

    # 校验通过后再建输出目录
    os.makedirs(output_dir, exist_ok=True)

    nb = cube.shape[0]
    bands = {f"b{i + 1}": cube[i].astype(np.float32) for i in range(nb)}

    # 确定表达式
    if args.expr:
        expr = args.expr
        preset_used = None
    else:
        preset_used = args.preset
        if nb < max(args.red, args.nir, args.green, args.blue):
            raise ValidationError(
                f"preset '{args.preset}' needs band index up to "
                f"{max(args.red, args.nir, args.green, args.blue)} but input has {nb} bands")
        expr = build_preset_expression(args.preset, args.red, args.nir, args.green, args.blue)

    result = evaluate_expression(expr, bands)

    out_tif = os.path.join(output_dir, "result.tif")
    write_geotiff(out_tif, result, bbox)

    meta = {"source": source_note, "expression": expr, "preset": preset_used,
            "n_bands": int(nb), "bbox": bbox,
            "shape": [int(result.shape[0]), int(result.shape[1])],
            "result_min": float(np.nanmin(result)), "result_max": float(np.nanmax(result)),
            "result_mean": float(np.nanmean(result)), "generated_at": _utc_now()}
    if synth_info is not None:
        meta["synthetic"] = synth_info
    meta_path = os.path.join(output_dir, "expression_meta.json")
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    qa = {"source": source_note, "expression": expr, "preset": preset_used,
          "result_min": meta["result_min"], "result_max": meta["result_max"],
          "result_mean": meta["result_mean"], "bbox": bbox}
    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": meta_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}  bands: {nb}")
        print(f"[{SKILL_NAME}] expr: {expr}")
        print(f"[{SKILL_NAME}] result range: [{meta['result_min']:.4f}, {meta['result_max']:.4f}]  mean: {meta['result_mean']:.4f}")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Evaluate map-algebra band-math expressions (e.g. NDVI) on rasters.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='Example: --expr "(b4-b3)/(b4+b3)"  or  --preset ndvi',
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"))
    p.add_argument("--input", help="input multi-band GeoTIFF")
    p.add_argument("--expr", help="band-math expression using b1..bN (overrides --preset)")
    p.add_argument("--preset", default="ndvi", choices=sorted(PRESETS.keys()),
                   help="index preset (default: ndvi)")
    p.add_argument("--red", type=int, default=3, help="red band index (1-based, default 3)")
    p.add_argument("--nir", type=int, default=4, help="nir band index (1-based, default 4)")
    p.add_argument("--green", type=int, default=2, help="green band index (default 2)")
    p.add_argument("--blue", type=int, default=1, help="blue band index (default 1)")
    p.add_argument("--synthetic", action="store_true")
    p.add_argument("--output-dir", default="./output")
    p.add_argument("--quiet", action="store_true")
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
