#!/usr/bin/env python3
"""lulc-change-matrix — 土地覆被转移矩阵

对两期土地覆被分类栅格（整数类别）做逐像元交叉制表，量化类别间的
转移（conversion）关系：

1. **转移矩阵**：统计每个 (t1 类别 → t2 类别) 组合的像元数量，
   对角线为未变化像元，非对角线为发生转移的像元。
2. **变化面积统计**：按类别计算总面积、毛损失、毛增益、净变化，
   并结合 bbox 换算为平方公里。
3. **Sankey 流数据**：把非对角线转移导出为 nodes + links，
   可直接用于 Sankey 流向图可视化。

合成模式生成两期分类，并向其中注入确定数量的类别转移
（如 cropland → built_up），便于离线验证算法正确性。

数据源：本地两期分类 GeoTIFF（整数类别），或 ``--synthetic`` 合成对。

隐私声明 / Privacy：
- 默认离线运行，不访问任何网络服务。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python lulc-change-matrix.py --t1 cls_2015.tif --t2 cls_2020.tif
    python lulc-change-matrix.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "lulc-change-matrix"

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


CLASS_NAMES = ["water", "vegetation", "cropland", "built_up", "bare_soil"]


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


def class_name(idx: int) -> str:
    if 0 <= idx < len(CLASS_NAMES):
        return CLASS_NAMES[idx]
    return f"class_{idx}"


def validate_bbox(bbox) -> None:
    """校验 bbox 是 W<E、S<N、lon∈[-180,180]、lat∈[-90,90]、非零面积。
    跨 180° 经线必须拆成两个子 bbox。"""
    if bbox is None:
        raise UsageError("provide --bbox (synthetic mode) or --t1/--t2 rasters")
    w, s, e, n = [float(v) for v in bbox]
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"bbox longitude out of range [-180, 180]: W={w}, E={e}",
            bbox=list(bbox),
        )
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"bbox latitude out of range [-90, 90]: S={s}, N={n}",
            bbox=list(bbox),
        )
    if w >= e:
        if w == e:
            raise ValidationError(
                f"bbox has zero width: W==E=={w} (degenerate AOI)",
                bbox=list(bbox),
            )
        raise ValidationError(
            f"bbox is reversed (W={w} >= E={e}); need W < E. "
            f"For datelines that cross 180° (e.g. 179.5 -> -179.5), "
            f"split into two sub-bboxes and run the skill on each separately.",
            bbox=list(bbox),
        )
    if s >= n:
        raise ValidationError(
            f"bbox is reversed (S={s} >= N={n}); need S < N",
            bbox=list(bbox),
        )


def _pixel_area_km2(bbox: List[float], shape: Tuple[int, int]) -> Tuple[float, float]:
    """返回 (单像元面积 km², 区域总面积 km²)，平面近似。"""
    w_deg = bbox[2] - bbox[0]
    h_deg = bbox[3] - bbox[1]
    lat_mid = (bbox[1] + bbox[3]) / 2.0
    km_per_deg_lon = 111.32 * np.cos(np.deg2rad(lat_mid))
    km_per_deg_lat = 110.57
    total = float(w_deg * km_per_deg_lon * h_deg * km_per_deg_lat)
    h, w = shape
    px = total / max(h * w, 1)
    return px, total


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def transition_counts(
    t1: np.ndarray,
    t2: np.ndarray,
    classes: Optional[List[int]] = None,
) -> Tuple[np.ndarray, List[int]]:
    """逐像元交叉制表，返回 (混淆/转移矩阵, 类别标签列表)。

    矩阵行 = t1（前期）类别，列 = t2（后期）类别，元素为像元数。
    """
    t1 = np.asarray(t1)
    t2 = np.asarray(t2)
    if t1.shape != t2.shape:
        raise ValidationError(
            f"t1 shape {t1.shape} != t2 shape {t2.shape}",
            t1_shape=list(t1.shape), t2_shape=list(t2.shape),
        )
    if t1.size == 0:
        raise ValidationError("input rasters are empty")

    if classes is None:
        classes = sorted({int(v) for v in np.unique(t1)} | {int(v) for v in np.unique(t2)})
    classes = [int(c) for c in classes]
    idx = {c: i for i, c in enumerate(classes)}

    cm = np.zeros((len(classes), len(classes)), dtype=np.int64)
    f1 = t1.ravel()
    f2 = t2.ravel()
    # 只统计两期都属于已知类别的像元
    i1 = np.array([idx.get(int(v), -1) for v in f1], dtype=np.int64)
    i2 = np.array([idx.get(int(v), -1) for v in f2], dtype=np.int64)
    valid = (i1 >= 0) & (i2 >= 0)
    np.add.at(cm, (i1[valid], i2[valid]), 1)
    return cm, classes


def matrix_proportions(cm: np.ndarray) -> np.ndarray:
    """转移矩阵归一化为占全部像元的比例（元素和为 1）。"""
    total = cm.sum()
    if total == 0:
        return cm.astype(np.float64)
    return (cm.astype(np.float64) / float(total))


def change_summary(
    cm: np.ndarray,
    classes: List[int],
    bbox: List[float],
    shape: Tuple[int, int],
) -> Dict[str, Any]:
    """由转移矩阵计算变化统计：总量、逐类毛损失/毛增益/净变化及面积。"""
    total_px = int(cm.sum())
    diag = int(np.trace(cm))
    changed_px = total_px - diag
    px_area, total_area = _pixel_area_km2(bbox, shape)

    row_sum = cm.sum(axis=1)  # t1 各类总量（前期面积）
    col_sum = cm.sum(axis=0)  # t2 各类总量（后期面积）
    per_class = []
    for i, c in enumerate(classes):
        t1_count = int(row_sum[i])
        t2_count = int(col_sum[i])
        persist = int(cm[i, i])
        gross_loss = t1_count - persist     # 从该类转出
        gross_gain = t2_count - persist     # 转入该类
        net = gross_gain - gross_loss
        per_class.append({
            "class_index": int(c),
            "class_name": class_name(int(c)),
            "t1_pixels": t1_count,
            "t2_pixels": t2_count,
            "persistent_pixels": persist,
            "gross_loss_pixels": int(gross_loss),
            "gross_gain_pixels": int(gross_gain),
            "net_change_pixels": int(net),
            "t1_area_km2": t1_count * px_area,
            "t2_area_km2": t2_count * px_area,
            "net_change_area_km2": net * px_area,
        })

    return {
        "total_pixels": total_px,
        "changed_pixels": int(changed_px),
        "unchanged_pixels": int(diag),
        "change_fraction": (changed_px / total_px) if total_px else 0.0,
        "pixel_area_km2": px_area,
        "total_area_km2": total_area,
        "changed_area_km2": changed_px * px_area,
        "per_class": per_class,
    }


def sankey_data(cm: np.ndarray, classes: List[int]) -> Dict[str, Any]:
    """把非对角线转移导出为 Sankey 图所需的 nodes + links。"""
    nodes: List[Dict[str, Any]] = []
    node_id: Dict[str, int] = {}

    def _node(side: str, c: int) -> int:
        key = f"{side}:{c}"
        if key not in node_id:
            node_id[key] = len(nodes)
            nodes.append({
                "id": key,
                "name": f"{class_name(c)} ({side})",
                "class_index": int(c),
                "side": side,
            })
        return node_id[key]

    links: List[Dict[str, Any]] = []
    for i, c1 in enumerate(classes):
        for j, c2 in enumerate(classes):
            if i == j:
                continue
            val = int(cm[i, j])
            if val <= 0:
                continue
            links.append({
                "source": _node("from", int(c1)),
                "target": _node("to", int(c2)),
                "from_class": int(c1),
                "to_class": int(c2),
                "from_name": class_name(int(c1)),
                "to_name": class_name(int(c2)),
                "value": val,
            })
    return {"nodes": nodes, "links": links}


# ---------------------------------------------------------------------------
# 合成数据：两期分类 + 注入确定数量的转移（离线）
# ---------------------------------------------------------------------------
def generate_synthetic_pair(
    bbox: List[float],
    n_classes: int = 5,
    width: int = 96,
    height: int = 96,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成两期 (H,W) 整数分类栅格，并注入确定数量的类别转移。

    前期 t1 用斜向条带分区构造；后期 t2 = t1，然后把中央块内
    属于 src 类的像元确定性地转为 dst 类（src=n-2 → dst=n-1），
    注入数量记录在 info['injected']，供验证使用。
    """
    n_classes = int(np.clip(n_classes, 2, len(CLASS_NAMES)))
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    yn = yy / max(height - 1, 1)
    xn = xx / max(width - 1, 1)

    t1 = np.zeros((height, width), dtype=np.int32)
    g = xn * 0.6 + yn * 0.4
    edges = np.linspace(0.0, 1.0, n_classes + 1)
    for i in range(n_classes):
        upper = edges[i + 1] + (1e-6 if i == n_classes - 1 else 0.0)
        t1[(g >= edges[i]) & (g < upper)] = i

    t2 = t1.copy()
    src = n_classes - 2
    dst = n_classes - 1
    block = np.zeros((height, width), dtype=bool)
    block[height // 4: 3 * height // 4, width // 4: 3 * width // 4] = True
    cand = (t1 == src) & block
    if int(cand.sum()) == 0:
        cand = (t1 == src)
    injected = int(cand.sum())
    t2[cand] = dst

    info = {
        "bbox": bbox,
        "width": width,
        "height": height,
        "n_classes": n_classes,
        "class_names": [class_name(i) for i in range(n_classes)],
        "injected": {
            "from_class": int(src),
            "to_class": int(dst),
            "from_name": class_name(src),
            "to_name": class_name(dst),
            "pixel_count": injected,
        },
    }
    return t1, t2, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O（直接用 rasterio，保证离线可用）
# ---------------------------------------------------------------------------
def write_geotiff(
    path: str,
    array: np.ndarray,
    bbox: List[float],
    dtype: str = "int32",
    nodata: Optional[float] = None,
) -> None:
    import rasterio
    from rasterio.transform import from_bounds

    arr = array
    if arr.ndim == 2:
        arr = arr[np.newaxis, ...]
    nb, h, w = arr.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    profile = {
        "driver": "GTiff", "height": h, "width": w, "count": nb,
        "dtype": dtype, "crs": "EPSG:4326", "transform": transform,
        "nodata": nodata, "compress": "deflate",
    }
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(arr[b].astype(dtype), b + 1)


def read_class_raster(path: str) -> Tuple[np.ndarray, List[float]]:
    """读取单波段整数分类栅格，返回 ((H,W) int32, bbox)。"""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        arr = src.read(1)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return arr.astype(np.int32), bbox


def write_transition_csv(
    path: str,
    cm: np.ndarray,
    classes: List[int],
) -> None:
    """用 pandas 把转移矩阵写成带行列标签 + 合计的 CSV。"""
    import pandas as pd
    labels = [f"{c}_{class_name(c)}" for c in classes]
    df = pd.DataFrame(cm.astype(np.int64), index=labels, columns=labels)
    df.index.name = "from_t1 \\ to_t2"
    df["row_total"] = df.sum(axis=1)
    col_total = df.sum(axis=0)
    col_total.name = "col_total"
    df = pd.concat([df, col_total.to_frame().T])
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    df.to_csv(path, encoding="utf-8")


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
            "t1": getattr(args, "t1", None),
            "t2": getattr(args, "t2", None),
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

    # 1) 获取两期分类栅格
    #    通用契约：给了 --t1/--t2 就读真实栅格；否则（含 --synthetic）走合成。
    synth_info: Optional[Dict[str, Any]] = None
    if (args.t1 or args.t2) and not args.synthetic:
        if not (args.t1 and args.t2):
            raise UsageError("real mode requires both --t1 and --t2 rasters")
        t1, b1 = read_class_raster(args.t1)
        t2, b2 = read_class_raster(args.t2)
        if t1.shape != t2.shape:
            raise ValidationError(
                f"t1 shape {t1.shape} != t2 shape {t2.shape}",
                t1_shape=list(t1.shape), t2_shape=list(t2.shape),
            )
        bbox = bbox if bbox is not None else b1
        if bbox is not None:
            validate_bbox(bbox)
        source_note = f"{args.t1} + {args.t2}"
    else:
        validate_bbox(bbox)
        t1, t2, synth_info = generate_synthetic_pair(
            bbox, n_classes=args.n_classes,
        )
        source_note = "synthetic"

    # 校验通过后再建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 2) 转移矩阵
    cm, classes = transition_counts(t1, t2)
    summary = change_summary(cm, classes, bbox, t1.shape)
    sk = sankey_data(cm, classes)

    # 3) 写出产物
    csv_path = os.path.join(output_dir, "transition_matrix.csv")
    write_transition_csv(csv_path, cm, classes)

    change_path = os.path.join(output_dir, "change_areas.json")
    change_doc = {"classes": classes, "summary": summary}
    with open(change_path, "w", encoding="utf-8") as f:
        json.dump(change_doc, f, ensure_ascii=False, indent=2)

    sankey_path = os.path.join(output_dir, "sankey.json")
    with open(sankey_path, "w", encoding="utf-8") as f:
        json.dump(sk, f, ensure_ascii=False, indent=2)

    # 变化图栅格：0=未变化，1=变化
    change_map = (t1 != t2).astype(np.int32)
    map_tif = os.path.join(output_dir, "change_map.tif")
    write_geotiff(map_tif, change_map, bbox, dtype="int32", nodata=-1)

    qa: Dict[str, Any] = {
        "source": source_note,
        "n_classes": len(classes),
        "total_pixels": summary["total_pixels"],
        "changed_pixels": summary["changed_pixels"],
        "change_fraction": summary["change_fraction"],
        "changed_area_km2": summary["changed_area_km2"],
        "n_transitions": len(sk["links"]),
    }
    if synth_info is not None:
        qa["injected_transition"] = synth_info["injected"]

    outputs = [
        {"path": csv_path, "kind": "table", "row_count": int(cm.shape[0] + 1)},
        {"path": change_path, "kind": "json"},
        {"path": sankey_path, "kind": "json"},
        {"path": map_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1, "nodata": -1},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] classes: {classes}")
        print(f"[{SKILL_NAME}] total pixels: {summary['total_pixels']}  "
              f"changed: {summary['changed_pixels']} "
              f"({summary['change_fraction']*100:.2f}%)")
        print(f"[{SKILL_NAME}] transitions (Sankey links): {len(sk['links'])}")
        print(f"[{SKILL_NAME}] matrix: {csv_path}")
        print(f"[{SKILL_NAME}] change areas: {change_path}")
        print(f"[{SKILL_NAME}] sankey: {sankey_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Land cover transition matrix from two classified rasters.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--t1", help="time-1 classified GeoTIFF (integer classes)")
    p.add_argument("--t2", help="time-2 classified GeoTIFF (integer classes)")
    p.add_argument("--n-classes", type=int, default=5,
                   help="number of classes for synthetic mode, 2-5 (default: 5)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a synthetic two-epoch class pair (offline)")
    p.add_argument("--output-dir", default="./output", help="output directory")
    p.add_argument("--quiet", action="store_true", help="suppress console output")
    p.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    return p


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.n_classes < 2 or args.n_classes > len(CLASS_NAMES):
            raise UsageError(
                f"--n-classes must be in [2, {len(CLASS_NAMES)}], got {args.n_classes}",
                n_classes=int(args.n_classes),
            )
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
