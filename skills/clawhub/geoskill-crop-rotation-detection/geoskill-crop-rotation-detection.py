#!/usr/bin/env python3
"""crop-rotation-detection — 作物轮作检测

对多年度作物分类栅格逐像元编码种植序列，识别轮作模式（单作 / N 年轮作 /
不规则），并统计各模式的像元频率，输出轮作分区与模式频率报告。

核心算法
--------
- **序列编码**：把每个像元的逐年作物类别向量映射为唯一序列 ID。
- **模式识别**：求序列最小周期 p；p=1→单作，1<p<年数→p 年轮作，否则不规则。
- **频率统计**：按模式聚合像元数与占比。

数据源：本地多年度分类栅格（波段=年份）或 ``--synthetic`` 离线模拟。

隐私声明 / Privacy：默认离线，``--synthetic`` 完全无网络，本地处理不上传。

Usage:
    python crop-rotation-detection.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "crop-rotation-detection"

# 作物类别编码
CLASS_NAMES = {0: "non-crop", 1: "corn", 2: "soybean", 3: "wheat"}

try:
    from _geoskill_core.errors import (
        GeoSkillError, UsageError, ValidationError, ProcessError, DependencyError, to_exit_code,
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

    class DependencyError(GeoSkillError):
        def __init__(self, m, **k): super().__init__(m, code=3, kind="EDepend", **k)

    class ProcessError(GeoSkillError):
        def __init__(self, m, **k): super().__init__(m, code=7, kind="EProcess", **k)

    def to_exit_code(exc):
        return getattr(exc, "code", 7)

    OutputManifest = None
    OutputFile = None


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def encode_sequences(class_stack: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """把 (years, H, W) 分类栈逐像元编码为序列 ID。

    返回 (seq_ids (H,W) int32, unique_seqs (N, years) int32)。
    """
    class_stack = np.asarray(class_stack)
    if class_stack.ndim != 3 or class_stack.shape[0] < 2:
        raise ValidationError("class_stack must be (years>=2, H, W)")
    years, h, w = class_stack.shape
    cols = class_stack.reshape(years, -1).T.astype(np.int32)  # (H*W, years)
    unique_seqs, inverse = np.unique(cols, axis=0, return_inverse=True)
    seq_ids = inverse.reshape(h, w).astype(np.int32)
    return seq_ids, unique_seqs.astype(np.int32)


def minimal_period(seq: np.ndarray) -> int:
    """求序列最小周期 p：满足 seq[i] == seq[i % p] 对所有 i 成立的最小 p。"""
    seq = np.asarray(seq).ravel()
    n = seq.shape[0]
    for p in range(1, n + 1):
        base = seq[:p]
        if np.all(seq == np.tile(base, int(np.ceil(n / p)))[:n]):
            return p
    return n


def recognize_pattern(seq: np.ndarray) -> str:
    """识别单个种植序列的轮作模式。"""
    seq = np.asarray(seq).ravel()
    n = seq.shape[0]
    if np.all(seq == 0):
        return "non-crop"
    p = minimal_period(seq)
    if p == 1:
        return "monoculture"
    if p < n:
        return f"rotation-{p}yr"
    # p == n：无法由重复确认周期
    return "irregular"


def rotation_frequency(class_stack: np.ndarray) -> Dict[str, Any]:
    """编码 + 逐序列模式识别 + 按模式聚合频率。"""
    seq_ids, unique_seqs = encode_sequences(class_stack)
    h, w = seq_ids.shape
    total = h * w
    pattern_of_seq: Dict[int, str] = {}
    for i, seqrow in enumerate(unique_seqs):
        pattern_of_seq[i] = recognize_pattern(seqrow)
    pattern_map = np.array([pattern_of_seq[int(sid)] for sid in seq_ids.ravel()]).reshape(h, w)

    counts: Dict[str, int] = {}
    for sid in range(unique_seqs.shape[0]):
        pat = pattern_of_seq[sid]
        counts[pat] = counts.get(pat, 0) + int(np.sum(seq_ids == sid))
    freq = {pat: {"count": int(c), "fraction": float(c / total)} for pat, c in counts.items()}
    return {
        "seq_ids": seq_ids,
        "unique_seqs": unique_seqs,
        "pattern_map": pattern_map,
        "pattern_of_seq": pattern_of_seq,
        "frequency": freq,
        "n_unique_sequences": int(unique_seqs.shape[0]),
        "n_patterns": int(len(counts)),
    }


def detect_rotation(class_stack: np.ndarray) -> Dict[str, Any]:
    """主流程封装（含统计摘要）。"""
    res = rotation_frequency(class_stack)
    res["stats"] = {
        "n_years": int(class_stack.shape[0]),
        "n_unique_sequences": res["n_unique_sequences"],
        "n_patterns": res["n_patterns"],
        "frequency": res["frequency"],
    }
    return res


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], width: int = 40, height: int = 40,
                       n_years: int = 6, seed: int = 42):
    """三个轮作区：玉米单作 / 玉米-大豆 2 年轮作 / 玉米-大豆-小麦 3 年轮作。"""
    rng = np.random.default_rng(seed)
    stack = np.zeros((n_years, height, width), dtype=np.int32)
    half_w = width // 2
    half_h = height // 2
    # 区 A 左半：玉米单作 (1)
    for y in range(n_years):
        stack[y, :, :half_w] = 1
    # 区 B 右上：玉米-大豆 2 年轮作
    for y in range(n_years):
        stack[y, :half_h, half_w:] = 1 if y % 2 == 0 else 2
    # 区 C 右下：玉米-大豆-小麦 3 年轮作
    seq3 = [1, 2, 3]
    for y in range(n_years):
        stack[y, half_h:, half_w:] = seq3[y % 3]

    # 少量噪声：随机翻转极少像元（保持主模式可识别）
    noise = rng.random(stack.shape) < 0.005
    stack[noise] = rng.integers(1, 4, size=int(noise.sum()))

    info = {"bbox": bbox, "width": width, "height": height, "n_years": n_years,
            "class_names": CLASS_NAMES,
            "expected_patterns": ["monoculture", "rotation-2yr", "rotation-3yr"]}
    return stack, info


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
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(path: str, cube: np.ndarray, bbox: List[float], nodata: float = -9999.0) -> None:
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
    """Read a multi-year classification stack, returning (cube, bbox) with NoData→NaN."""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read(masked=True).astype(np.float32)
        cube = np.ma.filled(cube, np.nan)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return cube, bbox


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
        inputs={"input": getattr(args, "input", None), "method": getattr(args, "method", None),
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

    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)  # bands = years of crop class
        bbox = bbox if bbox is not None else file_bbox
        stack = np.round(cube).astype(np.int32)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        stack, synth_info = generate_synthetic(bbox)
        source_note = "synthetic"

    # 校验（先于 makedirs）
    if stack.size == 0:
        raise ValidationError("input raster is empty")
    if stack.ndim != 3 or stack.shape[0] < 2:
        raise ValidationError("input needs >=2 bands as a multi-year classification")
    if bbox is not None:
        validate_bbox(bbox)
    # 对原始 float 立方体检查 NoData（int 转换会把 NaN 折成 0）：
    #   真实模式用 cube，合成模式用 stack（因为 cube 未定义）
    raw = cube if (args.input and not args.synthetic) else stack.astype(np.float32)
    if not np.any(np.isfinite(raw)):
        raise ValidationError(
            "input stack has no valid (finite) pixels across all years (all NoData or NaN)",
        )

    # 现在 makedirs
    os.makedirs(output_dir, exist_ok=True)

    res = detect_rotation(stack)

    seq_tif = os.path.join(output_dir, "rotation_sequences.tif")
    write_geotiff(seq_tif, res["seq_ids"].astype(np.float32), bbox)

    # 模式编码为整数：按 frequency 出现顺序
    patterns_sorted = sorted(res["frequency"].keys())
    pat_to_code = {p: i + 1 for i, p in enumerate(patterns_sorted)}
    pattern_code = np.vectorize(lambda x: pat_to_code.get(x, 0))(res["pattern_map"]).astype(np.float32)
    pat_tif = os.path.join(output_dir, "rotation_pattern.tif")
    write_geotiff(pat_tif, pattern_code, bbox)

    freq_json = os.path.join(output_dir, "rotation_frequency.json")
    with open(freq_json, "w", encoding="utf-8") as f:
        json.dump({
            "n_years": int(stack.shape[0]),
            "class_names": {str(k): v for k, v in CLASS_NAMES.items()},
            "n_unique_sequences": res["n_unique_sequences"],
            "pattern_code_map": pat_to_code,
            "frequency": res["frequency"],
            "unique_sequences": res["unique_seqs"].tolist(),
        }, f, ensure_ascii=False, indent=2)

    qa = {"source": source_note, "method": args.method,
          "n_unique_sequences": res["n_unique_sequences"], "n_patterns": res["n_patterns"],
          "frequency": res["frequency"]}
    if synth_info is not None:
        qa["synthetic"] = {k: v for k, v in synth_info.items() if k != "bbox"}

    outputs = [
        {"path": seq_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": pat_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": freq_json, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] years: {stack.shape[0]}  unique sequences: {res['n_unique_sequences']}")
        for pat, info in sorted(res["frequency"].items(), key=lambda kv: -kv[1]["fraction"]):
            print(f"  {pat}: {info['count']} px ({info['fraction'] * 100:.1f}%)")
        print(f"[{SKILL_NAME}] output: {freq_json}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Crop rotation detection via multi-year sequence encoding and period-based pattern recognition.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input multi-year crop-class GeoTIFF (bands = years)")
    p.add_argument("--method", default="sequence", choices=["sequence", "frequency"],
                   help="detection method (default: sequence)")
    p.add_argument("--synthetic", action="store_true", help="generate synthetic scene (offline)")
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
