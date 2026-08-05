#!/usr/bin/env python3
"""time-series-classification — 时序特征分类

从 NDVI 时间序列提取物候特征并用随机森林（RandomForest）做逐像元地物/作物
分类。提取的特征包括：

- **峰值 / 谷值**（max / min NDVI）
- **振幅**（amplitude = max - min）
- **均值**（mean）
- **峰值相位**（peak_time，达到峰值的时刻）
- **生长季长度**（growing_season_length，高于半振幅阈值的期数）
- **峰个数**（n_peaks，识别双季作物的双峰物候）

特征向量送入 RandomForest 训练（训练样本来自带噪声的类别物候模板），输出
分类栅格 + 特征重要性 + 各类典型物候曲线。

类别：1=双季稻（双峰）、2=单季稻（强单峰）、3=常绿林（平坦高值）、
4=落叶林（单峰深谷）。

数据源：本地多期 NDVI GeoTIFF（``--input``）或 ``--synthetic`` 生成含真值的
模拟时序场景（离线）。

隐私声明 / Privacy：
- 默认离线运行，完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python time-series-classification.py --bbox 116 39 117 40 --n-dates 12 --output-dir ./out
    python time-series-classification.py --input ndvi_stack.tif --output-dir ./out

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
SKILL_NAME = "time-series-classification"

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


CLASS_NAMES: Dict[int, str] = {
    1: "double_rice",
    2: "single_rice",
    3: "evergreen_forest",
    4: "deciduous_forest",
}
FEATURE_NAMES = [
    "max", "min", "amplitude", "mean",
    "peak_time", "growing_season_length", "n_peaks",
]


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# bbox validation
# ---------------------------------------------------------------------------
def validate_bbox(bbox, *, kind: str = "bbox"):
    """校验 W<S<E<N、lat∈[-90,90]、lon∈[-180,180]、跨 180° 单独报错。

    返回 [W, S, E, N]。失败抛 ValidationError (rc=6)。
    """
    if bbox is None:
        raise ValidationError(f"{kind} is required")
    if len(bbox) != 4:
        raise ValidationError(f"{kind} must have 4 floats [W S E N], got {len(bbox)}",
                              bbox=list(bbox))
    w, s, e, n = (float(x) for x in bbox)
    if not all(np.isfinite(v) for v in (w, s, e, n)):
        raise ValidationError(f"{kind} contains non-finite values", bbox=[w, s, e, n])
    if w == e or s == n:
        raise ValidationError(f"{kind} has zero area: W==E or S==N", bbox=[w, s, e, n])
    if w > e:
        raise ValidationError(
            f"{kind} crosses the 180° meridian (W={w} > E={e}); "
            "please split into two sub-bboxes or shift longitudes",
            bbox=[w, s, e, n],
        )
    if s > n:
        raise ValidationError(f"{kind} has S > N (S={s} > N={n})", bbox=[w, s, e, n])
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"{kind} latitude out of range [-90, 90]: S={s}, N={n}",
            bbox=[w, s, e, n],
        )
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"{kind} longitude out of range [-180, 180]: W={w}, E={e}",
            bbox=[w, s, e, n],
        )
    return [w, s, e, n]


# ---------------------------------------------------------------------------
# 物候模板
# ---------------------------------------------------------------------------
def _gauss(t: np.ndarray, center: float, width: float) -> np.ndarray:
    return np.exp(-0.5 * ((t - center) / width) ** 2)


def class_templates(n_dates: int) -> Dict[int, np.ndarray]:
    """各类别的理想物候曲线（NDVI，取值 0-1）。"""
    t = np.arange(n_dates, dtype=float)
    templates = {
        1: 0.25 + 0.50 * _gauss(t, 3.5, 1.2) + 0.55 * _gauss(t, 8.5, 1.2),  # 双季稻 双峰
        2: 0.12 + 0.75 * _gauss(t, 8.0, 1.8),                                # 单季稻 强单峰
        3: 0.78 + 0.03 * np.sin(2 * np.pi * t / n_dates),                    # 常绿林 平坦
        4: 0.22 + 0.55 * _gauss(t, 5.5, 2.2),                                # 落叶林 单峰深谷
    }
    return {k: np.clip(v, 0.0, 1.0) for k, v in templates.items()}


# ---------------------------------------------------------------------------
# 核心算法：物候特征提取
# ---------------------------------------------------------------------------
def extract_features(series: np.ndarray) -> np.ndarray:
    """从 (n_dates, N) 的时间序列矩阵提取 (N, n_features) 特征矩阵。

    特征顺序见 FEATURE_NAMES：
    max, min, amplitude, mean, peak_time, growing_season_length, n_peaks。
    """
    series = np.asarray(series, dtype=np.float64)
    if series.ndim != 2:
        raise ValidationError("extract_features expects a 2D (n_dates, N) array")
    n_dates, n_pix = series.shape
    if n_dates < 3:
        raise ValidationError("need at least 3 dates for phenology features")

    vmax = series.max(axis=0)
    vmin = series.min(axis=0)
    amp = vmax - vmin
    mean = series.mean(axis=0)
    peak_time = series.argmax(axis=0).astype(np.float64)

    # 生长季长度：高于 (min + 0.5*amp) 的期数
    half_thresh = vmin + 0.5 * amp
    gsl = (series > half_thresh[None, :]).sum(axis=0).astype(np.float64)

    # 峰个数：内部点同时高于左右邻且高于 (min + 0.15*amp)
    base_thresh = vmin + 0.15 * amp
    mid = series[1:-1, :]
    higher_left = mid > series[:-2, :]
    higher_right = mid >= series[2:, :]
    above = mid > base_thresh[None, :]
    n_peaks = (higher_left & higher_right & above).sum(axis=0).astype(np.float64)

    feats = np.stack([vmax, vmin, amp, mean, peak_time, gsl, n_peaks], axis=1)
    return feats.astype(np.float64)


def make_training_set(
    n_dates: int,
    n_per_class: int = 300,
    noise_std: float = 0.03,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray]:
    """从物候模板 + 高斯噪声生成训练样本，返回 (X, y)。"""
    rng = np.random.default_rng(seed)
    templates = class_templates(n_dates)
    X_list: List[np.ndarray] = []
    y_list: List[int] = []
    for cls, curve in templates.items():
        noisy = curve[None, :] + rng.normal(0.0, noise_std, size=(n_per_class, n_dates))
        noisy = np.clip(noisy, 0.0, 1.0).T  # (n_dates, n_per_class)
        X_list.append(extract_features(noisy))
        y_list.extend([cls] * n_per_class)
    X = np.vstack(X_list)
    y = np.asarray(y_list, dtype=np.int64)
    return X, y


def train_and_classify(
    X_train: np.ndarray,
    y_train: np.ndarray,
    X_predict: np.ndarray,
    n_estimators: int = 150,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray]:
    """训练 RandomForest 并预测，返回 (labels, feature_importances)。"""
    from sklearn.ensemble import RandomForestClassifier

    if X_train.shape[1] != X_predict.shape[1]:
        raise ValidationError("feature dimension mismatch between train and predict")
    rf = RandomForestClassifier(
        n_estimators=n_estimators, random_state=seed, n_jobs=1)
    rf.fit(X_train, y_train)
    labels = rf.predict(X_predict)
    return labels.astype(np.int64), rf.feature_importances_.astype(np.float64)


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    n_dates: int = 12,
    width: int = 64,
    height: int = 64,
    noise_std: float = 0.03,
    seed: int = 42,
) -> Dict[str, Any]:
    """生成 (n_dates, H, W) 的 NDVI 时序，四象限对应四种类别 + 真值栅格。"""
    rng = np.random.default_rng(seed)
    templates = class_templates(n_dates)

    truth = np.zeros((height, width), dtype=np.int64)
    mid_r, mid_c = height // 2, width // 2
    truth[:mid_r, :mid_c] = 1
    truth[:mid_r, mid_c:] = 2
    truth[mid_r:, :mid_c] = 3
    truth[mid_r:, mid_c:] = 4

    cube = np.zeros((n_dates, height, width), dtype=np.float32)
    for cls, curve in templates.items():
        mask = truth == cls
        for t in range(n_dates):
            layer = np.full((height, width), curve[t])
            layer += rng.normal(0.0, noise_std, size=(height, width))
            cube[t][mask] = layer[mask]
    cube = np.clip(cube, 0.0, 1.0)

    return {
        "bbox": list(bbox),
        "width": width,
        "height": height,
        "n_dates": n_dates,
        "cube": cube,
        "truth": truth,
    }


# ---------------------------------------------------------------------------
# GeoTIFF I/O（直接用 rasterio，保证离线可用）
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


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float]]:
    """读 GeoTIFF；NoData 像素替换为 NaN 后返回 (cube, bbox)。

    元数据通过模块级 _LAST_READ_META 暴露：nodata / n_valid_pixels / n_total_pixels。
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [float(b.left), float(b.bottom), float(b.right), float(b.top)]
        nodata = src.nodata
    if nodata is not None:
        cube = np.where(cube == float(nodata), np.nan, cube)
    n_valid = int(np.count_nonzero(np.isfinite(cube)))
    n_total = int(cube.size)
    globals()["_LAST_READ_META"] = {
        "nodata": nodata, "n_valid_pixels": n_valid, "n_total_pixels": n_total,
    }
    return cube, bbox


def get_last_read_meta() -> Dict[str, Any]:
    return globals().get("_LAST_READ_META", {"nodata": None,
                                              "n_valid_pixels": 0,
                                              "n_total_pixels": 0})


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
            "n_dates": getattr(args, "n_dates", None),
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
    bbox = list(args.bbox) if args.bbox else None
    truth: Optional[np.ndarray] = None
    in_meta: Dict[str, Any] = {"nodata": None, "n_valid_pixels": 0, "n_total_pixels": 0}

    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        in_meta = get_last_read_meta()
        if bbox is not None:
            bbox = validate_bbox(bbox, kind="--bbox")
        else:
            bbox = validate_bbox(file_bbox, kind="--input file bbox")
        if cube.ndim != 3 or cube.shape[0] < 3:
            raise ValidationError(
                "input raster must be a multiband (n_dates >= 3) NDVI stack")
        if in_meta["n_valid_pixels"] == 0:
            raise ValidationError(
                f"input raster has no valid pixels (all NoData={in_meta['nodata']})",
                path=args.input, n_total_pixels=in_meta["n_total_pixels"],
            )
        n_dates = cube.shape[0]
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        bbox = validate_bbox(bbox, kind="--bbox")
        if args.n_dates < 3:
            raise ValidationError(
                f"--n-dates must be >= 3 (need at least 3 dates for phenology features), got {args.n_dates}",
                n_dates=args.n_dates)
        synth = generate_synthetic(bbox, n_dates=args.n_dates)
        cube = synth["cube"]
        truth = synth["truth"]
        n_dates = synth["n_dates"]
        source_note = "synthetic"

    if cube.size == 0:
        raise ValidationError("input data is empty")

    # 校验通过后再建目录（失败时不留空目录）
    os.makedirs(output_dir, exist_ok=True)

    h, w = cube.shape[1], cube.shape[2]

    # 训练集来自物候模板；预测目标为影像所有像元
    X_train, y_train = make_training_set(n_dates)
    series_2d = cube.reshape(n_dates, -1)
    X_predict = extract_features(series_2d)

    labels_flat, importances = train_and_classify(X_train, y_train, X_predict)
    classified = labels_flat.reshape(h, w)

    # 写出产物
    out_tif = os.path.join(output_dir, "classification.tif")
    write_geotiff(out_tif, classified.astype(np.float32), bbox)

    imp = {name: float(v) for name, v in zip(FEATURE_NAMES, importances)}
    imp_path = os.path.join(output_dir, "feature_importance.json")
    with open(imp_path, "w", encoding="utf-8") as f:
        json.dump(imp, f, ensure_ascii=False, indent=2)

    # 各类典型曲线（模板 + 影像中该类的平均观测曲线）
    templates = class_templates(n_dates)
    curves: Dict[str, Any] = {}
    for cls in sorted(CLASS_NAMES.keys()):
        entry = {"name": CLASS_NAMES[cls],
                 "template": [float(v) for v in templates[cls]]}
        if cls in np.unique(classified):
            mask = classified == cls
            sub = series_2d[:, mask.ravel()]
            entry["observed_mean"] = [float(v) for v in sub.mean(axis=1)]
            entry["n_pixels"] = int(mask.sum())
        curves[str(cls)] = entry
    curves_path = os.path.join(output_dir, "typical_curves.json")
    with open(curves_path, "w", encoding="utf-8") as f:
        json.dump(curves, f, ensure_ascii=False, indent=2)

    # 类别面积统计
    unique, counts = np.unique(classified, return_counts=True)
    class_areas = {CLASS_NAMES.get(int(u), str(u)): int(c)
                   for u, c in zip(unique, counts)}

    qa: Dict[str, Any] = {
        "source": source_note,
        "n_dates": int(n_dates),
        "n_pixels": int(classified.size),
        "class_pixel_counts": class_areas,
        "top_feature": max(imp, key=imp.get),
    }
    if truth is not None:
        acc = float(np.mean(classified == truth))
        qa["synthetic_accuracy"] = acc
    if args.input and not args.synthetic:
        qa["input_nodata"] = in_meta["nodata"]
        qa["input_n_valid_pixels"] = in_meta["n_valid_pixels"]
        qa["input_n_total_pixels"] = in_meta["n_total_pixels"]

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": imp_path, "kind": "json"},
        {"path": curves_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] dates: {n_dates}  shape: ({h}, {w})")
        print(f"[{SKILL_NAME}] top feature: {qa['top_feature']}")
        if truth is not None:
            print(f"[{SKILL_NAME}] synthetic accuracy: {qa['synthetic_accuracy']:.3f}")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Phenology feature extraction + RandomForest time-series classification.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="multiband NDVI time-series GeoTIFF (>= 3 bands)")
    p.add_argument("--n-dates", type=int, default=12, dest="n_dates",
                   help="number of time steps in synthetic mode (default: 12)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a synthetic phenology scene (offline)")
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
