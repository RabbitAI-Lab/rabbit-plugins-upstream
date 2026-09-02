#!/usr/bin/env python3
"""Static contract check for the composite Skill package."""

from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LANES = {"character-count", "vip", "wanfang", "cnki", "aigc", "reduction", "report-verify", "guidance"}
COMMON = {
    "detection-knowledge.md",
    "aigc-knowledge.md",
    "intelligent-evaluation-knowledge.md",
    "character-count-standard.md",
    "async-workflow.md",
    "privacy-and-safety.md",
    "error-and-retry.md",
    "product-selection-playbook.md",
    "retrieval-and-matching-principles.md",
    "cross-system-differences.md",
    "report-interpretation.md",
    "preflight-checklist.md",
    "professional-faq.md",
}
PRODUCT_KNOWLEDGE = {"vip", "wanfang", "cnki"}


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def main() -> int:
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    config = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))
    if config.get("skill") != "paper-check" or set(config.get("lanes", [])) != LANES:
        fail("config skill/lanes 不完整")
    if config.get("default_environment") != "cqccjy" or config.get("environments") != ["cqccjy", "fanyu"]:
        fail("环境默认值或顺序不符合约定")
    if "MCP" not in skill or "独立界面" not in skill or "/api/paper/agent" in skill:
        fail("SKILL.md 未明确薄适配边界")
    for env, owner, deployment in (("cqccjy", 2, "current"), ("fanyu", 77, "config-only")):
        data = json.loads((ROOT / "domains" / f"{env}.json").read_text(encoding="utf-8"))
        if data.get("owner_user_id") != owner or data.get("deployment") != deployment:
            fail(f"{env} owner/deployment 不符合约定")
        if set(data.get("lanes", {})) != LANES:
            fail(f"{env} lane 不完整")
        for lane, route in data["lanes"].items():
            if not route.get("site", "").startswith("https://"):
                fail(f"{env}/{lane} site 非 HTTPS")
            for page in (route.get("pages") or {}).values():
                if not str(page).startswith("https://"):
                    fail(f"{env}/{lane} 页面地址非 HTTPS")
    for name in COMMON:
        if not (ROOT / "references" / "common" / name).is_file():
            fail(f"缺少 common reference: {name}")
    for lane in LANES:
        directory = ROOT / "references" / lane
        if not directory.is_dir() or not list(directory.glob("*.md")):
            fail(f"缺少 lane reference: {lane}")
    for lane in PRODUCT_KNOWLEDGE:
        if not (ROOT / "references" / lane / "products-and-scope.md").is_file():
            fail(f"缺少产品与检索范围知识: {lane}")
    if not (ROOT / "references" / "aigc" / "interpretation.md").is_file():
        fail("缺少 AIGC 解读知识")
    tutorial = ROOT / "references" / "report-verify" / "tutorial.md"
    if not tutorial.is_file():
        fail("缺少报告验真图文教程")
    required_assets = {
        "vpcs-verify-entry.png",
        "vpcs-verify-form.png",
        "wanfang-verify-form.png",
        "cnki-verify-form.png",
        "wanfang-aigc-report-redacted.png",
        "cnki-report-redacted.png",
        "vpcs-aigc-report-redacted.png",
        "vpcs-similarity-report-redacted.png",
    }
    for asset in required_assets:
        if not (ROOT / "assets" / "report-verify" / asset).is_file():
            fail(f"缺少报告验真示例图: {asset}")
    for required_phrase in (
        "product-selection-playbook.md",
        "retrieval-and-matching-principles.md",
        "cross-system-differences.md",
        "report-interpretation.md",
        "products-and-scope.md",
    ):
        if required_phrase not in skill:
            fail(f"SKILL.md 未路由专业知识: {required_phrase}")
    for source in ROOT.rglob("*.py"):
        if "__pycache__" in source.parts:
            continue
        try:
            ast.parse(source.read_text(encoding="utf-8"), filename=str(source))
        except SyntaxError as exc:
            fail(f"Python 语法错误 {source}: {exc}")
    client = (ROOT / "scripts" / "paper_check_client.py").read_text(encoding="utf-8")
    if "/api/paper/agent" in client or re.search(r"--(?:url|provider|employee-id)", client):
        fail("客户端包含旧 Agent API 或禁止参数")
    print("PASS: composite paper-check Skill static contract")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
