#!/usr/bin/env python3
"""pest-disease-detection — 病虫害遥感检测

融合红边异常、热红外温度异常、纹理变化与多时相早期胁迫信号，识别疑似
病虫害胁迫区域并给出概率图。

核心算法
--------
- **红边异常**：NDRE 相对基线的负偏差（叶绿素下降 → 红边反射降低）。
- **热红外异常**：LST 相对基线的正偏差（气孔关闭 → 冠层升温）。
- **纹理变化**：滑动窗口方差，病虫害常造成冠层空间异质性升高。
- **多时相早期胁迫**：当期 NDVI 相对上一期的下降幅度。
- 四路信号归一化后加权融合为 pest 概率 [0,1]。

数据源：本地多时相多光谱 + 热红外 GeoTIFF，或 ``--synthetic`` 离线模拟。

隐私声明 / Privacy：默认离线，``--synthetic`` 完全无网络，本地处理不上传。

Usage:
    python pest-disease-detection.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "pest-disease-detection"

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
# Validation helpers
# ---------------------------------------------------------------------------
def validate_bbox(bbox: List[float], source: str = "bbox") -> None:
    """Validate geographic bbox: W<=E, S<=N, lon/lat in range, min area.

    Cross-dateline (W>E) is a ValidationError with a hint to split.
    """
    if bbox is None or len(bbox) != 4:
        raise ValidationError(f"{source}: expected 4 floats [W S E N], got {bbox!r}")
    try:
        w, s, e, n = (float(v) for v in bbox)
    except (TypeError, ValueError) as exc:
        raise ValidationError(f"{source}: non-numeric bbox values: {bbox!r}") from exc
    for v, name in ((w, "W"), (s, "S"), (e, "E"), (n, "N")):
        if not (v == v):
            raise ValidationError(f"{source}: bbox contains NaN at {name}")
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(f"{source}: lon out of [-180,180]: W={w} E={e}")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(f"{source}: lat out of [-90,90]: S={s} N={n}")
    if w > e:
        raise ValidationError(
            f"{source}: W ({w}) > E ({e}); cross-dateline bboxes are not supported. "
            "Split into two bboxes on each side of the 180\u00b0 meridian and run separately."
        )
    if s > n:
        raise ValidationError(f"{source}: S ({s}) > N ({n})")
    if (e - w) < 1e-9 or (n - s) < 1e-9:
        raise ValidationError(
            f"{source}: bbox too small (dlon={e - w}, dlat={n - s}); need > 1e-9 degrees"
        )


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def _safe_ratio(num: np.ndarray, den: np.ndarray) -> np.ndarray:
    out = np.zeros_like(num, dtype=np.float32)
    mask = np.abs(den) > 1e-9
    np.divide(num, den, out=out, where=mask)
    return out


def compute_ndvi(red: np.ndarray, nir: np.ndarray) -> np.ndarray:
    red = np.asarray(red, dtype=np.float32)
    nir = np.asarray(nir, dtype=np.float32)
    return np.clip(_safe_ratio(nir - red, nir + red), -1.0, 1.0).astype(np.float32)


def compute_ndre(rededge: np.ndarray, nir: np.ndarray) -> np.ndarray:
    rededge = np.asarray(rededge, dtype=np.float32)
    nir = np.asarray(nir, dtype=np.float32)
    return np.clip(_safe_ratio(nir - rededge, nir + rededge), -1.0, 1.0).astype(np.float32)


def rededge_anomaly(ndre: np.ndarray, baseline: np.ndarray) -> np.ndarray:
    """红边异常 = (基线 NDRE - 当前 NDRE)，正值=叶绿素下降。"""
    return (np.asarray(baseline, dtype=np.float32) - np.asarray(ndre, dtype=np.float32)).astype(np.float32)


def thermal_anomaly(lst: np.ndarray, baseline: np.ndarray) -> np.ndarray:
    """热红外异常 = (当前 LST - 基线 LST)，正值=冠层升温。"""
    return (np.asarray(lst, dtype=np.float32) - np.asarray(baseline, dtype=np.float32)).astype(np.float32)


def texture_variance(arr: np.ndarray, window: int = 3) -> np.ndarray:
    """滑动窗口方差（空间纹理），窗口越大越平滑。病虫害升高异质性。"""
    try:
        from scipy.ndimage import uniform_filter
    except ImportError as exc:  # pragma: no cover
        raise DependencyError("scipy is required for texture analysis") from exc
    arr = np.asarray(arr, dtype=np.float32)
    w = max(3, int(window) | 1)  # 保证奇数
    mean = uniform_filter(arr, size=w, mode="reflect")
    mean_sq = uniform_filter(arr * arr, size=w, mode="reflect")
    var = mean_sq - mean * mean
    return np.clip(var, 0.0, None).astype(np.float32)


def temporal_decline(ndvi_now: np.ndarray, ndvi_prev: np.ndarray) -> np.ndarray:
    """多时相早期胁迫 = max(0, NDVI_prev - NDVI_now)，正值=长势下降。"""
    diff = np.asarray(ndvi_prev, dtype=np.float32) - np.asarray(ndvi_now, dtype=np.float32)
    return np.clip(diff, 0.0, None).astype(np.float32)


def _norm(arr: np.ndarray, scale: float) -> np.ndarray:
    """把非负异常量按特征尺度 scale 压到 [0,1]（1 - exp(-x/scale)）。"""
    arr = np.clip(np.asarray(arr, dtype=np.float32), 0.0, None)
    if scale <= 0:
        raise ValidationError("scale must be > 0", scale=scale)
    return (1.0 - np.exp(-arr / scale)).astype(np.float32)


def pest_probability(
    red_anom: np.ndarray,
    therm_anom: np.ndarray,
    texture: np.ndarray,
    decline: np.ndarray,
    w_red: float = 0.3,
    w_therm: float = 0.25,
    w_texture: float = 0.2,
    w_decline: float = 0.25,
) -> np.ndarray:
    """融合四路异常信号为病虫害概率 [0,1]。"""
    p_red = _norm(red_anom, 0.05)
    p_therm = _norm(therm_anom, 3.0)
    p_tex = _norm(texture, 0.002)
    p_dec = _norm(decline, 0.1)
    wsum = w_red + w_therm + w_texture + w_decline
    prob = (w_red * p_red + w_therm * p_therm + w_texture * p_tex + w_decline * p_dec) / wsum
    return np.clip(prob, 0.0, 1.0).astype(np.float32)


def classify_risk(prob: np.ndarray) -> np.ndarray:
    """风险分级：0=无, 1=低, 2=中, 3=高。"""
    prob = np.asarray(prob, dtype=np.float32)
    out = np.zeros(prob.shape, dtype=np.int32)
    out[prob >= 0.25] = 1
    out[prob >= 0.5] = 2
    out[prob >= 0.7] = 3
    return out


def detect(
    cube_now: np.ndarray,
    cube_prev: np.ndarray,
    ndre_baseline: np.ndarray,
    lst_baseline: np.ndarray,
) -> Dict[str, Any]:
    """主流程。波段顺序 [Red, RedEdge, NIR, LST]。"""
    cube_now = np.asarray(cube_now, dtype=np.float32)
    cube_prev = np.asarray(cube_prev, dtype=np.float32)
    for c in (cube_now, cube_prev):
        if c.ndim != 3 or c.shape[0] < 4:
            raise ValidationError("each epoch needs >=4 bands [Red, RedEdge, NIR, LST]")
    red, rededge, nir, lst = cube_now[0], cube_now[1], cube_now[2], cube_now[3]
    red_p, _, nir_p, _ = cube_prev[0], cube_prev[1], cube_prev[2], cube_prev[3]

    # NaN-safe computations: NaN pixels in any input propagate to NaN in
    # NDRE/NDVI/anomaly, then to NaN in the four normalized channels. The
    # final probability is masked to 0 for NaN inputs (a transparent
    # convention) so the spatial statistics and risk classification are not
    # biased by NoData.
    finite = np.isfinite(red) & np.isfinite(rededge) & np.isfinite(nir) & np.isfinite(lst)
    if not finite.any():
        raise ValidationError("cube_now has no valid (non-NoData) pixels in [Red, RedEdge, NIR, LST]")

    def _safe(arr: np.ndarray) -> np.ndarray:
        return np.where(finite, arr, 0.0).astype(np.float32)

    red_s, rededge_s, nir_s, lst_s = _safe(red), _safe(rededge), _safe(nir), _safe(lst)
    red_p_s, nir_p_s = _safe(red_p), _safe(nir_p)

    ndre = compute_ndre(rededge_s, nir_s)
    ndvi = compute_ndvi(red_s, nir_s)
    ndvi_prev = compute_ndvi(red_p_s, nir_p_s)

    red_anom = rededge_anomaly(ndre, ndre_baseline)
    therm_anom = thermal_anomaly(lst_s, lst_baseline)
    texture = texture_variance(nir_s, window=3)
    decline = temporal_decline(ndvi, ndvi_prev)

    prob = pest_probability(red_anom, therm_anom, texture, decline)
    # Mask NoData pixels in the probability/risk layers
    prob = np.where(finite, prob, 0.0).astype(np.float32)
    risk = classify_risk(prob)
    # NoData region gets a sentinel risk class for transparency
    risk = np.where(finite, risk, 255).astype(np.int32)

    # NaN-aware stats
    valid_prob = prob[finite]
    valid_red = red_anom[finite]
    valid_therm = therm_anom[finite]
    valid_risk = risk[finite]
    return {
        "prob": prob,
        "risk": risk,
        "red_anom": red_anom,
        "therm_anom": therm_anom,
        "texture": texture,
        "decline": decline,
        "stats": {
            "mean_prob": float(np.mean(valid_prob)) if valid_prob.size else 0.0,
            "high_risk_fraction": float(np.mean(valid_risk == 3)) if valid_risk.size else 0.0,
            "mean_red_anom": float(np.mean(valid_red)) if valid_red.size else 0.0,
            "mean_therm_anom": float(np.mean(valid_therm)) if valid_therm.size else 0.0,
            "n_valid_pixels": int(finite.sum()),
        },
    }


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], width: int = 64, height: int = 64, seed: int = 42):
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    xx /= max(width - 1, 1)
    yy /= max(height - 1, 1)

    # 上一期：均匀健康农田
    def make_epoch(nir_base, lst_base, noise):
        red = np.full((height, width), 0.05, dtype=np.float32)
        rededge = np.full((height, width), 0.09, dtype=np.float32)
        nir = np.full((height, width), nir_base, dtype=np.float32)
        lst = np.full((height, width), lst_base, dtype=np.float32)
        nir += rng.normal(0, noise, nir.shape).astype(np.float32)
        return np.stack([red, rededge, nir, lst], axis=0).astype(np.float32)

    cube_prev = make_epoch(0.50, 298.0, 0.004)

    # 当期：中心圆形病虫害斑块（NIR 降、LST 升、纹理增）
    cx, cy = 0.5, 0.5
    dist = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2)
    patch = np.clip(1.0 - dist / 0.22, 0.0, 1.0)  # 中心强，向外衰减

    cube_now = make_epoch(0.50, 298.0, 0.004)
    cube_now[2] -= (0.28 * patch)  # NIR 下降
    cube_now[3] += (14.0 * patch)  # LST 上升
    cube_now[2] += (rng.normal(0, 0.03, (height, width)) * patch).astype(np.float32)  # 纹理

    ndre_baseline = np.full((height, width), 0.68, dtype=np.float32)
    lst_baseline = np.full((height, width), 298.0, dtype=np.float32)

    info = {
        "bbox": bbox, "width": width, "height": height,
        "band_order": ["Red", "RedEdge", "NIR", "LST"],
        "patch_center": [cx, cy], "patch_radius": 0.22,
    }
    aux = {"cube_prev": cube_prev, "ndre_baseline": ndre_baseline, "lst_baseline": lst_baseline}
    return cube_now, {"info": info, "aux": aux}


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
    os.makedirs(output_dir, exist_ok=True)
    bbox = list(args.bbox) if args.bbox else None

    aux: Dict[str, np.ndarray] = {}
    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        # Validate band count up-front so a 1/2/3-band file gives rc=6 (data
        # error) rather than rc=7 from a downstream IndexError.
        if cube.ndim != 3 or cube.shape[0] < 4:
            raise ValidationError(
                f"--input needs >=4 bands [Red, RedEdge, NIR, LST]; got shape {cube.shape}"
            )
        # Replace NoData sentinel with NaN across the cube so the four anomaly
        # channels are not dominated by -9999 in the spatial statistics and
        # mean baseline.
        import rasterio as _rio
        with _rio.open(args.input) as _src:
            _nd = _src.nodata
        if _nd is not None:
            cube = np.where(cube == _nd, np.nan, cube).astype(np.float32)
        # Reject fully NoData inputs
        if not np.isfinite(cube).any():
            raise ValidationError(
                f"input raster '{args.input}' contains only NoData pixels; nothing to detect"
            )
        # NaN-safe band means for the synthetic-style baseline. If a band has
        # no valid pixels, fall back to 0 so the anomalies stay finite.
        def _band_mean(b_idx: int) -> float:
            v = cube[b_idx]
            finite = v[np.isfinite(v)]
            return float(finite.mean()) if finite.size else 0.0
        # 无多时相/基线时用当期自身做退化基线
        aux = {"cube_prev": cube.copy(),
               "ndre_baseline": np.full(cube.shape[1:], _band_mean(1), dtype=np.float32),
               "lst_baseline": np.full(cube.shape[1:], _band_mean(3), dtype=np.float32)}
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox, source="--bbox")
        cube, packed = generate_synthetic(bbox)
        aux = packed["aux"]
        synth_info = packed["info"]
        source_note = "synthetic"

    if cube.size == 0:
        raise ValidationError("input raster is empty")

    # If --bbox is also given with --input, validate the user-supplied bbox
    if bbox is not None and args.bbox is not None:
        validate_bbox(bbox, source="--bbox")

    res = detect(cube, aux["cube_prev"], aux["ndre_baseline"], aux["lst_baseline"])

    prob_tif = os.path.join(output_dir, "pest_probability.tif")
    write_geotiff(prob_tif, res["prob"], bbox)
    risk_tif = os.path.join(output_dir, "pest_risk.tif")
    write_geotiff(risk_tif, res["risk"].astype(np.float32), bbox)
    signals_tif = os.path.join(output_dir, "stress_signals.tif")
    write_geotiff(signals_tif, np.stack([res["red_anom"], res["therm_anom"], res["decline"]], 0), bbox)

    qa = {"source": source_note, "method": args.method, "mean_prob": res["stats"]["mean_prob"],
          "high_risk_fraction": res["stats"]["high_risk_fraction"]}
    if synth_info is not None:
        qa["synthetic"] = synth_info

    outputs = [
        {"path": prob_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": risk_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": signals_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 3},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] mean prob: {qa['mean_prob']:.4f}  high-risk frac: {qa['high_risk_fraction']:.4f}")
        print(f"[{SKILL_NAME}] output: {prob_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Pest and disease detection from red-edge, thermal, texture and multi-temporal stress.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input GeoTIFF with bands [Red, RedEdge, NIR, LST]")
    p.add_argument("--method", default="fusion", choices=["fusion", "single-temporal"],
                   help="detection strategy (default: fusion)")
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
