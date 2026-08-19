#!/usr/bin/env python3
"""Validate the six-skill JYS suite, shared resources, indexes, and eval fixtures."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


SKILLS = ("jys", "jys-s1", "jys-s2", "jys-s3", "jys-s4", "jys-s5")
REQUIRED_STATE_FIELDS = {
    "schema_version",
    "current_stage",
    "current_skill",
    "next_skill",
    "next_action",
    "waiting_for",
    "s1",
    "s2",
    "s3",
    "s4_outline",
    "s4_script",
    "s5_delivery",
    "final_confirmation",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> Any:
    return json.loads(read(path))


def markdown_links(text: str) -> list[str]:
    return re.findall(r"\[[^\]]*\]\(([^)]+)\)", text)


def frontmatter_keys(text: str) -> set[str]:
    if not text.startswith("---\n"):
        return set()
    end = text.find("\n---\n", 4)
    if end < 0:
        return set()
    keys = set()
    for line in text[4:end].splitlines():
        if line and not line.startswith(" ") and ":" in line:
            keys.add(line.split(":", 1)[0].strip())
    return keys


def validate(suite_root: Path) -> dict[str, Any]:
    failures: list[str] = []
    warnings: list[str] = []
    checked_files = 0

    for name in SKILLS:
        root = suite_root / name
        if not root.is_dir():
            failures.append(f"missing skill directory: {name}")
            continue
        entries = [p for p in root.rglob("SKILL.md") if "__pycache__" not in p.parts]
        if entries != [root / "SKILL.md"]:
            failures.append(f"{name}: expected exactly one root SKILL.md; found {[str(p.relative_to(root)) for p in entries]}")
        for path in root.rglob("*.md"):
            checked_files += 1
            try:
                text = read(path)
            except UnicodeDecodeError as exc:
                failures.append(f"invalid UTF-8: {path}: {exc}")
                continue
            for link in markdown_links(text):
                if link.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                target_text = link.split("#", 1)[0]
                if not target_text:
                    continue
                target = (path.parent / target_text).resolve()
                if not target.exists():
                    failures.append(f"broken link: {path.relative_to(suite_root)} -> {link}")

    jys = suite_root / "jys"
    for relative in (
        "references/workspace-contract.md",
        "references/creation-rules.md",
        "references/开头钩子设计指南.md",
        "assets/workspace-template.md",
        "assets/library-version.json",
        "evals/trigger_cases.json",
        "evals/state_transition_cases.json",
    ):
        if not (jys / relative).is_file():
            failures.append(f"jys missing shared artifact: {relative}")

    for child in SKILLS[1:]:
        skill_md = suite_root / child / "SKILL.md"
        if not skill_md.is_file():
            continue
        text = read(skill_md)
        if "../jys/references/workspace-contract.md" not in text:
            failures.append(f"{child}: missing explicit workspace contract dependency")
        if "默认由$jys主控调度" not in text:
            failures.append(f"{child}: description does not constrain natural-language routing to jys")

    behavior_contracts = {
        "jys-s4/SKILL.md": (
            "S2确定剧情走向和首段剧情功能，不锁定首段的具体台词、动作和画面",
            "references/01-事件级大纲.md",
            "references/02-逐段写作.md",
            "references/03-带货段落.md",
        ),
        "jys-s4/references/01-事件级大纲.md": (
            "台词、动作和画面必须按《开头钩子设计指南》重新构思",
            "不展开SKU和带货台词",
        ),
        "jys-s4/references/02-逐段写作.md": (
            "最后一句台词或动作及未完成事件",
            "不得删除事件级大纲已经确认的事件",
            "带货段不是普通剧情段",
            "对话优先自然、生活化",
            "使用一个可编辑 writing block",
            "修改正文前重新检查分析项目",
        ),
        "jys-s4/references/03-带货段落.md": (
            "不重新设计植入剧情",
            "完整SKU",
            "点击视频左下角链接",
            "【SKU复核】",
        ),
        "jys-s5/SKILL.md": (
            "【表情】【语气】不得省略",
            "使用段落分隔符，不使用软换行符",
        ),
        "jys-s5/references/text-output-guide.md": (
            "`【表情】``【语气】`不得省略",
            "完整交付使用一个可编辑 writing block",
        ),
    }
    for relative, required_phrases in behavior_contracts.items():
        path = suite_root / relative
        if not path.is_file():
            continue
        text = read(path)
        for phrase in required_phrases:
            if phrase not in text:
                failures.append(f"{relative}: missing behavior contract: {phrase}")

    s4_references = suite_root / "jys-s4" / "references"
    expected_s4_references = {"01-事件级大纲.md", "02-逐段写作.md", "03-带货段落.md"}
    if s4_references.is_dir():
        actual_s4_references = {path.name for path in s4_references.glob("*.md")}
        if actual_s4_references != expected_s4_references:
            failures.append(
                "jys-s4 reference structure mismatch: "
                f"missing={sorted(expected_s4_references-actual_s4_references)}, "
                f"stale={sorted(actual_s4_references-expected_s4_references)}"
            )
        combined_s4_text = "\n".join(read(path) for path in s4_references.glob("*.md"))
        for phrase in ("A路线", "B路线", "主对标原产品不得进入新大纲", "按S4共通内容取舍规则"):
            if phrase in combined_s4_text:
                failures.append(f"jys-s4 retains removed rule: {phrase}")

    s5_guide = suite_root / "jys-s5" / "references" / "text-output-guide.md"
    if s5_guide.is_file() and "【动作】`、`【表情】`、`【语气】`没有可确定内容时可以省略" in read(s5_guide):
        failures.append("jys-s5: retains forbidden optional action/expression/tone rule")

    forbidden = ("../jys-s4/references/creation-rules.md", "../jys-s2/references/开头钩子设计指南.md")
    for name in SKILLS:
        path = suite_root / name / "SKILL.md"
        if path.is_file():
            text = read(path)
            for value in forbidden:
                if value in text:
                    failures.append(f"{name}: retains cross-child dependency {value}")

    template = jys / "assets" / "workspace-template.md"
    if template.is_file():
        missing = sorted(REQUIRED_STATE_FIELDS - frontmatter_keys(read(template)))
        if missing:
            failures.append(f"workspace template missing state fields: {', '.join(missing)}")

    version_path = jys / "assets" / "library-version.json"
    if version_path.is_file():
        try:
            version = load_json(version_path)
        except Exception as exc:
            failures.append(f"invalid library-version.json: {exc}")
        else:
            for key in ("version", "updated_at", "updated_by"):
                if not isinstance(version, dict) or not version.get(key):
                    failures.append(f"library-version.json missing {key}")

    kernels = jys / "assets" / "kernels"
    if kernels.is_dir():
        actual = {p.name for p in kernels.iterdir() if p.is_dir()}
        indexed = set(re.findall(r"^##\s+(.+?)\s*$", read(kernels / "index.md"), re.MULTILINE))
        if actual != indexed:
            failures.append(f"kernel index mismatch: missing={sorted(actual-indexed)}, stale={sorted(indexed-actual)}")
        for directory in actual:
            if not (kernels / directory / "kernel.md").is_file():
                failures.append(f"kernel missing kernel.md: {directory}")

    products = jys / "assets" / "products"
    if products.is_dir():
        actual = {p.stem for p in products.glob("*.md") if p.name != "index.md" and not p.name.endswith(".bak")}
        index_text = read(products / "index.md")
        overview = index_text.split("## 产品总览", 1)[-1].split("## 产品黑名单", 1)[0]
        indexed = {
            match.strip()
            for match in re.findall(r"^\|\s*([^|]+?)\s*\|\s*$", overview, re.MULTILINE)
            if match.strip() not in {"产品名称", "---------"} and set(match.strip()) != {"-"}
        }
        if actual != indexed:
            failures.append(f"product index mismatch: missing={sorted(actual-indexed)}, stale={sorted(indexed-actual)}")

    trigger_path = jys / "evals" / "trigger_cases.json"
    if trigger_path.is_file():
        try:
            cases = load_json(trigger_path)
        except Exception as exc:
            failures.append(f"invalid trigger_cases.json: {exc}")
        else:
            for bucket in ("should_trigger", "should_not_trigger", "near_neighbor", "routing_cases"):
                if not isinstance(cases, dict) or not cases.get(bucket):
                    failures.append(f"trigger_cases.json missing {bucket}")

    state_path = jys / "evals" / "state_transition_cases.json"
    if state_path.is_file():
        try:
            state_cases = load_json(state_path)
        except Exception as exc:
            failures.append(f"invalid state_transition_cases.json: {exc}")
        else:
            rows = state_cases.get("cases", []) if isinstance(state_cases, dict) else []
            if len(rows) < 6:
                failures.append("state_transition_cases.json needs at least 6 cases")
            for index, row in enumerate(rows):
                for key in ("name", "state", "user_input", "expected_skill"):
                    if not isinstance(row, dict) or key not in row:
                        failures.append(f"state transition case {index} missing {key}")

    return {
        "ok": not failures,
        "suite_root": str(suite_root),
        "skills": list(SKILLS),
        "checked_markdown_files": checked_files,
        "failures": failures,
        "warnings": warnings,
        "evidence": {
            "static_suite_validation": "pass" if not failures else "fail",
            "provider_backed_routing_eval": "missing evidence",
            "human_end_to_end_review": "missing evidence",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate the JYS six-skill suite and its shared contracts.")
    parser.add_argument("suite_root", nargs="?", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--output", type=Path, help="Optional JSON report path")
    args = parser.parse_args()
    result = validate(args.suite_root.resolve())
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    if not result["ok"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
