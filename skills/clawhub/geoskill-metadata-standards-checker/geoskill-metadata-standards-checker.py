#!/usr/bin/env python3
"""metadata-standards-checker — 元数据标准检查

解析 ISO 19115 / FGDC 格式的 XML 元数据，按标准的必填项与受控词表规则做
验证，计算完整性评分（0-1），并输出问题清单（error / warning）。

数据源：本地 XML 元数据文件（``--input``），或 ``--synthetic`` 模式在本地
生成若干带有意缺漏的 ISO 19115 / FGDC 样例用于离线测试。

隐私声明 / Privacy：
- 默认完全离线运行，``--synthetic`` 模式不读取任何外部数据。
- 所有处理在本地完成，不上传用户数据。

Usage:
    python metadata-standards-checker.py --input metadata.xml --standard iso19115
    python metadata-standards-checker.py --bbox 116 39 117 40 --synthetic --output-dir ./out

License: MIT
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import sys
import xml.etree.ElementTree as ET
from typing import Any, Dict, List, Optional, Tuple

VERSION = "1.0.0"
SKILL_NAME = "metadata-standards-checker"

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
# 受控词表（公开标准中的典型取值）
# ---------------------------------------------------------------------------
ISO_HIERARCHY_LEVELS = {
    "dataset", "series", "featureType", "feature", "attributeType",
    "attribute", "tile", "model", "catalogue", "application", "service",
}
ISO_TOPIC_CATEGORIES = {
    "farming", "biota", "boundaries", "climatologyMeteorologyAtmosphere",
    "economy", "elevation", "environment", "geoscientificInformation",
    "health", "imageryBaseMapsEarthCover", "intelligenceMilitary",
    "inlandWaters", "location", "oceans", "planningCadastre", "society",
    "structure", "transportation", "utilitiesCommunication",
}

# 必填字段（local name），按标准划分
ISO_REQUIRED = [
    "fileIdentifier", "language", "characterSet", "hierarchyLevel",
    "contact", "dateStamp", "metadataStandardName", "referenceSystemInfo",
    "identificationInfo", "title", "abstract",
]
ISO_RECOMMENDED = ["keywords", "topicCategory", "extent", "resourceConstraints"]

FGDC_REQUIRED = [
    "idinfo", "citation", "descript", "timeperd", "status", "spdom",
    "keywords", "accconst", "useconst", "metainfo", "metstdn",
]
FGDC_RECOMMENDED = ["ptcontac", "crossref", "metc", "metd"]


def localname(tag: str) -> str:
    """去掉 XML 命名空间前缀，返回本地标签名。"""
    if "}" in tag:
        return tag.split("}", 1)[1]
    return tag


def validate_bbox(bbox) -> None:
    """Validate bbox as (W, S, E, N); raise ValidationError on bad input.

    Rules (WGS-84):
        * 4 floats
        * W < E, S < N (zero-area or reversed bbox rejected)
        * -180 <= W, E <= 180; -90 <= S, N <= 90
        * bbox spans <1e-4 deg on either axis rejected (effectively zero area)
    Cross-180° is reported as a hint to split, but rejected for clarity.
    """
    if bbox is None or len(bbox) != 4:
        raise ValidationError("bbox must be 4 floats (W, S, E, N)", bbox=bbox)
    W, S, E, N = [float(x) for x in bbox]
    if not (-180.0 <= W <= 180.0 and -180.0 <= E <= 180.0):
        raise ValidationError(
            f"longitude out of range: W={W}, E={E} must be in [-180, 180]",
            bbox=bbox,
        )
    if not (-90.0 <= S <= 90.0 and -90.0 <= N <= 90.0):
        raise ValidationError(
            f"latitude out of range: S={S}, N={N} must be in [-90, 90]",
            bbox=bbox,
        )
    if W >= E:
        raise ValidationError(
            f"bbox has W >= E (W={W}, E={E}); please use W < E. "
            f"For cross-180° regions, split into two bboxes.",
            bbox=bbox,
        )
    if S >= N:
        raise ValidationError(
            f"bbox has S >= N (S={S}, N={N}); please use S < N.",
            bbox=bbox,
        )
    if (E - W) < 1e-4 or (N - S) < 1e-4:
        raise ValidationError(
            f"bbox span too small: width={E - W}, height={N - S}; must be >= 1e-4 deg",
            bbox=bbox,
        )


def parse_metadata_xml(source: str) -> Tuple[ET.Element, Dict[str, List[str]]]:
    """解析 XML，返回 (root, fields)。

    fields 是以 local name 为键、出现过的文本值为列表的字典；
    同时包含一个特殊键 ``__present__``，列出所有出现过的 local name。
    """
    try:
        tree = ET.parse(source) if os.path.exists(source) else ET.fromstring(source)
        root = tree.getroot() if hasattr(tree, "getroot") else tree
    except ET.ParseError as exc:
        raise ValidationError(f"XML parse error: {exc}") from exc

    fields: Dict[str, List[str]] = {}
    present: List[str] = []
    for el in root.iter():
        ln = localname(el.tag)
        present.append(ln)
        text = (el.text or "").strip()
        if text:
            fields.setdefault(ln, []).append(text)
    fields["__present__"] = present
    return root, fields


def detect_standard(fields: Dict[str, List[str]]) -> str:
    """根据出现的标签自动判定元数据标准。"""
    present = set(fields.get("__present__", []))
    if "MD_Metadata" in present or "fileIdentifier" in present or "gmd" in " ".join(present):
        return "iso19115"
    if "idinfo" in present and "metainfo" in present:
        return "fgdc"
    if "idinfo" in present:
        return "fgdc"
    return "iso19115"


def completeness_score(fields: Dict[str, List[str]], required: List[str]) -> float:
    """必填字段命中率，范围 [0, 1]。"""
    present = set(fields.get("__present__", []))
    if not required:
        return 1.0
    hit = sum(1 for f in required if f in present)
    return hit / len(required)


def validate_metadata(
    fields: Dict[str, List[str]],
    standard: str,
) -> Dict[str, Any]:
    """按指定标准验证元数据，返回结构化结果。"""
    if standard == "iso19115":
        required, recommended = ISO_REQUIRED, ISO_RECOMMENDED
    elif standard == "fgdc":
        required, recommended = FGDC_REQUIRED, FGDC_RECOMMENDED
    else:
        raise UsageError(f"unknown standard '{standard}'. Choose from: iso19115, fgdc")

    present = set(fields.get("__present__", []))
    issues: List[Dict[str, str]] = []

    for f in required:
        if f not in present:
            issues.append({
                "level": "error", "field": f,
                "message": f"missing required element <{f}> for {standard}",
            })
    for f in recommended:
        if f not in present:
            issues.append({
                "level": "warning", "field": f,
                "message": f"recommended element <{f}> not found",
            })

    # 受控词表检查（仅 ISO 19115）
    if standard == "iso19115":
        for val in fields.get("hierarchyLevel", []):
            if val and val not in ISO_HIERARCHY_LEVELS:
                issues.append({
                    "level": "warning", "field": "hierarchyLevel",
                    "message": f"hierarchyLevel '{val}' not in controlled vocabulary",
                })
        for val in fields.get("topicCategory", []):
            if val and val not in ISO_TOPIC_CATEGORIES:
                issues.append({
                    "level": "warning", "field": "topicCategory",
                    "message": f"topicCategory '{val}' not in controlled vocabulary",
                })

    score = completeness_score(fields, required)
    n_err = sum(1 for i in issues if i["level"] == "error")
    n_warn = sum(1 for i in issues if i["level"] == "warning")
    return {
        "standard": standard,
        "completeness_score": round(score, 4),
        "required_fields": len(required),
        "present_required": len(required) - sum(
            1 for i in issues if i["level"] == "error"),
        "errors": n_err,
        "warnings": n_warn,
        "issues": issues,
        "passed": n_err == 0,
    }


# ---------------------------------------------------------------------------
# 合成数据：生成带有意缺漏的 ISO 19115 / FGDC 样例（离线测试）
# ---------------------------------------------------------------------------
def build_iso_xml(bbox: List[float], complete: bool) -> str:
    w, s, e, n = bbox
    # 缺漏版：整段移除 fileIdentifier 与 abstract 两个必填元素
    file_id_block = (
        '<gmd:fileIdentifier><gco:CharacterString>synthetic-iso-0001'
        "</gco:CharacterString></gmd:fileIdentifier>" if complete else ""
    )
    abstract_block = (
        "<gmd:abstract><gco:CharacterString>Sample abstract describing the "
        "synthetic dataset.</gco:CharacterString></gmd:abstract>"
        if complete else ""
    )
    keywords = ("<gmd:descriptiveKeywords><gmd:MD_Keywords>"
                "<gmd:keyword><gco:CharacterString>synthetic</gco:CharacterString>"
                "</gmd:keyword></gmd:MD_Keywords></gmd:descriptiveKeywords>"
                if complete else "")
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<gmd:MD_Metadata xmlns:gmd="http://www.isotc211.org/2005/gmd"
                 xmlns:gco="http://www.isotc211.org/2005/gco">
  {file_id_block}
  <gmd:language><gco:CharacterString>eng</gco:CharacterString></gmd:language>
  <gmd:characterSet><gmd:MD_CharacterSetCode>utf8</gmd:MD_CharacterSetCode></gmd:characterSet>
  <gmd:hierarchyLevel><gmd:MD_ScopeCode>dataset</gmd:MD_ScopeCode></gmd:hierarchyLevel>
  <gmd:contact><gmd:CI_ResponsibleParty><gmd:organisationName>
    <gco:CharacterString>Synthetic Org</gco:CharacterString></gmd:organisationName>
  </gmd:CI_ResponsibleParty></gmd:contact>
  <gmd:dateStamp><gco:Date>2026-01-01</gco:Date></gmd:dateStamp>
  <gmd:metadataStandardName><gco:CharacterString>ISO 19115</gco:CharacterString></gmd:metadataStandardName>
  <gmd:referenceSystemInfo><gmd:MD_ReferenceSystem>
    <gmd:referenceSystemIdentifier><gmd:RS_Identifier>
      <gmd:code><gco:CharacterString>EPSG:4326</gco:CharacterString></gmd:code>
    </gmd:RS_Identifier></gmd:referenceSystemIdentifier>
  </gmd:MD_ReferenceSystem></gmd:referenceSystemInfo>
  <gmd:identificationInfo><gmd:MD_DataIdentification>
    <gmd:citation><gmd:CI_Citation><gmd:title>
      <gco:CharacterString>Synthetic Dataset</gco:CharacterString></gmd:title>
    </gmd:CI_Citation></gmd:citation>
    {abstract_block}
    {keywords}
    <gmd:topicCategory><gmd:MD_TopicCategoryCode>geoscientificInformation</gmd:MD_TopicCategoryCode></gmd:topicCategory>
    <gmd:extent><gmd:EX_Extent><gmd:geographicElement>
      <gmd:EX_GeographicBoundingBox>
        <gmd:westBoundLongitude><gco:Decimal>{w}</gco:Decimal></gmd:westBoundLongitude>
        <gmd:eastBoundLongitude><gco:Decimal>{e}</gco:Decimal></gmd:eastBoundLongitude>
        <gmd:southBoundLatitude><gco:Decimal>{s}</gco:Decimal></gmd:southBoundLatitude>
        <gmd:northBoundLatitude><gco:Decimal>{n}</gco:Decimal></gmd:northBoundLatitude>
      </gmd:EX_GeographicBoundingBox>
    </gmd:geographicElement></gmd:EX_Extent></gmd:extent>
  </gmd:MD_DataIdentification></gmd:identificationInfo>
</gmd:MD_Metadata>
"""


def build_fgdc_xml(bbox: List[float], complete: bool) -> str:
    w, s, e, n = bbox
    metc = ("<metc><cntinfo><cntorgp><cntorg>Synthetic Org</cntorg></cntorgp></cntinfo></metc>"
            if complete else "")
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<metadata>
  <idinfo>
    <citation><citeinfo><title>Synthetic FGDC Dataset</title></citeinfo></citation>
    <descript><abstract>Sample FGDC abstract.</abstract><purpose>Testing</purpose></descript>
    <timeperd><timeinfo><sngdate><caldate>20260101</caldate></sngdate></timeinfo></timeperd>
    <status><progress>Complete</progress><update>None planned</update></status>
    <spdom><bounding>
      <westbc>{w}</westbc><eastbc>{e}</eastbc><northbc>{n}</northbc><southbc>{s}</southbc>
    </bounding></spdom>
    <keywords><theme><themekt>None</themekt><themekey>synthetic</themekey></theme></keywords>
    <accconst>None</accconst>
    <useconst>None</useconst>
    <ptcontac><cntinfo><cntorgp><cntorg>Synthetic Org</cntorg></cntorgp></cntinfo></ptcontac>
  </idinfo>
  <metainfo>
    <metd>20260101</metd>
    {metc}
    <metstdn>FGDC Content Standard for Digital Geospatial Metadata</metstdn>
  </metainfo>
</metadata>
"""


def generate_synthetic(
    output_dir: str, bbox: List[float]
) -> List[Dict[str, Any]]:
    """在 output_dir/samples 下生成 ISO/FGDC 样例（含一个刻意缺漏的 ISO）。"""
    sample_dir = os.path.join(output_dir, "samples")
    os.makedirs(sample_dir, exist_ok=True)
    samples = [
        ("iso_complete.xml", build_iso_xml(bbox, complete=True), "iso19115"),
        ("iso_incomplete.xml", build_iso_xml(bbox, complete=False), "iso19115"),
        ("fgdc_complete.xml", build_fgdc_xml(bbox, complete=True), "fgdc"),
    ]
    out = []
    for name, content, std in samples:
        path = os.path.join(sample_dir, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        out.append({"path": path, "standard": std})
    return out


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
            "standard": getattr(args, "standard", None),
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

    # 1) 获取待检查的元数据文件
    if args.input and not args.synthetic:
        if not os.path.exists(args.input):
            raise UsageError(f"input metadata file not found: {args.input}",
                             path=args.input)
        # Verify the file is non-empty
        if os.path.getsize(args.input) == 0:
            raise ValidationError(
                "input metadata file is empty",
                path=args.input,
            )
        targets = [{"path": args.input, "standard": args.standard}]
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <xml>")
        validate_bbox(bbox)
        # Now that inputs are valid, ensure output dir
        os.makedirs(output_dir, exist_ok=True)
        targets = generate_synthetic(output_dir, bbox)
        # auto 检测时保留标准；显式指定则覆盖
        if args.standard != "auto":
            for t in targets:
                t["standard"] = args.standard
        source_note = "synthetic"
    # input mode also needs the output dir (after input validation)
    if args.input and not args.synthetic:
        os.makedirs(output_dir, exist_ok=True)

    # 2) 逐文件检查
    results: List[Dict[str, Any]] = []
    for t in targets:
        root, fields = parse_metadata_xml(t["path"])
        std = t.get("standard", "auto")
        if std == "auto":
            std = detect_standard(fields)
        res = validate_metadata(fields, std)
        res["file"] = os.path.basename(t["path"])
        results.append(res)

    mean_score = (sum(r["completeness_score"] for r in results) / len(results)
                  if results else 0.0)
    report = {
        "skill": SKILL_NAME,
        "source": source_note,
        "n_files": len(results),
        "mean_completeness": round(mean_score, 4),
        "files_passed": sum(1 for r in results if r["passed"]),
        "results": results,
    }

    report_path = os.path.join(output_dir, "metadata_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    qa = {
        "source": source_note,
        "n_files": len(results),
        "mean_completeness": round(mean_score, 4),
        "files_passed": report["files_passed"],
        "total_errors": sum(r["errors"] for r in results),
        "total_warnings": sum(r["warnings"] for r in results),
    }
    outputs = [{"path": report_path, "kind": "json"}]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] files checked: {len(results)}")
        print(f"[{SKILL_NAME}] mean completeness: {qa['mean_completeness']:.4f}")
        print(f"[{SKILL_NAME}] passed: {report['files_passed']}/{len(results)}")
        print(f"[{SKILL_NAME}] errors: {qa['total_errors']}  warnings: {qa['total_warnings']}")
        print(f"[{SKILL_NAME}] report: {report_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Validate ISO 19115 / FGDC XML metadata and score completeness.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input XML metadata file")
    p.add_argument("--standard", default="auto",
                   choices=["auto", "iso19115", "fgdc"],
                   help="metadata standard to validate against (default: auto)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate synthetic ISO/FGDC sample metadata (offline)")
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
