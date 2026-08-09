#!/usr/bin/env python3
"""slum-mapping — 贫民窟/棚户区制图

用多指标综合指数制图贫民窟/棚户区。核心算法：

- **纹理不规则性**：局部标准差（高对比、无序）→ 棚户区建筑杂乱。
- **建筑密度**：极高密度（拥挤）→ 棚户区特征。
- **夜光**：低夜光（基础设施差）→ 棚户区。
- **人口密度**：高人口密度 → 棚户区。
- **贫民窟指数**：SI = w_tex×texture + w_den×density + w_pop×pop
                      − w_nl×nightlight，裁剪到 [0, 1]。
  各因子用绝对物理标度归一化，指数随纹理/密度/人口递增、随夜光递减。

数据源：本地多源栅格（灰度纹理 + 密度 + 夜光 + 人口），
或 ``--synthetic`` 离线模拟。

隐私声明 / Privacy：默认离线运行，``--synthetic`` 完全无网络。

Usage:
    python slum-mapping.py --input scene.tif --density den.tif --nightlight nl.tif
    python slum-mapping.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "slum-mapping"

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
# 校验前置
# ---------------------------------------------------------------------------
def validate_bbox(bbox, source: str = "bbox") -> None:
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
        if v != v:
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


def validate_threshold(threshold: float) -> None:
    """--threshold must be in [0, 1] (slum index is clipped to [0,1])."""
    try:
        v = float(threshold)
    except (TypeError, ValueError) as exc:
        raise ValidationError(f"--threshold must be a float (got {threshold!r})") from exc
    if v != v:  # NaN
        raise ValidationError(f"--threshold is NaN")
    if not (0.0 <= v <= 1.0):
        raise ValidationError(
            f"--threshold must be in [0, 1] (got {threshold!r}); "
            "the slum index is clipped to [0, 1]."
        )


def validate_kernel_size(kernel_size: int) -> None:
    """--kernel-size must be >= 2 (scipy uniform_filter with size<2 is degenerate)."""
    if int(kernel_size) < 2:
        raise ValidationError(
            f"--kernel-size must be >= 2 (got {kernel_size!r}); "
            "scipy.ndimage.uniform_filter with size<2 returns the input unchanged "
            "(no real neighborhood) and would make the texture map meaningless."
        )


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------

def local_std(gray: np.ndarray, size: int = 5) -> np.ndarray:
    """局部标准差（纹理不规则性）。

    NoData 语义：所有 NaN 像元及其邻域内的像元（被 NaN 污染的窗口）
    在输出中也置为 NaN；下游 ``slum_index`` 用 ``isfinite`` 掩膜把它们
    排除在统计之外，避免 -9999 哨兵被平方后污染 var。
    """
    from scipy.ndimage import uniform_filter
    g = np.asarray(gray, dtype=np.float32)
    # Mask finite pixels only; non-finite pixels (NaN / NoData) become 0 in mask
    finite = np.isfinite(g).astype(np.float32)
    g_safe = np.where(finite > 0, g, 0.0)
    # uniform_filter returns the MEAN of the window, not the sum
    # mean-of-finite = (count of finite in window) / (size*size)
    finite_frac = uniform_filter(finite, size=size, mode="nearest")
    cnt = finite_frac * float(size * size)  # actual count of finite pixels in window
    mean = uniform_filter(g_safe, size=size, mode="nearest") / np.clip(finite_frac, 1e-6, None)
    sq_mean = uniform_filter(g_safe * g_safe, size=size, mode="nearest") / np.clip(finite_frac, 1e-6, None)
    var = np.clip(sq_mean - mean * mean, 0.0, None)
    out = np.sqrt(var).astype(np.float32)
    # If a window contains ANY NoData, that pixel is considered contaminated
    window_full = (cnt >= float(size * size) - 1e-3)
    out = np.where(window_full, out, np.nan).astype(np.float32)
    return out


def slum_index(
    texture: np.ndarray,
    density: np.ndarray,
    nightlight: np.ndarray,
    pop_density: np.ndarray,
    w_tex: float = 0.3,
    w_den: float = 0.3,
    w_pop: float = 0.2,
    w_nl: float = 0.2,
    tex_scale: float = 0.3,
    pop_scale: float = 1000.0,
) -> np.ndarray:
    """贫民窟指数（绝对物理标度）：

    SI = w_tex×clip(tex/tex_scale) + w_den×clip(den) + w_pop×clip(pop/pop_scale)
         − w_nl×clip(nightlight)
    裁剪到 [0, 1]。随纹理/密度/人口递增，随夜光递减。

    NoData 语义：任一输入含 NaN 的像元在输出中也为 NaN（"数据缺失"而非
    "指数值 0"），由 ``process()`` 后续用 ``isfinite`` 掩膜写入 -1 哨兵。
    """
    tex = np.asarray(texture, dtype=np.float32)
    den = np.clip(np.asarray(density, dtype=np.float32), 0.0, 1.0)
    nl = np.clip(np.asarray(nightlight, dtype=np.float32), 0.0, 1.0)
    pop = np.clip(np.asarray(pop_density, dtype=np.float32), 0.0, None)

    tex_pos = np.clip(tex, 0.0, None)
    tex_norm = np.clip(tex_pos / max(tex_scale, 1e-6), 0.0, 1.0)
    pop_norm = np.clip(pop / max(pop_scale, 1e-6), 0.0, 1.0)

    si = w_tex * tex_norm + w_den * den + w_pop * pop_norm - w_nl * nl
    si = np.clip(si, 0.0, 1.0).astype(np.float32)
    # Propagate NaN: if any input is NaN, output is NaN
    any_nan = (~np.isfinite(tex)) | (~np.isfinite(den)) | (~np.isfinite(nl)) | (~np.isfinite(pop))
    si = np.where(any_nan, np.nan, si).astype(np.float32)
    return si


def classify_slum(slum_idx: np.ndarray, threshold: float = 0.5) -> np.ndarray:
    return (slum_idx >= threshold).astype(np.uint8)


# ---------------------------------------------------------------------------
# 合成数据：棚户区（高纹理/高密度/暗夜光/高人口）vs 正规区
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 128,
    height_px: int = 128,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成 gray(纹理源), density, nightlight, pop_density。

    左半区：棚户区（高噪声纹理、高密度、暗夜光、高人口）。
    右半区：正规规划区（平滑纹理、中密度、亮夜光、中人口）。
    """
    rng = np.random.default_rng(seed)
    gray = np.zeros((height_px, width), dtype=np.float32)
    density = np.zeros((height_px, width), dtype=np.float32)
    nightlight = np.zeros((height_px, width), dtype=np.float32)
    pop = np.zeros((height_px, width), dtype=np.float32)

    mid = width // 2
    # 棚户区（左）
    gray[:, :mid] = rng.uniform(0.1, 0.6, (height_px, mid)).astype(np.float32)
    density[:, :mid] = rng.uniform(0.7, 0.95, (height_px, mid)).astype(np.float32)
    nightlight[:, :mid] = rng.uniform(0.05, 0.2, (height_px, mid)).astype(np.float32)
    pop[:, :mid] = rng.uniform(800, 1200, (height_px, mid)).astype(np.float32)

    # 正规区（右）
    gray[:, mid:] = 0.3 + rng.normal(0, 0.02, (height_px, width - mid)).astype(np.float32)
    density[:, mid:] = rng.uniform(0.3, 0.5, (height_px, width - mid)).astype(np.float32)
    nightlight[:, mid:] = rng.uniform(0.7, 0.95, (height_px, width - mid)).astype(np.float32)
    pop[:, mid:] = rng.uniform(300, 500, (height_px, width - mid)).astype(np.float32)

    gray = np.clip(gray, 0.0, 1.0)

    info = {
        "bbox": bbox, "width": width, "height": height_px,
    }
    return gray, density, nightlight, pop, info


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


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float]]:
    """读取栅格，返回 (cube, bbox)。

    NoData 哨兵值（src.nodata）会被替换为 NaN 以避免污染下游 local_std
    （-9999 会被平方成 1e8 数量级，污染纹理 var 与最终贫民窟指数）。
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nd = src.nodata
        if nd is not None:
            cube = np.where(cube == float(nd), np.nan, cube).astype(np.float32)
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
    bbox = list(args.bbox) if args.bbox else None

    # ===== 0) Validate CLI up-front (no side effects, no mkdir) =====
    if not (args.input or args.synthetic or bbox):
        raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
    if bbox is not None:
        validate_bbox(bbox, source="--bbox")
    validate_threshold(args.threshold)
    validate_kernel_size(args.kernel_size)

    # mkdir AFTER validation (CONVENTIONS §1.1 / common bug pattern #6)
    os.makedirs(output_dir, exist_ok=True)

    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        if args.bbox is not None:
            validate_bbox(bbox, source="--bbox")
        if not np.isfinite(cube).any():
            raise ValidationError(
                f"input raster '{args.input}' contains only NoData / NaN pixels; nothing to map"
            )
        gray = cube[0]
        density = np.clip((cube[1] if cube.shape[0] > 1 else gray), 0.0, 1.0)
        if args.nightlight:
            nl_cube, _ = read_geotiff(args.nightlight)
            nightlight = nl_cube[0]
        else:
            nightlight = np.full_like(gray, 0.5)
        if args.population:
            pop_cube, _ = read_geotiff(args.population)
            pop = pop_cube[0]
        else:
            pop = np.full_like(gray, 500.0)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        gray, density, nightlight, pop, synth_info = generate_synthetic(bbox)
        source_note = "synthetic"

    if gray.size == 0:
        raise ValidationError("input raster is empty")

    # 2) 纹理 → 贫民窟指数 → 分类
    texture = local_std(gray, size=args.kernel_size)
    si = slum_index(texture, density, nightlight, pop)
    # 3) 写出：NaN 像素写 -1 哨兵
    finite = np.isfinite(si)
    si_for_write = np.where(finite, si, -1.0).astype(np.float32)
    # classify: NaN → 0 (not slum)
    si_for_classify = np.where(finite, si, 0.0)
    mask = classify_slum(si_for_classify, threshold=args.threshold)
    mask_for_write = mask.astype(np.float32)
    mask_for_write[~finite] = -1.0  # mask NoData with -1 sentinel
    out_tif = os.path.join(output_dir, "slum_index.tif")
    stack = np.stack([si_for_write, mask_for_write], axis=0)
    write_geotiff(out_tif, stack, bbox, nodata=-1.0)

    n_valid = int(finite.sum())
    n_total = int(finite.size)
    # Statistics only over valid pixels
    if n_valid > 0:
        mean_si = float(np.nanmean(si))
        slum_frac = float((si[finite] >= args.threshold).mean())
        mean_tex = float(np.nanmean(texture))
    else:
        mean_si, slum_frac, mean_tex = 0.0, 0.0, 0.0

    stats = {
        "mean_slum_index": mean_si,
        "slum_fraction": slum_frac,
        "mean_texture": mean_tex,
        "threshold": args.threshold,
        "n_valid_pixels": n_valid,
        "n_total_pixels": n_total,
    }
    stats_path = os.path.join(output_dir, "slum_stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {"source": source_note}
    qa.update(stats)

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 2},
        {"path": stats_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] mean slum index: {stats['mean_slum_index']:.3f}")
        print(f"[{SKILL_NAME}] slum fraction: {stats['slum_fraction']:.4f}")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Slum mapping via multi-indicator index (texture, density, nightlight, population).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input GeoTIFF (band1=gray texture source)")
    p.add_argument("--nightlight", help="nightlight GeoTIFF")
    p.add_argument("--population", help="population density GeoTIFF")
    p.add_argument("--threshold", type=float, default=0.5,
                   help="slum classification threshold (default: 0.5)")
    p.add_argument("--kernel-size", type=int, default=5,
                   help="texture kernel size (default: 5)")
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
