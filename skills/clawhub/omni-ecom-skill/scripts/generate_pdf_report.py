#!/usr/bin/env python3
"""Generate the default chart-led PDF delivery from report.json.

This module does not derive new business claims. It visualizes only metrics,
facts, judgments, actions and collaboration evidence already present in the
validated report package.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parents[1]
PDF_SKILL = ROOT / "skills" / "ecom-report-pdf-layout" / "scripts"
if str(PDF_SKILL) not in sys.path:
    sys.path.insert(0, str(PDF_SKILL))

from pdf_layout_kit import (  # type: ignore  # noqa: E402
    CONTENT_W,
    Paragraph,
    Spacer,
    body_left,
    build_doc,
    chart,
    cm,
    finding,
    judge,
    make_table,
    section_title,
    setup_matplotlib_cn,
    small,
    styles,
)


METRICS: list[tuple[str, str, str, bool]] = [
    ("gmv", "销售额", "money", False),
    ("net_gmv_reference", "净销售参考", "money", False),
    ("visitors", "访客数", "number", False),
    ("buyers", "支付买家", "number", False),
    ("orders", "订单量", "number", False),
    ("aov", "客单价", "money", False),
    ("conversion_rate", "支付转化率", "rate", False),
    ("refund_rate_amount", "金额退款率", "rate", True),
    ("roas", "ROAS", "ratio", False),
]


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def read_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(payload, dict):
        raise ValueError("report_json_invalid")
    return payload


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def num(value: Any) -> float | None:
    try:
        result = float(value)
        return result if math.isfinite(result) else None
    except (TypeError, ValueError):
        return None


def metric_value(row: dict[str, Any], key: str) -> float | None:
    for container in (row.get("metrics", {}), row.get("inputs", {}), row):
        if isinstance(container, dict) and key in container:
            return num(container.get(key))
    return None


def fmt(value: float | None, kind: str) -> str:
    if value is None:
        return "数据不足"
    if kind == "money":
        return f"{value:,.2f}元"
    if kind == "rate":
        return f"{value * 100:.2f}%"
    if kind == "ratio":
        return f"{value:.2f}"
    return f"{value:,.0f}"


def change(current: float | None, previous: float | None, kind: str) -> str:
    if current is None or previous in (None, 0):
        return "-"
    if kind == "rate":
        delta = (current - previous) * 100
        return f"{'↑' if delta > 0 else '↓' if delta < 0 else '—'}{abs(delta):.2f}pp" if delta else "—"
    delta = (current - previous) / abs(previous) * 100
    return f"{'↑' if delta > 0 else '↓' if delta < 0 else '—'}{abs(delta):.2f}%" if delta else "—"


def clean(value: Any, limit: int = 180) -> str:
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    return escape(text[:limit])


def strip_tag(text: str) -> str:
    """Drop a leading 【...】 tag so callers can prefix without doubling it."""
    return re.sub(r"^【[^】]*】\s*", "", str(text or "").strip())


def chart_sales(rows: list[dict[str, Any]], out: Path) -> bool:
    values = [(str(row.get("period", f"期间{i + 1}")), metric_value(row, "gmv")) for i, row in enumerate(rows)]
    values = [(label, value) for label, value in values if value is not None]
    if not values:
        return False
    setup_matplotlib_cn()
    import matplotlib.pyplot as plt
    labels, data = zip(*values)
    fig, ax = plt.subplots(figsize=(9, 3.4), dpi=160)
    bars = ax.bar(labels, data, color="#2E5AAC", width=0.55)
    ax.set_title("销售额趋势（元）", loc="left")
    ax.grid(axis="y", alpha=0.18)
    ax.spines[["top", "right"]].set_visible(False)
    ax.bar_label(bars, labels=[f"{v:,.0f}" for v in data], padding=3, fontsize=9)
    fig.tight_layout()
    fig.savefig(out, facecolor="white")
    plt.close(fig)
    return True


def chart_traffic(rows: list[dict[str, Any]], out: Path) -> bool:
    current = rows[-1] if rows else {}
    values = [("访客", metric_value(current, "visitors")), ("支付买家", metric_value(current, "buyers")), ("订单", metric_value(current, "orders"))]
    values = [(label, value) for label, value in values if value is not None]
    if len(values) < 2:
        return False
    setup_matplotlib_cn()
    import matplotlib.pyplot as plt
    labels, data = zip(*values)
    fig, ax = plt.subplots(figsize=(9, 3.4), dpi=160)
    bars = ax.barh(labels, data, color=["#6B8FD6", "#2E5AAC", "#8AA4D6"][: len(data)])
    ax.set_title("流量到成交规模（横轴为对数刻度）", loc="left")
    ax.set_xscale("log" if max(data) / max(min(data), 1) > 30 else "linear")
    ax.grid(axis="x", alpha=0.18)
    ax.spines[["top", "right"]].set_visible(False)
    ax.bar_label(bars, labels=[f"{v:,.0f}" for v in data], padding=4, fontsize=9)
    fig.tight_layout()
    fig.savefig(out, facecolor="white")
    plt.close(fig)
    return True


def chart_rates(rows: list[dict[str, Any]], out: Path) -> bool:
    current = rows[-1] if rows else {}
    previous = rows[-2] if len(rows) > 1 else None
    keys = [("支付转化率", "conversion_rate"), ("金额退款率", "refund_rate_amount")]
    labels: list[str] = []
    now_values: list[float] = []
    previous_values: list[float] = []
    for label, key in keys:
        value = metric_value(current, key)
        if value is not None:
            labels.append(label)
            now_values.append(value * 100)
            previous_values.append((metric_value(previous, key) or 0) * 100 if previous else 0)
    if not labels:
        return False
    setup_matplotlib_cn()
    import matplotlib.pyplot as plt
    import numpy as np
    x = np.arange(len(labels))
    width = 0.34
    fig, ax = plt.subplots(figsize=(9, 3.4), dpi=160)
    if previous:
        ax.bar(x - width / 2, previous_values, width, label="上一期", color="#B8C8E6")
        bars = ax.bar(x + width / 2, now_values, width, label="本期", color="#2E5AAC")
        ax.legend(frameon=False)
    else:
        bars = ax.bar(x, now_values, width=0.5, color="#2E5AAC")
    ax.set_title("关键比率（%）", loc="left")
    ax.set_xticks(x, labels)
    ax.grid(axis="y", alpha=0.18)
    ax.spines[["top", "right"]].set_visible(False)
    ax.bar_label(bars, labels=[f"{v:.2f}%" for v in now_values], padding=3, fontsize=9)
    fig.tight_layout()
    fig.savefig(out, facecolor="white")
    plt.close(fig)
    return True


def chart_actions(package: dict[str, Any], out: Path) -> bool:
    counts = Counter(str(item.get("priority") or "未分级") for item in package.get("actions", []) if isinstance(item, dict))
    if not counts:
        counts["待补数据"] = max(1, len(package.get("missing_data", [])))
    setup_matplotlib_cn()
    import matplotlib.pyplot as plt
    labels = list(counts)
    values = [counts[label] for label in labels]
    fig, ax = plt.subplots(figsize=(9, 3.4), dpi=160)
    bars = ax.bar(labels, values, color="#6B8FD6")
    ax.set_title("行动优先级分布", loc="left")
    ax.set_ylabel("行动数")
    ax.set_ylim(0, max(values) + 1)
    ax.spines[["top", "right"]].set_visible(False)
    ax.bar_label(bars, labels=[str(v) for v in values], padding=3)
    fig.tight_layout()
    fig.savefig(out, facecolor="white")
    plt.close(fig)
    return True


def chart_data_gate(package: dict[str, Any], out: Path) -> bool:
    values = [
        len(package.get("metrics", [])),
        len(package.get("sources", [])),
        len(package.get("missing_data", [])),
        len(package.get("risks", [])),
    ]
    setup_matplotlib_cn()
    import matplotlib.pyplot as plt
    labels = ["指标期间", "来源", "缺失项", "风险项"]
    fig, ax = plt.subplots(figsize=(9, 3.4), dpi=160)
    bars = ax.bar(labels, values, color=["#2E5AAC", "#6B8FD6", "#E6A23C", "#FF6B6B"])
    ax.set_title("数据闸门概况", loc="left")
    ax.set_ylim(0, max(values + [1]) + 1)
    ax.spines[["top", "right"]].set_visible(False)
    ax.bar_label(bars, labels=[str(v) for v in values], padding=3)
    fig.tight_layout()
    fig.savefig(out, facecolor="white")
    plt.close(fig)
    return True


def chart_participation(package: dict[str, Any], out: Path) -> bool:
    counts = Counter(
        "已贡献" if item.get("participation_status") == "contributed" else "待复核/未调用"
        for item in package.get("expert_participation", [])
        if isinstance(item, dict)
    )
    if not counts:
        return False
    setup_matplotlib_cn()
    import matplotlib.pyplot as plt
    labels = list(counts)
    values = [counts[label] for label in labels]
    fig, ax = plt.subplots(figsize=(9, 3.4), dpi=160)
    bars = ax.bar(labels, values, color=["#2E5AAC", "#B8C8E6"][: len(values)])
    ax.set_title("专家协作参与状态", loc="left")
    ax.set_ylabel("岗位数")
    ax.set_ylim(0, max(values) + 1)
    ax.spines[["top", "right"]].set_visible(False)
    ax.bar_label(bars, labels=[str(v) for v in values], padding=3)
    fig.tight_layout()
    fig.savefig(out, facecolor="white")
    plt.close(fig)
    return True


def render_charts(package: dict[str, Any], chart_dir: Path) -> list[tuple[Path, str]]:
    chart_dir.mkdir(parents=True, exist_ok=True)
    rows = [row for row in package.get("metrics", []) if isinstance(row, dict)]
    specs = [
        (chart_sales, (rows, chart_dir / "01-sales.png"), "图1 销售额趋势"),
        (chart_traffic, (rows, chart_dir / "02-traffic.png"), "图2 流量到成交规模"),
        (chart_rates, (rows, chart_dir / "03-rates.png"), "图3 转化与退款关键比率"),
        (chart_actions, (package, chart_dir / "04-actions.png"), "图4 行动优先级分布"),
        (chart_data_gate, (package, chart_dir / "05-data-gate.png"), "图5 数据闸门概况"),
        (chart_participation, (package, chart_dir / "06-participation.png"), "图6 专家协作参与状态"),
    ]
    result: list[tuple[Path, str]] = []
    for fn, args, caption in specs:
        if fn(*args):
            result.append((args[-1], caption))
    if len(result) < 3:
        raise ValueError("pdf_chart_minimum_not_met")
    return result


def page_decorator(canvas: Any, doc: Any) -> None:
    canvas.saveState()
    canvas.setFont("YaHei", 8)
    canvas.setFillColorRGB(0.42, 0.42, 0.42)
    canvas.drawString(2.5 * cm, 1.05 * cm, "标准经营报告 - 以 completion-receipt.json 为正式完成依据")
    canvas.drawRightString(18.5 * cm, 1.05 * cm, f"第 {doc.page} 页")
    canvas.restoreState()


def build_story(package: dict[str, Any], charts: list[tuple[Path, str]]) -> list[Any]:
    rows = [row for row in package.get("metrics", []) if isinstance(row, dict)]
    current = rows[-1] if rows else {}
    previous = rows[-2] if len(rows) > 1 else None
    story: list[Any] = [
        Paragraph(clean(package.get("title") or "电商经营分析报告"), styles["DocTitle"]),
        Paragraph(
            f"报告期：{clean(package.get('period'))} ｜ 任务：{clean(package.get('task_profile', {}).get('display_name'))} ｜ 专家团版本：{clean(package.get('team_version'))} ｜ 报告修订：{clean(package.get('report_revision'))} ｜ 数据闸门：{clean(package.get('gate_status'))}",
            styles["DocMeta"],
        ),
    ]
    summary = next((item.get("claim") for item in package.get("judgments", []) if isinstance(item, dict) and item.get("claim")), None)
    if not summary:
        summary = next((item.get("claim") for item in package.get("facts", []) if isinstance(item, dict) and item.get("claim")), "当前仅形成数据质量结论。")
    story += [judge(clean(summary, 260)), Spacer(1, 8)]

    story += [section_title("一", "核心指标速览")]
    metric_rows = [["指标", "本期", "上一期", "变化"]]
    for key, label, kind, _inverse in METRICS:
        cur = metric_value(current, key)
        prev = metric_value(previous, key) if previous else None
        if cur is not None:
            metric_rows.append([label, fmt(cur, kind), fmt(prev, kind), change(cur, prev, kind)])
    if len(metric_rows) > 1:
        story += [make_table(metric_rows, [4.0 * cm, 4.0 * cm, 4.0 * cm, 4.0 * cm], first_col_left=True)]
    else:
        story += [finding("当前数据闸门未提供可视化经营指标；以下只展示数据完整性和待补项。")]

    story += [section_title("二", "关键图表")]
    for path, caption in charts:
        story.extend(chart(str(path), caption=caption))

    story += [section_title("三", "事实、判断与限制")]
    for item in package.get("facts", [])[:8]:
        if isinstance(item, dict):
            story.append(body_left(f"【事实】{strip_tag(clean(item.get('claim'), 240))}"))
    for item in package.get("judgments", [])[:8]:
        if isinstance(item, dict):
            story.append(body_left(f"【判断/{clean(item.get('confidence') or '待定')}】{strip_tag(clean(item.get('claim'), 240))}"))
    for item in package.get("hypotheses", [])[:5]:
        if isinstance(item, dict):
            story.append(body_left(f"【待验证】{strip_tag(clean(item.get('claim'), 220))}；验证：{clean(item.get('verification_method'), 180)}"))
    for item in package.get("missing_data", [])[:12]:
        if isinstance(item, dict):
            detail = item.get("item") or item.get("name") or item.get("field") or item.get("description") or "待补项"
            purpose = item.get("purpose") or item.get("reason") or ""
            priority = item.get("priority") or ""
            suffix = "；".join(part for part in (f"用途：{purpose}" if purpose else "", f"优先级：{priority}" if priority else "") if part)
            story.append(small(f"待补数据：{clean(detail)}{('；' + suffix) if suffix else ''}"))
        else:
            story.append(small(f"待补数据：{clean(item)}"))

    story += [section_title("四", "优先行动")]
    action_rows = [["优先级", "动作", "负责人", "到期", "验收标准"]]
    for item in package.get("actions", [])[:10]:
        if isinstance(item, dict):
            action_rows.append([
                clean(item.get("priority") or "未分级", 20),
                clean(item.get("action"), 120),
                clean(item.get("owner") or "待指定", 30),
                clean(item.get("due") or "待指定", 16),
                clean(item.get("acceptance") or "待补充", 100),
            ])
    if len(action_rows) > 1:
        story.append(make_table(action_rows, [1.9 * cm, 5.4 * cm, 2.5 * cm, 1.6 * cm, 4.6 * cm], first_col_left=False))
    else:
        story.append(body_left("当前没有通过治理闸门的行动项。"))

    story += [section_title("五", "专家协作与版本凭证")]
    participation_rows = [["专家", "岗位", "状态", "Agent 子任务"]]
    for item in package.get("expert_participation", []):
        if isinstance(item, dict):
            agent_id = clean(item.get("agent_id"), 40)
            raw_status = clean(item.get("participation_status"), 24)
            if agent_id == "delivery-review" and raw_status in {"not_invoked", "pending_review"}:
                display_status = "交付前独立复核"
                display_task = "最终状态见放行凭证"
            else:
                display_status = raw_status
                display_task = clean(", ".join(item.get("agent_task_ids", [])) or "主任务", 70)
            participation_rows.append([
                clean(item.get("display_name") or item.get("agent_id"), 30),
                clean(item.get("profession"), 50),
                display_status,
                display_task,
            ])
    if len(participation_rows) > 1:
        story.append(make_table(participation_rows, [2.8 * cm, 4.8 * cm, 3.0 * cm, 5.4 * cm], first_col_left=True))
    for item in package.get("expert_participation", []):
        if isinstance(item, dict) and item.get("agent_id") != "delivery-review":
            summary = clean(item.get("contribution_summary") or "未提供贡献摘要", 180)
            story.append(small(f"{clean(item.get('display_name') or item.get('agent_id'), 30)}贡献：{summary}"))
    story += [
        small(f"专家团版本：{clean(package.get('team_version'))}；上一版本：{clean(package.get('team_previous_version'))}；本次报告修订：{clean(package.get('report_revision'))}。"),
        small("本 PDF 为已冻结复核候选稿。只有独立交付复核、公域隔离和最终完成闸门全部通过，且 completion-receipt.json 状态为 formal_delivery_complete 后，才构成正式交付。"),
    ]
    return story


def inspect_pdf(pdf_path: Path, render_dir: Path) -> dict[str, Any]:
    try:
        import fitz
    except ImportError as exc:
        raise ValueError("pdf_render_dependency_missing") from exc
    render_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(pdf_path)
    pages: list[dict[str, Any]] = []
    blank_pages: list[int] = []
    for index, page in enumerate(doc, 1):
        text = page.get_text().strip()
        images = len(page.get_images(full=True))
        if len(text) < 30 and images == 0:
            blank_pages.append(index)
        pix = page.get_pixmap(matrix=fitz.Matrix(1.25, 1.25), alpha=False)
        image_path = render_dir / f"page-{index:02d}.png"
        pix.save(image_path)
        pages.append({"page": index, "text_chars": len(text), "embedded_images": images, "render": image_path.name})
    page_count = doc.page_count
    text = "\n".join(page.get_text() for page in doc)
    doc.close()
    if page_count > 17 or blank_pages or not re.search(r"[\u4e00-\u9fff]", text):
        raise ValueError("pdf_render_quality_failed")
    return {"page_count": page_count, "blank_pages": blank_pages, "pages": pages, "text_chars": len(text)}


def generate(report_json: Path, output: Path, qa_output: Path, render_dir: Path) -> dict[str, Any]:
    package = read_json(report_json)
    required = ("team_version", "report_revision", "title", "gate_status", "expert_participation")
    if any(not package.get(key) for key in required):
        raise ValueError("report_package_missing_pdf_fields")
    chart_dir = output.parent / ".report_charts"
    charts = render_charts(package, chart_dir)
    output.parent.mkdir(parents=True, exist_ok=True)
    doc = build_doc(str(output), title=str(package.get("title") or "电商经营分析报告"))
    doc.build(build_story(package, charts), onFirstPage=page_decorator, onLaterPages=page_decorator)
    inspection = inspect_pdf(output, render_dir)
    receipt = {
        "schema_version": "1.0",
        "status": "pdf_render_verified",
        "team_version": package["team_version"],
        "report_revision": package["report_revision"],
        "report_file": output.name,
        "report_sha256": sha256(output),
        "report_bytes": output.stat().st_size,
        "chart_count": len(charts),
        "chart_files": [path.name for path, _caption in charts],
        "page_count": inspection["page_count"],
        "blank_pages": inspection["blank_pages"],
        "text_chars": inspection["text_chars"],
        "rendered_pages": inspection["pages"],
        "verified_at": utc_now(),
    }
    write_json(qa_output, receipt)
    return receipt


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate chart-led PDF from a report package")
    parser.add_argument("--report-json", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--qa-output", required=True)
    parser.add_argument("--render-dir", required=True)
    args = parser.parse_args()
    try:
        result = generate(
            Path(args.report_json).resolve(),
            Path(args.output).resolve(),
            Path(args.qa_output).resolve(),
            Path(args.render_dir).resolve(),
        )
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "pdf_generation_failed", "reason": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
