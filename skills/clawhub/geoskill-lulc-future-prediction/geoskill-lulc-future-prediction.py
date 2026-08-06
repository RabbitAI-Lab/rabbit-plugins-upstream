#!/usr/bin/env python3
"""lulc-future-prediction — 土地覆被预测（CA-Markov）

用两期土地覆盖（LULC）分类预测目标年的覆被格局，方法为**简化的
CA-Markov 模型**：

1. **马尔可夫转移概率**：由两期 LULC 构建转移矩阵，按行归一化得到转移
   概率矩阵 P（P[i,j] = 类别 i 在一个时间步内转为类别 j 的概率）。
2. **面积预测**：当前各类面积向量右乘 P^n（n = 时间步数），得到目标年
   各类的期望像元数。
3. **元胞自动机分配（CA）**：把需要转变的像元优先分配到邻域中已存在
   目标类别的位置（邻域适宜性），模拟城市沿边缘向外扩张的空间过程。

不确定性用逐像元「转出概率」(1 - P[i,i]) 表示，越高表示该像元所处类别
越不稳定。

数据源：本地 2 波段栅格（band1 = t1 分类, band2 = t2 分类，``--input``）；
``--synthetic`` 生成含城市扩张的两期场景（离线）。

隐私声明 / Privacy：
- 默认离线运行，完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python lulc-future-prediction.py --bbox 116 39 117 40 --target-year 2030 --output-dir ./out
    python lulc-future-prediction.py --input lulc_two_epochs.tif --target-year 2030 --output-dir ./out

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
SKILL_NAME = "lulc-future-prediction"

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
    1: "cropland",
    2: "forest",
    3: "water",
    4: "urban",
}
# 合成场景假设：t1=2010, t2=2020，时间步长 10 年
EPOCH_YEARS = (2010, 2020)
STEP_YEARS = 10


def validate_bbox(bbox) -> None:
    """校验 bbox 是 W<E、S<N、lon∈[-180,180]、lat∈[-90,90]、非零面积。
    跨 180° 经线必须拆成两个子 bbox。"""
    if bbox is None:
        raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
    w, s, e, n = [float(v) for v in bbox]
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"bbox longitude out of range [-180, 180]: W={w}, E={e}",
            bbox=list(bbox),
        )
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"bbox latitude out of range [-90, 90]: S={s}, N={n}",
            bbox=list(bbox),
        )
    if w >= e:
        if w == e:
            raise ValidationError(
                f"bbox has zero width: W==E=={w} (degenerate AOI)",
                bbox=list(bbox),
            )
        raise ValidationError(
            f"bbox is reversed (W={w} >= E={e}); need W < E. "
            f"For datelines that cross 180° (e.g. 179.5 -> -179.5), "
            f"split into two sub-bboxes and run the skill on each separately.",
            bbox=list(bbox),
        )
    if s >= n:
        raise ValidationError(
            f"bbox is reversed (S={s} >= N={n}); need S < N",
            bbox=list(bbox),
        )


def validate_target_year(target_year: int, t2_year: int) -> None:
    """校验 --target-year 在时间步起点之后。"""
    if not isinstance(target_year, int):
        try:
            target_year = int(target_year)
        except Exception:
            raise UsageError(f"--target-year must be an integer, got {target_year!r}")
    if target_year < 1900 or target_year > 2200:
        raise ValidationError(
            f"--target-year {target_year} outside plausible range [1900, 2200]",
            target_year=target_year,
        )
    if target_year <= t2_year:
        raise ValidationError(
            f"--target-year {target_year} must be after t2={t2_year} (this skill "
            f"performs forward projection; t1={EPOCH_YEARS[0]}, t2={EPOCH_YEARS[1]}, "
            f"step={STEP_YEARS} years). Set --target-year to a year after {t2_year}.",
            target_year=target_year, t2_year=t2_year,
        )


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def transition_matrix(lulc1: np.ndarray, lulc2: np.ndarray, n_classes: int) -> np.ndarray:
    """两期 LULC 的转移矩阵（像元计数），类别编码 1..n_classes。

    内部按 0-based 索引存储：行=期初类别-1，列=期末类别-1。
    """
    if lulc1.shape != lulc2.shape:
        raise ValidationError("lulc1 and lulc2 must have the same shape")
    a = np.asarray(lulc1).astype(np.int64).ravel() - 1
    b = np.asarray(lulc2).astype(np.int64).ravel() - 1
    if a.min() < 0 or b.min() < 0 or a.max() >= n_classes or b.max() >= n_classes:
        raise ValidationError(
            f"class codes must be within 1..{n_classes}")
    idx = a * n_classes + b
    return np.bincount(idx, minlength=n_classes * n_classes).reshape(n_classes, n_classes)


def markov_probabilities(cm: np.ndarray) -> np.ndarray:
    """转移矩阵按行归一化为转移概率矩阵；空行设为自身保持（对角=1）。"""
    cm = np.asarray(cm, dtype=np.float64)
    row_sum = cm.sum(axis=1, keepdims=True)
    with np.errstate(divide="ignore", invalid="ignore"):
        p = np.where(row_sum > 0, cm / row_sum, 0.0)
    empty = (row_sum[:, 0] == 0)
    if empty.any():
        p[empty] = 0.0
        idx = np.where(empty)[0]
        p[idx, idx] = 1.0
    return p


def project_areas(areas: np.ndarray, p: np.ndarray, n_steps: int) -> np.ndarray:
    """用 P^n 投影各类面积向量到 n_steps 个时间步之后。"""
    if n_steps < 0:
        raise ValidationError("n_steps must be >= 0")
    pk = np.linalg.matrix_power(p, int(n_steps))
    return np.asarray(areas, dtype=np.float64) @ pk


def neighborhood_fraction(lulc: np.ndarray, cls_code: int) -> np.ndarray:
    """每个像元的 8 邻域中属于 cls_code 的比例（0-1）。"""
    from scipy.ndimage import convolve
    kernel = np.ones((3, 3), dtype=np.float64)
    kernel[1, 1] = 0.0
    mask = (np.asarray(lulc) == cls_code).astype(np.float64)
    count = convolve(mask, kernel, mode="constant", cval=0.0)
    return count / 8.0


def ca_markov_predict(
    lulc1: np.ndarray,
    lulc2: np.ndarray,
    n_classes: int,
    n_steps: int = 1,
    seed: int = 42,
) -> Dict[str, Any]:
    """完整 CA-Markov 预测，返回预测栅格 + 不确定性 + 诊断。"""
    rng = np.random.default_rng(seed)
    cm = transition_matrix(lulc1, lulc2, n_classes)
    p = markov_probabilities(cm)

    current = np.bincount(np.asarray(lulc2).ravel() - 1,
                          minlength=n_classes).astype(np.float64)
    target = project_areas(current, p, n_steps)

    # 预先计算各类的邻域适宜性（基于当前 t2 状态）
    neigh = [neighborhood_fraction(lulc2, c + 1) for c in range(n_classes)]

    result = np.asarray(lulc2).astype(np.int64).copy()
    conversions = 0
    for i in range(n_classes):
        delta = target[i] - current[i]
        if delta >= -1e-9:
            continue  # 该类不减少，无需转出
        to_leave = int(round(-delta))
        mask_i = result == (i + 1)
        if to_leave <= 0 or not mask_i.any():
            continue

        # 逐像元对每个目标类 j 打分：p[i,j] * (邻域适宜性 + 微扰)
        score = np.zeros(result.shape, dtype=np.float64)
        best_j = np.full(result.shape, -1, dtype=np.int64)
        for j in range(n_classes):
            if j == i or p[i, j] <= 0:
                continue
            s = p[i, j] * (neigh[j] + rng.uniform(0.0, 0.02, size=result.shape))
            better = (s > score) & mask_i
            score[better] = s[better]
            best_j[better] = j

        ys, xs = np.where(mask_i)
        prop = score[ys, xs]
        order = np.argsort(-prop)
        take = order[:to_leave]
        for k in take:
            y, x = ys[k], xs[k]
            j = best_j[y, x]
            if j >= 0:
                result[y, x] = j + 1
                conversions += 1

    # 不确定性：逐像元转出概率 1 - P[class,class]
    stay = np.array([p[c, c] for c in range(n_classes)])
    leave_prob = 1.0 - stay
    uncertainty = leave_prob[np.clip(result - 1, 0, n_classes - 1)]

    predicted_counts = np.bincount(result.ravel() - 1, minlength=n_classes)

    return {
        "predicted": result.astype(np.int32),
        "uncertainty": uncertainty.astype(np.float32),
        "probabilities": p,
        "transition_matrix": cm.tolist(),
        "current_areas": current.tolist(),
        "target_areas": target.tolist(),
        "predicted_counts": predicted_counts.tolist(),
        "n_steps": int(n_steps),
        "conversions": int(conversions),
    }


# ---------------------------------------------------------------------------
# 合成数据：两期 LULC，含城市扩张
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 64,
    height: int = 64,
    seed: int = 42,
) -> Dict[str, Any]:
    """生成两期 LULC：t1 城市较小，t2 城市向周边耕地扩张。"""
    rng = np.random.default_rng(seed)
    mid_r, mid_c = height // 2, width // 2

    lulc1 = np.full((height, width), 1, dtype=np.int64)  # 耕地基底
    lulc1[:mid_r // 2, :mid_c // 2] = 2                  # 森林块
    lulc1[height - mid_r // 2:, width - mid_c // 2:] = 3  # 水体块

    lulc2 = lulc1.copy()
    # t1 城市核心（中心 8x8）
    c0 = (mid_c - 4, mid_c + 4)
    r0 = (mid_r - 4, mid_r + 4)
    lulc1[r0[0]:r0[1], c0[0]:c0[1]] = 4
    # t2 城市扩张（中心 16x16，吞并周边耕地）
    c1 = (mid_c - 8, mid_c + 8)
    r1 = (mid_r - 8, mid_r + 8)
    lulc2[r1[0]:r1[1], c1[0]:c1[1]] = 4
    # 保留森林/水体不被城市覆盖
    lulc2[:mid_r // 2, :mid_c // 2] = 2
    lulc2[height - mid_r // 2:, width - mid_c // 2:] = 3

    return {
        "bbox": list(bbox),
        "width": width,
        "height": height,
        "lulc1": lulc1.astype(np.int32),
        "lulc2": lulc2.astype(np.int32),
        "epoch_years": list(EPOCH_YEARS),
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
            "target_year": getattr(args, "target_year", None),
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
    n_classes = max(CLASS_NAMES.keys())

    t1, t2 = EPOCH_YEARS
    validate_target_year(args.target_year, t2)

    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        validate_bbox(bbox)
        if cube.ndim != 3 or cube.shape[0] < 2:
            raise ValidationError(
                "input raster must have 2 bands: band1=LULC t1, band2=LULC t2")
        lulc1 = np.rint(cube[0]).astype(np.int64)
        lulc2 = np.rint(cube[1]).astype(np.int64)
        source_note = args.input
    else:
        validate_bbox(bbox)
        synth = generate_synthetic(bbox)
        lulc1, lulc2 = synth["lulc1"], synth["lulc2"]
        source_note = "synthetic"

    if lulc1.size == 0:
        raise ValidationError("input data is empty")

    n_steps = max(1, int(round((args.target_year - t2) / STEP_YEARS)))

    # 校验通过后再建输出目录
    os.makedirs(output_dir, exist_ok=True)

    res = ca_markov_predict(lulc1, lulc2, n_classes, n_steps=n_steps)

    out_pred = os.path.join(output_dir, "predicted_lulc.tif")
    out_unc = os.path.join(output_dir, "uncertainty.tif")
    write_geotiff(out_pred, res["predicted"].astype(np.float32), bbox)
    write_geotiff(out_unc, res["uncertainty"], bbox)

    names = {str(k): v for k, v in CLASS_NAMES.items()}
    report = {
        "skill": SKILL_NAME,
        "method": "CA-Markov (transition probability + neighborhood suitability)",
        "epoch_years": [t1, t2],
        "target_year": args.target_year,
        "n_steps": res["n_steps"],
        "class_names": names,
        "transition_matrix": res["transition_matrix"],
        "transition_probabilities": res["probabilities"].tolist(),
        "current_areas": {names[str(c + 1)]: int(v)
                          for c, v in enumerate(res["current_areas"])},
        "target_areas_projected": {names[str(c + 1)]: float(v)
                                   for c, v in enumerate(res["target_areas"])},
        "predicted_counts": {names[str(c + 1)]: int(v)
                             for c, v in enumerate(res["predicted_counts"])},
        "conversions": res["conversions"],
    }
    report_path = os.path.join(output_dir, "transition_probabilities.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2, default=str)

    urban_code = 4
    urban_t2 = int(res["current_areas"][urban_code - 1])
    urban_pred = int(res["predicted_counts"][urban_code - 1])
    qa: Dict[str, Any] = {
        "source": source_note,
        "n_steps": res["n_steps"],
        "conversions": res["conversions"],
        "urban_t2": urban_t2,
        "urban_predicted": urban_pred,
        "mean_uncertainty": float(np.mean(res["uncertainty"])),
    }

    outputs = [
        {"path": out_pred, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": out_unc, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": report_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] target year: {args.target_year}  steps: {res['n_steps']}")
        print(f"[{SKILL_NAME}] urban: t2={urban_t2} -> predicted={urban_pred}")
        print(f"[{SKILL_NAME}] conversions: {res['conversions']}")
        print(f"[{SKILL_NAME}] output: {out_pred}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="LULC future prediction via simplified CA-Markov.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="2-band GeoTIFF: band1=LULC t1, band2=LULC t2")
    p.add_argument("--target-year", type=int, default=2030, dest="target_year",
                   help="prediction target year (default: 2030)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a synthetic urban-expansion scene (offline)")
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
