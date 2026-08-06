#!/usr/bin/env python3
"""sandstorm-source-identification — 沙尘暴源区识别

综合地表与气象条件识别沙尘暴源区：

- **植被覆盖**：NDVI 越低，地表越缺保护，越易起沙
- **裸土比例**：裸土越多，可蚀物质越丰富
- **风速超阈值**：风速超过起沙阈值才产生粉尘排放（风 excess 驱动）
- **后向轨迹权重**：相对下游受体位于上风方的像元贡献更大

粉尘排放潜势（[0,1]，绝对物理缩放，非归一化）：

    P = bare · clip(1 - NDVI/0.4, 0,1) · clip((V - V_thr)/10, 0,1)

源区掩膜 = {NDVI < NDVI_thr} ∩ {bare ≥ bare_thr} ∩ {V > V_thr}。

数据源：本地多波段 GeoTIFF（band1=NDVI、band2=裸土比例、band3=风速 m/s），
或 ``--synthetic`` 生成干旱区场景。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python sandstorm-source-identification.py --input scene.tif --threshold 6
    python sandstorm-source-identification.py --bbox 80 40 81 41 --synthetic --output-dir ./out

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
SKILL_NAME = "sandstorm-source-identification"

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


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def vegetation_protection(ndvi: np.ndarray, ndvi_full: float = 0.4) -> np.ndarray:
    """缺植被保护程度（[0,1]）：NDVI 越低越易起沙，NDVI≥ndvi_full 时为 0。"""
    n = np.asarray(ndvi, dtype=np.float64)
    return np.clip(1.0 - n / float(ndvi_full), 0.0, 1.0).astype(np.float32)


def wind_excess_factor(wind_speed: np.ndarray, threshold: float, scale: float = 10.0) -> np.ndarray:
    """风速超阈值因子（[0,1]）：低于阈值=0（不起沙），超出越多越大，scale 处饱和。"""
    v = np.asarray(wind_speed, dtype=np.float64)
    return np.clip((v - float(threshold)) / float(scale), 0.0, 1.0).astype(np.float32)


def dust_emission_potential(ndvi: np.ndarray, bare_soil: np.ndarray, wind_speed: np.ndarray,
                            threshold: float) -> np.ndarray:
    """粉尘排放潜势（[0,1]）= 裸土 × 缺植被保护 × 风超阈值。

    对风速(阈值以上)与裸土单调增，对 NDVI 单调减；风速≤阈值时潜势为 0。
    """
    if not (ndvi.shape == bare_soil.shape == wind_speed.shape):
        raise ValidationError("ndvi/bare_soil/wind_speed shape mismatch")
    bare = np.clip(np.asarray(bare_soil, dtype=np.float64), 0.0, 1.0)
    p = bare * vegetation_protection(ndvi) * wind_excess_factor(wind_speed, threshold)
    return np.clip(p, 0.0, 1.0).astype(np.float32)


def identify_sources(ndvi: np.ndarray, bare_soil: np.ndarray, wind_speed: np.ndarray,
                     threshold: float, ndvi_thresh: float = 0.15, bare_thresh: float = 0.5) -> np.ndarray:
    """源区掩膜：低植被 + 高裸土 + 风速超阈值。"""
    if not (ndvi.shape == bare_soil.shape == wind_speed.shape):
        raise ValidationError("ndvi/bare_soil/wind_speed shape mismatch")
    mask = ((np.asarray(ndvi) < ndvi_thresh)
            & (np.asarray(bare_soil) >= bare_thresh)
            & (np.asarray(wind_speed) > threshold))
    return mask.astype(bool)


def trajectory_weight(shape: Tuple[int, int], receptor_rc: Tuple[float, float],
                      wind_dir_deg: float) -> np.ndarray:
    """后向轨迹权重（[0,1]）：相对受体位于上风方的像元权重高，下风方为 0。

    wind_dir_deg 为风的去向（罗盘角，自北顺时针）。
    """
    H, W = shape
    theta = np.deg2rad(float(wind_dir_deg))
    tr_row, tr_col = -np.cos(theta), np.sin(theta)  # 输送方向（row 向下, col 向东）
    yy, xx = np.mgrid[0:H, 0:W]
    vr = receptor_rc[0] - yy
    vc = receptor_rc[1] - xx
    dist = np.hypot(vr, vc)
    dist = np.where(dist < 1e-9, 1e-9, dist)
    align = (vr * tr_row + vc * tr_col) / dist
    return np.clip(align, 0.0, 1.0).astype(np.float32)


# ---------------------------------------------------------------------------
# 合成数据：干旱区（西北荒漠低 NDVI 高裸土 大风，东南绿洲相反）
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], width: int = 64, height: int = 64,
                       seed: int = 42) -> Tuple[Dict[str, np.ndarray], Dict[str, Any]]:
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    xn = xx.astype(np.float64) / max(width - 1, 1)
    yn = yy.astype(np.float64) / max(height - 1, 1)
    ndvi = np.clip(0.05 + 0.5 * (xn + yn) / 2.0 + rng.normal(0, 0.02, (height, width)), 0, 0.8)
    bare = np.clip(0.9 - 0.7 * (xn + yn) / 2.0 + rng.normal(0, 0.03, (height, width)), 0, 1)
    wind = np.clip(9.0 - 4.0 * xn + rng.normal(0, 0.5, (height, width)), 0, 20)
    layers = {"ndvi": ndvi.astype(np.float32), "bare_soil": bare.astype(np.float32),
              "wind_speed": wind.astype(np.float32)}
    info = {"bbox": bbox, "width": width, "height": height, "max_wind": float(wind.max())}
    return layers, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(path: str, cube: np.ndarray, bbox: List[float],
                  nodata: float = -9999.0, dtype: str = "float32") -> None:
    import rasterio
    from rasterio.transform import from_bounds
    if cube.ndim == 2:
        cube = cube[np.newaxis, ...]
    nb, h, w = cube.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    profile = {"driver": "GTiff", "height": h, "width": w, "count": nb,
               "dtype": dtype, "crs": "EPSG:4326", "transform": transform,
               "nodata": nodata, "compress": "deflate"}
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(cube[b].astype(dtype), b + 1)


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float]]:
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return cube, bbox


def read_geotiff_full(path: str) -> Tuple[np.ndarray, List[float], Optional[float]]:
    """扩展版 read：同时返回 nodata 值（若无则为 None）。"""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nodata = src.nodata
        if nodata is not None:
            nodata = float(nodata)
    return cube, bbox, nodata


# ---------------------------------------------------------------------------
# 输入校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox: Optional[List[float]]) -> List[float]:
    """校验地理 bbox 合法性，失败抛 ValidationError（exit 6）。"""
    if bbox is None or len(bbox) != 4:
        raise ValidationError("bbox must be 4 floats [W S E N]")
    try:
        w, s, e, n = [float(x) for x in bbox]
    except (TypeError, ValueError) as exc:
        raise ValidationError(f"bbox entries must be numeric: {exc}")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(f"latitude out of [-90,90]: S={s}, N={n}")
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(f"longitude out of [-180,180]: W={w}, E={e}")
    if s >= n:
        raise ValidationError(
            f"S >= N (S={s}, N={n}); bbox inverted (S must be < N)"
        )
    if w >= e:
        raise ValidationError(
            f"W >= E (W={w}, E={e}); cross-180° bbox not supported. "
            f"Split into two non-antipodal bboxes."
        )
    if (e - w) < 0.001 or (n - s) < 0.001:
        raise ValidationError(
            f"bbox too small ({(e-w):.6f}°×{(n-s):.6f}°); min span is 0.001°"
        )
    return [w, s, e, n]


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------
def write_manifest(output_dir: str, inputs: Dict[str, Any], outputs: List[Dict[str, Any]],
                   qa: Dict[str, Any], started_at: str, exit_code: int) -> Optional[str]:
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME, skill_version=VERSION, command=cmd,
        started_at=started_at, finished_at=_utc_now(), exit_code=exit_code,
        inputs=inputs, outputs=[OutputFile(**o) for o in outputs], qa=qa,
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

    # 校验 CLI 参数（前置）
    if args.threshold < 0:
        raise ValidationError(
            f"--threshold must be >= 0 (wind speed in m/s; got {args.threshold})"
        )
    if not (0.0 <= args.ndvi_thresh <= 1.0):
        raise ValidationError(
            f"--ndvi-thresh must be in [0, 1] (got {args.ndvi_thresh})"
        )
    if not (0.0 <= args.bare_thresh <= 1.0):
        raise ValidationError(
            f"--bare-thresh must be in [0, 1] (got {args.bare_thresh})"
        )
    if not (0.0 <= args.wind_dir < 360.0):
        raise ValidationError(
            f"--wind-dir must be in [0, 360) (got {args.wind_dir})"
        )

    input_nodata: Optional[float] = None
    n_valid_pixels: Optional[int] = None

    if args.input and not args.synthetic:
        cube, file_bbox, src_nodata = read_geotiff_full(args.input)
        input_nodata = src_nodata
        if bbox is not None:
            bbox = validate_bbox(bbox)
        else:
            bbox = validate_bbox(file_bbox)
        if cube.shape[0] < 3:
            raise ValidationError("input needs >=3 bands (ndvi, bare_soil, wind_speed)")
        # NoData 处理
        if src_nodata is not None:
            n_total = int(cube[0].size)
            n_nd = int(np.count_nonzero(cube[0] == src_nodata))
            n_valid_pixels = n_total - n_nd
            if n_valid_pixels == 0:
                raise ValidationError(
                    f"input raster has no valid pixels "
                    f"(all {n_nd}/{n_total} are NoData={src_nodata})",
                    path=args.input, nodata=src_nodata,
                )
            cube = np.where(cube == src_nodata, np.nan, cube).astype(np.float32)
        else:
            n_valid_pixels = int(cube[0].size)
        ndvi, bare, wind = cube[0], cube[1], cube[2]
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        bbox = validate_bbox(bbox)
        layers, _info = generate_synthetic(bbox)
        ndvi, bare, wind = layers["ndvi"], layers["bare_soil"], layers["wind_speed"]
        n_valid_pixels = int(ndvi.size)
        source_note = "synthetic"

    # 校验通过后再建输出目录
    os.makedirs(output_dir, exist_ok=True)

    H, W = ndvi.shape
    potential = dust_emission_potential(ndvi, bare, wind, args.threshold)
    sources = identify_sources(ndvi, bare, wind, args.threshold,
                               ndvi_thresh=args.ndvi_thresh, bare_thresh=args.bare_thresh)
    rec_row = args.receptor_row if args.receptor_row is not None else H / 2.0
    rec_col = args.receptor_col if args.receptor_col is not None else W / 2.0
    receptor = (rec_row, rec_col)
    traj = trajectory_weight((H, W), receptor, args.wind_dir)
    contribution = np.clip(potential * traj, 0, 1).astype(np.float32)

    pot_tif = os.path.join(output_dir, "emission_potential.tif")
    write_geotiff(pot_tif, potential, bbox)
    src_tif = os.path.join(output_dir, "source_mask.tif")
    write_geotiff(src_tif, sources.astype("int16"), bbox, nodata=-1, dtype="int16")
    contrib_tif = os.path.join(output_dir, "source_contribution.tif")
    write_geotiff(contrib_tif, contribution, bbox)

    params = {"source": source_note, "threshold": args.threshold,
              "ndvi_thresh": args.ndvi_thresh, "bare_thresh": args.bare_thresh,
              "wind_dir_deg": args.wind_dir, "receptor_rc": list(receptor)}
    params_path = os.path.join(output_dir, "sandstorm_params.json")
    with open(params_path, "w", encoding="utf-8") as f:
        json.dump(params, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "n_valid_pixels": int(n_valid_pixels) if n_valid_pixels is not None else None,
        "input_nodata": input_nodata,
        "mean_potential": float(potential.mean()),
        "max_potential": float(potential.max()),
        "source_pixels": int(np.count_nonzero(sources)),
        "source_fraction": float(np.mean(sources)),
        "mean_contribution": float(contribution.mean()),
    }
    outputs = [
        {"path": pot_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": src_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": contrib_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": params_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, {"input": args.input, "bbox": bbox, "threshold": args.threshold,
                              "synthetic": bool(args.synthetic),
                              "input_nodata": input_nodata}, outputs, qa, started_at, 0)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] threshold: {args.threshold} m/s  max potential: {qa['max_potential']:.3f}")
        print(f"[{SKILL_NAME}] source pixels: {qa['source_pixels']} ({qa['source_fraction']*100:.1f}%)")
        print(f"[{SKILL_NAME}] outputs: {output_dir}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Sandstorm source identification (NDVI + bare soil + wind threshold + trajectory).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"))
    p.add_argument("--input", help="input GeoTIFF (band1=ndvi, band2=bare soil fraction, band3=wind speed m/s)")
    p.add_argument("--threshold", type=float, default=6.0, help="dust-emission wind threshold (m/s, default: 6)")
    p.add_argument("--ndvi-thresh", type=float, default=0.15, help="NDVI threshold for sparse vegetation (default: 0.15)")
    p.add_argument("--bare-thresh", type=float, default=0.5, help="bare soil fraction threshold (default: 0.5)")
    p.add_argument("--wind-dir", type=float, default=270.0, help="wind transport direction degrees (toward), default: 270")
    p.add_argument("--receptor-row", type=float, default=None, help="receptor row (default: image center)")
    p.add_argument("--receptor-col", type=float, default=None, help="receptor col (default: image center)")
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
