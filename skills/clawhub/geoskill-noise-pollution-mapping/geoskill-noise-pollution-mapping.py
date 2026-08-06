#!/usr/bin/env python3
"""noise-pollution-mapping — 噪声污染制图

基于交通噪声衰减模型制图噪声等级（dB(A)）。

- 声源级：由车流量/车速估算（FHWA 简化：L = 10·log10(flow) + 20·log10(speed/50) + 30），
- 几何发散：点源 -20·log10(R/R0)，线源 -10·log10(R/R0)，
- 建筑屏障衰减：每排建筑 ~5 dB（上限 20 dB），
- 地面吸收：软地面 ~0.5 dB/100m，
- 最终噪声级 = 声源级 + 几何发散 - 屏障 - 地面吸收，clip [0, 120] dB。

数据源：--synthetic 生成路网（中心横线）+ 建筑带；--input 读取距离/屏障栅格。

隐私声明 / Privacy：
- 完全离线运行。

Usage:
    python noise-pollution-mapping.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "noise-pollution-mapping"

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
# 输入校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox, source: str = "bbox") -> None:
    """校验 EPSG:4326 经纬度 bbox：W<=E、S<=N、超经纬度→ValidationError(6)。
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
    if (e - w) < 1e-9 or (n - s) < 1e-9:
        raise ValidationError(
            f"{source} too small (Δlon={e - w}, Δlat={n - s}); must be > 1e-9 degrees",
            bbox=bbox,
        )


def validate_flow_speed(flow: float, speed: float) -> None:
    """校验流量 / 速度的物理合理性。flow 允许 0（无车流）；speed 必须 > 0。
    flow 负数 / speed 非正 → ValidationError exit 6。
    """
    if flow is None or not np.isfinite(flow) or flow < 0.0:
        raise ValidationError(
            f"--flow must be a finite non-negative number (vehicles/hour), got {flow!r}",
            flow=flow,
        )
    if speed is None or not np.isfinite(speed) or speed <= 0.0:
        raise ValidationError(
            f"--speed must be a finite positive number (km/h), got {speed!r}",
            speed=speed,
        )


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def source_level(flow: float, speed: float = 60.0) -> float:
    """FHWA 简化：参考距离（15m）处声源级 dB(A)。"""
    if flow <= 0:
        return 0.0
    return float(10.0 * np.log10(flow) + 20.0 * np.log10(max(speed, 1.0) / 50.0) + 30.0)


def geometric_attenuation(distance: np.ndarray, ref_dist: float = 15.0,
                          source_type: str = "point") -> np.ndarray:
    """几何发散衰减（dB，负值）：点源 -20log10(R/R0)，线源 -10log10(R/R0)。"""
    d_safe = np.maximum(distance, ref_dist)
    ratio = d_safe / ref_dist
    if source_type == "line":
        return (-10.0 * np.log10(ratio)).astype(np.float32)
    return (-20.0 * np.log10(ratio)).astype(np.float32)


def barrier_attenuation(barrier_count: np.ndarray, per_barrier_db: float = 5.0,
                        max_db: float = 20.0) -> np.ndarray:
    """建筑屏障衰减（dB，正值）= min(count × per_barrier, max)。"""
    return np.clip(barrier_count * per_barrier_db, 0.0, max_db).astype(np.float32)


def ground_attenuation(distance: np.ndarray, rate_db_per_100m: float = 0.5) -> np.ndarray:
    """地面吸收衰减（dB，正值）= distance/100 × rate。"""
    return (distance / 100.0 * rate_db_per_100m).astype(np.float32)


def noise_level(source_db: float, distance: np.ndarray, barrier_count: np.ndarray,
                ref_dist: float = 15.0, source_type: str = "point",
                ground_rate: float = 0.5) -> np.ndarray:
    """合成噪声级 dB(A) = 声源 + 几何发散 - 屏障 - 地面，clip [0, 120]。"""
    geo = geometric_attenuation(distance, ref_dist, source_type)
    bar = barrier_attenuation(barrier_count)
    gnd = ground_attenuation(distance, ground_rate)
    level = source_db + geo - bar - gnd
    return np.clip(level, 0.0, 120.0).astype(np.float32)


def generate_synthetic_noise(bbox: List[float], width: int = 128, height: int = 128,
                             seed: int = 42) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """返回 (distance_from_road_px, barrier_count, info)。"""
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    road_row = height // 2
    dist_px = np.abs(yy - road_row)
    barriers = np.zeros((height, width), dtype=np.float32)
    barriers[(dist_px >= 2) & (dist_px <= 5)] = 1.0
    barriers[(dist_px >= 10) & (dist_px <= 12)] = 1.0
    barriers += (rng.random((height, width)) < 0.05).astype(np.float32)
    barriers = np.clip(barriers, 0.0, 3.0)
    info = {"bbox": bbox, "width": width, "height": height, "road_row": road_row}
    return dist_px, barriers, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(path: str, cube: np.ndarray, bbox: List[float], nodata: float = -9999.0) -> None:
    import rasterio
    from rasterio.transform import from_bounds
    if cube.ndim == 2:
        cube = cube[np.newaxis, ...]
    cube = np.asarray(cube, dtype=np.float32)
    # NaN → nodata（GeoTIFF 物理写盘前必须把 NaN 替换为 sentinel，否则 rasterio 写 -inf 异常）
    cube = np.where(np.isnan(cube), np.float32(nodata), cube)
    nb, h, w = cube.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    profile = {"driver": "GTiff", "height": h, "width": w, "count": nb,
               "dtype": "float32", "crs": "EPSG:4326", "transform": transform,
               "nodata": nodata, "compress": "deflate"}
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(cube[b], b + 1)


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float]]:
    """读 GeoTIFF，返回 (cube[C, H, W] float32, bbox) — NoData 像元为 NaN（band0 之外不 mask）。"""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nd = src.nodata
        if nd is not None and np.isfinite(nd) and cube.shape[0] >= 1:
            # band0 的 NoData 像元 → NaN，传播到整个 band0 列；barriers (band1) 不强制
            mask0 = cube[0] == float(nd)
            cube[0][mask0] = np.nan
    return cube, bbox


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------
def write_manifest(output_dir, args, outputs, qa, started_at, exit_code, bbox) -> Optional[str]:
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME, skill_version=VERSION, command=cmd,
        started_at=started_at, finished_at=_utc_now(), exit_code=exit_code,
        inputs={
            "input": getattr(args, "input", None),
            "flow": getattr(args, "flow", None),
            "speed": getattr(args, "speed", None),
            "source_type": getattr(args, "source_type", None),
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
    os.makedirs(output_dir, exist_ok=True)
    bbox = list(args.bbox) if args.bbox else None

    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        dist_px = cube[0]
        barriers = cube[1] if cube.shape[0] >= 2 else np.zeros_like(dist_px)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox, source="--bbox")
        dist_px, barriers, _ = generate_synthetic_noise(bbox)
        source_note = "synthetic"

    if bbox is not None:
        # 即便 --input 路径也要校验（输入数据本身可能越界/颠倒）
        validate_bbox(bbox, source="bbox from --input")

    if dist_px.size == 0:
        raise ValidationError("input raster is empty")

    # 输入栅格全 NoData 校验
    finite_mask = np.isfinite(dist_px)
    if not finite_mask.any():
        raise ValidationError(
            "input raster has no valid (non-NoData) pixels in band0",
            shape=list(dist_px.shape),
        )

    validate_flow_speed(args.flow, args.speed)

    h, w = dist_px.shape
    lat_mid = (bbox[1] + bbox[3]) / 2.0
    dx_m = (bbox[2] - bbox[0]) / w * 111320 * np.cos(np.deg2rad(lat_mid))
    dy_m = (bbox[3] - bbox[1]) / h * 111320
    pixel_m = (dx_m + dy_m) / 2.0
    distance_m = dist_px * pixel_m  # NaN 自动传播

    src_db = source_level(args.flow, args.speed)
    level = noise_level(src_db, distance_m, barriers,
                        ref_dist=15.0, source_type=args.source_type)

    out_path = os.path.join(output_dir, "noise_level.tif")
    write_geotiff(out_path, level, bbox)

    # NaN-safe 统计
    valid = level[np.isfinite(level)]
    n_valid = int(valid.size)
    n_total = int(level.size)
    if n_valid > 0:
        mean_dB = float(np.mean(valid))
        max_dB = float(np.max(valid))
        min_dB = float(np.min(valid))
    else:
        mean_dB = max_dB = min_dB = float("nan")

    params = {
        "flow_veh_h": args.flow, "speed_km_h": args.speed,
        "source_level_dB": src_db, "source_type": args.source_type,
        "pixel_m": pixel_m,
        "n_valid_pixels": n_valid, "n_total_pixels": n_total,
        "mean_noise_dB": mean_dB,
        "max_noise_dB": max_dB,
        "min_noise_dB": min_dB,
    }
    params_path = os.path.join(output_dir, "noise_params.json")
    with open(params_path, "w", encoding="utf-8") as f:
        json.dump(params, f, ensure_ascii=False, indent=2)

    outputs = [
        {"path": out_path, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": params_path, "kind": "json"},
    ]
    qa: Dict[str, Any] = {
        "source": source_note, "source_level_dB": src_db,
        "n_valid_pixels": n_valid, "n_total_pixels": n_total,
        "mean_noise_dB": mean_dB,
        "max_noise_dB": max_dB,
    }
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] source level: {src_db:.1f} dB(A)")
        print(f"[{SKILL_NAME}] mean noise: {mean_dB:.1f} dB(A) (n_valid={n_valid}/{n_total})")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Traffic noise pollution mapping with attenuation models.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input GeoTIFF (band0=distance px, band1=barriers)")
    p.add_argument("--flow", type=float, default=1000.0, help="traffic flow (veh/h)")
    p.add_argument("--speed", type=float, default=60.0, help="vehicle speed (km/h)")
    p.add_argument("--source-type", default="point", choices=["point", "line"],
                   help="source geometry (default: point)")
    p.add_argument("--synthetic", action="store_true", help="generate synthetic road scene (offline)")
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
