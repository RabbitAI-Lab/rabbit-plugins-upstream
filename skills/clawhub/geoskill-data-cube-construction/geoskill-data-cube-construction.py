#!/usr/bin/env python3
"""data-cube-construction — 遥感数据立方体构建

把多时相、多波段的栅格影像组织为一个带完整坐标（time / band / y / x）的
四维数据立方体（analysis-ready data cube），并以 NetCDF 格式落盘。这是
GEE / odc-stac / stackstac 等"立方体优先"工作流的本地离线替代：

- 将 N 个时相、B 个波段堆叠为 (time, band, y, x) 的 4D 数组；
- 用 ``xarray.DataArray`` 组织带坐标与维度属性的立方体；
- 以 NetCDF（``.nc``）写出，附带逐时相、逐波段的统计元数据 JSON。

数据源：本地多波段 GeoTIFF（``--input``，单景按单时相处理）；或使用
``--synthetic`` / 仅给 ``--bbox`` 时离线生成物理一致的多时相模拟立方体
（植被季节信号 + 波段光谱差异），用于无网络测试。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python data-cube-construction.py --bbox 116 39 117 40 --n-dates 6 --bands 4
    python data-cube-construction.py --bbox 116 39 117 40 --synthetic --output-dir ./out
    python data-cube-construction.py --input scene.tif --output-dir ./out

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
SKILL_NAME = "data-cube-construction"

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


# 可选依赖：xarray 优先，缺失时退化到 scipy.io.netcdf_file（NetCDF3）。
try:
    import xarray as xr  # noqa: F401
    _HAS_XARRAY = True
except ImportError:  # pragma: no cover
    xr = None
    _HAS_XARRAY = False

try:
    from scipy.io import netcdf_file as _scipy_netcdf
    _HAS_SCIPY_NC = True
except ImportError:  # pragma: no cover
    _scipy_netcdf = None
    _HAS_SCIPY_NC = False


# 默认波段名称（generic 4 波段：蓝绿红近红外）
DEFAULT_BAND_NAMES = ["blue", "green", "red", "nir"]


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# 校验：bbox 合法性
# ---------------------------------------------------------------------------
def validate_bbox(bbox) -> None:
    """P0: bbox 合法性前置校验。
    - 长度 4
    - 经度范围 -360 ≤ W,E ≤ 360
    - 纬度范围 -90 ≤ S,N ≤ 90
    - W < E, S < N
    - 面积 > 0
    跨 180° 经线（antimeridian crossing）不支持，给出拆分提示。
    """
    if not isinstance(bbox, (list, tuple)) or len(bbox) != 4:
        raise ValidationError(
            f"bbox must be a 4-element [W S E N]; got {bbox!r}"
        )
    try:
        w, s, e, n = [float(v) for v in bbox]
    except (TypeError, ValueError) as exc:
        raise ValidationError(f"bbox values must be numeric; got {bbox!r}") from exc
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"bbox longitude out of range [-180, 180]: W={w}, E={e}"
        )
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"bbox latitude out of range [-90, 90]: S={s}, N={n}"
        )
    if w >= e:
        # 跨 180° 经线：W > 0 且 E < 0
        if w > 0 and e < 0 and (e - w) > -360:
            raise ValidationError(
                f"bbox W ({w}) >= E ({e}); cross-180° antimeridian is not "
                f"supported — split into two extents"
            )
        raise ValidationError(f"bbox W ({w}) must be < E ({e})")
    if s >= n:
        raise ValidationError(f"bbox S ({s}) must be < N ({n})")
    area = (e - w) * (n - s)
    if area <= 0:
        raise ValidationError(f"bbox area must be > 0; got {area}")


# ---------------------------------------------------------------------------
# 校验：合成参数
# ---------------------------------------------------------------------------
def validate_synthetic_params(n_dates: int, bands: int) -> None:
    if not isinstance(n_dates, int) or n_dates < 1:
        raise UsageError(f"n-dates must be >= 1; got {n_dates}")
    if not isinstance(bands, int) or bands < 1:
        raise UsageError(f"bands must be >= 1; got {bands}")


# ---------------------------------------------------------------------------
# 核心算法：4D 数组 → 带坐标的 xarray.DataArray
# ---------------------------------------------------------------------------
def build_data_array(
    cube: np.ndarray,
    bbox: List[float],
    dates: List[str],
    band_names: List[str],
) -> "xr.DataArray":
    """把 (time, band, y, x) 的 4D 数组组织为带坐标的 xarray.DataArray。

    坐标：
    - time：ISO 日期字符串（维度长度须与 cube.shape[0] 一致）
    - band：波段名（长度须与 cube.shape[1] 一致）
    - y / x：由 bbox 与栅格尺寸线性生成的地理坐标（EPSG:4326）

    返回的 DataArray 携带 ``attrs``（crs、bbox、来源约定）。
    """
    if cube.ndim != 4:
        raise ValidationError(
            f"cube must be 4D (time, band, y, x); got ndim={cube.ndim}",
            ndim=int(cube.ndim),
        )
    nt, nb, ny, nx = cube.shape
    if len(dates) != nt:
        raise ValidationError(
            f"dates length {len(dates)} != cube time dim {nt}",
            dates=len(dates), time=int(nt),
        )
    if len(band_names) != nb:
        raise ValidationError(
            f"band_names length {len(band_names)} != cube band dim {nb}",
            bands=len(band_names), band_dim=int(nb),
        )

    w, s, e, n = bbox
    ys = np.linspace(n, s, ny, dtype=np.float64)   # 行从上到下（北→南）
    xs = np.linspace(w, e, nx, dtype=np.float64)   # 列从左到右（西→东）

    if not _HAS_XARRAY:
        raise ProcessError(
            "xarray is required to build the data cube; install xarray",
        )

    da = xr.DataArray(
        data=cube.astype(np.float32),
        dims=("time", "band", "y", "x"),
        coords={
            "time": ("time", list(dates)),
            "band": ("band", list(band_names)),
            "y": ("y", ys),
            "x": ("x", xs),
        },
        name="reflectance",
        attrs={
            "crs": "EPSG:4326",
            "bbox_wgs84": json.dumps([float(w), float(s), float(e), float(n)]),
            "units": "reflectance",
            "long_name": "surface reflectance data cube",
        },
    )
    return da


def cube_statistics(cube: np.ndarray) -> Dict[str, Any]:
    """逐时相、逐波段统计 + 全局统计。"""
    nt, nb = cube.shape[0], cube.shape[1]
    per_time = []
    for t in range(nt):
        per_time.append({
            "time_index": t,
            "mean": float(np.nanmean(cube[t])),
            "std": float(np.nanstd(cube[t])),
        })
    per_band = []
    for b in range(nb):
        per_band.append({
            "band_index": b,
            "mean": float(np.nanmean(cube[:, b])),
            "std": float(np.nanstd(cube[:, b])),
        })
    return {
        "global_mean": float(np.nanmean(cube)),
        "global_std": float(np.nanstd(cube)),
        "per_time": per_time,
        "per_band": per_band,
    }


# ---------------------------------------------------------------------------
# 合成数据：多时相 × 多波段立方体（离线）
# ---------------------------------------------------------------------------
def generate_synthetic_cube(
    bbox: List[float],
    n_dates: int = 6,
    bands: int = 4,
    width: int = 96,
    height: int = 96,
    start_date: str = "2023-01-01",
    step_days: int = 16,
    seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成 (n_dates, bands, H, W) 的反射率立方体。

    物理一致性设计：
    - 空间上分植被 / 土壤 / 水体三类地物（平滑分区掩膜）；
    - 各波段有典型光谱（蓝低、绿中、红低、NIR 高，对植被而言）；
    - 时间上叠加一个季节性物候信号（NIR 随"生长季"正弦变化），
      使时间维度有真实可用的变化结构。

    返回 (cube, info)，cube 值域约 [0, 1]。
    """
    if n_dates < 1:
        raise UsageError("n-dates must be >= 1", n_dates=int(n_dates))
    if bands < 1:
        raise UsageError("bands must be >= 1", bands=int(bands))

    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    yy = yy.astype(np.float32) / max(height - 1, 1)
    xx = xx.astype(np.float32) / max(width - 1, 1)

    veg_mask = ((xx + yy) > 1.1).astype(np.float32)
    water_mask = ((xx + yy) < 0.5).astype(np.float32)
    soil_mask = np.clip(1.0 - veg_mask - water_mask, 0.0, 1.0)

    # 每类地物在 4 个波段（蓝绿红NIR）上的基准反射率
    veg_rho = [0.03, 0.08, 0.04, 0.45]
    soil_rho = [0.10, 0.14, 0.18, 0.28]
    water_rho = [0.06, 0.05, 0.03, 0.01]

    start = _dt.date.fromisoformat(start_date)
    dates = [(start + _dt.timedelta(days=step_days * i)).isoformat()
             for i in range(n_dates)]

    band_names = [DEFAULT_BAND_NAMES[b] if b < len(DEFAULT_BAND_NAMES)
                  else f"band_{b}" for b in range(bands)]

    cube = np.zeros((n_dates, bands, height, width), dtype=np.float32)
    for t in range(n_dates):
        # 季节物候：生长季正弦（夏季 NIR 升高）
        phase = 2.0 * np.pi * (t / max(n_dates, 1))
        veg_season = 0.5 + 0.5 * np.sin(phase - np.pi / 2.0)  # [0,1]
        for b in range(bands):
            vi = min(b, 3)
            base = (veg_mask * veg_rho[vi]
                    + soil_mask * soil_rho[vi]
                    + water_mask * water_rho[vi])
            layer = base.copy()
            # 物候主要影响 NIR（波段索引 3）及红边附近
            if vi == 3:
                layer = layer + veg_mask * (0.20 * veg_season)
            layer = layer + rng.normal(0.0, 0.004, size=layer.shape).astype(np.float32)
            cube[t, b] = np.clip(layer, 0.0, 1.0)

    info = {
        "bbox": bbox,
        "width": width,
        "height": height,
        "n_dates": n_dates,
        "bands": bands,
        "band_names": band_names,
        "dates": dates,
        "step_days": step_days,
    }
    return cube, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O（直接用 rasterio，保证离线可用）
# ---------------------------------------------------------------------------
def read_geotiff(path: str) -> Tuple[np.ndarray, List[float], Optional[float]]:
    """读 GeoTIFF，返回 (cube, bbox, nodata)。
    P0: 把 NoData 替换为 NaN，以便 cube_statistics() 用 nanmean/nanstd 正确处理。
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read(masked=False).astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nodata = src.nodata
    # 把 NoData 替换为 NaN（仅在 nodata 显式给出时）
    if nodata is not None:
        cube = np.where(cube == float(nodata), np.nan, cube)
    return cube, bbox, nodata


# ---------------------------------------------------------------------------
# NetCDF I/O（xarray 优先，scipy 兜底）
# ---------------------------------------------------------------------------
def write_netcdf(da: "xr.DataArray", path: str) -> str:
    """把 DataArray 写出为 NetCDF。优先 xarray（scipy engine / NetCDF3），
    若 xarray 不可用则用 scipy.io.netcdf_file 直接写。"""
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    if _HAS_XARRAY:
        ds = da.to_dataset(name=da.name or "reflectance")
        try:
            ds.to_netcdf(path, engine="scipy")
        except Exception:  # pragma: no cover - engine 回退
            ds.to_netcdf(path)
        return path
    if _HAS_SCIPY_NC:
        _write_scipy_netcdf(da, path)
        return path
    raise ProcessError("no NetCDF backend available (need xarray or scipy)")


def _write_scipy_netcdf(da: "xr.DataArray", path: str) -> None:
    """纯 scipy.io.netcdf_file 兜底写出（NetCDF3）。"""
    arr = np.asarray(da.values, dtype=np.float32)
    nt, nb, ny, nx = arr.shape
    with _scipy_netcdf(path, "w") as f:
        f.createDimension("time", nt)
        f.createDimension("band", nb)
        f.createDimension("y", ny)
        f.createDimension("x", nx)
        var = f.createVariable("reflectance", "f", ("time", "band", "y", "x"))
        var[:] = arr
        # 坐标变量
        for dimname, vals in (("y", da.coords["y"].values),
                              ("x", da.coords["x"].values)):
            cv = f.createVariable(dimname, "f", (dimname,))
            cv[:] = vals.astype(np.float32)


def read_netcdf(path: str) -> Tuple[np.ndarray, Dict[str, Any]]:
    """读回 NetCDF 立方体，返回 (4D array, meta)。用于自检/测试。"""
    if not os.path.exists(path):
        raise UsageError(f"netcdf not found: {path}", path=path)
    if _HAS_XARRAY:
        try:
            ds = xr.open_dataset(path, engine="scipy")
        except Exception:  # pragma: no cover
            ds = xr.open_dataset(path)
        name = "reflectance" if "reflectance" in ds else list(ds.data_vars)[0]
        arr = ds[name].transpose("time", "band", "y", "x").values.astype(np.float32)
        meta = {"name": name, "engine": "xarray"}
        ds.close()
        return arr, meta
    if _HAS_SCIPY_NC:
        with _scipy_netcdf(path, "r") as f:
            arr = f.variables["reflectance"][:].astype(np.float32).copy()
        return arr, {"name": "reflectance", "engine": "scipy"}
    raise ProcessError("no NetCDF backend available (need xarray or scipy)")


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
            "n_dates": getattr(args, "n_dates", None),
            "bands": getattr(args, "bands", None),
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
    n_dates = int(getattr(args, "n_dates", 6))
    bands = int(getattr(args, "bands", 4))

    # 0) 参数前置校验（P1）：--synthetic 时 n_dates/bands 必须合法
    if args.synthetic or not args.input:
        validate_synthetic_params(n_dates, bands)

    # 1) 获取立方体（通用契约）
    synth_info: Optional[Dict[str, Any]] = None
    input_nodata: Optional[float] = None
    if args.input and not args.synthetic:
        raw, file_bbox, input_nodata = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        # 单景多波段 → 单时相立方体 (1, bands, H, W)
        if raw.ndim == 2:
            raw = raw[np.newaxis, ...]
        cube = raw[np.newaxis, ...]
        nb = cube.shape[1]
        dates = [_dt.date.today().isoformat()]
        band_names = [DEFAULT_BAND_NAMES[b] if b < len(DEFAULT_BAND_NAMES)
                      else f"band_{b}" for b in range(nb)]
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        cube, synth_info = generate_synthetic_cube(
            bbox, n_dates=n_dates, bands=bands,
        )
        dates = synth_info["dates"]
        band_names = synth_info["band_names"]
        source_note = "synthetic"

    if cube.size == 0:
        raise ValidationError("input cube is empty")

    # 2) bbox / NoData 校验（前置，确保无效输入不创建 output 目录）
    validate_bbox(bbox)
    n_valid = int(np.count_nonzero(np.isfinite(cube)))
    if n_valid == 0:
        raise ValidationError(
            "input cube has no valid pixels (all NoData/NaN); nothing to build"
        )

    # 3) 所有校验通过后才创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 4) 组织为带坐标的 DataArray
    da = build_data_array(cube, bbox, dates, band_names)

    # 5) 写出 NetCDF 立方体
    out_nc = os.path.join(output_dir, "data_cube.nc")
    write_netcdf(da, out_nc)

    # 自检：读回验证形状一致
    read_back, _meta = read_netcdf(out_nc)
    if read_back.shape != cube.shape:
        raise ProcessError(
            f"netcdf roundtrip shape mismatch: {read_back.shape} != {cube.shape}",
        )

    # 6) 元数据 JSON
    stats = cube_statistics(cube)
    meta = {
        "source": source_note,
        "bbox": bbox,
        "shape": list(cube.shape),
        "dims": ["time", "band", "y", "x"],
        "dates": dates,
        "band_names": band_names,
        "crs": "EPSG:4326",
        "statistics": stats,
        "input_nodata": input_nodata,
        "n_valid_pixels": n_valid,
    }
    meta_path = os.path.join(output_dir, "cube_metadata.json")
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "shape": list(cube.shape),
        "n_dates": int(cube.shape[0]),
        "n_bands": int(cube.shape[1]),
        "n_valid_pixels": n_valid,
        "input_nodata": input_nodata,
        "global_mean": stats["global_mean"],
        "global_std": stats["global_std"],
        "netcdf_roundtrip_ok": True,
    }

    outputs = [
        {"path": out_nc, "kind": "netcdf", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": int(cube.shape[1])},
        {"path": meta_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] cube shape (time,band,y,x): {cube.shape}")
        print(f"[{SKILL_NAME}] dates: {len(dates)}  bands: {len(band_names)}")
        print(f"[{SKILL_NAME}] netcdf: {out_nc}")
        print(f"[{SKILL_NAME}] metadata: {meta_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
        print(f"[{SKILL_NAME}] global mean reflectance: {stats['global_mean']:.4f}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Build a multi-temporal, multi-band raster data cube (xarray/NetCDF).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input multiband GeoTIFF (treated as one time step)")
    p.add_argument("--n-dates", type=int, default=6,
                   help="number of time steps in synthetic cube (default: 6)")
    p.add_argument("--bands", type=int, default=4,
                   help="number of bands in synthetic cube (default: 4)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a physics-consistent synthetic cube (offline)")
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
