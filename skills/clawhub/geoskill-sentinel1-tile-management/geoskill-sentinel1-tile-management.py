#!/usr/bin/env python3
"""sentinel1-tile-management — Sentinel-1 数据管理流水线

模拟 Sentinel-1 GRD（地距多视）影像的标准预处理流水线：

1. **读入 / 生成 σ⁰**（线性功率）。
2. **分贝转换**：``dB = 10·log10(σ⁰)``，SAR 惯用的对数刻度。
3. **裁剪到 bbox**：把场景裁到用户指定的地理范围。
4. **逐极化处理**（VV / VH）：IW 模式双极化、EW 模式可选。
5. **输出** 预处理后的 σ⁰(dB) GeoTIFF + 处理日志 JSON（步骤、参数、统计）。

物理约束：地表 σ⁰(dB) 典型范围约 −30 ~ 0 dB（平静水面接近 −30 dB，城市
角反射器接近 0 dB）；流水线会把超出 ``--db-min/--db-max`` 物理区间的值标记
并在日志中报告越界像元比例。

数据源：本地线性 σ⁰ GeoTIFF（``--input``，多波段视为 VV/VH/...），或
``--synthetic`` 生成 S1 风格双极化 σ⁰ 场景（VV > VH，含斑点噪声）。

隐私声明 / Privacy：
- 默认完全离线，``--synthetic`` 无网络。
- 所有处理本地完成，不上传用户数据。

Usage:
    python sentinel1-tile-management.py --input grd.tif --bbox 116 39 117 40 --output-dir ./out
    python sentinel1-tile-management.py --bbox 116 39 117 40 --mode iw --polarization vv,vh --output-dir ./out

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
SKILL_NAME = "sentinel1-tile-management"

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

VALID_POLS = ("vv", "vh", "hh", "hv")


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


def validate_db_range(db_min: float, db_max: float) -> None:
    """--db-min / --db-max must satisfy db_min < db_max (and finite)."""
    for v, name in ((db_min, "--db-min"), (db_max, "--db-max")):
        try:
            float(v)
        except (TypeError, ValueError) as exc:
            raise ValidationError(f"{name} must be a float (got {v!r})") from exc
        if float(v) != float(v):  # NaN check
            raise ValidationError(f"{name} is NaN")
    if float(db_min) >= float(db_max):
        raise ValidationError(
            f"--db-min ({db_min}) must be < --db-max ({db_max}); otherwise no value "
            "can be in range and the QA statistics are meaningless."
        )


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def linear_to_db(sigma0: np.ndarray, floor: float = 1e-6) -> np.ndarray:
    """线性功率 σ⁰ → 分贝：``dB = 10·log10(σ⁰)``。

    ``floor`` 防止 log10(0)：低于 floor 的正值被抬到 floor。
    NaN 保留为 NaN（不让 NoData 静默转为 -60 dB 假数据），在下游
    ``band_statistics`` / ``db_in_range`` 中由 ``isfinite`` 过滤。
    """
    s = np.asarray(sigma0, dtype=np.float64)
    # Only floor the FINITE non-positive values (0 / negative numerical noise)
    # NaN / Inf are passed through as NaN — NoData must remain NoData.
    finite_pos = np.isfinite(s) & (s > floor)
    s = np.where(finite_pos, s, np.where(np.isfinite(s), floor, np.nan))
    return (10.0 * np.log10(s)).astype(np.float32)


def clip_to_bbox(
    array: np.ndarray, src_bbox: List[float], dst_bbox: List[float]
) -> Tuple[np.ndarray, List[float]]:
    """把 2D/3D 数组从 src_bbox 裁到 dst_bbox（像素对齐，取交集）。

    返回 ``(clipped, actual_bbox)``；交集为空时抛 ValidationError。
    行 0 对应北边界（标准 GeoTIFF 北向在上）。
    """
    arr = np.asarray(array)
    two_d = arr.ndim == 2
    if two_d:
        arr = arr[np.newaxis, ...]
    _, h, w = arr.shape

    sw, ss, se, sn = src_bbox
    dw, ds, de, dn = dst_bbox
    px_w = (se - sw) / w
    px_h = (sn - ss) / h

    # 经度 → 列；纬度 → 行（行 0 在北）
    col0 = max(int(np.floor((dw - sw) / px_w)), 0)
    col1 = min(int(np.ceil((de - sw) / px_w)), w)
    row0 = max(int(np.floor((sn - dn) / px_h)), 0)   # 目标北界 → 起始行
    row1 = min(int(np.ceil((sn - ds) / px_h)), h)    # 目标南界 → 结束行

    if col1 <= col0 or row1 <= row0:
        raise ValidationError(
            f"bbox {dst_bbox} does not intersect scene {src_bbox}",
            src_bbox=src_bbox, dst_bbox=dst_bbox,
        )

    clipped = arr[:, row0:row1, col0:col1]
    actual = [
        sw + col0 * px_w,      # west
        sn - row1 * px_h,      # south
        sw + col1 * px_w,      # east
        sn - row0 * px_h,      # north
    ]
    if two_d:
        clipped = clipped[0]
    return clipped, actual


def band_statistics(db: np.ndarray) -> Dict[str, Any]:
    """单波段 dB 统计。"""
    v = db[np.isfinite(db)]
    if v.size == 0:
        return {"min_db": None, "max_db": None, "mean_db": None, "std_db": None, "pixels": 0}
    return {
        "min_db": float(v.min()),
        "max_db": float(v.max()),
        "mean_db": float(v.mean()),
        "std_db": float(v.std()),
        "pixels": int(v.size),
    }


def db_in_range(db: np.ndarray, db_min: float, db_max: float) -> Dict[str, Any]:
    """检查 dB 是否落在物理合理区间，返回越界统计。"""
    v = db[np.isfinite(db)]
    if v.size == 0:
        return {"in_range_fraction": 1.0, "below_fraction": 0.0, "above_fraction": 0.0}
    below = float((v < db_min).mean())
    above = float((v > db_max).mean())
    return {
        "in_range_fraction": float(1.0 - below - above),
        "below_fraction": below,
        "above_fraction": above,
    }


def process_pipeline(
    sigma0_linear: np.ndarray,
    pols: List[str],
    src_bbox: List[float],
    dst_bbox: Optional[List[float]],
    db_min: float = -35.0,
    db_max: float = 5.0,
) -> Tuple[np.ndarray, List[float], Dict[str, Any]]:
    """完整预处理流水线：dB 转换 → 裁剪 → 逐极化统计。

    ``sigma0_linear`` 形状 ``(n_pol, H, W)``，波段顺序与 ``pols`` 对应。
    返回 ``(db_cube, out_bbox, log_dict)``。
    """
    cube = np.asarray(sigma0_linear, dtype=np.float64)
    if cube.ndim == 2:
        cube = cube[np.newaxis, ...]
    if cube.shape[0] != len(pols):
        raise ValidationError(
            f"polarization count {len(pols)} != band count {cube.shape[0]}",
            pols=pols, bands=int(cube.shape[0]),
        )

    steps: List[Dict[str, Any]] = []
    steps.append({"step": "load", "bands": int(cube.shape[0]),
                  "shape": [int(cube.shape[1]), int(cube.shape[2])]})

    # 1) dB 转换
    db_cube = np.stack([linear_to_db(cube[b]) for b in range(cube.shape[0])])
    steps.append({"step": "linear_to_db", "formula": "10*log10(sigma0)"})

    # 2) 裁剪
    out_bbox = list(src_bbox)
    if dst_bbox is not None:
        db_cube, out_bbox = clip_to_bbox(db_cube, src_bbox, dst_bbox)
        steps.append({"step": "clip_to_bbox", "dst_bbox": list(dst_bbox),
                      "actual_bbox": out_bbox,
                      "shape": [int(db_cube.shape[1]), int(db_cube.shape[2])]})
    else:
        steps.append({"step": "clip_to_bbox", "skipped": True})

    # 3) 逐极化统计 + 物理区间检查
    pol_stats: Dict[str, Any] = {}
    for b, pol in enumerate(pols):
        stats = band_statistics(db_cube[b])
        stats.update(db_in_range(db_cube[b], db_min, db_max))
        pol_stats[pol] = stats

    log = {
        "steps": steps,
        "polarizations": pols,
        "physical_range_db": [db_min, db_max],
        "per_pol_statistics": pol_stats,
        "output_shape": [int(db_cube.shape[1]), int(db_cube.shape[2])],
        "output_bbox": out_bbox,
    }
    return db_cube.astype(np.float32), out_bbox, log


# ---------------------------------------------------------------------------
# 合成数据：S1 风格双极化 σ⁰ 场景
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    pols: List[str],
    width: int = 128,
    height: int = 128,
    seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成 S1 风格 σ⁰（线性功率）场景。

    地物：农田基底（VV ≈ -12 dB，VH 比 VV 低 ~7 dB）、水体（极低）、城市
    斑块（高）。乘性斑点噪声模拟 SAR 散斑。返回 ``(cube, info)``，cube 形状
    ``(n_pol, H, W)``。
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    yy_n = yy.astype(np.float32) / max(height - 1, 1)
    xx_n = xx.astype(np.float32) / max(width - 1, 1)

    # 基准 dB 场（VV）
    db_vv = np.full((height, width), -12.0, dtype=np.float32)  # 农田
    water = (xx_n + yy_n) < 0.5
    db_vv[water] = -22.0
    # 城市斑块
    blocks = [(20, 20, 45, 45), (70, 75, 100, 105)]
    for (r0, c0, r1, c1) in blocks:
        r1 = min(r1, height)
        c1 = min(c1, width)
        db_vv[r0:r1, c0:c1] = -4.0
    # 斑点（dB 域加性高斯 ~ 线性域乘性）
    db_vv = db_vv + rng.normal(0, 1.2, (height, width)).astype(np.float32)

    # 各极化相对 VV 的偏移（典型：VH ≈ VV - 7 dB；HH ≈ VV；HV ≈ VH）
    offsets = {"vv": 0.0, "vh": -7.0, "hh": -0.5, "hv": -7.0}
    bands = []
    for pol in pols:
        db = db_vv + offsets.get(pol, -7.0)
        lin = np.power(10.0, db / 10.0)
        bands.append(lin.astype(np.float32))
    cube = np.stack(bands).astype(np.float32)

    info = {
        "bbox": bbox, "width": width, "height": height, "seed": seed,
        "polarizations": pols,
        "db_offsets_vs_vv": {p: offsets.get(p, -7.0) for p in pols},
    }
    return cube, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(
    path: str, cube: np.ndarray, bbox: List[float],
    nodata: float = -9999.0, dtype: str = "float32",
) -> None:
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
    """读取栅格，返回 (cube, bbox)。

    NoData 哨兵值（src.nodata）会被替换为 NaN 以避免污染下游 dB 转换
    （-9999 会被 floor 成 -60 dB 假数据，污染物理区间 QA 统计）。
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


def _parse_pols(spec: str) -> List[str]:
    """解析 --polarization vv,vh → ['vv','vh']，校验合法性。"""
    parts = [p.strip().lower() for p in spec.split(",") if p.strip()]
    if not parts:
        raise UsageError("--polarization must list at least one channel", pols=spec)
    bad = [p for p in parts if p not in VALID_POLS]
    if bad:
        raise UsageError(
            f"invalid polarization(s) {bad}; valid: {list(VALID_POLS)}", pols=spec,
        )
    # 去重保序
    seen = set()
    out = []
    for p in parts:
        if p not in seen:
            seen.add(p)
            out.append(p)
    return out


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------
def write_manifest(
    output_dir, args, outputs, qa, started_at, exit_code, bbox,
) -> Optional[str]:
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME, skill_version=VERSION, command=cmd,
        started_at=started_at, finished_at=_utc_now(), exit_code=exit_code,
        inputs={
            "input": getattr(args, "input", None),
            "mode": getattr(args, "mode", None),
            "polarization": getattr(args, "polarization", None),
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
        raise UsageError("provide --bbox (synthetic mode) or --input <grd raster>")
    if bbox is not None:
        validate_bbox(bbox, source="--bbox")
    validate_db_range(args.db_min, args.db_max)
    pols = _parse_pols(args.polarization)

    # mkdir AFTER validation (CONVENTIONS §1.1 / common bug pattern #6)
    os.makedirs(output_dir, exist_ok=True)

    synth_info: Optional[Dict[str, Any]] = None

    # 1) 获取线性 σ⁰（通用契约）
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        # Validate user-supplied bbox against file bbox if both given
        if args.bbox is not None and bbox is not None:
            validate_bbox(bbox, source="--bbox")
        src_bbox = file_bbox
        # Reject all-NaN (would otherwise produce empty stats)
        if not np.isfinite(cube).any():
            raise ValidationError(
                f"input raster '{args.input}' contains only NoData / NaN pixels; nothing to process"
            )
        # 波段数对齐到请求的极化数（截断 / 报错）
        if cube.shape[0] < len(pols):
            raise ValidationError(
                f"input has {cube.shape[0]} bands but {len(pols)} polarizations requested",
                bands=int(cube.shape[0]), pols=pols,
            )
        cube = cube[:len(pols)]
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <grd raster>")
        cube, synth_info = generate_synthetic(bbox, pols)
        src_bbox = list(bbox)
        source_note = "synthetic"

    if cube.size == 0:
        raise ValidationError("input raster is empty")

    # 2) 预处理流水线
    db_cube, out_bbox, log = process_pipeline(
        cube, pols, src_bbox=src_bbox, dst_bbox=bbox,
        db_min=args.db_min, db_max=args.db_max,
    )
    log["mode"] = args.mode
    log["source"] = source_note

    # 3) 写出
    out_tif = os.path.join(output_dir, "sigma0_db.tif")
    # Write NaN pixels as -9999 sentinel so the GeoTIFF reader can detect NoData
    db_cube_for_write = np.where(np.isfinite(db_cube), db_cube, -9999.0).astype(np.float32)
    write_geotiff(out_tif, db_cube_for_write, out_bbox, nodata=-9999.0)

    log_path = os.path.join(output_dir, "processing_log.json")
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(log, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "mode": args.mode,
        "polarizations": pols,
        "output_shape": log["output_shape"],
        "per_pol_mean_db": {p: log["per_pol_statistics"][p]["mean_db"] for p in pols},
        "n_valid_pixels_per_pol": {p: int(log["per_pol_statistics"][p].get("pixels", 0)) for p in pols},
    }
    if synth_info is not None:
        qa["synthetic_db_offsets"] = synth_info["db_offsets_vs_vv"]

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": out_bbox, "band_count": int(db_cube.shape[0])},
        {"path": log_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, out_bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}  mode: {args.mode}")
        print(f"[{SKILL_NAME}] pols: {pols}  shape: {log['output_shape']}")
        for p in pols:
            st = log["per_pol_statistics"][p]
            print(f"[{SKILL_NAME}]   {p.upper()}: mean {st['mean_db']:.2f} dB "
                  f"[{st['min_db']:.2f}, {st['max_db']:.2f}]")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Sentinel-1 GRD preprocessing pipeline: dB conversion, bbox clip, dual-pol.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input S1 GRD σ⁰ GeoTIFF (linear power)")
    p.add_argument("--mode", default="iw", choices=["iw", "ew"],
                   help="acquisition mode (default: iw)")
    p.add_argument("--polarization", default="vv,vh",
                   help="comma-separated polarization channels, e.g. vv,vh (default: vv,vh)")
    p.add_argument("--db-min", type=float, default=-35.0,
                   help="physical lower bound for σ⁰(dB) QA (default: -35)")
    p.add_argument("--db-max", type=float, default=5.0,
                   help="physical upper bound for σ⁰(dB) QA (default: 5)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a synthetic S1-style σ⁰ scene (offline)")
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
