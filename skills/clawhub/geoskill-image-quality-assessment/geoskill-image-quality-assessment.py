#!/usr/bin/env python3
"""image-quality-assessment — 影像质量评估

评估多光谱影像的辐射质量与空间质量，输出量化评分与 HTML 报告。

指标体系
--------
辐射质量（Radiometric）
  - **SNR**（信噪比）：逐波段 mean / std，越高越干净。
  - **striping**（条带指数）：逐列均值的标准差 / 全局标准差，越大条带越重。
  - **dead_lines**（坏线比例）：方差≈0 的行或列占总数的比例。

空间质量（Spatial）
  - **cloud_cover**（云覆盖率）：高反射率像元（>阈值）占比。
  - **sharpness**（清晰度）：Laplacian 方差，越大越清晰。

综合评分：各指标归一化到 0-100 后加权求和（辐射 60% + 空间 40%）。

数据源：本地多波段 GeoTIFF；或 ``--synthetic`` / 仅给 ``--bbox`` 时离线生成
含可控质量缺陷（噪声、条带、坏线、云、模糊）的模拟影像。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python image-quality-assessment.py --bbox 116 39 117 40 --synthetic
    python image-quality-assessment.py --input scene.tif --metrics snr,striping,cloud

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
SKILL_NAME = "image-quality-assessment"

ALL_METRICS = ["snr", "striping", "dead_lines", "cloud", "sharpness"]


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


def validate_synth_params(noise, stripe, dead_cols, cloud_frac, blur, cloud_threshold) -> None:
    """Validate synthetic-mode defect parameters. Raise ValidationError -> exit 6."""
    for name, val in (
        ("--noise", noise), ("--stripe", stripe),
        ("--cloud-frac", cloud_frac), ("--blur", blur),
    ):
        try:
            v = float(val)
        except (TypeError, ValueError) as exc:
            raise ValidationError(f"{name} must be numeric: {val}") from exc
        if v < 0:
            raise ValidationError(f"{name} must be >= 0 (got {v})")
    try:
        thr = float(cloud_threshold)
    except (TypeError, ValueError) as exc:
        raise ValidationError(f"--cloud-threshold must be numeric: {cloud_threshold}") from exc
    if not (0.0 <= thr <= 1.0):
        raise ValidationError(f"--cloud-threshold must be in [0,1] (got {thr})")
    if int(dead_cols) < 0:
        raise ValidationError(f"--dead-cols must be >= 0 (got {dead_cols})")

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
# 核心指标
# ---------------------------------------------------------------------------
def compute_snr(band: np.ndarray) -> float:
    """SNR = mean / std（越大越好）。std≈0 时返回 inf。"""
    valid = band[np.isfinite(band)]
    if valid.size == 0:
        return 0.0
    mu = float(np.mean(valid))
    sd = float(np.std(valid))
    if sd < 1e-9:
        return float("inf") if abs(mu) > 1e-9 else 0.0
    return abs(mu) / sd


def compute_striping(band: np.ndarray) -> float:
    """条带指数 = std(列均值) / std(全图)（越小越好，0=无条带）。"""
    valid = np.where(np.isfinite(band), band, np.nan)
    col_means = np.nanmean(valid, axis=0)
    col_means = col_means[np.isfinite(col_means)]
    global_std = float(np.nanstd(valid))
    if global_std < 1e-9 or col_means.size == 0:
        return 0.0
    return float(np.std(col_means) / global_std)


def compute_dead_lines(band: np.ndarray, var_threshold: float = 1e-6) -> float:
    """坏线比例 = 方差≈0 的行+列 占总行+列的比例（越小越好）。"""
    valid = np.where(np.isfinite(band), band, 0.0)
    row_vars = np.var(valid, axis=1)
    col_vars = np.var(valid, axis=0)
    dead_rows = int(np.sum(row_vars < var_threshold))
    dead_cols = int(np.sum(col_vars < var_threshold))
    total = valid.shape[0] + valid.shape[1]
    if total == 0:
        return 0.0
    return (dead_rows + dead_cols) / total


def compute_cloud_cover(band: np.ndarray, threshold: float = 0.6) -> float:
    """云覆盖率 = 反射率 > threshold 的像元占比（越小越好）。

    对单一波段（通常用蓝光或全波段均值）做阈值判断。
    """
    valid = band[np.isfinite(band)]
    if valid.size == 0:
        return 0.0
    return float(np.mean(valid > threshold))


def compute_sharpness(band: np.ndarray) -> float:
    """清晰度 = Laplacian 方差（越大越清晰）。用 3×3 Laplacian 卷积。"""
    valid = np.where(np.isfinite(band), band, 0.0)
    # Laplacian kernel [[0,1,0],[1,-4,1],[0,1,0]]
    kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], dtype=np.float64)
    from scipy.ndimage import convolve
    lap = convolve(valid.astype(np.float64), kernel, mode="reflect")
    return float(np.var(lap))


def assess_quality(
    cube: np.ndarray,
    metrics: List[str],
    cloud_threshold: float = 0.6,
) -> Dict[str, Any]:
    """对 (bands, H, W) 立方体计算指定指标，返回逐波段 + 汇总结果。"""
    if cube.ndim == 2:
        cube = cube[np.newaxis, ...]
    nb = cube.shape[0]

    per_band: List[Dict[str, Any]] = []
    for b in range(nb):
        band = cube[b].astype(np.float64)
        entry: Dict[str, Any] = {"band_index": b}
        if "snr" in metrics:
            entry["snr"] = round(compute_snr(band), 4)
        if "striping" in metrics:
            entry["striping"] = round(compute_striping(band), 6)
        if "dead_lines" in metrics:
            entry["dead_lines"] = round(compute_dead_lines(band), 6)
        if "cloud" in metrics:
            entry["cloud_cover"] = round(compute_cloud_cover(band, cloud_threshold), 6)
        if "sharpness" in metrics:
            entry["sharpness"] = round(compute_sharpness(band), 4)
        per_band.append(entry)

    # 汇总（各指标跨波段平均）
    summary: Dict[str, float] = {}
    if "snr" in metrics:
        snrs = [e["snr"] for e in per_band if np.isfinite(e["snr"])]
        summary["mean_snr"] = round(float(np.mean(snrs)), 4) if snrs else 0.0
    if "striping" in metrics:
        summary["mean_striping"] = round(
            float(np.mean([e["striping"] for e in per_band])), 6)
    if "dead_lines" in metrics:
        summary["mean_dead_lines"] = round(
            float(np.mean([e["dead_lines"] for e in per_band])), 6)
    if "cloud" in metrics:
        summary["mean_cloud_cover"] = round(
            float(np.mean([e["cloud_cover"] for e in per_band])), 6)
    if "sharpness" in metrics:
        summary["mean_sharpness"] = round(
            float(np.mean([e["sharpness"] for e in per_band])), 4)

    # 综合评分 0-100（辐射 60% + 空间 40%）
    score = compute_score(summary, metrics)

    return {
        "n_bands": nb,
        "metrics": metrics,
        "per_band": per_band,
        "summary": summary,
        "overall_score": score,
    }


def compute_score(summary: Dict[str, float], metrics: List[str]) -> float:
    """把各指标归一化到 0-100 并加权求综合评分。"""
    radiometric_scores: List[float] = []
    spatial_scores: List[float] = []

    if "snr" in metrics and "mean_snr" in summary:
        # SNR > 50 视为优秀，< 5 视为差
        radiometric_scores.append(min(100.0, summary["mean_snr"] / 50.0 * 100.0))
    if "striping" in metrics and "mean_striping" in summary:
        # striping < 0.05 优秀，> 0.5 差
        radiometric_scores.append(max(0.0, 100.0 * (1.0 - summary["mean_striping"] / 0.5)))
    if "dead_lines" in metrics and "mean_dead_lines" in summary:
        # dead_lines = 0 优秀，> 0.1 差
        radiometric_scores.append(max(0.0, 100.0 * (1.0 - summary["mean_dead_lines"] / 0.1)))
    if "cloud" in metrics and "mean_cloud_cover" in summary:
        # cloud = 0 优秀，> 0.5 差
        spatial_scores.append(max(0.0, 100.0 * (1.0 - summary["mean_cloud_cover"] / 0.5)))
    if "sharpness" in metrics and "mean_sharpness" in summary:
        # sharpness > 100 优秀，< 1 差（对数尺度）
        sh = summary["mean_sharpness"]
        spatial_scores.append(min(100.0, 100.0 * np.log1p(sh) / np.log1p(100.0)))

    rad = float(np.mean(radiometric_scores)) if radiometric_scores else None
    spa = float(np.mean(spatial_scores)) if spatial_scores else None
    if rad is not None and spa is not None:
        return round(0.6 * rad + 0.4 * spa, 2)
    if rad is not None:
        return round(rad, 2)
    if spa is not None:
        return round(spa, 2)
    return 0.0


# ---------------------------------------------------------------------------
# 合成数据：含可控质量缺陷的影像
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 128,
    height: int = 128,
    noise_level: float = 0.02,
    stripe_strength: float = 0.0,
    n_dead_cols: int = 0,
    cloud_fraction: float = 0.0,
    blur_sigma: float = 0.0,
    seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成 (4, H, W) 反射率立方体，可注入噪声/条带/坏线/云/模糊。"""
    rng = np.random.default_rng(seed)
    nb = 4
    yy, xx = np.mgrid[0:height, 0:width]
    yn = yy.astype(np.float64) / max(height - 1, 1)
    xn = xx.astype(np.float64) / max(width - 1, 1)

    cube = np.zeros((nb, height, width), dtype=np.float64)
    base_means = [0.12, 0.15, 0.18, 0.35]   # 蓝 绿 红 近红外
    for b in range(nb):
        # 平滑地表梯度 + 纹理
        surf = base_means[b] * (0.6 + 0.4 * np.sin(3 * np.pi * xn) * np.cos(2 * np.pi * yn))
        surf = np.clip(surf, 0.02, 0.9)
        # 高斯噪声
        surf = surf + rng.normal(0, noise_level, size=surf.shape)
        cube[b] = surf

    # 条带：逐列加随机偏移
    if stripe_strength > 0:
        for b in range(nb):
            col_offsets = rng.normal(0, stripe_strength, size=width)
            cube[b] += col_offsets[np.newaxis, :]

    # 坏列：设为常数
    if n_dead_cols > 0:
        dead_cols = rng.choice(width, size=min(n_dead_cols, width), replace=False)
        for b in range(nb):
            cube[b][:, dead_cols] = 0.0

    # 云：随机椭圆区域设为高反射率
    if cloud_fraction > 0:
        mask = rng.random((height, width)) < cloud_fraction
        for b in range(nb):
            cube[b][mask] = 0.85 + rng.normal(0, 0.03, size=int(mask.sum()))

    # 模糊：高斯平滑
    if blur_sigma > 0:
        from scipy.ndimage import gaussian_filter
        for b in range(nb):
            cube[b] = gaussian_filter(cube[b], sigma=blur_sigma)

    cube = np.clip(cube, 0.0, 1.0).astype(np.float32)
    info = {
        "bbox": bbox, "width": width, "height": height,
        "noise_level": noise_level, "stripe_strength": stripe_strength,
        "n_dead_cols": n_dead_cols, "cloud_fraction": cloud_fraction,
        "blur_sigma": blur_sigma,
    }
    return cube, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
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
# HTML 报告
# ---------------------------------------------------------------------------
def write_html_report(path: str, result: Dict[str, Any], source: str) -> None:
    score = result["overall_score"]
    grade = ("优秀" if score >= 80 else "良好" if score >= 60
             else "一般" if score >= 40 else "较差")
    color = ("#2e7d32" if score >= 80 else "#558b2f" if score >= 60
             else "#f9a825" if score >= 40 else "#c62828")
    rows = []
    for k, v in result["summary"].items():
        rows.append(f"<tr><td>{k}</td><td>{v}</td></tr>")
    band_rows = []
    for e in result["per_band"]:
        cells = "".join(f"<td>{v}</td>" for k, v in e.items())
        band_rows.append(f"<tr>{cells}</tr>")
    html = f"""<!DOCTYPE html>
<html lang="zh"><head><meta charset="utf-8"><title>影像质量报告</title>
<style>
body{{font-family:sans-serif;margin:2em;}}
h1{{color:#1565c0;}}
.score{{font-size:2.5em;font-weight:bold;color:{color};}}
table{{border-collapse:collapse;margin:1em 0;}}
td,th{{border:1px solid #ccc;padding:6px 12px;text-align:left;}}
th{{background:#f5f5f5;}}
</style></head><body>
<h1>影像质量评估报告 | Image Quality Report</h1>
<p>数据源 / Source: <b>{source}</b></p>
<p>综合评分 / Overall Score: <span class="score">{score}</span> / 100（{grade}）</p>
<h2>汇总指标 / Summary</h2>
<table><tr><th>指标</th><th>数值</th></tr>{''.join(rows)}</table>
<h2>逐波段 / Per-band</h2>
<table><tr>{''.join(f'<th>{k}</th>' for k in result['per_band'][0].keys())}</tr>
{''.join(band_rows)}</table>
<p><small>Generated by {SKILL_NAME} v{VERSION} at {_utc_now()}</small></p>
</body></html>"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------
def write_manifest(output_dir, args, outputs, qa, started_at, exit_code, bbox):
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME, skill_version=VERSION, command=cmd,
        started_at=started_at, finished_at=_utc_now(), exit_code=exit_code,
        inputs={
            "input": getattr(args, "input", None),
            "metrics": getattr(args, "metrics", None),
            "synthetic": bool(getattr(args, "synthetic", False)),
        },
        outputs=[OutputFile(**o) for o in outputs], qa=qa,
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

    metrics = [m.strip() for m in args.metrics.split(",") if m.strip()]
    for m in metrics:
        if m not in ALL_METRICS:
            raise UsageError(
                f"unknown metric '{m}'. Choose from: {ALL_METRICS}", metric=m)

    # Validate bbox and synthetic params BEFORE creating output directory.
    if bbox is not None:
        validate_bbox(bbox)
    validate_synth_params(
        args.noise, args.stripe, args.dead_cols, args.cloud_frac,
        args.blur, args.cloud_threshold,
    )

    os.makedirs(output_dir, exist_ok=True)

    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        if bbox is None:
            validate_bbox(file_bbox)
            bbox = file_bbox
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        cube, synth_info = generate_synthetic(
            bbox,
            noise_level=args.noise, stripe_strength=args.stripe,
            n_dead_cols=args.dead_cols, cloud_fraction=args.cloud_frac,
            blur_sigma=args.blur,
        )
        source_note = "synthetic"

    if cube.size == 0:
        raise ValidationError("input raster is empty")

    result = assess_quality(cube, metrics, cloud_threshold=args.cloud_threshold)

    # 输出 JSON
    json_path = os.path.join(output_dir, "quality_report.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    # 输出 HTML
    html_path = os.path.join(output_dir, "quality_report.html")
    write_html_report(html_path, result, source_note)

    qa: Dict[str, Any] = {
        "source": source_note,
        "metrics": metrics,
        "overall_score": result["overall_score"],
    }
    qa.update(result["summary"])
    if synth_info is not None:
        qa["synthetic_defects"] = {
            k: synth_info[k] for k in
            ("noise_level", "stripe_strength", "n_dead_cols", "cloud_fraction", "blur_sigma")
        }

    outputs = [
        {"path": json_path, "kind": "json"},
        {"path": html_path, "kind": "text"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] metrics: {', '.join(metrics)}")
        print(f"[{SKILL_NAME}] overall score: {result['overall_score']} / 100")
        for k, v in result["summary"].items():
            print(f"[{SKILL_NAME}]   {k}: {v}")
        print(f"[{SKILL_NAME}] JSON: {json_path}")
        print(f"[{SKILL_NAME}] HTML: {html_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Assess radiometric & spatial quality of multispectral imagery.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input multiband GeoTIFF")
    p.add_argument("--metrics", default="snr,striping,dead_lines,cloud,sharpness",
                   help=f"comma-separated metrics: {ALL_METRICS}")
    p.add_argument("--cloud-threshold", type=float, default=0.6,
                   help="reflectance threshold for cloud detection (default: 0.6)")
    # synthetic defect controls
    p.add_argument("--noise", type=float, default=0.02,
                   help="synthetic Gaussian noise level (default: 0.02)")
    p.add_argument("--stripe", type=float, default=0.0,
                   help="synthetic striping strength (default: 0)")
    p.add_argument("--dead-cols", type=int, default=0,
                   help="synthetic number of dead columns (default: 0)")
    p.add_argument("--cloud-frac", type=float, default=0.0,
                   help="synthetic cloud fraction (default: 0)")
    p.add_argument("--blur", type=float, default=0.0,
                   help="synthetic blur sigma (default: 0)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a synthetic scene with controlled defects (offline)")
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
