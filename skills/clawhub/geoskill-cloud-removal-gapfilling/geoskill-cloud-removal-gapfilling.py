#!/usr/bin/env python3
"""cloud-removal-gapfilling — 去云与间隙填充

利用多时相影像合成去除云/云影与数据间隙，生成无云合成影像。核心思想：
云在时间维度上是瞬态的，而地表反射相对稳定，因此对同一像元在多个时相上
取稳健统计量（中值 / 百分位）即可剔除被云污染的高值观测，得到干净的合成。

实现了两种合成方法：

- **median**（中值合成）：逐像元取所有有效时相的中值，对离群（云）最稳健。
- **percentile**（百分位合成）：逐像元取指定百分位（默认 50，等价中值；
  可选低百分位以偏向暗目标，或高百分位以偏向亮目标）。

云/间隙在输入立方体中以 ``nan`` 编码（真实模式下 nodata 会被转为 nan）。
合成会自动忽略 nan，并统计逐时相云覆盖率与时序完全失效率（残隙）。

数据源：本地多时相 GeoTIFF（各波段视为同一谱段的时序观测，nodata 为云/间隙），
或使用 ``--synthetic`` 生成含随机云块的物理一致模拟时序用于离线测试。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python cloud-removal-gapfilling.py --input stack.tif --method median
    python cloud-removal-gapfilling.py --bbox 116 39 117 40 --synthetic --output-dir ./out

License: MIT
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import sys
import warnings
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

VERSION = "1.0.0"
SKILL_NAME = "cloud-removal-gapfilling"

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
def composite_scenes(
    scenes: np.ndarray,
    method: str = "median",
    percentile: float = 50.0,
) -> np.ndarray:
    """对 (n_scenes, bands, H, W) 的时序立方体做逐像元稳健合成。

    nan 被视为云/间隙并在统计中忽略。返回 (bands, H, W) 的合成影像。
    对于在所有时相上均无效（全 nan）的像元，结果保持 nan（残隙）。
    """
    if scenes.ndim != 4:
        raise ValidationError(
            f"scenes must be 4-D (n_scenes, bands, H, W), got ndim={scenes.ndim}",
            ndim=int(scenes.ndim),
        )
    if scenes.shape[0] < 1:
        raise ValidationError("need at least one scene to composite")
    if method not in ("median", "percentile"):
        raise UsageError(
            f"unknown method '{method}'. Choose from: median, percentile",
            method=method,
        )

    arr = scenes.astype(np.float32)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        if method == "median":
            comp = np.nanmedian(arr, axis=0)
        else:
            comp = np.nanpercentile(arr, percentile, axis=0)
    return comp.astype(np.float32)


def cloud_coverage_stats(scenes: np.ndarray) -> Dict[str, Any]:
    """统计逐时相云覆盖率与时序完全失效率。

    - per_scene_cloud_fraction[t]：第 t 期任一波段为 nan 的像元比例。
    - full_gap_fraction：所有时相都为 nan（无任何有效观测）的像元比例，
      即合成后仍无法填充的残隙。
    """
    n_scenes, nb, h, w = scenes.shape
    invalid = ~np.isfinite(scenes)
    # 单期：任一波段无效即视为该像元被云污染
    per_scene = [
        float(np.mean(invalid[t].any(axis=0))) for t in range(n_scenes)
    ]
    full_gap = float(np.mean(invalid.all(axis=0)))
    mean_cloud = float(np.mean(per_scene)) if per_scene else 0.0
    return {
        "n_scenes": int(n_scenes),
        "n_bands": int(nb),
        "per_scene_cloud_fraction": per_scene,
        "mean_cloud_fraction": mean_cloud,
        "full_gap_fraction": full_gap,
    }


# ---------------------------------------------------------------------------
# 合成数据：物理一致的模拟时序（离线测试）
# ---------------------------------------------------------------------------
def _cloud_mask(
    rng: np.random.Generator,
    height: int,
    width: int,
    target_fraction: float,
) -> np.ndarray:
    """生成团块状随机云掩膜（布尔型），覆盖率约等于 target_fraction。

    用低分辨率随机场双线性上采样得到平滑云块，再按分位数阈值截断到目标覆盖率。
    """
    from scipy.ndimage import zoom

    ch, cw = max(height // 8, 2), max(width // 8, 2)
    coarse = rng.random((ch, cw)).astype(np.float32)
    field = zoom(coarse, (height / ch, width / cw), order=1)
    field = field[:height, :width]
    thr = float(np.quantile(field, 1.0 - np.clip(target_fraction, 0.0, 1.0)))
    return field >= thr


def generate_synthetic_scenes(
    bbox: List[float],
    n_scenes: int = 5,
    bands: int = 4,
    width: int = 128,
    height: int = 128,
    cloud_fraction: float = 0.25,
    seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成 (n_scenes, bands, H, W) 的含云时序立方体。

    地表真值由平滑梯度 + 纹理构成（反射率量级 [0,1]），各时相共享同一地表，
    叠加小幅观测噪声，并在随机位置加入团块状云（设为 nan）。由于云在时间上
    随机分布，多时相合成后绝大多数像元都能被有效观测覆盖。
    """
    rng = np.random.default_rng(seed)

    yy, xx = np.mgrid[0:height, 0:width]
    yn = yy.astype(np.float32) / max(height - 1, 1)
    xn = xx.astype(np.float32) / max(width - 1, 1)

    truth = np.zeros((bands, height, width), dtype=np.float32)
    for b in range(bands):
        base = 0.15 + 0.35 * xn + 0.25 * yn + 0.08 * b / max(bands - 1, 1)
        base = base + rng.normal(0, 0.01, size=base.shape).astype(np.float32)
        truth[b] = np.clip(base, 0.0, 1.0)

    scenes = np.repeat(truth[np.newaxis, ...], n_scenes, axis=0).copy()
    masks: List[np.ndarray] = []
    for t in range(n_scenes):
        scenes[t] = scenes[t] + rng.normal(0, 0.008, size=scenes[t].shape).astype(np.float32)
        mask = _cloud_mask(rng, height, width, cloud_fraction)
        masks.append(mask)
        scenes[t][:, mask] = np.nan

    info = {
        "bbox": bbox,
        "width": width,
        "height": height,
        "bands": bands,
        "n_scenes": n_scenes,
        "target_cloud_fraction": cloud_fraction,
        "truth_mean_per_band": [float(np.mean(truth[b])) for b in range(bands)],
    }
    return scenes, info


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
    out = np.where(np.isfinite(cube), cube, nodata).astype(np.float32)
    profile = {
        "driver": "GTiff", "height": h, "width": w, "count": nb,
        "dtype": "float32", "crs": "EPSG:4326", "transform": transform,
        "nodata": nodata, "compress": "deflate",
    }
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(out[b], b + 1)


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float]]:
    """Read a multi-band GeoTIFF, returning (cube, bbox) with NoData→NaN.

    Uses ``rasterio.read(masked=True)`` so that any value matching
    ``src.nodata`` is converted to NaN.  If ``src.nodata`` is None we still
    rely on the masked array default; downstream code treats NaN as
    "cloud/gap" and ignores it.
    """
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
            "method": getattr(args, "method", None),
            "n_scenes": getattr(args, "n_scenes", None),
            "percentile": getattr(args, "percentile", None),
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

    # 1) 获取时序立方体 (n_scenes, bands, H, W)
    #    通用契约：给了 --input 就读真实栅格（各波段视为时序观测，nodata→nan）；
    #    否则（含显式 --synthetic）走合成模式。
    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        # 真实栅格 (K, H, W)：视为 K 期、单谱段时序
        scenes = cube[:, np.newaxis, :, :]
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        scenes, synth_info = generate_synthetic_scenes(
            bbox, n_scenes=args.n_scenes, cloud_fraction=args.cloud_fraction,
        )
        source_note = "synthetic"

    # 2) 校验（先于 makedirs，避免错误路径产生空目录）
    if scenes.size == 0:
        raise ValidationError("input data is empty")
    if bbox is not None:
        validate_bbox(bbox)
    # 全 NaN 立方体 = 无任何有效观测；合成必然全空
    if not np.any(np.isfinite(scenes)):
        raise ValidationError(
            "input scenes have no valid (finite) pixels across all time steps "
            "and bands (all NoData or NaN); cannot produce a cloud-free composite",
        )

    # 现在 makedirs（所有校验已通过）
    os.makedirs(output_dir, exist_ok=True)

    # 2) 多时相合成去云
    comp = composite_scenes(scenes, method=args.method, percentile=args.percentile)
    stats = cloud_coverage_stats(scenes)

    residual_nan = int(np.sum(~np.isfinite(comp)))
    finite_vals = comp[np.isfinite(comp)]

    # 3) 写出产物
    out_tif = os.path.join(output_dir, "cloud_free_composite.tif")
    write_geotiff(out_tif, comp, bbox)

    stats_out = dict(stats)
    stats_out.update({
        "method": args.method,
        "percentile": args.percentile,
        "residual_gap_pixels": residual_nan,
        "composite_valid_fraction": float(np.mean(np.isfinite(comp))),
    })
    stats_path = os.path.join(output_dir, "cloud_stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats_out, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "method": args.method,
        "n_scenes": int(scenes.shape[0]),
        "n_bands_out": int(comp.shape[0]),
        "mean_cloud_fraction": stats["mean_cloud_fraction"],
        "full_gap_fraction": stats["full_gap_fraction"],
        "composite_valid_fraction": float(np.mean(np.isfinite(comp))),
    }
    if finite_vals.size:
        qa["composite_mean_value"] = float(np.mean(finite_vals))
    if synth_info is not None:
        qa["synthetic_truth_mean_per_band"] = synth_info["truth_mean_per_band"]

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": int(comp.shape[0])},
        {"path": stats_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] method: {args.method}  scenes: {scenes.shape[0]}")
        print(f"[{SKILL_NAME}] mean cloud fraction: {stats['mean_cloud_fraction']:.3f}")
        print(f"[{SKILL_NAME}] residual gap fraction: {stats['full_gap_fraction']:.4f}")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        print(f"[{SKILL_NAME}] stats:  {stats_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Multi-temporal cloud removal & gap filling (median / percentile composite).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input multi-temporal GeoTIFF (bands=time, nodata=cloud)")
    p.add_argument("--method", default="median", choices=["median", "percentile"],
                   help="composite method (default: median)")
    p.add_argument("--n-scenes", type=int, default=5,
                   help="number of synthetic scenes to generate (default: 5)")
    p.add_argument("--percentile", type=float, default=50.0,
                   help="percentile value for method=percentile (default: 50)")
    p.add_argument("--cloud-fraction", type=float, default=0.25,
                   help="target per-scene cloud fraction for synthetic mode (default: 0.25)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a physics-consistent synthetic time series (offline)")
    p.add_argument("--output-dir", default="./output", help="output directory")
    p.add_argument("--quiet", action="store_true", help="suppress console output")
    p.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    return p


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.n_scenes < 1:
        print(f"[{SKILL_NAME}] ERROR [EUsage] --n-scenes must be >= 1", file=sys.stderr)
        return 2
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
