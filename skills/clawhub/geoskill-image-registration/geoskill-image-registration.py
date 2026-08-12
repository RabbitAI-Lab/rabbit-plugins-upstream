#!/usr/bin/env python3
"""image-registration — 影像配准

用相位相关（phase correlation）估计两幅影像之间的平移量，并把目标影像
（target）对齐到参考影像（reference）。相位相关在频域计算互功率谱，其逆
傅里叶变换是一个尖锐的相关峰，峰的位置即平移量，对亮度偏移与噪声稳健，
可达亚像素精度。

流程：
1. 取参考与目标影像的波段均值做二维 FFT；
2. 归一化互功率谱 R = F·conj(G)/|F·conj(G)|；
3. IFFT(R) 的相关峰位置 → 平移量 (dy, dx)，并用三点抛物线做亚像素细化；
4. 用 scipy.ndimage.shift 把 target 平移 −(dy,dx) 对齐到 reference。

数据源：本地参考 + 目标 GeoTIFF（``--input`` + ``--target``），或使用
``--synthetic`` / 仅 ``--bbox`` 自动生成带已知平移的影像对用于离线测试。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python image-registration.py --input ref.tif --target mov.tif --output-dir ./out
    python image-registration.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "image-registration"


# ---------------------------------------------------------------------------
# 校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox) -> None:
    """Validate geographic bbox. Raise ValidationError -> exit 6.

    Rules:
        - 4 floats, W<S, W<=E, S<=N,  -180<=W,E<=180,  -90<=S,N<=90
        - width/height > 1e-9 (non-degenerate)
    Anti-meridian wrap (W>E) is not supported: clearly error out, do not silently
    wrap or produce garbage.
    """
    if bbox is None or len(bbox) != 4:
        raise ValidationError("bbox must be 4 floats [W S E N]")
    try:
        W, S, E, N = [float(v) for v in bbox]
    except (TypeError, ValueError) as exc:
        raise ValidationError(f"bbox values must be numeric: {bbox}") from exc
    if not (-180.0 <= W <= 180.0 and -180.0 <= E <= 180.0):
        raise ValidationError(f"bbox lon out of range [-180,180]: W={W} E={E}")
    if not (-90.0 <= S <= 90.0 and -90.0 <= N <= 90.0):
        raise ValidationError(f"bbox lat out of range [-90,90]: S={S} N={N}")
    if W >= E:
        raise ValidationError(
            f"bbox W>=E ({W}>={E}); crossing 180° not supported, please split"
        )
    if S >= N:
        raise ValidationError(f"bbox S>=N ({S}>={N})")
    if (E - W) < 1e-9 or (N - S) < 1e-9:
        raise ValidationError("bbox has zero or negative area")

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
# 核心算法：相位相关 + 亚像素平移估计 + 重采样配准
# ---------------------------------------------------------------------------
def _to_2d(cube: np.ndarray) -> np.ndarray:
    """把 (bands,H,W) 或 (H,W) 压缩为用于相关的单波段 (H,W)。"""
    cube = np.asarray(cube, dtype=np.float64)
    if cube.ndim == 3:
        return cube.mean(axis=0)
    if cube.ndim == 2:
        return cube
    raise ValidationError(f"expected 2-D/3-D image, got ndim={cube.ndim}")


def _parabolic_refine(values: np.ndarray, i: int, n: int) -> float:
    """在环形数组 values 上，对峰值索引 i 做三点抛物线亚像素细化。"""
    im = (i - 1) % n
    ip = (i + 1) % n
    y0, y1, y2 = float(values[im]), float(values[i]), float(values[ip])
    denom = y0 - 2.0 * y1 + y2
    if abs(denom) < 1e-12:
        return float(i)
    delta = 0.5 * (y0 - y2) / denom
    # 抛物线近似在峰附近有效，限制在 ±0.5 像元内
    delta = max(-0.5, min(0.5, delta))
    return float(i) + delta


def estimate_shift(ref: np.ndarray, target: np.ndarray) -> Tuple[float, float]:
    """相位相关估计 target 相对 ref 的平移量 (dy, dx)。

    约定：若 target = shift(ref, (dy,dx))，则本函数返回 ≈ (dy,dx)。
    要把 target 对齐到 ref，应施加 shift(target, (-dy,-dx))。
    """
    ref2 = _to_2d(ref)
    tgt2 = _to_2d(target)
    if ref2.shape != tgt2.shape:
        raise ValidationError(
            f"ref/target shape mismatch: {ref2.shape} vs {tgt2.shape}"
        )
    h, w = ref2.shape
    # 去均值 + 汉宁窗，抑制边界振铃
    win = np.outer(np.hanning(h), np.hanning(w))
    a = (ref2 - ref2.mean()) * win
    b = (tgt2 - tgt2.mean()) * win

    fa = np.fft.fft2(a)
    fb = np.fft.fft2(b)
    cross = fa * np.conj(fb)
    mag = np.abs(cross)
    mag[mag < 1e-12] = 1e-12
    cross = cross / mag
    corr = np.fft.ifft2(cross).real

    py, px = np.unravel_index(int(np.argmax(corr)), corr.shape)
    dy = _parabolic_refine(corr[:, px], py, h)
    dx = _parabolic_refine(corr[py, :], px, w)
    # 环形相关：超过半幅的峰表示负方向平移
    if dy > h / 2.0:
        dy -= h
    if dx > w / 2.0:
        dx -= w
    # 相关峰 (dy,dx) 是"把 target 对齐到 ref 需施加的改正量"；
    # target 相对 ref 的位移 D 为其相反数：target ≈ shift(ref, (-dy,-dx))。
    return float(-dy), float(-dx)


def apply_shift(cube: np.ndarray, dy: float, dx: float) -> np.ndarray:
    """对 cube (bands,H,W) 逐波段施加平移 (dy,dx)，双线性重采样。"""
    from scipy.ndimage import shift

    cube = np.asarray(cube, dtype=np.float64)
    single = cube.ndim == 2
    if single:
        cube = cube[np.newaxis, ...]
    out = np.zeros_like(cube, dtype=np.float32)
    for b in range(cube.shape[0]):
        out[b] = shift(cube[b], (dy, dx), order=1, mode="constant", cval=0.0).astype(np.float32)
    return out[0] if single else out


def register_image(
    ref: np.ndarray, target: np.ndarray
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """把 target 配准到 ref。返回 (registered_cube, report)。"""
    dy, dx = estimate_shift(ref, target)
    registered = apply_shift(target, -dy, -dx)
    report = {
        "estimated_shift_y": float(dy),
        "estimated_shift_x": float(dx),
        "shift_magnitude": float(np.hypot(dy, dx)),
    }
    return registered, report


# ---------------------------------------------------------------------------
# 合成数据：参考影像 + 已知平移的目标影像（离线测试）
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 128,
    height: int = 128,
    shift_y: float = 4.0,
    shift_x: float = -6.0,
    bands: int = 3,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成参考影像 ref 与平移后的目标影像 target。

    target = shift(ref, (shift_y, shift_x))。返回 (ref, target, info)，
    info 内含 true_shift 供 QA 验证偏移恢复。
    """
    from scipy.ndimage import shift

    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    yn = yy.astype(np.float32) / max(height - 1, 1)
    xn = xx.astype(np.float32) / max(width - 1, 1)

    ref = np.zeros((bands, height, width), dtype=np.float32)
    for b in range(bands):
        grad = 0.25 + 0.35 * xn + 0.25 * yn
        blob1 = 0.30 * np.exp(-(((xn - 0.35) ** 2 + (yn - 0.55) ** 2) / 0.02))
        blob2 = 0.22 * np.exp(-(((xn - 0.70) ** 2 + (yn - 0.30) ** 2) / 0.015))
        ripple = 0.04 * np.sin(2 * np.pi * 4 * xn) * np.cos(2 * np.pi * 3 * yn)
        val = grad + blob1 + blob2 + ripple + rng.normal(0, 0.003, size=(height, width))
        ref[b] = np.clip(val, 0.0, 1.0).astype(np.float32)

    target = np.zeros_like(ref)
    for b in range(bands):
        target[b] = shift(ref[b], (shift_y, shift_x), order=1, mode="constant", cval=0.0).astype(np.float32)

    info = {
        "bbox": list(bbox),
        "bands": bands,
        "shape": [int(bands), int(height), int(width)],
        "true_shift": [float(shift_y), float(shift_x)],
    }
    return ref, target, info


def _interior_rmse(a: np.ndarray, b: np.ndarray, margin: int = 20) -> float:
    """中心裁剪区域的 RMSE，避开配准后的边界无效区。"""
    a = np.asarray(a, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)
    if a.ndim == 2:
        a = a[np.newaxis, ...]
        b = b[np.newaxis, ...]
    m = margin
    aa = a[:, m:-m, m:-m] if a.shape[1] > 2 * m else a
    bb = b[:, m:-m, m:-m] if b.shape[1] > 2 * m else b
    return float(np.sqrt(np.mean((aa - bb) ** 2)))


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
            "target": getattr(args, "target", None),
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
    synth_info: Optional[Dict[str, Any]] = None

    # Validate bbox BEFORE creating output directory.
    if bbox is not None:
        validate_bbox(bbox)

    os.makedirs(output_dir, exist_ok=True)

    if args.input and not args.synthetic:
        ref, file_bbox = read_geotiff(args.input)
        if bbox is None:
            validate_bbox(file_bbox)
            bbox = file_bbox
        if not args.target:
            raise UsageError("real-data mode requires --target <raster>")
        target, _ = read_geotiff(args.target)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input + --target")
        ref, target, synth_info = generate_synthetic(bbox)
        source_note = "synthetic"

    if ref.size == 0 or target.size == 0:
        raise ValidationError("input raster is empty")
    if ref.shape[1:] != target.shape[1:]:
        raise ValidationError(
            f"ref/target spatial shape mismatch: {ref.shape[1:]} vs {target.shape[1:]}"
        )

    registered, report = register_image(ref, target)

    out_tif = os.path.join(output_dir, "registered.tif")
    write_geotiff(out_tif, registered, bbox)

    qa: Dict[str, Any] = {
        "source": source_note,
        "estimated_shift_y": report["estimated_shift_y"],
        "estimated_shift_x": report["estimated_shift_x"],
        "shift_magnitude": report["shift_magnitude"],
        "n_bands": int(registered.shape[0]),
        "interior_rmse_vs_ref": _interior_rmse(registered, ref),
    }
    if synth_info is not None:
        true = synth_info["true_shift"]
        qa["true_shift_y"] = true[0]
        qa["true_shift_x"] = true[1]
        qa["shift_recovery_error"] = float(np.hypot(
            report["estimated_shift_y"] - true[0],
            report["estimated_shift_x"] - true[1],
        ))

    offset_path = os.path.join(output_dir, "offset.json")
    with open(offset_path, "w", encoding="utf-8") as f:
        json.dump(qa, f, ensure_ascii=False, indent=2)

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": int(registered.shape[0])},
        {"path": offset_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] estimated shift: dy={report['estimated_shift_y']:.3f}, "
              f"dx={report['estimated_shift_x']:.3f} px")
        if "shift_recovery_error" in qa:
            print(f"[{SKILL_NAME}] shift recovery error: {qa['shift_recovery_error']:.4f} px")
        print(f"[{SKILL_NAME}] interior RMSE vs ref: {qa['interior_rmse_vs_ref']:.5f}")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        print(f"[{SKILL_NAME}] offset: {offset_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Sub-pixel image registration via FFT phase correlation.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="reference GeoTIFF")
    p.add_argument("--target", help="target GeoTIFF to align to reference")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a synthetic shifted image pair (offline)")
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
