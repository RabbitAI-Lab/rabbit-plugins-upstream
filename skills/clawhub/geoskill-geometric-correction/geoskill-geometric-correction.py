#!/usr/bin/env python3
"""geometric-correction — 几何精校正

基于地面控制点（GCP）对影像做多项式几何精校正。GCP 把源影像的像元坐标
(col, row) 关联到地理坐标 (lon, lat)，拟合一个多项式变换，再把源影像重采样到
规则的地理网格上，并评估每个 GCP 的残差 RMS。

- **order 1**（仿射 / 一次多项式）：6 参数（x、y 各 3），可校正平移、缩放、
  旋转、剪切。至少需要 3 个 GCP。
- **order 2**（二次多项式）：12 参数（x、y 各 6），额外建模弯曲/二阶畸变。
  至少需要 6 个 GCP。

重采样用 ``scipy.ndimage.map_coordinates``（一阶双线性），对反向变换
(geo → pixel) 逐输出像元采样。

数据源：本地畸变 GeoTIFF（``--input``，可选配 ``--gcps`` JSON），或使用
``--synthetic`` / 仅 ``--bbox`` 自动生成带已知畸变的影像与控制点用于离线测试。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python geometric-correction.py --input raw.tif --gcps gcps.json --order 1
    python geometric-correction.py --bbox 116 39 117 40 --synthetic --order 2 --output-dir ./out

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
SKILL_NAME = "geometric-correction"

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
# 输入校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox) -> None:
    """校验 bbox 合法性（W<=E, S<=N, 经纬度范围, 零面积）。"""
    if not (isinstance(bbox, (list, tuple)) and len(bbox) == 4):
        raise ValidationError(f"bbox must have 4 floats, got {bbox!r}", bbox=list(bbox))
    W_, S_, E_, N_ = (float(x) for x in bbox)
    if not (W_ <= E_ and S_ <= N_):
        raise ValidationError(
            f"invalid bbox ordering: W={W_} E={E_} S={S_} N={N_} "
            f"(require W<=E and S<=N)",
            w=W_, e=E_, s=S_, n=N_,
        )
    if not (-180.0 <= W_ <= 180.0 and -180.0 <= E_ <= 180.0):
        raise ValidationError(
            f"lon out of range [-180,180]: W={W_} E={E_}",
            w=W_, e=E_,
        )
    if not (-90.0 <= S_ <= 90.0 and -90.0 <= N_ <= 90.0):
        raise ValidationError(
            f"lat out of range [-90,90]: S={S_} N={N_}",
            s=S_, n=N_,
        )
    if (E_ - W_) <= 0.0 or (N_ - S_) <= 0.0:
        raise ValidationError(
            f"zero-area bbox: W={W_} E={E_} S={S_} N={N_}",
            w=W_, e=E_, s=S_, n=N_,
        )


def validate_gcps(gcp_pixel, gcp_geo) -> None:
    """校验 GCP 几何合法性。"""
    if gcp_pixel is None or gcp_geo is None:
        raise ValidationError("GCPs are required (got None)")
    gp = np.asarray(gcp_pixel, dtype=np.float64)
    gg = np.asarray(gcp_geo, dtype=np.float64)
    if gp.shape != gg.shape or gp.ndim != 2 or gp.shape[1] != 2:
        raise ValidationError(
            f"GCP shape must be (N, 2) for both pixel and geo, got {gp.shape} / {gg.shape}",
            pixel_shape=list(gp.shape), geo_shape=list(gg.shape),
        )
    if not np.isfinite(gp).all() or not np.isfinite(gg).all():
        raise ValidationError("GCPs contain NaN/Inf values")


# 各阶多项式所需的最少 GCP 数（项数 = (order+1)(order+2)/2）
MIN_GCPS = {1: 3, 2: 6}


# ---------------------------------------------------------------------------
# 核心算法：多项式拟合 / 评估 / RMS / 重采样
# ---------------------------------------------------------------------------
def poly_design(pts: np.ndarray, order: int) -> np.ndarray:
    """构造多项式设计矩阵。pts: (N, 2) = (col, row)。

    order 1: [1, c, r]
    order 2: [1, c, r, c*c, c*r, r*r]
    """
    pts = np.asarray(pts, dtype=np.float64)
    if pts.ndim != 2 or pts.shape[1] != 2:
        raise ValidationError("points must have shape (N, 2)")
    if order not in (1, 2):
        raise UsageError(f"order must be 1 or 2, got {order}", order=int(order))
    c = pts[:, 0]
    r = pts[:, 1]
    cols = [np.ones_like(c), c, r]
    if order == 2:
        cols += [c * c, c * r, r * r]
    return np.column_stack(cols)


def fit_poly(src: np.ndarray, dst: np.ndarray, order: int) -> np.ndarray:
    """最小二乘拟合多项式 src (N,2) → dst (N,2)。返回系数 (2, nterms)。"""
    src = np.asarray(src, dtype=np.float64)
    dst = np.asarray(dst, dtype=np.float64)
    need = MIN_GCPS.get(order, 3)
    if src.shape[0] < need:
        raise ValidationError(
            f"order {order} needs >= {need} GCPs, got {src.shape[0]}",
            n_gcp=int(src.shape[0]), order=int(order),
        )
    A = poly_design(src, order)
    coeff_x, *_ = np.linalg.lstsq(A, dst[:, 0], rcond=None)
    coeff_y, *_ = np.linalg.lstsq(A, dst[:, 1], rcond=None)
    return np.vstack([coeff_x, coeff_y])


def eval_poly(coeffs: np.ndarray, pts: np.ndarray) -> np.ndarray:
    """用系数 (2, nterms) 在 pts (N,2) 上求值，返回 (N,2)。"""
    pts = np.asarray(pts, dtype=np.float64)
    order = 2 if coeffs.shape[1] == 6 else 1
    A = poly_design(pts, order)
    x = A @ coeffs[0]
    y = A @ coeffs[1]
    return np.column_stack([x, y])


def gcp_rms(coeffs: np.ndarray, src: np.ndarray, dst: np.ndarray) -> Dict[str, Any]:
    """计算 GCP 残差 RMS（坐标单位）。"""
    pred = eval_poly(coeffs, src)
    resid = pred - np.asarray(dst, dtype=np.float64)
    rms_x = float(np.sqrt(np.mean(resid[:, 0] ** 2)))
    rms_y = float(np.sqrt(np.mean(resid[:, 1] ** 2)))
    rms_total = float(np.sqrt(np.mean(np.sum(resid ** 2, axis=1))))
    per_gcp = np.sqrt(np.sum(resid ** 2, axis=1))
    return {
        "rms_x": rms_x,
        "rms_y": rms_y,
        "rms_total": rms_total,
        "per_gcp_residual": [float(v) for v in per_gcp],
    }


def resample_cube(
    cube: np.ndarray,
    inv_coeffs: np.ndarray,
    bbox: List[float],
    out_h: int,
    out_w: int,
    nodata: float = -9999.0,
) -> np.ndarray:
    """把 cube (bands, Hs, Ws) 重采样到 bbox 定义的 out_h×out_w 地理网格。

    inv_coeffs: geo → pixel(col,row) 的多项式系数。
    """
    from scipy.ndimage import map_coordinates

    w0, s0, w1, n0 = bbox
    js = np.arange(out_w, dtype=np.float64)
    is_ = np.arange(out_h, dtype=np.float64)
    gx = w0 + (js + 0.5) * (w1 - w0) / out_w          # (out_w,)
    gy = n0 + (is_ + 0.5) * (s0 - n0) / out_h          # (out_h,) 顶部=n0
    gxg, gyg = np.meshgrid(gx, gy)                     # (out_h, out_w)
    geo_pts = np.column_stack([gxg.ravel(), gyg.ravel()])
    pix = eval_poly(inv_coeffs, geo_pts)               # (N, 2) = (col, row)
    cols = pix[:, 0].reshape(out_h, out_w)
    rows = pix[:, 1].reshape(out_h, out_w)

    nb, hs, ws = cube.shape
    out = np.full((nb, out_h, out_w), nodata, dtype=np.float32)
    for b in range(nb):
        sampled = map_coordinates(
            cube[b].astype(np.float64), [rows, cols],
            order=1, mode="constant", cval=nodata,
        )
        out[b] = sampled.astype(np.float32)
    return out


def correct_geometry(
    cube: np.ndarray,
    gcp_pixel: np.ndarray,
    gcp_geo: np.ndarray,
    bbox: List[float],
    order: int = 1,
    out_h: Optional[int] = None,
    out_w: Optional[int] = None,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """完整几何精校正：拟合 + RMS + 重采样。返回 (corrected_cube, report)。"""
    gcp_pixel = np.asarray(gcp_pixel, dtype=np.float64)
    gcp_geo = np.asarray(gcp_geo, dtype=np.float64)
    if gcp_pixel.shape != gcp_geo.shape:
        raise ValidationError("gcp_pixel and gcp_geo shape mismatch")

    fwd = fit_poly(gcp_pixel, gcp_geo, order)      # pixel -> geo
    inv = fit_poly(gcp_geo, gcp_pixel, order)      # geo -> pixel
    rms = gcp_rms(fwd, gcp_pixel, gcp_geo)

    hs, ws = cube.shape[1], cube.shape[2]
    if out_h is None:
        out_h = hs
    if out_w is None:
        out_w = ws

    corrected = resample_cube(cube, inv, bbox, out_h, out_w)
    report = {
        "order": int(order),
        "n_gcp": int(gcp_pixel.shape[0]),
        "rms": rms,
        "forward_coeffs": fwd.tolist(),
        "inverse_coeffs": inv.tolist(),
        "output_shape": [int(cube.shape[0]), int(out_h), int(out_w)],
    }
    return corrected, report


# ---------------------------------------------------------------------------
# 合成数据：带已知畸变的影像 + 控制点（离线测试）
# ---------------------------------------------------------------------------
def _ideal_surface(gx: np.ndarray, gy: np.ndarray, bbox: List[float]) -> np.ndarray:
    """定义在地理坐标上的平滑理想影像（梯度 + 纹理），范围约 [0,1]。"""
    w0, s0, w1, n0 = bbox
    u = (gx - w0) / (w1 - w0)
    v = (gy - s0) / (n0 - s0)
    val = 0.2 + 0.4 * u + 0.3 * v + 0.08 * np.sin(6 * np.pi * u) * np.cos(4 * np.pi * v)
    return np.clip(val, 0.0, 1.0)


def generate_synthetic(
    bbox: List[float],
    order: int = 1,
    width: int = 128,
    height: int = 128,
    n_gcp_grid: int = 4,
    noise_pix: float = 0.3,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成 (src_cube, gcp_pixel, gcp_geo, info)。

    真值正向变换为仿射（含微小剪切），把源影像像素映射到 bbox 地理坐标。
    GCP 在源影像网格上均匀采样，geo 加微小扰动（模拟量测误差）。
    src_cube 为 3 波段，内容 = 理想影像在该像素地理坐标处的取值。
    """
    rng = np.random.default_rng(seed)
    w0, s0, w1, n0 = bbox
    hs, ws = height, width

    # 真值正向变换 pixel(col,row) -> geo(lon,lat)，含微小交叉项（剪切）
    sx = (w1 - w0) / (ws - 1)
    sy = (s0 - n0) / (hs - 1)   # row 增大 -> 纬度减小
    shear = 0.02 * sx
    a = np.array([
        [w0, sx, shear],       # lon = w0 + sx*col + shear*row
        [n0, -shear, sy],      # lat = n0 - shear*col + sy*row
    ], dtype=np.float64)

    # 源影像每个像素的地理坐标
    cols, rows = np.meshgrid(np.arange(ws), np.arange(hs))
    gx = a[0, 0] + a[0, 1] * cols + a[0, 2] * rows
    gy = a[1, 0] + a[1, 1] * cols + a[1, 2] * rows

    # 源影像 3 波段 = 理想曲面 + 微小波段差异
    base = _ideal_surface(gx, gy, bbox).astype(np.float32)
    nb = 3
    src = np.zeros((nb, hs, ws), dtype=np.float32)
    for b in range(nb):
        src[b] = np.clip(base + 0.05 * b, 0.0, 1.0)

    # GCP：网格采样像素点
    gi = np.linspace(0, hs - 1, n_gcp_grid)
    gj = np.linspace(0, ws - 1, n_gcp_grid)
    gr, gc = np.meshgrid(gi, gj, indexing="ij")
    gcp_row = gr.ravel()
    gcp_col = gc.ravel()
    gcp_pixel = np.column_stack([gcp_col, gcp_row])
    # 真值 geo + 微小扰动（像素量级噪声 -> 地理量级）
    gcp_gx = a[0, 0] + a[0, 1] * gcp_col + a[0, 2] * gcp_row
    gcp_gy = a[1, 0] + a[1, 1] * gcp_col + a[1, 2] * gcp_row
    gcp_gx += rng.normal(0, noise_pix * sx, size=gcp_gx.shape)
    gcp_gy += rng.normal(0, noise_pix * abs(sy), size=gcp_gy.shape)
    gcp_geo = np.column_stack([gcp_gx, gcp_gy])

    # 理想校正影像（输出网格上），供 QA 对比
    out_js = np.arange(ws)
    out_is = np.arange(hs)
    ogx = w0 + (out_js + 0.5) * (w1 - w0) / ws
    ogy = n0 + (out_is + 0.5) * (s0 - n0) / hs
    ogxg, ogyg = np.meshgrid(ogx, ogy)
    ideal = _ideal_surface(ogxg, ogyg, bbox).astype(np.float32)

    info = {
        "bbox": list(bbox),
        "order": int(order),
        "n_gcp": int(gcp_pixel.shape[0]),
        "noise_pix": float(noise_pix),
        "src_shape": [int(nb), int(hs), int(ws)],
        "_ideal": ideal,
    }
    return src, gcp_pixel, gcp_geo, info


def load_gcps(path: str) -> Tuple[np.ndarray, np.ndarray]:
    """读取 GCP JSON: {"gcps": [{"pixel": [col,row], "geo": [lon,lat]}, ...]}。"""
    if not os.path.exists(path):
        raise UsageError(f"GCP file not found: {path}", path=path)
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    items = data.get("gcps", [])
    if not items:
        raise ValidationError("GCP file contains no gcps")
    pix = np.array([it["pixel"] for it in items], dtype=np.float64)
    geo = np.array([it["geo"] for it in items], dtype=np.float64)
    return pix, geo


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
            "gcps": getattr(args, "gcps", None),
            "order": getattr(args, "order", None),
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

    # 1) 校验（在 makedirs 之前）
    if bbox is not None:
        validate_bbox(bbox)

    synth_info: Optional[Dict[str, Any]] = None

    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        if bbox is None:
            bbox = file_bbox
        if bbox is not None:
            validate_bbox(bbox)
        if args.gcps:
            gcp_pixel, gcp_geo = load_gcps(args.gcps)
        else:
            # 无 GCP 文件：基于 bbox 自动生成一套（均匀网格，无噪声）
            _, gcp_pixel, gcp_geo, synth_info = generate_synthetic(
                bbox, order=args.order, width=cube.shape[2], height=cube.shape[1],
                noise_pix=0.0,
            )
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        cube, gcp_pixel, gcp_geo, synth_info = generate_synthetic(bbox, order=args.order)
        source_note = "synthetic"

    if cube.size == 0:
        raise ValidationError("input raster is empty")
    if gcp_pixel is None or len(gcp_pixel) == 0:
        raise ValidationError(
            "no GCPs available; provide --gcps JSON or use --synthetic",
        )
    validate_gcps(gcp_pixel, gcp_geo)

    # 2) 校验通过后再创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    corrected, report = correct_geometry(cube, gcp_pixel, gcp_geo, bbox, order=args.order)

    out_tif = os.path.join(output_dir, "corrected.tif")
    write_geotiff(out_tif, corrected, bbox)

    rms_report = {
        "order": report["order"],
        "n_gcp": report["n_gcp"],
        "rms_x": report["rms"]["rms_x"],
        "rms_y": report["rms"]["rms_y"],
        "rms_total": report["rms"]["rms_total"],
        "per_gcp_residual": report["rms"]["per_gcp_residual"],
        "forward_coeffs": report["forward_coeffs"],
        "inverse_coeffs": report["inverse_coeffs"],
    }
    rms_path = os.path.join(output_dir, "rms_report.json")
    with open(rms_path, "w", encoding="utf-8") as f:
        json.dump(rms_report, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "order": report["order"],
        "n_gcp": report["n_gcp"],
        "rms_total": report["rms"]["rms_total"],
        "rms_x": report["rms"]["rms_x"],
        "rms_y": report["rms"]["rms_y"],
        "n_bands": int(corrected.shape[0]),
        "n_valid_gcp": int(gcp_pixel.shape[0]),
    }
    if synth_info is not None and "_ideal" in synth_info:
        ideal = synth_info["_ideal"]
        band0 = corrected[0]
        valid = band0 > -9000
        if valid.any():
            qa["reconstruction_rmse_vs_ideal"] = float(
                np.sqrt(np.nanmean((band0[valid] - ideal[valid]) ** 2))
            )

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": int(corrected.shape[0])},
        {"path": rms_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] order: {report['order']}  GCPs: {report['n_gcp']}")
        print(f"[{SKILL_NAME}] RMS total: {report['rms']['rms_total']:.6f} "
              f"(x={report['rms']['rms_x']:.6f}, y={report['rms']['rms_y']:.6f})")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        print(f"[{SKILL_NAME}] rms report: {rms_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="GCP-based polynomial geometric correction with RMS report.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input distorted GeoTIFF")
    p.add_argument("--gcps", help="GCP JSON file")
    p.add_argument("--order", type=int, default=1, choices=[1, 2],
                   help="polynomial order (default: 1)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a synthetic distorted scene + GCPs (offline)")
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
