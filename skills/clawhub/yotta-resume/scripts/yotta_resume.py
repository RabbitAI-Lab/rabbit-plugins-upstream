#!/usr/bin/env python3
"""yotta-resume: local resume analysis, follow-up questions, and document export."""

import argparse
import errno
import hashlib
import html
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import zipfile
from pathlib import Path
from xml.etree import ElementTree

from contract_validate import validate_contracts
import interview_engine as interview

try:
    sys.stdin.reconfigure(encoding="utf-8")
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass


SKILL_ROOT = Path(__file__).resolve().parent.parent
VERSION = "0.2.1"
SCHEMA_VERSION = "1.1"
JD_LEXICON_VERSION = "2026-11-21.2"

_PHONE_RE = re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)")
_EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
_URL_RE = re.compile(r"https?://[^\s，。；;、）)]+", re.IGNORECASE)
_IPV4_RE = re.compile(
    r"(?<![\d.])(?:\d{1,3}\.){3}\d{1,3}(?![\d.])"
)
_CLIENT_NAME_RE = re.compile(
    r"(?P<prefix>客户\s*[:：]?\s*|委托方\s*[:：]?\s*|服务对象\s*[:：]?\s*|负责\s*)"
    r"(?P<name>[\u4e00-\u9fffA-Za-z0-9·]{2,30}"
    r"(?:公司|集团|银行|大学|医院|政府|中心|平台))"
)
_HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
_BULLET_RE = re.compile(r"^\s*(?:[-*+]\s+|\d+[.、)]\s+)(.+)$")
_PLACEHOLDER_RE = re.compile(
    r"(?<![A-Za-z0-9])(?:x{2,}|X{2,}|待填|TO" r"DO|TBD)(?![A-Za-z0-9])",
    re.IGNORECASE,
)
_LONG_TOKEN_RE = re.compile(r"\b[A-Za-z0-9_]{18,}\b")

_JD_KEYWORDS = (
    "SOC",
    "SIEM",
    "SOAR",
    "EDR",
    "XDR",
    "IDS",
    "IPS",
    "WAF",
    "NGFW",
    "VPN",
    "PKI",
    "TLS",
    "IAM",
    "零信任",
    "安全基线",
    "日志分析",
    "告警研判",
    "误报治理",
    "威胁狩猎",
    "威胁情报",
    "事件响应",
    "Python",
    "SQL",
    "Linux",
    "Windows",
    "Docker",
    "Kubernetes",
    "Terraform",
    "OpenTelemetry",
    "AWS",
    "Azure",
    "GCP",
    "MITRE ATT&CK",
    "OWASP",
    "OWASP Top 10",
    "WSTG",
    "CWE",
    "CISA KEV",
    "应急响应",
    "漏洞管理",
    "渗透测试",
    "红队",
    "蓝队",
    "代码审计",
    "应用安全",
    "安全研发",
    "供应链安全",
    "云安全",
    "数据安全",
    "数据分类分级",
    "个人信息保护",
    "风险评估",
    "安全合规",
    "等保",
    "访问控制",
    "备份恢复",
    "变更管理",
    "取证分析",
    "恶意样本",
    "逆向分析",
)

_SECTION_ALIASES = {
    "工作经历": "experience",
    "工作经验": "experience",
    "实习经历": "experience",
    "项目经历": "projects",
    "项目经验": "projects",
    "技能": "skills",
    "专业技能": "skills",
    "教育背景": "education",
    "教育经历": "education",
    "求职意向": "intent",
    "相关技能": "skills",
    "SRC 挖掘": "src",
    "SRC挖掘": "src",
    "自我评价": "self_evaluation",
}


class ResumeInputError(Exception):
    """A controlled, user-facing input parse failure."""

    def __init__(self, message, exit_code=5):
        super().__init__(message)
        self.exit_code = exit_code


def _mask_contact(text):
    """Mask direct contact channels while retaining useful diagnostic wording."""
    text = _PHONE_RE.sub("[电话]", text)
    text = _EMAIL_RE.sub("[邮箱]", text)
    text = _URL_RE.sub("[URL]", text)
    text = _IPV4_RE.sub("[IP]", text)
    return _CLIENT_NAME_RE.sub(
        lambda match: match.group("prefix") + "[客户名]",
        text,
    )


def _masked(original):
    return _mask_contact(original.strip()) or "[空内容]"


def _normalise_plain_resume(text):
    """Restore section markers for text extracted from PDF or DOCX."""
    known_titles = set(_SECTION_ALIASES) | {
        "个人简介",
        "简介",
        "个人总结",
        "总结",
    }
    lines = []
    new_field_prefixes = (
        "电话",
        "邮箱",
        "性别",
        "户籍",
        "最高学历",
        "毕业时间",
        "意向岗位",
        "意向城市",
        "期望薪资",
        "求职类型",
        "期望行业",
        "当前状态",
    )

    def starts_entry(value):
        return bool(
            _BULLET_RE.match(value)
            or re.match(r"^20\d{2}[./年-]\d{1,2}", value)
            or " | " in value
            or value.startswith(new_field_prefixes)
        )

    for raw_line in text.splitlines():
        stripped = raw_line.strip()
        if not stripped:
            lines.append("")
            continue
        if stripped in known_titles:
            lines.append("## " + stripped)
        elif _HEADING_RE.match(stripped):
            lines.append(stripped)
        elif starts_entry(stripped) or not lines:
            lines.append(stripped)
        else:
            previous = lines[-1]
            if not previous or previous.startswith("#"):
                lines.append(stripped)
            elif previous[-1].isascii() and previous[-1].isalnum() and stripped[0].isascii() and stripped[0].isalnum():
                lines[-1] = previous + " " + stripped
            else:
                lines[-1] = previous + stripped
    return "\n".join(lines).strip()


def _sha256_file(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def _year_month_match(pattern, text):
    match = re.search(pattern, text, re.MULTILINE)
    if not match:
        return None
    year = int(match.group(1))
    month = int(match.group(2))
    if not 1 <= month <= 12:
        return None
    return year * 12 + month


def _date_conflict(text):
    declared = _year_month_match(
        r"毕业时间\s*[:：]\s*(20\d{2})[./年-](\d{1,2})",
        text,
    )
    education_end = None
    match = re.search(
        r"教育(?:背景|经历)[\s\S]{0,220}?"
        r"(20\d{2})[./年-](\d{1,2})[^\n]{0,24}?"
        r"(?:-|–|—|至|到)\s*"
        r"(20\d{2})[./年-](\d{1,2})",
        text,
        re.MULTILINE,
    )
    if match and 1 <= int(match.group(4)) <= 12:
        education_end = int(match.group(3)) * 12 + int(match.group(4))
    if declared is not None and education_end is not None and declared != education_end:
        return True
    return False


def _finding(code, section, heading, original, reason, severity="medium", needs_confirmation=False):
    return {
        "id": "",
        "code": code,
        "section": section,
        "heading": heading,
        "original": _masked(original),
        "reason": reason,
        "severity": severity,
        "source_type": "rule",
        "needs_confirmation": needs_confirmation,
    }


def _assign_finding_ids(issues):
    for index, issue in enumerate(issues, 1):
        issue["id"] = "YS-{:03d}".format(index)
    return issues


def parse_markdown_resume(markdown):
    """Parse a simple Markdown resume into a stable content model."""
    lines = markdown.splitlines()
    model = {
        "schema_version": SCHEMA_VERSION,
        "name": "",
        "headline": "",
        "contact": [],
        "summary": "",
        "sections": [],
    }
    current_section = None
    current_item = None
    summary_lines = []

    for raw_line in lines:
        line = raw_line.rstrip()
        match = _HEADING_RE.match(line)
        if match:
            level = len(match.group(1))
            title = match.group(2).strip()
            if level == 1 and not model["name"]:
                model["name"] = title
                current_section = None
                current_item = None
                continue
            if level == 2:
                if title in {"个人简介", "简介", "个人总结", "总结"}:
                    current_section = "summary"
                else:
                    current_section = {"title": title, "items": []}
                    model["sections"].append(current_section)
                current_item = None
                continue
            if level >= 3 and current_section and current_section != "summary":
                current_item = {"heading": title, "bullets": []}
                current_section["items"].append(current_item)
                continue
            if level >= 3:
                continue

        bullet = _BULLET_RE.match(line)
        if bullet:
            content = bullet.group(1).strip()
            if current_section == "summary":
                summary_lines.append(content)
            elif current_item is not None:
                current_item["bullets"].append(content)
            elif current_section:
                current_section["items"].append({"heading": "", "bullets": [content]})
            continue

        if line.strip():
            if current_section == "summary":
                summary_lines.append(line.strip())
            elif current_section is None:
                for part in re.split(r"[|｜;；,，\s]+", line.strip()):
                    if part:
                        model["contact"].append(part)
            elif current_section:
                if not current_section["items"]:
                    current_section["items"].append({"heading": "", "bullets": []})
                current_section["items"][-1]["bullets"].append(line.strip())

    model["summary"] = "\n".join(summary_lines).strip()
    return model


def _bullet_texts(model):
    for section in model.get("sections", []):
        for item in section.get("items", []):
            for bullet in item.get("bullets", []):
                yield section.get("title", ""), item.get("heading", ""), bullet


def _has_metric(text):
    return bool(
        re.search(r"\d+(?:\.\d+)?\s*(?:%|％|倍|x|X|次|个|条|台|天|小时|分钟|人|万|k|K)", text)
    )


def _keyword_in_text(keyword, text):
    if keyword.isascii():
        pattern = r"(?<![A-Za-z0-9]){}(?![A-Za-z0-9])".format(
            re.escape(keyword)
        )
        return re.search(pattern, text, re.IGNORECASE) is not None
    return keyword.casefold() in text.casefold()


def _jd_match(resume, jd):
    if not jd.strip():
        return {
            "matched": [],
            "missing": [],
            "coverage": None,
            "status": "not_provided",
            "note": "未提供目标 JD，不能判断岗位匹配。",
            "lexicon_version": JD_LEXICON_VERSION,
            "limitations": (
                "固定关键词词表只检查明确术语，不做语义匹配、岗位排名或招聘竞争力判断。"
            ),
        }
    matched = []
    missing = []
    for keyword in _JD_KEYWORDS:
        if _keyword_in_text(keyword, resume):
            matched.append(keyword)
        elif _keyword_in_text(keyword, jd):
            missing.append(keyword)
    total = len(matched) + len(missing)
    coverage = round(100 * len(matched) / total, 1) if total else 0.0
    return {
        "matched": matched,
        "missing": missing,
        "coverage": coverage,
        "status": "matched",
        "note": "",
        "lexicon_version": JD_LEXICON_VERSION,
        "limitations": (
            "固定关键词词表只检查明确术语，不做语义匹配、岗位排名或招聘竞争力判断；"
            "未收录的同义表达可能漏检。"
        ),
    }


def _industry_registry():
    path = SKILL_ROOT / "data" / "industry-registry.json"
    try:
        registry = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise RuntimeError("行业注册表不可用：{}".format(error)) from error
    if not isinstance(registry, dict) or not isinstance(registry.get("industries"), list):
        raise RuntimeError("行业注册表格式无效。")
    return registry


def detect_industry(resume, registry=None):
    """Detect an industry profile with deterministic keyword scoring."""
    registry = registry or _industry_registry()
    industries = [
        item for item in registry.get("industries", [])
        if isinstance(item, dict) and item.get("id")
    ]
    fallback_id = registry.get("default_industry", "generic")
    fallback = next(
        (item for item in industries if item.get("id") == fallback_id),
        {
            "id": "generic",
            "display_name": "通用",
            "evidence_dimensions": [],
            "question_dimensions": [],
            "role_map_ref": None,
        },
    )
    detection = registry.get("detection") or {}
    min_high = int(detection.get("min_high_confidence_hits", 4))
    ambiguity_margin = int(detection.get("ambiguity_margin", 1))

    scored = []
    for industry in industries:
        if industry.get("is_fallback"):
            continue
        matched = [
            keyword for keyword in industry.get("keywords", [])
            if isinstance(keyword, str) and _keyword_in_text(keyword, resume)
        ]
        if matched:
            scored.append({
                "id": industry["id"],
                "display_name": industry.get("display_name", industry["id"]),
                "matched_count": len(matched),
                "matched_keywords": matched,
                "evidence_dimensions": industry.get("evidence_dimensions", []),
                "question_dimensions": industry.get("question_dimensions", []),
                "role_map_ref": industry.get("role_map_ref"),
            })

    scored.sort(key=lambda item: (-item["matched_count"], item["id"]))
    base = {
        "registry_contract_version": registry.get("contract_version"),
        "detection_strategy": detection.get("strategy", "keyword_score_v1"),
        "matched_keywords": sorted({
            keyword
            for item in scored
            for keyword in item["matched_keywords"]
        }),
        "candidates": scored[:5],
    }
    if not scored:
        return {
            **base,
            "status": "fallback",
            "primary_industry": fallback_id,
            "display_name": fallback.get("display_name"),
            "confidence": "low",
            "needs_confirmation": True,
            "evidence_dimensions": fallback.get("evidence_dimensions", []),
            "question_dimensions": fallback.get("question_dimensions", []),
            "role_map_ref": fallback.get("role_map_ref"),
            "reason": "未命中已登记行业的明确关键词，使用通用简历证据维度。",
        }

    top = scored[0]
    second = scored[1] if len(scored) > 1 else None
    if second and top["matched_count"] - second["matched_count"] <= ambiguity_margin:
        return {
            **base,
            "status": "ambiguous",
            "primary_industry": None,
            "display_name": None,
            "confidence": "low",
            "needs_confirmation": True,
            "evidence_dimensions": fallback.get("evidence_dimensions", []),
            "question_dimensions": fallback.get("question_dimensions", []),
            "role_map_ref": fallback.get("role_map_ref"),
            "reason": "多个行业信号接近，需用户确认目标行业后再应用行业专属规则。",
        }

    confidence = (
        "high" if top["matched_count"] >= min_high
        else "medium" if top["matched_count"] >= 2
        else "low"
    )
    return {
        **base,
        "status": "detected",
        "primary_industry": top["id"],
        "display_name": top["display_name"],
        "confidence": confidence,
        "needs_confirmation": confidence == "low",
        "evidence_dimensions": top["evidence_dimensions"],
        "question_dimensions": top["question_dimensions"],
        "role_map_ref": top["role_map_ref"],
        "reason": "基于简历明确关键词命中识别，未使用受保护个人属性。",
    }


def _build_issues(model, bullets, has_jd, text="", source_manifest=None):
    source_manifest = source_manifest or {}
    issues = []
    weak_claims = []
    no_metric = []
    for section, heading, bullet in bullets:
        if any(word in bullet for word in ("负责", "参与", "协助", "熟悉", "沟通能力强", "认真")) and not _has_metric(bullet):
            weak_claims.append((section, heading, bullet))
        elif not _has_metric(bullet) and any(word in bullet for word in ("提升", "优化", "减少", "建设", "处置", "分析")):
            no_metric.append((section, heading, bullet))

    for section, heading, bullet in weak_claims:
        issues.append(_finding(
            "weak_claim",
            section,
            heading,
            bullet,
            "职责描述缺少结果或个人边界，读者无法判断贡献质量。",
        ))
    for section, heading, bullet in no_metric:
        issues.append(_finding(
            "missing_metric",
            section,
            heading,
            bullet,
            "有效改进缺少基线、规模或结果指标。",
        ))

    if _PLACEHOLDER_RE.search(text):
        placeholder = _PLACEHOLDER_RE.search(text).group(0)
        issues.append(_finding(
            "placeholder",
            "全文",
            "",
            placeholder,
            "检测到未填写的占位符，成果口径不完整。",
            severity="high",
        ))
    if text.count("意向岗位") > 1:
        issues.append(_finding(
            "duplicate_field",
            "求职意向",
            "",
            "意向岗位出现多次",
            "同一求职字段重复，容易造成信息冗余或口径不一致。",
        ))
    if _date_conflict(text):
        issues.append(_finding(
            "date_conflict",
            "教育经历",
            "",
            "毕业时间与教育起止时间不一致",
            "文本中的毕业月份和教育结束月份冲突，需要用户确认唯一口径。",
            severity="high",
            needs_confirmation=True,
        ))
    if "精通" in text and "了解" in text:
        issues.append(_finding(
            "mixed_skill_levels",
            "技能",
            "",
            "同时出现「精通」与「了解」",
            "能力等级跨度大，需确认是否有足够证据支撑高等级表述。",
            needs_confirmation=True,
        ))

    token_counts = {}
    for token in _LONG_TOKEN_RE.findall(text):
        token_counts[token] = token_counts.get(token, 0) + 1
    repeated = [token for token, count in token_counts.items() if count >= 3]
    if repeated:
        token = repeated[0]
        issues.append(_finding(
            "template_watermark",
            "输入文件",
            "",
            "重复模板串：{}...".format(token[:16]),
            "长字符串在简历中重复出现，可能是模板水印或导出残留。",
            severity="high",
            needs_confirmation=True,
        ))

    image_count = int(source_manifest.get("images") or 0)
    if image_count > 0:
        issues.append(_finding(
            "image_text_gap",
            "输入文件",
            "",
            "PDF 含 {} 张图片，未执行 OCR。".format(image_count),
            "图片内的证书、成绩或成果不会进入文本分析。",
            needs_confirmation=True,
        ))

    if model.get("contact"):
        issues.append(_finding(
            "sensitive_contact",
            "联系方式",
            "",
            "联系方式已识别：[电话] / [邮箱]",
            "分析报告只保留联系方式类型，不回显手机号或邮箱原文。",
        ))
    if has_jd and not model.get("summary"):
        issues.append(_finding(
            "missing_summary",
            "个人简介",
            "",
            "[空内容]",
            "缺少面向岗位的简介，招聘方难以快速定位候选方向。",
        ))
    return _assign_finding_ids(issues)


def _build_questions(issues, jd, industry_detection=None):
    industry_id = (industry_detection or {}).get("primary_industry") or "generic"
    impact_questions = {
        "cybersecurity": (
            "请补充这条工作的规模和结果：覆盖多少资产 / 日志量 / 告警量，"
            "最终效率或风险指标变化多少？"
        ),
        "software_engineering": (
            "请补充这条工作的业务场景、服务或用户规模、技术栈、个人实现和结果："
            "覆盖多少接口 / 服务 / 用户，性能、质量或稳定性指标变化多少？"
        ),
        "data_ai": (
            "请补充这条工作的数据规模、方法范围、个人实现和评估结果："
            "覆盖多少数据 / 用户 / 任务，指标相对基线变化多少？"
        ),
        "business_operations": (
            "请补充这条工作的业务目标、用户或渠道规模、个人动作和结果："
            "转化、留存、收入或效率指标相对基线变化多少？"
        ),
        "generic": (
            "请补充这条工作的场景、个人职责、动作、规模和结果："
            "最终指标或交付质量相对基线变化多少？"
        ),
    }
    questions = [
        {
            "target": "impact",
            "question": impact_questions.get(industry_id, impact_questions["generic"]),
            "why": "把职责描述转为可验证证据。",
        },
        {
            "target": "ownership",
            "question": "这项工作是你独立负责、牵头还是参与？请说明分工边界和个人动作。",
            "why": "避免团队成果被误写成个人成果。",
        },
    ]
    if any(issue["code"] == "sensitive_contact" for issue in issues):
        questions.append({
            "target": "privacy",
            "question": "导出的正式简历会保留联系方式，但分析报告会打码。请确认联系方式是否为本人真实信息。",
            "why": "防止误用他人联系方式或泄露敏感信息。",
        })
    if (
        industry_id == "cybersecurity"
        and jd
        and ("MITRE ATT&CK" in jd or "OWASP" in jd)
    ):
        questions.append({
            "target": "jd_gap",
            "question": "JD 提到 MITRE ATT&CK / OWASP，你是否在真实项目里用过？请给出对应场景和动作。",
            "why": "补齐岗位关键词必须基于真实经历。",
        })
    return questions


def _build_suggestions(issues, jd_match, industry_detection=None):
    industry_id = (industry_detection or {}).get("primary_industry") or "generic"
    weak_claim_examples = {
        "cybersecurity": (
            "改写为「我的动作 + 工具/流程 + 规模 + 结果」，例如：独立处置 X 类告警 "
            "Y 条/日，通过 Z 规则将重复告警降低 N%。"
        ),
        "software_engineering": (
            "改写为「业务/用户场景 + 技术栈 + 个人动作 + 规模 + 质量或性能结果」，"
            "例如：负责 X 个服务的接口迁移，覆盖 Y 个用户，将响应时间降低 N%。"
        ),
        "data_ai": (
            "改写为「业务问题 + 数据规模 + 方法 + 评估指标 + 上线结果」，"
            "例如：使用 X 方法处理 Y 条数据，将 Z 指标相对基线提升 N%。"
        ),
        "business_operations": (
            "改写为「业务目标 + 用户/渠道规模 + 策略动作 + 转化或留存结果」，"
            "例如：负责 X 渠道活动，覆盖 Y 名用户，将转化率提升 N%。"
        ),
        "generic": (
            "改写为「场景 + 个人动作 + 规模 + 结果 + 证据」，"
            "例如：负责 X 范围的工作，覆盖 Y 个对象，将 Z 指标改善 N%。"
        ),
    }
    summary_examples = {
        "cybersecurity": "安全方向",
        "software_engineering": "技术方向",
        "data_ai": "数据或 AI 方向",
        "business_operations": "业务方向",
        "generic": "目标岗位方向",
    }
    suggestions = []
    for issue in issues:
        if issue["code"] == "weak_claim":
            suggestions.append({
                "code": "rewrite_weak_claim",
                "finding_id": issue["id"],
                "original": issue["original"],
                "suggestion": weak_claim_examples.get(
                    industry_id,
                    weak_claim_examples["generic"],
                ),
                "priority": "high",
            })
        elif issue["code"] == "missing_metric":
            suggestions.append({
                "code": "add_metric",
                "finding_id": issue["id"],
                "original": issue["original"],
                "suggestion": "保留真实口径：补充优化前基线、优化后结果、时间范围或覆盖规模；不能编造数字。",
                "priority": "high",
            })
        elif issue["code"] == "sensitive_contact":
            suggestions.append({
                "code": "protect_contact",
                "finding_id": issue["id"],
                "original": issue["original"],
                "suggestion": "联系方式只出现在正式简历，不出现在分享给他人的分析报告。",
                "priority": "medium",
            })
        elif issue["code"] == "missing_summary":
            suggestions.append({
                "code": "add_summary",
                "finding_id": issue["id"],
                "original": issue["original"],
                "suggestion": "在简介写 2-3 句：{}、核心经验、代表性成果和目标岗位。".format(
                    summary_examples.get(industry_id, summary_examples["generic"])
                ),
                "priority": "medium",
            })
        elif issue["code"] == "placeholder":
            suggestions.append({
                "code": "fill_placeholder",
                "finding_id": issue["id"],
                "original": issue["original"],
                "suggestion": "填写真实数据；无法确认时删除该分句，不能保留 xx 或待填标记。",
                "priority": "high",
            })
        elif issue["code"] == "duplicate_field":
            suggestions.append({
                "code": "deduplicate_field",
                "finding_id": issue["id"],
                "original": issue["original"],
                "suggestion": "保留一处求职意向，其他位置改为岗位方向或删除。",
                "priority": "medium",
            })
        elif issue["code"] == "date_conflict":
            suggestions.append({
                "code": "confirm_dates",
                "finding_id": issue["id"],
                "original": issue["original"],
                "suggestion": "确认毕业月份、教育起止和入职性质，全篇统一为一个口径。",
                "priority": "high",
            })
        elif issue["code"] == "mixed_skill_levels":
            suggestions.append({
                "code": "normalise_skill_levels",
                "finding_id": issue["id"],
                "original": issue["original"],
                "suggestion": "按真实掌握程度统一为熟悉 / 掌握 / 了解；没有项目证据时不要写精通。",
                "priority": "medium",
            })
        elif issue["code"] == "template_watermark":
            suggestions.append({
                "code": "remove_watermark",
                "finding_id": issue["id"],
                "original": issue["original"],
                "suggestion": "使用无水印模板重新导出，并确认文本层不再包含模板串。",
                "priority": "high",
            })
        elif issue["code"] == "image_text_gap":
            suggestions.append({
                "code": "move_image_text_to_text",
                "finding_id": issue["id"],
                "original": issue["original"],
                "suggestion": "把关键证书、成绩和成果转成可检索文字；图片只作装饰。",
                "priority": "medium",
            })

    for keyword in jd_match.get("missing", []):
        suggestions.append({
            "code": "jd_gap",
            "original": "JD 关键词缺失：{}".format(keyword),
            "suggestion": "只在真实项目里补写该关键词；没有经历就不要硬写。",
            "priority": "medium",
        })
    if not suggestions:
        suggestions.append({
            "code": "keep_evidence",
            "original": "当前简历已有基础结构和经历描述。",
            "suggestion": "继续保留事实口径，并优先检查每条经历的量化证据。",
            "priority": "low",
        })
    return suggestions


def _build_structure_check(sections, bullet_count, metric_count, issues, jd_match):
    required_sections = ("experience", "skills", "education")
    present_sections = sum(1 for item in required_sections if item in sections)
    section_score = round(100 * present_sections / len(required_sections))
    metric_ratio = round(100 * metric_count / bullet_count, 1) if bullet_count else 0.0
    evidence_score = round(min(100.0, metric_ratio))
    high_count = sum(1 for item in issues if item.get("severity") == "high")
    medium_count = sum(1 for item in issues if item.get("severity") == "medium")
    hygiene_score = max(0, 100 - high_count * 20 - medium_count * 8)

    dimensions = [
        {
            "key": "sections",
            "label": "章节结构",
            "score": section_score,
            "weight": 25,
            "evidence": "工作经历 / 技能 / 教育背景：{}/{}".format(
                present_sections, len(required_sections)
            ),
        },
        {
            "key": "quantitative_evidence",
            "label": "量化证据",
            "score": evidence_score,
            "weight": 35,
            "evidence": "含指标要点 {} / {}".format(metric_count, bullet_count),
        },
        {
            "key": "hygiene",
            "label": "文本清洁度",
            "score": hygiene_score,
            "weight": 25,
            "evidence": "high {} 项 / medium {} 项".format(high_count, medium_count),
        },
    ]
    if jd_match.get("status") == "matched" and jd_match.get("coverage") is not None:
        dimensions.append({
            "key": "jd_match",
            "label": "JD 关键词匹配",
            "score": round(float(jd_match["coverage"])),
            "weight": 15,
            "evidence": "命中 {} / 缺失 {}".format(
                len(jd_match.get("matched", [])),
                len(jd_match.get("missing", [])),
            ),
        })

    total_weight = sum(item["weight"] for item in dimensions)
    score = round(
        sum(item["score"] * item["weight"] for item in dimensions) / total_weight
    )
    level = "结构完整" if score >= 75 else "部分完整" if score >= 50 else "结构薄弱"
    return {
        "score": max(0, min(100, score)),
        "score_type": "structure_rule_score",
        "label": "结构准备度（规则分）",
        "level": level,
        "not_market_fit": True,
        "dimensions": dimensions,
        "metric_ratio": metric_ratio,
        "guidance": "该分数只反映章节、量化证据、文本清洁度和可选的 JD 关键词覆盖，不代表招聘竞争力；不得改写为其他数值。",
    }


def audit_resume(markdown, jd="", source_manifest=None, parse_warnings=None):
    """Analyze a resume and return an auditable JSON-safe diagnostic report."""
    model = parse_markdown_resume(markdown)
    bullets = list(_bullet_texts(model))
    metric_count = sum(1 for _, _, bullet in bullets if _has_metric(bullet))
    sections = {
        _SECTION_ALIASES.get(section.get("title"), section.get("title"))
        for section in model.get("sections", [])
    }
    sections.discard(None)
    manifest = dict(source_manifest or {
        "type": "text",
        "filename": "inline",
        "backend": "python",
        "pages": None,
        "images": 0,
        "text_chars": len(markdown),
        "sha256": None,
        "warnings": [],
    })
    warnings = list(parse_warnings or manifest.get("warnings") or [])
    if int(manifest.get("images") or 0) > 0 and not any("图片" in item for item in warnings):
        warnings.append(
            "输入文件含 {} 张图片，未执行 OCR；图片内文字不会进入分析。".format(
                manifest.get("images")
            )
        )
    manifest["warnings"] = warnings
    issues = _build_issues(
        model,
        bullets,
        bool(jd),
        text=markdown,
        source_manifest=manifest,
    )
    jd_match = _jd_match(markdown, jd)
    industry_detection = detect_industry(markdown)
    readiness = _build_structure_check(
        sections,
        len(bullets),
        metric_count,
        issues,
        jd_match,
    )
    unknowns = []
    if not jd:
        unknowns.append("未提供目标 JD，无法判断岗位关键词匹配和岗位适配度。")
    if int(manifest.get("images") or 0) > 0:
        unknowns.append("输入文件包含图片，未执行 OCR；图片内的信息未进入分析。")
    if industry_detection.get("status") == "ambiguous":
        unknowns.append("行业识别存在多个接近信号，需确认目标行业后再使用行业专属规则。")
    elif industry_detection.get("needs_confirmation"):
        unknowns.append("行业识别置信度较低，需确认目标行业。")
    unknowns.append("规则引擎无法判断招聘竞争力、面试通过率或 Offer 结果，需人工复核。")

    return {
        "schema_version": SCHEMA_VERSION,
        "source_manifest": manifest,
        "parse_warnings": warnings,
        "sections": sorted(sections),
        "stats": {
            "bullet_count": len(bullets),
            "metric_bullets": metric_count,
            "metric_ratio": readiness["metric_ratio"],
            "issue_count": len(issues),
        },
        "issues": issues,
        "questions": _build_questions(issues, jd, industry_detection),
        "suggestions": _build_suggestions(issues, jd_match, industry_detection),
        "jd_match": jd_match,
        "industry_detection": industry_detection,
        "readiness": readiness,
        "unknowns": unknowns,
        "disclaimer": "分析仅识别结构、证据与岗位匹配度，不承诺 ATS、面试或 Offer 结果，也不替代人工判断。",
    }


def render_audit_markdown(report):
    lines = ["# 元简简历分析", ""]
    readiness = report.get("readiness", {})
    manifest = report.get("source_manifest", {})
    lines.append("## 输入与解析")
    lines.append("- 类型：{}".format(manifest.get("type", "unknown")))
    if manifest.get("filename"):
        lines.append("- 文件：{}".format(manifest.get("filename")))
    if manifest.get("backend"):
        lines.append("- 解析后端：{}".format(manifest.get("backend")))
    if manifest.get("pages") is not None:
        lines.append("- 页数：{}".format(manifest.get("pages")))
    lines.append("- 图片：{}".format(manifest.get("images", 0)))
    if manifest.get("text_chars") is not None:
        lines.append("- 文本字符：{}".format(manifest.get("text_chars")))
    if manifest.get("sha256"):
        lines.append("- SHA-256：`{}`".format(manifest.get("sha256")))
    for warning in report.get("parse_warnings", []):
        lines.append("- 解析提示：{}".format(warning))
    lines.append("")

    lines.append("## 行业识别")
    industry = report.get("industry_detection", {})
    if industry.get("primary_industry"):
        lines.append("- 主行业：{}（{} / {}）".format(
            industry.get("display_name") or industry.get("primary_industry"),
            industry.get("primary_industry"),
            industry.get("confidence", "low"),
        ))
    else:
        lines.append("- 主行业：待确认（多个行业信号接近）")
    if industry.get("matched_keywords"):
        lines.append("- 命中关键词：{}".format(
            "、".join(industry["matched_keywords"])
        ))
    if industry.get("role_map_ref"):
        lines.append("- 岗位映射：{}".format(industry["role_map_ref"]))
    if industry.get("evidence_dimensions"):
        lines.append("- 行业证据维度：{}".format(
            "、".join(industry["evidence_dimensions"])
        ))
    if industry.get("reason"):
        lines.append("- 识别说明：{}".format(industry["reason"]))
    lines.append("")

    lines.append("## 总览")
    lines.append("- {}：{} / 100（{}）".format(
        readiness.get("label", "结构准备度（规则分）"),
        readiness.get("score", 0),
        readiness.get("level", "未知"),
    ))
    lines.append("- 评分类型：{}；不代表招聘竞争力。".format(
        readiness.get("score_type", "structure_rule_score")
    ))
    stats = report.get("stats", {})
    lines.append("- 经历要点：{} 条；其中含指标：{} 条（{}%）。".format(
        stats.get("bullet_count", 0),
        stats.get("metric_bullets", 0),
        stats.get("metric_ratio", 0),
    ))
    jd_match = report.get("jd_match", {})
    if jd_match.get("status") == "not_provided" or jd_match.get("coverage") is None:
        lines.append("- JD 匹配：未提供 JD，不能判断岗位匹配。")
    else:
        lines.append("- JD 关键词覆盖：{}%。".format(jd_match.get("coverage")))
        lines.append("- JD 词表版本：{}。".format(
            jd_match.get("lexicon_version", "unknown")
        ))
        if jd_match.get("limitations"):
            lines.append("- JD 匹配边界：{}".format(jd_match["limitations"]))
    for dimension in readiness.get("dimensions", []):
        score = "未知" if dimension.get("score") is None else "{} / 100".format(dimension.get("score"))
        lines.append("- {}：{}；{}".format(
            dimension.get("label", dimension.get("key", "维度")),
            score,
            dimension.get("evidence", ""),
        ))
    lines.append("")

    lines.append("## 工具发现")
    if report.get("issues"):
        for issue in report.get("issues", []):
            lines.append("- **[{}][{}][{}]** {}：{}".format(
                issue.get("id", ""),
                issue.get("severity", "medium"),
                issue.get("source_type", "rule"),
                issue.get("code", ""),
                issue.get("original", ""),
            ))
            lines.append("  - {}".format(issue.get("reason", "")))
    else:
        lines.append("- 未发现当前规则可确定的问题。")
    lines.append("")

    lines.append("## 高价值追问")
    for index, item in enumerate(report.get("questions", []), 1):
        lines.append("{}. {}".format(index, item.get("question", "")))
    lines.append("")

    lines.append("## 修改建议")
    for item in report.get("suggestions", []):
        lines.append("- **[{}]** {}".format(item.get("priority", "medium"), item.get("suggestion", "")))
        if item.get("finding_id"):
            lines.append("  - 关联：{}".format(item.get("finding_id")))
        lines.append("  - 原文：{}".format(item.get("original", "")))
    lines.append("")

    lines.append("## 无法判断 / 待确认")
    for item in report.get("unknowns", []):
        lines.append("- {}".format(item))
    pending = [
        issue for issue in report.get("issues", []) if issue.get("needs_confirmation")
    ]
    for issue in pending:
        lines.append("- {} 需用户确认：{}".format(issue.get("id", ""), issue.get("reason", "")))
    if not report.get("unknowns") and not pending:
        lines.append("- 未记录额外未知项。")
    lines.append("")

    lines.append("## 输出口径")
    lines.append(
        "- 只能原样引用工具返回的「结构准备度（规则分）」；不得改写为其他数值、"
        "“招聘方分数”或主观数字区间。主观判断只能定性表达并列出证据。"
    )
    lines.append(
        "- 报告必须区分工具规则发现、智能体复核发现和待用户确认事实；"
        "智能体补充的发现不得冒充工具输出。"
    )
    lines.append("")

    lines.append("## 边界")
    lines.append(report.get("disclaimer", ""))
    return "\n".join(lines)


def _xml_escape(text):
    return html.escape(str(text), quote=True)


def render_resume_html(model):
    name = html.escape(model.get("name", ""))
    headline = html.escape(model.get("headline", ""))
    contact = [html.escape(item) for item in model.get("contact", [])]
    summary = html.escape(model.get("summary", ""))
    parts = [
        "<!doctype html>",
        '<html lang="zh-CN">',
        "<head>",
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        "<title>Resume</title>",
        """<style>
        :root { color-scheme: light; }
        body { font-family: "Microsoft YaHei", "Noto Sans SC", Arial, sans-serif; color: #17212b; line-height: 1.55; margin: 40px auto; max-width: 800px; }
        h1 { font-size: 30px; margin-bottom: 4px; }
        h2 { border-bottom: 1px solid #cfd8dc; font-size: 20px; margin-top: 28px; padding-bottom: 4px; }
        h3 { font-size: 16px; margin-bottom: 4px; }
        .contact { color: #54616e; margin-top: 0; }
        ul { margin-top: 4px; padding-left: 20px; }
        @media print { body { margin: 18mm; max-width: none; } }
        </style>""",
        "</head>",
        "<body>",
        "<header>",
        "<h1>{}</h1>".format(name),
    ]
    if headline:
        parts.append('<div class="headline">{}</div>'.format(headline))
    if contact:
        parts.append('<p class="contact">{}</p>'.format(" | ".join(contact)))
    parts.append("</header>")
    if summary:
        parts.append("<h2>个人简介</h2><p>{}</p>".format(summary))
    for section in model.get("sections", []):
        parts.append("<h2>{}</h2>".format(html.escape(section.get("title", ""))))
        for item in section.get("items", []):
            if item.get("heading"):
                parts.append("<h3>{}</h3>".format(html.escape(item["heading"])))
            bullets = item.get("bullets", [])
            if bullets:
                parts.append("<ul>")
                for bullet in bullets:
                    parts.append("<li>{}</li>".format(html.escape(bullet)))
                parts.append("</ul>")
    parts.append("</body></html>")
    return "\n".join(parts)


def export_html(model, output_path):
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(render_resume_html(model))
    return output


_CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
</Types>"""

_ROOT_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>"""

_DOC_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>"""

_STYLES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:pPr><w:spacing w:after="80"/></w:pPr><w:rPr><w:rFonts w:eastAsia="Microsoft YaHei"/><w:sz w:val="36"/><w:b/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:pPr><w:spacing w:before="220" w:after="80"/><w:outlineLvl w:val="1"/></w:pPr><w:rPr><w:rFonts w:eastAsia="Microsoft YaHei"/><w:sz w:val="28"/><w:b/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading3"><w:name w:val="heading 3"/><w:pPr><w:spacing w:before="120" w:after="40"/><w:outlineLvl w:val="2"/></w:pPr><w:rPr><w:rFonts w:eastAsia="Microsoft YaHei"/><w:sz w:val="23"/><w:b/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="BodyText"><w:name w:val="Body Text"/><w:pPr><w:spacing w:after="80"/><w:ind w:left="240"/></w:pPr><w:rPr><w:rFonts w:eastAsia="Microsoft YaHei"/><w:sz w:val="21"/></w:rPr></w:style>
</w:styles>"""


def _docx_paragraph(text, style="BodyText"):
    return (
        '<w:p><w:pPr><w:pStyle w:val="{}"/></w:pPr>'
        '<w:r><w:t xml:space="preserve">{}</w:t></w:r></w:p>'
    ).format(style, _xml_escape(text))


def _docx_body(model):
    paragraphs = [_docx_paragraph(model.get("name", ""), "Title")]
    if model.get("headline"):
        paragraphs.append(_docx_paragraph(model["headline"], "BodyText"))
    if model.get("contact"):
        paragraphs.append(_docx_paragraph(" | ".join(model["contact"]), "BodyText"))
    if model.get("summary"):
        paragraphs.append(_docx_paragraph("个人简介", "Heading2"))
        paragraphs.append(_docx_paragraph(model["summary"], "BodyText"))
    for section in model.get("sections", []):
        paragraphs.append(_docx_paragraph(section.get("title", ""), "Heading2"))
        for item in section.get("items", []):
            if item.get("heading"):
                paragraphs.append(_docx_paragraph(item["heading"], "Heading3"))
            for bullet in item.get("bullets", []):
                paragraphs.append(_docx_paragraph("• " + bullet, "BodyText"))
    return "".join(paragraphs)


def export_docx(model, output_path):
    """Create a minimal but valid WordprocessingML DOCX package."""
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    document = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        "<w:body>{}<w:sectPr>"
        '<w:pgSz w:w="11906" w:h="16838"/>'
        '<w:pgMar w:top="1134" w:right="1134" w:bottom="1134" w:left="1134"/>'
        "</w:sectPr></w:body></w:document>"
    ).format(_docx_body(model))

    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as package:
        package.writestr("[Content_Types].xml", _CONTENT_TYPES)
        package.writestr("_rels/.rels", _ROOT_RELS)
        package.writestr("word/document.xml", document)
        package.writestr("word/_rels/document.xml.rels", _DOC_RELS)
        package.writestr("word/styles.xml", _STYLES)
    return output


def _extract_docx_text(source):
    try:
        with zipfile.ZipFile(source) as package:
            root = ElementTree.fromstring(package.read("word/document.xml"))
    except (OSError, KeyError, zipfile.BadZipFile, ElementTree.ParseError) as error:
        raise ResumeInputError("DOCX 解析失败：{}".format(error)) from error
    namespace = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
    return "\n".join(
        "".join(node.text or "" for node in paragraph.iter(namespace + "t")).strip()
        for paragraph in root.iter(namespace + "p")
    )


def _read_pdf_document(source):
    try:
        import pymupdf as pdf_backend
        backend_name = "PyMuPDF"
    except ImportError:
        try:
            import fitz as pdf_backend
            backend_name = "PyMuPDF(fitz)"
        except ImportError as error:
            raise ResumeInputError(
                "PDF 解析需要本地 PyMuPDF。请执行 `pip install pymupdf`，"
                "或先把 PDF 转成 Markdown / DOCX 文本。"
            ) from error

    document = None
    try:
        document = pdf_backend.open(str(source))
        if getattr(document, "needs_pass", False):
            raise ResumeInputError("PDF 已加密，无法读取；请先导出无密码版本。")
        page_texts = [page.get_text() for page in document]
        images = sum(len(page.get_images(full=True)) for page in document)
    except ResumeInputError:
        raise
    except Exception as error:
        raise ResumeInputError("PDF 解析失败：{}".format(error)) from error
    finally:
        if document is not None:
            document.close()

    raw_text = "\n\n".join(page_texts).strip()
    if len(raw_text) < 20:
        raise ResumeInputError(
            "PDF 可解析文字过少，可能是扫描件；请粘贴文字或先进行本地 OCR。"
        )
    backend_version = getattr(pdf_backend, "__version__", "unknown")
    warnings = []
    if images:
        warnings.append(
            "PDF 含 {} 张图片，未执行 OCR；图片内文字不会进入分析。".format(images)
        )
    manifest = {
        "type": "pdf",
        "filename": source.name,
        "backend": "{} {}".format(backend_name, backend_version),
        "pages": len(page_texts),
        "images": images,
        "text_chars": len(raw_text),
        "sha256": _sha256_file(source),
        "extraction_status": "text_extracted",
        "warnings": warnings,
    }
    return {"text": _normalise_plain_resume(raw_text), "manifest": manifest}


def read_resume_document(path):
    """Read Markdown, text, DOCX, or PDF with an explicit source manifest."""
    source = Path(path)
    if not source.is_file():
        raise FileNotFoundError("简历文件不存在：{}".format(source))
    suffix = source.suffix.lower()
    if suffix == ".pdf":
        return _read_pdf_document(source)
    if suffix == ".docx":
        raw_text = _extract_docx_text(source)
        return {
            "text": _normalise_plain_resume(raw_text),
            "manifest": {
                "type": "docx",
                "filename": source.name,
                "backend": "WordprocessingML",
                "pages": None,
                "images": None,
                "text_chars": len(raw_text),
                "sha256": _sha256_file(source),
                "extraction_status": "text_extracted",
                "warnings": ["DOCX 仅提取正文文字，复杂文本框和图片内文字可能丢失。"],
            },
        }
    if suffix == ".doc":
        raise ResumeInputError(
            "暂不支持旧版 .doc；请另存为 .docx、PDF 或 Markdown，"
            "也可以先复制正文并用 --resume-text - 从 stdin 读取。"
        )
    try:
        raw_text = source.read_text(encoding="utf-8")
    except UnicodeDecodeError as error:
        raise ResumeInputError("文本输入必须为 UTF-8；无法解码该文件。") from error
    return {
        "text": raw_text,
        "manifest": {
            "type": "markdown" if suffix in (".md", ".markdown") else "text",
            "filename": source.name,
            "backend": "utf-8",
            "pages": None,
            "images": 0,
            "text_chars": len(raw_text),
            "sha256": _sha256_file(source),
            "extraction_status": "text_loaded",
            "warnings": [],
        },
    }


def read_resume_text(value):
    """Read pasted resume text directly or from stdin with a source manifest."""
    if value == "-":
        raw_text = sys.stdin.read()
        filename = "<stdin>"
    else:
        raw_text = value
        filename = "<inline-text>"
    if not isinstance(raw_text, str) or not raw_text.strip():
        raise ResumeInputError("--resume-text 不能为空。")
    normalized = _normalise_plain_resume(raw_text)
    encoded = normalized.encode("utf-8")
    return {
        "text": normalized,
        "manifest": {
            "type": "text",
            "filename": filename,
            "backend": "utf-8",
            "pages": None,
            "images": 0,
            "text_chars": len(normalized),
            "sha256": hashlib.sha256(encoded).hexdigest(),
            "extraction_status": "text_loaded",
            "warnings": [],
        },
    }


def _load_resume_input(args):
    resume_text = getattr(args, "resume_text", None)
    if resume_text is not None:
        return read_resume_text(resume_text)
    return read_resume_document(args.resume)


def extract_text(path):
    """Extract normalized text from a supported resume input."""
    return read_resume_document(path)["text"]


def find_pdf_browser():
    """Find a local Chromium-compatible browser suitable for headless PDF export."""
    candidates = [
        Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
        Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
        Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
        Path(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"),
        Path.home() / r"AppData\Local\Google\Chrome\Application\chrome.exe",
        Path("/usr/bin/chromium"),
        Path("/usr/bin/chromium-browser"),
        Path("/usr/bin/google-chrome"),
    ]
    for candidate in candidates:
        if candidate.is_file():
            return str(candidate)

    for command in ("msedge", "chrome", "chromium", "google-chrome"):
        found = shutil.which(command)
        if found:
            return found
    return None


def export_pdf(model, output_path, browser_path=None, retries=2):
    """Render the resume to PDF with a local Chromium-compatible browser."""
    browser = browser_path or find_pdf_browser()
    if not browser:
        raise RuntimeError("未找到本机 Chromium/Edge/Chrome，无法导出 PDF；请安装浏览器或改用 DOCX/HTML。")
    if isinstance(retries, bool) or not isinstance(retries, int) or retries < 1:
        raise RuntimeError("PDF 重试次数必须是大于等于 1 的整数。")
    output = Path(output_path).resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="yotta-resume-") as tmp:
        page = Path(tmp) / "resume.html"
        export_html(model, page)
        last_detail = ""
        for attempt in range(1, retries + 1):
            if output.exists():
                output.unlink()
            profile_dir = Path(
                tempfile.mkdtemp(prefix="yotta-resume-profile-", dir=tmp)
            )
            command = [
                browser,
                "--headless=new",
                "--disable-gpu",
                "--no-first-run",
                "--disable-extensions",
                "--user-data-dir=" + str(profile_dir),
                "--print-to-pdf=" + str(output),
                page.as_uri(),
            ]
            try:
                completed = subprocess.run(
                    command,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    timeout=90,
                    check=False,
                )
                detail = completed.stderr.decode("utf-8", errors="replace").strip()
                if (
                    completed.returncode == 0
                    and output.is_file()
                    and output.read_bytes().startswith(b"%PDF")
                ):
                    return output
                last_detail = detail or "未生成有效 PDF"
            except subprocess.TimeoutExpired:
                last_detail = "浏览器渲染超时"
            except OSError as error:
                last_detail = str(error)
            if output.exists():
                output.unlink()
            if attempt < retries:
                time.sleep(min(0.2 * attempt, 0.5))
        raise RuntimeError(
            "PDF 导出失败（已尝试 {} 次）：{}".format(
                retries,
                last_detail or "浏览器未生成有效 PDF",
            )
        )
    return output


class ExportPlanError(ValueError):
    """Invalid output path combination supplied by the user."""


def _export_plan(args):
    configured = []
    for label, value in (
        ("DOCX", args.docx),
        ("HTML", args.html),
        ("PDF", args.pdf),
    ):
        if not value:
            continue
        target = Path(value).expanduser().resolve()
        configured.append((label, target))

    if not configured:
        raise ExportPlanError("未指定输出文件：请至少提供 --docx、--html 或 --pdf。")

    seen = {}
    for label, target in configured:
        key = os.path.normcase(str(target))
        if key in seen:
            raise ExportPlanError(
                "输出路径重复：{} 与 {} 指向同一文件：{}".format(
                    seen[key],
                    label,
                    target,
                )
            )
        seen[key] = label
        if target.exists() and target.is_dir():
            raise ExportPlanError("输出路径是目录，无法写入文件：{}".format(target))
    return configured


def _commit_export_outputs(staged, backup_dir):
    def move_path(source, destination):
        try:
            os.replace(source, destination)
        except OSError as error:
            if error.errno != errno.EXDEV:
                raise
            shutil.move(str(source), str(destination))

    backups = []
    committed = []
    backup_dir = Path(backup_dir)
    backup_dir.mkdir(parents=True, exist_ok=True)
    try:
        for index, (label, staged_path, target) in enumerate(staged):
            target.parent.mkdir(parents=True, exist_ok=True)
            backup = None
            if target.exists():
                backup = backup_dir / "{}-{}.bak".format(index, target.name)
                move_path(target, backup)
            backups.append((target, backup))
            move_path(staged_path, target)
            committed.append(target)
    except OSError:
        for target in reversed(committed):
            try:
                target.unlink()
            except OSError:
                pass
        for target, backup in reversed(backups):
            if backup is not None and backup.exists():
                try:
                    move_path(backup, target)
                except OSError:
                    pass
        raise


def cmd_audit(args):
    try:
        document = _load_resume_input(args)
        jd = read_resume_document(args.jd)["text"] if args.jd else ""
    except FileNotFoundError as error:
        print(str(error), file=sys.stderr)
        return 3
    except ResumeInputError as error:
        print(str(error), file=sys.stderr)
        return error.exit_code

    try:
        report = audit_resume(
            document["text"],
            jd,
            source_manifest=document["manifest"],
        )
    except RuntimeError as error:
        print(str(error), file=sys.stderr)
        return 5
    if args.format == "json":
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(render_audit_markdown(report))
    return 0


def cmd_export(args):
    try:
        document = read_resume_document(args.input)
    except FileNotFoundError as error:
        print(str(error), file=sys.stderr)
        return 3
    except ResumeInputError as error:
        print(str(error), file=sys.stderr)
        return error.exit_code

    try:
        plan = _export_plan(args)
    except ExportPlanError as error:
        print(str(error), file=sys.stderr)
        return 2

    model = parse_markdown_resume(document["text"])
    try:
        with tempfile.TemporaryDirectory(prefix="yotta-resume-export-") as tmp:
            root = Path(tmp)
            staged = []
            for index, (label, target) in enumerate(plan):
                staged_path = root / "output-{}{}".format(index, target.suffix)
                if label == "DOCX":
                    export_docx(model, staged_path)
                elif label == "HTML":
                    export_html(model, staged_path)
                else:
                    export_pdf(model, staged_path)
                staged.append((label, staged_path, target))
            _commit_export_outputs(staged, root / "backups")
    except RuntimeError as error:
        print(str(error), file=sys.stderr)
        return 4
    except OSError as error:
        print("导出文件写入失败：{}".format(error), file=sys.stderr)
        return 5

    print("已导出：" + "、".join(label for label, _ in plan))
    return 0


def cmd_contracts(args):
    report = validate_contracts(args.root, args.today)
    if args.format == "json":
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print("元简数据契约：{}".format("PASS" if report["ok"] else "FAIL"))
        print(
            "文件 {checked_files} / 岗位族 {role_family_count} / "
            "职级 {level_count} / 题目 {question_count} / 来源 {source_count} / "
            "行业 {industry_count}".format(
                **report
            )
        )
        for item in report["errors"]:
            print("- [{}] {}: {}".format(
                item["code"],
                item["path"],
                item["message"],
            ))
    return 0 if report["ok"] else 6


def _doctor_checks(root=None, today=None):
    checks = []
    errors = []
    warnings = []

    contract_report = validate_contracts(root, today)
    contract_status = "PASS" if contract_report.get("ok") else "FAIL"
    checks.append({
        "id": "contracts",
        "status": contract_status,
        "message": "数据契约校验通过" if contract_report.get("ok") else "数据契约校验失败",
    })
    for item in contract_report.get("errors", []):
        errors.append("[{}] {}: {}".format(
            item.get("code", "CONTRACT"),
            item.get("path", "data"),
            item.get("message", "unknown error"),
        ))

    package_root = SKILL_ROOT
    required_files = (
        "SKILL.md",
        "README.md",
        "references/usage.md",
        "references/faq.md",
        "references/data-contracts.md",
        "examples/resume.template.md",
        "examples/jd.example.md",
        "examples/audit-report.example.md",
        "examples/audit-report.example.json",
        "examples/interview-session.example.json",
        "examples/interview-review.example.md",
        "data/industry-registry.json",
        "data/industry-registry.schema.json",
        "data/interview-session.schema.json",
        "data/source-watch-state.json",
        "data/source-watch-state.schema.json",
        "scripts/yotta_resume.py",
        "scripts/contract_validate.py",
        "scripts/interview_engine.py",
    )
    missing = [name for name in required_files if not (package_root / name).is_file()]
    checks.append({
        "id": "package_files",
        "status": "PASS" if not missing else "FAIL",
        "message": (
            "关键随包文件完整"
            if not missing
            else "缺少关键文件：{}".format(", ".join(missing))
        ),
    })
    for name in missing:
        errors.append("缺少关键随包文件：{}".format(name))

    pdf_input = (
        importlib.util.find_spec("pymupdf") is not None
        or importlib.util.find_spec("fitz") is not None
    )
    checks.append({
        "id": "pdf_input",
        "status": "PASS" if pdf_input else "WARN",
        "message": (
            "PyMuPDF 可用，可读取文字层 PDF"
            if pdf_input
            else "未安装 PyMuPDF；PDF 输入不可用，可改用 Markdown/DOCX 或执行 pip install pymupdf"
        ),
    })
    if not pdf_input:
        warnings.append("PDF 输入需要 PyMuPDF；当前未检测到可用后端。")

    browser = find_pdf_browser()
    checks.append({
        "id": "pdf_export",
        "status": "PASS" if browser else "WARN",
        "message": (
            "PDF 导出浏览器可用：{}".format(browser)
            if browser
            else "未找到 Chromium/Chrome/Edge；PDF 导出不可用，仍可导出 DOCX/HTML"
        ),
    })
    if not browser:
        warnings.append("PDF 导出需要本机 Chromium、Chrome 或 Edge。")

    temp_ok = False
    try:
        with tempfile.TemporaryDirectory(prefix="yotta-resume-doctor-") as tmp:
            probe = Path(tmp) / "write-test.txt"
            probe.write_text("ok", encoding="utf-8")
            temp_ok = probe.read_text(encoding="utf-8") == "ok"
    except OSError as error:
        errors.append("临时目录不可写：{}".format(error))
    checks.append({
        "id": "temp_dir",
        "status": "PASS" if temp_ok else "FAIL",
        "message": "临时目录可读写" if temp_ok else "临时目录不可读写",
    })

    interview_state_ok = False
    try:
        interview_state_ok = interview.probe_state_support()
    except (OSError, ValueError) as error:
        errors.append("面试会话写入不可用：{}".format(error))
    checks.append({
        "id": "interview_state",
        "status": "PASS" if interview_state_ok else "FAIL",
        "message": (
            "面试会话可原子写入"
            if interview_state_ok
            else "面试会话原子写入不可用"
        ),
    })

    python_ok = sys.version_info >= (3, 8)
    checks.append({
        "id": "cli",
        "status": "PASS" if python_ok else "FAIL",
        "message": "Python {}.{}.{}".format(*sys.version_info[:3]),
    })
    if not python_ok:
        errors.append("需要 Python 3.8 或更高版本。")

    return {
        "ok": not errors,
        "version": VERSION,
        "checks": checks,
        "warnings": warnings,
        "errors": errors,
    }


def cmd_doctor(args):
    report = _doctor_checks(args.root, args.today)
    if args.format == "json":
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print("元简自检：{}".format("PASS" if report["ok"] else "FAIL"))
        print("版本：{}".format(report["version"]))
        for item in report["checks"]:
            print("- [{}] {}: {}".format(
                item["status"],
                item["id"],
                item["message"],
            ))
        for item in report["warnings"]:
            print("- WARN: {}".format(item))
        for item in report["errors"]:
            print("- FAIL: {}".format(item))
    return 0 if report["ok"] else 6


def _quickstart_next_steps(report):
    steps = [
        "核对 source_manifest、parse_warnings、industry_detection、issues、"
        "questions、unknowns 和 jd_match。",
        "只把用户确认的事实写入 Markdown，不补造数字、职责或结果。",
        "python scripts/yotta_resume.py export --input revised.md "
        "--docx revised.docx --html revised.html --pdf revised.pdf",
    ]
    industry = report.get("industry_detection", {}).get("primary_industry")
    if industry and industry != "cybersecurity":
        steps.append(
            "如需模拟面试，运行 interview start；非安全行业会自动使用 generic 岗位族。"
        )
    return steps


def cmd_quickstart(args):
    doctor_report = _doctor_checks(args.root, args.today)
    if not doctor_report["ok"]:
        print("元简自检未通过，先修复以下问题：", file=sys.stderr)
        for item in doctor_report.get("errors", []):
            print("- {}".format(item), file=sys.stderr)
        return 6
    try:
        document = _load_resume_input(args)
        jd = read_resume_document(args.jd)["text"] if args.jd else ""
    except FileNotFoundError as error:
        print(str(error), file=sys.stderr)
        return 3
    except ResumeInputError as error:
        print(str(error), file=sys.stderr)
        return error.exit_code
    try:
        report = audit_resume(
            document["text"],
            jd,
            source_manifest=document["manifest"],
        )
    except RuntimeError as error:
        print(str(error), file=sys.stderr)
        return 5
    payload = {
        "doctor": doctor_report,
        "audit": report,
        "next_steps": _quickstart_next_steps(report),
    }
    if args.format == "json":
        rendered = json.dumps(payload, ensure_ascii=False, indent=2)
    else:
        lines = [
            "# 元简快速开始",
            "",
            "## 自检",
            "",
            "- 状态：PASS",
            "- 版本：{}".format(doctor_report.get("version")),
            "",
            render_audit_markdown(report),
            "",
            "## 下一步",
            "",
        ]
        lines.extend("- {}".format(item) for item in payload["next_steps"])
        rendered = "\n".join(lines)
    if args.out:
        target = Path(args.out)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(rendered + "\n", encoding="utf-8", newline="\n")
    print(rendered)
    return 0


def _read_interview_answer(source):
    if source == "-":
        return sys.stdin.read()
    try:
        return Path(source).read_text(encoding="utf-8")
    except FileNotFoundError as error:
        raise interview.InterviewError(
            "回答文件不存在：{}".format(source),
            exit_code=3,
        ) from error
    except (OSError, UnicodeDecodeError) as error:
        raise interview.InterviewError(
            "回答文件无法读取：{}".format(error),
            exit_code=5,
        ) from error


def cmd_interview_start(args):
    target = Path(args.session)
    if target.exists() and not args.force:
        print(
            "会话文件已存在：{}；如需覆盖请显式追加 --force。".format(target),
            file=sys.stderr,
        )
        return 2
    try:
        document = _load_resume_input(args)
        jd = read_resume_document(args.jd)["text"] if args.jd else ""
    except FileNotFoundError as error:
        print(str(error), file=sys.stderr)
        return 3
    except ResumeInputError as error:
        print(str(error), file=sys.stderr)
        return error.exit_code
    try:
        report = audit_resume(
            document["text"],
            jd,
            source_manifest=document["manifest"],
        )
        session = interview.build_session(
            document["text"],
            jd,
            report,
            role_family=args.role_family,
            level=args.level,
            count=args.count,
            seed=args.seed,
            today=args.today,
        )
        interview.write_session_atomic(target, session)
    except interview.InterviewError as error:
        print(str(error), file=sys.stderr)
        return error.exit_code
    except RuntimeError as error:
        print(str(error), file=sys.stderr)
        return 5
    except OSError as error:
        print("会话状态写入失败：{}".format(error), file=sys.stderr)
        return 5
    if args.format == "json":
        print(json.dumps(session, ensure_ascii=False, indent=2))
    else:
        print(interview.render_session_markdown(session))
    return 0


def cmd_interview_answer(args):
    try:
        bank = interview.load_question_bank()
        session = interview.load_session(
            args.session,
            bank_version=bank.get("bank_version"),
        )
        answer = _read_interview_answer(args.answer)
        updated = interview.record_answer(session, answer)
        interview.write_session_atomic(args.session, updated)
    except interview.InterviewError as error:
        print(str(error), file=sys.stderr)
        return error.exit_code
    except OSError as error:
        print("会话状态写入失败：{}".format(error), file=sys.stderr)
        return 5
    if args.format == "json":
        print(json.dumps(updated, ensure_ascii=False, indent=2))
    else:
        print(interview.render_session_markdown(updated))
    return 0


def cmd_interview_review(args):
    try:
        bank = interview.load_question_bank()
        session = interview.load_session(
            args.session,
            bank_version=bank.get("bank_version"),
        )
        review = interview.build_review(session)
    except interview.InterviewError as error:
        print(str(error), file=sys.stderr)
        return error.exit_code
    if args.format == "json":
        print(json.dumps(review, ensure_ascii=False, indent=2))
    else:
        print(interview.render_review_markdown(review))
    return 0


def build_parser():
    parser = argparse.ArgumentParser(
        prog="yotta-resume",
        description="元简 — 本地求职者简历分析与成品导出技能：分析简历结构、证据、岗位匹配和风险，向用户追问缺失事实，给出逐条合理化修改建议，并把确认后的内容导出为 DOCX/PDF。边界：不编造经历，不承诺 ATS、面试或 Offer 结果；不自动投递；默认本地处理且不联网。",
    )
    sub = parser.add_subparsers(dest="command")

    audit = sub.add_parser("audit", help="分析简历并输出追问与建议")
    audit_source = audit.add_mutually_exclusive_group(required=True)
    audit_source.add_argument(
        "--resume", help="简历 Markdown、文本、DOCX 或 PDF 文件"
    )
    audit_source.add_argument(
        "--resume-text",
        help="直接传入简历文本；传 - 表示从 stdin 读取",
    )
    audit.add_argument("--jd", help="目标岗位 JD 文本文件")
    audit.add_argument("--format", choices=("json", "markdown"), default="markdown", help="输出格式")
    audit.set_defaults(func=cmd_audit)

    export = sub.add_parser("export", help="把确认后的简历导出为成品")
    export.add_argument("--input", required=True, help="简历 Markdown、文本、DOCX 或 PDF 文件")
    export.add_argument("--docx", help="输出 DOCX 文件")
    export.add_argument("--html", help="输出 HTML 文件")
    export.add_argument("--pdf", help="输出 PDF 文件")
    export.set_defaults(func=cmd_export)

    contracts = sub.add_parser("contracts", help="离线校验岗位族、题库、来源与双角色契约")
    contracts.add_argument("--root", help="data 目录或技能根目录；默认使用随包 data")
    contracts.add_argument("--format", choices=("json", "text"), default="json")
    contracts.add_argument("--today", help="覆盖校验日期（YYYY-MM-DD），用于测试与回放")
    contracts.set_defaults(func=cmd_contracts)

    doctor = sub.add_parser("doctor", help="检查随包文件、契约、PDF 依赖和输出环境")
    doctor.add_argument("--root", help="data 目录或技能根目录；默认使用随包 data")
    doctor.add_argument("--format", choices=("json", "text"), default="text")
    doctor.add_argument("--today", help="覆盖校验日期（YYYY-MM-DD），用于测试与回放")
    doctor.set_defaults(func=cmd_doctor)

    quickstart = sub.add_parser(
        "quickstart",
        help="自检、分析并输出下一步命令",
    )
    quickstart_source = quickstart.add_mutually_exclusive_group(required=True)
    quickstart_source.add_argument("--resume", help="简历文件")
    quickstart_source.add_argument(
        "--resume-text",
        help="直接传入简历文本；传 - 表示从 stdin 读取",
    )
    quickstart.add_argument("--jd", help="目标岗位 JD 文本文件")
    quickstart.add_argument(
        "--format",
        choices=("json", "markdown"),
        default="markdown",
    )
    quickstart.add_argument("--out", help="把结果写入本地文件")
    quickstart.add_argument("--root", help="data 目录或技能根目录")
    quickstart.add_argument("--today", help="覆盖校验日期 YYYY-MM-DD")
    quickstart.set_defaults(func=cmd_quickstart)

    interview_parser = sub.add_parser(
        "interview",
        help="运行本地单轮模拟面试并生成证据复盘",
    )
    interview_sub = interview_parser.add_subparsers(dest="interview_command")
    interview_sub.required = True

    interview_start = interview_sub.add_parser("start", help="开始或覆盖一轮模拟面试")
    interview_source = interview_start.add_mutually_exclusive_group(required=True)
    interview_source.add_argument("--resume", help="简历文件")
    interview_source.add_argument(
        "--resume-text",
        help="直接传入简历文本；传 - 表示从 stdin 读取",
    )
    interview_start.add_argument("--jd", help="目标岗位 JD 文本文件")
    interview_start.add_argument(
        "--role-family",
        help="显式指定岗位族；通用岗位用 generic",
    )
    interview_start.add_argument(
        "--level",
        choices=("junior", "mid", "senior", "lead"),
        help="求职目标职级；缺省为 mid",
    )
    interview_start.add_argument(
        "--count",
        type=int,
        default=interview.DEFAULT_COUNT,
        help="主题数量，默认 6，范围 3-10",
    )
    interview_start.add_argument("--seed", help="固定选题 seed，便于复算")
    interview_start.add_argument(
        "--session",
        required=True,
        help="本地会话 JSON 文件；必须显式指定",
    )
    interview_start.add_argument("--force", action="store_true", help="覆盖已有会话")
    interview_start.add_argument(
        "--format",
        choices=("json", "markdown"),
        default="markdown",
    )
    interview_start.add_argument("--today", help="覆盖校验日期 YYYY-MM-DD")
    interview_start.set_defaults(func=cmd_interview_start)

    interview_answer = interview_sub.add_parser("answer", help="记录当前问题的回答")
    interview_answer.add_argument("--session", required=True, help="会话 JSON 文件")
    interview_answer.add_argument(
        "--answer",
        required=True,
        help="回答文本文件；传 - 表示从 stdin 读取",
    )
    interview_answer.add_argument(
        "--format",
        choices=("json", "markdown"),
        default="markdown",
    )
    interview_answer.set_defaults(func=cmd_interview_answer)

    interview_review = interview_sub.add_parser("review", help="查看证据缺口复盘")
    interview_review.add_argument("--session", required=True, help="会话 JSON 文件")
    interview_review.add_argument(
        "--format",
        choices=("json", "markdown"),
        default="markdown",
    )
    interview_review.set_defaults(func=cmd_interview_review)
    return parser


def main(argv=None):
    args = list(sys.argv[1:] if argv is None else argv)
    if args in (["--version"], ["-V"]):
        print("yotta-resume {}".format(VERSION))
        return 0
    parser = build_parser()
    parsed = parser.parse_args(args)
    if not getattr(parsed, "func", None):
        parser.print_help()
        return 0
    return parsed.func(parsed)


if __name__ == "__main__":
    sys.exit(main())
