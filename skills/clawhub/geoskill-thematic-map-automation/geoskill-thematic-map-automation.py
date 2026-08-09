#!/usr/bin/env python3
"""thematic-map-automation — 专题地图自动化

自动生成三类专题地图：**分级色彩**（choropleth）、**比率符号**（proportional
symbol）、**点值法**（dot density）。内置三种统计分类（等间距 / 分位数 /
Jenks 自然断点），用 matplotlib 完成图例 + 边框整饰，输出 PNG 与矢量 PDF。

数据源：本地矢量（GeoJSON / Shapefile，含数值字段），或 ``--synthetic`` 生成
规则格网多边形 + 空间渐变属性用于离线测试。

隐私声明 / Privacy：完全离线；所有处理本地完成，不上传用户数据。

Usage:
    python thematic-map-automation.py --input regions.geojson --field pop --symbol choropleth
    python thematic-map-automation.py --bbox 116 39 117 40 --synthetic --classes 5

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
SKILL_NAME = "thematic-map-automation"

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


CLASSIFY_METHODS = ["equal_interval", "quantile", "jenks"]
SYMBOLS = ["choropleth", "proportional", "dot"]
CMAPS = ["YlOrRd", "YlGnBu", "viridis", "plasma", "Reds", "Blues", "Spectral"]


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# bbox validation
# ---------------------------------------------------------------------------
def validate_bbox(bbox, *, kind: str = "bbox"):
    """校验 W<S<E<N、lat∈[-90,90]、lon∈[-180,180]、跨 180° 单独报错。

    返回 [W, S, E, N]。失败抛 ValidationError (rc=6)。
    """
    if bbox is None:
        raise ValidationError(f"{kind} is required")
    if len(bbox) != 4:
        raise ValidationError(f"{kind} must have 4 floats [W S E N], got {len(bbox)}",
                              bbox=list(bbox))
    w, s, e, n = (float(x) for x in bbox)
    if not all(np.isfinite(v) for v in (w, s, e, n)):
        raise ValidationError(f"{kind} contains non-finite values", bbox=[w, s, e, n])
    if w == e or s == n:
        raise ValidationError(f"{kind} has zero area: W==E or S==N", bbox=[w, s, e, n])
    if w > e:
        raise ValidationError(
            f"{kind} crosses the 180° meridian (W={w} > E={e}); "
            "please split into two sub-bboxes or shift longitudes",
            bbox=[w, s, e, n],
        )
    if s > n:
        raise ValidationError(f"{kind} has S > N (S={s} > N={n})", bbox=[w, s, e, n])
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"{kind} latitude out of range [-90, 90]: S={s}, N={n}",
            bbox=[w, s, e, n],
        )
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"{kind} longitude out of range [-180, 180]: W={w}, E={e}",
            bbox=[w, s, e, n],
        )
    return [w, s, e, n]


# ---------------------------------------------------------------------------
# 核心算法：统计分类
# ---------------------------------------------------------------------------
def jenks_breaks(data: np.ndarray, n_classes: int) -> List[float]:
    """Fisher-Jenks 自然断点（一维 DP 最优分割）。

    返回 n_classes+1 个升序断点（含 min/max）。使类内离差平方和最小，
    在双峰数据上断点会落在两簇之间的空隙。
    """
    arr = sorted(float(x) for x in data if np.isfinite(x))
    n = len(arr)
    if n == 0:
        return [0.0] * (n_classes + 1)
    if n <= n_classes:
        edges = [arr[0]] + arr + [arr[-1]]
        edges = sorted(set(edges))
        while len(edges) < n_classes + 1:
            edges.append(edges[-1])
        return edges[: n_classes + 1]

    mat1 = [[0] * (n_classes + 1) for _ in range(n + 1)]
    mat2 = [[float("inf")] * (n_classes + 1) for _ in range(n + 1)]
    for i in range(1, n_classes + 1):
        mat1[1][i] = 1
        mat2[1][i] = 0.0
        for j in range(2, n + 1):
            mat2[j][i] = float("inf")
    v = 0.0
    for ell in range(2, n + 1):
        s1 = s2 = 0.0
        w = 0
        for m in range(1, ell + 1):
            i3 = ell - m + 1
            val = float(arr[i3 - 1])
            s2 += val * val
            s1 += val
            w += 1
            v = s2 - (s1 * s1) / w
            i4 = i3 - 1
            if i4 != 0:
                for j in range(2, n_classes + 1):
                    if mat2[ell][j] >= (v + mat2[i4][j - 1]):
                        mat1[ell][j] = i3
                        mat2[ell][j] = v + mat2[i4][j - 1]
        mat1[ell][1] = 1
        mat2[ell][1] = v

    kclass = [0.0] * (n_classes + 1)
    kclass[n_classes] = arr[n - 1]
    kclass[0] = arr[0]
    k = n
    count = n_classes
    while count >= 2:
        idx = int(mat1[k][count])
        kclass[count - 1] = arr[idx - 2]
        k = idx - 1
        count -= 1
    edges = sorted(set(kclass))
    while len(edges) < n_classes + 1:
        edges.append(edges[-1])
    return edges[: n_classes + 1]


def classify(values: np.ndarray, method: str = "quantile", n_classes: int = 5) -> List[float]:
    """返回 n_classes+1 个升序分类断点（含全局 min/max）。"""
    if method not in CLASSIFY_METHODS:
        raise UsageError(f"unknown method '{method}'. Choose: {CLASSIFY_METHODS}", method=method)
    if n_classes < 2:
        raise UsageError("n_classes must be >= 2", n_classes=n_classes)
    v = np.asarray([float(x) for x in values if np.isfinite(x)])
    if v.size == 0:
        return [0.0] * (n_classes + 1)
    if method == "equal_interval":
        edges = np.linspace(float(v.min()), float(v.max()), n_classes + 1)
    elif method == "quantile":
        edges = np.percentile(v, np.linspace(0, 100, n_classes + 1))
    else:  # jenks
        edges = np.array(jenks_breaks(v, n_classes))
    edges = np.sort(np.asarray(edges, dtype=float))
    # 确保端点为全局 min/max
    edges[0] = float(v.min())
    edges[-1] = float(v.max())
    return [float(x) for x in edges]


def assign_class(values: np.ndarray, edges: List[float]) -> np.ndarray:
    """把数值按断点分配为类别索引 [0, n_classes-1]。"""
    edges_arr = np.asarray(edges, dtype=float)
    n = len(edges_arr) - 1
    idx = np.searchsorted(edges_arr, values, side="right") - 1
    return np.clip(idx, 0, max(n - 1, 0)).astype(int)


# ---------------------------------------------------------------------------
# 核心算法：比率符号 & 点值
# ---------------------------------------------------------------------------
def proportional_sizes(values: np.ndarray, max_size: float = 800.0) -> np.ndarray:
    """面积正比于数值的符号大小（点面积 ∝ value，故半径 ∝ sqrt(value)）。

    返回 matplotlib scatter 的 size（points^2，即面积）。
    """
    v = np.asarray(values, dtype=float)
    vmax = float(np.nanmax(v)) if np.any(np.isfinite(v)) else 0.0
    if vmax <= 0:
        return np.zeros_like(v)
    return np.clip(v / vmax, 0.0, 1.0) * float(max_size)


def dot_counts(values: np.ndarray, value_per_dot: float) -> np.ndarray:
    """每个单元的点数 = round(value / value_per_dot)。"""
    if value_per_dot <= 0:
        raise UsageError("value_per_dot must be > 0", value_per_dot=value_per_dot)
    v = np.asarray(values, dtype=float)
    return np.clip(np.round(v / value_per_dot), 0, None).astype(int)


def random_points_in_polygon(poly, n: int, rng) -> List[Tuple[float, float]]:
    """在多边形内拒绝采样 n 个点。"""
    from shapely.geometry import Point
    if n <= 0:
        return []
    minx, miny, maxx, maxy = poly.bounds
    pts: List[Tuple[float, float]] = []
    tries = 0
    max_tries = n * 80 + 200
    while len(pts) < n and tries < max_tries:
        x = rng.uniform(minx, maxx)
        y = rng.uniform(miny, maxy)
        if poly.contains(Point(x, y)):
            pts.append((x, y))
        tries += 1
    return pts


# ---------------------------------------------------------------------------
# 渲染
# ---------------------------------------------------------------------------
def render_thematic(gdf, edges, cmap_name, symbol, value_per_dot, seed, title):
    """用 matplotlib 渲染专题地图，返回 fig（调用方保存为 png/pdf）。"""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.colors as mcolors

    gdf = gdf.copy()
    gdf["_class"] = assign_class(gdf["value"].to_numpy(), edges)
    n_classes = len(edges) - 1
    cmap = matplotlib.colormaps[cmap_name]

    fig, ax = plt.subplots(figsize=(8, 8), dpi=110)
    if symbol == "choropleth":
        norm = mcolors.Normalize(vmin=0, vmax=max(n_classes - 1, 1))
        gdf.plot(column="_class", categorical=True, ax=ax, cmap=cmap_name,
                 edgecolor="white", linewidth=0.4, legend=True,
                 legend_kwds={"loc": "lower left", "frameon": True,
                              "title": "class"})
    else:
        gdf.plot(ax=ax, color="#e8e8e8", edgecolor="#999999", linewidth=0.4)
        cx = gdf.geometry.centroid.x.to_numpy()
        cy = gdf.geometry.centroid.y.to_numpy()
        if symbol == "proportional":
            sizes = proportional_sizes(gdf["value"].to_numpy())
            ax.scatter(cx, cy, s=sizes, cmap=cmap, c=gdf["value"].to_numpy(),
                       edgecolor="black", linewidth=0.3, alpha=0.8)
        else:  # dot
            rng = np.random.default_rng(seed)
            counts = dot_counts(gdf["value"].to_numpy(), value_per_dot)
            for poly, nd in zip(gdf.geometry, counts):
                pts = random_points_in_polygon(poly, int(nd), rng)
                if pts:
                    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
                    ax.plot(xs, ys, ".", color="#1a4f8a", markersize=2.5)

    ax.set_title(title)
    ax.set_xlabel("Longitude"); ax.set_ylabel("Latitude")
    ax.set_aspect("equal")
    fig.tight_layout()
    return fig


# ---------------------------------------------------------------------------
# 合成数据：规则格网多边形 + 空间渐变属性
# ---------------------------------------------------------------------------
def generate_synthetic(bbox, nx=8, ny=8, seed=42):
    from shapely.geometry import box
    import geopandas as gpd
    w, s, e, n = bbox
    dx = (e - w) / nx; dy = (n - s) / ny
    rng = np.random.default_rng(seed)
    polys, vals = [], []
    for j in range(ny):
        for i in range(nx):
            x0 = w + i * dx; y0 = s + j * dy
            polys.append(box(x0, y0, x0 + dx, y0 + dy))
            v = 5.0 + 6.0 * i + 4.0 * j + rng.normal(0, 1.5)
            vals.append(max(0.1, float(v)))
    gdf = gpd.GeoDataFrame({"value": vals, "geometry": polys}, crs="EPSG:4326")
    return gdf


def read_vector(path):
    import geopandas as gpd
    if not os.path.exists(path):
        raise UsageError(f"input vector not found: {path}", path=path)
    return gpd.read_file(path)


# ---------------------------------------------------------------------------
# GeoTIFF I/O（产出分类栅格作为可验证产物）
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
        inputs={"input": getattr(args, "input", None),
                "method": getattr(args, "method", None),
                "symbol": getattr(args, "symbol", None),
                "synthetic": bool(getattr(args, "synthetic", False))},
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

    synth = False
    if args.input and not args.synthetic:
        gdf = read_vector(args.input)
        field = args.field
        if field is None:
            num_cols = [c for c in gdf.columns
                        if c != "geometry" and np.issubdtype(gdf[c].dtype, np.number)]
            if not num_cols:
                raise ValidationError("input vector has no numeric field; use --field")
            field = num_cols[0]
        if field not in gdf.columns:
            raise UsageError(f"field '{field}' not found in input", field=field)
        gdf = gdf.rename(columns={field: "value"})[["value", "geometry"]]
        b = gdf.total_bounds  # [minx, miny, maxx, maxy]
        bbox = bbox if bbox is not None else [float(b[0]), float(b[1]), float(b[2]), float(b[3])]
        bbox = validate_bbox(bbox, kind="--bbox/--input bbox")
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <vector>")
        bbox = validate_bbox(bbox, kind="--bbox")
        gdf = generate_synthetic(bbox)
        synth = True
        source_note = "synthetic"

    if len(gdf) == 0:
        raise ValidationError("input has no features")

    # NaN 处理：把不可用值（NaN/inf）独立标记，分类时仅用有效值
    raw_values = gdf["value"].to_numpy(dtype=float)
    valid_mask = np.isfinite(raw_values)
    n_total = int(raw_values.size)
    n_valid = int(valid_mask.sum())
    if n_valid == 0:
        raise ValidationError(
            f"input field has no valid (finite) values (n={n_total})",
            n_features=n_total,
        )
    if n_valid < n_total:
        # 提示但不阻塞：synthetic 模式不应该触发
        if not synth:
            print(f"[{SKILL_NAME}] note: {n_total - n_valid}/{n_total} features have non-finite values; "
                  f"will be marked as class=-1 (nodata)", file=sys.stderr)

    # 校验通过后再建目录（失败时不留空目录）
    os.makedirs(output_dir, exist_ok=True)

    values = raw_values[valid_mask]
    edges = classify(values, method=args.method, n_classes=args.classes)
    # assign_class 对全 array：有效值按断点分箱；非有效值强制 class=-1
    valid_classes = assign_class(values, edges)
    classes = np.full(n_total, -1, dtype=int)
    classes[valid_mask] = valid_classes
    gdf_out = gdf.copy()
    gdf_out["class"] = classes

    # 渲染 PNG + PDF
    fig = render_thematic(gdf_out, edges, args.cmap, args.symbol,
                          args.value_per_dot, args.seed, args.title)
    png_path = os.path.join(output_dir, "thematic_map.png")
    pdf_path = os.path.join(output_dir, "thematic_map.pdf")
    fig.savefig(png_path, dpi=110)
    fig.savefig(pdf_path, format="pdf")
    import matplotlib.pyplot as plt
    plt.close(fig)

    # 矢量产物（带 class 字段）
    geojson_path = os.path.join(output_dir, "classified.geojson")
    gdf_out.to_file(geojson_path, driver="GeoJSON")

    # 可验证栅格产物：把分类结果栅格化到 bbox（NoData 像素写 -1，nodata=-1.0）
    cls_raster = rasterize_classes(gdf_out, bbox, 64, 64)
    tif_path = os.path.join(output_dir, "class_raster.tif")
    write_geotiff(tif_path, cls_raster.astype(np.float32), bbox, nodata=-1.0)

    # meta/qa 仅基于有效值
    meta = {"source": source_note, "method": args.method, "symbol": args.symbol,
            "cmap": args.cmap, "n_classes": args.classes, "edges": edges,
            "value_min": float(np.min(values)), "value_max": float(np.max(values)),
            "value_mean": float(np.mean(values)), "n_features": int(len(gdf)),
            "n_valid_features": n_valid, "n_invalid_features": n_total - n_valid,
            "bbox": bbox, "generated_at": _utc_now()}
    meta_path = os.path.join(output_dir, "thematic_meta.json")
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    used_classes = set(classes.tolist())
    used_classes.discard(-1)
    qa = {"source": source_note, "method": args.method, "symbol": args.symbol,
          "n_features": int(len(gdf)), "n_classes": int(len(used_classes)),
          "n_valid_features": n_valid, "n_invalid_features": n_total - n_valid,
          "edges": edges, "bbox": bbox}
    outputs = [
        {"path": png_path, "kind": "text"},
        {"path": pdf_path, "kind": "text"},
        {"path": geojson_path, "kind": "vector", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "feature_count": int(len(gdf_out))},
        {"path": tif_path, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": meta_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}  features: {len(gdf)}")
        print(f"[{SKILL_NAME}] method: {args.method}  symbol: {args.symbol}  classes: {args.classes}")
        print(f"[{SKILL_NAME}] edges: {[round(e,2) for e in edges]}")
        print(f"[{SKILL_NAME}] png: {png_path}")
        print(f"[{SKILL_NAME}] pdf: {pdf_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def rasterize_classes(gdf, bbox, width, height):
    """把多边形 class 字段栅格化：每个像元取其中心点所在多边形的 class。"""
    from shapely.geometry import Point
    w, s, e, n = bbox
    out = np.full((height, width), -1, dtype=np.int32)
    polys = list(gdf.geometry)
    cls = gdf["class"].to_numpy()
    xs = np.linspace(w, e, width + 1)
    ys = np.linspace(n, s, height + 1)  # 行从上到下
    for r in range(height):
        cy = 0.5 * (ys[r] + ys[r + 1])
        for c in range(width):
            cx = 0.5 * (xs[c] + xs[c + 1])
            pt = Point(cx, cy)
            for k, poly in enumerate(polys):
                if poly.contains(pt):
                    out[r, c] = int(cls[k]); break
    return out


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Automate thematic maps: choropleth, proportional symbol, dot density.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"))
    p.add_argument("--input", help="input vector (GeoJSON/Shapefile) with a numeric field")
    p.add_argument("--field", help="numeric field to map (default: first numeric column)")
    p.add_argument("--method", default="quantile", choices=CLASSIFY_METHODS)
    p.add_argument("--classes", type=int, default=5, help="number of classes (default: 5)")
    p.add_argument("--symbol", default="choropleth", choices=SYMBOLS)
    p.add_argument("--cmap", default="YlOrRd", choices=CMAPS)
    p.add_argument("--value-per-dot", type=float, default=5.0,
                   help="value represented by one dot (dot density)")
    p.add_argument("--title", default="Thematic Map")
    p.add_argument("--seed", type=int, default=42)
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
