#!/usr/bin/env python3
"""Validate structure and safety invariants of a rendered GEO HTML report."""

from __future__ import annotations

import argparse
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from typing import Optional
from urllib.parse import urlsplit

SCRIPT_DIRECTORY = Path(__file__).resolve().parent
if str(SCRIPT_DIRECTORY) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIRECTORY))

from artifact_safety import extract_visible_text, find_user_facing_leaks


BASE_ORDER = [
    "report-intro", "overall", "visibility", "ranking", "products", "sentiment",
    "sources", "recommendations", "appendix-a", "appendix-b", "appendix-c",
]
PRODUCT_ORDER = [
    "report-intro", "overall", "visibility", "product-visibility", "ranking", "products",
    "sentiment", "sources", "recommendations", "appendix-a", "appendix-b", "appendix-c", "appendix-d",
]
FORBIDDEN_TAGS = {"script", "iframe", "object", "embed", "base", "form"}
REQUIRED_PROVENANCE = {
    "task_id",
    "task_name",
    "data_period",
    "data_time",
}
FORBIDDEN_PROVENANCE = {"route", "confirmed_scope", "result_limitations"}
PROVENANCE_LABELS = {
    "task_id": "任务 ID",
    "task_name": "任务名称",
    "route": "报告路径",
    "data_period": "数据周期",
    "data_time": "数据时间",
    "confirmed_scope": "确认输入范围",
    "result_limitations": "结果局限",
    "direct_report_source": "直接报告来源",
}
PROVENANCE_ATTR_TO_KEY = {
    "任务标识": "task_id",
    "任务名称": "task_name",
    "报告方式": "route",
    "数据周期": "data_period",
    "数据时间": "data_time",
    "诊断范围": "confirmed_scope",
    "结果局限": "result_limitations",
    "报告来源": "direct_report_source",
}
EXPECTED_CSP = {
    "default-src": ["'none'"],
    "connect-src": ["'none'"],
    "frame-src": ["'none'"],
    "object-src": ["'none'"],
    "base-uri": ["'none'"],
    "form-action": ["'none'"],
    "style-src": ["'unsafe-inline'"],
    "img-src": ["https:", "data:"],
}
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


def official_aidso_url(value: str) -> bool:
    try:
        parsed = urlsplit(value.strip())
        port = parsed.port
    except ValueError:
        return False
    hostname = (parsed.hostname or "").rstrip(".").lower()
    return (
        parsed.scheme == "https"
        and (hostname == "aidso.com" or hostname.endswith(".aidso.com"))
        and parsed.username is None
        and parsed.password is None
        and port in {None, 443}
    )


class ReportParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.section_ids: list[str] = []
        self.nav_hrefs: list[str] = []
        self.has_product: Optional[str] = None
        self.lang: Optional[str] = None
        self.has_viewport = False
        self.has_charset = False
        self.title_depth = 0
        self.title_parts: list[str] = []
        self.forbidden_tags: list[str] = []
        self.event_handlers: list[str] = []
        self.external_stylesheets = 0
        self.meta_refreshes = 0
        self.csp_values: list[str] = []
        self.style_depth = 0
        self.style_count = 0
        self.style_end_count = 0
        self.style_parts: list[str] = []
        self.inline_styles: list[str] = []
        self.duplicate_attributes: list[str] = []
        self.element_depth = 0
        self.element_stack: list[tuple[str, frozenset[str]]] = []
        self.mismatched_tags: list[str] = []
        self.main_child_roles: list[str] = []
        self.provenance_panel_count = 0
        self.invalid_provenance_parent = 0
        self.hidden_depths: list[int] = []
        self.inline_style_depths: list[int] = []
        self.invisible_container_depths: list[int] = []
        self.hidden_provenance_panels = 0
        self.provenance_panel_depths: list[int] = []
        self.provenance_records: list[dict[str, object]] = []
        self.current_provenance: Optional[dict[str, object]] = None
        self.provenance_item_depth: Optional[int] = None
        self.provenance_capture: Optional[str] = None
        self.provenance_capture_depth: Optional[int] = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, Optional[str]]]) -> None:
        tag = tag.lower()
        self.element_depth += 1
        values: dict[str, Optional[str]] = {}
        for name, value in attrs:
            normalized_name = str(name).lower()
            if normalized_name in values:
                self.duplicate_attributes.append(f"{tag}.{normalized_name}")
                continue
            values[normalized_name] = value
        if tag in FORBIDDEN_TAGS:
            self.forbidden_tags.append(tag)
        for name in values:
            if name.startswith("on"):
                self.event_handlers.append(name)
        if values.get("style"):
            self.inline_styles.append(str(values["style"]))
            self.inline_style_depths.append(self.element_depth)

        inline_style = re.sub(r"\s+", "", str(values.get("style") or "")).lower()
        hidden_self = (
            "hidden" in values
            or "popover" in values
            or str(values.get("aria-hidden") or "").strip().lower() == "true"
            or "display:none" in inline_style
            or "visibility:hidden" in inline_style
            or re.search(r"(?:^|;)opacity:0(?:[;!]|$)", inline_style) is not None
        )
        if hidden_self:
            self.hidden_depths.append(self.element_depth)
        invisible_container = tag == "template" or (
            tag in {"details", "dialog"} and "open" not in values
        )
        if invisible_container:
            self.invisible_container_depths.append(self.element_depth)

        classes = set(str(values.get("class") or "").split())
        parent = self.element_stack[-1] if self.element_stack else None
        if parent and parent[0] == "main" and "main" in parent[1]:
            if tag == "header" and "hero" in classes:
                role = "hero"
            elif tag == "section" and "provenance-panel" in classes:
                role = "provenance"
            elif tag == "section" and values.get("id"):
                role = f"section:{values['id']}"
            elif tag == "div" and "footer" in classes:
                role = "footer"
            else:
                role = f"other:{tag}"
            self.main_child_roles.append(role)
        if tag == "section" and "provenance-panel" in classes:
            self.provenance_panel_count += 1
            self.provenance_panel_depths.append(self.element_depth)
            if not parent or parent[0] != "main" or "main" not in parent[1]:
                self.invalid_provenance_parent += 1
            if (
                self.hidden_depths
                or self.inline_style_depths
                or self.invisible_container_depths
            ):
                self.hidden_provenance_panels += 1
        if self.provenance_panel_depths:
            if tag == "div" and "provenance-item" in classes:
                record: dict[str, object] = {
                    "key": str(values.get("data-provenance-key") or "").lower(),
                    "label_parts": [],
                    "value_parts": [],
                    "links": [],
                }
                self.provenance_records.append(record)
                self.current_provenance = record
                self.provenance_item_depth = self.element_depth
            elif self.current_provenance is not None and tag == "div":
                if "label" in classes:
                    self.provenance_capture = "label_parts"
                    self.provenance_capture_depth = self.element_depth
                elif "value" in classes:
                    self.provenance_capture = "value_parts"
                    self.provenance_capture_depth = self.element_depth
            if self.current_provenance is not None and tag == "a":
                href = values.get("href")
                if href is not None:
                    links = self.current_provenance["links"]
                    assert isinstance(links, list)
                    links.append(str(href))

        if tag == "html":
            self.lang = values.get("lang")
        elif tag == "body":
            self.has_product = values.get("data-has-product")
        elif tag == "section" and values.get("id"):
            self.section_ids.append(str(values["id"]))
        elif tag == "a" and str(values.get("href") or "").startswith("#"):
            self.nav_hrefs.append(str(values["href"])[1:])
        elif tag == "meta":
            if str(values.get("name") or "").lower() == "viewport":
                self.has_viewport = True
            if values.get("charset"):
                self.has_charset = True
            http_equiv = str(values.get("http-equiv") or "").strip().lower()
            if http_equiv == "refresh":
                self.meta_refreshes += 1
            elif http_equiv == "content-security-policy":
                self.csp_values.append(str(values.get("content") or ""))
        elif tag == "title":
            self.title_depth += 1
        elif tag == "style":
            self.style_count += 1
            self.style_depth += 1
        elif tag == "link":
            rel_values = str(values.get("rel") or "").lower().split()
            if "stylesheet" in rel_values:
                self.external_stylesheets += 1
        self.element_stack.append((tag, frozenset(classes)))

    def handle_startendtag(
        self, tag: str, attrs: list[tuple[str, Optional[str]]]
    ) -> None:
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "title":
            self.title_depth = max(0, self.title_depth - 1)
        elif tag == "style":
            self.style_end_count += 1
            self.style_depth = max(0, self.style_depth - 1)
        if self.provenance_capture_depth == self.element_depth:
            self.provenance_capture = None
            self.provenance_capture_depth = None
        if self.provenance_item_depth == self.element_depth:
            self.current_provenance = None
            self.provenance_item_depth = None
        if (
            self.provenance_panel_depths
            and self.provenance_panel_depths[-1] == self.element_depth
        ):
            self.provenance_panel_depths.pop()
        if self.hidden_depths and self.hidden_depths[-1] == self.element_depth:
            self.hidden_depths.pop()
        if (
            self.inline_style_depths
            and self.inline_style_depths[-1] == self.element_depth
        ):
            self.inline_style_depths.pop()
        if (
            self.invisible_container_depths
            and self.invisible_container_depths[-1] == self.element_depth
        ):
            self.invisible_container_depths.pop()
        if not self.element_stack or self.element_stack[-1][0] != tag:
            self.mismatched_tags.append(tag)
        else:
            self.element_stack.pop()
        self.element_depth = max(0, self.element_depth - 1)

    def handle_data(self, data: str) -> None:
        if self.title_depth:
            self.title_parts.append(data)
        if self.style_depth:
            self.style_parts.append(data)
        if self.current_provenance is not None and self.provenance_capture:
            parts = self.current_provenance[self.provenance_capture]
            assert isinstance(parts, list)
            parts.append(data)


def parse_csp(value: str) -> dict[str, list[str]]:
    directives: dict[str, list[str]] = {}
    for raw_directive in value.split(";"):
        parts = raw_directive.strip().split()
        if not parts:
            continue
        name = parts[0].lower()
        if name in directives:
            raise ValueError(f"重复 CSP 指令：{name}")
        directives[name] = parts[1:]
    return directives


def csp_errors(values: list[str]) -> list[str]:
    if len(values) != 1:
        return ["必须且只能有一个 Content-Security-Policy meta"]
    try:
        directives = parse_csp(values[0])
    except ValueError as exc:
        return [str(exc)]
    errors = []
    unexpected = sorted(set(directives) - set(EXPECTED_CSP))
    missing = sorted(set(EXPECTED_CSP) - set(directives))
    if unexpected:
        errors.append("CSP 包含未授权指令：" + "、".join(unexpected))
    if missing:
        errors.append("CSP 缺少必需指令：" + "、".join(missing))
    for name, expected_sources in EXPECTED_CSP.items():
        if directives.get(name) != expected_sources:
            errors.append(
                f"CSP {name} 必须精确为：{' '.join(expected_sources)}"
            )
    return errors


def visible_provenance(
    parsed: ReportParser,
) -> tuple[
    dict[str, str],
    dict[str, str],
    dict[str, list[str]],
    set[str],
]:
    values: dict[str, str] = {}
    labels: dict[str, str] = {}
    links: dict[str, list[str]] = {}
    duplicate_keys: set[str] = set()
    for record in parsed.provenance_records:
        attribute_key = str(record.get("key") or "")
        key = PROVENANCE_ATTR_TO_KEY.get(attribute_key, attribute_key)
        if key in values:
            duplicate_keys.add(key)
            continue
        label_parts = record.get("label_parts")
        value_parts = record.get("value_parts")
        record_links = record.get("links")
        labels[key] = "".join(label_parts if isinstance(label_parts, list) else []).strip()
        values[key] = "".join(value_parts if isinstance(value_parts, list) else []).strip()
        links[key] = list(record_links) if isinstance(record_links, list) else []
    return values, labels, links, duplicate_keys


def decode_css_escapes(value: str) -> str:
    def replace(match: re.Match[str]) -> str:
        hexadecimal = match.group(1)
        if hexadecimal:
            codepoint = int(hexadecimal, 16)
            if codepoint == 0 or codepoint > 0x10FFFF:
                return "\ufffd"
            return chr(codepoint)
        escaped = match.group(2)
        return "" if escaped in {"\n", "\r", "\f"} else escaped

    return re.sub(
        r"\\([0-9a-fA-F]{1,6})(?:\r\n|[ \t\r\n\f])?|\\(.)",
        replace,
        value,
        flags=re.DOTALL,
    )


def remote_css_url(css: str) -> bool:
    normalized = re.sub(r"/\*.*?\*/", "", css, flags=re.DOTALL)
    normalized = decode_css_escapes(normalized)
    if re.search(r"(?:-webkit-)?image-set\s*\(", normalized, flags=re.I):
        return True
    for match in re.finditer(r"url\s*\((.*?)\)", normalized, flags=re.I | re.S):
        target = match.group(1).strip().strip("'\"").strip()
        if not target or target.startswith("#"):
            continue
        if target.startswith("//") or re.match(
            r"[a-z][a-z0-9+.-]*:", target, flags=re.IGNORECASE
        ):
            return True
    return False


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


def validate_path(path: Path) -> Path:
    workspace = Path.cwd().resolve()
    candidate = path if path.is_absolute() else workspace / path
    try:
        resolved = candidate.resolve(strict=True)
    except OSError as exc:
        raise ValueError(f"报告 HTML 无法解析：{exc}") from exc
    outputs_root = (workspace / "outputs").resolve()
    if (
        not outputs_root.is_relative_to(workspace)
        or not resolved.is_relative_to(outputs_root)
    ):
        raise ValueError("报告 HTML 必须位于当前工作区 outputs/ 下")
    return resolved


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html", type=Path)
    args = parser.parse_args()
    try:
        report_path = validate_path(args.html)
        text = report_path.read_text(encoding="utf-8")
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    errors: list[str] = []
    warnings: list[str] = []
    if not text.lstrip().lower().startswith("<!doctype html>"):
        errors.append("缺少 HTML5 doctype")
    if len(text.encode("utf-8")) < 5000:
        warnings.append("报告小于 5 KB，请确认不是空壳")

    parsed = ReportParser()
    try:
        parsed.feed(text)
        parsed.close()
    except Exception as exc:
        errors.append(f"HTML 解析失败：{exc}")

    if parsed.lang != "zh-CN":
        errors.append("html.lang 必须是 zh-CN")
    if not parsed.has_viewport:
        errors.append("缺少 viewport meta")
    if not parsed.has_charset:
        errors.append("缺少 charset meta")
    if not "".join(parsed.title_parts).strip():
        errors.append("缺少 title")
    if parsed.forbidden_tags:
        errors.append("报告不得包含主动标签：" + "、".join(sorted(set(parsed.forbidden_tags))))
    if parsed.event_handlers:
        errors.append("报告不得包含事件处理属性：" + "、".join(sorted(set(parsed.event_handlers))))
    if parsed.duplicate_attributes:
        errors.append(
            "报告不得包含重复属性："
            + "、".join(sorted(set(parsed.duplicate_attributes)))
        )
    if parsed.mismatched_tags or parsed.element_stack:
        errors.append("HTML 元素嵌套不完整或结束标签不匹配")
    if parsed.meta_refreshes:
        errors.append("报告不得包含 meta refresh")
    if parsed.external_stylesheets:
        errors.append("报告不得依赖外部样式表")
    if parsed.style_count != 1 or parsed.style_end_count != 1:
        errors.append("报告必须且只能包含一个完整的内联 style")
    if len(re.findall(r"</style\s*>", text, flags=re.IGNORECASE)) != 1:
        errors.append("检测到 style 终止注入或样式结构异常")
    css = "".join(parsed.style_parts)
    normalized_css = decode_css_escapes(
        re.sub(r"/\*.*?\*/", "", css, flags=re.DOTALL)
    )
    if re.search(r"@\s*import\b", normalized_css, flags=re.IGNORECASE):
        errors.append("内联 CSS 不得包含 @import")
    if remote_css_url(css) or any(remote_css_url(value) for value in parsed.inline_styles):
        errors.append("CSS url() 不得指向远程资源")
    try:
        bundled_css = (
            Path(__file__).resolve().parent.parent / "assets" / "report.css"
        ).read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(f"无法读取打包 CSS：{exc}")
    else:
        if css != bundled_css:
            errors.append("报告内联样式必须与打包的 assets/report.css 完全一致")
    errors.extend(csp_errors(parsed.csp_values))

    has_product = parsed.has_product == "true"
    if parsed.has_product not in {"true", "false"}:
        errors.append("body 缺少有效 data-has-product")
    expected = PRODUCT_ORDER if has_product else BASE_ORDER
    if parsed.section_ids != expected:
        errors.append(f"章节顺序错误：{parsed.section_ids}")
    if parsed.nav_hrefs != expected:
        errors.append(f"侧栏导航顺序或目标错误：{parsed.nav_hrefs}")
    expected_main_children = ["hero", "provenance"] + [
        f"section:{section_id}" for section_id in expected
    ] + ["footer"]
    if parsed.main_child_roles != expected_main_children:
        errors.append("main 顶层结构错误：溯源面板必须紧邻 Hero 且位于正文前")
    if not has_product:
        for term in no_product_analysis_leaks(text):
            errors.append(f"无产品报告泄漏产品层内容：{term}")

    if parsed.provenance_panel_count != 1:
        errors.append("必须且只能有一个可见的报告溯源面板")
    if parsed.invalid_provenance_parent:
        errors.append("报告溯源面板必须是 main.main 的直接子节点")
    if parsed.hidden_provenance_panels:
        errors.append(
            "报告溯源面板及其祖先不得使用 hidden、popover、隐藏容器或任何内联样式"
        )
    provenance, provenance_labels, provenance_links, duplicate_provenance = (
        visible_provenance(parsed)
    )
    if duplicate_provenance:
        errors.append(
            "溯源字段不得重复：" + "、".join(sorted(duplicate_provenance))
        )
    forbidden_provenance = sorted(FORBIDDEN_PROVENANCE & set(provenance))
    if forbidden_provenance:
        errors.append(
            "报告溯源面板不得包含："
            + "、".join(PROVENANCE_LABELS[key] for key in forbidden_provenance)
        )
    missing_keys = sorted(REQUIRED_PROVENANCE - set(provenance))
    if missing_keys:
        errors.append("缺少溯源字段：" + "、".join(missing_keys))
    empty_keys = sorted(key for key in REQUIRED_PROVENANCE if not provenance.get(key))
    if empty_keys:
        errors.append("溯源字段不得为空：" + "、".join(empty_keys))
    invalid_labels = sorted(
        key
        for key in REQUIRED_PROVENANCE
        if provenance_labels.get(key) != PROVENANCE_LABELS[key]
    )
    if invalid_labels:
        errors.append("溯源标签缺失或不匹配：" + "、".join(invalid_labels))
    if "direct_report_source" in provenance:
        source_value = provenance.get("direct_report_source", "")
        if not source_value:
            errors.append("爱搜直接生成的诊断报告缺少来源")
        if provenance_labels.get("direct_report_source") != PROVENANCE_LABELS["direct_report_source"]:
            errors.append("爱搜直接生成的诊断报告缺少来源标签")
        source_links = provenance_links.get("direct_report_source", [])
        if source_links and (
            len(source_links) != 1 or not official_aidso_url(source_links[0])
        ):
            errors.append("直接报告必须且只能链接一个官方 HTTPS AIDSO 来源")
        if not source_links and "不可点击的不可信来源" not in source_value:
            errors.append("非官方直接报告来源必须以纯文本警示")

    score_values = re.findall(
        r'<div class="score">\s*([0-9]{1,3})\s*<small>/100</small></div>',
        text,
    )
    if len(score_values) != 1:
        errors.append("报告必须且只能显示一个 0 至 100 的整数品牌得分")
    elif not 0 <= int(score_values[0]) <= 100:
        errors.append("品牌得分必须位于 0 至 100")
    score_notes = re.findall(r'<div class="score-note">([^<]*)</div>', text)
    if len(score_notes) != 1 or score_notes[0] not in {
        "五指标综合口径 · v1",
        "爱搜口径",
    }:
        errors.append("品牌得分必须标注五指标综合口径版本或爱搜口径")
    if "无已审计归一化公式" in extract_visible_text(text):
        errors.append("正式报告不得使用无归一化公式的品牌得分占位说明")

    for leak in find_user_facing_leaks(extract_visible_text(text)):
        errors.append(f"报告用户可见内容含接口原始字段或平台内部代码：{leak}")

    forbidden_patterns = {
        "TODO": r"\bTODO\b",
        "模板占位符": r"\{\{[^}]+\}\}",
        "NaN": r"\bNaN\b",
        "Infinity": r"\bInfinity\b",
        "undefined": r"\bundefined\b",
    }
    for label, pattern in forbidden_patterns.items():
        if re.search(pattern, text):
            errors.append(f"发现禁止内容：{label}")

    result = {
        "file": str(report_path),
        "valid": not errors,
        "has_product": has_product,
        "sections": parsed.section_ids,
        "errors": errors,
        "warnings": warnings,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 2


if __name__ == "__main__":
    raise SystemExit(main())
