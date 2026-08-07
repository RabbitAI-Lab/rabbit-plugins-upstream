#!/usr/bin/env python3
"""multi-hazard-risk-assessment — 多灾种综合风险评估

将多个单灾种风险（危险度 × 暴露度 × 脆弱性）按权重融合为综合风险指数，
并依据分位数阈值做风险分区（低/中低/中/中高/高）。

风险模型（IPCC 风险三元组的栅格化实现）：

    R_single = H' · E' · V'      （H'/E'/V' 为 [0,1] 归一化图层）
    R_multi  = Σ wᵢ · Rᵢ / Σ wᵢ  （加权平均，仍落在 [0,1]）

数据源：本地多波段 GeoTIFF（band1=危险度、band2=暴露度、band3=脆弱性），
或使用 ``--synthetic`` 生成物理一致的多灾种模拟场景用于离线测试。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python multi-hazard-risk-assessment.py --input scene.tif
    python multi-hazard-risk-assessment.py --bbox 116 39 117 40 --hazards 3 --synthetic --output-dir ./out

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
SKILL_NAME = "multi-hazard-risk-assessment"

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
def normalize01(arr: np.ndarray) -> np.ndarray:
    """Min-max 归一化到 [0,1]；常数图层返回全 0。"""
    a = np.asarray(arr, dtype=np.float64)
    finite = a[np.isfinite(a)]
    if finite.size == 0:
        return np.zeros_like(a, dtype=np.float32)
    lo, hi = float(finite.min()), float(finite.max())
    if hi - lo <= 1e-12:
        return np.zeros_like(a, dtype=np.float32)
    out = (a - lo) / (hi - lo)
    out = np.where(np.isfinite(out), out, 0.0)
    return out.astype(np.float32)


def compute_single_risk(
    hazard: np.ndarray,
    exposure: np.ndarray,
    vulnerability: np.ndarray,
) -> np.ndarray:
    """单灾种风险 = 归一化危险度 × 归一化暴露度 × 归一化脆弱性。

    三个因子先各自 min-max 归一化到 [0,1]，再逐像元相乘，结果落在 [0,1]。
    任一因子为 0 的像元风险为 0（例如无暴露则无风险）。
    """
    if not (hazard.shape == exposure.shape == vulnerability.shape):
        raise ValidationError(
            f"shape mismatch: hazard {hazard.shape}, exposure {exposure.shape}, "
            f"vulnerability {vulnerability.shape}"
        )
    h = normalize01(hazard)
    e = normalize01(exposure)
    v = normalize01(vulnerability)
    risk = h * e * v
    return np.clip(risk, 0.0, 1.0).astype(np.float32)


def combine_hazards(
    risk_layers: List[np.ndarray],
    weights: Optional[List[float]] = None,
) -> np.ndarray:
    """多灾种加权融合：R = Σ wᵢRᵢ / Σ wᵢ。

    权重缺省为等权；所有图层必须同形。结果为各风险的凸组合，仍落在 [0,1]，
    且对任一输入图层单调不减。
    """
    if not risk_layers:
        raise ValidationError("risk_layers is empty")
    shape = risk_layers[0].shape
    for r in risk_layers:
        if r.shape != shape:
            raise ValidationError(f"risk layer shape {r.shape} != {shape}")
    n = len(risk_layers)
    if weights is None:
        weights = [1.0] * n
    if len(weights) != n:
        raise ValidationError(f"weights length {len(weights)} != layers {n}")
    w = np.asarray(weights, dtype=np.float64)
    if np.any(w < 0):
        raise ValidationError("weights must be non-negative")
    wsum = float(w.sum())
    if wsum <= 1e-12:
        raise ValidationError("sum of weights must be positive")
    acc = np.zeros(shape, dtype=np.float64)
    for i, r in enumerate(risk_layers):
        acc += float(w[i]) * np.asarray(r, dtype=np.float64)
    out = acc / wsum
    return np.clip(out, 0.0, 1.0).astype(np.float32)


def classify_zones(
    risk: np.ndarray,
    breaks: Tuple[float, ...] = (0.2, 0.4, 0.6, 0.8),
) -> np.ndarray:
    """按阈值把连续风险切成整型分区（0=最低 … len(breaks)=最高）。"""
    r = np.asarray(risk, dtype=np.float64)
    zones = np.digitize(r, list(breaks), right=False)
    return zones.astype(np.int16)


# ---------------------------------------------------------------------------
# 合成数据：物理一致的多灾种场景（离线测试）
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    n_hazards: int = 3,
    width: int = 64,
    height: int = 64,
    seed: int = 42,
) -> Tuple[Dict[str, np.ndarray], Dict[str, Any]]:
    """生成 n_hazards 个危险度图层 + 共享暴露度 + 脆弱性。

    危险度用不同空间结构的高斯/斜坡场模拟（洪水沿河谷、滑坡依山、地震随断层衰减）；
    暴露度为人口型高斯斑块；脆弱性为建成度代理。全部为 float32 物理量。
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    yn = yy.astype(np.float64) / max(height - 1, 1)
    xn = xx.astype(np.float64) / max(width - 1, 1)

    hazards: List[np.ndarray] = []
    for k in range(n_hazards):
        cx = 0.3 + 0.4 * (k % 3) / 2.0
        cy = 0.3 + 0.4 * (k // 3 + (k % 2)) / 2.0
        g = np.exp(-(((xn - cx) ** 2 + (yn - cy) ** 2)) / (2 * 0.18 ** 2))
        slope = (xn + yn) / 2.0  # 地形代理
        field = 0.6 * g + 0.4 * slope
        field = field + rng.normal(0, 0.02, field.shape)
        hazards.append(np.clip(field, 0, None).astype(np.float32))

    exposure = np.exp(-(((xn - 0.5) ** 2 + (yn - 0.5) ** 2)) / (2 * 0.25 ** 2))
    exposure = (exposure * 5000.0).astype(np.float32)  # 人口密度代理

    vulnerability = (0.3 + 0.5 * exposure / max(float(exposure.max()), 1e-6)
                     + rng.normal(0, 0.03, exposure.shape))
    vulnerability = np.clip(vulnerability, 0.05, 1.0).astype(np.float32)

    layers = {
        "hazards": hazards,
        "exposure": exposure,
        "vulnerability": vulnerability,
    }
    info = {
        "bbox": bbox, "width": width, "height": height,
        "n_hazards": n_hazards,
        "mean_exposure": float(np.mean(exposure)),
    }
    return layers, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O（直接用 rasterio，保证离线可用）
# ---------------------------------------------------------------------------
def write_geotiff(path: str, cube: np.ndarray, bbox: List[float],
                  nodata: float = -9999.0, dtype: str = "float32") -> None:
    import rasterio
    from rasterio.transform import from_bounds

    if cube.ndim == 2:
        cube = cube[np.newaxis, ...]
    nb, h, w = cube.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    profile = {
        "driver": "GTiff", "height": h, "width": w, "count": nb,
        "dtype": dtype, "crs": "EPSG:4326", "transform": transform,
        "nodata": nodata, "compress": "deflate",
    }
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
# 输入校验（前置；统一 exit code = 6 ValidationError）
# ---------------------------------------------------------------------------
def validate_bbox(bbox: Any) -> List[float]:
    """W<E、S<N、坐标超范围、零面积、跨 180° 经线 → ValidationError。"""
    if not bbox or len(bbox) != 4:
        raise ValidationError("bbox must be 4 floats [W S E N]", bbox=bbox)
    W, S, E, N = [float(x) for x in bbox]
    if not (all(np.isfinite([W, S, E, N]))):
        raise ValidationError("bbox must be finite", bbox=[W, S, E, N])
    if not (-180.0 <= W <= 180.0 and -180.0 <= E <= 180.0):
        raise ValidationError("longitude out of [-180, 180]", W=W, E=E)
    if not (-90.0 <= S <= 90.0 and -90.0 <= N <= 90.0):
        raise ValidationError("latitude out of [-90, 90]", S=S, N=N)
    if W >= E:
        raise ValidationError(
            f"bbox W must be < E (W={W}, E={E})", W=W, E=E)
    if S >= N:
        raise ValidationError(
            f"bbox S must be < N (S={S}, N={N})", S=S, N=N)
    if (E - W) * (N - S) <= 0.0:
        raise ValidationError("bbox area is zero or negative", area=(E - W) * (N - S))
    return [W, S, E, N]


def validate_breaks(breaks: Any) -> Tuple[float, ...]:
    """分区阈值必须 0<=b<1（端点 1.0 会让整图落入 0 区），且严格单调递增。"""
    if not breaks:
        raise ValidationError("breaks must not be empty")
    vals: List[float] = []
    for b in breaks:
        v = float(b)
        if not np.isfinite(v):
            raise ValidationError("breaks must be finite", value=v)
        if not (0.0 <= v < 1.0):
            raise ValidationError(
                f"each break must be in [0, 1) (got {v})", value=v)
        vals.append(v)
    if any(vals[i] >= vals[i + 1] for i in range(len(vals) - 1)):
        raise ValidationError(
            f"breaks must be strictly increasing (got {vals})", breaks=vals)
    return tuple(vals)


def validate_hazards(n_hazards: int) -> int:
    """合成灾种数必须 >= 1。"""
    if not isinstance(n_hazards, int):
        raise ValidationError("hazards must be an integer", n_hazards=n_hazards)
    if n_hazards < 1:
        raise ValidationError(
            f"hazards must be >= 1 (got {n_hazards})", n_hazards=n_hazards)
    return n_hazards


# ---------------------------------------------------------------------------
# 主流程
# ---------------------------------------------------------------------------
def process(args: argparse.Namespace) -> int:
    started_at = _utc_now()
    output_dir = args.output_dir
    bbox = list(args.bbox) if args.bbox else None
    breaks = tuple(args.breaks) if args.breaks else None

    # 校验前置（input 模式：bbox 可选；synthetic 模式：bbox 与 hazards 必填）
    if args.input and not args.synthetic:
        if not os.path.exists(args.input):
            raise UsageError(f"input raster not found: {args.input}", path=args.input)
        if bbox is not None:
            bbox = validate_bbox(bbox)
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        bbox = validate_bbox(bbox)
        n_hazards = validate_hazards(args.hazards)
    if breaks is None:
        breaks = (0.2, 0.4, 0.6, 0.8)
    else:
        breaks = validate_breaks(breaks)

    os.makedirs(output_dir, exist_ok=True)

    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        if cube.shape[0] < 3:
            raise ValidationError("input raster needs >=3 bands (hazard, exposure, vulnerability)")
        hazard_layers = [cube[0]]
        exposure = cube[1]
        vulnerability = cube[2]
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        layers, _info = generate_synthetic(bbox, n_hazards=n_hazards)
        hazard_layers = layers["hazards"]
        exposure = layers["exposure"]
        vulnerability = layers["vulnerability"]
        source_note = "synthetic"

    # 单灾种风险
    risks = [compute_single_risk(h, exposure, vulnerability) for h in hazard_layers]
    weights = [1.0] * len(risks)
    combined = combine_hazards(risks, weights)
    zones = classify_zones(combined, breaks=breaks)

    risk_tif = os.path.join(output_dir, "risk_index.tif")
    write_geotiff(risk_tif, combined, bbox)
    zone_tif = os.path.join(output_dir, "risk_zones.tif")
    write_geotiff(zone_tif, zones.astype("int16"), bbox, nodata=-1, dtype="int16")

    # 分区面积占比
    zone_frac = {}
    total = zones.size
    for z in range(len(breaks) + 1):
        zone_frac[f"zone_{z}"] = float(np.count_nonzero(zones == z) / total)

    params = {
        "source": source_note,
        "n_hazards": len(risks),
        "breaks": list(breaks),
        "weights": weights,
        "mean_single_risk": [float(np.mean(r)) for r in risks],
    }
    params_path = os.path.join(output_dir, "risk_params.json")
    with open(params_path, "w", encoding="utf-8") as f:
        json.dump(params, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "n_hazards": len(risks),
        "mean_risk": float(np.mean(combined)),
        "max_risk": float(np.max(combined)),
        "zone_area_fraction": zone_frac,
        "high_risk_fraction": float(np.mean(combined >= breaks[-1])),
    }
    outputs = [
        {"path": risk_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": zone_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": params_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, {"input": args.input, "bbox": bbox,
                              "hazards": len(risks), "synthetic": bool(args.synthetic)},
                              outputs, qa, started_at, 0)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] hazards: {len(risks)}  shape: {combined.shape}")
        print(f"[{SKILL_NAME}] mean risk: {qa['mean_risk']:.4f}  max: {qa['max_risk']:.4f}")
        print(f"[{SKILL_NAME}] risk:  {risk_tif}")
        print(f"[{SKILL_NAME}] zones: {zone_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Multi-hazard risk assessment (hazard x exposure x vulnerability).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input GeoTIFF (band1=hazard, band2=exposure, band3=vulnerability)")
    p.add_argument("--hazards", type=int, default=3, help="number of synthetic hazard layers (default: 3)")
    p.add_argument("--breaks", nargs="+", type=float, default=[0.2, 0.4, 0.6, 0.8],
                   help="zone classification thresholds (default: 0.2 0.4 0.6 0.8)")
    p.add_argument("--synthetic", action="store_true", help="generate a synthetic scene (offline)")
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
