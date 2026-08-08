#!/usr/bin/env python3
"""virtual-globe-export — 虚拟地球导出

把时空点/线数据导出为虚拟地球（Google Earth / Cesium）可读格式：
- **KML**：Placemark + Point + coordinates + TimeStamp（时间属性）
  + ExtendedData（弹出信息）。坐标严格按 lon,lat,alt 顺序。
- **CZML**：Cesium 时间动态 JSON 包，首包为 document，随后每个要素一个
  实体包，position 用 cartographicDegrees，时间用 availability 区间。

数据源：本地点 CSV/GeoJSON（可选），或 ``--synthetic`` 生成带时间戳的
模拟移动目标轨迹。

隐私声明 / Privacy：完全离线；所有处理本地完成，不上传用户数据。

Usage:
    python virtual-globe-export.py --input track.geojson --format kml
    python virtual-globe-export.py --bbox 116 39 117 40 --synthetic --n-points 10 --format both

License: MIT
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import sys
from typing import Any, Dict, List, Optional, Tuple
from xml.sax.saxutils import escape

import numpy as np

VERSION = "1.0.0"
SKILL_NAME = "virtual-globe-export"

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


def validate_bbox(bbox):
    """Validate WGS-84 bbox. Returns (W, S, E, N) as floats.

    Rules:
      - 4 numeric values
      - -180 <= W, E <= 180; -90 <= S, N <= 90
      - W < E (no antimeridian crossing; split into two bboxes if needed)
      - S < N
      - width / height strictly positive
    Raises ValidationError (exit 6) on any failure.
    """
    if bbox is None or len(bbox) != 4:
        raise ValidationError(f"bbox must be 4 floats [W S E N], got: {bbox}")
    w, s, e, n = (float(v) for v in bbox)
    for label, val, lo, hi in (("W", w, -180.0, 180.0), ("E", e, -180.0, 180.0),
                               ("S", s, -90.0, 90.0), ("N", n, -90.0, 90.0)):
        if val < lo or val > hi:
            raise ValidationError(
                f"bbox {label}={val} out of range [{lo}, {hi}]; got bbox={bbox}"
            )
    if w >= e:
        raise ValidationError(
            f"bbox W={w} must be < E={e} (no antimeridian crossing; "
            f"if needed, split into two bboxes)"
        )
    if s >= n:
        raise ValidationError(
            f"bbox S={s} must be < N={n}"
        )
    if (e - w) < 1e-9 or (n - s) < 1e-9:
        raise ValidationError(
            f"bbox has zero or negative area: width={e - w:.3e}, height={n - s:.3e}"
        )
    return w, s, e, n


def validate_n_points(n):
    """n-points must be a positive integer (>= 2 to form a meaningful track)."""
    try:
        v = int(n)
    except (TypeError, ValueError):
        raise ValidationError(f"n-points must be an integer, got: {n!r}")
    if v < 2:
        raise ValidationError(
            f"n-points must be >= 2 (need at least 2 points for a track), got: {v}"
        )
    return v


# ---------------------------------------------------------------------------
# 核心算法：KML 坐标与文档
# ---------------------------------------------------------------------------
def format_kml_coord(lon: float, lat: float, alt: float = 0.0) -> str:
    """KML 坐标串：严格 lon,lat,alt（经度在前），空格分隔多点。"""
    return f"{float(lon):.6f},{float(lat):.6f},{float(alt):.1f}"


def format_kml_coords(points: List[Tuple[float, float, float]]) -> str:
    return " ".join(format_kml_coord(p[0], p[1], p[2] if len(p) > 2 else 0.0)
                    for p in points)


def build_kml(features: List[Dict[str, Any]], name: str = "Export") -> str:
    """由要素列表生成 KML 文档字符串。

    每个 feature: {name, coords:[(lon,lat,alt),...], time(str ISO),
    properties:dict}。单点用 Point，多点用 LineString；time 写 TimeStamp；
    properties 写 ExtendedData（Google Earth 弹出气泡）。
    """
    parts = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<kml xmlns="http://www.opengis.net/kml/2.2">',
             "<Document>", f"<name>{escape(name)}</name>"]
    for f in features:
        coords = f.get("coords") or []
        if not coords:
            continue
        parts.append("<Placemark>")
        parts.append(f"<name>{escape(str(f.get('name', 'feature')))}</name>")
        # 时间属性
        if f.get("time"):
            parts.append(f"<TimeStamp><when>{f['time']}</when></TimeStamp>")
        # 弹出信息 ExtendedData
        props = f.get("properties") or {}
        if props:
            parts.append("<ExtendedData>")
            for k, v in props.items():
                parts.append(f'<Data name="{escape(str(k))}">'
                             f"<value>{escape(str(v))}</value></Data>")
            parts.append("</ExtendedData>")
        coord_str = format_kml_coords(coords)
        if len(coords) == 1:
            parts.append(f"<Point><coordinates>{coord_str}</coordinates></Point>")
        else:
            parts.append("<LineString><tessellate>1</tessellate>"
                         f"<coordinates>{coord_str}</coordinates></LineString>")
        parts.append("</Placemark>")
    parts.append("</Document></kml>")
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# 核心算法：CZML
# ---------------------------------------------------------------------------
def build_czml(features: List[Dict[str, Any]], name: str = "Export") -> List[Dict[str, Any]]:
    """生成 CZML 包列表：首包 document，其余为实体。

    实体 position 用 cartographicDegrees=[lon,lat,alt]；时间用
    availability="start/end" 区间（无 time 时退化为单时刻）。
    """
    packets: List[Dict[str, Any]] = [
        {"id": "document", "name": name, "version": "1.0"}]
    for i, f in enumerate(features):
        coords = f.get("coords") or []
        if not coords:
            continue
        first = coords[0]
        pkt: Dict[str, Any] = {
            "id": f"feature-{i}",
            "name": str(f.get("name", f"feature-{i}")),
            "position": {"cartographicDegrees":
                         [float(first[0]), float(first[1]),
                          float(first[2] if len(first) > 2 else 0.0)]},
        }
        if f.get("time"):
            t = f["time"]
            pkt["availability"] = f"{t}/{f.get('time_end', t)}"
        props = f.get("properties") or {}
        if props:
            pkt["description"] = "<br/>".join(
                f"<b>{escape(str(k))}</b>: {escape(str(v))}" for k, v in props.items())
        pkt["point"] = {"pixelSize": 8, "color": {"rgba": [255, 80, 80, 255]}}
        packets.append(pkt)
    return packets


def iso_time(dt: _dt.datetime) -> str:
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


# ---------------------------------------------------------------------------
# 合成数据：带时间戳的移动目标轨迹
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], n_points: int = 10, seed: int = 42
                       ) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    rng = np.random.default_rng(seed)
    w, s, e, n = bbox
    t0 = _dt.datetime(2020, 1, 1, 0, 0, 0)
    features = []
    # 一条从西南到东北的轨迹
    fr = np.linspace(0, 1, n_points)
    lons = w + fr * (e - w)
    lats = s + fr * (n - s)
    coords = [(float(lons[i]), float(lats[i]), float(100 + 20 * i))
              for i in range(n_points)]
    for i, c in enumerate(coords):
        t = t0 + _dt.timedelta(hours=i)
        features.append({
            "name": f"track-pt-{i + 1}",
            "coords": [c],
            "time": iso_time(t),
            "properties": {"speed_kmh": round(float(rng.uniform(40, 90)), 1),
                           "sensor": "synthetic", "index": i + 1}})
    # 额外加一条完整 LineString 轨迹
    features.append({"name": "full-track", "coords": coords,
                     "time": iso_time(t0),
                     "properties": {"type": "trajectory", "n": n_points}})
    info = {"bbox": bbox, "n_points": n_points, "kind": "synthetic-track",
            "start": iso_time(t0),
            "end": iso_time(t0 + _dt.timedelta(hours=n_points - 1))}
    return features, info


def read_points(path: str) -> List[Dict[str, Any]]:
    """从 GeoJSON/CSV 读取点要素为统一结构。"""
    if not os.path.exists(path):
        raise UsageError(f"input not found: {path}", path=path)
    features: List[Dict[str, Any]] = []
    if path.lower().endswith((".geojson", ".json")):
        with open(path, encoding="utf-8") as f:
            gj = json.load(f)
        for ft in gj.get("features", []):
            geom = ft.get("geometry") or {}
            props = ft.get("properties") or {}
            if geom.get("type") == "Point":
                c = geom["coordinates"]
                coords = [(c[0], c[1], c[2] if len(c) > 2 else 0.0)]
            elif geom.get("type") == "LineString":
                coords = [(c[0], c[1], c[2] if len(c) > 2 else 0.0)
                          for c in geom["coordinates"]]
            else:
                continue
            features.append({"name": props.get("name", "feature"), "coords": coords,
                             "time": props.get("time"), "properties": props})
    else:  # CSV: lon,lat[,alt][,name][,time]
        import csv
        with open(path, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                try:
                    lon = float(row["lon"]); lat = float(row["lat"])
                except (KeyError, ValueError):
                    continue
                alt = float(row.get("alt", 0) or 0)
                features.append({"name": row.get("name", "point"),
                                 "coords": [(lon, lat, alt)],
                                 "time": row.get("time"),
                                 "properties": {k: v for k, v in row.items()
                                                if k not in ("lon", "lat", "alt",
                                                             "name", "time")}})
    return features


# ---------------------------------------------------------------------------
# GeoTIFF I/O（轨迹点密度栅格，作可验证空间产物）
# ---------------------------------------------------------------------------
def track_density_raster(features: List[Dict[str, Any]], bbox: List[float],
                         width: int, height: int) -> np.ndarray:
    grid = np.zeros((height, width), dtype=np.float32)
    w, s, e, n = bbox
    for f in features:
        for c in f.get("coords", []):
            col = int((c[0] - w) / (e - w) * width)
            row = int((n - c[1]) / (n - s) * height)
            if 0 <= col < width and 0 <= row < height:
                grid[row, col] += 1
    return grid


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
                "format": getattr(args, "format", None),
                "n_points": getattr(args, "n_points", None),
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

    # ---- P0/P1: validate bbox, n-points BEFORE mkdir ----
    if bbox is not None:
        bbox = list(validate_bbox(bbox))
    args.n_points = validate_n_points(args.n_points)

    os.makedirs(output_dir, exist_ok=True)

    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        features = read_points(args.input)
        if not features:
            raise ValidationError("no features read from input")
        # 推断 bbox
        allc = [c for f in features for c in f.get("coords", [])]
        xs = [c[0] for c in allc]; ys = [c[1] for c in allc]
        bbox = bbox or [float(min(xs)), float(min(ys)), float(max(xs)), float(max(ys))]
        bbox = list(validate_bbox(bbox))
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input")
        features, synth_info = generate_synthetic(bbox, n_points=args.n_points)
        source_note = "synthetic"

    if bbox is None:
        raise UsageError("could not determine bbox")

    written: List[str] = []
    outputs: List[Dict[str, Any]] = []
    if args.format in ("kml", "both"):
        kml = build_kml(features, name=args.name)
        kml_path = os.path.join(output_dir, "export.kml")
        with open(kml_path, "w", encoding="utf-8") as f:
            f.write(kml)
        written.append(kml_path)
        outputs.append({"path": kml_path, "kind": "text"})
    if args.format in ("czml", "both"):
        czml = build_czml(features, name=args.name)
        czml_path = os.path.join(output_dir, "export.czml")
        with open(czml_path, "w", encoding="utf-8") as f:
            json.dump(czml, f, ensure_ascii=False, indent=2)
        written.append(czml_path)
        outputs.append({"path": czml_path, "kind": "json"})

    # 可验证产物：导出 JSON（结构化）+ 密度栅格
    export_json = {"name": args.name, "source": source_note, "bbox": bbox,
                   "n_features": len(features), "features": features,
                   "generated_at": _utc_now()}
    if synth_info is not None:
        export_json["synthetic"] = synth_info
    json_path = os.path.join(output_dir, "export.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(export_json, f, ensure_ascii=False, indent=2)
    outputs.append({"path": json_path, "kind": "json"})

    density = track_density_raster(features, bbox, 64, 64)
    tif_path = os.path.join(output_dir, "track_density.tif")
    write_geotiff(tif_path, density, bbox)
    outputs.append({"path": tif_path, "kind": "raster", "crs_epsg": 4326,
                    "bbox_wgs84": bbox, "band_count": 1})

    qa = {"source": source_note, "format": args.format,
          "n_features": len(features), "density_total": float(density.sum()),
          "bbox": bbox}
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}  features: {len(features)}  format: {args.format}")
        for p in written:
            print(f"[{SKILL_NAME}] wrote: {p}")
        print(f"[{SKILL_NAME}] json: {json_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Export spatio-temporal features to KML / CZML for virtual globes.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"))
    p.add_argument("--input", help="input GeoJSON/CSV points")
    p.add_argument("--format", default="both", choices=["kml", "czml", "both"],
                   help="export format (default: both)")
    p.add_argument("--n-points", type=int, default=10,
                   help="synthetic track point count (default: 10)")
    p.add_argument("--name", default="Track Export", help="document name")
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
