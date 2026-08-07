#!/usr/bin/env python3
"""tile-service-generator — 瓦片服务生成

把栅格按 Web Mercator（EPSG:3857）XYZ 切片方案切分为多缩放级别的 PNG
瓦片，目录结构 ``{z}/{x}/{y}.png``，可直接被 Leaflet / OpenLayers /
mapbox 等前端作为 XYZ 瓦片服务加载。

核心实现：
- **XYZ 切片数学**：经纬度 ↔ 瓦片坐标 ↔ Web Mercator 米制边界，含 Bing
  风格 quadkey 编码。
- **纯 Python PNG 编码**：仅用 ``zlib`` + ``struct`` 写 8-bit 灰度 PNG，
  无 PIL/GDAL 依赖，完全离线。
- **逐瓦片重采样**：把瓦片像元中心反投影回经纬度，再从源栅格最近邻取样。

数据源：本地 GeoTIFF（``--input``），或 ``--synthetic`` 模式生成 64x64 渐变
栅格（离线）。

隐私声明 / Privacy：
- 默认完全离线运行，``--synthetic`` 模式不读取任何外部数据。
- 所有处理在本地完成，不上传用户数据。

Usage:
    python tile-service-generator.py --input dem.tif --min-zoom 6 --max-zoom 9
    python tile-service-generator.py --bbox 116 39 117 40 --synthetic --output-dir ./out

License: MIT
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import math
import os
import struct
import sys
import zlib
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

VERSION = "1.0.0"
SKILL_NAME = "tile-service-generator"

EARTH_RADIUS = 6378137.0
ORIGIN_SHIFT = math.pi * EARTH_RADIUS  # ~20037508.342789244

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
# 核心算法：XYZ 切片数学
# ---------------------------------------------------------------------------
def lon_to_tile_x(lon: float, z: int) -> float:
    n = 2 ** z
    return (lon + 180.0) / 360.0 * n


def lat_to_tile_y(lat: float, z: int) -> float:
    n = 2 ** z
    lat_r = math.radians(lat)
    return (1.0 - math.log(math.tan(lat_r) + 1.0 / math.cos(lat_r)) / math.pi) / 2.0 * n


def tile_x_to_lon(x: float, z: int) -> float:
    n = 2 ** z
    return x / n * 360.0 - 180.0


def tile_y_to_lat(y: float, z: int) -> float:
    n = 2 ** z
    return math.degrees(math.atan(math.sinh(math.pi * (1 - 2 * y / n))))


def tile_lonlat_bounds(x: int, y: int, z: int) -> Tuple[float, float, float, float]:
    """返回瓦片的经纬度边界 (west, south, east, north)。"""
    w = tile_x_to_lon(x, z)
    e = tile_x_to_lon(x + 1, z)
    n = tile_y_to_lat(y, z)
    s = tile_y_to_lat(y + 1, z)
    return w, s, e, n


def lonlat_to_mercator(lon: float, lat: float) -> Tuple[float, float]:
    x = math.radians(lon) * EARTH_RADIUS
    y = math.log(math.tan(math.pi / 4 + math.radians(lat) / 2)) * EARTH_RADIUS
    return x, y


def mercator_to_lonlat(x: float, y: float) -> Tuple[float, float]:
    lon = math.degrees(x / EARTH_RADIUS)
    lat = math.degrees(2 * math.atan(math.exp(y / EARTH_RADIUS)) - math.pi / 2)
    return lon, lat


def tile_mercator_bounds(x: int, y: int, z: int) -> Tuple[float, float, float, float]:
    """返回瓦片的 Web Mercator 米制边界 (minx, miny, maxx, maxy)。"""
    w, s, e, n = tile_lonlat_bounds(x, y, z)
    minx, miny = lonlat_to_mercator(w, s)
    maxx, maxy = lonlat_to_mercator(e, n)
    return minx, miny, maxx, maxy


def quadkey(x: int, y: int, z: int) -> str:
    """Bing Maps quadkey 编码。"""
    key = []
    for i in range(z, 0, -1):
        digit = 0
        mask = 1 << (i - 1)
        if x & mask:
            digit += 1
        if y & mask:
            digit += 2
        key.append(str(digit))
    return "".join(key)


def tile_range_for_bbox(bbox: List[float], z: int) -> Tuple[int, int, int, int]:
    """返回覆盖 bbox 的瓦片索引范围 (x_min, y_min, x_max, y_max)（含端点）。"""
    w, s, e, n = bbox
    n_tiles = 2 ** z
    x0 = int(math.floor(lon_to_tile_x(w, z)))
    x1 = int(math.floor(lon_to_tile_x(e, z)))
    y0 = int(math.floor(lat_to_tile_y(n, z)))  # 北纬 → 较小 y
    y1 = int(math.floor(lat_to_tile_y(s, z)))
    x0, x1 = max(0, min(x0, x1)), min(n_tiles - 1, max(x0, x1))
    y0, y1 = max(0, min(y0, y1)), min(n_tiles - 1, max(y0, y1))
    return x0, y0, x1, y1


# ---------------------------------------------------------------------------
# 纯 Python PNG 编码（8-bit 灰度）
# ---------------------------------------------------------------------------
def _png_chunk(typ: bytes, data: bytes) -> bytes:
    chunk = struct.pack(">I", len(data)) + typ + data
    crc = struct.pack(">I", zlib.crc32(typ + data) & 0xFFFFFFFF)
    return chunk + crc


def encode_png_grayscale(path: str, arr: np.ndarray) -> None:
    """把 (H, W) uint8 数组写为 8-bit 灰度 PNG。"""
    arr = np.ascontiguousarray(arr, dtype=np.uint8)
    h, w = arr.shape
    sig = b"\x89PNG\r\n\x1a\n"
    ihdr = struct.pack(">IIBBBBB", w, h, 8, 0, 0, 0, 0)
    raw = bytearray()
    for row in arr:
        raw.append(0)  # filter type 0 (None)
        raw.extend(row.tobytes())
    idat = zlib.compress(bytes(raw), 6)
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "wb") as f:
        f.write(sig)
        f.write(_png_chunk(b"IHDR", ihdr))
        f.write(_png_chunk(b"IDAT", idat))
        f.write(_png_chunk(b"IEND", b""))


def decode_png_size(path: str) -> Tuple[int, int]:
    """读 PNG IHDR，返回 (width, height)，并校验签名。"""
    with open(path, "rb") as f:
        sig = f.read(8)
        if sig != b"\x89PNG\r\n\x1a\n":
            raise ValidationError(f"not a valid PNG: {path}")
        f.read(4)  # length
        typ = f.read(4)
        if typ != b"IHDR":
            raise ValidationError(f"missing IHDR in {path}")
        w, h = struct.unpack(">II", f.read(8))
    return w, h


# ---------------------------------------------------------------------------
# 逐瓦片重采样
# ---------------------------------------------------------------------------
def resample_tile(band: np.ndarray, bbox: List[float],
                  x: int, y: int, z: int, tile_size: int = 256,
                  nodata: Optional[float] = None) -> np.ndarray:
    """把瓦片像元反投影回经纬度并从源栅格最近邻取样，返回 (tile_size, tile_size)。"""
    h, w = band.shape
    tw, ts, te, tn = tile_lonlat_bounds(x, y, z)
    px = np.arange(tile_size)
    py = np.arange(tile_size)
    # 像元中心经纬度
    lons = tw + (px + 0.5) / tile_size * (te - tw)
    lats = tn - (py + 0.5) / tile_size * (tn - ts)
    LON, LAT = np.meshgrid(lons, lats)
    # 经纬度 → 源栅格像元索引
    col = (LON - bbox[0]) / (bbox[2] - bbox[0]) * w - 0.5
    row = (bbox[3] - LAT) / (bbox[3] - bbox[1]) * h - 0.5
    cidx = np.round(col).astype(int)
    ridx = np.round(row).astype(int)
    valid = (cidx >= 0) & (cidx < w) & (ridx >= 0) & (ridx < h)
    cidx_c = np.clip(cidx, 0, w - 1)
    ridx_c = np.clip(ridx, 0, h - 1)
    tile = band[ridx_c, cidx_c].astype(np.float64)
    tile[~valid] = np.nan
    return tile


def normalize_uint8(tile: np.ndarray) -> np.ndarray:
    """把瓦片值线性拉伸到 0-255；NaN 置 0（背景）。"""
    valid = np.isfinite(tile)
    if not valid.any():
        return np.zeros(tile.shape, dtype=np.uint8)
    vmin = float(np.nanmin(tile))
    vmax = float(np.nanmax(tile))
    if vmax - vmin < 1e-12:
        out = np.where(valid, 128.0, 0.0)
    else:
        out = (tile - vmin) / (vmax - vmin) * 255.0
    out = np.where(valid, out, 0.0)
    return np.clip(out, 0, 255).astype(np.uint8)


def generate_tiles(band: np.ndarray, bbox: List[float], zooms: List[int],
                   output_dir: str, tile_size: int = 256) -> Dict[str, Any]:
    """生成所有缩放级别的 XYZ 瓦片，返回元数据。"""
    tiles_root = os.path.join(output_dir, "tiles")
    meta_zooms: Dict[str, Any] = {}
    total = 0
    for z in zooms:
        x0, y0, x1, y1 = tile_range_for_bbox(bbox, z)
        z_tiles = []
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                tile = resample_tile(band, bbox, x, y, z, tile_size)
                png = normalize_uint8(tile)
                rel = os.path.join(str(z), str(x), f"{y}.png")
                path = os.path.join(tiles_root, rel)
                encode_png_grayscale(path, png)
                z_tiles.append({"x": x, "y": y, "path": rel,
                                "quadkey": quadkey(x, y, z)})
                total += 1
        meta_zooms[str(z)] = {"count": len(z_tiles), "tiles": z_tiles}
    return {"zooms": meta_zooms, "total_tiles": total, "tile_size": tile_size}


# ---------------------------------------------------------------------------
# 合成数据 / GeoTIFF I/O
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], size: int = 64) -> Tuple[np.ndarray, Dict[str, Any]]:
    yy, xx = np.mgrid[0:size, 0:size].astype(np.float64)
    band = (np.sin(xx / size * math.pi * 2) * 0.5 + 0.5) * 100 + yy / size * 50
    return band.astype(np.float32)[np.newaxis, ...], {"bbox": bbox, "size": size}


def write_geotiff(path: str, cube: np.ndarray, bbox: List[float],
                  nodata: float = -9999.0) -> None:
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


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float]]:
    """读 GeoTIFF；NoData 像素替换为 NaN 后返回 (cube, bbox)。

    元数据通过模块级 _LAST_READ_META 暴露：nodata / n_valid_pixels / n_total_pixels。
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [float(b.left), float(b.bottom), float(b.right), float(b.top)]
        nodata = src.nodata
    if nodata is not None:
        cube = np.where(cube == float(nodata), np.nan, cube)
    n_valid = int(np.count_nonzero(np.isfinite(cube)))
    n_total = int(cube.size)
    globals()["_LAST_READ_META"] = {
        "nodata": nodata, "n_valid_pixels": n_valid, "n_total_pixels": n_total,
    }
    return cube, bbox


def get_last_read_meta() -> Dict[str, Any]:
    return globals().get("_LAST_READ_META", {"nodata": None,
                                              "n_valid_pixels": 0,
                                              "n_total_pixels": 0})


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
            "min_zoom": getattr(args, "min_zoom", None),
            "max_zoom": getattr(args, "max_zoom", None),
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
    in_meta: Dict[str, Any] = {"nodata": None, "n_valid_pixels": 0, "n_total_pixels": 0}

    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        in_meta = get_last_read_meta()
        if bbox is not None:
            bbox = validate_bbox(bbox, kind="--bbox")
        else:
            bbox = validate_bbox(file_bbox, kind="--input file bbox")
        if in_meta["n_valid_pixels"] == 0:
            raise ValidationError(
                f"input raster has no valid pixels (all NoData={in_meta['nodata']})",
                path=args.input, n_total_pixels=in_meta["n_total_pixels"],
            )
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        bbox = validate_bbox(bbox, kind="--bbox")
        cube, _info = generate_synthetic(bbox, size=args.size)
        source_note = "synthetic"

    if cube.size == 0:
        raise ValidationError("input raster is empty")
    if args.min_zoom > args.max_zoom:
        raise UsageError("min-zoom must be <= max-zoom")
    if args.min_zoom < 0 or args.max_zoom > 22:
        raise UsageError(
            f"zoom levels must be in [0, 22] (got min={args.min_zoom}, max={args.max_zoom})",
            min_zoom=args.min_zoom, max_zoom=args.max_zoom,
        )
    if args.tile_size < 8 or args.tile_size > 2048:
        raise UsageError(
            f"tile-size must be in [8, 2048] (got {args.tile_size})",
            tile_size=args.tile_size,
        )
    if args.size < 1:
        raise UsageError(f"--size must be >= 1 (got {args.size})", size=args.size)

    # 校验通过后再建目录（失败时不留空目录）
    os.makedirs(output_dir, exist_ok=True)

    band = cube[0]
    zooms = list(range(args.min_zoom, args.max_zoom + 1))
    tile_meta = generate_tiles(band, bbox, zooms, output_dir, tile_size=args.tile_size)

    tiles_json = os.path.join(output_dir, "tiles.json")
    tile_meta["bbox"] = bbox
    tile_meta["source"] = source_note
    tile_meta["zoom_levels"] = zooms
    with open(tiles_json, "w", encoding="utf-8") as f:
        json.dump(tile_meta, f, ensure_ascii=False, indent=2)

    qa = {
        "source": source_note,
        "zoom_levels": zooms,
        "total_tiles": tile_meta["total_tiles"],
        "tile_size": args.tile_size,
    }
    if args.input and not args.synthetic:
        qa["input_nodata"] = in_meta["nodata"]
        qa["input_n_valid_pixels"] = in_meta["n_valid_pixels"]
        qa["input_n_total_pixels"] = in_meta["n_total_pixels"]
    outputs = [{"path": tiles_json, "kind": "json"}]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] zooms: {zooms}")
        print(f"[{SKILL_NAME}] total tiles: {tile_meta['total_tiles']}")
        print(f"[{SKILL_NAME}] tiles: {os.path.join(output_dir, 'tiles')}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Slice a raster into multi-zoom XYZ Web Mercator PNG tiles.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input GeoTIFF raster")
    p.add_argument("--min-zoom", dest="min_zoom", type=int, default=6,
                   help="minimum zoom level (default: 6)")
    p.add_argument("--max-zoom", dest="max_zoom", type=int, default=8,
                   help="maximum zoom level (default: 8)")
    p.add_argument("--tile-size", dest="tile_size", type=int, default=256,
                   help="tile edge in pixels (default: 256)")
    p.add_argument("--size", type=int, default=64,
                   help="synthetic raster size in pixels (default: 64)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate synthetic raster (offline)")
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
