#!/usr/bin/env python3
"""检查 HTML 产物是否符合微信公众号编辑器的技术约束。

微信公众号编辑器在粘贴富文本时会过滤大量 HTML 元素和 CSS 属性，
导致样式丢失。本工具将这些已知的平台约束固化为自动化检查，
在交付前确定性地拦截问题。

约束来源：微信公众号编辑器的实际粘贴行为（经验性测试，非官方文档）。
官方未公开完整的过滤规则列表，以下规则基于反复测试总结，
可能随编辑器版本更新而变化。

用法:
    validate_output.py <file.html>
    validate_output.py --stdin < file.html

退出码: 0 = 通过, 1 = 存在必须修复的问题
"""

import argparse
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "validation_config.json"


def _load_config():
    """从 validation_config.json 加载规则配置。"""
    try:
        with open(CONFIG_PATH, encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None


_CONFIG = _load_config()

if _CONFIG:
    LAST_TESTED = _CONFIG["last_tested"]
    FILTERED_TAGS = _CONFIG["filtered_tags"]
    STRIPPED_ATTRS = _CONFIG["stripped_attrs"]
    UNSUPPORTED_CSS = [(p, r) for p, r in _CONFIG["unsupported_css"]]
    MAX_ANCHORS = _CONFIG.get("content_rules", {}).get("max_anchors", 5)
    UNDERLINE_PARA_THRESHOLD = _CONFIG.get("content_rules", {}).get("min_underlines_per_para_threshold", 5)
else:
    LAST_TESTED = "2026-07"
    FILTERED_TAGS = {
        "style": "编辑器会移除 <style>，所有样式必须写在 style 属性里",
        "script": "编辑器会移除 <script>",
        "link": "编辑器会移除 <link>（外部 CSS / 字体无法加载）",
        "meta": "编辑器会移除 <meta>",
        "iframe": "编辑器不支持 <iframe>",
        "form": "编辑器不支持 <form>",
        "input": "编辑器不支持 <input>",
        "div": "编辑器会改写 <div>，应改用 <section>",
    }
    STRIPPED_ATTRS = {
        "class": "编辑器会移除 class 属性",
        "id": "编辑器会移除 id 属性",
    }
    UNSUPPORTED_CSS = [
        (r"position\s*:\s*(?:fixed|absolute|sticky)", "不支持 position 定位"),
        (r"float\s*:", "不支持 float"),
        (r"@media", "不支持 @media 查询"),
        (r"@keyframes", "不支持 @keyframes 动画"),
        (r"@import", "不支持 @import"),
        (r"display\s*:\s*grid", "不支持 display:grid，应改用 flex"),
        (r"var\s*\(\s*--", "不支持 CSS 自定义属性（变量）"),
        (r"url\s*\(\s*['\"]?https?://[^)]*\.(?:woff2?|ttf|otf)", "不支持外部字体文件引用"),
    ]
    MAX_ANCHORS = 5
    UNDERLINE_PARA_THRESHOLD = 5

# 危险的事件处理器属性（XSS 风险）
EVENT_HANDLER_PATTERN = re.compile(r"\son\w+\s*=", re.I)

# 中文 Unicode 范围
CJK_RANGE = re.compile(r"[\u4e00-\u9fff\u3400-\u4dbf]")

# 中文字符后紧跟半角标点 → 应改为全角
NEEDS_FULLWIDTH = re.compile(r"[\u4e00-\u9fff\u3400-\u4dbf][,;!?]")

# 西文直引号出现在中文上下文中
STRAIGHT_QUOTE = re.compile(r"[\"']")

# 等宽字体或 pre-wrap 特征 → 判定为代码区域
CODE_AREA = re.compile(r"monospace|courier|consolas|sf.?mono|pre-wrap|white-space\s*:\s*pre", re.I)

# 这些标签内部的内容不参与公众号正文粘贴
NON_BODY_TAGS = {"head", "title", "style", "script", "meta", "link"}


class WeChatHTMLAnalyzer(HTMLParser):
    """解析 HTML，记录每个文本节点的上下文信息。

    与简单的深度计数不同，这里维护一个显式的「祖先链」，
    通过查询祖先链判断文本节点是否处于 leaf span 或代码区域内。
    """

    def __init__(self):
        super().__init__(convert_charrefs=True)
        # 祖先链：记录从根到当前节点的路径
        self._ancestors: list[tuple[str, bool, bool]] = []
        # 结果收集
        self.total_leaf_spans = 0
        self.text_outside_leaf: list[tuple[str, str]] = []
        self.punctuation_issues: list[str] = []

    def handle_starttag(self, tag, attrs):
        attr_map = dict(attrs)
        wrapped = tag == "span" and "leaf" in attr_map
        styled = attr_map.get("style", "") or ""
        is_code_context = bool(CODE_AREA.search(styled))

        if wrapped:
            self.total_leaf_spans += 1

        self._ancestors.append((tag, wrapped, is_code_context))

    def handle_endtag(self, tag):
        # 从栈顶向下找到匹配的标签，截断
        for i in range(len(self._ancestors) - 1, -1, -1):
            if self._ancestors[i][0] == tag:
                del self._ancestors[i:]
                break

    def handle_data(self, raw):
        content = raw.strip()
        if not content or not CJK_RANGE.search(content):
            return

        # 跳过非正文区域
        if any(a[0] in NON_BODY_TAGS for a in self._ancestors):
            return

        in_leaf = any(a[1] for a in self._ancestors)
        in_code = any(a[2] for a in self._ancestors)

        if not in_leaf:
            nearest = self._ancestors[-1][0] if self._ancestors else "(root)"
            self.text_outside_leaf.append((content[:40], nearest))

        if not in_code:
            if NEEDS_FULLWIDTH.search(content) or STRAIGHT_QUOTE.search(content):
                self.punctuation_issues.append(content[:40])


def check_filtered_tags(html: str) -> list[str]:
    """检测会被编辑器过滤的 HTML 元素。"""
    problems = []
    for tag, reason in FILTERED_TAGS.items():
        pattern = re.compile(rf"<{tag}[\s/>]", re.I)
        hits = len(pattern.findall(html))
        if hits:
            problems.append(f"{reason}（{hits} 处）")
    return problems


def check_stripped_attrs(html: str) -> list[str]:
    """检测会被编辑器移除的属性。"""
    problems = []
    for attr, reason in STRIPPED_ATTRS.items():
        pattern = re.compile(rf"\s{attr}\s*=", re.I)
        hits = len(pattern.findall(html))
        if hits:
            problems.append(f"{reason}（{hits} 处）")
    return problems


def check_event_handlers(html: str) -> list[str]:
    """检测危险的 HTML 事件处理器属性（XSS 风险）。"""
    problems = []
    hits = len(EVENT_HANDLER_PATTERN.findall(html))
    if hits:
        problems.append(f"检测到事件处理器属性（onerror/onload 等，{hits} 处），存在 XSS 风险")
    return problems


def check_unsupported_css(html: str) -> list[str]:
    """检测不支持的 CSS 特性。"""
    problems = []
    for pattern, reason in UNSUPPORTED_CSS:
        rx = re.compile(pattern, re.I)
        hits = len(rx.findall(html))
        if hits:
            problems.append(f"{reason}（{hits} 处）")
    return problems


def _is_neutral_color(hex_str):
    """判断 hex 色值是否为中性色（黑/白/灰），用于排除非锚点的结构性加粗。

    中性色 = 饱和度低（s<0.15）或亮度极端（<0.12 或 >0.92）。
    这些是标题色/正文色/白色文字，不是主题主色锚点。
    """
    h = hex_str.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    try:
        r, g, b = int(h[0:2], 16) / 255, int(h[2:4], 16) / 255, int(h[4:6], 16) / 255
    except (ValueError, IndexError):
        return False
    cmax, cmin = max(r, g, b), min(r, g, b)
    l = (cmax + cmin) / 2
    if cmax == cmin:
        return True  # 纯灰/黑/白
    s = (cmax - cmin) / (2 - cmax - cmin) if l > 0.5 else (cmax - cmin) / (cmax + cmin)
    return s < 0.15 or l < 0.12 or l > 0.92


def check_content_quality(html: str) -> list[str]:
    """检查内容智能处理规则的量化指标（warnings 级别）。"""
    warnings = []

    # 锚点层：主色加粗 span 的数量（全文 ≤5 处）
    # 先找所有 font-weight:bold 的 span，再排除中性色（标题/正文/白色）加粗
    bold_span_pattern = re.compile(
        r'<span[^>]*style="([^"]*font-weight:bold[^"]*)"[^>]*>', re.I
    )
    color_in_style = re.compile(r'color:\s*(#[0-9a-fA-F]{3,6})', re.I)
    anchor_count = 0
    for match in bold_span_pattern.finditer(html):
        style = match.group(1)
        color_match = color_in_style.search(style)
        if color_match and not _is_neutral_color(color_match.group(1)):
            anchor_count += 1
        elif not color_match:
            # 加粗但无 color 属性 → 继承正文色，不是主色锚点
            pass

    if anchor_count > MAX_ANCHORS:
        warnings.append(
            f"锚点层（主色加粗）共 {anchor_count} 处，超过 ≤{MAX_ANCHORS} 处上限，"
            f"过度强调等于没有重点"
        )

    # 下划线标记：统计 border-bottom 的 span（关键词下划线）
    underline_pattern = re.compile(
        r'<span[^>]*style="[^"]*border-bottom[^"]*"[^>]*>', re.I
    )
    underline_count = len(underline_pattern.findall(html))

    # 正文段落数量（粗略统计 <p> 标签）
    para_count = len(re.findall(r'<p\s', html, re.I))

    if para_count > UNDERLINE_PARA_THRESHOLD and underline_count == 0:
        warnings.append(
            f"共 {para_count} 个段落但未检测到任何关键词下划线，"
            f"应每段标记 1-3 个核心短语"
        )

    return warnings


def analyze(html: str) -> dict:
    """对 HTML 执行全套检查，返回结构化报告。"""
    errors = []
    warnings = []

    # 第一阶段：正则扫描禁止的模式
    errors.extend(check_filtered_tags(html))
    errors.extend(check_stripped_attrs(html))
    errors.extend(check_event_handlers(html))
    errors.extend(check_unsupported_css(html))

    # 第二阶段：解析 DOM 结构，检查文本包裹和标点
    analyzer = WeChatHTMLAnalyzer()
    try:
        analyzer.feed(html)
    except Exception as exc:
        warnings.append(f"HTML 解析过程中断: {exc}")

    has_chinese = bool(CJK_RANGE.search(html))

    if has_chinese and analyzer.total_leaf_spans == 0:
        errors.append(
            "全文未检测到任何 <span leaf=\"\"> 包裹，"
            "粘贴后样式将大面积丢失"
        )
    elif analyzer.text_outside_leaf:
        samples = "、".join(
            f"[{text[:20]}…] in <{tag}>" for text, tag in analyzer.text_outside_leaf[:5]
        )
        warnings.append(
            f"{len(analyzer.text_outside_leaf)} 处中文文本缺少 <span leaf> 包裹: {samples}"
        )

    if analyzer.punctuation_issues:
        samples = "、".join(f"[{s[:20]}…]" for s in analyzer.punctuation_issues[:5])
        warnings.append(
            f"{len(analyzer.punctuation_issues)} 处可能需要全角标点（代码区域除外）: {samples}"
        )

    # 内容智能处理检查
    warnings.extend(check_content_quality(html))

    return {
        "errors": errors,
        "warnings": warnings,
        "leaf_count": analyzer.total_leaf_spans,
    }


def format_report(report: dict, source: str) -> str:
    """将检查结果格式化为可读报告。"""
    lines = []
    lines.append(f"检查目标: {source}")
    lines.append(f"规则验证时间: {LAST_TESTED}")
    lines.append(f"<span leaf> 包裹计数: {report['leaf_count']}")
    lines.append("")

    if report["errors"]:
        lines.append(f"[严重] {len(report['errors'])} 个问题必须修复:")
        for item in report["errors"]:
            lines.append(f"  - {item}")
        lines.append("")

    if report["warnings"]:
        lines.append(f"[提醒] {len(report['warnings'])} 项建议检查:")
        for item in report["warnings"]:
            lines.append(f"  - {item}")
        lines.append("")

    if not report["errors"] and not report["warnings"]:
        lines.append("全部通过，可安全粘贴到公众号编辑器")
    elif not report["errors"]:
        lines.append("无严重问题，可粘贴（建议处理提醒项）")

    lines.append("")
    lines.append("注意: 以上规则基于经验性测试，微信公众号官方未公开完整过滤规则。")
    lines.append("规则可能随编辑器版本更新而变化。")

    return "\n".join(lines)


def check_ops_quality(html: str) -> list[str]:
    """运营维度检查：标题长度、段落长度、图片数、阅读时长（warnings 级别）。"""
    warnings = []

    # 提取纯文本（去标签）
    text_only = re.sub(r"<[^>]+>", "", html)
    cjk_chars = len(CJK_RANGE.findall(text_only))

    # 标题长度：找最大的 font-size 文本作为标题粗略判断
    title_pattern = re.compile(r'font-size:\s*(\d+)px', re.I)
    sizes = [int(m) for m in title_pattern.findall(html)]
    max_size = max(sizes) if sizes else 0
    if max_size >= 22:
        title_spans = re.findall(
            rf'font-size:\s*{max_size}px[^"]*"[^>]*><span[^>]*>([^<]+)</span>',
            html, re.I
        )
        for title_text in title_spans[:1]:
            title_len = len(title_text)
            if title_len > 22:
                warnings.append(
                    f"标题「{title_text[:15]}…」共 {title_len} 字，"
                    f"建议 ≤22 字以保证手机端完整显示"
                )

    # 图片数量
    img_count = len(re.findall(r'<img\s', html, re.I))
    if img_count == 0:
        warnings.append("未检测到图片，公众号文章建议配图提升阅读体验")

    # 阅读时长估算（按 400 字/分钟）
    if cjk_chars > 0:
        read_minutes = max(1, round(cjk_chars / 400))
        if cjk_chars < 200:
            warnings.append(f"全文仅约 {cjk_chars} 字，内容可能过于单薄")
        elif cjk_chars > 3000:
            warnings.append(
                f"全文约 {cjk_chars} 字（预计 {read_minutes} 分钟阅读），"
                f"较长文章建议添加章节导读"
            )

    return warnings


def main():
    parser = argparse.ArgumentParser(
        description="检查 HTML 是否符合微信公众号编辑器技术约束"
    )
    parser.add_argument("file", nargs="?", help="待检查的 HTML 文件")
    parser.add_argument("--stdin", action="store_true", help="从标准输入读取")
    parser.add_argument("--ops", action="store_true",
                        help="额外执行运营维度检查（标题长度/图片数/阅读时长）")
    args = parser.parse_args()

    if args.stdin or not args.file:
        html_content = sys.stdin.read()
        source_name = "<stdin>"
    else:
        with open(args.file, encoding="utf-8", errors="replace") as f:
            html_content = f.read()
        source_name = args.file

    report = analyze(html_content)
    if args.ops:
        report["warnings"].extend(check_ops_quality(html_content))
    print(format_report(report, source_name))
    sys.exit(1 if report["errors"] else 0)


if __name__ == "__main__":
    main()
