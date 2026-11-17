#!/usr/bin/env python3
"""交付前质检：把「看起来没做完」的常见缺陷查出来。

用法::

    python qa_check.py 报表.xlsx
    python qa_check.py 报表.xlsx --report qa.json

stdout 输出一个 JSON，`status` 取 pass / warn / fail。
退出码固定为 0（除非脚本自身出错），**判定请读 JSON 的 status，不要看退出码**。
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

try:
    from openpyxl import load_workbook
    from openpyxl.utils import get_column_letter
except ImportError:  # pragma: no cover
    sys.exit("缺少 openpyxl，请先安装：python -m pip install openpyxl")

import theme_engine as te  # noqa: E402

ERROR_MARKERS = ("#REF!", "#DIV/0!", "#VALUE!", "#NAME?", "#N/A", "#NULL!", "#NUM!", "#SPILL!", "#CALC!")
NUMERIC_TEXT = re.compile(r"^[+-]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?%?$")
ILLEGAL_SHEET_CHARS = set('[]:*?/\\')

FAIL_CODES = {"formula_error", "header_missing", "duplicate_header", "bad_sheet_name"}


def issue(level: str, code: str, sheet: str, message: str, cell: str | None = None,
          fix: str | None = None) -> dict[str, Any]:
    item = {"level": level, "code": code, "sheet": sheet, "message": message}
    if cell:
        item["cell"] = cell
    if fix:
        item["fix"] = fix
    return item


def check_sheet(ws, cached_ws) -> list[dict[str, Any]]:
    found: list[dict[str, Any]] = []
    layout = te.detect_layout(ws)

    if layout.reason == "empty":
        found.append(issue("info", "empty_sheet", ws.title, "工作表为空"))
        return found

    # 1. 表头完整性
    blank_headers = [
        get_column_letter(col)
        for col in range(layout.first_col, layout.last_col + 1)
        if te._is_blank(ws.cell(row=layout.header_row, column=col).value)  # noqa: SLF001
    ]
    if blank_headers:
        found.append(
            issue(
                "fail",
                "header_missing",
                ws.title,
                f"表头行第 {layout.header_row} 行有 {len(blank_headers)} 个空表头：{', '.join(blank_headers[:8])}",
                cell=f"{blank_headers[0]}{layout.header_row}",
                fix="补齐列名，或把空列删掉；无表头的数据区在筛选和透视时不可用",
            )
        )

    # 2. 重复表头
    seen: dict[str, int] = {}
    for col in range(layout.first_col, layout.last_col + 1):
        value = ws.cell(row=layout.header_row, column=col).value
        if te._is_blank(value):
            continue
        key = str(value).strip()
        seen[key] = seen.get(key, 0) + 1
    dup = [k for k, v in seen.items() if v > 1]
    if dup:
        found.append(
            issue(
                "fail",
                "duplicate_header",
                ws.title,
                f"表头重复：{'、'.join(dup[:6])}",
                fix="同名列改写为可区分的名字（如「金额-含税」「金额-不含税」）",
            )
        )

    # 3. 公式错误值
    error_cells = []
    numbers_as_text = []
    for row in ws.iter_rows(
        min_row=layout.first_data_row, max_row=layout.last_data_row,
        min_col=layout.first_col, max_col=layout.last_col,
    ):
        for cell in row:
            value = cell.value
            if isinstance(value, str):
                if value.strip().upper().startswith(ERROR_MARKERS):
                    error_cells.append(cell.coordinate)
                    continue
                if NUMERIC_TEXT.match(value.strip()) and len(value.strip()) <= 18:
                    if cell.number_format in ("@", "General", "general") and cell.alignment.horizontal in (None, "left"):
                        numbers_as_text.append(cell.coordinate)
    if error_cells:
        found.append(
            issue(
                "fail",
                "formula_error",
                ws.title,
                f"{len(error_cells)} 个错误值单元格：{', '.join(error_cells[:8])}",
                cell=error_cells[0],
                fix="补空值/除零保护后重算；错误值会在筛选、汇总与图表里连锁放大",
            )
        )
    if numbers_as_text:
        found.append(
            issue(
                "warn",
                "number_as_text",
                ws.title,
                f"{len(numbers_as_text)} 个数字以文本形式存储：{', '.join(numbers_as_text[:8])}",
                cell=numbers_as_text[0],
                fix="转成数值并设置数字格式，否则 SUM/排序/条件格式都会失效",
            )
        )

    # 4. 数据区内的合并单元格
    merged_in_data = []
    for rng in ws.merged_cells.ranges:
        if rng.max_row >= layout.first_data_row and rng.min_row <= layout.last_data_row:
            merged_in_data.append(rng.coord)
    if merged_in_data:
        found.append(
            issue(
                "warn",
                "merged_in_data",
                ws.title,
                f"数据区存在 {len(merged_in_data)} 处合并单元格：{', '.join(merged_in_data[:6])}",
                cell=merged_in_data[0],
                fix="数据区合并会破坏排序与筛选；改为每行填满，或把合并上移到标题区",
            )
        )

    # 5. 列宽不足
    narrow = []
    for col in range(layout.first_col, layout.last_col + 1):
        letter = get_column_letter(col)
        header = ws.cell(row=layout.header_row, column=col).value
        need = te.display_width(header)
        width = ws.column_dimensions[letter].width
        if need >= 10 and (width is None or width < need * 0.8):
            narrow.append(letter)
    if narrow:
        found.append(
            issue(
                "warn",
                "column_too_narrow",
                ws.title,
                f"{len(narrow)} 列宽度不足以显示表头：{', '.join(narrow[:8])}",
                fix="重算列宽（beautify.py 默认会做），或对表头开启自动换行",
            )
        )

    # 6. 冻结与筛选
    if layout.data_rows > 30 and not ws.freeze_panes:
        found.append(
            issue("warn", "no_freeze", ws.title, f"{layout.data_rows} 行数据但未冻结窗格",
                  fix="冻结表头下方，滚动时保持列名可见")
        )
    if layout.data_rows > 20 and not ws.auto_filter.ref and not merged_in_data:
        found.append(
            issue("warn", "no_filter", ws.title, f"{layout.data_rows} 行数据但未开启筛选",
                  fix="在表头行加 AutoFilter")
        )

    # 7. 打印设置
    if layout.columns > 6 and not ws.print_title_rows:
        found.append(
            issue("warn", "no_print_titles", ws.title, "宽表未设置打印标题行",
                  fix="print_title_rows 设为表头行，跨页时每页重复表头")
        )

    # 8. 长文本未换行
    long_no_wrap = 0
    for col in range(layout.first_col, layout.last_col + 1):
        for row in range(layout.first_data_row, min(layout.last_data_row, layout.first_data_row + 300) + 1):
            cell = ws.cell(row=row, column=col)
            if isinstance(cell.value, str) and len(cell.value) > 40 and not cell.alignment.wrap_text:
                long_no_wrap += 1
    if long_no_wrap > 3:
        found.append(
            issue("info", "long_text_no_wrap", ws.title, f"{long_no_wrap} 个长文本单元格未换行",
                  fix="对长文本列开启 wrap_text 并适当加宽")
        )

    # 9. 公式缓存值
    if cached_ws is not None:
        missing = 0
        for row in ws.iter_rows(
            min_row=1, max_row=layout.last_data_row,
            min_col=1, max_col=layout.last_col,
        ):
            for cell in row:
                if isinstance(cell.value, str) and cell.value.startswith("="):
                    cached = cached_ws[cell.coordinate].value
                    if cached is None:
                        missing += 1
        if missing:
            found.append(
                issue(
                    "warn",
                    "formula_cache_missing",
                    ws.title,
                    f"{missing} 个公式单元格没有缓存值，第三方预览器会显示空白",
                    fix="跑重算脚本补缓存值；仅靠 fullCalcOnLoad 只对 Excel/WPS 有效",
                )
            )

    return found


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Excel 交付前质检")
    parser.add_argument("input", help="待检查的 .xlsx 路径")
    parser.add_argument("--report", help="把 JSON 报告写入该路径")
    args = parser.parse_args(argv)

    path = Path(args.input).expanduser().resolve()
    if not path.is_file():
        print(json.dumps({"status": "error", "message": f"文件不存在：{path}"}, ensure_ascii=False))
        return 1

    try:
        wb = load_workbook(path)
        cached = load_workbook(path, data_only=True)
    except Exception as exc:
        print(json.dumps({"status": "error", "message": f"无法读取工作簿：{exc}"}, ensure_ascii=False))
        return 1

    findings: list[dict[str, Any]] = []

    for ws in wb.worksheets:
        if ws.sheet_state != "visible":
            findings.append(issue("info", "hidden_sheet", ws.title, "工作表处于隐藏状态"))
            continue
        if len(ws.title) > 31:
            findings.append(issue("fail", "bad_sheet_name", ws.title, "工作表名超过 31 字符"))
        if ILLEGAL_SHEET_CHARS & set(ws.title):
            findings.append(
                issue("fail", "bad_sheet_name", ws.title, f"工作表名含非法字符：{''.join(sorted(ILLEGAL_SHEET_CHARS & set(ws.title)))}")
            )
        try:
            findings.extend(check_sheet(ws, cached[ws.title] if ws.title in cached.sheetnames else None))
        except Exception as exc:
            findings.append(issue("warn", "check_error", ws.title, f"检查该表时出错：{exc}"))

    levels = {f["level"] for f in findings}
    if any(f["code"] in FAIL_CODES for f in findings):
        status = "fail"
    elif "warn" in levels:
        status = "warn"
    else:
        status = "pass"

    summary = {
        "fail": sum(1 for f in findings if f["level"] == "fail"),
        "warn": sum(1 for f in findings if f["level"] == "warn"),
        "info": sum(1 for f in findings if f["level"] == "info"),
    }

    payload = {
        "status": status,
        "file": str(path),
        "sheets": len(wb.sheetnames),
        "summary": summary,
        "issues": findings,
    }
    text = json.dumps(payload, ensure_ascii=False, indent=2)
    print(text)
    if args.report:
        Path(args.report).write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
