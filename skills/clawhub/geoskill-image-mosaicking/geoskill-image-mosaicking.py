#!/usr/bin/env python3
"""image-mosaicking — 无缝影像镶嵌

把多幅相邻且互相重叠的瓦片拼接为一幅无缝镶嵌影像。重叠区采用两种融合策略：

- **average**（均值融合）：重叠像元取各瓦片的算术平均。简单、无缝，但在
  辐射不一致时可能出现平均色。
- **feather**（羽化融合）：每个瓦片的权重随"到瓦片边缘的距离"线性增大，
  越靠瓦片内部权重越高。重叠区按权重归一化加权平均，接缝过渡平滑自然。

输出为与输入地理范围一致的镶嵌 GeoTIFF，无数据区填 nodata。

数据源：本地多幅 GeoTIFF（``--inputs`` 目录），或使用 ``--synthetic`` 生成
两幅重叠瓦片用于离线测试。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python image-mosaicking.py --inputs ./tiles --method feather
    python image-mosaicking.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "image-mosaicking"


# ---------------------------------------------------------------------------
# 校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox) -> None:
    """Validate geographic bbox. Raise ValidationError -> exit 6.

    Rules:
        - 4 floats, W<S, W<=E, S<=N,  -180<=W,E<=180,  -90<=S,N<=90
        - width/height > 1e-9 (non-degenerate)
    Anti-meridian wrap (W>E) is not supported: clearly error out, do not silently
    wrap or produce garbage.
    """
    if bbox is None or len(bbox) != 4:
        raise ValidationError("bbox must be 4 floats [W S E N]")
    try:
        W, S, E, N = [float(v) for v in bbox]
    except (TypeError, ValueError) as exc:
        raise ValidationError(f"bbox values must be numeric: {bbox}") from exc
    if not (-180.0 <= W <= 180.0 and -180.0 <= E <= 180.0):
        raise ValidationError(f"bbox lon out of range [-180,180]: W={W} E={E}")
    if not (-90.0 <= S <= 90.0 and -90.0 <= N <= 90.0):
        raise ValidationError(f"bbox lat out of range [-90,90]: S={S} N={N}")
    if W >= E:
        raise ValidationError(
            f"bbox W>=E ({W}>={E}); crossing 180° not supported, please split"
        )
    if S >= N:
        raise ValidationError(f"bbox S>=N ({S}>={N})")
    if (E - W) < 1e-9 or (N - S) < 1e-9:
        raise ValidationError("bbox has zero or negative area")

# ---- 复用共享核心库（本地 vendored，随脚本目录一起分发）----
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
# 核心算法
# ---------------------------------------------------------------------------
def _feather_weight(th: int, tw: int) -> np.ndarray:
    """生成 (th, tw) 的羽化权重：到瓦片边缘越远（越靠内部）权重越大。"""
    rows = np.arange(th, dtype=np.float32)
    cols = np.arange(tw, dtype=np.float32)
    dr = np.minimum(rows, (th - 1) - rows)
    dc = np.minimum(cols, (tw - 1) - cols)
    w = np.minimum(dr[:, None], dc[None, :]) + 1.0
    return w


def mosaic(
    tiles: List[np.ndarray],
    offsets: List[Tuple[int, int]],
    canvas_shape: Tuple[int, int],
    method: str = "feather",
) -> np.ndarray:
    """把多幅瓦片镶嵌到统一画布上。

    参数
    ----
    tiles   : list of (bands, th, tw) 瓦片
    offsets : list of (row_off, col_off) 各瓦片左上角在画布中的位置
    canvas_shape : (H, W)
    method  : "average" | "feather"

    返回镶嵌结果 (bands, H, W)，无覆盖像元为 nan。
    """
    if method not in ("average", "feather"):
        raise UsageError(
            f"unknown method '{method}'. Choose from: average, feather", method=method,
        )
    if len(tiles) == 0:
        raise ValidationError("no tiles to mosaic")
    if len(tiles) != len(offsets):
        raise ValidationError(
            f"tiles ({len(tiles)}) and offsets ({len(offsets)}) length mismatch"
        )

    nb = tiles[0].shape[0]
    H, W = canvas_shape
    acc = np.zeros((nb, H, W), dtype=np.float64)
    wsum = np.zeros((H, W), dtype=np.float64)

    for tile, (r0, c0) in zip(tiles, offsets):
        tile = np.asarray(tile, dtype=np.float64)
        if tile.ndim != 3:
            raise ValidationError("each tile must be 3-D (bands, th, tw)")
        if tile.shape[0] != nb:
            raise ValidationError("all tiles must have the same band count")
        th, tw = tile.shape[1], tile.shape[2]
        if r0 < 0 or c0 < 0 or r0 + th > H or c0 + tw > W:
            raise ValidationError(
                f"tile at offset ({r0},{c0}) size ({th},{tw}) exceeds canvas ({H},{W})"
            )

        if method == "average":
            w = np.ones((th, tw), dtype=np.float64)
        else:
            w = _feather_weight(th, tw).astype(np.float64)

        acc[:, r0:r0 + th, c0:c0 + tw] += tile * w[None, ...]
        wsum[r0:r0 + th, c0:c0 + tw] += w

    out = np.full((nb, H, W), np.nan, dtype=np.float32)
    valid = wsum > 0
    for b in range(nb):
        out[b][valid] = (acc[b][valid] / wsum[valid]).astype(np.float32)
    return out


# ---------------------------------------------------------------------------
# 合成数据：两幅重叠瓦片（离线测试）
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    bands: int = 3,
    width: int = 128,
    height: int = 128,
    seed: int = 42,
) -> Tuple[List[np.ndarray], List[Tuple[int, int]], Tuple[int, int], Dict[str, Any]]:
    """生成一幅完整影像并切成左右两幅重叠瓦片。

    返回 (tiles, offsets, canvas_shape, info)。info 内含真值影像用于 QA 对比。
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    yn = yy.astype(np.float32) / max(height - 1, 1)
    xn = xx.astype(np.float32) / max(width - 1, 1)

    truth = np.zeros((bands, height, width), dtype=np.float32)
    for b in range(bands):
        base = 0.15 + 0.4 * xn + 0.25 * yn + 0.08 * b / max(bands - 1, 1)
        base = base + rng.normal(0, 0.01, size=base.shape).astype(np.float32)
        truth[b] = np.clip(base, 0.0, 1.0)

    # 左右两幅瓦片，中间重叠 32 列
    overlap = 32
    split = width // 2
    left_end = split + overlap // 2     # 左瓦片覆盖 [0, left_end)
    right_start = split - overlap // 2  # 右瓦片覆盖 [right_start, width)

    left = truth[:, :, 0:left_end].copy()
    right = truth[:, :, right_start:width].copy()

    tiles = [left, right]
    offsets = [(0, 0), (0, right_start)]
    canvas_shape = (height, width)

    info = {
        "bbox": bbox,
        "bands": bands,
        "canvas_shape": list(canvas_shape),
        "n_tiles": 2,
        "overlap_cols": int(left_end - right_start),
        "truth_mean_per_band": [float(np.mean(truth[b])) for b in range(bands)],
    }
    # 附带真值，供主流程做 QA 对比
    info["_truth"] = truth
    return tiles, offsets, canvas_shape, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O（直接用 rasterio，保证离线可用）
# ---------------------------------------------------------------------------
def write_geotiff(
    path: str,
    cube: np.ndarray,
    bbox: List[float],
    nodata: float = -9999.0,
) -> None:
    import rasterio
    from rasterio.transform import from_bounds

    if cube.ndim == 2:
        cube = cube[np.newaxis, ...]
    nb, h, w = cube.shape
    cube = np.where(np.isfinite(cube), cube, nodata).astype(np.float32)
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    profile = {
        "driver": "GTiff", "height": h, "width": w, "count": nb,
        "dtype": "float32", "crs": "EPSG:4326", "transform": transform,
        "nodata": nodata, "compress": "deflate",
    }
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(cube[b], b + 1)


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float]]:
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read(masked=True).astype(np.float32)
        cube = np.ma.filled(cube, np.nan)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return cube, bbox


def load_tiles_from_dir(inputs_dir: str) -> Tuple[List[np.ndarray], List[Tuple[int, int]], Tuple[int, int], List[float]]:
    """从目录读取所有 .tif，按其 bounds 对齐到公共像素网格，返回瓦片+偏移。

    简化处理：以所有瓦片的外包 bbox 为画布，按各瓦片 bounds 计算像素偏移
    （取最左上角为原点，按最小分辨率对齐）。用于真实多景拼接。
    """
    import glob as _glob
    paths = sorted(_glob.glob(os.path.join(inputs_dir, "*.tif")))
    if not paths:
        raise UsageError(f"no .tif tiles found in: {inputs_dir}", path=inputs_dir)

    tiles: List[np.ndarray] = []
    bounds_list: List[List[float]] = []
    for p in paths:
        cube, bbox = read_geotiff(p)
        tiles.append(cube)
        bounds_list.append(bbox)

    nb = tiles[0].shape[0]
    # 外包 bbox
    W0 = min(b[0] for b in bounds_list)
    S0 = min(b[1] for b in bounds_list)
    E0 = max(b[2] for b in bounds_list)
    N0 = max(b[3] for b in bounds_list)

    # 取最高分辨率（最小像元尺寸）作为画布分辨率
    res_xs, res_ys = [], []
    for t, b in zip(tiles, bounds_list):
        res_xs.append((b[2] - b[0]) / t.shape[2])
        res_ys.append((b[3] - b[1]) / t.shape[1])
    res_x = min(res_xs)
    res_y = min(res_ys)

    H = int(round((N0 - S0) / res_y))
    W = int(round((E0 - W0) / res_x))
    H = max(H, 1)
    W = max(W, 1)

    offsets: List[Tuple[int, int]] = []
    placed: List[np.ndarray] = []
    for t, b in zip(tiles, bounds_list):
        c0 = int(round((b[0] - W0) / res_x))
        r0 = int(round((N0 - b[3]) / res_y))
        th, tw = t.shape[1], t.shape[2]
        # 裁剪越界部分
        r0c = max(r0, 0)
        c0c = max(c0, 0)
        tr = r0c - r0
        tc = c0c - c0
        t_crop = t[:, tr:tr + (H - r0c), tc:tc + (W - c0c)]
        if t_crop.shape[1] == 0 or t_crop.shape[2] == 0:
            continue
        placed.append(t_crop)
        offsets.append((r0c, c0c))

    if not placed:
        raise ValidationError("no tiles could be placed on the canvas")
    if any(p.shape[0] != nb for p in placed):
        raise ValidationError("tiles have inconsistent band counts")

    return placed, offsets, (H, W), [W0, S0, E0, N0]


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
    bbox: List[float],
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
            "inputs": getattr(args, "inputs", None),
            "method": getattr(args, "method", None),
            "synthetic": bool(getattr(args, "synthetic", False)),
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
    synth_info: Optional[Dict[str, Any]] = None

    # Validate bbox BEFORE creating output directory.
    if bbox is not None:
        validate_bbox(bbox)

    os.makedirs(output_dir, exist_ok=True)

    # 1) 获取瓦片
    if args.inputs and not args.synthetic:
        tiles, offsets, canvas_shape, bbox = load_tiles_from_dir(args.inputs)
        # Real-data bbox already validated inside load_tiles_from_dir (it builds
        # it from per-tile bounds); still call validate_bbox for consistency.
        validate_bbox(bbox)
        source_note = args.inputs
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --inputs <dir>")
        tiles, offsets, canvas_shape, synth_info = generate_synthetic(bbox)
        source_note = "synthetic"

    # 2) 镶嵌
    mosaic_cube = mosaic(tiles, offsets, canvas_shape, method=args.method)

    coverage = float(np.mean(np.isfinite(mosaic_cube[0])))
    if coverage <= 0:
        raise ValidationError("mosaic produced no valid pixels")

    # 3) 写出产物
    out_tif = os.path.join(output_dir, "mosaic.tif")
    write_geotiff(out_tif, mosaic_cube, bbox)

    # QA
    qa: Dict[str, Any] = {
        "source": source_note,
        "method": args.method,
        "n_tiles": len(tiles),
        "canvas_shape": list(canvas_shape),
        "coverage_fraction": coverage,
        "mean_value_per_band": [
            float(np.nanmean(mosaic_cube[b])) for b in range(mosaic_cube.shape[0])
        ],
    }
    if synth_info is not None:
        qa["overlap_cols"] = synth_info["overlap_cols"]
        truth = synth_info.get("_truth")
        if truth is not None:
            diff = np.abs(mosaic_cube - truth)
            qa["reconstruction_max_abs_err"] = float(np.nanmax(diff))
            qa["reconstruction_mean_abs_err"] = float(np.nanmean(diff))
            qa["synthetic_truth_mean_per_band"] = synth_info["truth_mean_per_band"]

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": int(mosaic_cube.shape[0])},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] method: {args.method}  tiles: {len(tiles)}")
        print(f"[{SKILL_NAME}] canvas: {canvas_shape}  coverage: {coverage:.3f}")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Seamless image mosaicking with average / feather blending.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--inputs", help="directory of input GeoTIFF tiles")
    p.add_argument("--method", default="feather", choices=["average", "feather"],
                   help="overlap blending method (default: feather)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate two overlapping synthetic tiles (offline)")
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
