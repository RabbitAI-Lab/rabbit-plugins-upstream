#!/usr/bin/env python3
"""wildfire-spread-modeling — 野火蔓延模拟

基于元胞自动机（CA）的野火蔓延模拟。每个时间步，燃烧像元向 8 邻域未燃像元
以概率点火，点火概率综合：

    p = p0 · 燃料可燃性 · 坡度因子 · 风因子 · 湿度因子
    坡度因子 = 1 + 0.8·slope      （上坡蔓延更快）
    风因子   = exp(k · wind_speed · cosθ)  （顺风 >1，逆风 <1，θ 为蔓延方向与风向夹角）
    湿度因子 = exp(-3·moisture)    （越湿越难点燃）

一旦点燃永不熄灭，故过火面积随时间单调不减。输出最终过火范围与到达时间。

数据源：本地多波段 GeoTIFF（band1=燃料可燃性0-1、band2=湿度0-1、band3=坡度0-1），
或 ``--synthetic`` 生成火场场景。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python wildfire-spread-modeling.py --input fuel.tif --steps 20 --wind-speed 2
    python wildfire-spread-modeling.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "wildfire-spread-modeling"

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


_NEIGH = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


# ---------------------------------------------------------------------------
# 输入校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox: Optional[List[float]], source: str = "bbox") -> None:
    """校验 EPSG:4326 经纬度 bbox：W<=E、S<=N、超经纬度→ValidationError(rc=6)。
    跨 180° 经线（|E-W| > 360）→ValidationError 并附"拆分为两侧"提示。
    """
    if bbox is None or len(bbox) != 4:
        raise ValidationError(
            f"{source} must be [W, S, E, N] with 4 floats, got {bbox!r}",
            bbox=bbox,
        )
    w, s, e, n = bbox
    if not all(isinstance(v, (int, float)) and np.isfinite(v) for v in (w, s, e, n)):
        raise ValidationError(
            f"{source} contains non-finite values: {bbox!r}", bbox=bbox,
        )
    if w < -180.0 or e > 180.0 or s < -90.0 or n > 90.0:
        raise ValidationError(
            f"{source} out of WGS-84 range (lon∈[-180,180], lat∈[-90,90]): {bbox!r}",
            bbox=bbox,
        )
    if w > e:
        gap = e - w  # 负数
        if abs(gap) > 360.0:
            raise ValidationError(
                f"{source} span exceeds 360°: {bbox!r}", bbox=bbox,
            )
        raise ValidationError(
            f"{source} has W>E ({w} > {e}); cross-dateline not supported. "
            f"Split into two bboxes (e.g. [{w}, {s}, 180, {n}] and [-180, {s}, {e}, {n}]) "
            f"and run separately.",
            bbox=bbox,
        )
    if s > n:
        raise ValidationError(
            f"{source} has S>N ({s} > {n}); latitude must increase northward", bbox=bbox,
        )
    if (e - w) <= 0.0 or (n - s) <= 0.0:
        raise ValidationError(
            f"{source} has zero or negative area: {bbox!r}", bbox=bbox,
        )


def validate_params(args: argparse.Namespace) -> None:
    """校验 --steps / --base-prob / --wind-speed / --wind-dir → ValidationError(rc=6)。"""
    if int(args.steps) < 0:
        raise ValidationError(
            f"--steps must be >= 0, got {args.steps}", steps=args.steps,
        )
    if not (0.0 <= float(args.base_prob) <= 1.0):
        raise ValidationError(
            f"--base-prob must be in [0, 1], got {args.base_prob}", base_prob=args.base_prob,
        )
    if float(args.wind_speed) < 0.0:
        raise ValidationError(
            f"--wind-speed must be >= 0, got {args.wind_speed}", wind_speed=args.wind_speed,
        )
    if not np.isfinite(float(args.wind_dir)):
        raise ValidationError(
            f"--wind-dir must be finite, got {args.wind_dir}", wind_dir=args.wind_dir,
        )


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def ignition_probability(fuel: np.ndarray, moisture: np.ndarray, slope: np.ndarray = 0.0,
                         wind_factor: float = 1.0, base_prob: float = 0.6,
                         moisture_coeff: float = 3.0, slope_coeff: float = 0.8) -> np.ndarray:
    """单像元点火概率（[0,1]）。

    对燃料可燃性、坡度、风因子单调递增，对湿度单调递减。
    """
    fuel = np.clip(np.asarray(fuel, dtype=np.float64), 0.0, 1.0)
    moisture = np.clip(np.asarray(moisture, dtype=np.float64), 0.0, 1.0)
    slope = np.clip(np.asarray(slope, dtype=np.float64), 0.0, 1.0)
    p = base_prob * fuel * np.exp(-moisture_coeff * moisture) * (1.0 + slope_coeff * slope) * float(wind_factor)
    return np.clip(p, 0.0, 1.0).astype(np.float32)


def _shift(mask: np.ndarray, di: int, dj: int) -> np.ndarray:
    """返回 out[i,j] = mask[i-di, j-dj]（不循环，边界补 0）。"""
    H, W = mask.shape
    out = np.zeros_like(mask)
    sr0, sr1 = max(-di, 0), min(H - di, H)
    sc0, sc1 = max(-dj, 0), min(W - dj, W)
    tr0, tr1 = max(di, 0), min(H + di, H)
    tc0, tc1 = max(dj, 0), min(W + dj, W)
    out[tr0:tr1, tc0:tc1] = mask[sr0:sr1, sc0:sc1]
    return out


def simulate_spread(fuel: np.ndarray, moisture: np.ndarray, slope: np.ndarray,
                    wind_speed: float, wind_dir_deg: float, ignition: np.ndarray,
                    steps: int, base_prob: float = 0.6, wind_coeff: float = 1.2,
                    seed: int = 42) -> Tuple[np.ndarray, np.ndarray]:
    """CA 蔓延模拟。返回 (最终过火掩膜 bool, 到达时间步 int，未燃为 -1)。

    每步对每个邻域方向计算含风向夹角的点火概率并抽取点火；已燃像元保持燃烧，
    因此过火面积随 steps 单调不减。
    """
    if fuel.shape != moisture.shape or fuel.shape != np.asarray(slope).shape:
        raise ValidationError("fuel/moisture/slope shape mismatch")
    if steps < 0:
        raise ValidationError("steps must be >= 0")
    rng = np.random.default_rng(seed)
    fuel = np.clip(np.asarray(fuel, dtype=np.float64), 0.0, 1.0)
    moisture = np.clip(np.asarray(moisture, dtype=np.float64), 0.0, 1.0)
    slope = np.clip(np.asarray(slope, dtype=np.float64), 0.0, 1.0)

    burned = np.zeros(fuel.shape, dtype=bool)
    burned[np.asarray(ignition, dtype=bool)] = True
    if not burned.any():
        raise ValidationError("ignition mask is empty")
    arrival = np.full(fuel.shape, -1, dtype=np.int32)
    arrival[burned] = 0

    wdir = np.deg2rad(float(wind_dir_deg))
    wx, wy = np.cos(wdir), np.sin(wdir)
    slope_f = 1.0 + 0.8 * slope
    moist_f = np.exp(-3.0 * moisture)

    for t in range(1, int(steps) + 1):
        ignite = np.zeros(fuel.shape, dtype=bool)
        rand = rng.random(fuel.shape)
        for di, dj in _NEIGH:
            src = _shift(burned, di, dj)
            nrm = float(np.hypot(di, dj))
            align = (di * wx + dj * wy) / nrm  # 蔓延方向·风向
            wind_f = float(np.exp(wind_coeff * float(wind_speed) * align))
            p = base_prob * fuel * slope_f * moist_f * wind_f
            p = np.clip(p, 0.0, 1.0)
            cand = src & (~burned)
            ignite |= cand & (rand < p)
        ignite &= ~burned
        if not ignite.any():
            break
        burned[ignite] = True
        arrival[ignite] = t

    return burned, arrival


def burned_area_series(arrival: np.ndarray, steps: int) -> List[int]:
    """由到达时间重建 0..steps 每步的累计过火像元数（单调不减）。"""
    out = []
    for t in range(int(steps) + 1):
        out.append(int(np.count_nonzero((arrival >= 0) & (arrival <= t))))
    return out


# ---------------------------------------------------------------------------
# 合成数据：火场（燃料斑块 + 湿度场 + 坡度 + 中心点火）
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], width: int = 64, height: int = 64,
                       seed: int = 42) -> Tuple[Dict[str, np.ndarray], Dict[str, Any]]:
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    xn = xx.astype(np.float64) / max(width - 1, 1)
    yn = yy.astype(np.float64) / max(height - 1, 1)
    # 燃料：森林高可燃，河谷低可燃
    fuel = 0.7 + 0.25 * np.sin(3 * np.pi * xn) * np.cos(2 * np.pi * yn)
    fuel = np.clip(fuel + rng.normal(0, 0.05, fuel.shape), 0.05, 1.0)
    # 湿度：西北湿、东南干
    moisture = np.clip(0.6 - 0.4 * (xn + yn) / 2.0 + rng.normal(0, 0.03, fuel.shape), 0.0, 1.0)
    # 坡度：缓变地形
    slope = np.clip(0.3 + 0.3 * np.sin(np.pi * yn) + rng.normal(0, 0.02, fuel.shape), 0.0, 1.0)
    ignition = np.zeros((height, width), dtype=bool)
    ignition[height // 2, width // 2] = True
    layers = {"fuel": fuel.astype(np.float32), "moisture": moisture.astype(np.float32),
              "slope": slope.astype(np.float32), "ignition": ignition}
    info = {"bbox": bbox, "width": width, "height": height,
            "ignition": [int(height // 2), int(width // 2)]}
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

    # ---- 输入校验（先于 os.makedirs，避免错误路径下也创建空目录） ----
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        validate_bbox(bbox, source=f"--input bbox {file_bbox!r}")
        if cube.shape[0] < 3:
            raise ValidationError("input needs >=3 bands (fuel, moisture, slope)")
        fuel, moisture, slope = cube[0], cube[1], cube[2]
        ignition = np.zeros(fuel.shape, dtype=bool)
        ignition[fuel.shape[0] // 2, fuel.shape[1] // 2] = True
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox, source="--bbox")
        layers, _info = generate_synthetic(bbox)
        fuel, moisture, slope, ignition = (layers["fuel"], layers["moisture"],
                                           layers["slope"], layers["ignition"])
        source_note = "synthetic"

    # ---- 数值参数校验（在所有输入数据 ok 之后） ----
    validate_params(args)

    # ---- 校验全部通过后再创建输出目录 ----
    os.makedirs(output_dir, exist_ok=True)

    burned, arrival = simulate_spread(
        fuel, moisture, slope, wind_speed=args.wind_speed, wind_dir_deg=args.wind_dir,
        ignition=ignition, steps=args.steps, base_prob=args.base_prob, seed=args.seed,
    )

    burned_tif = os.path.join(output_dir, "burned_area.tif")
    write_geotiff(burned_tif, burned.astype("int16"), bbox, nodata=-1, dtype="int16")
    arrival_tif = os.path.join(output_dir, "arrival_time.tif")
    write_geotiff(arrival_tif, arrival.astype("int16"), bbox, nodata=-1, dtype="int16")

    series = burned_area_series(arrival, args.steps)
    params = {"source": source_note, "steps": args.steps, "wind_speed": args.wind_speed,
              "wind_dir_deg": args.wind_dir, "base_prob": args.base_prob,
              "burned_area_series": series}
    params_path = os.path.join(output_dir, "fire_params.json")
    with open(params_path, "w", encoding="utf-8") as f:
        json.dump(params, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "burned_pixels": int(np.count_nonzero(burned)),
        "burned_fraction": float(np.mean(burned)),
        "max_arrival_step": int(arrival[arrival >= 0].max()) if np.any(arrival >= 0) else 0,
        "final_area": series[-1],
    }
    outputs = [
        {"path": burned_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": arrival_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": params_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, {"input": args.input, "bbox": bbox,
                              "steps": args.steps, "synthetic": bool(args.synthetic)},
                              outputs, qa, started_at, 0)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] steps: {args.steps}  wind: {args.wind_speed} @ {args.wind_dir}deg")
        print(f"[{SKILL_NAME}] burned: {qa['burned_pixels']} px ({qa['burned_fraction']*100:.1f}%)")
        print(f"[{SKILL_NAME}] outputs: {output_dir}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Wildfire spread modeling via cellular automaton (slope/wind/fuel/moisture).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"))
    p.add_argument("--input", help="input GeoTIFF (band1=fuel 0-1, band2=moisture 0-1, band3=slope 0-1)")
    p.add_argument("--steps", type=int, default=15, help="CA time steps (default: 15)")
    p.add_argument("--wind-speed", type=float, default=1.0, help="wind speed factor (default: 1.0)")
    p.add_argument("--wind-dir", type=float, default=45.0, help="wind direction degrees (toward), default: 45")
    p.add_argument("--base-prob", type=float, default=0.6, help="base ignition probability (default: 0.6)")
    p.add_argument("--seed", type=int, default=42, help="RNG seed (default: 42)")
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
