#!/usr/bin/env python3
"""Validate an AIDSO diagnosis plan, expand paid calls, and calculate points.

This script never calls a network service. It creates a local planned manifest only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import uuid
from collections import OrderedDict
from datetime import datetime
from decimal import Decimal
from pathlib import Path
from typing import Optional


PLATFORMS = {
    "DB": {"brand": "豆包", "terminal": "网页", "name": "豆包·网页版", "fast": "0.8", "thinking": "0.8", "thinking_label": "思考"},
    "DOUBA": {"brand": "豆包", "terminal": "手机", "name": "豆包·手机版", "fast": "0.8", "thinking": "0.8", "thinking_label": "思考"},
    "DP": {"brand": "DeepSeek", "terminal": "网页", "name": "DeepSeek·网页版", "fast": "0.8", "thinking": "0.8", "thinking_label": "深度"},
    "DPA": {"brand": "DeepSeek", "terminal": "手机", "name": "DeepSeek·手机版", "fast": "1", "thinking": "1", "thinking_label": "深度"},
    "TXYB": {"brand": "元宝（腾讯元宝）", "terminal": "网页", "name": "腾讯元宝·网页版", "fast": "0.8", "thinking": "0.8", "thinking_label": "深度"},
    "TXYBA": {"brand": "元宝（腾讯元宝）", "terminal": "手机", "name": "腾讯元宝·手机版", "fast": "1", "thinking": "1", "thinking_label": "深度"},
    "TYQW": {"brand": "千问", "terminal": "网页", "name": "千问·网页版", "fast": "0.8", "thinking": "0.8", "thinking_label": "深度"},
    "TYQWA": {"brand": "千问", "terminal": "手机", "name": "千问·手机版", "fast": "1", "thinking": "1", "thinking_label": "深度"},
    "BDAI": {"brand": "百度 AI", "terminal": "网页", "name": "百度 AI·网页版", "fast": "0.8", "thinking": None, "thinking_label": "深度"},
    "WXYY": {"brand": "文心", "terminal": "网页", "name": "文心·网页版", "fast": "0.8", "thinking": "0.8", "thinking_label": "深度"},
    "KIMI": {"brand": "Kimi", "terminal": "网页", "name": "Kimi·网页版", "fast": "0.8", "thinking": "0.8", "thinking_label": "思考"},
    "DYAI": {"brand": "AI 抖音", "terminal": "网页", "name": "AI 抖音·网页版", "fast": "0.8", "thinking": "0.8", "thinking_label": "深度"},
    "XHSA": {"brand": "红书问一问", "terminal": "手机", "name": "红书问一问·手机版", "fast": "3", "thinking": None, "thinking_label": "深度"},
}

ALIASES = {
    "豆包网页版": "DB", "豆包·网页版": "DB", "豆包web": "DB",
    "豆包手机版": "DOUBA", "豆包·手机版": "DOUBA", "豆包app": "DOUBA",
    "deepseek网页版": "DP", "deepseek·网页版": "DP", "deepseekweb": "DP",
    "deepseek手机版": "DPA", "deepseek·手机版": "DPA", "deepseekapp": "DPA",
    "腾讯元宝网页版": "TXYB", "腾讯元宝·网页版": "TXYB", "元宝网页版": "TXYB",
    "腾讯元宝手机版": "TXYBA", "腾讯元宝·手机版": "TXYBA", "元宝手机版": "TXYBA",
    "通义千问网页版": "TYQW", "通义千问·网页版": "TYQW", "千问网页版": "TYQW",
    "通义千问手机版": "TYQWA", "通义千问·手机版": "TYQWA", "千问手机版": "TYQWA",
    "百度ai网页版": "BDAI", "百度ai·网页版": "BDAI",
    "文心一言网页版": "WXYY", "文心一言·网页版": "WXYY",
    "kimi网页版": "KIMI", "kimi·网页版": "KIMI",
    "ai抖音网页版": "DYAI", "ai抖音·网页版": "DYAI", "抖音ai": "DYAI",
    "红书问一问手机版": "XHSA", "红书问一问·手机版": "XHSA", "小红书问一问": "XHSA",
}


def fail(message: str) -> None:
    raise ValueError(message)


def normalize_platform(value: object) -> str:
    raw = str(value).strip()
    code = raw.upper()
    if code in PLATFORMS:
        return code
    key = re.sub(r"[\s_-]+", "", raw).lower()
    if key in ALIASES:
        return ALIASES[key]
    fail(f"不支持的平台：{raw}")


def normalize_mode(value: object) -> str:
    raw = str(value).strip().lower()
    if raw in {"fast", "quick", "快速", "0"}:
        return "fast"
    if raw in {"thinking", "think", "deep", "思考", "深度", "1"}:
        return "thinking"
    fail(f"不支持的模式：{value}")


def clean_name(value: str) -> str:
    value = re.sub(r"[\\/:*?\"<>|]+", "-", value.strip())
    value = re.sub(r"\s+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-.")
    return value[:160] or "aidso-geo-task"


def decimal_text(value: Decimal) -> str:
    text = format(value.normalize(), "f")
    return "0" if text == "-0" else text


def platform_catalog() -> list[dict]:
    catalog = []
    for item in PLATFORMS.values():
        modes = [mode for mode in ("fast", "thinking") if item[mode] is not None]
        labels = [
            "快速" if mode == "fast" else item["thinking_label"]
            for mode in modes
        ]
        catalog.append(
            {
                "platform": item["brand"],
                "terminal": item["terminal"],
                "display_name": item["name"],
                "modes": labels,
                "points": {label: item[mode] for mode, label in zip(modes, labels)},
            }
        )
    return catalog


def load_plan(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"无法读取计划 JSON：{exc}")
    if not isinstance(data, dict):
        fail("计划 JSON 顶层必须是对象")
    return data


def is_within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
    except ValueError:
        return False
    return True


def workspace_path(
    path: Path,
    label: str,
    *,
    required_root: Optional[Path] = None,
    must_exist: bool = False,
) -> Path:
    workspace = Path.cwd().resolve()
    candidate = path if path.is_absolute() else workspace / path
    try:
        resolved = candidate.resolve(strict=must_exist)
    except OSError as exc:
        fail(f"{label}无法解析：{exc}")
    if not is_within(resolved, workspace):
        fail(f"{label}必须位于当前工作区内")
    if required_root is not None:
        root = (workspace / required_root).resolve()
        if not is_within(root, workspace):
            fail(f"{label}的规定目录不得通过符号链接逃逸工作区")
        if not is_within(resolved, root):
            fail(f"{label}必须位于当前工作区 {required_root.as_posix()}/ 下")
    return resolved


def authorization_scope(manifest: dict) -> dict:
    """Return the immutable paid scope used for confirmation authorization."""
    plan = manifest.get("plan") if isinstance(manifest.get("plan"), dict) else {}
    estimate = (
        manifest.get("estimate") if isinstance(manifest.get("estimate"), dict) else {}
    )
    targets = []
    for target in plan.get("targets", []):
        if isinstance(target, dict):
            targets.append(
                {
                    "platform_code": target.get("platform_code"),
                    "mode": target.get("mode"),
                }
            )
    jobs = []
    for job in manifest.get("jobs", []):
        if isinstance(job, dict):
            jobs.append(
                {
                    "job_id": job.get("job_id"),
                    "question_index": job.get("question_index"),
                    "prompt": job.get("prompt"),
                    "platform_code": job.get("platform_code"),
                    "mode": job.get("mode"),
                    "thinking_enabled": job.get("thinking_enabled"),
                    "repetition": job.get("repetition"),
                    "unit_points": job.get("unit_points"),
                }
            )
    return {
        "brand": plan.get("brand"),
        "product": plan.get("product") or None,
        "questions": plan.get("questions"),
        "targets": targets,
        "repetitions": plan.get("repetitions"),
        "report_path": plan.get("report_path"),
        "report_requirements": plan.get("report_requirements"),
        "jobs": jobs,
        "atomic_calls": estimate.get("atomic_calls"),
        "quoted_total_points": estimate.get("quoted_total_points"),
    }


def compute_plan_digest(manifest: dict) -> str:
    canonical = json.dumps(
        authorization_scope(manifest),
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(canonical).hexdigest()


def build_manifest(plan: dict, now: datetime, diagnosis_id: Optional[str]) -> dict:
    brand = str(plan.get("brand") or "").strip()
    if not brand:
        fail("brand（品牌名称）必填")
    product_raw = plan.get("product")
    product = str(product_raw).strip() if product_raw is not None else ""

    questions_raw = plan.get("questions")
    if not isinstance(questions_raw, list) or not questions_raw:
        fail("questions 必须是非空数组")
    questions = [str(item).strip() for item in questions_raw]
    if any(not item for item in questions):
        fail("questions 不得包含空问题")
    if len(set(questions)) != len(questions):
        fail("questions 存在重复项；请使用 repetitions 表示重复次数")

    repetitions = plan.get("repetitions", 1)
    if isinstance(repetitions, bool) or not isinstance(repetitions, int) or repetitions < 1:
        fail("repetitions 必须是正整数")
    if repetitions > 1000:
        fail("repetitions 超过 1000；请拆分任务并重新确认")

    route = str(plan.get("report_path") or "raw_data_custom_html").strip()
    if route != "raw_data_custom_html":
        fail("当前公开 API 仅支持从原始对话生成 raw_data_custom_html 报告")

    requirements_raw = plan.get("report_requirements")
    report_requirements = (
        str(requirements_raw).strip() if requirements_raw is not None else ""
    )

    targets_raw = plan.get("targets")
    if not isinstance(targets_raw, list) or not targets_raw:
        fail("targets 必须是非空数组")

    combinations: list[tuple[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for target in targets_raw:
        if not isinstance(target, dict):
            fail("targets 的每一项必须是对象")
        code = normalize_platform(target.get("platform"))
        modes = target.get("modes")
        if not isinstance(modes, list) or not modes:
            fail(f"{code} 必须至少选择一个模式")
        for raw_mode in modes:
            mode = normalize_mode(raw_mode)
            if PLATFORMS[code][mode] is None:
                fail(f"{PLATFORMS[code]['name']} 不支持{PLATFORMS[code]['thinking_label']}模式")
            pair = (code, mode)
            if pair in seen:
                fail(f"重复的平台-模式组合：{code}/{mode}")
            seen.add(pair)
            combinations.append(pair)

    stamp = now.strftime("%Y%m%d-%H%M")
    name_parts = [brand]
    if product:
        name_parts.append(product)
    terminal_count = len({code for code, _ in combinations})
    name_parts.extend([f"{len(questions)}题", f"{terminal_count}终端", stamp])
    task_name = clean_name("-".join(name_parts))
    local_id = diagnosis_id or f"aidso-{now.strftime('%Y%m%d')}-{uuid.uuid4().hex[:10]}"

    jobs = []
    breakdown: OrderedDict[tuple[str, str], dict] = OrderedDict()
    total = Decimal("0")
    sequence = 0
    for question_index, question in enumerate(questions, start=1):
        for code, mode in combinations:
            platform = PLATFORMS[code]
            unit = Decimal(str(platform[mode]))
            key = (code, mode)
            breakdown.setdefault(key, {"calls": 0, "unit": unit})
            for repetition in range(1, repetitions + 1):
                sequence += 1
                total += unit
                breakdown[key]["calls"] += 1
                jobs.append({
                    "job_id": f"j{sequence:05d}",
                    "question_index": question_index,
                    "prompt": question,
                    "platform_code": code,
                    "platform_name": platform["name"],
                    "mode": mode,
                    "mode_label": "快速" if mode == "fast" else platform["thinking_label"],
                    "thinking_enabled": 0 if mode == "fast" else 1,
                    "repetition": repetition,
                    "unit_points": decimal_text(unit),
                    "request_id": None,
                    "status": "PLANNED",
                })

    point_breakdown = []
    for (code, mode), item in breakdown.items():
        platform = PLATFORMS[code]
        subtotal = item["unit"] * item["calls"]
        point_breakdown.append({
            "platform_code": code,
            "platform_name": platform["name"],
            "mode": mode,
            "mode_label": "快速" if mode == "fast" else platform["thinking_label"],
            "calls": item["calls"],
            "unit_points": decimal_text(item["unit"]),
            "subtotal_points": decimal_text(subtotal),
        })

    created_at = now.isoformat(timespec="seconds")
    manifest = {
        "schema_version": 2,
        "diagnosis_id": local_id,
        "task_name": task_name,
        "created_at": created_at,
        "confirmed_at": None,
        "confirmation": None,
        "submitted_at": None,
        "status": "PLANNED",
        "plan": {
            "brand": brand,
            "product": product or None,
            "questions": questions,
            "targets": [
                {
                    "platform_code": code,
                    "platform_name": PLATFORMS[code]["name"],
                    "mode": mode,
                    "mode_label": "快速" if mode == "fast" else PLATFORMS[code]["thinking_label"],
                }
                for code, mode in combinations
            ],
            "repetitions": repetitions,
            "report_path": route,
            "report_requirements": report_requirements or "无",
            "auto_poll": False,
        },
        "estimate": {
            "price_source": "用户附件《爱搜GEOAPI文档》价格表（2026-08-25）；实时价格以 https://geo.aidso.com/question 为准",
            "terminal_count": terminal_count,
            "mode_combination_count": len(combinations),
            "atomic_calls": len(jobs),
            "total_points": decimal_text(total),
            "quoted_total_points": decimal_text(total),
            "breakdown": point_breakdown,
        },
        "jobs": jobs,
    }
    manifest["plan_digest"] = compute_plan_digest(manifest)
    return manifest


def confirmation(manifest: dict) -> str:
    plan = manifest["plan"]
    estimate = manifest["estimate"]
    product = plan.get("product") or "未设置（不生成产品层可见度分析）"
    lines = [
        "# 爱搜 GEO 诊断任务提交前确认",
        "",
        f"- 任务名称：{manifest['task_name']}",
        f"- 诊断 ID：{manifest['diagnosis_id']}",
        f"- 品牌：{plan['brand']}",
        f"- 产品：{product}",
        f"- 问题数：{len(plan['questions'])}",
        f"- 平台终端数：{estimate['terminal_count']}",
        f"- 平台终端-思考模式组合数：{estimate['mode_combination_count']}",
        f"- 每组诊断次数：{plan['repetitions']}",
        f"- 原子调用总数：{estimate['atomic_calls']}",
        f"- 确认报价积分：{estimate['quoted_total_points']}",
        f"- 计划摘要：{manifest['plan_digest']}",
        "- 报告路径：完整原始数据 → 定制单文件 HTML",
        f"- 报告自定义需求：{plan['report_requirements']}",
        "- 自动轮询：否；提交后凭任务 ID 或名称查询",
        "- 预计耗时：每轮对话约 10～30 分钟",
        "",
        "## 问题清单",
        "",
    ]
    lines.extend(f"{index}. {question}" for index, question in enumerate(plan["questions"], start=1))
    lines.extend(["", "## 积分明细", ""])
    for item in estimate["breakdown"]:
        lines.append(
            f"- {item['platform_name']} · {item['mode_label']}："
            f"{item['calls']} 次 × {item['unit_points']} = {item['subtotal_points']} 积分"
        )
    lines.extend([
        "",
        f"> 价格来源：{estimate['price_source']}",
        "> 对话数公式：问题数 × 平台终端数 × 所选思考模式数 × 对话轮数；各终端模式数不同时，以展开后的组合数为准。",
        "> 只有明确回复“确认执行”后才会调用 API 提交并产生积分消耗。",
    ])
    return "\n".join(lines)


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with path.open("x", encoding="utf-8") as stream:
            json.dump(payload, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
    except FileExistsError as exc:
        fail(f"拒绝覆盖已有文件：{path}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", type=Path, nargs="?", help="诊断计划 JSON")
    parser.add_argument("--list-platforms", action="store_true", help="输出完整平台、终端、模式与价格目录")
    parser.add_argument("-o", "--output", type=Path, help="写入 planned manifest")
    parser.add_argument("--format", choices=["confirmation", "json"], default="confirmation")
    parser.add_argument("--now", help="测试或固定命名时间，ISO-8601")
    parser.add_argument("--diagnosis-id", help="显式指定本地诊断 ID")
    args = parser.parse_args()
    try:
        if args.list_platforms:
            print(json.dumps(platform_catalog(), ensure_ascii=False, indent=2))
            return 0
        if args.plan is None:
            fail("缺少诊断计划 JSON；如需查看选项请使用 --list-platforms")
        now = datetime.fromisoformat(args.now) if args.now else datetime.now().astimezone()
        plan_path = workspace_path(args.plan, "计划 JSON", must_exist=True)
        manifest = build_manifest(load_plan(plan_path), now, args.diagnosis_id)
        if args.output:
            output_path = workspace_path(
                args.output,
                "manifest 输出",
                required_root=Path(".aidso-geo/tasks"),
            )
            write_json(output_path, manifest)
        if args.format == "json":
            print(json.dumps(manifest, ensure_ascii=False, indent=2))
        else:
            print(confirmation(manifest))
        return 0
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
