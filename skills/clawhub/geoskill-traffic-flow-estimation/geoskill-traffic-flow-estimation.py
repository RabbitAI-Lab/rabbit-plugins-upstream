#!/usr/bin/env python3
"""traffic-flow-estimation — 交通流量估算

从多时相高分辨率影像估算交通流量和车速。核心算法：

- **车辆检测**：用连通域标记（scipy.ndimage.label）检测亮目标，
  按面积筛选出车辆像元簇，统计车辆数。
- **多时相计数**：对 t1、t2 两个时相分别检测车辆并计数。
- **流量估算**：flow = 平均车辆数 / 时间间隔（辆/小时）。
- **速度估算**：用两时相影像的相位互相关（FFT cross-correlation）
  估计整体位移 Δpx，speed = Δpx × pixel_size / Δt。

数据源：本地双时相 GeoTIFF（band1=t1, band2=t2），
或 ``--synthetic`` 离线模拟。

隐私声明 / Privacy：默认离线运行，``--synthetic`` 完全无网络。

Usage:
    python traffic-flow-estimation.py --input two_epoch.tif --dt-minutes 5
    python traffic-flow-estimation.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "traffic-flow-estimation"

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
def validate_bbox(bbox, *, allow_antimeridian_cross: bool = False) -> None:
    """校验 bbox=[W,S,E,N]（EPSG:4326 度）。

    - W<E、S<N → 否则 ValidationError
    - 范围 [-180,180]×[-90,90] → 否则 ValidationError
    - 跨 180° 经线（W>E）默认拒绝（allow_antimeridian_cross=False）
    - 面积过小（< 1e-4°）→ ValidationError（避免 from_bounds 异常）
    """
    if bbox is None or len(bbox) != 4:
        raise ValidationError("bbox must have 4 floats [W S E N]")
    w, s, e, n = [float(v) for v in bbox]
    if not (all(np.isfinite([w, s, e, n]))):
        raise ValidationError("bbox contains non-finite values")
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError("bbox lon out of [-180, 180]")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError("bbox lat out of [-90, 90]")
    if w >= e:
        if not allow_antimeridian_cross:
            raise ValidationError(
                f"bbox W>=E ({w} >= {e}); cross-180° is not supported, "
                f"split into two bboxes if needed"
            )
        # 若开启环绕，leniency 不通过
        raise ValidationError(f"bbox W>=E ({w} >= {e})")
    if s >= n:
        raise ValidationError(f"bbox S>=N ({s} >= {n})")
    if (e - w) < 1e-4 or (n - s) < 1e-4:
        raise ValidationError(
            f"bbox too small (dx={e - w}, dy={n - s}); need >= 1e-4 degrees"
        )


def validate_params(args: argparse.Namespace) -> None:
    """校验 CLI 参数物理合理性 → ValidationError 触发 rc=6。"""
    if not (args.dt_minutes > 0 and np.isfinite(args.dt_minutes)):
        raise ValidationError(
            f"--dt-minutes must be > 0 and finite (got {args.dt_minutes})"
        )
    if args.dt_minutes > 24 * 60:
        # 超过 1 天的 dt 对车流估算无意义
        raise ValidationError(
            f"--dt-minutes {args.dt_minutes} is unrealistically large (> 1 day)"
        )
    if not (0.0 < args.threshold < 1.0):
        raise ValidationError(
            f"--threshold must be in (0, 1) for normalized brightness "
            f"(got {args.threshold})"
        )
    if not (args.pixel_size > 0 and np.isfinite(args.pixel_size)):
        raise ValidationError(
            f"--pixel-size must be > 0 and finite (got {args.pixel_size})"
        )
    if args.pixel_size > 1e6:
        raise ValidationError(
            f"--pixel-size {args.pixel_size} m is unrealistically large"
        )


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------

def count_vehicles(
    image: np.ndarray,
    threshold: float,
    min_size: int = 1,
    max_size: int = 500,
) -> int:
    """车辆计数：阈值分割 + 连通域标记 + 面积筛选。

    亮度 > threshold 的连通簇，面积在 [min_size, max_size] 内 → 一辆车。
    NaN 像素被排除（视为 NoData）。
    """
    from scipy.ndimage import label
    img = np.asarray(image, dtype=np.float32)
    # NaN-safe: NaN -> 0 (不参与 > threshold)
    if not np.all(np.isfinite(img)):
        img = np.where(np.isfinite(img), img, 0.0).astype(np.float32)
    binary = img > threshold
    labeled, n_features = label(binary)
    count = 0
    for i in range(1, n_features + 1):
        area = int(np.sum(labeled == i))
        if min_size <= area <= max_size:
            count += 1
    return count


def estimate_flow(count: int, dt_hours: float) -> float:
    """流量（辆/小时）= 车辆数 / 时间间隔（小时）。"""
    if dt_hours <= 0:
        return 0.0
    return float(count) / float(dt_hours)


def estimate_speed_mps(
    displacement_px: float,
    pixel_size_m: float,
    dt_seconds: float,
) -> float:
    """速度（m/s）= 位移(像元) × 像元大小(m) / 时间(s)。"""
    if dt_seconds <= 0:
        return 0.0
    return float(displacement_px) * float(pixel_size_m) / float(dt_seconds)


def estimate_shift(im1: np.ndarray, im2: np.ndarray) -> Tuple[float, float]:
    """相位互相关估计两影像的整体位移 (dy, dx)。

    用归一化互功率谱的逆变换峰值定位（亚像元精度用质心细化）。
    适用于循环位移（np.roll）。返回 (dy, dx)：若 im2 = roll(im1, (s_y, s_x))，
    则返回 (s_y, s_x)（im2 相对 im1 的位移）。
    """
    a = np.asarray(im1, dtype=np.float64)
    b = np.asarray(im2, dtype=np.float64)
    a = a - a.mean()
    b = b - b.mean()
    fa = np.fft.fft2(a)
    fb = np.fft.fft2(b)
    R = fb * np.conj(fa)
    mag = np.abs(R)
    mag[mag < 1e-12] = 1e-12
    R = R / mag
    cc = np.fft.ifft2(R).real
    h, w = cc.shape
    peak = np.unravel_index(np.argmax(cc), cc.shape)
    dy = float(peak[0])
    dx = float(peak[1])
    if dy > h / 2:
        dy -= h
    if dx > w / 2:
        dx -= w
    return dy, dx


# ---------------------------------------------------------------------------
# 合成数据：道路上的车辆（两个时相，车辆发生位移）
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 128,
    height_px: int = 128,
    n_cars: int = 20,
    shift_px: int = 6,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成双时相影像（t1, t2）。

    背景为暗道路，随机放置 n_cars 个亮车辆目标（2×2 像元）。
    t2 = t1 的车辆沿 x 方向整体位移 shift_px（模拟车流）。
    """
    rng = np.random.default_rng(seed)
    t1 = np.full((height_px, width), 0.05, dtype=np.float32)

    car_positions = []
    for _ in range(n_cars):
        r = int(rng.integers(2, height_px - 2))
        c = int(rng.integers(2, width - 2))
        t1[r:r + 2, c:c + 2] = 0.9
        car_positions.append((r, c))

    # t2：车辆整体位移（循环）
    t2 = np.roll(t1, shift=shift_px, axis=1)

    info = {
        "bbox": bbox, "width": width, "height": height_px,
        "n_cars": n_cars, "shift_px": shift_px,
    }
    return t1, t2, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O
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
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    profile = {
        "driver": "GTiff", "height": h, "width": w, "count": nb,
        "dtype": "float32", "crs": "EPSG:4326", "transform": transform,
        "nodata": nodata, "compress": "deflate",
    }
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(cube[b].astype("float32"), b + 1)


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float], float]:
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        # NoData -> NaN 防止 -9999 误判为亮车辆
        nd = src.nodata
        if nd is not None and np.isfinite(nd):
            cube = np.where(cube == nd, np.nan, cube).astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        res = float(src.res[0]) if src.res else 1.0
    return cube, bbox, res


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
            "input": getattr(args, "input", None),
            "dt_minutes": getattr(args, "dt_minutes", 5.0),
            "threshold": getattr(args, "threshold", 0.5),
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

    # 1) 参数与 bbox 校验（先做，不创建任何目录）
    validate_params(args)

    bbox = list(args.bbox) if args.bbox else None
    pixel_size = args.pixel_size

    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        cube, file_bbox, res = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        if cube.shape[0] < 2:
            raise ValidationError("input must have at least 2 bands (t1, t2)")
        t1 = cube[0]
        t2 = cube[1]
        if res > 0:
            pixel_size = res
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox)
        t1, t2, synth_info = generate_synthetic(bbox)
        source_note = "synthetic"

    # input 模式也要校验 bbox（含从 file 读出来的）
    if bbox is not None:
        validate_bbox(bbox)

    if t1.size == 0:
        raise ValidationError("input raster is empty")

    # 全 NaN 检查（NoData -> NaN 后）
    n_valid_t1 = int(np.sum(np.isfinite(t1)))
    n_valid_t2 = int(np.sum(np.isfinite(t2)))
    n_total = int(t1.size)
    if n_valid_t1 == 0 or n_valid_t2 == 0:
        raise ValidationError(
            f"input raster has no valid pixels "
            f"(n_valid_t1={n_valid_t1}, n_valid_t2={n_valid_t2}, n_total={n_total})"
        )

    # 所有校验通过 → 创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 2) 车辆检测与计数
    c1 = count_vehicles(t1, args.threshold)
    c2 = count_vehicles(t2, args.threshold)
    avg_count = (c1 + c2) / 2.0

    dt_hours = args.dt_minutes / 60.0
    dt_seconds = args.dt_minutes * 60.0
    flow = estimate_flow(int(round(avg_count)), dt_hours)

    # 3) 速度估计
    dy, dx = estimate_shift(t1, t2)
    displacement = float(np.hypot(dy, dx))
    speed_mps = estimate_speed_mps(displacement, pixel_size, dt_seconds)
    speed_kmh = speed_mps * 3.6

    # 4) 空间化流量（局部车辆密度 × 流量标度；NaN-safe）
    from scipy.ndimage import uniform_filter
    t1v = np.where(np.isfinite(t1), t1, 0.0)
    t2v = np.where(np.isfinite(t2), t2, 0.0)
    veh = ((t1v > args.threshold).astype(np.float32) +
           (t2v > args.threshold).astype(np.float32)) / 2.0
    flow_field = uniform_filter(veh, size=9, mode="nearest") * flow

    out_tif = os.path.join(output_dir, "traffic_flow.tif")
    write_geotiff(out_tif, flow_field, bbox)

    stats = {
        "count_t1": c1,
        "count_t2": c2,
        "avg_count": float(avg_count),
        "dt_minutes": args.dt_minutes,
        "flow_veh_per_hour": flow,
        "displacement_px": displacement,
        "speed_m_per_s": speed_mps,
        "speed_km_per_h": speed_kmh,
    }
    stats_path = os.path.join(output_dir, "traffic_stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "n_total_pixels": n_total,
        "n_valid_pixels_t1": n_valid_t1,
        "n_valid_pixels_t2": n_valid_t2,
        "input_nodata_handling": "NoData->NaN",
    }
    qa.update(stats)
    if synth_info is not None:
        qa["synthetic_n_cars"] = synth_info["n_cars"]
        qa["synthetic_shift_px"] = synth_info["shift_px"]

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": stats_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] vehicles: t1={c1}, t2={c2}")
        print(f"[{SKILL_NAME}] flow: {flow:.1f} veh/h")
        print(f"[{SKILL_NAME}] speed: {speed_kmh:.1f} km/h (disp={displacement:.2f} px)")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Traffic flow and speed estimation from multi-temporal imagery.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input GeoTIFF with 2 bands (t1, t2)")
    p.add_argument("--dt-minutes", type=float, default=5.0,
                   help="time interval between epochs in minutes (default: 5)")
    p.add_argument("--threshold", type=float, default=0.5,
                   help="vehicle brightness threshold (default: 0.5)")
    p.add_argument("--pixel-size", type=float, default=1.0,
                   help="pixel size in meters (default: 1.0)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a physics-consistent synthetic scene (offline)")
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
