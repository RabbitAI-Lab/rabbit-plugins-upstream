#!/usr/bin/env python3
"""insurance-risk-mapping — 保险风险制图

面向财产/巨灾保险的多灾种期望损失 (Expected Annual Loss) 制图。核心模型：

    EAL = Σ_h  P_h · Asset · V_h(I_h)

- **P_h**：第 h 种灾害的年超越概率 = 1 / 重现期 T。
- **Asset**：像元资产价值（保额/重置成本）。
- **V_h(I_h)**：脆弱性曲线，把灾害强度 I_h 映射为损失比 ∈[0,1]；支持线性与
  Sigmoid 两种解析曲线。

对洪水、风灾、地震三种灾害分别计算后叠加，得到逐像元年期望损失与风险等级。

数据源：本地多波段 GeoTIFF（Asset/Flood/Wind/Seismic 强度），或 ``--synthetic``
生成含高风险热点的模拟场景用于离线测试。

隐私声明 / Privacy：默认离线运行，``--synthetic`` 完全无网络；本地处理，不上传数据。

Usage:
    python insurance-risk-mapping.py --input data.tif --output-dir ./out
    python insurance-risk-mapping.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "insurance-risk-mapping"

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


BAND_ROLES = ["asset", "flood", "wind", "seismic"]
N_REQUIRED_BANDS = len(BAND_ROLES)
HAZARDS = ["flood", "wind", "seismic"]
# 默认重现期 (年)
DEFAULT_RETURN_PERIODS = {"flood": 100.0, "wind": 50.0, "seismic": 475.0}
# 默认脆弱性曲线起止强度
DEFAULT_CURVE = {
    "flood": (0.5, 3.0),    # 洪水水深 m
    "wind": (20.0, 60.0),   # 风速 m/s
    "seismic": (0.1, 0.6),  # PGA g
}


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# Input validation (P0/P1)
# ---------------------------------------------------------------------------
def validate_bbox(bbox) -> None:
    """Validate a [W, S, E, N] bbox. Raises ValidationError on bad order, range,
    zero-area, or crossing the 180° meridian.
    """
    try:
        w, s, e, n = [float(v) for v in bbox]
    except Exception:
        raise ValidationError(f"bbox must be 4 floats, got {bbox!r}")
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"longitude out of range [-180, 180]: W={w}, E={e}")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"latitude out of range [-90, 90]: S={s}, N={n}")
    if w >= e:
        raise ValidationError(
            f"bbox requires W < E (got W={w}, E={e}); check --bbox order")
    if s >= n:
        raise ValidationError(
            f"bbox requires S < N (got S={s}, N={n}); check --bbox order")
    if e - w > 360.0 or n - s > 180.0:
        raise ValidationError(
            f"bbox span too large (dx={e - w}, dy={n - s})")
    if w > 180.0 or e > 180.0 or w < -180.0 or e < -180.0:
        raise ValidationError(
            f"bbox crosses 180° meridian; please split into two sub-bboxes")


def validate_class_breaks(breaks) -> None:
    """Validate --class-breaks: strictly ascending, non-empty, all non-negative.
    """
    if not breaks or len(breaks) == 0:
        raise ValidationError("--class-breaks must be non-empty")
    try:
        bvals = [float(b) for b in breaks]
    except Exception:
        raise ValidationError(
            f"--class-breaks must be numbers, got {breaks!r}")
    if any(b < 0.0 for b in bvals):
        raise ValidationError(
            f"--class-breaks must be non-negative, got {breaks}")
    for i in range(1, len(bvals)):
        if bvals[i] <= bvals[i - 1]:
            raise ValidationError(
                f"--class-breaks must be strictly ascending; got {breaks}")


def read_geotiff_with_nodata(path: str):
    """Read a multiband raster and return (data, bbox, nodata).

    Values equal to the source nodata (if any) are replaced with NaN.
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [float(b.left), float(b.bottom), float(b.right), float(b.top)]
        nd = src.nodata
    if nd is not None:
        cube = np.where(cube == nd, np.nan, cube)
    return cube, bbox, nd


def count_valid_pixels(cube: np.ndarray) -> int:
    """Number of locations where ALL bands are finite (not NaN / inf)."""
    if cube.ndim == 3:
        valid_loc = np.all(np.isfinite(cube), axis=0)
    else:
        valid_loc = np.isfinite(cube)
    return int(valid_loc.sum())


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def annual_probability(return_period: float) -> float:
    """年超越概率 P = 1 / T。"""
    t = float(return_period)
    if t <= 0:
        raise ValidationError(f"return period must be > 0, got {t}")
    return 1.0 / t


def vulnerability_ratio(
    intensity: np.ndarray,
    i0: float,
    i1: float,
    curve: str = "linear",
    k: float = 8.0,
) -> np.ndarray:
    """把灾害强度映射为损失比 ∈[0,1]。

    - linear：在 [i0, i1] 上线性插值，<i0 取 0，>i1 取 1；
    - sigmoid：以 (i0+i1)/2 为中点、陡度 k 的 Sigmoid。
    """
    x = np.asarray(intensity, dtype=np.float32)
    if i1 <= i0:
        raise ValidationError(f"curve requires i1 > i0 (got {i0}, {i1})")
    if curve == "sigmoid":
        mid = 0.5 * (i0 + i1)
        ratio = 1.0 / (1.0 + np.exp(-float(k) * (x - mid)))
    else:  # linear
        ratio = (x - float(i0)) / (float(i1) - float(i0))
    return np.clip(ratio, 0.0, 1.0).astype(np.float32)


def expected_loss_single(
    asset: np.ndarray,
    intensity: np.ndarray,
    return_period: float,
    i0: float,
    i1: float,
    curve: str = "linear",
) -> np.ndarray:
    """单一灾害年期望损失 = P · Asset · V(I)。"""
    p = annual_probability(return_period)
    ratio = vulnerability_ratio(intensity, i0, i1, curve)
    asset = np.asarray(asset, dtype=np.float32)
    return (p * asset * ratio).astype(np.float32)


def multi_hazard_loss(
    asset: np.ndarray,
    intensities: Dict[str, np.ndarray],
    return_periods: Optional[Dict[str, float]] = None,
    curves: Optional[Dict[str, Tuple[float, float]]] = None,
    curve: str = "linear",
) -> Tuple[np.ndarray, Dict[str, np.ndarray]]:
    """多灾种年期望损失（叠加）。返回 (total_eal, per_hazard_dict)。"""
    rps = dict(DEFAULT_RETURN_PERIODS if return_periods is None else return_periods)
    cvs = dict(DEFAULT_CURVE if curves is None else curves)
    asset = np.asarray(asset, dtype=np.float32)
    total = np.zeros(asset.shape, dtype=np.float32)
    per: Dict[str, np.ndarray] = {}
    for name, inten in intensities.items():
        if name not in rps:
            raise ValidationError(f"no return period defined for hazard '{name}'")
        i0, i1 = cvs.get(name, (0.0, 1.0))
        loss = expected_loss_single(asset, inten, rps[name], i0, i1, curve)
        per[name] = loss
        total = total + loss
    return total.astype(np.float32), per


def risk_class(loss: np.ndarray, breaks: List[float]) -> np.ndarray:
    """按分档阈值把期望损失分级（0..len(breaks)）。"""
    loss = np.asarray(loss, dtype=np.float32)
    cls = np.zeros(loss.shape, dtype=np.int16)
    for i, b in enumerate(breaks, start=1):
        cls = np.where(loss >= b, i, cls)
    return cls.astype(np.int16)


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic_cube(
    bbox: List[float], width: int = 128, height: int = 128, seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成 (4,H,W)：Asset/Flood/Wind/Seismic，含三个灾害热点。"""
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    # 资产：城市中心高
    cx, cy = 0.5 * (width - 1), 0.5 * (height - 1)
    asset = 5e4 + 4e5 * np.exp(-(((xx - cx) ** 2 + (yy - cy) ** 2)) / (2 * (0.28 * width) ** 2))
    asset = (asset + rng.normal(0, 5e3, asset.shape)).astype(np.float32)
    asset = np.clip(asset, 0, None)

    def hotspot(fx, fy, amp, sig):
        hx, hy = fx * (width - 1), fy * (height - 1)
        return amp * np.exp(-(((xx - hx) ** 2 + (yy - hy) ** 2)) / (2 * (sig * width) ** 2))

    flood = np.clip(hotspot(0.35, 0.6, 3.0, 0.18) + rng.normal(0, 0.1, asset.shape), 0, None)
    wind = np.clip(hotspot(0.7, 0.4, 60.0, 0.22) + rng.normal(0, 1.0, asset.shape), 0, None)
    seismic = np.clip(hotspot(0.55, 0.55, 0.6, 0.25) + rng.normal(0, 0.01, asset.shape), 0, None)

    cube = np.stack([asset, flood, wind, seismic], axis=0).astype(np.float32)
    info = {"bbox": bbox, "width": width, "height": height, "band_roles": BAND_ROLES,
            "return_periods": DEFAULT_RETURN_PERIODS}
    return cube, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(path, cube, bbox, nodata=-9999.0, dtype="float32"):
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


def read_geotiff(path):
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return cube, bbox


def write_manifest(output_dir, args, outputs, qa, started_at, exit_code, bbox):
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME, skill_version=VERSION, command=cmd,
        started_at=started_at, finished_at=_utc_now(), exit_code=exit_code,
        inputs={"input": getattr(args, "input", None),
                "curve": getattr(args, "curve", None),
                "synthetic": bool(getattr(args, "synthetic", False)), "bbox": bbox},
        outputs=[OutputFile(**o) for o in outputs], qa=qa,
        software={"python": sys.version.split()[0], "skill": SKILL_NAME},
    )
    path = os.path.join(output_dir, "output-manifest.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(man.to_dict(), f, ensure_ascii=False, indent=2, default=str)
    return path


def process(args):
    started_at = _utc_now()
    output_dir = args.output_dir
    bbox = list(args.bbox) if args.bbox else None

    synth_info = None
    src_nd = None
    if args.input and not args.synthetic:
        cube, file_bbox, _src_nd = read_geotiff_with_nodata(args.input)
        bbox = bbox if bbox is not None else file_bbox
        source_note = args.input
        src_nd = _src_nd
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox)
        cube, synth_info = generate_synthetic_cube(bbox)
        source_note = "synthetic"

    # Parameter validation (BEFORE side-effect makedirs).
    if bbox is not None:
        validate_bbox(bbox)
    validate_class_breaks(args.class_breaks)

    if cube.size == 0:
        raise ValidationError("input raster is empty")
    if cube.ndim != 3 or cube.shape[0] < N_REQUIRED_BANDS:
        raise ValidationError(
            f"input must have >= {N_REQUIRED_BANDS} bands ({BAND_ROLES}); got {cube.shape}")

    # Reject all-NoData input.
    n_valid = count_valid_pixels(cube)
    if n_valid == 0:
        raise ValidationError(
            "input raster has no valid pixels (all NoData / NaN); cannot compute loss")

    asset, flood, wind, seismic = cube[0], cube[1], cube[2], cube[3]
    intensities = {"flood": flood, "wind": wind, "seismic": seismic}

    total_eal, per = multi_hazard_loss(asset, intensities, curve=args.curve)
    breaks = [b for b in args.class_breaks]
    rcls = risk_class(total_eal, breaks)

    # Side effects begin only after all validation passes.
    os.makedirs(output_dir, exist_ok=True)

    out_eal = os.path.join(output_dir, "expected_annual_loss.tif")
    # NaN locations → -9999 in EAL raster
    eal_to_write = np.where(np.isfinite(total_eal), total_eal, -9999.0)
    write_geotiff(out_eal, eal_to_write, bbox)
    # 各灾种堆栈 (band-aligned with input: Asset/Flood/Wind/Seismic
    # but per-hazard loss only covers HAZARDS). NaN → -9999.
    per_stack = np.stack([
        np.where(np.isfinite(per[h]), per[h], -9999.0) for h in HAZARDS
    ], axis=0)
    out_per = os.path.join(output_dir, "per_hazard_loss.tif")
    write_geotiff(out_per, per_stack, bbox)
    out_class = os.path.join(output_dir, "risk_class.tif")
    write_geotiff(out_class, rcls.astype(np.float32), bbox, nodata=-1.0)

    finite_asset = np.isfinite(asset)
    finite_eal = np.isfinite(total_eal)
    total_value = float(np.nansum(asset)) if finite_asset.any() else 0.0
    eal_sum = float(np.nansum(total_eal)) if finite_eal.any() else 0.0
    report = {
        "source": source_note, "curve": args.curve,
        "return_periods": DEFAULT_RETURN_PERIODS,
        "class_breaks": breaks,
        "total_asset_value": total_value,
        "total_expected_annual_loss": eal_sum,
        "loss_ratio": (eal_sum / total_value) if total_value > 0 else 0.0,
        "per_hazard_total_loss": {
            h: (float(np.nansum(per[h])) if np.isfinite(per[h]).any() else 0.0)
            for h in HAZARDS
        },
        "risk_class_counts": {str(c): int(np.count_nonzero(rcls == c))
                              for c in range(len(breaks) + 1)},
    }
    report_path = os.path.join(output_dir, "risk_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    n_total = int(cube.shape[1] * cube.shape[2]) if cube.ndim >= 2 else 0
    qa = {
        "source": source_note,
        "n_valid_pixels": n_valid,
        "n_total_pixels": n_total,
        "input_nodata": src_nd,
        "total_expected_annual_loss": eal_sum,
        "loss_ratio": report["loss_ratio"],
        "max_eal": (float(np.nanmax(total_eal)) if finite_eal.any() else 0.0),
    }
    if synth_info is not None:
        qa["synthetic"] = True

    outputs = [
        {"path": out_eal, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": out_per, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": len(HAZARDS)},
        {"path": out_class, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": report_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] total asset: {total_value:,.0f}")
        print(f"[{SKILL_NAME}] total EAL: {eal_sum:,.1f}  loss ratio: {report['loss_ratio']:.5f}")
        print(f"[{SKILL_NAME}] report: {report_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser():
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Multi-hazard insurance risk mapping: EAL = sum P * Asset * Vulnerability.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"))
    p.add_argument("--input", help="input multi-band GeoTIFF (Asset/Flood/Wind/Seismic)")
    p.add_argument("--synthetic", action="store_true")
    p.add_argument("--curve", default="linear", choices=["linear", "sigmoid"],
                   help="vulnerability curve type (default: linear)")
    p.add_argument("--class-breaks", type=float, nargs="+", default=[1.0, 10.0, 100.0],
                   help="EAL class break values (default: 1 10 100)")
    p.add_argument("--output-dir", default="./output")
    p.add_argument("--quiet", action="store_true")
    p.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    return p


def main(argv=None):
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
