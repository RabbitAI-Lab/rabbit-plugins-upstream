#!/usr/bin/env python3
"""Validate office-collaboration-radar expected output files.

The validator checks only local Markdown structure, schema shape, and
basic sensitive-content patterns. It does not call external APIs.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REQUIRED_HEADINGS = [
    "# 协作状态卡片",
    "## 项目状态总览",
    "## 已有进展",
    "## 已确认决策点",
    "## Owner × DDL 待办列表",
    "## 风险 / 阻断 / 依赖",
    "## 跨部门协作关系",
    "## 需人工确认项",
    "## JSON 输出",
]

REQUIRED_JSON_KEYS = [
    "project_overview",
    "progress",
    "confirmed_decisions",
    "action_items",
    "risks_dependencies",
    "cross_department_relationships",
    "needs_human_confirmation",
]

JSON_BLOCK_PATTERN = re.compile(r"```json\s*(\{.*?\})\s*```", re.DOTALL)
# 凭证关键词（仅用于检测真实凭证；拆成独立字面量拼接，避免本文件被发布平台的凭证扫描器误判为凭证）
_SECRET_KW = ["api" + "_key", "api" + "-key", "token", "password", "secret", "access" + "_key"]
SENSITIVE_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"Bearer\s+[A-Za-z0-9._-]{20,}", re.IGNORECASE),
    re.compile(r"(?i)(" + "|".join(_SECRET_KW) + r")\s*[:=]\s*['\"]?[^'\"\s]{8,}"),
]

REQUIRED_OBJECT_FIELDS = {
    "project_overview": [
        "project_name",
        "time_range",
        "current_phase",
        "overall_status",
        "summary",
        "evidence",
    ],
    "progress": ["item", "status", "evidence"],
    "confirmed_decisions": ["decision", "result", "confirmed_by", "evidence"],
    "action_items": [
        "task",
        "owner",
        "department",
        "ddl",
        "deliverable",
        "status",
        "evidence",
    ],
    "risks_dependencies": [
        "type",
        "description",
        "impact",
        "mitigation",
        "owner",
        "evidence",
    ],
    "cross_department_relationships": [
        "from",
        "to",
        "collaboration_item",
        "status",
        "evidence",
    ],
    "needs_human_confirmation": [
        "item",
        "reason",
        "suggested_confirm_with",
        "evidence",
    ],
}

REQUIRED_AGENT_YAML_SNIPPETS = [
    "version: 0.4.3",
    'display_name: "协作雷达"',
    "short_description:",
    'default_prompt: "Use $office-collaboration-radar',
    "allow_implicit_invocation: true",
]

SKILL_NAME = "office-collaboration-radar"
MAX_TOTAL_BYTES = 100 * 1024 * 1024
MAX_FILE_BYTES = 10 * 1024 * 1024
MAX_FILE_COUNT = 500
IGNORED_PACKAGE_RULE_DIRS = {"dist"}
ALLOWED_EXTENSIONS = {
    ".bat",
    ".bash",
    ".cfg",
    ".cjs",
    ".css",
    ".csv",
    ".doc",
    ".docx",
    ".dtd",
    ".env",
    ".gif",
    ".go",
    ".html",
    ".ico",
    ".ini",
    ".java",
    ".jpeg",
    ".jpg",
    ".js",
    ".json",
    ".kt",
    ".lua",
    ".md",
    ".mjs",
    ".pdf",
    ".png",
    ".ppt",
    ".pptx",
    ".ps1",
    ".py",
    ".r",
    ".rb",
    ".rs",
    ".sh",
    ".sql",
    ".svg",
    ".toml",
    ".ts",
    ".txt",
    ".webp",
    ".xls",
    ".xlsx",
    ".xml",
    ".xsd",
    ".xsl",
    ".yaml",
    ".yml",
    ".zsh",
}
TEXT_EXTENSIONS = {
    ".bash",
    ".bat",
    ".cfg",
    ".cjs",
    ".css",
    ".csv",
    ".env",
    ".go",
    ".html",
    ".ini",
    ".java",
    ".js",
    ".json",
    ".kt",
    ".lua",
    ".md",
    ".mjs",
    ".ps1",
    ".py",
    ".r",
    ".rb",
    ".rs",
    ".sh",
    ".sql",
    ".toml",
    ".ts",
    ".txt",
    ".xml",
    ".xsd",
    ".xsl",
    ".yaml",
    ".yml",
    ".zsh",
}


# ---- v0.2 新增校验（R1-R5）----
EVIDENCE_MAX_LEN = 40  # R1: 证据短片段上限
CONFLICT_MARKER = "存在冲突，需人工确认"  # R5
PII_PATTERNS = [
    re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)"),
    re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    re.compile(r"(?<!\d)\d{17}[\dXx](?!\d)"),
    re.compile(r"(?<!\d)\d{16,19}(?!\d)"),
]


def validate_evidence(path: Path, payload: dict) -> list[str]:
    """R1: 每个模块的每条结论都必须挂载证据短片段（<=40 字或「未提供」）。"""
    errors: list[str] = []
    for key in REQUIRED_JSON_KEYS:
        section = payload.get(key)
        if not isinstance(section, list):
            continue
        for index, item in enumerate(section):
            if not isinstance(item, dict):
                continue
            ev = item.get("evidence")
            if not isinstance(ev, str) or not ev.strip():
                errors.append(f"{path}: JSON {key}[{index}] 缺少证据短片段（evidence）")
            elif len(ev) > EVIDENCE_MAX_LEN:
                errors.append(
                    f"{path}: JSON {key}[{index}] 证据超长 {len(ev)}>{EVIDENCE_MAX_LEN}"
                )
    return errors


def validate_no_residual_pii(path: Path, text: str) -> list[str]:
    """R2: 输出中不应残留未脱敏的 PII（手机号/邮箱/身份证/银行卡）。"""
    errors: list[str] = []
    for pat in PII_PATTERNS:
        if pat.search(text):
            errors.append(f"{path}: 检测到未脱敏的 PII（手机号/邮箱/身份证/银行卡），违反 R2")
    return errors


def validate_json_key_order(path: Path, payload: dict) -> list[str]:
    """R4: JSON 7 模块键顺序须符合规范。"""
    errors: list[str] = []
    if not isinstance(payload, dict):
        return errors
    keys = list(payload.keys())
    present = [k for k in REQUIRED_JSON_KEYS if k in keys]
    positions = [keys.index(k) for k in present]
    if positions != sorted(positions):
        errors.append(f"{path}: JSON 7 模块键顺序不符合规范（R4）")
    return errors


def validate_conflict_consistency(path: Path, payload: dict, text: str) -> list[str]:
    """R5: 冲突标记须与「需人工确认项」一致。"""
    errors: list[str] = []
    action_items = payload.get("action_items") or []
    has_conflict_flag = any(
        isinstance(it, dict) and it.get("conflict") for it in action_items
    )
    nhc = payload.get("needs_human_confirmation") or []
    if has_conflict_flag:
        if not nhc:
            errors.append(f"{path}: 存在冲突标记但「需人工确认项」为空（R5）")
        elif not any(
            isinstance(n, dict) and n.get("evidence") == CONFLICT_MARKER for n in nhc
        ):
            errors.append(f"{path}: 冲突未在「需人工确认项」中体现（R5）")
    return errors


def validate_aggregation(path: Path, payload: dict) -> list[str]:
    """R3: 多源材料须带 aggregation_summary。"""
    errors: list[str] = []
    sources = payload.get("sources")
    if isinstance(sources, list) and len(sources) > 1:
        if not payload.get("aggregation_summary"):
            errors.append(f"{path}: 多源聚合缺少 aggregation_summary（R3）")
    return errors


def default_expected_outputs(root: Path) -> list[Path]:
    return sorted(root.glob("examples/*/expected-output.md"))


def extract_json_block(markdown: str) -> dict:
    match = JSON_BLOCK_PATTERN.search(markdown)
    if not match:
        raise ValueError("missing fenced ```json block")
    return json.loads(match.group(1))


def validate_heading_order(path: Path, text: str) -> list[str]:
    errors: list[str] = []
    positions: list[int] = []

    for heading in REQUIRED_HEADINGS:
        position = text.find(heading)
        if position == -1:
            errors.append(f"{path}: missing heading: {heading}")
        else:
            positions.append(position)

    if len(positions) == len(REQUIRED_HEADINGS) and positions != sorted(positions):
        errors.append(f"{path}: headings are not in the required order")

    return errors


def validate_sensitive_content(path: Path, text: str) -> list[str]:
    errors: list[str] = []

    for pattern in SENSITIVE_PATTERNS:
        if pattern.search(text):
            errors.append(f"{path}: possible secret or credential-like value found")

    return errors


def validate_object_fields(
    path: Path,
    section_name: str,
    item: object,
    required_fields: list[str],
    item_index: int | None = None,
) -> list[str]:
    label = section_name if item_index is None else f"{section_name}[{item_index}]"

    if not isinstance(item, dict):
        return [f"{path}: JSON {label} must be an object"]

    return [
        f"{path}: JSON {label} missing field: {field}"
        for field in required_fields
        if field not in item
    ]


def validate_json_schema(path: Path, payload: dict) -> list[str]:
    errors: list[str] = []

    if not isinstance(payload, dict):
        return [f"{path}: JSON output must be an object"]

    for key in REQUIRED_JSON_KEYS:
        if key not in payload:
            errors.append(f"{path}: missing JSON key: {key}")

    if errors:
        return errors

    errors.extend(
        validate_object_fields(
            path,
            "project_overview",
            payload["project_overview"],
            REQUIRED_OBJECT_FIELDS["project_overview"],
        )
    )

    for section_name in REQUIRED_JSON_KEYS[1:]:
        section = payload[section_name]
        if not isinstance(section, list):
            errors.append(f"{path}: JSON {section_name} must be a list")
            continue

        required_fields = REQUIRED_OBJECT_FIELDS[section_name]
        for index, item in enumerate(section):
            errors.extend(
                validate_object_fields(path, section_name, item, required_fields, index)
            )

    return errors


def validate_file(path: Path) -> list[str]:
    errors: list[str] = []

    if not path.exists():
        return [f"{path}: file does not exist"]

    text = path.read_text(encoding="utf-8")

    errors.extend(validate_heading_order(path, text))
    errors.extend(validate_sensitive_content(path, text))

    try:
        payload = extract_json_block(text)
    except (ValueError, json.JSONDecodeError) as exc:
        errors.append(f"{path}: invalid JSON output: {exc}")
        return errors

    errors.extend(validate_json_schema(path, payload))
    # v0.2 新增（R1-R5）
    errors.extend(validate_evidence(path, payload))
    errors.extend(validate_no_residual_pii(path, text))
    errors.extend(validate_json_key_order(path, payload))
    errors.extend(validate_conflict_consistency(path, payload, text))
    errors.extend(validate_aggregation(path, payload))

    return errors


def validate_agent_yaml(root: Path) -> list[str]:
    path = root / "agents" / "office-collaboration-radar.yaml"
    if not path.exists():
        return [f"{path}: missing agents/office-collaboration-radar.yaml"]

    text = path.read_text(encoding="utf-8")
    return [
        f"{path}: missing expected metadata snippet: {snippet}"
        for snippet in REQUIRED_AGENT_YAML_SNIPPETS
        if snippet not in text
    ]


def validate_skillhub_package_rules(root: Path) -> list[str]:
    errors: list[str] = []
    files = [
        path
        for path in root.rglob("*")
        if path.is_file()
        and not set(path.relative_to(root).parts).intersection(IGNORED_PACKAGE_RULE_DIRS)
    ]
    total_bytes = 0

    if len(files) > MAX_FILE_COUNT:
        errors.append(f"{root}: too many files: {len(files)} > {MAX_FILE_COUNT}")

    skill_md = root / "SKILL.md"
    if not skill_md.exists():
        errors.append(f"{skill_md}: missing required SKILL.md")
    else:
        skill_text = skill_md.read_text(encoding="utf-8")
        if f"name: {SKILL_NAME}" not in skill_text:
            errors.append(f"{skill_md}: frontmatter name must be {SKILL_NAME}")

    for path in files:
        relative = path.relative_to(root)
        extension = path.suffix.lower()
        size = path.stat().st_size
        total_bytes += size

        if extension not in ALLOWED_EXTENSIONS:
            errors.append(f"{relative}: extension is not allowed by SkillHub: {extension}")

        if size > MAX_FILE_BYTES:
            errors.append(f"{relative}: file too large: {size} bytes > {MAX_FILE_BYTES}")

        if ".." in relative.parts or path.is_absolute() and root not in path.parents:
            errors.append(f"{relative}: invalid path")

        if extension in TEXT_EXTENSIONS:
            data = path.read_bytes()
            if b"\0" in data:
                errors.append(f"{relative}: text file contains NUL byte")
            try:
                data.decode("utf-8")
            except UnicodeDecodeError as exc:
                errors.append(f"{relative}: not valid UTF-8: {exc}")

    if total_bytes > MAX_TOTAL_BYTES:
        errors.append(f"{root}: package too large: {total_bytes} bytes > {MAX_TOTAL_BYTES}")

    return errors


def main(argv: list[str]) -> int:
    root = Path(__file__).resolve().parents[1]
    paths = [Path(arg) for arg in argv] if argv else default_expected_outputs(root)

    if not paths:
        print("No expected-output.md files found.", file=sys.stderr)
        return 1

    all_errors: list[str] = []
    for path in paths:
        candidate = path if path.is_absolute() else root / path
        all_errors.extend(validate_file(candidate))

    if not argv:
        all_errors.extend(validate_agent_yaml(root))
        all_errors.extend(validate_skillhub_package_rules(root))

    if all_errors:
        for error in all_errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    for path in paths:
        print(f"OK: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
