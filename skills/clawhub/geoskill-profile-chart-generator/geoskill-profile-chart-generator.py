#!/usr/bin/env python3
"""profile-chart-generator — 剖面图生成器

沿用户给定的折线路径对 DEM 做等距重采样，用双线性内插逐点提取高程，
计算累计地面距离，输出 matplotlib 剖面图（PNG）与 CSV / JSON 采样表。
采样点数由“路径长度 / 采样间隔”自动确定，保证与路径长度一致。

数据源：本地 DEM GeoTIFF，或 ``--synthetic`` 生成模拟 DEM 用于离线测试。

隐私声明 / Privacy：完全离线；所有处理本地完成，不上传用户数据。

Usage:
    python profile-chart-generator.py --input dem.tif --vertices "116.0,39.0" "116.5,39.8"
    python profile-chart-generator.py --bbox 116 39 117 40 --synthetic --interval 500

License: MIT
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import sys
from typing import Any, Dict, List, Optional, Sequence, Tuple

import numpy as np

VERSION = "1.0.0"
SKILL_NAME = "profile-chart-generator"

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


M_PER_DEG = 111320.0  # 赤道每经/纬度约米数


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# 核心算法：路径几何
# ---------------------------------------------------------------------------
def segment_lengths_m(vertices: np.ndarray, ref_lat: Optional[float] = None) -> np.ndarray:
    """各段地面长度（米），等距圆柱近似（经度按参考纬度缩放）。"""
    v = np.asarray(vertices, dtype=float)
    if v.shape[0] < 2:
        raise UsageError("need at least 2 vertices")
    if ref_lat is None:
        ref_lat = float(np.mean(v[:, 1]))
    kx = M_PER_DEG * np.cos(np.deg2rad(ref_lat))
    ky = M_PER_DEG
    dx = np.diff(v[:, 0]) * kx
    dy = np.diff(v[:, 1]) * ky
    return np.sqrt(dx ** 2 + dy ** 2)


def path_length_m(vertices: np.ndarray, ref_lat: Optional[float] = None) -> float:
    return float(np.sum(segment_lengths_m(vertices, ref_lat)))


def samples_from_interval(length_m: float, interval_m: float) -> int:
    """由路径长度与采样间隔确定采样点数：ceil(L/d)+1（>=2）。"""
    if interval_m <= 0:
        raise UsageError("interval must be > 0", interval=interval_m)
    return max(2, int(np.ceil(length_m / interval_m)) + 1)


def resample_path(vertices: np.ndarray, n: int) -> Tuple[np.ndarray, float]:
    """把折线按等弧长重采样为 n 个点（经纬度）。返回 (points(n,2), total_m)。

    重采样在“米制弧长”参数上进行，保证相邻点地面间距一致。
    """
    v = np.asarray(vertices, dtype=float)
    if v.shape[0] < 2:
        raise UsageError("need at least 2 vertices")
    if n < 2:
        raise UsageError("n must be >= 2", n=int(n))
    seg = segment_lengths_m(v)
    total = float(np.sum(seg))
    if total <= 0:
        return np.repeat(v[:1], n, axis=0), 0.0
    cum = np.concatenate([[0.0], np.cumsum(seg)])
    s = np.linspace(0.0, total, n)
    lon = np.interp(s, cum, v[:, 0])
    lat = np.interp(s, cum, v[:, 1])
    return np.stack([lon, lat], axis=1), total


# ---------------------------------------------------------------------------
# 核心算法：栅格双线性采样
# ---------------------------------------------------------------------------
def bilinear_sample(raster: np.ndarray, bbox: Sequence[float],
                    x: float, y: float) -> float:
    """在 bbox 配准的栅格上对地理坐标 (x=lon, y=lat) 做双线性内插。

    配准约定同 rasterio.from_bounds：像元中心位于 (i+0.5)。
    对线性平面（z = a*x + b*y）内插结果精确等于真值。
    """
    w, s, e, n = bbox
    h, wpx = raster.shape
    pw = (e - w) / wpx
    ph = (n - s) / h
    col = (x - w) / pw - 0.5
    row = (n - y) / ph - 0.5
    c0 = int(np.floor(col)); r0 = int(np.floor(row))
    dc = col - c0; dr = row - r0
    c0c = min(max(c0, 0), wpx - 1); c1c = min(max(c0 + 1, 0), wpx - 1)
    r0c = min(max(r0, 0), h - 1); r1c = min(max(r0 + 1, 0), h - 1)
    v00 = raster[r0c, c0c]; v01 = raster[r0c, c1c]
    v10 = raster[r1c, c0c]; v11 = raster[r1c, c1c]
    top = (1 - dc) * v00 + dc * v01
    bot = (1 - dc) * v10 + dc * v11
    return float((1 - dr) * top + dr * bot)


def extract_profile(raster: np.ndarray, bbox: Sequence[float],
                    points: np.ndarray) -> np.ndarray:
    """沿点序列提取栅格值，返回与 points 等长的值数组。"""
    pts = np.asarray(points, dtype=float)
    out = np.array([bilinear_sample(raster, bbox, x, y) for x, y in pts],
                   dtype=np.float32)
    return out


# ---------------------------------------------------------------------------
# 绘图 / 表格
# ---------------------------------------------------------------------------
def render_profile_png(dist_m: np.ndarray, values: np.ndarray, title: str) -> bytes:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(9, 4.5), dpi=110)
    d_km = dist_m / 1000.0
    ax.fill_between(d_km, values, values.min(), color="#cfe3f5", alpha=0.6)
    ax.plot(d_km, values, color="#1f5f9f", linewidth=1.6)
    ax.set_xlabel("Distance (km)")
    ax.set_ylabel("Elevation (m)")
    ax.set_title(title)
    ax.grid(True, linestyle=":", alpha=0.5)
    fig.tight_layout()
    import io
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=110)
    plt.close(fig)
    return buf.getvalue()


def write_profile_csv(path: str, dist_m: np.ndarray, points: np.ndarray,
                      values: np.ndarray) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write("index,distance_m,lon,lat,value\n")
        for i in range(len(values)):
            f.write(f"{i},{dist_m[i]:.2f},{points[i, 0]:.6f},{points[i, 1]:.6f},"
                    f"{values[i]:.4f}\n")


# ---------------------------------------------------------------------------
# 合成数据：沿对角线升高的 DEM（便于剖面单调性校验）
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], width: int = 64, height: int = 64,
                       seed: int = 42) -> Tuple[np.ndarray, Dict[str, Any]]:
    rng = np.random.default_rng(seed)
    w, s, e, n = bbox
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    xx /= max(width - 1, 1); yy /= max(height - 1, 1)
    hill = 600.0 * np.exp(-(((xx - 0.5) ** 2 + (yy - 0.5) ** 2) / 0.03))
    base = 100.0 + 300.0 * xx
    noise = rng.normal(0, 4.0, size=(height, width)).astype(np.float32)
    dem = (base + hill + noise).astype(np.float32)
    info = {"bbox": bbox, "width": width, "height": height,
            "min_elev": float(dem.min()), "max_elev": float(dem.max()),
            "kind": "synthetic-dem"}
    return dem, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(path, cube, bbox, nodata=-9999.0):
    import rasterio
    from rasterio.transform import from_bounds
    if cube.ndim == 2:
        cube = cube[np.newaxis, ...]
    nb, h, w = cube.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    profile = {"driver": "GTiff", "height": h, "width": w, "count": nb,
               "dtype": "float32", "crs": "EPSG:4326", "transform": transform,
               "nodata": nodata, "compress": "deflate"}
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(cube[b].astype("float32"), b + 1)


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


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------
def write_manifest(output_dir, args, outputs, qa, started_at, exit_code, bbox,
                   input_nodata=None):
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME, skill_version=VERSION, command=cmd,
        started_at=started_at, finished_at=_utc_now(), exit_code=exit_code,
        inputs={"input": getattr(args, "input", None),
                "interval": getattr(args, "interval", None),
                "samples": getattr(args, "samples", None),
                "synthetic": bool(getattr(args, "synthetic", False)),
                "input_nodata": input_nodata},
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
def parse_vertices(items: List[str]) -> np.ndarray:
    pts = []
    for it in items:
        parts = it.replace(",", " ").split()
        if len(parts) != 2:
            raise UsageError(f"vertex '{it}' must be 'lon,lat'", vertex=it)
        pts.append([float(parts[0]), float(parts[1])])
    return np.asarray(pts, dtype=float)


def process(args: argparse.Namespace) -> int:
    started_at = _utc_now()
    output_dir = args.output_dir
    bbox = list(args.bbox) if args.bbox else None

    # 校验 samples 参数
    if getattr(args, "samples", 0) and int(args.samples) < 2:
        raise UsageError(
            f"--samples must be >= 2 (got {args.samples})", samples=int(args.samples)
        )

    synth_info: Optional[Dict[str, Any]] = None
    input_nodata: Optional[float] = None
    n_valid_pixels: Optional[int] = None
    if args.input and not args.synthetic:
        cube, file_bbox, src_nodata = read_geotiff_full(args.input)
        input_nodata = src_nodata
        # 若 CLI 同时给 --bbox，先校验之；否则用文件 bbox
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
        dem = cube[0]
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        bbox = validate_bbox(bbox)
        dem, synth_info = generate_synthetic(bbox)
        n_valid_pixels = int(dem.size)
        source_note = "synthetic"

    if dem.size == 0:
        raise ValidationError("input raster is empty")
    if bbox is None:
        raise UsageError("could not determine bbox")

    # 校验通过后再建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 确定路径顶点
    if args.vertices:
        vertices = parse_vertices(args.vertices)
    else:
        # 默认沿 bbox 对角线
        vertices = np.array([[bbox[0], bbox[1]], [bbox[2], bbox[3]]], dtype=float)

    length_m = path_length_m(vertices)
    if args.samples:
        n = max(2, int(args.samples))
        interval_used = length_m / (n - 1)
    else:
        n = samples_from_interval(length_m, args.interval)
        interval_used = args.interval

    points, total = resample_path(vertices, n)
    values = extract_profile(dem, bbox, points)
    # 累计距离（米）
    seg = segment_lengths_m(points)
    dist_m = np.concatenate([[0.0], np.cumsum(seg)])

    png_bytes = render_profile_png(dist_m, values, args.title)
    png_path = os.path.join(output_dir, "profile.png")
    with open(png_path, "wb") as f:
        f.write(png_bytes)

    csv_path = os.path.join(output_dir, "profile.csv")
    write_profile_csv(csv_path, dist_m, points, values)

    # 可验证产物：采样 JSON + DEM 栅格
    prof_json = {"source": source_note, "bbox": bbox, "n_samples": int(n),
                 "path_length_m": length_m, "interval_m": interval_used,
                 "value_min": float(np.nanmin(values)), "value_max": float(np.nanmax(values)),
                 "gain": float(values[-1] - values[0]),
                 "samples": [{"distance_m": float(dist_m[i]), "lon": float(points[i, 0]),
                              "lat": float(points[i, 1]), "value": float(values[i])}
                             for i in range(n)],
                 "generated_at": _utc_now()}
    if synth_info is not None:
        prof_json["synthetic"] = synth_info
    json_path = os.path.join(output_dir, "profile.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(prof_json, f, ensure_ascii=False, indent=2)

    dem_tif = os.path.join(output_dir, "profile_dem.tif")
    write_geotiff(dem_tif, dem.astype(np.float32), bbox)

    qa = {"source": source_note, "n_samples": int(n), "path_length_m": length_m,
          "interval_m": interval_used, "value_min": prof_json["value_min"],
          "value_max": prof_json["value_max"], "bbox": bbox,
          "n_valid_pixels": int(n_valid_pixels) if n_valid_pixels is not None else None,
          "input_nodata": input_nodata}
    outputs = [
        {"path": png_path, "kind": "text"},
        {"path": csv_path, "kind": "table", "row_count": int(n)},
        {"path": json_path, "kind": "json"},
        {"path": dem_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox,
                              input_nodata=input_nodata)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] path length: {length_m:.1f} m  samples: {n}  interval: {interval_used:.1f} m")
        print(f"[{SKILL_NAME}] elevation: [{prof_json['value_min']:.1f}, {prof_json['value_max']:.1f}]  gain: {prof_json['gain']:.1f}")
        print(f"[{SKILL_NAME}] png: {png_path}  csv: {csv_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Extract an elevation profile along a path and render a chart + CSV.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"))
    p.add_argument("--input", help="input DEM GeoTIFF")
    p.add_argument("--vertices", nargs="+", default=None,
                   help='path vertices as "lon,lat" pairs (default: bbox diagonal)')
    p.add_argument("--interval", type=float, default=500.0,
                   help="sampling interval in meters (default: 500)")
    p.add_argument("--samples", type=int, default=0,
                   help="override sample count (0 = derive from interval)")
    p.add_argument("--title", default="Elevation Profile")
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
