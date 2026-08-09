#!/usr/bin/env python3
"""post-disaster-reconstruction — 灾后重建遥感监测

用多期高分辨率影像的建筑强度代理监测重建进度。对比三个时期：

- **灾前 (before)**、**损毁期 (damage)**、**重建期 (rebuild)** 的建筑强度（[0,1]）

逐像元重建进度分类：

    unchanged          灾前=建筑 且 损毁期仍完好
    destroyed          灾前=建筑、损毁期消失、重建期仍未恢复
    under_construction 损毁后重建期部分恢复（未达灾前）
    rebuilt            损毁后重建期已恢复到灾前水平
    non_building       灾前即无建筑

恢复进度（对毁坏像元）= clip((R - D)/(B - D), 0,1)，随重建期强度单调增。

数据源：本地多波段 GeoTIFF（band1=灾前、band2=损毁期、band3=重建期建筑强度），
或 ``--synthetic`` 生成三期场景（含可调恢复程度）。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python post-disaster-reconstruction.py --input series.tif
    python post-disaster-reconstruction.py --bbox 116 39 117 40 --recovery 0.7 --synthetic --output-dir ./out

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
SKILL_NAME = "post-disaster-reconstruction"

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


def validate_thresholds(thr_build: float, thr_damage: float) -> None:
    """Validate classify_progress thresholds."""
    if not (0.0 <= thr_damage < thr_build <= 1.0):
        raise ValidationError(
            f"--thr-damage ({thr_damage}) and --thr-build ({thr_build}) must satisfy "
            f"0 <= thr_damage < thr_build <= 1; otherwise categories are ill-defined"
        )


CATEGORY_LABELS = ["non_building", "unchanged", "destroyed", "under_construction", "rebuilt"]


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def classify_progress(before: np.ndarray, damage: np.ndarray, rebuild: np.ndarray,
                      thr_build: float = 0.5, thr_damage: float = 0.3) -> np.ndarray:
    """三期建筑强度 → 重建进度分类（整型 0–4，见 CATEGORY_LABELS）。

    0=non_building, 1=unchanged, 2=destroyed, 3=under_construction, 4=rebuilt。
    各类互斥；判定基于灾前是否有建筑及损毁/重建期强度阈值。
    """
    if not (before.shape == damage.shape == rebuild.shape):
        raise ValidationError("before/damage/rebuild shape mismatch")
    if not (0 <= thr_damage < thr_build <= 1):
        raise ValidationError("require 0 <= thr_damage < thr_build <= 1")
    B = np.clip(np.asarray(before, dtype=np.float64), 0, 1)
    D = np.clip(np.asarray(damage, dtype=np.float64), 0, 1)
    R = np.clip(np.asarray(rebuild, dtype=np.float64), 0, 1)
    cat = np.zeros(B.shape, dtype=np.int16)
    had_building = B > thr_build
    unchanged = had_building & (D >= thr_build)
    destroyed = had_building & (D < thr_damage) & (R < thr_damage)
    under_construction = had_building & (D < thr_damage) & (R >= thr_damage) & (R < thr_build)
    rebuilt = had_building & (D < thr_damage) & (R >= thr_build)
    cat[unchanged] = 1
    cat[destroyed] = 2
    cat[under_construction] = 3
    cat[rebuilt] = 4
    return cat


def reconstruction_progress(before: np.ndarray, damage: np.ndarray, rebuild: np.ndarray) -> np.ndarray:
    """毁坏像元的恢复进度 = clip((R-D)/(B-D), 0,1)；B≈D（未毁坏）处为 0。

    对固定 B、D，随重建期强度 R 单调不减；R=D → 0，R=B → 1。
    """
    if not (before.shape == damage.shape == rebuild.shape):
        raise ValidationError("before/damage/rebuild shape mismatch")
    B = np.clip(np.asarray(before, dtype=np.float64), 0, 1)
    D = np.clip(np.asarray(damage, dtype=np.float64), 0, 1)
    R = np.clip(np.asarray(rebuild, dtype=np.float64), 0, 1)
    denom = B - D
    prog = np.zeros_like(B, dtype=np.float64)
    np.divide(R - D, denom, out=prog, where=denom > 1e-6)
    return np.clip(prog, 0.0, 1.0).astype(np.float32)


def category_fractions(cat: np.ndarray) -> Dict[str, float]:
    """各类别面积占比。"""
    total = cat.size
    return {CATEGORY_LABELS[i]: float(np.count_nonzero(cat == i) / total) for i in range(len(CATEGORY_LABELS))}


# ---------------------------------------------------------------------------
# 合成数据：灾前建筑区 → 中心毁坏 → 重建期按 recovery 恢复
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], recovery: float = 0.7, width: int = 64, height: int = 64,
                       seed: int = 42) -> Tuple[Dict[str, np.ndarray], Dict[str, Any]]:
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    xn = xx.astype(np.float64) / max(width - 1, 1)
    yn = yy.astype(np.float64) / max(height - 1, 1)
    recovery = float(np.clip(recovery, 0.0, 1.0))
    # 灾前：城市建筑斑块（高强度），背景低
    built = np.exp(-(((xn - 0.5) ** 2 + (yn - 0.5) ** 2)) / (2 * 0.28 ** 2))
    before = np.clip(0.15 + 0.8 * built + rng.normal(0, 0.03, built.shape), 0, 1)
    # 损毁期：震中(0.5,0.5)附近建筑大量毁坏
    damage_field = 0.6 * np.exp(-(((xn - 0.5) ** 2 + (yn - 0.5) ** 2)) / (2 * 0.15 ** 2))
    damage = np.clip(before * (1.0 - damage_field) + rng.normal(0, 0.02, built.shape), 0, 1)
    # 重建期：毁坏区按 recovery 程度向灾前恢复
    rebuild = np.clip(damage + recovery * (before - damage) + rng.normal(0, 0.02, built.shape), 0, 1)
    layers = {"before": before.astype(np.float32), "damage": damage.astype(np.float32),
              "rebuild": rebuild.astype(np.float32)}
    info = {"bbox": bbox, "width": width, "height": height, "recovery": recovery}
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
    os.makedirs(output_dir, exist_ok=True)
    bbox = list(args.bbox) if args.bbox else None

    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        if cube.shape[0] < 3:
            raise ValidationError("input needs >=3 bands (before, damage, rebuild)")
        # Replace NoData sentinel with NaN so the thresholds don't see -9999
        # as a "high-intensity building". Also detect fully NoData inputs.
        import rasterio as _rio
        with _rio.open(args.input) as _src:
            _nd = _src.nodata
        if _nd is not None:
            cube = np.where(cube == _nd, np.nan, cube).astype(np.float32)
        if not np.isfinite(cube).any():
            raise ValidationError(
                f"input raster '{args.input}' contains only NoData pixels; nothing to classify"
            )
        before, damage, rebuild = cube[0], cube[1], cube[2]
        # Validate thresholds up-front (so a config error fails fast)
        validate_thresholds(args.thr_build, args.thr_damage)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox, source="--bbox")
        validate_thresholds(args.thr_build, args.thr_damage)
        layers, _info = generate_synthetic(bbox, recovery=args.recovery)
        before, damage, rebuild = layers["before"], layers["damage"], layers["rebuild"]
        source_note = "synthetic"

    # If --bbox is also given with --input, validate the user-supplied bbox
    if bbox is not None and args.bbox is not None:
        validate_bbox(bbox, source="--bbox")

    cat = classify_progress(before, damage, rebuild, thr_build=args.thr_build, thr_damage=args.thr_damage)
    prog = reconstruction_progress(before, damage, rebuild)

    # Identify NoData pixels: any of the three epochs is NaN → NoData.
    finite = np.isfinite(before) & np.isfinite(damage) & np.isfinite(rebuild)
    # Mark NoData pixels in the class raster with -1 (write_geotiff nodata=-1)
    cat = np.where(finite, cat, -1).astype(np.int16)
    # Mark NoData pixels in the progress raster with -9999.0
    prog_out = np.where(finite, prog, -9999.0).astype(np.float32)

    cat_tif = os.path.join(output_dir, "progress_class.tif")
    write_geotiff(cat_tif, cat, bbox, nodata=-1, dtype="int16")
    prog_tif = os.path.join(output_dir, "recovery_progress.tif")
    write_geotiff(prog_tif, prog_out, bbox)

    # Category fractions only over valid pixels
    cat_valid = cat[finite]
    fracs = category_fractions(cat_valid)
    # 毁坏像元的平均恢复进度（仅 valid 像素）
    destroyed_mask = (cat_valid == 2) | (cat_valid == 3) | (cat_valid == 4)
    prog_valid = prog[finite]
    mean_progress = float(prog_valid[destroyed_mask].mean()) if destroyed_mask.any() else 0.0

    params = {"source": source_note, "thr_build": args.thr_build, "thr_damage": args.thr_damage,
              "labels": CATEGORY_LABELS}
    params_path = os.path.join(output_dir, "reconstruction_params.json")
    with open(params_path, "w", encoding="utf-8") as f:
        json.dump(params, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "category_fraction": fracs,
        "mean_recovery_progress": mean_progress,
        "rebuilt_fraction": fracs["rebuilt"],
        "destroyed_fraction": fracs["destroyed"],
        "n_valid_pixels": int(finite.sum()),
        "n_total_pixels": int(finite.size),
    }
    outputs = [
        {"path": cat_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": prog_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": params_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, {"input": args.input, "bbox": bbox, "recovery": args.recovery,
                              "synthetic": bool(args.synthetic)}, outputs, qa, started_at, 0)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] rebuilt: {fracs['rebuilt']:.3f}  destroyed: {fracs['destroyed']:.3f}  "
              f"under_construction: {fracs['under_construction']:.3f}")
        print(f"[{SKILL_NAME}] mean recovery progress (damaged px): {mean_progress:.3f}")
        print(f"[{SKILL_NAME}] outputs: {output_dir}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Post-disaster reconstruction monitoring (multi-temporal building change).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"))
    p.add_argument("--input", help="input GeoTIFF (band1=before, band2=damage, band3=rebuild building intensity)")
    p.add_argument("--thr-build", type=float, default=0.5, help="building presence threshold (default: 0.5)")
    p.add_argument("--thr-damage", type=float, default=0.3, help="damaged/lost threshold (default: 0.3)")
    p.add_argument("--recovery", type=float, default=0.7, help="synthetic recovery degree 0-1 (default: 0.7)")
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
