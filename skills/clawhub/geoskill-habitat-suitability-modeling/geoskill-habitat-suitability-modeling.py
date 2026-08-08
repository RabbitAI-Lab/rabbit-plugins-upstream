#!/usr/bin/env python3
"""habitat-suitability-modeling — 栖息地适宜性建模

由多变量环境栅格（温度、降水、植被、地形等）训练一个物种分布模型，输出
0–1 的栖息地适宜性概率，并给出各环境变量的相对贡献。实现两种模型：

- **rf**（随机森林，RandomForest）：非线性、可输出特征重要度。
- **logreg**（逻辑回归，Logistic Regression）：线性可解释、系数即贡献方向。

样本：``--synthetic`` 模式用已知生态位生成 presence/absence 标签；真实
``--input`` 模式用高分位适宜度生成伪 presence（unsupervised fallback）。

数据源：本地多波段 GeoTIFF（各波段=环境变量），或 ``--synthetic`` 离线模拟。

隐私声明 / Privacy：
- 默认离线运行，仅 ``--place`` 解析地名时才访问 Nominatim/Open-Meteo。
- ``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python habitat-suitability-modeling.py --input env.tif --model rf
    python habitat-suitability-modeling.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "habitat-suitability-modeling"

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


ENV_BANDS = ["temperature", "precipitation", "ndvi", "elevation"]
MODELS = ["logreg", "rf"]


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# 输入校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox):
    """Validate a geographic bbox [W, S, E, N] in EPSG:4326.

    Rules (consistent across the project):
      - W < E (no antimeridian wrap; user must split the request)
      - S < N
      - -180 <= W, E <= 180
      - -90 <= S, N <= 90
    Returns the bbox on success; raises ValidationError on failure.
    """
    if not isinstance(bbox, (list, tuple)) or len(bbox) != 4:
        raise ValidationError("bbox must be a sequence of 4 floats [W S E N]")
    w, s, e, n = [float(v) for v in bbox]
    if not (w < e):
        raise ValidationError(
            f"bbox W={w} must be < E={e} (antimeridian wrap not supported; "
            f"split your request into two boxes if needed)")
    if not (s < n):
        raise ValidationError(f"bbox S={s} must be < N={n}")
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"bbox lon must be in [-180, 180], got W={w}, E={e}")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"bbox lat must be in [-90, 90], got S={s}, N={n}")
    return [w, s, e, n]


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def normalize_stack(stack: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """逐波段 min-max 归一化到 [0, 1]。返回 (normalized, mins, maxs)。"""
    nb = stack.shape[0]
    out = np.empty_like(stack, dtype=np.float32)
    mins = np.zeros(nb, dtype=np.float64)
    maxs = np.zeros(nb, dtype=np.float64)
    for b in range(nb):
        band = stack[b].astype(np.float64)
        finite = band[np.isfinite(band)]
        lo = float(np.min(finite)) if finite.size else 0.0
        hi = float(np.max(finite)) if finite.size else 1.0
        mins[b], maxs[b] = lo, hi
        rng = hi - lo
        if rng < 1e-9:
            out[b] = 0.0
        else:
            out[b] = np.clip((band - lo) / rng, 0.0, 1.0)
    return out, mins, maxs


def build_samples(env_norm: np.ndarray, presence: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """把 (nbands, H, W) 环境栈与 (H, W) presence 拉平为 (X, y)。"""
    nb = env_norm.shape[0]
    X = env_norm.reshape(nb, -1).T.astype(np.float32)
    y = presence.reshape(-1).astype(np.int32)
    return X, y


def fit_suitability(X: np.ndarray, y: np.ndarray, model: str = "rf", seed: int = 42) -> Any:
    """训练物种分布模型。model ∈ {rf, logreg}。"""
    if model == "rf":
        from sklearn.ensemble import RandomForestClassifier
        m = RandomForestClassifier(n_estimators=60, max_depth=8, random_state=seed, n_jobs=1)
    elif model == "logreg":
        from sklearn.linear_model import LogisticRegression
        m = LogisticRegression(max_iter=2000, random_state=seed)
    else:
        raise UsageError(f"unknown model '{model}'. Choose from: {sorted(MODELS)}", model=model)
    if len(np.unique(y)) < 2:
        raise ValidationError("presence labels need both 0 and 1 classes", n_unique=int(len(np.unique(y))))
    m.fit(X, y)
    return m


def predict_suitability(model: Any, env_norm: np.ndarray) -> np.ndarray:
    """预测适宜性概率 ∈ [0, 1]，形状 (H, W)。"""
    nb, h, w = env_norm.shape
    X = env_norm.reshape(nb, -1).T.astype(np.float32)
    proba = model.predict_proba(X)
    # 取正类（presence=1）列
    pos_idx = list(model.classes_).index(1) if 1 in list(model.classes_) else proba.shape[1] - 1
    prob = proba[:, pos_idx]
    return prob.reshape(h, w).astype(np.float32)


def variable_importance(model: Any, names: List[str]) -> Dict[str, float]:
    """各变量的相对贡献（归一化和为 1）。RF 用 feature_importances_；
    logreg 用系数绝对值归一化。"""
    if hasattr(model, "feature_importances_"):
        imp = np.asarray(model.feature_importances_, dtype=np.float64)
    else:
        imp = np.abs(np.asarray(model.coef_[0], dtype=np.float64))
    total = imp.sum()
    if total < 1e-12:
        imp = np.ones_like(imp) / imp.size
    else:
        imp = imp / total
    return {names[i]: float(imp[i]) for i in range(min(len(names), imp.size))}


def cross_val_auc(X: np.ndarray, y: np.ndarray, model: str = "rf", seed: int = 42) -> float:
    """3 折交叉验证 AUC，度量模型判别能力（>0.5 表示学到信号）。"""
    from sklearn.metrics import roc_auc_score
    from sklearn.model_selection import cross_val_predict

    m = fit_suitability(X, y, model=model, seed=seed)
    proba = cross_val_predict(m, X, y, cv=3, method="predict_proba")
    pos_idx = list(m.classes_).index(1) if 1 in list(m.classes_) else proba.shape[1] - 1
    return float(roc_auc_score(y, proba[:, pos_idx]))


# ---------------------------------------------------------------------------
# 合成数据：已知生态位的 presence/absence（离线测试）
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 128,
    height: int = 128,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """返回 (env_stack(4,H,W), presence(H,W), info)。

    presence 主要由 ndvi 驱动（ndvi>0.55 偏好），叠加少量噪声，
    使 RF / logreg 能稳定学到 ndvi 为主导变量。
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    yy /= max(height - 1, 1)
    xx /= max(width - 1, 1)

    temp = 15.0 + 15.0 * xx + rng.normal(0, 0.5, xx.shape).astype(np.float32)
    precip = 400.0 + 800.0 * yy + rng.normal(0, 20.0, yy.shape).astype(np.float32)
    # ndvi：两个高植被斑块
    bump = (
        np.exp(-(((xx - 0.3) ** 2 + (yy - 0.7) ** 2) / 0.03))
        + np.exp(-(((xx - 0.75) ** 2 + (yy - 0.35) ** 2) / 0.04))
    )
    ndvi = np.clip(0.15 + 0.7 * bump + rng.normal(0, 0.03, xx.shape), 0.0, 1.0).astype(np.float32)
    elev = 100.0 + 900.0 * (1.0 - yy) + rng.normal(0, 15.0, xx.shape).astype(np.float32)

    stack = np.stack([temp, precip, ndvi, elev], axis=0).astype(np.float32)

    # 生态位：ndvi 归一化 > 0.55 偏好，含 8% 标签翻转噪声
    ndvi_n = (ndvi - ndvi.min()) / (ndvi.max() - ndvi.min() + 1e-9)
    p = np.clip((ndvi_n - 0.55) / 0.15, 0.0, 1.0)
    presence = (rng.random(p.shape) < p).astype(np.uint8)
    flip = rng.random(p.shape) < 0.08
    presence[flip] = 1 - presence[flip]

    info = {
        "bbox": bbox,
        "width": width,
        "height": height,
        "bands": ENV_BANDS,
        "prevalence": float(np.mean(presence)),
    }
    return stack, presence, info


def pseudo_presence(env_norm: np.ndarray, quantile: float = 0.80) -> np.ndarray:
    """真实输入无标签时，用环境适宜度（各波段均值）高分位作伪 presence。"""
    fav = np.mean(env_norm, axis=0)
    thr = np.quantile(fav, quantile)
    return (fav >= thr).astype(np.uint8)


# ---------------------------------------------------------------------------
# GeoTIFF I/O（直接用 rasterio，保证离线可用）
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
    """Read an environmental multi-band GeoTIFF. Returns (cube, bbox).

    NoData values declared in the file are replaced with NaN in the returned
    cube. Callers should treat any NaN as a non-finite observation.
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nodata = src.nodata
    if nodata is not None:
        cube = np.where(cube == float(nodata), np.nan, cube)
    return cube, bbox


def finite_pixel_mask(cube: np.ndarray) -> np.ndarray:
    """Per-pixel mask: True iff every band is finite (not NaN/inf)."""
    return np.isfinite(np.asarray(cube)).all(axis=0)


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
            "model": getattr(args, "model", None),
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

    # --- pre-flight validation (BEFORE making output dir) -----------------
    bbox = list(args.bbox) if args.bbox else None

    synth_info: Optional[Dict[str, Any]] = None
    input_nodata_value: Optional[float] = None
    n_valid = 0
    band_names: List[str]
    if args.input and not args.synthetic:
        stack, file_bbox = read_geotiff(args.input)
        # Re-read to capture the declared NoData value for the qa/manifest.
        # (We do this without re-opening the file by inspecting the
        # stored nodata via an env-stashed handle, but rasterio returns
        # it via src.nodata above; we mirror that to a known local here.)
        import rasterio as _rio
        with _rio.open(args.input) as _src:
            input_nodata_value = _src.nodata
        if bbox is not None:
            bbox = validate_bbox(bbox)
        else:
            bbox = validate_bbox(file_bbox)
        if stack.shape[0] < 1:
            raise ValidationError("input raster has no bands")
        if stack.size == 0:
            raise ValidationError("input raster is empty")
        valid = finite_pixel_mask(stack)
        n_valid = int(valid.sum())
        if n_valid == 0:
            raise ValidationError(
                f"input raster has no valid pixels "
                f"(all values are nodata={input_nodata_value})")
        source_note = args.input
        env_norm, _, _ = normalize_stack(stack)
        presence = pseudo_presence(env_norm, quantile=0.80)
        band_names = [f"band_{i}" for i in range(stack.shape[0])]
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        bbox = validate_bbox(bbox)
        stack, presence, synth_info = generate_synthetic(bbox)
        env_norm, _, _ = normalize_stack(stack)
        n_valid = int(presence.size)
        source_note = "synthetic"
        band_names = list(ENV_BANDS)

    # All checks passed → now create the output dir.
    os.makedirs(output_dir, exist_ok=True)

    X, y = build_samples(env_norm, presence)
    model = fit_suitability(X, y, model=args.model, seed=args.seed)
    suitability = predict_suitability(model, env_norm)
    importance = variable_importance(model, band_names)
    auc = cross_val_auc(X, y, model=args.model, seed=args.seed)

    out_tif = os.path.join(output_dir, "habitat_suitability.tif")
    write_geotiff(out_tif, suitability, bbox)

    params = {
        "model": args.model,
        "n_samples": int(X.shape[0]),
        "n_features": int(X.shape[1]),
        "prevalence": float(np.mean(y)),
        "cv_auc": auc,
        "variable_importance": importance,
        "band_names": band_names,
    }
    params_path = os.path.join(output_dir, "suitability_params.json")
    with open(params_path, "w", encoding="utf-8") as f:
        json.dump(params, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "model": args.model,
        "cv_auc": auc,
        "mean_suitability": float(np.mean(suitability)),
        "top_variable": max(importance, key=importance.get),
        "prevalence": float(np.mean(y)),
        "n_valid_pixels": n_valid,
    }
    if input_nodata_value is not None:
        qa["input_nodata"] = input_nodata_value
    if synth_info is not None:
        qa["synthetic_prevalence"] = synth_info["prevalence"]

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": params_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] model: {args.model}  CV AUC: {auc:.3f}")
        print(f"[{SKILL_NAME}] top variable: {qa['top_variable']} ({importance[qa['top_variable']]:.3f})")
        print(f"[{SKILL_NAME}] mean suitability: {qa['mean_suitability']:.3f}")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Habitat suitability modeling (RF / logistic regression) from environmental rasters.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input multi-band GeoTIFF (each band = environmental variable)")
    p.add_argument("--model", default="rf", choices=MODELS,
                   help="species distribution model (default: rf)")
    p.add_argument("--seed", type=int, default=42, help="random seed (default: 42)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a synthetic niche scene with known presence (offline)")
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
