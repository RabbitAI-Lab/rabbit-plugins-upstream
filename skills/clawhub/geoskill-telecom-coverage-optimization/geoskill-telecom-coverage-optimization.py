#!/usr/bin/env python3
"""telecom-coverage-optimization — 通信覆盖优化

基于简化 Okumura-Hata 传播模型 + 地形/建筑杂波损耗，估算基站覆盖与盲区，
为通信网络规划提供依据。

- **路径损耗**：Hata 经验模型（150–1500 MHz），
  L = 69.55 + 26.16·log10(f) − 13.82·log10(hb) − a(hm)
      + (44.9 − 6.55·log10(hb))·log10(d)
  其中 a(hm) 为移动台天线高度修正，随城市规模变化；郊区/开阔地在城市值上做
  经验修正。
- **接收功率**：RSL = 发射功率 + 天线增益 − 路径损耗 − 杂波损耗（地形高差与
  建筑高度引起的附加 dB）。
- **覆盖/盲区**：RSL ≥ 门限判为覆盖，服务区内未覆盖像元为盲区。

数据源：本地多波段 GeoTIFF（DEM/建筑高度）+ 基站坐标，或 ``--synthetic`` 生成
含地形起伏与建筑簇的模拟场景用于离线测试。

隐私声明 / Privacy：默认离线运行，``--synthetic`` 完全无网络；本地处理，不上传数据。

Usage:
    python telecom-coverage-optimization.py --input terrain.tif --output-dir ./out
    python telecom-coverage-optimization.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "telecom-coverage-optimization"

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


BAND_ROLES = ["dem", "building_height"]
N_REQUIRED_BANDS = len(BAND_ROLES)
ENVIRONMENTS = ["urban", "suburban", "open"]


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# Input validation
# ---------------------------------------------------------------------------
def validate_bbox(bbox: Any) -> None:
    """Validate a W,S,E,N geographic bbox. Raises ValidationError on bad input."""
    if not isinstance(bbox, (list, tuple)) or len(bbox) != 4:
        raise ValidationError(
            f"bbox must be [W,S,E,N] (4 floats), got {bbox!r}",
            bbox=list(bbox) if hasattr(bbox, "__iter__") else None,
        )
    W, S, E, N = bbox
    for v, name in [(W, "W"), (S, "S"), (E, "E"), (N, "N")]:
        try:
            fv = float(v)
        except (TypeError, ValueError):
            raise ValidationError(
                f"bbox {name}={v!r} is not a finite number", bbox=list(bbox),
            )
        if not np.isfinite(fv):
            raise ValidationError(
                f"bbox {name}={v!r} is not a finite number", bbox=list(bbox),
            )
    if not (-180.0 <= float(W) <= 180.0 and -180.0 <= float(E) <= 180.0):
        raise ValidationError(
            f"bbox longitude out of range [-180,180]: W={W}, E={E}", bbox=list(bbox),
        )
    if not (-90.0 <= float(S) <= 90.0 and -90.0 <= float(N) <= 90.0):
        raise ValidationError(
            f"bbox latitude out of range [-90,90]: S={S}, N={N}", bbox=list(bbox),
        )
    if float(W) >= float(E) and not (float(W) > 170.0 and float(E) < -170.0):
        raise ValidationError(
            f"bbox has W >= E ({W} >= {E}); crossing the antimeridian "
            f"(W near +180, E near -180) is not supported. "
            f"Pass a bbox with W < E (e.g. split into two bboxes).",
            bbox=list(bbox),
        )
    if float(W) > 170.0 and float(E) < -170.0:
        raise ValidationError(
            f"bbox crosses the antimeridian (W={W}, E={E}); not supported. "
            f"Split into two bboxes: [{W}, {S}, 180.0, {N}] and [-180.0, {S}, {E}, {N}].",
            bbox=list(bbox),
        )
    if float(S) >= float(N):
        raise ValidationError(
            f"bbox has S >= N ({S} >= {N}); south must be strictly less than north.",
            bbox=list(bbox),
        )
    if (float(E) - float(W)) < 1e-4 or (float(N) - float(S)) < 1e-4:
        raise ValidationError(
            f"bbox is too small (extent < 1e-4 degrees): W={W},S={S},E={E},N={N}.",
            bbox=list(bbox),
        )


def validate_params(frequency: float, hm: float, tx_power: float, gain: float,
                    threshold: float, environment: str) -> None:
    """Cross-check CLI params beyond argparse type coercion."""
    if not isinstance(frequency, (int, float)) or not np.isfinite(frequency) or frequency <= 0:
        raise ValidationError(
            f"frequency must be a finite positive number, got {frequency!r}", frequency=frequency,
        )
    if frequency < 100.0 or frequency > 6000.0:
        # Hata 经验式适用范围 150–1500 MHz；扩展到 100–6000 MHz 仍用同式但误差大
        raise ValidationError(
            f"frequency {frequency} MHz out of practical Hata range [100, 6000] MHz",
            frequency=frequency,
        )
    if not isinstance(hm, (int, float)) or not np.isfinite(hm) or hm <= 0:
        raise ValidationError(f"hm (mobile height) must be > 0, got {hm!r}", hm=hm)
    if hm > 100.0:
        raise ValidationError(f"hm {hm} m implausibly large (> 100 m)", hm=hm)
    if not isinstance(tx_power, (int, float)) or not np.isfinite(tx_power):
        raise ValidationError(f"tx-power must be finite, got {tx_power!r}", tx_power=tx_power)
    if tx_power < -10.0 or tx_power > 60.0:
        raise ValidationError(
            f"tx-power {tx_power} dBm out of typical range [-10, 60] dBm", tx_power=tx_power,
        )
    if not isinstance(gain, (int, float)) or not np.isfinite(gain):
        raise ValidationError(f"gain must be finite, got {gain!r}", gain=gain)
    if gain < -5.0 or gain > 40.0:
        raise ValidationError(
            f"gain {gain} dBi out of typical range [-5, 40] dBi", gain=gain,
        )
    if not isinstance(threshold, (int, float)) or not np.isfinite(threshold):
        raise ValidationError(
            f"threshold must be finite, got {threshold!r}", threshold=threshold,
        )
    if threshold < -150.0 or threshold > 0.0:
        raise ValidationError(
            f"threshold {threshold} dBm out of typical range [-150, 0] dBm", threshold=threshold,
        )
    if environment not in ENVIRONMENTS:
        raise ValidationError(
            f"environment must be one of {ENVIRONMENTS}, got {environment!r}",
            environment=environment,
        )


# ---------------------------------------------------------------------------
# 核心算法（Okumura-Hata 简化）
# ---------------------------------------------------------------------------
def mobile_height_correction(f_mhz: float, hm: float, environment: str = "urban") -> float:
    """移动台天线高度修正因子 a(hm)（dB）。

    中小城市：a = (1.1·log10(f) − 0.7)·hm − (1.56·log10(f) − 0.8)
    大城市在高频段略有差异，这里做简化处理。
    """
    f = float(f_mhz)
    if f <= 0:
        raise ValidationError(f"frequency must be > 0, got {f}")
    lf = np.log10(f)
    hm = float(hm)
    if environment == "urban" and f >= 400:
        # 大城市高频段经验式
        a = 3.2 * (np.log10(11.75 * hm)) ** 2 - 4.97
    else:
        a = (1.1 * lf - 0.7) * hm - (1.56 * lf - 0.8)
    return float(a)


def hata_path_loss(
    f_mhz: float,
    hb: float,
    hm: float,
    d_km: np.ndarray,
    environment: str = "urban",
) -> np.ndarray:
    """Hata 路径损耗 (dB)，d_km 为距离栅格(km)。

    城市模型为基础；郊区在城区值上减 2·[log10(f/28)]² + 5.4；
    开阔地再减 4.78·(log10 f)² − 18.33·log10 f − 40.94（相对郊区）。
    """
    f = float(f_mhz)
    if f <= 0:
        raise ValidationError(f"frequency must be > 0, got {f}")
    if hb <= 0 or hm <= 0:
        raise ValidationError("antenna heights must be > 0")
    lf = np.log10(f)
    lhb = np.log10(float(hb))
    a_hm = mobile_height_correction(f, hm, environment)

    d = np.asarray(d_km, dtype=np.float32)
    d_safe = np.clip(d, 1e-3, None)  # Hata 适用 d >= ~1km 附近，下限防 log(0)
    ld = np.log10(d_safe)

    urban = (69.55 + 26.16 * lf - 13.82 * lhb - a_hm
             + (44.9 - 6.55 * lhb) * ld)

    if environment == "suburban":
        loss = urban - 2.0 * (np.log10(f / 28.0)) ** 2 - 5.4
    elif environment == "open":
        suburban = urban - 2.0 * (np.log10(f / 28.0)) ** 2 - 5.4
        loss = suburban - 4.78 * lf ** 2 + 18.33 * lf - 40.94
    else:
        loss = urban
    return loss.astype(np.float32)


def clutter_loss(dem: np.ndarray, building: np.ndarray, hb: float,
                 terrain_weight: float = 0.05, building_weight: float = 0.3) -> np.ndarray:
    """杂波损耗 (dB)：相对地形高差 + 建筑高度遮挡的附加衰减。

    地形高于基站有效高度时产生绕射损耗（按高差线性近似），建筑高度直接折算
    为穿透/绕射附加损耗。
    """
    dem = np.asarray(dem, dtype=np.float32)
    building = np.asarray(building, dtype=np.float32)
    base = float(np.nanpercentile(dem, 50))
    terrain_excess = np.clip(dem - (base + float(hb)), 0.0, None)
    loss = float(terrain_weight) * terrain_excess + float(building_weight) * np.clip(building, 0, None)
    return loss.astype(np.float32)


def received_power(
    tx_dbm: float,
    gain_db: float,
    path_loss: np.ndarray,
    clutter: Optional[np.ndarray] = None,
) -> np.ndarray:
    """接收信号电平 RSL = 发射功率 + 天线增益 − 路径损耗 − 杂波损耗 (dBm)。"""
    rsl = float(tx_dbm) + float(gain_db) - np.asarray(path_loss, dtype=np.float32)
    if clutter is not None:
        rsl = rsl - np.asarray(clutter, dtype=np.float32)
    return rsl.astype(np.float32)


def distance_km_grid(bbox: List[float], height: int, width: int,
                     tower_lon: float, tower_lat: float) -> np.ndarray:
    """每个像元到基站的大圆距离近似(km)（等距柱状投影近似）。"""
    lat_mid = 0.5 * (bbox[1] + bbox[3])
    kx = 111.320 * np.cos(np.deg2rad(lat_mid))
    ky = 110.574
    xs = np.linspace(bbox[0], bbox[2], width, dtype=np.float32)
    ys = np.linspace(bbox[3], bbox[1], height, dtype=np.float32)  # 行向下纬度递减
    xx, yy = np.meshgrid(xs, ys)
    dx = (xx - tower_lon) * kx
    dy = (yy - tower_lat) * ky
    return np.sqrt(dx * dx + dy * dy).astype(np.float32)


def coverage_from_towers(
    bbox: List[float],
    height: int,
    width: int,
    dem: np.ndarray,
    building: np.ndarray,
    towers: List[Dict[str, Any]],
    f_mhz: float,
    hm: float,
    environment: str,
    tx_dbm: float,
    gain_db: float,
    threshold_dbm: float,
) -> Tuple[np.ndarray, np.ndarray]:
    """多基站覆盖：逐基站算 RSL，逐像元取最强信号。

    返回 (best_rsl, covered_mask bool)。
    """
    best = np.full((height, width), -1e9, dtype=np.float32)
    for tw in towers:
        hb = float(tw.get("height", 30.0))
        d = distance_km_grid(bbox, height, width, tw["lon"], tw["lat"])
        pl = hata_path_loss(f_mhz, hb, hm, d, environment)
        cl = clutter_loss(dem, building, hb)
        rsl = received_power(tw.get("power", tx_dbm), tw.get("gain", gain_db), pl, cl)
        best = np.maximum(best, rsl)
    covered = best >= float(threshold_dbm)
    return best, covered


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic_cube(
    bbox: List[float], width: int = 128, height: int = 128, seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成 (2,H,W)：DEM/建筑高度；并布置若干基站。"""
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    ny = yy / max(height - 1, 1)
    nx = xx / max(width - 1, 1)
    dem = (50.0 + 30.0 * np.sin(np.pi * nx) * np.cos(np.pi * ny)
           + rng.normal(0, 1.0, (height, width))).astype(np.float32)

    # 建筑簇：城市中心高
    building = np.zeros((height, width), dtype=np.float32)
    for (fx, fy, amp, sig) in [(0.5, 0.5, 60.0, 0.15), (0.25, 0.7, 30.0, 0.10), (0.75, 0.3, 35.0, 0.12)]:
        building += amp * np.exp(-(((nx - fx) ** 2 + (ny - fy) ** 2)) / (2 * sig ** 2))
    building = (building + np.clip(rng.normal(0, 2, building.shape), -2, 5)).astype(np.float32)
    building = np.clip(building, 0, None)

    towers = [
        {"lon": bbox[0] + 0.5 * (bbox[2] - bbox[0]), "lat": bbox[1] + 0.5 * (bbox[3] - bbox[1]),
         "height": 40.0, "power": 43.0, "gain": 15.0},
        {"lon": bbox[0] + 0.25 * (bbox[2] - bbox[0]), "lat": bbox[1] + 0.3 * (bbox[3] - bbox[1]),
         "height": 30.0, "power": 40.0, "gain": 12.0},
    ]
    cube = np.stack([dem, building], axis=0).astype(np.float32)
    info = {"bbox": bbox, "width": width, "height": height,
            "band_roles": BAND_ROLES, "towers": towers}
    return cube, info


def default_towers(bbox: List[float]) -> List[Dict[str, Any]]:
    """真实输入模式下未指定基站时，在中心放一座默认基站。"""
    return [{"lon": 0.5 * (bbox[0] + bbox[2]), "lat": 0.5 * (bbox[1] + bbox[3]),
             "height": 30.0, "power": 43.0, "gain": 15.0}]


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


def towers_to_geojson(towers):
    feats = []
    for i, t in enumerate(towers):
        feats.append({"type": "Feature", "id": i,
                      "geometry": {"type": "Point", "coordinates": [round(t["lon"], 6), round(t["lat"], 6)]},
                      "properties": {"tower_id": i, "height_m": t.get("height", 30.0),
                                     "power_dbm": t.get("power", 43.0), "gain_db": t.get("gain", 15.0)}})
    return {"type": "FeatureCollection", "features": feats}


def write_manifest(output_dir, args, outputs, qa, started_at, exit_code, bbox):
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME, skill_version=VERSION, command=cmd,
        started_at=started_at, finished_at=_utc_now(), exit_code=exit_code,
        inputs={"input": getattr(args, "input", None),
                "environment": getattr(args, "environment", None),
                "synthetic": bool(getattr(args, "synthetic", False)), "bbox": bbox},
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

    # ---- Validate CLI / params up front (no filesystem side effects yet) ----
    validate_params(args.frequency, args.hm, args.tx_power, args.gain,
                    args.threshold, args.environment)
    bbox = list(args.bbox) if args.bbox else None

    synth_info = None
    towers = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        if args.bbox is not None:
            validate_bbox(bbox)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox)
        cube, synth_info = generate_synthetic_cube(bbox)
        towers = synth_info["towers"]
        source_note = "synthetic"

    if cube.size == 0:
        raise ValidationError("input raster is empty")
    if cube.ndim != 3 or cube.shape[0] < N_REQUIRED_BANDS:
        raise ValidationError(
            f"input must have >= {N_REQUIRED_BANDS} bands ({BAND_ROLES}); got {cube.shape}")

    # ---- All validation passed — safe to create output directory ----
    os.makedirs(output_dir, exist_ok=True)

    dem, building = cube[0], cube[1]
    _, h, w = cube.shape
    if towers is None:
        towers = default_towers(bbox)

    best_rsl, covered = coverage_from_towers(
        bbox, h, w, dem, building, towers,
        f_mhz=args.frequency, hm=args.hm, environment=args.environment,
        tx_dbm=args.tx_power, gain_db=args.gain, threshold_dbm=args.threshold,
    )
    coverage_frac = float(np.mean(covered))
    blind_frac = 1.0 - coverage_frac

    out_rsl = os.path.join(output_dir, "signal_strength.tif")
    write_geotiff(out_rsl, best_rsl, bbox)
    out_cov = os.path.join(output_dir, "coverage_mask.tif")
    write_geotiff(out_cov, covered.astype(np.float32), bbox, nodata=-1.0)
    towers_path = os.path.join(output_dir, "towers.geojson")
    with open(towers_path, "w", encoding="utf-8") as f:
        json.dump(towers_to_geojson(towers), f, ensure_ascii=False)

    report = {
        "source": source_note, "environment": args.environment,
        "frequency_mhz": args.frequency, "threshold_dbm": args.threshold,
        "n_towers": len(towers),
        "coverage_fraction": coverage_frac, "blind_fraction": blind_frac,
        "mean_rsl_dbm": float(np.mean(best_rsl)),
        "min_rsl_dbm": float(np.min(best_rsl)), "max_rsl_dbm": float(np.max(best_rsl)),
        "suggestion": ("盲区占比偏高(>30%)，建议增补基站或提高发射功率/天线高度。"
                       if blind_frac > 0.3 else "覆盖良好，盲区占比可接受。"),
    }
    report_path = os.path.join(output_dir, "coverage_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    qa = {"source": source_note, "coverage_fraction": coverage_frac,
          "blind_fraction": blind_frac, "n_towers": len(towers),
          "mean_rsl_dbm": float(np.mean(best_rsl))}
    outputs = [
        {"path": out_rsl, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": out_cov, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": towers_path, "kind": "vector", "crs_epsg": 4326, "bbox_wgs84": bbox, "feature_count": len(towers)},
        {"path": report_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] towers: {len(towers)}  env: {args.environment}  f: {args.frequency} MHz")
        print(f"[{SKILL_NAME}] coverage: {coverage_frac:.3f}  blind: {blind_frac:.3f}")
        print(f"[{SKILL_NAME}] report: {report_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser():
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Telecom coverage optimization via simplified Okumura-Hata propagation.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"))
    p.add_argument("--input", help="input multi-band GeoTIFF (DEM/building height)")
    p.add_argument("--synthetic", action="store_true")
    p.add_argument("--environment", default="urban", choices=ENVIRONMENTS,
                   help="propagation environment (default: urban)")
    p.add_argument("--frequency", type=float, default=1800.0, help="carrier frequency MHz (default: 1800)")
    p.add_argument("--hm", type=float, default=1.5, help="mobile antenna height m (default: 1.5)")
    p.add_argument("--tx-power", type=float, default=43.0, help="TX power dBm (default: 43)")
    p.add_argument("--gain", type=float, default=15.0, help="antenna gain dBi (default: 15)")
    p.add_argument("--threshold", type=float, default=-100.0, help="coverage threshold dBm (default: -100)")
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
