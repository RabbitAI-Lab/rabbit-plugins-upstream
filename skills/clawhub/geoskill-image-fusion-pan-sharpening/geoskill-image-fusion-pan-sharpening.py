#!/usr/bin/env python3
"""image-fusion-pan-sharpening — 影像融合与全色锐化

将高空间分辨率的全色波段（PAN）与低分辨率多光谱（MS）融合，得到兼具
高空间分辨率与多光谱信息的影像。实现了两种经典方法：

- **Brovey** 变换：fused_b = MS_b↑ × PAN / Σ(MS↑)。它保持各波段比例，
  融合后各波段之和等于 PAN，纹理细节由 PAN 注入。
- **IHS**（强度-色调-饱和度，等权简化）：I = mean(MS↑)，用 PAN 替换强度
  分量，反变换即 fused_b = MS_b↑ + (PAN − I)。空间细节通过强度差注入各波段。

多光谱先经双三次插值上采样到 PAN 的分辨率，再参与融合。

数据源：本地多光谱 + 全色 GeoTIFF（``--input`` + ``--pan``），或使用
``--synthetic`` 生成物理一致的模拟数据用于离线测试。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python image-fusion-pan-sharpening.py --input ms.tif --pan pan.tif --method brovey
    python image-fusion-pan-sharpening.py --bbox 116 39 117 40 --synthetic --scale 2

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
SKILL_NAME = "image-fusion-pan-sharpening"


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
# 核心算法
# ---------------------------------------------------------------------------
def _upsample_ms(ms_lr: np.ndarray, scale: int) -> np.ndarray:
    """双三次上采样低分辨率多光谱 (bands, h, w) → (bands, h*scale, w*scale)。"""
    from scipy.ndimage import zoom

    ms_lr = ms_lr.astype(np.float32)
    up = zoom(ms_lr, (1.0, float(scale), float(scale)), order=3)
    return up.astype(np.float32)


def _match_shape(a: np.ndarray, b: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """把两个 (bands, H, W) 数组裁剪到共同的空间尺寸（取左上角交集）。"""
    h = min(a.shape[1], b.shape[1])
    w = min(a.shape[2], b.shape[2])
    return a[:, :h, :w], b[:, :h, :w]


def pansharpen(
    ms_lr: np.ndarray,
    pan: np.ndarray,
    method: str = "brovey",
    scale: Optional[int] = None,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """全色锐化。

    参数
    ----
    ms_lr : (bands, h, w) 低分辨率多光谱
    pan   : (1, H, W) 或 (H, W) 高分辨率全色波段
    method: "brovey" | "ihs"
    scale : 放大倍数；None 时由 pan/ms 分辨率比自动推断

    返回 (fused (bands, H, W), params)。
    """
    if method not in ("brovey", "ihs"):
        raise UsageError(
            f"unknown method '{method}'. Choose from: brovey, ihs", method=method,
        )
    ms_lr = np.asarray(ms_lr, dtype=np.float32)
    pan = np.asarray(pan, dtype=np.float32)
    if ms_lr.ndim != 3:
        raise ValidationError(f"ms must be 3-D (bands,h,w), got ndim={ms_lr.ndim}")
    if pan.ndim == 2:
        pan = pan[np.newaxis, ...]
    if pan.ndim != 3:
        raise ValidationError(f"pan must be 2-D/3-D, got ndim={pan.ndim}")
    if ms_lr.shape[0] < 1:
        raise ValidationError("ms has no bands")

    if scale is None:
        scale = max(1, int(round(pan.shape[1] / float(ms_lr.shape[1]))))
    if scale < 1:
        raise UsageError(f"scale must be >= 1, got {scale}", scale=int(scale))

    ms_up = _upsample_ms(ms_lr, scale)
    pan_1 = pan[0:1]
    ms_up, pan_1 = _match_shape(ms_up, pan_1)
    pan_up = pan_1[0]

    denom_eps = 1e-6
    if method == "brovey":
        denom = np.sum(ms_up, axis=0)
        ratio = pan_up / np.where(np.abs(denom) > denom_eps, denom, denom_eps)
        fused = ms_up * ratio[np.newaxis, ...]
    else:  # ihs
        intensity = np.mean(ms_up, axis=0)
        detail = pan_up - intensity
        fused = ms_up + detail[np.newaxis, ...]

    fused = np.clip(fused, 0.0, None).astype(np.float32)
    params = {
        "method": method,
        "scale": int(scale),
        "n_bands": int(fused.shape[0]),
        "ms_shape": list(ms_lr.shape),
        "pan_shape": list(pan.shape),
        "output_shape": list(fused.shape),
    }
    return fused, params


# ---------------------------------------------------------------------------
# 合成数据：物理一致的模拟 MS + PAN（离线测试）
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    scale: int = 2,
    bands: int = 3,
    width: int = 64,
    height: int = 64,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成高分辨率多光谱真值，再派生低分辨率 MS 与高分辨率 PAN。

    返回 (ms_lr (bands,h,w), pan_hr (1, h*scale, w*scale), info)。
    PAN 由高分辨率多光谱的亮度 + 高频纹理构成，模拟真实全色波段。
    """
    from scipy.ndimage import zoom

    rng = np.random.default_rng(seed)
    hh, ww = height * scale, width * scale

    yy, xx = np.mgrid[0:hh, 0:ww]
    yn = yy.astype(np.float32) / max(hh - 1, 1)
    xn = xx.astype(np.float32) / max(ww - 1, 1)

    truth = np.zeros((bands, hh, ww), dtype=np.float32)
    for b in range(bands):
        base = 0.12 + 0.4 * xn + 0.3 * yn + 0.1 * b / max(bands - 1, 1)
        # 高频纹理（条纹 + 噪声），让 PAN 有锐利细节
        texture = 0.08 * np.sin(2 * np.pi * 8 * xn) * np.cos(2 * np.pi * 6 * yn)
        base = base + texture + rng.normal(0, 0.01, size=base.shape).astype(np.float32)
        truth[b] = np.clip(base, 0.0, 1.0)

    # 高分辨率 PAN：多光谱亮度 + 额外纹理细节
    pan_hr = (np.mean(truth, axis=0) + 0.05 * rng.standard_normal((hh, ww))).astype(np.float32)
    pan_hr = np.clip(pan_hr, 0.0, 1.0)[np.newaxis, ...]

    # 低分辨率 MS：对高分辨率真值按 scale 块平均下采样
    ms_lr = zoom(truth, (1.0, 1.0 / scale, 1.0 / scale), order=1)
    ms_lr = np.clip(ms_lr, 0.0, 1.0).astype(np.float32)

    info = {
        "bbox": bbox,
        "scale": scale,
        "bands": bands,
        "ms_shape": list(ms_lr.shape),
        "pan_shape": list(pan_hr.shape),
        "truth_mean_per_band": [float(np.mean(truth[b])) for b in range(bands)],
    }
    return ms_lr, pan_hr, info


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
            "pan": getattr(args, "pan", None),
            "method": getattr(args, "method", None),
            "scale": getattr(args, "scale", None),
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

    # Validate bbox BEFORE creating output directory.
    if bbox is not None:
        validate_bbox(bbox)

    os.makedirs(output_dir, exist_ok=True)

    # 1) 获取数据：真实模式需同时提供 MS(--input) 与 PAN(--pan)
    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        ms_lr, file_bbox = read_geotiff(args.input)
        if bbox is None:
            validate_bbox(file_bbox)
            bbox = file_bbox
        if not args.pan:
            raise UsageError("real-data mode requires --pan <panchromatic raster>")
        pan_hr, _ = read_geotiff(args.pan)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input + --pan")
        ms_lr, pan_hr, synth_info = generate_synthetic(bbox, scale=args.scale)
        source_note = "synthetic"

    if ms_lr.size == 0 or pan_hr.size == 0:
        raise ValidationError("input raster is empty")

    # 2) 全色锐化
    fused, params = pansharpen(ms_lr, pan_hr, method=args.method, scale=args.scale)

    # 3) 写出产物
    out_tif = os.path.join(output_dir, "fused_pansharpened.tif")
    write_geotiff(out_tif, fused, bbox)

    params_path = os.path.join(output_dir, "fusion_params.json")
    with open(params_path, "w", encoding="utf-8") as f:
        json.dump(params, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "method": args.method,
        "scale": int(params["scale"]),
        "n_bands": int(fused.shape[0]),
        "output_shape": list(fused.shape),
        "mean_value_per_band": [float(np.mean(fused[b])) for b in range(fused.shape[0])],
        "overall_mean": float(np.mean(fused)),
    }
    if synth_info is not None:
        qa["synthetic_truth_mean_per_band"] = synth_info["truth_mean_per_band"]

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": int(fused.shape[0])},
        {"path": params_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] method: {args.method}  scale: {params['scale']}")
        print(f"[{SKILL_NAME}] fused shape: {fused.shape}")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        print(f"[{SKILL_NAME}] params: {params_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
        print(f"[{SKILL_NAME}] overall mean: {qa['overall_mean']:.4f}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Pan-sharpening (Brovey / IHS) fusing PAN with multispectral imagery.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input low-resolution multispectral GeoTIFF")
    p.add_argument("--pan", help="input high-resolution panchromatic GeoTIFF")
    p.add_argument("--method", default="brovey", choices=["brovey", "ihs"],
                   help="fusion method (default: brovey)")
    p.add_argument("--scale", type=int, default=2, choices=[2, 4],
                   help="spatial upscaling factor (default: 2)")
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
