#!/usr/bin/env python3
"""ai-report-generator — AI 遥感分析报告生成

把一份遥感分析结果（指标字典 / 栅格统计 / JSON）自动渲染成结构化的
HTML 与 Markdown 分析报告，含标题、概览、指标表、质量评级与结论。

本 skill 是 LLM 自动报告生成系统的**离线 numpy 等价实现**：
不依赖大模型/网络，而用可验证的模板流程复现"结果 -> 摘要 -> 报告"——

1. **结果解析**：从分析结果 JSON（``--analysis``）或输入栅格的逐波段统计
   构建结构化指标字典；
2. **摘要统计**：对数值指标计算 min/max/mean，生成概览与质量评级
   （按阈值给 PASS/WARN/FAIL 旗标，等价于规则化结论生成）；
3. **模板填充**：用 HTML 转义安全的模板渲染 HTML 与 Markdown 报告。

数据源：分析结果 JSON / 本地 GeoTIFF（自动算统计），或 ``--synthetic`` 生成
示例分析结果用于离线演示。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python ai-report-generator.py --analysis results.json --title "地块分析" --output-dir ./out
    python ai-report-generator.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "ai-report-generator"

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


# ---------------------------------------------------------------------------
# 核心算法：结果解析 / 摘要 / 评级 / 模板渲染
# ---------------------------------------------------------------------------
def html_escape(text: Any) -> str:
    """HTML 转义，防止报告内容注入（& < > " '）。"""
    s = str(text)
    return (s.replace("&", "&amp;")
             .replace("<", "&lt;")
             .replace(">", "&gt;")
             .replace('"', "&quot;")
             .replace("'", "&#39;"))


def load_analysis(source: Any) -> Dict[str, Any]:
    """加载分析结果：dict 直接返回，str 视为 JSON 文件路径。"""
    if isinstance(source, dict):
        return source
    path = str(source)
    if not os.path.exists(path):
        raise UsageError(f"analysis JSON not found: {path}", path=path)
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as exc:
        raise ValidationError(f"analysis JSON is not valid JSON: {exc}", path=path)
    if not isinstance(data, dict):
        raise ValidationError("analysis JSON root must be an object/dict")
    return data


def validate_bbox(bbox: List[float], source: str = "bbox") -> None:
    """校验 bbox 范围 [W, S, E, N]：反序/超界 → ValidationError exit 6。

    这是与 buffer-analysis / ai-accuracy-assessment 共享的「先想清楚再动手」检查：
    跨 180° 经线 (W > E) 静默产出"反转"地理参考/负值，必须报错。
    """
    if not isinstance(bbox, (list, tuple)) or len(bbox) != 4:
        raise ValidationError(f"{source} must be [W, S, E, N] with 4 numbers")
    w, s, e, n = (float(x) for x in bbox)
    if not all(np.isfinite(x) for x in (w, s, e, n)):
        raise ValidationError(f"{source} contains non-finite values")
    if w >= e:
        raise ValidationError(
            f"{source} has W ({w}) >= E ({e}); "
            f"cross-180° bboxes are not supported (split or use a single-hemisphere bbox)"
        )
    if s >= n:
        raise ValidationError(
            f"{source} has S ({s}) >= N ({n}); bbox is inverted"
        )
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(f"{source} latitude out of range [-90, 90]: S={s} N={n}")
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(f"{source} longitude out of range [-180, 180]: W={w} E={e}")


def numeric_metrics(results: Dict[str, Any]) -> Dict[str, float]:
    """从结果字典中抽取所有数值型指标（扁平化一层）。"""
    out: Dict[str, float] = {}
    for k, v in results.items():
        if isinstance(v, bool):
            continue
        if isinstance(v, (int, float)) and np.isfinite(v):
            out[k] = float(v)
    return out


def compute_summary(results: Dict[str, Any]) -> Dict[str, Any]:
    """对数值指标计算概览统计：个数、最小/最大/均值、最大最小指标名。"""
    metrics = numeric_metrics(results)
    if not metrics:
        return {"n_metrics": 0, "min": None, "max": None, "mean": None,
                "min_key": None, "max_key": None, "metrics": {}}
    vals = np.array(list(metrics.values()), dtype=np.float64)
    min_key = min(metrics, key=metrics.get)
    max_key = max(metrics, key=metrics.get)
    return {
        "n_metrics": int(len(metrics)),
        "min": float(vals.min()),
        "max": float(vals.max()),
        "mean": float(vals.mean()),
        "min_key": min_key,
        "max_key": max_key,
        "metrics": metrics,
    }


def quality_flags(results: Dict[str, Any],
                  thresholds: Optional[Dict[str, Tuple[float, float]]] = None
                  ) -> Dict[str, str]:
    """按阈值给指标评级：value < low -> FAIL，< high -> WARN，否则 PASS。

    thresholds: {metric_name: (low_fail, high_warn)}。未配置的指标不评级。
    """
    if thresholds is None:
        thresholds = {}
    metrics = numeric_metrics(results)
    flags: Dict[str, str] = {}
    for name, (low, high) in thresholds.items():
        if name not in metrics:
            continue
        v = metrics[name]
        if v < low:
            flags[name] = "FAIL"
        elif v < high:
            flags[name] = "WARN"
        else:
            flags[name] = "PASS"
    return flags


def render_markdown(results: Dict[str, Any], title: str,
                    flags: Optional[Dict[str, str]] = None,
                    meta: Optional[Dict[str, Any]] = None) -> str:
    """渲染 Markdown 报告。"""
    flags = flags or {}
    meta = meta or {}
    summary = compute_summary(results)
    lines: List[str] = []
    lines.append(f"# {title}")
    lines.append("")
    if meta:
        lines.append("## 元信息")
        for k, v in meta.items():
            lines.append(f"- **{k}**: {v}")
        lines.append("")
    lines.append("## 概览")
    if summary["n_metrics"] == 0:
        lines.append("（无数值指标）")
    else:
        lines.append(f"- 指标数量: {summary['n_metrics']}")
        lines.append(f"- 最小值: {summary['min']:.4g}（{summary['min_key']}）")
        lines.append(f"- 最大值: {summary['max']:.4g}（{summary['max_key']}）")
        lines.append(f"- 均值: {summary['mean']:.4g}")
    lines.append("")
    if summary["n_metrics"] > 0:
        lines.append("## 指标明细")
        lines.append("")
        lines.append("| 指标 | 数值 | 评级 |")
        lines.append("|---|---|---|")
        for k, v in summary["metrics"].items():
            flag = flags.get(k, "")
            lines.append(f"| {k} | {v:.4g} | {flag} |")
        lines.append("")
    if flags:
        n_fail = sum(1 for f in flags.values() if f == "FAIL")
        n_warn = sum(1 for f in flags.values() if f == "WARN")
        lines.append("## 结论")
        if n_fail:
            lines.append(f"- 存在 {n_fail} 项不达标（FAIL），需要关注。")
        elif n_warn:
            lines.append(f"- 全部达标，但有 {n_warn} 项处于警告（WARN）区间。")
        else:
            lines.append("- 所有受评指标均达标（PASS）。")
        lines.append("")
    return "\n".join(lines) + "\n"


def render_html(results: Dict[str, Any], title: str,
                flags: Optional[Dict[str, str]] = None,
                meta: Optional[Dict[str, Any]] = None) -> str:
    """渲染独立 HTML 报告（内联样式，所有动态内容均经转义）。"""
    flags = flags or {}
    meta = meta or {}
    summary = compute_summary(results)
    esc = html_escape
    parts: List[str] = []
    parts.append("<!DOCTYPE html>")
    parts.append('<html lang="zh"><head><meta charset="utf-8">')
    parts.append(f"<title>{esc(title)}</title>")
    parts.append("<style>body{font-family:sans-serif;margin:2em;}"
                 "table{border-collapse:collapse;}td,th{border:1px solid #ccc;"
                 "padding:4px 10px;}th{background:#f0f0f0;}"
                 ".PASS{color:#1a7f37;}.WARN{color:#b58105;}.FAIL{color:#c0392b;}"
                 "</style></head><body>")
    parts.append(f"<h1>{esc(title)}</h1>")
    if meta:
        parts.append("<h2>元信息</h2><ul>")
        for k, v in meta.items():
            parts.append(f"<li><b>{esc(k)}</b>: {esc(v)}</li>")
        parts.append("</ul>")
    parts.append("<h2>概览</h2>")
    if summary["n_metrics"] == 0:
        parts.append("<p>（无数值指标）</p>")
    else:
        parts.append("<ul>")
        parts.append(f"<li>指标数量: {summary['n_metrics']}</li>")
        parts.append(f"<li>最小值: {summary['min']:.4g}（{esc(summary['min_key'])}）</li>")
        parts.append(f"<li>最大值: {summary['max']:.4g}（{esc(summary['max_key'])}）</li>")
        parts.append(f"<li>均值: {summary['mean']:.4g}</li>")
        parts.append("</ul>")
    if summary["n_metrics"] > 0:
        parts.append("<h2>指标明细</h2>")
        parts.append("<table><tr><th>指标</th><th>数值</th><th>评级</th></tr>")
        for k, v in summary["metrics"].items():
            flag = flags.get(k, "")
            cls = f' class="{flag}"' if flag in ("PASS", "WARN", "FAIL") else ""
            parts.append(f"<tr><td>{esc(k)}</td><td>{v:.4g}</td>"
                         f"<td{cls}>{esc(flag)}</td></tr>")
        parts.append("</table>")
    parts.append("</body></html>")
    return "\n".join(parts) + "\n"


# ---------------------------------------------------------------------------
# 合成分析结果（离线演示）
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], seed: int = 42) -> Dict[str, Any]:
    """生成一份示例遥感分析结果字典（含数值与非数值字段）。"""
    rng = np.random.default_rng(seed)
    return {
        "bbox": bbox,
        "scene_id": "SYNTH-2026",
        "cloud_cover_pct": float(rng.uniform(0, 8)),
        "ndvi_mean": float(rng.uniform(0.3, 0.7)),
        "ndvi_std": float(rng.uniform(0.05, 0.2)),
        "vegetation_fraction": float(rng.uniform(0.2, 0.8)),
        "water_fraction": float(rng.uniform(0.0, 0.15)),
        "built_fraction": float(rng.uniform(0.0, 0.3)),
        "valid_pixels": int(rng.integers(10000, 16000)),
        "sensor": "synthetic",
    }


# ---------------------------------------------------------------------------
# 栅格统计（真实输入模式）
# ---------------------------------------------------------------------------
def raster_band_stats(cube: np.ndarray, nodata: Optional[float] = None) -> Dict[str, Any]:
    """逐波段统计 min/max/mean/std，汇总为分析结果字典。

    nodata: 如果给定，必须在统计前从每个波段剔除该值（避免 -9999 静默参与计算）。
    全波段全 NoData → ValidationError exit 6（与 buffer-analysis / ai-accuracy 一致）。
    """
    arr = np.asarray(cube, dtype=np.float64)
    if arr.ndim == 2:
        arr = arr[np.newaxis, ...]
    stats: Dict[str, Any] = {"n_bands": int(arr.shape[0])}
    band_means: List[float] = []
    any_valid = False
    for b in range(arr.shape[0]):
        band = arr[b]
        valid = np.isfinite(band)
        if nodata is not None and not (isinstance(nodata, float) and np.isnan(nodata)):
            valid = valid & (band != float(nodata))
        masked = band[valid]
        if masked.size == 0:
            continue
        any_valid = True
        stats[f"band_{b}_n_valid"] = int(masked.size)
        stats[f"band_{b}_min"] = float(masked.min())
        stats[f"band_{b}_max"] = float(masked.max())
        stats[f"band_{b}_mean"] = float(masked.mean())
        stats[f"band_{b}_std"] = float(masked.std())
        band_means.append(float(masked.mean()))
    if not any_valid:
        raise ValidationError(
            "all bands contain only NoData (or no valid pixels) — nothing to report"
        )
    if band_means:
        stats["overall_mean"] = float(np.mean(band_means))
    return stats


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(path: str, array: np.ndarray, bbox: List[float], nodata: float = -9999.0) -> None:
    import rasterio
    from rasterio.transform import from_bounds

    arr = np.asarray(array, dtype=np.float32)
    if arr.ndim == 2:
        arr = arr[np.newaxis, ...]
    nb, h, w = arr.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    profile = {
        "driver": "GTiff", "height": h, "width": w, "count": nb,
        "dtype": "float32", "crs": "EPSG:4326", "transform": transform,
        "nodata": nodata, "compress": "deflate",
    }
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(arr[b].astype("float32"), b + 1)


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float]]:
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return cube, bbox


def read_geotiff_nodata(path: str) -> Any:
    """仅读取 src.nodata，不读数据。轻量，避免在 read_geotiff 返回值上挂
    np.ndarray 不支持的实例属性。"""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        return src.nodata


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
        inputs={
            "input": getattr(args, "input", None),
            "analysis": getattr(args, "analysis", None),
            "title": getattr(args, "title", None),
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
DEFAULT_THRESHOLDS: Dict[str, Tuple[float, float]] = {
    # (low_fail, high_warn)：指标值 < low -> FAIL，< high -> WARN，>= high -> PASS
    "ndvi_mean": (0.2, 0.35),
    "vegetation_fraction": (0.1, 0.25),
    "valid_pixels": (1000.0, 5000.0),
}


def process(args: argparse.Namespace) -> int:
    started_at = _utc_now()
    output_dir = args.output_dir
    os.makedirs(output_dir, exist_ok=True)

    bbox = list(args.bbox) if args.bbox else None

    # 构建分析结果字典
    if args.analysis:
        results = load_analysis(args.analysis)
        source_note = args.analysis
        if bbox is None:
            embedded = results.get("bbox")
            if embedded is None:
                # 无 bbox 时用 [0,0,1,1] 占位 (不会被校验，因为是 internal 字段)
                bbox = [0.0, 0.0, 1.0, 1.0]
            else:
                bbox = list(embedded)
                validate_bbox(bbox, source="analysis JSON bbox")
    elif args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        nodata = read_geotiff_nodata(args.input)
        bbox = bbox if bbox is not None else file_bbox
        results = raster_band_stats(cube, nodata=nodata)
        results["bbox"] = bbox
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode), --input, or --analysis")
        validate_bbox(bbox, source="--bbox")
        results = generate_synthetic(bbox, seed=args.seed)
        source_note = "synthetic"

    flags = quality_flags(results, DEFAULT_THRESHOLDS)
    meta = {"数据来源": source_note, "bbox": bbox, "生成时间": _utc_now()}

    outputs: List[Dict[str, Any]] = []
    if args.format in ("html", "both"):
        html = render_html(results, args.title, flags, meta)
        html_path = os.path.join(output_dir, "report.html")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html)
        outputs.append({"path": html_path, "kind": "document"})
    if args.format in ("md", "both"):
        md = render_markdown(results, args.title, flags, meta)
        md_path = os.path.join(output_dir, "report.md")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md)
        outputs.append({"path": md_path, "kind": "document"})

    summary = compute_summary(results)
    summary_path = os.path.join(output_dir, "report_summary.json")
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump({"summary": summary, "flags": flags, "results": results},
                  f, ensure_ascii=False, indent=2, default=str)
    outputs.append({"path": summary_path, "kind": "json"})

    qa: Dict[str, Any] = {
        "source": source_note,
        "format": args.format,
        "n_metrics": summary["n_metrics"],
        "flags": flags,
    }
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] title: {args.title}")
        print(f"[{SKILL_NAME}] metrics: {summary['n_metrics']}  flags: {flags}")
        for o in outputs:
            print(f"[{SKILL_NAME}] output: {o['path']}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="AI remote-sensing report generator (JSON results -> HTML/MD, offline equivalent).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input GeoTIFF (per-band stats used as results)")
    p.add_argument("--analysis", help="analysis results JSON file")
    p.add_argument("--title", default="遥感分析报告", help="report title")
    p.add_argument("--format", default="both", choices=["html", "md", "both"],
                   help="output report format (default: both)")
    p.add_argument("--seed", type=int, default=42, help="seed for synthetic results")
    p.add_argument("--synthetic", action="store_true", help="generate demo results (offline)")
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
