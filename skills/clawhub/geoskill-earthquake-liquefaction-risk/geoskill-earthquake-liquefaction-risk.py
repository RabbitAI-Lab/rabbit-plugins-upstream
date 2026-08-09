#!/usr/bin/env python3
"""earthquake-liquefaction-risk — 地震液化风险评估

用 Youd 简化法评估砂土液化风险。逐像元计算循环应力比 CSR 与循环阻抗比 CRR，
得到安全系数 FS = CRR/CSR，再按 Iwasaki 深度加权积分得液化指数 LPI。

模型：

    CSR = 0.65 · (PGA/g) · rd(z) · gw            （rd 为应力折减，gw 为浅地下水放大）
    CRR = 0.05 + 0.015·N · (1 - 0.005·fines)     （N 为标准贯入击数，越高越抗液化）
    FS  = CRR / CSR                               （FS<1 判定液化）
    LPI = Σ_{FS<1} (1 - FS) · w(z) · Δz,  w(z)=10-0.5z  （Iwasaki 液化指数，≥0）

PGA 越高 → CSR 越大 → FS 越小 → LPI 越大（正相关）；土质越密实(N 越大) → 越抗液化。

数据源：本地多波段 GeoTIFF（band1=PGA(g)、band2=SPT N值、band3=地下水位埋深m），
或 ``--synthetic`` 生成场景。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python earthquake-liquefaction-risk.py --input site.tif --depth 3
    python earthquake-liquefaction-risk.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "earthquake-liquefaction-risk"

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
# Input validation
# ---------------------------------------------------------------------------
def validate_bbox(bbox: List[float]) -> None:
    """Validate a [W, S, E, N] geographic bbox (exit 6 on failure)."""
    w, s, e, n = bbox
    if not all(np.isfinite([w, s, e, n])):
        raise ValidationError(
            f"bbox contains non-finite values: W={w} S={s} E={e} N={n}",
            bbox=list(bbox),
        )
    if abs(w) > 180.0 or abs(e) > 180.0:
        raise ValidationError(
            f"bbox longitude out of range: W={w} E={e} (must be in [-180, 180])",
            bbox=list(bbox),
        )
    if abs(s) > 90.0 or abs(n) > 90.0:
        raise ValidationError(
            f"bbox latitude out of range: S={s} N={n} (must be in [-90, 90])",
            bbox=list(bbox),
        )
    if w >= e:
        raise ValidationError(
            f"bbox reversed: W ({w}) must be < E ({e}). "
            f"For antimeridian-crossing bboxes, split into W..180 and -180..E.",
            bbox=list(bbox),
        )
    if s >= n:
        raise ValidationError(
            f"bbox reversed: S ({s}) must be < N ({n})", bbox=list(bbox)
        )
    if (e - w) < 1e-9 or (n - s) < 1e-9:
        raise ValidationError(
            f"bbox has zero area: W={w} S={s} E={e} N={n}", bbox=list(bbox)
        )


def validate_params(depth: float, fines_pct: float) -> None:
    """Validate the engineering parameters. depth>0, fines_pct in [0,100]."""
    if not np.isfinite(depth) or depth <= 0:
        raise ValidationError(
            f"--depth must be a positive number, got {depth}", depth=depth
        )
    if not np.isfinite(fines_pct) or fines_pct < 0 or fines_pct > 100:
        raise ValidationError(
            f"--fines must be in [0, 100], got {fines_pct}", fines_pct=fines_pct
        )


def read_geotiff_with_nodata(
    path: str,
) -> Tuple[np.ndarray, List[float], int]:
    """Read multi-band GeoTIFF replacing NoData with NaN; report n_valid."""
    cube, bbox = read_geotiff(path)
    import rasterio
    with rasterio.open(path) as src:
        nodata = src.nodata
    if nodata is not None:
        cube = np.where(cube == nodata, np.nan, cube).astype(np.float32)
    n_valid = int(np.sum(np.any(np.isfinite(cube), axis=0)))
    return cube, bbox, n_valid


# ---------------------------------------------------------------------------
# 核心算法（Youd / Iwasaki 简化）
# ---------------------------------------------------------------------------
def stress_reduction(depth: float) -> float:
    """应力折减系数 rd(z)：随深度递减（0.6–1.0）。"""
    return float(np.clip(1.0 - 0.015 * float(depth), 0.6, 1.0))


def groundwater_factor(water_table_depth: float) -> float:
    """地下水放大系数：水位越浅（越饱和）CSR 放大越多（1.0–1.5）。"""
    wt = max(float(water_table_depth), 0.0)
    return float(1.0 + 0.5 * np.exp(-wt / 3.0))


def cyclic_stress_ratio(pga_g, depth: float = 3.0, water_table_depth: float = 2.0):
    """循环应力比 CSR = 0.65·(PGA/g)·rd·gw。对 PGA 单调增、随深度递减、浅水位增大。"""
    rd = stress_reduction(depth)
    gw = groundwater_factor(water_table_depth)
    pga = np.clip(np.asarray(pga_g, dtype=np.float64), 0.0, None)
    return (0.65 * pga * rd * gw).astype(np.float32) if isinstance(pga, np.ndarray) else float(0.65 * pga * rd * gw)


def cyclic_resistance_ratio(n_value, fines_pct: float = 0.0):
    """循环阻抗比 CRR：随 SPT 击数 N 增大（更密实更抗液化），含细粒含量微调。[0.05,0.6]。"""
    n = np.clip(np.asarray(n_value, dtype=np.float64), 0.0, None)
    fines = np.clip(float(fines_pct), 0.0, 100.0)
    crr = (0.05 + 0.015 * n) * (1.0 - 0.005 * fines)
    crr = np.clip(crr, 0.05, 0.6)
    return crr.astype(np.float32) if isinstance(n, np.ndarray) else float(np.clip(crr, 0.05, 0.6))


def factor_of_safety(crr, csr):
    """安全系数 FS = CRR/CSR；FS<1 判定液化。"""
    crr = np.asarray(crr, dtype=np.float64)
    csr = np.clip(np.asarray(csr, dtype=np.float64), 1e-6, None)
    out = crr / csr
    return out.astype(np.float32) if out.ndim else float(out)


def layer_weight(depth: float) -> float:
    """Iwasaki 深度权重 w(z)=10-0.5z（[0,10]）。"""
    return float(np.clip(10.0 - 0.5 * float(depth), 0.0, 10.0))


def lpi_raster(pga_g, n_value, depth: float = 3.0, dz: float = 3.0,
               water_table_depth: float = 2.0, fines_pct: float = 0.0) -> Tuple[np.ndarray, np.ndarray]:
    """逐像元液化指数 LPI（单层近似）与 FS。

    LPI = (1-FS)·w(z)·Δz（仅 FS<1），否则 0。恒 ≥0；随 PGA 单调增、随 N 单调减。
    """
    if np.shape(pga_g) != np.shape(n_value):
        raise ValidationError("pga/n_value shape mismatch")
    csr = np.asarray(cyclic_stress_ratio(pga_g, depth, water_table_depth), dtype=np.float64)
    crr = np.asarray(cyclic_resistance_ratio(n_value, fines_pct), dtype=np.float64)
    fs = crr / np.clip(csr, 1e-6, None)
    w = layer_weight(depth)
    lpi = np.where(fs < 1.0, (1.0 - fs) * w * float(dz), 0.0)
    return np.clip(lpi, 0.0, None).astype(np.float32), fs.astype(np.float32)


def classify_lpi(lpi: np.ndarray, breaks: Tuple[float, ...] = (5.0, 15.0)) -> np.ndarray:
    """液化等级：0=低/无(<5), 1=中(5-15), 2=高(>15)。"""
    return np.digitize(np.asarray(lpi, dtype=np.float64), list(breaks)).astype(np.int16)


# ---------------------------------------------------------------------------
# 合成数据：PGA 衰减场 + 地质 N 值 + 地下水位
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], width: int = 64, height: int = 64,
                       seed: int = 42) -> Tuple[Dict[str, np.ndarray], Dict[str, Any]]:
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    xn = xx.astype(np.float64) / max(width - 1, 1)
    yn = yy.astype(np.float64) / max(height - 1, 1)
    # PGA：从震中(0.4,0.5)向外衰减，峰值 0.4g
    r = np.hypot(xn - 0.4, yn - 0.5)
    pga = 0.4 * np.exp(-r / 0.35) + rng.normal(0, 0.01, (height, width))
    pga = np.clip(pga, 0.02, 0.6)
    # N 值：河谷松散沉积低 N（易液化），基岩高 N
    n_value = 8.0 + 25.0 * xn + rng.normal(0, 2, (height, width))
    n_value = np.clip(n_value, 2.0, 50.0)
    # 地下水位：河谷浅（0.5m），高地深（5m）
    water_table = 0.5 + 4.5 * xn + rng.normal(0, 0.2, (height, width))
    water_table = np.clip(water_table, 0.0, 8.0)
    layers = {"pga": pga.astype(np.float32), "n_value": n_value.astype(np.float32),
              "water_table": water_table.astype(np.float32)}
    info = {"bbox": bbox, "width": width, "height": height, "max_pga": float(pga.max())}
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
    # validate bbox & engineering params up front (before any disk I/O or makedirs)
    if bbox is not None:
        validate_bbox(bbox)
    validate_params(float(args.depth), float(args.fines))

    if args.input and not args.synthetic:
        if not os.path.exists(args.input):
            raise UsageError(f"input raster not found: {args.input}", path=args.input)
        cube, file_bbox, n_valid = read_geotiff_with_nodata(args.input)
        if bbox is None:
            bbox = file_bbox
            validate_bbox(bbox)
        if cube.shape[0] < 3:
            raise ValidationError(
                f"input needs >=3 bands (pga_g, n_value, water_table_depth); got {cube.shape[0]}",
                n_bands=int(cube.shape[0]),
            )
        if n_valid == 0:
            raise ValidationError(
                "input raster has no valid (non-NoData) pixels", n_bands=int(cube.shape[0])
            )
        pga, n_value, water_table = cube[0], cube[1], cube[2]
        wt_mean = float(np.nanmean(water_table))
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        layers, _info = generate_synthetic(bbox)
        pga, n_value, water_table = layers["pga"], layers["n_value"], layers["water_table"]
        wt_mean = float(np.nanmean(water_table))
        source_note = "synthetic"
        n_valid = int(np.sum(np.isfinite(pga) & np.isfinite(n_value) & np.isfinite(water_table)))

    lpi, fs = lpi_raster(pga, n_value, depth=args.depth, dz=args.depth,
                         water_table_depth=wt_mean, fines_pct=args.fines)
    level = classify_lpi(lpi)

    # create output dir only after all validations have passed
    os.makedirs(output_dir, exist_ok=True)

    lpi_tif = os.path.join(output_dir, "liquefaction_index.tif")
    write_geotiff(lpi_tif, lpi, bbox)
    fs_tif = os.path.join(output_dir, "factor_of_safety.tif")
    write_geotiff(fs_tif, fs, bbox)

    params = {"source": source_note, "depth": args.depth, "fines_pct": args.fines,
              "mean_water_table": wt_mean, "method": "Youd-Iwasaki-simplified"}
    params_path = os.path.join(output_dir, "liquefaction_params.json")
    with open(params_path, "w", encoding="utf-8") as f:
        json.dump(params, f, ensure_ascii=False, indent=2)

    n_total = int(lpi.size)
    qa: Dict[str, Any] = {
        "source": source_note,
        "mean_lpi": float(np.nanmean(lpi)) if np.any(np.isfinite(lpi)) else 0.0,
        "max_lpi": float(np.nanmax(lpi)) if np.any(np.isfinite(lpi)) else 0.0,
        "liquefied_fraction": float(np.mean(fs < 1.0)),
        "high_lpi_fraction": float(np.mean(level == 2)),
        "n_valid_pixels": n_valid,
        "n_total_pixels": n_total,
    }
    outputs = [
        {"path": lpi_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": fs_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": params_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, {"input": args.input, "bbox": bbox, "depth": args.depth,
                              "synthetic": bool(args.synthetic)}, outputs, qa, started_at, 0)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] mean LPI: {qa['mean_lpi']:.2f}  max: {qa['max_lpi']:.2f}")
        print(f"[{SKILL_NAME}] liquefied fraction (FS<1): {qa['liquefied_fraction']:.3f}")
        print(f"[{SKILL_NAME}] outputs: {output_dir}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Earthquake liquefaction risk (Youd CSR/CRR + Iwasaki LPI).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"))
    p.add_argument("--input", help="input GeoTIFF (band1=pga_g, band2=SPT N-value, band3=water table depth m)")
    p.add_argument("--depth", type=float, default=3.0, help="evaluated soil layer depth/thickness (m, default: 3)")
    p.add_argument("--fines", type=float, default=10.0, help="fines content percent (default: 10)")
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
