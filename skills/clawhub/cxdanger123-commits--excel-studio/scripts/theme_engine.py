#!/usr/bin/env python3
"""excel-studio 主题引擎。

把统一的设计令牌一次性应用到 openpyxl 工作簿：标题区、表头、数据区、
合计行、列宽、数字格式、冻结窗格、筛选、打印设置与图表配色。

作为库使用（推荐，在 build.py 末尾调用）::

    import sys
    sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
    from theme_engine import apply_theme

    apply_theme(wb, theme="business")
    wb.save("out.xlsx")

作为命令行使用::

    python theme_engine.py --list-themes
    python theme_engine.py --show business

设计令牌的取值口径见 references/design_system.md，本文件是它的唯一实现。
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from dataclasses import dataclass, field
from datetime import date, datetime, time
from typing import Any, Iterable, Sequence

try:
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter
except ImportError:  # pragma: no cover
    sys.exit("缺少 openpyxl，请先安装：python -m pip install openpyxl")

FONT_FAMILY = "Microsoft YaHei"
FONT_FALLBACK = "微软雅黑"

# 字号梯度
SIZE_TITLE = 16
SIZE_SUBTITLE = 10
SIZE_HEADER = 11
SIZE_BODY = 10
SIZE_NOTE = 9

# 行高梯度
HEIGHT_TITLE = 34
HEIGHT_SUBTITLE = 20
HEIGHT_HEADER = 30
HEIGHT_BODY = 22
HEIGHT_TOTAL = 24

# 列宽边界（Excel 字符宽）
WIDTH_MIN = 8.0
WIDTH_MAX = 42.0
WIDTH_WRAP = 34.0


# --------------------------------------------------------------------------
# 颜色
# --------------------------------------------------------------------------
def xl(css_hex: str) -> str:
    """把 ``#RRGGBB`` 转成 openpyxl 需要的 ARGB。"""
    value = str(css_hex).lstrip("#").upper()
    if len(value) != 6 or any(c not in "0123456789ABCDEF" for c in value):
        raise ValueError(f"期望 #RRGGBB，收到：{css_hex!r}")
    return "FF" + value


def chart_rgb(css_hex: str) -> str:
    """图表 API 需要不带 alpha 的六位 RGB。"""
    return str(css_hex).lstrip("#").upper()


@dataclass(frozen=True)
class Theme:
    key: str
    label: str
    note: str
    accent: str
    accent_light: str
    accent_text: str
    surface: str
    band: str
    grid: str
    text: str
    muted: str
    rise: str
    fall: str
    warn: str
    info: str
    series: tuple[str, ...]


THEMES: dict[str, Theme] = {
    "business": Theme(
        key="business",
        label="商务蓝",
        note="默认主题。适合对外汇报、管理层周报、财务分析。",
        accent="#1F4E79",
        accent_light="#2E75B6",
        accent_text="#FFFFFF",
        surface="#EBF2F9",
        band="#F5F9FC",
        grid="#D8E2EC",
        text="#1A202C",
        muted="#64748B",
        rise="#C0392B",
        fall="#1E8449",
        warn="#B7791F",
        info="#2E75B6",
        series=(
            "#1F4E79",
            "#2E75B6",
            "#5B9BD5",
            "#9DC3E6",
            "#B7791F",
            "#1E8449",
            "#C0392B",
            "#7F8C99",
        ),
    ),
    "graphite": Theme(
        key="graphite",
        label="石墨灰",
        note="低饱和中性色。适合排版密集的运营台账与内部数据表。",
        accent="#334155",
        accent_light="#64748B",
        accent_text="#FFFFFF",
        surface="#F1F5F9",
        band="#F8FAFC",
        grid="#DDE4EC",
        text="#1A202C",
        muted="#6B7280",
        rise="#B91C1C",
        fall="#0F766E",
        warn="#B7791F",
        info="#475569",
        series=(
            "#334155",
            "#64748B",
            "#94A3B8",
            "#CBD5E1",
            "#0F766E",
            "#B7791F",
            "#B91C1C",
            "#7C3AED",
        ),
    ),
    "emerald": Theme(
        key="emerald",
        label="松石绿",
        note="适合生产、库存、质量、供应链等制造侧报表。",
        accent="#0F5132",
        accent_light="#0F766E",
        accent_text="#FFFFFF",
        surface="#E9F5F1",
        band="#F3FAF7",
        grid="#D3E8E0",
        text="#1A202C",
        muted="#5C7268",
        rise="#B91C1C",
        fall="#0F766E",
        warn="#B7791F",
        info="#1F4E79",
        series=(
            "#0F5132",
            "#0F766E",
            "#14B8A6",
            "#5EAAA8",
            "#1F4E79",
            "#B7791F",
            "#B91C1C",
            "#6B7280",
        ),
    ),
    "amber": Theme(
        key="amber",
        label="琥珀棕",
        note="暖色调。适合项目计划、进度跟踪、人力与预算类表格。",
        accent="#92400E",
        accent_light="#B45309",
        accent_text="#FFFFFF",
        surface="#FDF3E7",
        band="#FEF9F2",
        grid="#EADCC8",
        text="#1A202C",
        muted="#7A6653",
        rise="#B91C1C",
        fall="#15803D",
        warn="#B45309",
        info="#1F4E79",
        series=(
            "#92400E",
            "#B45309",
            "#D97706",
            "#F59E0B",
            "#1F4E79",
            "#0F766E",
            "#B91C1C",
            "#6B7280",
        ),
    ),
}

DEFAULT_THEME = "business"


def get_theme(name: str = DEFAULT_THEME) -> Theme:
    key = (name or DEFAULT_THEME).strip().lower()
    if key not in THEMES:
        raise KeyError(
            f"未知主题 {name!r}，可选：{', '.join(THEMES)}"
        )
    return THEMES[key]


# --------------------------------------------------------------------------
# 结构探测
# --------------------------------------------------------------------------
TOTAL_PATTERN = ("合计", "总计", "小计", "合 计", "总 计", "累计", "total", "subtotal", "sum")
DATE_HINT = ("日期", "时间", "年月", "date", "time", "month")
RATE_HINT = ("率", "占比", "比例", "同比", "环比", "增长", "占比%", "percent", "ratio", "%")
MONEY_HINT = (
    "金额", "单价", "总价", "价格", "价", "额", "成本", "收入", "营收", "费用",
    "利润", "毛利", "净利", "工资", "薪酬", "税", "应收", "应付", "余额",
    "库存金额", "产值", "预算", "实际支出", "amount", "price", "cost", "revenue",
)
QTY_HINT = (
    "数量", "件数", "个数", "台数", "套数", "箱数", "人数", "次数", "天数",
    "工时", "库存量", "在制", "产量", "销量", "qty", "quantity", "count",
)
CODE_HINT = (
    "单号", "编号", "编码", "代码", "料号", "订单号", "工单号", "批次",
    "序列号", "身份证", "电话", "手机", "code", "no.", "id",
)


@dataclass
class Layout:
    """单个工作表的版式结构。"""

    header_row: int = 1
    first_data_row: int = 2
    last_data_row: int = 1
    first_col: int = 1
    last_col: int = 1
    title_rows: tuple[int, ...] = ()
    total_rows: tuple[int, ...] = ()
    merged_title: str | None = None
    sheet_last_row: int = 1
    reason: str = "fallback"

    @property
    def data_rows(self) -> int:
        return max(0, self.last_data_row - self.first_data_row + 1)

    @property
    def columns(self) -> int:
        return max(0, self.last_col - self.first_col + 1)


def display_width(value: Any) -> int:
    """按东亚字符宽度估算显示宽度（中日韩字符算 2）。"""
    if value is None:
        return 0
    if isinstance(value, (datetime, date, time)):
        text = "2099-12-31"
    elif isinstance(value, float):
        text = f"{value:,.2f}"
    else:
        text = str(value)
    total = 0
    for ch in text:
        total += 2 if unicodedata.east_asian_width(ch) in ("W", "F") else 1
    return total


def _is_blank(value: Any) -> bool:
    return value is None or (isinstance(value, str) and not value.strip())


def _row_profile(ws, row: int, last_col: int) -> tuple[int, int]:
    """返回 (非空单元格数, 纯文本单元格数)。"""
    filled = 0
    textual = 0
    for col in range(1, last_col + 1):
        value = ws.cell(row=row, column=col).value
        if _is_blank(value):
            continue
        filled += 1
        if isinstance(value, str) and not value.startswith("="):
            textual += 1
    return filled, textual


def _used_bounds(ws) -> tuple[int, int]:
    """返回去掉尾部空行空列后的 (last_row, last_col)。"""
    last_row = ws.max_row or 1
    last_col = ws.max_column or 1

    probe = 0
    while last_row > 1 and probe < 800:
        filled, _ = _row_profile(ws, last_row, last_col)
        if filled:
            break
        last_row -= 1
        probe += 1

    probe = 0
    while last_col > 1 and probe < 200:
        has_value = any(
            not _is_blank(ws.cell(row=r, column=last_col).value)
            for r in range(1, min(last_row, 200) + 1)
        )
        if has_value:
            break
        last_col -= 1
        probe += 1

    return last_row, last_col


def detect_layout(ws) -> Layout:
    """推断表头行、数据区、合计行与标题行。无法判定时退回第 1 行为表头。"""
    last_row, last_col = _used_bounds(ws)
    if last_row <= 1 and last_col <= 1 and _is_blank(ws.cell(row=1, column=1).value):
        return Layout(reason="empty")

    profiles = {
        r: _row_profile(ws, r, last_col) for r in range(1, min(last_row, 20) + 1)
    }

    threshold = max(3, int(last_col * 0.4))
    header_row = 0
    for row in range(1, min(last_row, 12) + 1):
        filled, textual = profiles.get(row, (0, 0))
        if filled < threshold:
            continue
        if filled and textual / filled < 0.7:
            continue
        below = profiles.get(row + 1, (0, 0))[0]
        if below >= max(2, int(filled * 0.6)):
            header_row = row
            break

    reason = "heuristic"
    if not header_row:
        # 退化：取前 6 行里填得最满且文本占比高的一行
        candidates = [
            (profiles[r][0], r)
            for r in range(1, min(last_row, 6) + 1)
            if profiles[r][1] >= profiles[r][0] * 0.6 and profiles[r][0] > 0
        ]
        if candidates:
            header_row = max(candidates)[1]
            reason = "densest"
        else:
            header_row = 1
            reason = "fallback"

    # 标题行：表头之上还有内容的行
    title_rows = tuple(
        r for r in range(1, header_row) if profiles.get(r, (0, 0))[0] > 0
    )

    merged_title = None
    for rng in ws.merged_cells.ranges:
        if rng.min_row in title_rows and rng.max_row in title_rows and rng.max_col > rng.min_col:
            merged_title = rng.coord
            break

    first_data_row = header_row + 1
    while first_data_row < last_row:
        filled, _ = _row_profile(ws, first_data_row, last_col)
        if filled:
            break
        first_data_row += 1

    # 数据块：从首行数据起连续推进；遇到空行后若下一行明显不是表格行（如脚注）就收尾
    data_threshold = max(2, int(threshold * 0.5))
    last_data_row = first_data_row
    row = first_data_row
    while row <= last_row:
        filled, _ = profiles.get(row) or _row_profile(ws, row, last_col)
        if filled == 0:
            below, _ = profiles.get(row + 1) or _row_profile(ws, row + 1, last_col)
            if below >= data_threshold:
                row += 1
                continue
            break
        last_data_row = row
        row += 1
    if last_data_row < first_data_row:
        last_data_row = first_data_row

    # 合计行
    total_rows: list[int] = []
    scan_from = max(first_data_row, last_data_row - 40)
    for row in range(scan_from, last_data_row + 1):
        label = None
        for col in range(1, min(last_col, 4) + 1):
            value = ws.cell(row=row, column=col).value
            if isinstance(value, str) and value.strip():
                label = value.strip().lower().replace(" ", "")
                break
        if label and any(label.startswith(p.replace(" ", "")) for p in TOTAL_PATTERN):
            total_rows.append(row)

    return Layout(
        header_row=header_row,
        first_data_row=first_data_row,
        last_data_row=last_data_row,
        first_col=1,
        last_col=last_col,
        title_rows=title_rows,
        total_rows=tuple(total_rows),
        merged_title=merged_title,
        sheet_last_row=last_row,
        reason=reason,
    )


# --------------------------------------------------------------------------
# 列语义与数字格式
# --------------------------------------------------------------------------
def _header_text(ws, layout: Layout, col: int) -> str:
    value = ws.cell(row=layout.header_row, column=col).value
    return str(value).strip() if value is not None else ""


def _sample_values(ws, layout: Layout, col: int, limit: int = 80) -> list[Any]:
    values: list[Any] = []
    row = layout.first_data_row
    while row <= layout.last_data_row and len(values) < limit:
        if row in layout.total_rows:
            row += 1
            continue
        value = ws.cell(row=row, column=col).value
        if not _is_blank(value) and not (isinstance(value, str) and value.startswith("=")):
            values.append(value)
        row += 1
    return values


def _has_formula(ws, layout: Layout, col: int, limit: int = 60) -> bool:
    row = layout.first_data_row
    seen = 0
    while row <= layout.last_data_row and seen < limit:
        value = ws.cell(row=row, column=col).value
        if isinstance(value, str) and value.startswith("="):
            return True
        if not _is_blank(value):
            seen += 1
        row += 1
    return False


def guess_number_format(ws, layout: Layout, col: int) -> str | None:
    """按表头语义 + 样本值推断数字格式，返回 Excel 格式串或 None。"""
    header = _header_text(ws, layout, col).lower()
    samples = _sample_values(ws, layout, col)
    numeric = [v for v in samples if isinstance(v, (int, float)) and not isinstance(v, bool)]
    temporal = [v for v in samples if isinstance(v, (datetime, date))]

    if temporal:
        if any(isinstance(v, datetime) and (v.hour or v.minute) for v in temporal):
            return "yyyy-mm-dd hh:mm"
        return "yyyy-mm-dd"

    # 表头语义优先：全列都是公式时样本为空，仍要靠表头定格式
    if any(h in header for h in RATE_HINT):
        return "0.0%"
    if any(h in header for h in DATE_HINT):
        return None
    if any(h in header for h in MONEY_HINT):
        return '¥#,##0.00;[Red]-¥#,##0.00'
    if any(h in header for h in QTY_HINT):
        return '#,##0'
    if any(h in header for h in CODE_HINT):
        return None

    if not numeric:
        if _has_formula(ws, layout, col):
            return '#,##0.00'
        return None

    if all(isinstance(v, int) for v in numeric) and all(abs(v) < 1e12 for v in numeric):
        return '#,##0'

    return '#,##0.00'


def _looks_like_rate_column(ws, layout: Layout, col: int) -> bool:
    header = _header_text(ws, layout, col).lower()
    if any(h in header for h in RATE_HINT):
        return True
    samples = _sample_values(ws, layout, col, limit=40)
    numeric = [v for v in samples if isinstance(v, (int, float)) and not isinstance(v, bool)]
    return bool(numeric) and all(0 <= v <= 1 for v in numeric)


# --------------------------------------------------------------------------
# 样式应用
# --------------------------------------------------------------------------
def _base_font(theme: Theme, *, size: int = SIZE_BODY, bold: bool = False,
               color: str | None = None, italic: bool = False) -> Font:
    return Font(
        name=FONT_FAMILY, size=size, bold=bold, italic=italic,
        color=xl(color or theme.text),
    )


NOTE_PREFIX = ("注", "说明", "备注", "数据来源", "口径", "※", "＊", "*", "note", "source")


def _style_note_rows(ws, layout: Layout, theme: Theme) -> None:
    """把表格下方的单行脚注降为 9pt 灰字，避免它和正文抢视觉权重。"""
    if layout.sheet_last_row <= layout.last_data_row:
        return
    for row in range(layout.last_data_row + 1, layout.sheet_last_row + 1):
        filled, _ = _row_profile(ws, row, layout.last_col)
        if filled != 1:
            continue
        anchor = 0
        text = ""
        for col in range(1, layout.last_col + 1):
            value = ws.cell(row=row, column=col).value
            if isinstance(value, str) and value.strip():
                anchor = col
                text = value.strip()
                break
        if not anchor or not text.lower().startswith(NOTE_PREFIX):
            continue
        cell = ws.cell(row=row, column=anchor)
        cell.font = _base_font(theme, size=SIZE_NOTE, color=theme.muted)
        cell.alignment = Alignment(horizontal="left", vertical="top")
        ws.row_dimensions[row].height = 18


def _apply_title_block(ws, layout: Layout, theme: Theme) -> None:
    for row in layout.title_rows:
        primary = row == layout.title_rows[0]
        ws.row_dimensions[row].height = HEIGHT_TITLE if primary else HEIGHT_SUBTITLE
        for col in range(layout.first_col, layout.last_col + 1):
            cell = ws.cell(row=row, column=col)
            if _is_blank(cell.value):
                continue
            cell.font = _base_font(
                theme,
                size=SIZE_TITLE if primary else SIZE_SUBTITLE,
                bold=primary,
                color=theme.text if primary else theme.muted,
            )
            cell.alignment = Alignment(horizontal="left", vertical="center")
        # 标题下缘画一条主色细线，替代色块
        if primary:
            for col in range(layout.first_col, layout.last_col + 1):
                cell = ws.cell(row=row, column=col)
                cell.border = Border(bottom=Side(style="medium", color=xl(theme.accent)))


def _apply_header(ws, layout: Layout, theme: Theme) -> None:
    row = layout.header_row
    ws.row_dimensions[row].height = HEIGHT_HEADER
    fill = PatternFill("solid", fgColor=xl(theme.accent))
    edge = Side(style="medium", color=xl(theme.accent))
    for col in range(layout.first_col, layout.last_col + 1):
        cell = ws.cell(row=row, column=col)
        cell.fill = fill
        cell.font = _base_font(theme, size=SIZE_HEADER, bold=True, color=theme.accent_text)
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = Border(bottom=edge)


def _apply_body(ws, layout: Layout, theme: Theme, *, banding: bool,
                vertical_grid: bool, total_emphasis: bool = False,
                formats: dict[str, str] | None = None) -> None:
    if layout.data_rows <= 0:
        return

    formats = formats or {}
    band_fill = PatternFill("solid", fgColor=xl(theme.band))
    hair = Side(style="hair", color=xl(theme.grid))
    thin = Side(style="thin", color=xl(theme.grid))
    row_side = thin if layout.data_rows <= 60 else hair
    edge = Side(style="thin", color=xl(theme.grid)) if vertical_grid else None

    for offset, row in enumerate(range(layout.first_data_row, layout.last_data_row + 1)):
        is_total = row in layout.total_rows
        ws.row_dimensions[row].height = 28 if (is_total and total_emphasis) else HEIGHT_BODY
        striped = banding and not is_total and offset % 2 == 1
        for col in range(layout.first_col, layout.last_col + 1):
            cell = ws.cell(row=row, column=col)
            value = cell.value
            numeric_format = formats.get(get_column_letter(col))
            horizontal = None
            if isinstance(value, (int, float)) and not isinstance(value, bool):
                horizontal = "right"
            elif isinstance(value, (datetime, date)):
                horizontal = "center"
            elif isinstance(value, str) and value.startswith("="):
                # 公式单元格：按该列的数字格式判断它是数字还是文本，别一律当文本左对齐
                horizontal = "right" if numeric_format else "left"
            elif value is not None:
                horizontal = "left"
            cell.alignment = Alignment(
                horizontal=horizontal, vertical="center", wrap_text=False
            )
            cell.border = Border(
                bottom=row_side,
                left=edge,
                right=edge,
            )
            if not is_total:
                # 保留原有的加粗/斜体强调，只统一字体族、字号与字色
                current = cell.font
                cell.font = _base_font(
                    theme,
                    size=SIZE_BODY,
                    bold=bool(current.bold),
                    italic=bool(current.italic),
                    color=theme.text,
                )
            if striped and cell.fill.patternType in (None, "none"):
                cell.fill = band_fill
            if is_total:
                cell.fill = PatternFill("solid", fgColor=xl(theme.surface))
                cell.font = _base_font(
                    theme, size=SIZE_HEADER if total_emphasis else SIZE_BODY,
                    bold=True, color=theme.text,
                )
                cell.border = Border(
                    top=Side(style="thin", color=xl(theme.accent)),
                    bottom=Side(style="medium", color=xl(theme.accent)),
                    left=edge,
                    right=edge,
                )


    # 没有合计行时，用一条主色收边线把表尾封住，避免表格「悬空」
    if not layout.total_rows and layout.last_data_row >= layout.first_data_row:
        for col in range(layout.first_col, layout.last_col + 1):
            cell = ws.cell(row=layout.last_data_row, column=col)
            existing = cell.border
            cell.border = Border(
                top=existing.top,
                bottom=Side(style="medium", color=xl(theme.accent)),
                left=existing.left,
                right=existing.right,
            )


def _formatted_width(value: Any, fmt: str | None) -> int:
    """按目标数字格式估算真实显示宽度——千分位和货币符号会让数字变长很多。"""
    if fmt and isinstance(value, (int, float)) and not isinstance(value, bool):
        try:
            if "%" in fmt:
                return display_width(f"{value * 100:,.1f}%")
            if "¥" in fmt:
                return display_width(f"¥{value:,.2f}")
            if fmt.strip() == "#,##0":
                return display_width(f"{value:,.0f}")
            if ",.00" in fmt:
                return display_width(f"{value:,.2f}")
        except Exception:
            pass
    return display_width(value)


def _format_width(fmt: str | None) -> int:
    """公式单元格无法读到结果值时，按数字格式估算需要的显示宽度。"""
    if not fmt:
        return 10
    if "¥" in fmt or "$" in fmt:
        return 13
    if "%" in fmt:
        return 8
    if fmt.strip() == "#,##0":
        return 10
    return 11


def _apply_column_metrics(ws, layout: Layout, theme: Theme, *,
                          keep_widths: bool, wrap_long_text: bool,
                          formats: dict[str, str] | None = None) -> dict[str, float]:
    formats = formats or {}
    widths: dict[str, float] = {}
    for col in range(layout.first_col, layout.last_col + 1):
        letter = get_column_letter(col)
        if keep_widths:
            current = ws.column_dimensions[letter].width
            if current:
                widths[letter] = round(float(current), 2)
                continue

        header_len = display_width(ws.cell(row=layout.header_row, column=col).value)
        content_len = 0
        formula_len = 0
        col_fmt = formats.get(letter)
        for row in range(layout.first_data_row, min(layout.last_data_row, layout.first_data_row + 200) + 1):
            value = ws.cell(row=row, column=col).value
            if isinstance(value, str) and value.startswith("="):
                formula_len = _format_width(col_fmt)
                continue
            content_len = max(content_len, _formatted_width(value, col_fmt))

        target = max(header_len, content_len, formula_len)
        # 带格式的数字列多留一格呼吸位，避免货币符号与千分位把右边缘顶满
        padding = 4 if col_fmt else 3
        width = max(WIDTH_MIN, min(WIDTH_MAX, target + padding))
        ws.column_dimensions[letter].width = width
        widths[letter] = round(width, 2)

        if wrap_long_text and content_len > WIDTH_WRAP:
            for row in range(layout.first_data_row, layout.last_data_row + 1):
                cell = ws.cell(row=row, column=col)
                if isinstance(cell.value, str) and not cell.value.startswith("="):
                    cell.alignment = Alignment(
                        horizontal="left", vertical="center", wrap_text=True
                    )
    return widths


def _is_datetime_format(fmt: str | None) -> bool:
    """粗判一个 Excel 格式串是否属于日期/时间类。"""
    if not fmt:
        return False
    cleaned = re.sub(r"\[[^\]]*\]", "", fmt)
    cleaned = re.sub(r'"[^"]*"', "", cleaned)
    if any(token in cleaned for token in ("%", "¥", "$", "0")):
        return False
    return bool(re.search(r"[ymdhs]", cleaned.lower()))


def _apply_number_formats(ws, layout: Layout, *, force: bool) -> dict[str, str]:
    applied: dict[str, str] = {}
    for col in range(layout.first_col, layout.last_col + 1):
        fmt = guess_number_format(ws, layout, col)
        if not fmt:
            continue
        touched = False
        for row in range(layout.first_data_row, layout.last_data_row + 1):
            cell = ws.cell(row=row, column=col)
            if _is_blank(cell.value):
                continue
            if not isinstance(cell.value, (int, float, datetime, date)) and not (
                isinstance(cell.value, str) and cell.value.startswith("=")
            ):
                continue
            if not force:
                existing = cell.number_format
                if existing not in ("General", "general", "", "@"):
                    # 日期→日期属于「统一口径」，覆盖；其余自定义格式一律保留
                    if not (_is_datetime_format(existing) and _is_datetime_format(fmt)):
                        continue
            cell.number_format = fmt
            touched = True
        if touched:
            applied[get_column_letter(col)] = fmt
    return applied


def _apply_freeze_and_filter(ws, layout: Layout, theme: Theme, *,
                             freeze: bool, autofilter: bool) -> None:
    if freeze and layout.last_data_row > layout.header_row:
        freeze_col = 1
        if layout.columns >= 7:
            first_col_values = [
                ws.cell(row=r, column=layout.first_col).value
                for r in range(layout.first_data_row, min(layout.last_data_row, layout.first_data_row + 20) + 1)
            ]
            textual = sum(1 for v in first_col_values if isinstance(v, str))
            if textual >= max(1, len(first_col_values) * 0.6):
                freeze_col = layout.first_col + 1
        ws.freeze_panes = f"{get_column_letter(freeze_col)}{layout.header_row + 1}"

    if not autofilter or layout.data_rows <= 0:
        return
    data_end = layout.last_data_row
    while data_end > layout.first_data_row and data_end in layout.total_rows:
        data_end -= 1
    if data_end <= layout.header_row:
        return
    window = f"{get_column_letter(layout.first_col)}{layout.header_row}:{get_column_letter(layout.last_col)}{data_end}"
    blocked = any(
        rng.max_row >= layout.header_row and rng.min_row <= data_end
        and rng.max_col > rng.min_col
        for rng in ws.merged_cells.ranges
    )
    if blocked:
        return
    try:
        ws.auto_filter.ref = window
    except Exception:
        pass


def _apply_print_setup(ws, layout: Layout, theme: Theme) -> None:
    wide = layout.columns > 6
    ws.page_setup.orientation = "landscape" if wide else "portrait"
    try:
        ws.page_setup.paperSize = ws.PAPERSIZE_A4
    except Exception:
        pass
    if ws.sheet_properties.pageSetUpPr is None:
        from openpyxl.worksheet.properties import PageSetupProperties

        ws.sheet_properties.pageSetUpPr = PageSetupProperties()
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.print_options.horizontalCentered = True
    ws.page_margins.left = 0.4
    ws.page_margins.right = 0.4
    ws.page_margins.top = 0.75
    ws.page_margins.bottom = 0.75
    ws.page_margins.header = 0.3
    ws.page_margins.footer = 0.35
    if layout.last_data_row > layout.header_row:
        try:
            ws.print_title_rows = f"{layout.header_row}:{layout.header_row}"
        except Exception:
            pass
    ws.oddFooter.left.text = "&A"
    ws.oddFooter.right.text = "&P / &N"


def _apply_conditional(ws, layout: Layout, theme: Theme) -> int:
    """对纯数值列加数据条。最多 2 列——数据条一多就变成视觉噪音。"""
    from openpyxl.formatting.rule import DataBarRule

    count = 0
    for col in range(layout.first_col, layout.last_col + 1):
        if count >= 2:
            break
        if _looks_like_rate_column(ws, layout, col):
            continue
        samples = _sample_values(ws, layout, col, limit=40)
        numeric = [v for v in samples if isinstance(v, (int, float)) and not isinstance(v, bool)]
        if len(numeric) < 5 or len(numeric) != len(samples):
            continue
        if len(set(numeric)) < 3:
            continue
        rng = f"{get_column_letter(col)}{layout.first_data_row}:{get_column_letter(col)}{layout.last_data_row}"
        ws.conditional_formatting.add(
            rng,
            DataBarRule(
                start_type="min",
                end_type="max",
                color=chart_rgb(theme.accent_light),
                showValue=True,
                minLength=None,
                maxLength=None,
            ),
        )
        count += 1
    return count


def apply_chart_palette(wb, theme: Theme) -> int:
    """把图表系列配色统一到主题色板。返回处理过的图表数量。"""
    palette = [chart_rgb(c) for c in theme.series]
    touched = 0
    for ws in wb.worksheets:
        for chart in getattr(ws, "_charts", []) or []:
            try:
                for index, series in enumerate(chart.series):
                    color = palette[index % len(palette)]
                    props = series.graphicalProperties
                    if props is None:
                        continue
                    props.solidFill = color
                    try:
                        if props.line is not None:
                            props.line.solidFill = color
                        else:
                            props.line.noFill = False
                    except Exception:
                        pass
                legend = getattr(chart, "legend", None)
                if legend is not None and len(chart.series) > 1:
                    legend.position = "b"
                    legend.overlay = False
                touched += 1
            except Exception:
                continue
    return touched


def style_sheet(
    ws,
    theme: Theme,
    *,
    layout: Layout | None = None,
    title_style: bool = True,
    header_style: bool = True,
    body_style: bool = True,
    banding: bool = True,
    freeze: bool = True,
    autofilter: bool = True,
    number_formats: bool = True,
    force_formats: bool = False,
    keep_widths: bool = False,
    wrap_long_text: bool = True,
    gridlines_off: bool = True,
    print_setup: bool = True,
    conditional: bool = False,
    total_emphasis: bool = False,
    note_style: bool = True,
    tab_color: bool = True,
) -> dict[str, Any]:
    """对单个工作表应用主题。返回该表的处理摘要。"""
    layout = layout or detect_layout(ws)
    if layout.reason == "empty":
        return {"sheet": ws.title, "skipped": "empty"}

    # 先定数字格式：正文对齐与列宽都要靠它判断这一列是数字还是文本
    formats = _apply_number_formats(ws, layout, force=force_formats) if number_formats else {}

    if title_style:
        _apply_title_block(ws, layout, theme)
    if header_style:
        _apply_header(ws, layout, theme)
    if body_style:
        _apply_body(
            ws, layout, theme, banding=banding,
            vertical_grid=layout.columns >= 12, total_emphasis=total_emphasis,
            formats=formats,
        )
    if note_style:
        _style_note_rows(ws, layout, theme)

    widths = _apply_column_metrics(
        ws, layout, theme, keep_widths=keep_widths, wrap_long_text=wrap_long_text,
        formats=formats,
    )

    _apply_freeze_and_filter(ws, layout, theme, freeze=freeze, autofilter=autofilter)

    if print_setup:
        _apply_print_setup(ws, layout, theme)

    if gridlines_off:
        try:
            ws.sheet_view.showGridLines = False
        except Exception:
            pass

    if tab_color:
        try:
            ws.sheet_properties.tabColor = xl(theme.accent)
        except Exception:
            pass

    rules = _apply_conditional(ws, layout, theme) if conditional else 0

    return {
        "sheet": ws.title,
        "header_row": layout.header_row,
        "data_rows": layout.data_rows,
        "columns": layout.columns,
        "title_rows": list(layout.title_rows),
        "total_rows": list(layout.total_rows),
        "detect": layout.reason,
        "column_widths": widths,
        "number_formats": formats,
        "conditional_bars": rules,
    }


def apply_theme(
    wb,
    theme: str | Theme = DEFAULT_THEME,
    *,
    charts: bool = True,
    skip_sheets: Sequence[str] = (),
    **options: Any,
) -> list[dict[str, Any]]:
    """对整个工作簿应用主题，返回每张表的处理摘要。"""
    resolved = theme if isinstance(theme, Theme) else get_theme(theme)

    plans: list[dict[str, Any]] = []
    for ws in wb.worksheets:
        if ws.title in skip_sheets:
            continue
        plans.append(style_sheet(ws, resolved, **options))

    if charts:
        try:
            apply_chart_palette(wb, resolved)
        except Exception:
            pass

    try:
        wb.calculation.fullCalcOnLoad = True
    except Exception:
        pass

    set_default_font(wb, resolved)
    return plans


def set_default_font(wb, theme: Theme) -> None:
    """把 Normal 样式的默认字体改成主题字体，避免新增单元格回落到 Calibri。"""
    try:
        named = wb._named_styles["Normal"]  # noqa: SLF001
        named.font = _base_font(theme, size=SIZE_BODY)
    except Exception:
        pass


# --------------------------------------------------------------------------
# 便捷助手（供 build.py 直接调用）
# --------------------------------------------------------------------------
def add_data_bar(ws, cell_range: str, theme: str | Theme = DEFAULT_THEME) -> None:
    from openpyxl.formatting.rule import DataBarRule

    resolved = theme if isinstance(theme, Theme) else get_theme(theme)
    ws.conditional_formatting.add(
        cell_range,
        DataBarRule(
            start_type="min",
            end_type="max",
            color=chart_rgb(resolved.accent_light),
            showValue=True,
        ),
    )


def add_color_scale(ws, cell_range: str, theme: str | Theme = DEFAULT_THEME) -> None:
    from openpyxl.formatting.rule import ColorScaleRule

    resolved = theme if isinstance(theme, Theme) else get_theme(theme)
    ws.conditional_formatting.add(
        cell_range,
        ColorScaleRule(
            start_type="min",
            start_color=chart_rgb("#FFFFFF"),
            mid_type="percentile",
            mid_value=50,
            mid_color=chart_rgb(resolved.surface),
            end_type="max",
            end_color=chart_rgb(resolved.accent_light),
        ),
    )


def mark_total_row(ws, row: int, layout: Layout, theme: str | Theme = DEFAULT_THEME) -> None:
    """显式声明某行为合计行（用于合计行不以「合计」开头的场景）。"""
    resolved = theme if isinstance(theme, Theme) else get_theme(theme)
    edge = Side(style="thin", color=xl(resolved.accent))
    fill = PatternFill("solid", fgColor=xl(resolved.surface))
    for col in range(layout.first_col, layout.last_col + 1):
        cell = ws.cell(row=row, column=col)
        cell.fill = fill
        cell.font = _base_font(resolved, bold=True)
        cell.border = Border(top=edge, bottom=edge)


def kpi_card(
    ws,
    top_left: str,
    label: str,
    value: Any,
    *,
    delta: str | None = None,
    number_format: str | None = None,
    theme: str | Theme = DEFAULT_THEME,
    span: int = 3,
) -> str:
    """在 ``top_left`` 处画一张 KPI 卡片，占 ``span`` 列 × 3 行。

    卡片结构：标签（9 号灰）／数值（24 号加粗）／变化幅（10 号，涨红跌绿）。
    左侧有一条主色竖线作为视觉锚点。返回卡片占用的单元格范围。
    """
    from openpyxl.utils import coordinate_to_tuple

    resolved = theme if isinstance(theme, Theme) else get_theme(theme)
    row, col = coordinate_to_tuple(top_left)
    last_col = col + max(1, span) - 1
    rows = (row, row + 1, row + 2) if delta is not None else (row, row + 1)
    last_row = rows[-1]

    for r in rows:
        if last_col > col:
            ws.merge_cells(start_row=r, start_column=col, end_row=r, end_column=last_col)

    fill = PatternFill("solid", fgColor=xl(resolved.surface))
    rail = Side(style="medium", color=xl(resolved.accent))
    hair = Side(style="thin", color=xl(resolved.grid))

    for r in rows:
        for c in range(col, last_col + 1):
            cell = ws.cell(row=r, column=c)
            cell.fill = fill
            cell.border = Border(
                left=rail if c == col else hair,
                right=hair,
                top=hair if r == row else None,
                bottom=hair if r == last_row else None,
            )

    label_cell = ws.cell(row=row, column=col, value=label)
    label_cell.font = _base_font(resolved, size=SIZE_NOTE, color=resolved.muted)
    label_cell.alignment = Alignment(horizontal="left", vertical="center", indent=1)

    value_cell = ws.cell(row=row + 1, column=col, value=value)
    value_cell.font = _base_font(resolved, size=24, bold=True, color=resolved.text)
    value_cell.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    if number_format:
        value_cell.number_format = number_format

    ws.row_dimensions[row].height = 20
    ws.row_dimensions[row + 1].height = 40

    if delta is not None:
        delta_cell = ws.cell(row=row + 2, column=col, value=delta)
        negative = isinstance(delta, str) and delta.strip().startswith("-")
        color = resolved.fall if negative else resolved.rise
        delta_cell.font = _base_font(resolved, size=SIZE_BODY, color=color)
        delta_cell.alignment = Alignment(horizontal="left", vertical="center", indent=1)
        ws.row_dimensions[row + 2].height = 18

    return f"{get_column_letter(col)}{row}:{get_column_letter(last_col)}{last_row}"


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------
def _cli() -> int:
    parser = argparse.ArgumentParser(description="excel-studio 主题引擎")
    parser.add_argument("--list-themes", action="store_true", help="列出全部主题")
    parser.add_argument("--show", metavar="THEME", help="打印指定主题的令牌 JSON")
    args = parser.parse_args()

    if args.list_themes:
        for key, theme in THEMES.items():
            print(f"{key:<10} {theme.label:<6} {theme.note}")
        return 0

    if args.show:
        theme = get_theme(args.show)
        print(json.dumps(theme.__dict__, ensure_ascii=False, indent=2))
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(_cli())
