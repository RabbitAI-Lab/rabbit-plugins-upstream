#!/usr/bin/env python3
"""crs-transformation — 坐标系转换

基于 pyproj 的坐标参考系（CRS）转换工具：

- **EPSG 转换**：任意 EPSG 代码之间的严格转换（如 WGS84 4326 ↔ Web
  Mercator 3857），底层使用 PROJ 的 ``Transformer``，支持往返一致。
- **中国常用坐标系互转**：内置 WGS-84（GPS）↔ GCJ-02（火星坐标，高德/
  腾讯）↔ BD-09（百度）的解析公式（国测局加偏算法），并提供迭代反算的
  GCJ-02 → WGS-84。
- **矢量要素转换**：把整个 GeoDataFrame 的几何从源 CRS 转到目标 CRS。

数据源：本地矢量/点集（``--input``），或 ``--synthetic`` 模式在 bbox 内生成
随机点用于离线测试。

隐私声明 / Privacy：
- 默认完全离线运行，``--synthetic`` 模式不读取任何外部数据。
- 所有处理在本地完成，不上传用户数据。

Usage:
    python crs-transformation.py --input pts.geojson --from EPSG:4326 --to EPSG:3857
    python crs-transformation.py --bbox 116 39 117 40 --synthetic --system gcj02 --output-dir ./out

License: MIT
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import math
import os
import sys
from typing import Any, Dict, List, Optional, Sequence, Tuple

import numpy as np

VERSION = "1.0.0"
SKILL_NAME = "crs-transformation"

# ---- 中国坐标系加偏算法常量（公开算法，克拉索夫斯基椭球）----
_A = 6378245.0               # 长半轴
_EE = 0.00669342162296594323  # 偏心率平方

SYSTEMS = {"wgs84", "gcj02", "bd09"}

# ---- 共享核心库（本地 vendored，随脚本目录一起分发）----
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
# 输入校验：bbox（共用同 animated-map-series 模板）
# ---------------------------------------------------------------------------
def validate_bbox(bbox: List[float]) -> None:
    """Validate a [W, S, E, N] bbox in WGS-84.

    Raises ValidationError (exit 6) for:
      - wrong length
      - non-finite values
      - longitude out of [-180, 180]
      - latitude  out of [-90, 90]
      - W >= E (would make a non-positive-width raster)
      - S >= N
    """
    if bbox is None or len(bbox) != 4:
        raise ValidationError(
            f"bbox must have 4 floats [W S E N], got {bbox!r}",
        )
    w, s, e, n = bbox
    vals = [w, s, e, n]
    if not all(np.isfinite(vals)):
        raise ValidationError(f"bbox contains non-finite values: {vals}")
    if not (-180.0 <= w <= 180.0) or not (-180.0 <= e <= 180.0):
        raise ValidationError(
            f"longitude out of [-180, 180]: W={w}, E={e}",
        )
    if not (-90.0 <= s <= 90.0) or not (-90.0 <= n <= 90.0):
        raise ValidationError(
            f"latitude out of [-90, 90]: S={s}, N={n}",
        )
    if w >= e:
        raise ValidationError(
            f"bbox W must be < E (W={w}, E={e}); cross-180 not supported; "
            f"split into two bboxes at the dateline",
        )
    if s >= n:
        raise ValidationError(
            f"bbox S must be < N (S={s}, N={n})",
        )
    if (e - w) < 1e-9 or (n - s) < 1e-9:
        raise ValidationError(
            f"bbox extent too small (W={w}, E={e}, S={s}, N={n})",
        )


# ---------------------------------------------------------------------------
# EPSG 转换（pyproj）
# ---------------------------------------------------------------------------
def make_transformer(from_crs: str, to_crs: str, always_xy: bool = True) -> Any:
    from pyproj import CRS, Transformer
    try:
        src = CRS.from_user_input(from_crs)
        dst = CRS.from_user_input(to_crs)
    except Exception as exc:  # noqa: BLE001
        raise UsageError(f"invalid CRS ({from_crs} -> {to_crs}): {exc}") from exc
    return Transformer.from_crs(src, dst, always_xy=always_xy)


def transform_points(
    xs: Sequence[float], ys: Sequence[float], transformer: Any
) -> Tuple[np.ndarray, np.ndarray]:
    """用已建好的 transformer 转换点集（lon/lat 顺序，always_xy）。"""
    xs = np.asarray(xs, dtype=np.float64)
    ys = np.asarray(ys, dtype=np.float64)
    ox, oy = transformer.transform(xs, ys)
    return np.asarray(ox, dtype=np.float64), np.asarray(oy, dtype=np.float64)


# ---------------------------------------------------------------------------
# WGS-84 / GCJ-02 / BD-09 互转（解析公式）
# ---------------------------------------------------------------------------
def _out_of_china(lon: float, lat: float) -> bool:
    return not (72.004 <= lon <= 137.8347 and 0.8293 <= lat <= 55.8271)


def _transform_lat(x: float, y: float) -> float:
    ret = (-100.0 + 2.0 * x + 3.0 * y + 0.2 * y * y
           + 0.1 * x * y + 0.2 * math.sqrt(abs(x)))
    ret += (20.0 * math.sin(6.0 * x * math.pi)
            + 20.0 * math.sin(2.0 * x * math.pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(y * math.pi)
            + 40.0 * math.sin(y / 3.0 * math.pi)) * 2.0 / 3.0
    ret += (160.0 * math.sin(y / 12.0 * math.pi)
            + 320.0 * math.sin(y * math.pi / 30.0)) * 2.0 / 3.0
    return ret


def _transform_lon(x: float, y: float) -> float:
    ret = (300.0 + x + 2.0 * y + 0.1 * x * x
           + 0.1 * x * y + 0.1 * math.sqrt(abs(x)))
    ret += (20.0 * math.sin(6.0 * x * math.pi)
            + 20.0 * math.sin(2.0 * x * math.pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(x * math.pi)
            + 40.0 * math.sin(x / 3.0 * math.pi)) * 2.0 / 3.0
    ret += (150.0 * math.sin(x / 12.0 * math.pi)
            + 300.0 * math.sin(x / 30.0 * math.pi)) * 2.0 / 3.0
    return ret


def wgs84_to_gcj02(lon: float, lat: float) -> Tuple[float, float]:
    """WGS-84 → GCJ-02（火星坐标）。中国境外原样返回。"""
    if _out_of_china(lon, lat):
        return lon, lat
    dlat = _transform_lat(lon - 105.0, lat - 35.0)
    dlon = _transform_lon(lon - 105.0, lat - 35.0)
    radlat = lat / 180.0 * math.pi
    magic = math.sin(radlat)
    magic = 1 - _EE * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((_A * (1 - _EE)) / (magic * sqrtmagic) * math.pi)
    dlon = (dlon * 180.0) / (_A / sqrtmagic * math.cos(radlat) * math.pi)
    return lon + dlon, lat + dlat


def gcj02_to_bd09(lon: float, lat: float) -> Tuple[float, float]:
    """GCJ-02 → BD-09（百度坐标）。"""
    z = math.sqrt(lon * lon + lat * lat) + 0.00002 * math.sin(lat * math.pi * 3000.0 / 180.0)
    theta = math.atan2(lat, lon) + 0.000003 * math.cos(lon * math.pi * 3000.0 / 180.0)
    return z * math.cos(theta) + 0.0065, z * math.sin(theta) + 0.006


def bd09_to_gcj02(lon: float, lat: float) -> Tuple[float, float]:
    """BD-09 → GCJ-02。"""
    x = lon - 0.0065
    y = lat - 0.006
    z = math.sqrt(x * x + y * y) - 0.00002 * math.sin(y * math.pi * 3000.0 / 180.0)
    theta = math.atan2(y, x) - 0.000003 * math.cos(x * math.pi * 3000.0 / 180.0)
    return z * math.cos(theta), z * math.sin(theta)


def gcj02_to_wgs84(lon: float, lat: float, max_iter: int = 30, tol: float = 1e-9) -> Tuple[float, float]:
    """GCJ-02 → WGS-84（迭代反算，精度可达 ~1e-6 度）。"""
    if _out_of_china(lon, lat):
        return lon, lat
    wlon, wlat = lon, lat
    for _ in range(max_iter):
        glon, glat = wgs84_to_gcj02(wlon, wlat)
        dlon = lon - glon
        dlat = lat - glat
        wlon += dlon
        wlat += dlat
        if abs(dlon) < tol and abs(dlat) < tol:
            break
    return wlon, wlat


def bd09_to_wgs84(lon: float, lat: float) -> Tuple[float, float]:
    glon, glat = bd09_to_gcj02(lon, lat)
    return gcj02_to_wgs84(glon, glat)


def wgs84_to_bd09(lon: float, lat: float) -> Tuple[float, float]:
    glon, glat = wgs84_to_gcj02(lon, lat)
    return gcj02_to_bd09(glon, glat)


# 有向系统转换派发表
_SYSTEM_FUNCS = {
    ("wgs84", "gcj02"): wgs84_to_gcj02,
    ("gcj02", "bd09"): gcj02_to_bd09,
    ("bd09", "gcj02"): bd09_to_gcj02,
    ("gcj02", "wgs84"): gcj02_to_wgs84,
    ("bd09", "wgs84"): bd09_to_wgs84,
    ("wgs84", "bd09"): wgs84_to_bd09,
}


def convert_system(lon: float, lat: float, from_sys: str, to_sys: str) -> Tuple[float, float]:
    """在 wgs84/gcj02/bd09 三个系统之间转换单点。"""
    f, t = from_sys.lower(), to_sys.lower()
    if f not in SYSTEMS or t not in SYSTEMS:
        raise UsageError(f"unknown coordinate system. Choose from: {sorted(SYSTEMS)}")
    if f == t:
        return lon, lat
    fn = _SYSTEM_FUNCS.get((f, t))
    if fn is None:
        raise UsageError(f"unsupported conversion {f} -> {t}")
    return fn(lon, lat)


# ---------------------------------------------------------------------------
# 矢量要素转换
# ---------------------------------------------------------------------------
def transform_geodataframe(gdf: Any, to_crs: str) -> Any:
    """把 GeoDataFrame 转换到目标 CRS（返回副本）。"""
    try:
        return gdf.to_crs(to_crs)
    except Exception as exc:  # noqa: BLE001
        raise ValidationError(f"failed to transform vector to {to_crs}: {exc}") from exc


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], n: int = 20, seed: int = 42) -> Any:
    """在 bbox 内生成 n 个随机点（WGS-84 / EPSG:4326）。"""
    import geopandas as gpd
    from shapely.geometry import Point
    from pyproj import CRS

    rng = np.random.default_rng(seed)
    w, s, e, n_ = bbox
    xs = rng.uniform(w, e, n)
    ys = rng.uniform(s, n_, n)
    geoms = [Point(x, y) for x, y in zip(xs, ys)]
    return gpd.GeoDataFrame(
        {"id": np.arange(1, n + 1)}, geometry=geoms, crs=CRS.from_epsg(4326))


def write_geojson(path: str, gdf: Any) -> None:
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    if len(gdf) == 0:
        with open(path, "w", encoding="utf-8") as f:
            json.dump({"type": "FeatureCollection", "features": []}, f)
        return
    gdf.to_file(path, driver="GeoJSON")


def read_vector(path: str) -> Any:
    import geopandas as gpd
    if not os.path.exists(path):
        raise UsageError(f"input vector not found: {path}", path=path)
    try:
        return gpd.read_file(path)
    except Exception as exc:  # noqa: BLE001
        raise ValidationError(f"failed to read vector '{path}': {exc}") from exc


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
    bbox: Optional[List[float]],
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
            "from_crs": getattr(args, "from_crs", None),
            "to_crs": getattr(args, "to_crs", None),
            "system": getattr(args, "system", None),
            "synthetic": bool(getattr(args, "synthetic", False)),
            "bbox": bbox,
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

    # 1) bbox 校验（先于 generate_synthetic，因为后者对 bbox 进行 np.random.uniform）
    if bbox is not None:
        validate_bbox(bbox)

    # 2) 加载数据
    if args.input and not args.synthetic:
        gdf = read_vector(args.input)
        if bbox is None and gdf.crs is not None:
            b = gdf.total_bounds
            bbox = [float(b[0]), float(b[1]), float(b[2]), float(b[3])]
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <vector>")
        gdf = generate_synthetic(bbox)
        source_note = "synthetic"

    # 3) 进一步校验
    if len(gdf) == 0:
        raise ValidationError("input vector has no features")
    if args.input and not args.synthetic and gdf.crs is None:
        raise ValidationError(
            f"input vector '{args.input}' has no CRS defined; "
            f"set --from-crs explicitly or provide a GeoJSON with a 'crs' member",
        )

    # 现在 makedirs
    os.makedirs(output_dir, exist_ok=True)

    # 两条转换路径：EPSG 路径（默认）或 中国坐标系路径
    mode = args.mode
    if mode == "epsg":
        transformer = make_transformer(args.from_crs, args.to_crs)
        out_gdf = transform_geodataframe(gdf, args.to_crs)
        # 抽样记录若干点的转换前后坐标
        sample = []
        xs = np.array([g.x for g in gdf.geometry])
        ys = np.array([g.y for g in gdf.geometry])
        ox, oy = transform_points(xs, ys, transformer)
        for i in range(min(5, len(xs))):
            sample.append({"in": [float(xs[i]), float(ys[i])],
                           "out": [float(ox[i]), float(oy[i])]})
        conversion = {"mode": "epsg", "from": args.from_crs, "to": args.to_crs,
                      "samples": sample}
    else:
        f, t = args.system_from, args.system_to
        out_pts = [convert_system(g.x, g.y, f, t) for g in gdf.geometry]
        out_gdf = gdf.copy()
        from shapely.geometry import Point
        out_gdf["geometry"] = [Point(x, y) for x, y in out_pts]
        out_gdf = out_gdf.set_crs(4326, allow_override=True)
        sample = [{"in": [float(g.x), float(g.y)], "out": [float(p[0]), float(p[1])]}
                  for g, p in list(zip(gdf.geometry, out_pts))[:5]]
        conversion = {"mode": "system", "from": f, "to": t, "samples": sample}

    # 写出产物
    out_geojson = os.path.join(output_dir, "transformed.geojson")
    write_geojson(out_geojson, out_gdf)
    report = {
        "skill": SKILL_NAME,
        "source": source_note,
        "n_features": int(len(gdf)),
        "conversion": conversion,
        "output_crs": (out_gdf.crs.to_string() if out_gdf.crs is not None else None),
    }
    report_path = os.path.join(output_dir, "transformation_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2, default=str)

    qa = {
        "source": source_note,
        "mode": mode,
        "n_features": int(len(gdf)),
        "from": conversion["from"],
        "to": conversion["to"],
    }
    outputs = [
        {"path": out_geojson, "kind": "vector",
         "feature_count": int(len(out_gdf))},
        {"path": report_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] mode: {mode}  {conversion['from']} -> {conversion['to']}")
        print(f"[{SKILL_NAME}] features: {len(gdf)}")
        print(f"[{SKILL_NAME}] output: {out_geojson}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="CRS transformation via pyproj plus WGS84/GCJ02/BD09 conversions.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input vector file (points / any geometry)")
    p.add_argument("--mode", default="epsg", choices=["epsg", "system"],
                   help="transformation mode: epsg (pyproj) or system (CN grids)")
    p.add_argument("--from-crs", dest="from_crs", default="EPSG:4326",
                   help="source CRS for epsg mode (default: EPSG:4326)")
    p.add_argument("--to-crs", dest="to_crs", default="EPSG:3857",
                   help="target CRS for epsg mode (default: EPSG:3857)")
    p.add_argument("--system-from", dest="system_from", default="wgs84",
                   choices=sorted(SYSTEMS), help="source CN coordinate system")
    p.add_argument("--system-to", dest="system_to", default="gcj02",
                   choices=sorted(SYSTEMS), help="target CN coordinate system")
    p.add_argument("--synthetic", action="store_true",
                   help="generate synthetic random points (offline)")
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
