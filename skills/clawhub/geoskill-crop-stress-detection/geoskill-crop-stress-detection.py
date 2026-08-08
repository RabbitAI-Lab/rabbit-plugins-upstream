#!/usr/bin/env python3
"""crop-stress-detection — 作物胁迫检测

融合三路胁迫信号检测作物胁迫等级：
- **CWSI 水分胁迫指数**（冠层温度与干/湿参考温差之比）；
- **红边叶绿素**（红边叶绿素指数 CIre，反映叶绿素/氮含量）；
- **SAR 含水量**（后向散射反演的冠层含水量代理）。
归一化后加权融合为综合胁迫指数 [0,1]，并分级。

核心算法
--------
- CWSI = (Tc − Twet) / (Tdry − Twet)，0=无水分胁迫，1=最大胁迫。
- CIre = (NIR / RedEdge) − 1，越高叶绿素越多；反向归一为叶绿素胁迫。
- SAR 含水量经经验映射，反向归一为水分亏缺胁迫。

数据源：本地热红外+多光谱+SAR 栅格或 ``--synthetic`` 离线模拟。

隐私声明 / Privacy：默认离线，``--synthetic`` 完全无网络，本地处理不上传。

Usage:
    python crop-stress-detection.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "crop-stress-detection"

try:
    from _geoskill_core.errors import (
        GeoSkillError, UsageError, ValidationError, ProcessError, DependencyError, to_exit_code,
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

    class DependencyError(GeoSkillError):
        def __init__(self, m, **k): super().__init__(m, code=3, kind="EDepend", **k)

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
def compute_cwsi(canopy_temp: np.ndarray, t_wet: float, t_dry: float) -> np.ndarray:
    """作物水分胁迫指数 CWSI = (Tc − Twet)/(Tdry − Twet)，裁剪到 [0,1]。"""
    if t_dry <= t_wet:
        raise ValidationError("t_dry must exceed t_wet", t_dry=t_dry, t_wet=t_wet)
    tc = np.asarray(canopy_temp, dtype=np.float32)
    cwsi = (tc - t_wet) / (t_dry - t_wet)
    return np.clip(cwsi, 0.0, 1.0).astype(np.float32)


def chlorophyll_rededge_index(rededge: np.ndarray, nir: np.ndarray) -> np.ndarray:
    """红边叶绿素指数 CIre = NIR/RedEdge − 1（Gitelson et al.）。"""
    rededge = np.asarray(rededge, dtype=np.float32)
    nir = np.asarray(nir, dtype=np.float32)
    ratio = np.zeros_like(nir, dtype=np.float32)
    mask = rededge > 1e-6
    np.divide(nir, rededge, out=ratio, where=mask)
    return np.clip(ratio - 1.0, 0.0, None).astype(np.float32)


def chlorophyll_stress(cire: np.ndarray, ci_max: float = 4.0) -> np.ndarray:
    """叶绿素胁迫：CIre 越低胁迫越高，s = 1 − CIre/ci_max，[0,1]。"""
    if ci_max <= 0:
        raise ValidationError("ci_max must be > 0", ci_max=ci_max)
    cire = np.clip(np.asarray(cire, dtype=np.float32), 0.0, ci_max)
    return (1.0 - cire / ci_max).astype(np.float32)


def sar_water_content(sigma_vv: np.ndarray, sigma_min: float = 1e-4,
                      sigma_max: float = 1e-1) -> np.ndarray:
    """由 SAR 后向散射（线性）经验映射冠层相对含水量 [0,1]（对数拉伸）。"""
    s = np.clip(np.asarray(sigma_vv, dtype=np.float32), sigma_min, sigma_max)
    wc = (np.log10(s) - np.log10(sigma_min)) / (np.log10(sigma_max) - np.log10(sigma_min))
    return np.clip(wc, 0.0, 1.0).astype(np.float32)


def water_deficit_stress(water_content: np.ndarray) -> np.ndarray:
    """水分亏缺胁迫 = 1 − 相对含水量。"""
    return (1.0 - np.clip(np.asarray(water_content, dtype=np.float32), 0.0, 1.0)).astype(np.float32)


def fuse_stress(cwsi: np.ndarray, chl_stress: np.ndarray, water_stress: np.ndarray,
                w_cwsi: float = 0.4, w_chl: float = 0.3, w_water: float = 0.3) -> np.ndarray:
    """加权融合三路胁迫为综合胁迫指数 [0,1]。"""
    wsum = w_cwsi + w_chl + w_water
    if wsum <= 0:
        raise ValidationError("weights must sum to > 0")
    fused = (w_cwsi * np.asarray(cwsi) + w_chl * np.asarray(chl_stress)
             + w_water * np.asarray(water_stress)) / wsum
    return np.clip(fused, 0.0, 1.0).astype(np.float32)


def classify_stress(stress: np.ndarray) -> np.ndarray:
    """胁迫分级：0=无, 1=轻, 2=中, 3=重。"""
    stress = np.asarray(stress, dtype=np.float32)
    out = np.zeros(stress.shape, dtype=np.int32)
    out[stress >= 0.25] = 1
    out[stress >= 0.5] = 2
    out[stress >= 0.7] = 3
    return out


def detect_stress(canopy_temp: np.ndarray, rededge: np.ndarray, nir: np.ndarray,
                  sigma_vv: np.ndarray, t_wet: float, t_dry: float) -> Dict[str, Any]:
    """主流程：融合 CWSI + 红边叶绿素 + SAR 含水量。"""
    cwsi = compute_cwsi(canopy_temp, t_wet, t_dry)
    cire = chlorophyll_rededge_index(rededge, nir)
    chl_s = chlorophyll_stress(cire)
    wc = sar_water_content(sigma_vv)
    water_s = water_deficit_stress(wc)
    fused = fuse_stress(cwsi, chl_s, water_s)
    grade = classify_stress(fused)
    return {
        "stress": fused, "cwsi": cwsi, "cire": cire, "chlorophyll_stress": chl_s,
        "water_content": wc, "water_stress": water_s, "grade": grade,
        "stats": {
            "mean_stress": float(np.nanmean(fused)),
            "mean_cwsi": float(np.nanmean(cwsi)),
            "mean_chlorophyll_stress": float(np.nanmean(chl_s)),
            "mean_water_stress": float(np.nanmean(water_s)),
            "high_stress_fraction": float(np.mean(grade == 3)),
        },
    }


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], width: int = 64, height: int = 64, seed: int = 42):
    """波段 [canopy_temp_K, rededge, nir, sigma_vv_linear]。

    场景：左侧无胁迫（低温、高叶绿素、高含水），右侧重胁迫。
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    xx /= max(width - 1, 1)
    t_wet, t_dry = 295.0, 315.0
    # 冠层温度从左（湿，近 Twet）到右（干，近 Tdry）
    canopy_temp = (t_wet + (t_dry - t_wet) * xx + rng.normal(0, 0.5, (height, width))).astype(np.float32)
    nir = np.clip(0.50 - 0.30 * xx + rng.normal(0, 0.01, (height, width)), 0.05, 0.7)
    rededge = np.clip(0.09 + 0.05 * xx, 0.05, 0.4)  # 右侧 RedEdge 升 -> CIre 降
    # SAR 后向散射：左侧高含水 -> 高 sigma
    sigma_vv = (1e-1 * (1.0 - 0.85 * xx)).astype(np.float32)
    sigma_vv = np.clip(sigma_vv * (1 + rng.normal(0, 0.05, sigma_vv.shape)), 1e-4, 1e-1)

    cube = np.stack([canopy_temp, rededge, nir, sigma_vv], 0).astype(np.float32)
    info = {"bbox": bbox, "width": width, "height": height,
            "band_order": ["canopy_temp_K", "rededge", "nir", "sigma_vv_linear"],
            "t_wet": t_wet, "t_dry": t_dry}
    return cube, info


# ---------------------------------------------------------------------------
# 输入校验：bbox（共用同 animated-map-series 模板）
# ---------------------------------------------------------------------------
def validate_bbox(bbox: List[float]) -> None:
    """Validate a [W, S, E, N] bbox in WGS-84.

    Raises ValidationError (exit 6) for:
      - wrong length
      - non-finite values
      - longitude out of [-180, 180]
      - latitude  out of [-90, 90]
      - W >= E (would make a non-positive-width raster)
      - S >= N
    """
    if bbox is None or len(bbox) != 4:
        raise ValidationError(
            f"bbox must have 4 floats [W S E N], got {bbox!r}",
        )
    w, s, e, n = bbox
    vals = [w, s, e, n]
    if not all(np.isfinite(vals)):
        raise ValidationError(f"bbox contains non-finite values: {vals}")
    if not (-180.0 <= w <= 180.0) or not (-180.0 <= e <= 180.0):
        raise ValidationError(
            f"longitude out of [-180, 180]: W={w}, E={e}",
        )
    if not (-90.0 <= s <= 90.0) or not (-90.0 <= n <= 90.0):
        raise ValidationError(
            f"latitude out of [-90, 90]: S={s}, N={n}",
        )
    if w >= e:
        raise ValidationError(
            f"bbox W must be < E (W={w}, E={e}); cross-180 not supported; "
            f"split into two bboxes at the dateline",
        )
    if s >= n:
        raise ValidationError(
            f"bbox S must be < N (S={s}, N={n})",
        )
    if (e - w) < 1e-9 or (n - s) < 1e-9:
        raise ValidationError(
            f"bbox extent too small (W={w}, E={e}, S={s}, N={n})",
        )


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(path: str, cube: np.ndarray, bbox: List[float], nodata: float = -9999.0) -> None:
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


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float]]:
    """Read a multiband GeoTIFF, returning (cube, bbox) with NoData→NaN."""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read(masked=True).astype(np.float32)
        cube = np.ma.filled(cube, np.nan)
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
        inputs={"input": getattr(args, "input", None), "method": getattr(args, "method", None),
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
    t_wet, t_dry = args.t_wet, args.t_dry
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        cube, synth_info = generate_synthetic(bbox)
        source_note = "synthetic"

    # 校验（先于 makedirs）
    if cube.size == 0:
        raise ValidationError("input raster is empty")
    if cube.shape[0] < 4:
        raise ValidationError("input needs 4 bands [canopy_temp_K, rededge, nir, sigma_vv_linear]")
    if bbox is not None:
        validate_bbox(bbox)
    if not np.any(np.isfinite(cube)):
        raise ValidationError(
            "input cube has no valid (finite) pixels across all bands (all NoData or NaN)",
        )

    # 现在 makedirs
    os.makedirs(output_dir, exist_ok=True)

    canopy_temp, rededge, nir, sigma_vv = cube[0], cube[1], cube[2], cube[3]
    res = detect_stress(canopy_temp, rededge, nir, sigma_vv, t_wet, t_dry)

    stress_tif = os.path.join(output_dir, "stress_index.tif")
    write_geotiff(stress_tif, res["stress"], bbox)
    grade_tif = os.path.join(output_dir, "stress_grade.tif")
    write_geotiff(grade_tif, res["grade"].astype(np.float32), bbox)
    comp_tif = os.path.join(output_dir, "stress_components.tif")
    write_geotiff(comp_tif, np.stack([res["cwsi"], res["chlorophyll_stress"], res["water_stress"]], 0), bbox)

    qa = {"source": source_note, "method": args.method, "mean_stress": res["stats"]["mean_stress"],
          "mean_cwsi": res["stats"]["mean_cwsi"], "high_stress_fraction": res["stats"]["high_stress_fraction"]}
    if synth_info is not None:
        qa["synthetic"] = synth_info

    outputs = [
        {"path": stress_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": grade_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": comp_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 3},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] mean stress: {qa['mean_stress']:.4f}  mean CWSI: {qa['mean_cwsi']:.4f}")
        print(f"[{SKILL_NAME}] high-stress fraction: {qa['high_stress_fraction']:.4f}")
        print(f"[{SKILL_NAME}] output: {stress_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Crop stress detection by fusing CWSI, red-edge chlorophyll and SAR water content.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input GeoTIFF [canopy_temp_K, rededge, nir, sigma_vv_linear]")
    p.add_argument("--method", default="fusion", choices=["fusion", "cwsi-only"],
                   help="detection method (default: fusion)")
    p.add_argument("--t-wet", dest="t_wet", type=float, default=295.0,
                   help="wet reference canopy temperature K (default: 295)")
    p.add_argument("--t-dry", dest="t_dry", type=float, default=315.0,
                   help="dry reference canopy temperature K (default: 315)")
    p.add_argument("--synthetic", action="store_true", help="generate synthetic scene (offline)")
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
