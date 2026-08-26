#!/usr/bin/env python3
"""Render an audited GEO report model as a self-contained HTML file."""

from __future__ import annotations

import argparse
import copy
import html
import json
import math
import re
import sys
from pathlib import Path
from typing import Any, Optional
from urllib.parse import urlsplit

SCRIPT_DIRECTORY = Path(__file__).resolve().parent
if str(SCRIPT_DIRECTORY) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIRECTORY))

from artifact_safety import extract_visible_text, find_user_facing_leaks
from brand_score import METHOD_ID as TEMPLATE_SCORE_METHOD
from brand_score import calculate_brand_score
from plan_diagnosis import PLATFORMS


BASE_SECTION_ORDER = [
    "report-intro",
    "overall",
    "visibility",
    "ranking",
    "products",
    "sentiment",
    "sources",
    "recommendations",
    "appendix-a",
    "appendix-b",
    "appendix-c",
]
PRODUCT_SECTION_ORDER = [
    "report-intro",
    "overall",
    "visibility",
    "product-visibility",
    "ranking",
    "products",
    "sentiment",
    "sources",
    "recommendations",
    "appendix-a",
    "appendix-b",
    "appendix-c",
    "appendix-d",
]
COLORS = {"purple", "green", "orange", "red", "blue"}
SCOPES = {"brand", "product"}
NO_PRODUCT_LEAKS = (
    "产品提及率",
    "产品层 AI 可见度",
    "产品层AI可见度",
    "品牌→产品转化",
    "品牌→产品承接率",
)
PRODUCT_ANALYSIS_TERMS = (
    "曝光",
    "露出",
    "出镜",
    "可见",
    "提及",
    "推荐",
    "出现",
    "频次",
    "概率",
    "转化",
    "承接",
    "份额",
    "占比",
    "排名",
    "声量",
    "渗透",
    "覆盖",
)
PRODUCT_TARGET_REFERENCES = (
    "目标产品",
    "该产品",
    "本产品",
    "此产品",
    "这款产品",
    "上述产品",
)
CSP = (
    "default-src 'none'; connect-src 'none'; frame-src 'none'; "
    "object-src 'none'; base-uri 'none'; form-action 'none'; "
    "style-src 'unsafe-inline'; img-src https: data:"
)
BUNDLED_CSS_PATH = Path(__file__).resolve().parent.parent / "assets" / "report.css"
PROVENANCE_ATTR_KEYS = {
    "task_id": "任务标识",
    "task_name": "任务名称",
    "data_period": "数据周期",
    "data_time": "数据时间",
    "direct_report_source": "报告来源",
}
DISPLAY_PLATFORM_MODES = {
    f"{item['name']}｜{'快速' if mode == 'fast' else item['thinking_label']}"
    for item in PLATFORMS.values()
    for mode in ("fast", "thinking")
    if item[mode] is not None
}


def esc(value: Any) -> str:
    if value is None:
        return "—"
    return html.escape(str(value), quote=True)


def safe_url(value: Any) -> Optional[str]:
    if not isinstance(value, str):
        return None
    value = value.strip()
    try:
        parsed = urlsplit(value)
    except ValueError:
        return None
    return value if parsed.scheme in {"http", "https"} and parsed.netloc else None


def official_aidso_url(value: Any) -> Optional[str]:
    if not isinstance(value, str):
        return None
    candidate = value.strip()
    try:
        parsed = urlsplit(candidate)
        port = parsed.port
    except ValueError:
        return None
    hostname = (parsed.hostname or "").rstrip(".").lower()
    official_host = hostname == "aidso.com" or hostname.endswith(".aidso.com")
    if (
        parsed.scheme != "https"
        or not official_host
        or parsed.username is not None
        or parsed.password is not None
        or port not in {None, 443}
    ):
        return None
    return candidate


def number(value: Any, fallback: float = 0.0) -> float:
    try:
        result = float(value)
    except (TypeError, ValueError):
        return fallback
    return result if math.isfinite(result) else fallback


def render_cell(value: Any) -> str:
    if isinstance(value, dict):
        text = esc(value.get("text", "—"))
        url = safe_url(value.get("url"))
        if url:
            return f'<a href="{esc(url)}" target="_blank" rel="noopener noreferrer">{text}</a>'
        return text
    return esc(value)


def render_info_score(block: dict) -> str:
    items = []
    for item in block.get("items", []):
        items.append(
            '<div class="info-item">'
            f'<div class="label">{esc(item.get("label"))}</div>'
            f'<div class="value">{esc(item.get("value"))}</div>'
            "</div>"
        )
    score = block.get("score") or {}
    score_html = (
        '<div class="score-card"><div>'
        f'<div class="score">{esc(score.get("value", "—"))}'
        f'<small>{esc(score.get("suffix", "/100"))}</small></div>'
        f'<div class="score-label">{esc(score.get("label", "GEO 品牌得分"))}</div>'
        f'<div class="score-note">{esc(score.get("note", ""))}</div>'
        "</div></div>"
    )
    return f'<div class="intro-grid"><div class="info-list">{"".join(items)}</div>{score_html}</div>'


def render_kpis(block: dict) -> str:
    output = []
    for item in block.get("items", []):
        color = str(item.get("color") or "purple")
        color = color if color in COLORS else "purple"
        output.append(
            '<div class="kpi-card">'
            f'<div class="kpi-value {color}">{esc(item.get("value"))}</div>'
            f'<div class="kpi-label">{esc(item.get("label"))}</div>'
            f'<div class="kpi-sub">{esc(item.get("sub", ""))}</div>'
            "</div>"
        )
    return f'<div class="kpi-grid">{"".join(output)}</div>'


def render_table(block: dict) -> str:
    headers = block.get("headers") or []
    rows = block.get("rows") or []
    min_width = max(0, min(int(number(block.get("min_width"), 0)), 3000))
    style = f' style="min-width:{min_width}px"' if min_width else ""
    head = "".join(f"<th>{esc(item)}</th>" for item in headers)
    body_rows = []
    for row in rows:
        if not isinstance(row, list):
            raise ValueError("table.rows 的每一行必须是数组")
        body_rows.append("<tr>" + "".join(f"<td>{render_cell(value)}</td>" for value in row) + "</tr>")
    return (
        f'<div class="table-wrap"><table{style}><thead><tr>{head}</tr></thead>'
        f'<tbody>{"".join(body_rows)}</tbody></table></div>'
    )


def render_heatmap(block: dict) -> str:
    columns = block.get("columns") or []
    rows = block.get("rows") or []
    head = "".join(f"<th>{esc(item)}</th>" for item in columns)
    body = []
    for row in rows:
        label = esc(row.get("label"))
        cells = [f"<td>{label}</td>"]
        for value in row.get("values", []):
            if value is None:
                cells.append('<td><div class="heat-cell" style="background:#f4f4f8;color:#999">—</div></td>')
                continue
            value_num = max(0.0, min(100.0, number(value)))
            alpha = 0.08 + 0.55 * value_num / 100.0
            cells.append(
                '<td><div class="heat-cell" '
                f'style="background:rgba(108,80,255,{alpha:.3f})">{value_num:.1f}%</div></td>'
            )
        body.append(f"<tr>{''.join(cells)}</tr>")
    return (
        '<div class="table-wrap"><table style="min-width:760px">'
        f'<thead><tr>{head}</tr></thead><tbody>{"".join(body)}</tbody></table></div>'
    )


def render_bars(block: dict) -> str:
    maximum = max(number(block.get("max"), 100), 0.000001)
    output = []
    for row in block.get("rows", []):
        target = bool(row.get("target"))
        width = max(0.0, min(100.0, number(row.get("value")) / maximum * 100.0))
        target_class = " target" if target else ""
        output.append(
            '<div class="bar-row">'
            f'<div class="bar-label{target_class}">{esc(row.get("label"))}</div>'
            f'<div class="bar-track"><div class="bar-fill{target_class}" style="width:{width:.2f}%"></div></div>'
            f'<div class="bar-value">{esc(row.get("display", row.get("value")))}</div>'
            "</div>"
        )
    return "".join(output)


def render_scatter(block: dict) -> str:
    y_max = max(2.0, number(block.get("y_max"), 8))
    parts = ['<svg class="chart-svg" viewBox="0 0 920 470" role="img" aria-label="品牌提及率与平均排名散点图">']
    for tick in range(0, 101, 20):
        x = 70 + 8.1 * tick
        parts.append(f'<line stroke="#e9e7f5" x1="{x:.1f}" x2="{x:.1f}" y1="35" y2="415"></line>')
        parts.append(f'<text fill="#64748b" font-size="11" text-anchor="middle" x="{x:.1f}" y="445">{tick}%</text>')
    rank = 1
    while rank <= int(math.ceil(y_max)):
        y = 35 + (rank - 1) / (y_max - 1) * 380
        parts.append(f'<line stroke="#e9e7f5" x1="70" x2="880" y1="{y:.1f}" y2="{y:.1f}"></line>')
        parts.append(f'<text fill="#64748b" font-size="11" text-anchor="middle" x="48" y="{y + 4:.1f}">{rank}</text>')
        rank += 1
    parts.append('<text fill="#64748b" font-size="12" text-anchor="middle" x="460" y="466">品牌提及率</text>')
    parts.append('<text fill="#64748b" font-size="12" text-anchor="middle" transform="rotate(-90 14 235)" x="14" y="235">平均排名（越小越好）</text>')
    palette = ["#27b3a2", "#f59e0b", "#ef5da8", "#4e7cff", "#16a34a", "#ef4444", "#8b5cf6"]
    for index, point in enumerate(block.get("points", [])):
        x = 70 + 8.1 * max(0.0, min(100.0, number(point.get("x"))))
        y_value = max(1.0, min(y_max, number(point.get("y"), y_max)))
        y = 35 + (y_value - 1) / (y_max - 1) * 380
        radius = max(8.0, min(28.0, number(point.get("size"), 14)))
        target = bool(point.get("target"))
        fill = "#6c50ff" if target else palette[index % len(palette)]
        weight = "700" if target else "500"
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" fill="{fill}" fill-opacity=".78" r="{radius:.1f}"></circle>')
        parts.append(f'<text fill="#334155" font-size="12" font-weight="{weight}" x="{x + radius + 4:.1f}" y="{y + 4:.1f}">{esc(point.get("label"))}</text>')
    parts.append("</svg>")
    return "".join(parts)


def render_platform_cards(block: dict) -> str:
    items = []
    for item in block.get("items", []):
        items.append(
            '<div class="platform-card">'
            f'<h4>{esc(item.get("title"))}</h4>'
            f'<span class="tier">{esc(item.get("tier"))}</span>'
            f'<p>{esc(item.get("text"))}</p>'
            "</div>"
        )
    return f'<div class="platform-cards">{"".join(items)}</div>'


def render_product_cards(block: dict) -> str:
    output = []
    for item in block.get("items", []):
        url = safe_url(item.get("url"))
        image_url = safe_url(item.get("image_url"))
        tag = "a" if url else "div"
        attrs = f' href="{esc(url)}" target="_blank" rel="noopener noreferrer"' if url else ""
        image_html = (
            f'<img src="{esc(image_url)}" alt="{esc(item.get("title", "商品图片"))}" loading="lazy"/>'
            if image_url
            else '<div class="img-placeholder">暂无图片</div>'
        )
        output.append(
            f'<{tag} class="product-card"{attrs}>'
            f'<div class="product-image">{image_html}</div>'
            '<div class="product-body">'
            f'<div class="product-rank">{esc(item.get("rank", "—"))}</div>'
            f'<div class="product-title">{esc(item.get("title"))}</div>'
            f'<div class="product-meta">{esc(item.get("meta", ""))}</div>'
            '<div class="product-stat">'
            f'<span>{esc(item.get("stat_label", ""))}</span><b>{esc(item.get("stat_value", ""))}</b>'
            "</div>"
            f'<span class="product-brand">{esc(item.get("brand", "未知品牌"))}</span>'
            f'</div></{tag}>'
        )
    return f'<div class="products">{"".join(output)}</div>'


def render_word_cloud(block: dict) -> str:
    words = []
    for item in block.get("items", []):
        cls = "word neg" if item.get("negative") else "word"
        words.append(f'<span class="{cls}">{esc(item.get("text"))}</span>')
    return f'<div class="word-cloud">{"".join(words)}</div>'


def render_recommendations(block: dict) -> str:
    output = []
    for item in block.get("items", []):
        priority = str(item.get("priority") or "P2").upper()
        if priority not in {"P0", "P1", "P2"}:
            priority = "P2"
        output.append(
            '<div class="rec">'
            f'<div class="priority">{priority}</div>'
            '<div>'
            f'<h4>{esc(item.get("title"))}</h4>'
            f'<p>{esc(item.get("text"))}</p>'
            "</div></div>"
        )
    return f'<div class="rec-grid">{"".join(output)}</div>'


def render_block(block: dict) -> str:
    kind = block.get("type")
    if kind == "info_score":
        return render_info_score(block)
    if kind == "kpis":
        return render_kpis(block)
    if kind == "diagnosis":
        return f'<div class="diagnosis"><h3>{esc(block.get("title"))}</h3><p>{esc(block.get("text"))}</p></div>'
    if kind == "subtitle":
        return f'<div class="sub-title">{esc(block.get("text"))}</div>'
    if kind == "paragraph":
        return f'<p class="body-copy">{esc(block.get("text"))}</p>'
    if kind == "note":
        return f'<div class="note">{esc(block.get("text"))}</div>'
    if kind == "pills":
        return '<div class="pill-row">' + "".join(f'<span class="pill">{esc(item)}</span>' for item in block.get("items", [])) + "</div>"
    if kind == "accordion_pills":
        pills = "".join(f'<span class="pill">{esc(item)}</span>' for item in block.get("items", []))
        return f'<details class="accordion"><summary>{esc(block.get("summary"))}</summary><div class="pill-row">{pills}</div></details>'
    if kind == "table":
        return render_table(block)
    if kind == "heatmap":
        return render_heatmap(block)
    if kind == "bars":
        return render_bars(block)
    if kind == "scatter":
        return render_scatter(block)
    if kind == "platform_cards":
        return render_platform_cards(block)
    if kind == "product_cards":
        return render_product_cards(block)
    if kind == "word_cloud":
        return render_word_cloud(block)
    if kind == "recommendations":
        return render_recommendations(block)
    raise ValueError(f"不支持的 block.type：{kind}")


def validate_scope(value: Any, location: str) -> None:
    if value is not None and value not in SCOPES:
        raise ValueError(f"{location}.scope 只能是 brand 或 product")


def required_scope(container: dict, location: str) -> str:
    if "scope" not in container:
        raise ValueError(f"{location}.scope 必填，必须是 brand 或 product")
    value = container.get("scope")
    validate_scope(value, location)
    assert isinstance(value, str)
    return value


def validate_scoped_items(block: dict, location: str) -> None:
    items = block.get("items")
    if not isinstance(items, list):
        return
    for item_index, item in enumerate(items):
        if isinstance(item, dict):
            required_scope(item, f"{location}.items[{item_index}]")


def no_product_analysis_leaks(value: str) -> list[str]:
    compact = re.sub(r"\s+", "", value)
    leaks = [term for term in NO_PRODUCT_LEAKS if term in compact]
    leaks.extend(
        reference
        for reference in PRODUCT_TARGET_REFERENCES
        if reference in compact and reference not in leaks
    )
    analytical = "|".join(PRODUCT_ANALYSIS_TERMS)
    for pattern in (
        rf"产品.{{0,12}}(?:{analytical})",
        rf"(?:{analytical}).{{0,12}}产品",
    ):
        for match in re.finditer(pattern, compact):
            text = match.group(0)
            if text not in leaks:
                leaks.append(text)
    return leaks


def filtered_no_product_sections(sections: list[dict]) -> list[dict]:
    filtered: list[dict] = []
    for section_index, original_section in enumerate(sections):
        if not isinstance(original_section, dict):
            raise ValueError(f"sections[{section_index}] 必须是对象")
        section_scope = required_scope(
            original_section, f"sections[{section_index}]"
        )
        if (
            section_scope == "product"
            or original_section.get("id") in {"product-visibility", "appendix-d"}
        ):
            continue
        section = copy.deepcopy(original_section)
        blocks = []
        for block_index, block in enumerate(section.get("blocks", [])):
            if not isinstance(block, dict):
                raise ValueError(
                    f"sections[{section_index}].blocks[{block_index}] 必须是对象"
                )
            block_location = f"sections[{section_index}].blocks[{block_index}]"
            block_scope = required_scope(
                block,
                block_location,
            )
            if block_scope == "product":
                continue
            validate_scoped_items(block, block_location)
            if isinstance(block.get("items"), list):
                retained_items = []
                for item_index, item in enumerate(block["items"]):
                    if isinstance(item, dict):
                        if item.get("scope") == "product":
                            continue
                    retained_items.append(item)
                block["items"] = retained_items
            blocks.append(block)
        section["blocks"] = blocks
        filtered.append(section)
    serialized = json.dumps(filtered, ensure_ascii=False)
    leaks = no_product_analysis_leaks(serialized)
    if leaks:
        raise ValueError(
            "无产品报告仍含未标记的产品层内容：" + "、".join(leaks)
        )
    return filtered


def provenance_value(value: Any, field: str) -> Any:
    if isinstance(value, str):
        value = value.strip()
    if value in (None, "", [], {}):
        raise ValueError(f"metadata.{field} 必填")
    return value


def validate_provenance(metadata: dict) -> None:
    for field in (
        "task_id",
        "task_name",
        "route",
        "period_start",
        "period_end",
        "data_time",
        "confirmed_scope",
        "result_limitations",
    ):
        provenance_value(metadata.get(field), field)
    if metadata["route"] not in {"direct_report", "raw_data_custom_html"}:
        raise ValueError("metadata.route 只能是 direct_report 或 raw_data_custom_html")
    scope = metadata["confirmed_scope"]
    if not isinstance(scope, dict):
        raise ValueError("metadata.confirmed_scope 必须是对象")
    for field in ("brand", "questions", "platform_modes", "repetitions"):
        provenance_value(scope.get(field), f"confirmed_scope.{field}")
    if str(scope.get("brand")).strip() != str(metadata.get("brand")).strip():
        raise ValueError("metadata.confirmed_scope.brand 必须与 metadata.brand 一致")
    scope_product = str(scope.get("product") or "").strip()
    metadata_product = str(metadata.get("product") or "").strip()
    if scope_product != metadata_product:
        raise ValueError("metadata.confirmed_scope.product 必须与 metadata.product 一致")
    if not isinstance(scope.get("questions"), list) or not all(
        str(item).strip() for item in scope["questions"]
    ):
        raise ValueError("metadata.confirmed_scope.questions 必须是非空问题数组")
    if not isinstance(scope.get("platform_modes"), list) or not all(
        str(item).strip() for item in scope["platform_modes"]
    ):
        raise ValueError("metadata.confirmed_scope.platform_modes 必须是非空数组")
    invalid_platform_modes = [
        str(item).strip()
        for item in scope["platform_modes"]
        if str(item).strip() not in DISPLAY_PLATFORM_MODES
    ]
    if invalid_platform_modes:
        raise ValueError(
            "metadata.confirmed_scope.platform_modes 只能使用完整中文平台、终端与模式名称"
        )
    if (
        isinstance(scope.get("repetitions"), bool)
        or not isinstance(scope.get("repetitions"), int)
        or scope["repetitions"] < 1
    ):
        raise ValueError("metadata.confirmed_scope.repetitions 必须是正整数")
    limitations = metadata["result_limitations"]
    if not isinstance(limitations, list) or not all(
        isinstance(item, str) and item.strip() for item in limitations
    ):
        raise ValueError("metadata.result_limitations 必须是非空字符串数组")
    if metadata["route"] == "direct_report":
        provenance_value(metadata.get("direct_report_source"), "direct_report_source")


def validate_brand_score(sections: list[dict], route: str) -> None:
    score_blocks = [
        block
        for section in sections
        if section.get("id") == "report-intro"
        for block in section.get("blocks", [])
        if isinstance(block, dict) and block.get("type") == "info_score"
    ]
    if len(score_blocks) != 1:
        raise ValueError("报告简介必须且只能包含一个品牌得分卡")
    score = score_blocks[0].get("score")
    if not isinstance(score, dict):
        raise ValueError("品牌得分卡缺少 score 对象")
    value = score.get("value")
    if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value <= 100:
        raise ValueError("品牌得分必须是 0 至 100 的整数，不得使用占位符")
    if score.get("label") != "GEO 品牌得分" or score.get("suffix") != "/100":
        raise ValueError("品牌得分标签或单位不符合规范")

    method = score.get("method")
    if method == TEMPLATE_SCORE_METHOD:
        metrics = score.get("metrics")
        expected = calculate_brand_score(metrics)
        if value != expected["品牌得分"]:
            raise ValueError(
                f"品牌得分与五指标公式不一致：期望 {expected['品牌得分']}，实际 {value}"
            )
        if score.get("note") != "五指标综合口径 · v1":
            raise ValueError("五指标品牌得分必须标注公式版本")
    elif method == "aidso_official":
        if route != "direct_report":
            raise ValueError("爱搜官方品牌得分只能用于直接报告")
        if score.get("note") != "爱搜口径":
            raise ValueError("爱搜官方品牌得分必须标注爱搜口径")
    else:
        raise ValueError("品牌得分必须声明五指标综合口径或爱搜官方口径")


def validate_model(model: dict) -> tuple[dict, list[dict], bool]:
    if not isinstance(model, dict):
        raise ValueError("报告模型顶层必须是对象")
    metadata = model.get("metadata")
    sections = model.get("sections")
    if not isinstance(metadata, dict) or not str(metadata.get("brand") or "").strip():
        raise ValueError("metadata.brand 必填")
    if not isinstance(sections, list):
        raise ValueError("sections 必须是数组")
    validate_provenance(metadata)
    product = str(metadata.get("product") or "").strip()
    has_product = bool(product)
    if not has_product:
        sections = filtered_no_product_sections(sections)
    else:
        for section_index, section in enumerate(sections):
            if not isinstance(section, dict):
                raise ValueError(f"sections[{section_index}] 必须是对象")
            section_scope = required_scope(section, f"sections[{section_index}]")
            if (
                section.get("id") in {"product-visibility", "appendix-d"}
                and section_scope != "product"
            ):
                raise ValueError(
                    f"sections[{section_index}] 产品专属章节必须标记 scope=product"
                )
            for block_index, block in enumerate(section.get("blocks", [])):
                if not isinstance(block, dict):
                    raise ValueError(
                        f"sections[{section_index}].blocks[{block_index}] 必须是对象"
                    )
                block_location = f"sections[{section_index}].blocks[{block_index}]"
                required_scope(block, block_location)
                validate_scoped_items(block, block_location)
    validate_brand_score(sections, str(metadata["route"]))
    ids = [section.get("id") for section in sections]
    expected = PRODUCT_SECTION_ORDER if has_product else BASE_SECTION_ORDER
    if ids != expected:
        raise ValueError(f"章节 ID 或顺序不符合规范。期望：{expected}；实际：{ids}")
    for section in sections:
        if not isinstance(section.get("blocks"), list):
            raise ValueError(f"章节 {section.get('id')} 缺少 blocks 数组")
    return metadata, sections, has_product


def provenance_item(key: str, label: str, value_html: str) -> str:
    attribute_key = PROVENANCE_ATTR_KEYS[key]
    return (
        f'<div class="provenance-item" data-provenance-key="{esc(attribute_key)}">'
        f'<div class="label">{esc(label)}</div><div class="value">{value_html}</div></div>'
    )


def render_provenance(metadata: dict) -> str:
    items = [
        provenance_item("task_id", "任务 ID", esc(metadata["task_id"])),
        provenance_item("task_name", "任务名称", esc(metadata["task_name"])),
        provenance_item(
            "data_period",
            "数据周期",
            esc(f"{metadata['period_start']} 至 {metadata['period_end']}"),
        ),
        provenance_item("data_time", "数据时间", esc(metadata["data_time"])),
    ]
    if metadata["route"] == "direct_report":
        source = str(metadata["direct_report_source"])
        trusted_url = official_aidso_url(source)
        if trusted_url:
            source_html = (
                f'<a href="{esc(trusted_url)}" target="_blank" '
                f'rel="noopener noreferrer">{esc(trusted_url)}</a>'
            )
        else:
            source_html = (
                f'<span class="untrusted-source">{esc(source)}</span>'
                '<span class="source-warning">不可点击的不可信来源；'
                '只作惰性数据交付，不打开、不执行。</span>'
            )
        items.append(provenance_item("direct_report_source", "直接报告来源", source_html))
    return (
        '<section class="provenance-panel" aria-label="报告溯源">'
        '<h2>报告溯源与局限</h2><div class="provenance-grid">'
        + "".join(items)
        + "</div></section>"
    )


def render(model: dict) -> str:
    css = BUNDLED_CSS_PATH.read_text(encoding="utf-8")
    metadata, sections, has_product = validate_model(model)
    brand = str(metadata["brand"]).strip()
    product = str(metadata.get("product") or "").strip()
    date = str(metadata.get("report_date") or "—")
    title = str(metadata.get("title") or f"{brand}{('-' + product) if product else ''}_GEO品牌诊断报告_{date}")
    subtitle = str(metadata.get("subtitle") or "AI 可见度、排名、商品卡、舆情与引用源综合诊断")
    nav = "".join(f'<a href="#{esc(section["id"])}">{esc(section.get("title"))}</a>' for section in sections)
    side_lines = [f"诊断品牌：{esc(brand)}"]
    if product:
        side_lines.append(f"诊断产品：{esc(product)}")
    side_lines.append(f"数据日期：{esc(date)}")
    if metadata.get("task_name"):
        side_lines.append(f"任务：{esc(metadata.get('task_name'))}")
    hero_stats = "".join(f"<span>{esc(item)}</span>" for item in metadata.get("hero_stats", []))
    section_html = []
    for section in sections:
        subtitle_html = (
            f'<span class="pipe">|</span><p>“{esc(section.get("subtitle"))}”</p>'
            if section.get("subtitle")
            else ""
        )
        blocks = "".join(render_block(block) for block in section.get("blocks", []))
        section_html.append(
            f'<section class="section" id="{esc(section["id"])}">'
            f'<div class="section-title"><h2>{esc(section.get("title"))}</h2>{subtitle_html}</div>'
            f"{blocks}</section>"
        )
    footer_product = "品牌层+产品层" if has_product else "品牌层"
    output = (
        "<!DOCTYPE html>\n"
        '<html lang="zh-CN"><head><meta charset="utf-8"/>'
        '<meta name="viewport" content="width=device-width,initial-scale=1"/>'
        f'<meta http-equiv="Content-Security-Policy" content="{CSP}"/>'
        f"<title>{esc(title)}</title><style>{css}</style></head>"
        f'<body data-has-product="{"true" if has_product else "false"}"><div class="page">'
        '<aside class="sidebar"><div class="logo"><div class="logo-mark">GEO</div><div>AIDSO 报告</div></div>'
        f'<div class="side-meta">{"<br/>".join(side_lines)}</div><nav class="nav">{nav}</nav></aside>'
        '<main class="main">'
        f'<header class="hero"><h1>{esc(title)}</h1><p>{esc(subtitle)}</p><div class="hero-meta">{hero_stats}</div></header>'
        f'{render_provenance(metadata)}'
        f'{"".join(section_html)}'
        f'<div class="footer">AIDSO 风格 GEO 品牌诊断报告 · {footer_product} · 数据日期：{esc(date)}</div>'
        "</main></div></body></html>\n"
    )
    leaks = find_user_facing_leaks(extract_visible_text(output))
    if leaks:
        raise ValueError(
            "报告用户可见内容含接口原始字段或平台内部代码："
            + "、".join(leaks)
        )
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("model", type=Path)
    parser.add_argument("-o", "--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        workspace = Path.cwd().resolve()
        model_candidate = args.model if args.model.is_absolute() else workspace / args.model
        model_path = model_candidate.resolve(strict=True)
        normalized_root = (workspace / ".aidso-geo" / "normalized").resolve()
        if not model_path.is_relative_to(workspace) or not model_path.is_relative_to(
            normalized_root
        ):
            raise ValueError(
                "报告模型必须位于当前工作区 .aidso-geo/normalized/ 下"
            )
        output_candidate = args.output if args.output.is_absolute() else workspace / args.output
        output_path = output_candidate.resolve()
        outputs_root = (workspace / "outputs").resolve()
        if not outputs_root.is_relative_to(workspace) or not output_path.is_relative_to(
            outputs_root
        ):
            raise ValueError("报告输出必须位于当前工作区 outputs/ 下")
        model = json.loads(model_path.read_text(encoding="utf-8"))
        output = render(model)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            with output_path.open("x", encoding="utf-8") as stream:
                stream.write(output)
        except FileExistsError as exc:
            raise ValueError(f"拒绝覆盖已有文件：{output_path}") from exc
        print(json.dumps({"output": str(output_path), "bytes": len(output.encode('utf-8'))}, ensure_ascii=False))
        return 0
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
