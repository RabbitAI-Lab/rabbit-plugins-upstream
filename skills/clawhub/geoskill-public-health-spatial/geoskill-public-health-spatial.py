#!/usr/bin/env python3
"""public-health-spatial — 公共卫生空间分析

面向公共卫生的空间分析工具集，覆盖四个核心方法：

- **核密度估计 (KDE)**：2D 高斯核对病例点做密度制图，识别聚集热点。
- **空间扫描统计 (Kulldorff)**：圆形移动窗口最大化对数似然比 (LLR)，
  探测发病率显著升高的最可能聚集区。
- **环境关联**：发病率与环境因子栅格的 Pearson 相关，量化环境暴露关联。
- **可达性**：到最近医疗设施的距离（欧氏距离变换），评估服务覆盖。

数据源：本地多波段 GeoTIFF（人口/环境因子），或 ``--synthetic`` 生成含真实
聚集信号与正向环境关联的模拟场景用于离线测试。

隐私声明 / Privacy：默认离线运行，``--synthetic`` 完全无网络；本地处理，不上传数据。

Usage:
    python public-health-spatial.py --input data.tif --output-dir ./out
    python public-health-spatial.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "public-health-spatial"

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


BAND_ROLES = ["population", "environment"]
N_REQUIRED_BANDS = len(BAND_ROLES)
METHODS = ["kde", "scan", "all"]


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def kde_grid(
    points: np.ndarray,
    height: int,
    width: int,
    bandwidth: float = 3.0,
) -> np.ndarray:
    """2D 高斯核密度估计。points 为 (n,2) 像元坐标 [row, col]。"""
    pts = np.asarray(points, dtype=np.float64)
    out = np.zeros((height, width), dtype=np.float32)
    if pts.size == 0:
        return out
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float64)
    bw2 = 2.0 * float(bandwidth) ** 2
    norm = 1.0 / (2.0 * np.pi * float(bandwidth) ** 2)
    for r, c in pts:
        out += (norm * np.exp(-((yy - r) ** 2 + (xx - c) ** 2) / bw2)).astype(np.float32)
    return out


def kulldorff_llr(c_in: float, pop_in: float, c_total: float, pop_total: float) -> float:
    """单个窗口的 Kulldorff 对数似然比（仅 elevated 方向，<0 取 0）。"""
    c_out = c_total - c_in
    pop_out = pop_total - pop_in
    if pop_in <= 0 or pop_out <= 0 or c_total <= 0:
        return 0.0
    rate_in = c_in / pop_in
    rate_out = c_out / pop_out if pop_out > 0 else 0.0
    if rate_in <= rate_out:
        return 0.0
    llr = 0.0
    if c_in > 0:
        llr += c_in * np.log(c_in / max(pop_in * (c_total / pop_total), 1e-12))
    if c_out > 0:
        llr += c_out * np.log(c_out / max(pop_out * (c_total / pop_total), 1e-12))
    return max(float(llr), 0.0)


def spatial_scan(
    cases: np.ndarray,
    population: np.ndarray,
    centroids: np.ndarray,
    max_frac: float = 0.5,
    n_radii: int = 12,
) -> Dict[str, Any]:
    """圆形空间扫描统计。cases/population 为每个区域的计数，centroids (n,2)。

    返回最可能聚集：{center_idx, radius, llr, cases_in, pop_in, rr}。
    """
    cases = np.asarray(cases, dtype=np.float64)
    population = np.asarray(population, dtype=np.float64)
    centroids = np.asarray(centroids, dtype=np.float64)
    n = len(cases)
    c_total = float(cases.sum())
    pop_total = float(population.sum())
    if c_total <= 0 or pop_total <= 0:
        return {"center_idx": -1, "radius": 0.0, "llr": 0.0,
                "cases_in": 0.0, "pop_in": 0.0, "rr": 1.0}

    # 区域两两距离
    diff = centroids[:, None, :] - centroids[None, :, :]
    dist = np.sqrt(np.sum(diff * diff, axis=2))
    max_d = float(dist.max())
    radii = np.linspace(max_d / max(n_radii, 2), max_d, n_radii)

    best = {"llr": -1.0}
    for ci in range(n):
        for r in radii:
            inside = dist[ci] <= r
            pop_in = float(population[inside].sum())
            if pop_in <= 0 or pop_in > max_frac * pop_total:
                continue
            c_in = float(cases[inside].sum())
            llr = kulldorff_llr(c_in, pop_in, c_total, pop_total)
            if llr > best["llr"]:
                rate_in = c_in / pop_in
                rate_out = (c_total - c_in) / max(pop_total - pop_in, 1e-12)
                best = {"center_idx": int(ci), "radius": float(r), "llr": float(llr),
                        "cases_in": c_in, "pop_in": pop_in,
                        "rr": float(rate_in / rate_out) if rate_out > 0 else float("inf")}
    if best["llr"] < 0:
        return {"center_idx": -1, "radius": 0.0, "llr": 0.0,
                "cases_in": 0.0, "pop_in": 0.0, "rr": 1.0}
    return best


def pearson_corr(a: np.ndarray, b: np.ndarray) -> float:
    """两栅格的 Pearson 相关系数（忽略 NaN）。"""
    a = np.asarray(a, dtype=np.float64).ravel()
    b = np.asarray(b, dtype=np.float64).ravel()
    mask = np.isfinite(a) & np.isfinite(b)
    a, b = a[mask], b[mask]
    if a.size < 2:
        return 0.0
    am, bm = a - a.mean(), b - b.mean()
    denom = np.sqrt(np.sum(am * am) * np.sum(bm * bm))
    if denom < 1e-12:
        return 0.0
    return float(np.sum(am * bm) / denom)


def accessibility_distance(facility_mask: np.ndarray, pixel_size: float = 1.0) -> np.ndarray:
    """到最近设施的距离栅格（欧氏距离变换 × 像元尺寸）。"""
    from scipy.ndimage import distance_transform_edt
    m = np.asarray(facility_mask) > 0
    if not m.any():
        return np.full(facility_mask.shape, np.inf, dtype=np.float32)
    d = distance_transform_edt(~m)
    return (d * float(pixel_size)).astype(np.float32)


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic_scene(
    bbox: List[float], width: int = 128, height: int = 128, seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成 (人口, 环境) 栅格 + 病例/设施点，含一个真实聚集簇与正向环境关联。

    返回 (cube[2,H,W], case_points[N,2](row,col), info)。
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    population = (500.0 + 100.0 * np.sin(np.pi * xx / width) +
                  rng.normal(0, 20, (height, width))).astype(np.float32)
    population = np.clip(population, 1, None)

    # 环境因子：一个污染高值区在 (0.35,0.35) 处
    env = (rng.normal(0, 0.1, (height, width))).astype(np.float32)
    env += 2.0 * np.exp(-((((yy / height) - 0.35) ** 2 + ((xx / width) - 0.35) ** 2)) / (2 * 0.08 ** 2))

    # 病例点：聚集簇在 (0.35,0.35) + 均匀背景
    cluster_n = 60
    bg_n = 40
    cr, cc = 0.35 * height, 0.35 * width
    cluster = np.column_stack([
        rng.normal(cr, 0.05 * height, cluster_n),
        rng.normal(cc, 0.05 * width, cluster_n),
    ])
    bg = np.column_stack([rng.uniform(0, height, bg_n), rng.uniform(0, width, bg_n)])
    case_points = np.clip(np.vstack([cluster, bg]), 0, [height - 1, width - 1])

    # 设施：两个固定点
    facilities = np.array([[0.15 * height, 0.8 * width], [0.85 * height, 0.2 * width]])

    cube = np.stack([population, env], axis=0).astype(np.float32)
    info = {"bbox": bbox, "width": width, "height": height,
            "band_roles": BAND_ROLES, "cluster_center_rc": [float(cr), float(cc)],
            "facilities_rc": facilities.tolist(), "n_cases": int(case_points.shape[0])}
    return cube, case_points, info


def case_points_to_kde_rate(case_points, population, height, width, bandwidth=3.0):
    """把病例点做 KDE 得到病例密度，再除以人口得发病率（供环境关联用）。"""
    kde = kde_grid(case_points, height, width, bandwidth)
    pop = np.clip(np.asarray(population, dtype=np.float32), 1.0, None)
    return (kde / pop).astype(np.float32)


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(path, cube, bbox, nodata=-9999.0, dtype="float32"):
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


def read_geotiff(path):
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return cube, bbox


def read_geotiff_full(path: str) -> Tuple[np.ndarray, List[float], Optional[float]]:
    """扩展版 read：同时返回 nodata 值（若无则为 None）。"""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nodata = src.nodata
        if nodata is not None:
            nodata = float(nodata)
    return cube, bbox, nodata


# ---------------------------------------------------------------------------
# 输入校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox: Optional[List[float]]) -> List[float]:
    """校验地理 bbox 合法性，失败抛 ValidationError（exit 6）。"""
    if bbox is None or len(bbox) != 4:
        raise ValidationError("bbox must be 4 floats [W S E N]")
    try:
        w, s, e, n = [float(x) for x in bbox]
    except (TypeError, ValueError) as exc:
        raise ValidationError(f"bbox entries must be numeric: {exc}")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(f"latitude out of [-90,90]: S={s}, N={n}")
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(f"longitude out of [-180,180]: W={w}, E={e}")
    if s >= n:
        raise ValidationError(
            f"S >= N (S={s}, N={n}); bbox inverted (S must be < N)"
        )
    if w >= e:
        raise ValidationError(
            f"W >= E (W={w}, E={e}); cross-180° bbox not supported. "
            f"Split into two non-antipodal bboxes."
        )
    if (e - w) < 0.001 or (n - s) < 0.001:
        raise ValidationError(
            f"bbox too small ({(e-w):.6f}°×{(n-s):.6f}°); min span is 0.001°"
        )
    return [w, s, e, n]


def write_manifest(output_dir, args, outputs, qa, started_at, exit_code, bbox,
                   input_nodata=None):
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME, skill_version=VERSION, command=cmd,
        started_at=started_at, finished_at=_utc_now(), exit_code=exit_code,
        inputs={"input": getattr(args, "input", None),
                "method": getattr(args, "method", None),
                "synthetic": bool(getattr(args, "synthetic", False)),
                "bbox": bbox, "input_nodata": input_nodata},
        outputs=[OutputFile(**o) for o in outputs], qa=qa,
        software={"python": sys.version.split()[0], "skill": SKILL_NAME},
    )
    path = os.path.join(output_dir, "output-manifest.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(man.to_dict(), f, ensure_ascii=False, indent=2, default=str)
    return path


def process(args):
    started_at = _utc_now()
    output_dir = args.output_dir
    bbox = list(args.bbox) if args.bbox else None

    # 校验 CLI 参数（前置）
    if args.bandwidth <= 0:
        raise ValidationError(
            f"--bandwidth must be > 0 (got {args.bandwidth})"
        )

    synth_info = None
    input_nodata: Optional[float] = None
    n_valid_pixels: Optional[int] = None
    if args.input and not args.synthetic:
        cube, file_bbox, src_nodata = read_geotiff_full(args.input)
        input_nodata = src_nodata
        if bbox is not None:
            bbox = validate_bbox(bbox)
        else:
            bbox = validate_bbox(file_bbox)
        # NoData 处理
        if src_nodata is not None:
            n_total = int(cube[0].size)
            n_nd = int(np.count_nonzero(cube[0] == src_nodata))
            n_valid_pixels = n_total - n_nd
            if n_valid_pixels == 0:
                raise ValidationError(
                    f"input raster has no valid pixels "
                    f"(all {n_nd}/{n_total} are NoData={src_nodata})",
                    path=args.input, nodata=src_nodata,
                )
            cube = np.where(cube == src_nodata, np.nan, cube).astype(np.float32)
        else:
            n_valid_pixels = int(cube[0].size)
        # 真实模式：用人口加权随机生成病例/设施（演示），保持离线
        rng = np.random.default_rng(0)
        h, w = cube.shape[1], cube.shape[2]
        case_points = np.column_stack([rng.uniform(0, h, 80), rng.uniform(0, w, 80)])
        facilities = np.array([[0.2 * h, 0.2 * w], [0.8 * h, 0.8 * w]])
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        bbox = validate_bbox(bbox)
        cube, case_points, synth_info = generate_synthetic_scene(bbox)
        facilities = np.array(synth_info["facilities_rc"])
        n_valid_pixels = int(cube[0].size)
        source_note = "synthetic"

    if cube.size == 0:
        raise ValidationError("input raster is empty")
    if cube.ndim != 3 or cube.shape[0] < N_REQUIRED_BANDS:
        raise ValidationError(
            f"input must have >= {N_REQUIRED_BANDS} bands ({BAND_ROLES}); got {cube.shape}")

    # 校验通过后再建输出目录
    os.makedirs(output_dir, exist_ok=True)

    population, env = cube[0], cube[1]
    _, h, w = cube.shape

    outputs = []
    qa: Dict[str, Any] = {
        "source": source_note, "method": args.method,
        "n_valid_pixels": int(n_valid_pixels) if n_valid_pixels is not None else None,
        "input_nodata": input_nodata,
    }

    if args.method in ("kde", "all"):
        kde = kde_grid(case_points, h, w, bandwidth=args.bandwidth)
        rate = case_points_to_kde_rate(case_points, population, h, w, args.bandwidth)
        out_kde = os.path.join(output_dir, "case_density.tif")
        write_geotiff(out_kde, kde, bbox)
        peak = np.unravel_index(np.argmax(kde), kde.shape)
        qa["kde_peak_rc"] = [int(peak[0]), int(peak[1])]
        qa["kde_max"] = float(kde.max())
        outputs.append({"path": out_kde, "kind": "raster", "crs_epsg": 4326,
                        "bbox_wgs84": bbox, "band_count": 1})
        _ = rate

    if args.method in ("scan", "all"):
        # 把栅格聚合成粗网格区域做扫描统计
        gh, gw = 16, 16
        bh, bw = h // gh, w // gw
        cases_grid = np.zeros(gh * gw)
        pop_grid = np.zeros(gh * gw)
        centroids = np.zeros((gh * gw, 2))
        for gi in range(gh):
            for gj in range(gw):
                idx = gi * gw + gj
                r0, r1 = gi * bh, min((gi + 1) * bh, h)
                c0, c1 = gj * bw, min((gj + 1) * bw, w)
                sub = case_points[(case_points[:, 0] >= r0) & (case_points[:, 0] < r1) &
                                  (case_points[:, 1] >= c0) & (case_points[:, 1] < c1)]
                cases_grid[idx] = len(sub)
                pop_grid[idx] = float(population[r0:r1, c0:c1].sum())
                centroids[idx] = [gi + 0.5, gj + 0.5]
        scan = spatial_scan(cases_grid, pop_grid, centroids, max_frac=0.5)
        qa["scan"] = {k: (float(v) if isinstance(v, (int, float, np.floating)) else v)
                      for k, v in scan.items()}
        scan_path = os.path.join(output_dir, "scan_result.json")
        with open(scan_path, "w", encoding="utf-8") as f:
            json.dump(scan, f, ensure_ascii=False, indent=2, default=float)
        outputs.append({"path": scan_path, "kind": "json"})

    # 环境关联（总是计算）
    rate_full = case_points_to_kde_rate(case_points, population, h, w, args.bandwidth)
    corr = pearson_corr(rate_full, env)
    qa["env_correlation"] = corr

    # 可达性
    fac_mask = np.zeros((h, w), dtype=bool)
    for fr, fc in facilities:
        fac_mask[int(np.clip(fr, 0, h - 1)), int(np.clip(fc, 0, w - 1))] = True
    acc = accessibility_distance(fac_mask, pixel_size=1.0)
    out_acc = os.path.join(output_dir, "accessibility.tif")
    write_geotiff(out_acc, acc, bbox)
    qa["mean_accessibility"] = float(acc[np.isfinite(acc)].mean())
    outputs.append({"path": out_acc, "kind": "raster", "crs_epsg": 4326,
                    "bbox_wgs84": bbox, "band_count": 1})

    report = {"source": source_note, "method": args.method, "env_correlation": corr,
              "qa": qa, "n_cases": int(case_points.shape[0])}
    report_path = os.path.join(output_dir, "health_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2, default=float)
    outputs.append({"path": report_path, "kind": "json"})

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox,
                              input_nodata=input_nodata)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}  method: {args.method}")
        if "kde_peak_rc" in qa:
            print(f"[{SKILL_NAME}] KDE peak (row,col): {qa['kde_peak_rc']}  max: {qa['kde_max']:.4f}")
        if "scan" in qa:
            print(f"[{SKILL_NAME}] scan LLR: {qa['scan']['llr']:.3f}  RR: {qa['scan']['rr']:.3f}")
        print(f"[{SKILL_NAME}] env correlation: {corr:.3f}")
        print(f"[{SKILL_NAME}] mean accessibility: {qa['mean_accessibility']:.2f} px")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser():
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Public health spatial analysis: KDE, spatial scan, environment "
                    "association and accessibility.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"))
    p.add_argument("--input", help="input multi-band GeoTIFF (population/environment)")
    p.add_argument("--synthetic", action="store_true")
    p.add_argument("--method", default="all", choices=METHODS,
                   help="analysis method (default: all)")
    p.add_argument("--bandwidth", type=float, default=3.0, help="KDE bandwidth in pixels (default: 3)")
    p.add_argument("--output-dir", default="./output")
    p.add_argument("--quiet", action="store_true")
    p.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    return p


def main(argv=None):
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
