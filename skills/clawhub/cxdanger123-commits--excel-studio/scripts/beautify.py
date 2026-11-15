#!/usr/bin/env python3
"""对已有 Excel 工作簿做规则化美化：只动版式与样式，不改数据、不改公式。

用法::

    python beautify.py 报表.xlsx                       # 输出 报表_styled.xlsx
    python beautify.py 报表.xlsx -o 报表-终版.xlsx      # 指定输出
    python beautify.py 报表.xlsx --level conservative  # 只修列宽/格式/冻结，不动配色
    python beautify.py 报表.xlsx --dry-run             # 只出诊断计划，不落盘

退出码：0=成功，1=脚本错误，2=风险闸门拦截（需 --force 才继续）。
判定以 stdout 的 JSON `status` 为准。
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

try:
    from openpyxl import load_workbook
except ImportError:  # pragma: no cover
    sys.exit("缺少 openpyxl，请先安装：python -m pip install openpyxl")

import theme_engine as te  # noqa: E402

LEVELS = ("conservative", "standard", "bold")

LEVEL_OPTIONS: dict[str, dict[str, Any]] = {
    "conservative": dict(
        title_style=False,
        header_style=False,
        body_style=False,
        banding=False,
        number_formats=True,
        force_formats=False,
        wrap_long_text=True,
        gridlines_off=True,
        print_setup=True,
        total_emphasis=False,
        note_style=False,
        tab_color=False,
    ),
    "standard": dict(
        title_style=True,
        header_style=True,
        body_style=True,
        banding=True,
        number_formats=True,
        force_formats=False,
        wrap_long_text=True,
        gridlines_off=True,
        print_setup=True,
        total_emphasis=False,
        note_style=True,
        tab_color=True,
    ),
    "bold": dict(
        title_style=True,
        header_style=True,
        body_style=True,
        banding=True,
        number_formats=True,
        force_formats=False,
        wrap_long_text=True,
        gridlines_off=True,
        print_setup=True,
        total_emphasis=True,
        note_style=True,
        tab_color=True,
    ),
}


def scan_risks(wb) -> dict[str, list[dict[str, Any]]]:
    """扫描 openpyxl 读写往返会丢失或降级的对象。"""
    blocking: list[dict[str, Any]] = []
    warning: list[dict[str, Any]] = []

    for ws in wb.worksheets:
        charts = getattr(ws, "_charts", None) or []
        images = getattr(ws, "_images", None) or []
        pivots = getattr(ws, "_pivots", None) or []
        if charts:
            blocking.append(
                {
                    "type": "chart",
                    "sheet": ws.title,
                    "count": len(charts),
                    "why": "openpyxl 往返重存会丢失或降级已有图表",
                }
            )
        if images:
            blocking.append(
                {
                    "type": "image",
                    "sheet": ws.title,
                    "count": len(images),
                    "why": "图片可能丢失或被重新锚定错位",
                }
            )
        if pivots:
            blocking.append(
                {
                    "type": "pivot",
                    "sheet": ws.title,
                    "count": len(pivots),
                    "why": "数据透视表无法通过 openpyxl 原样保留",
                }
            )

    external = getattr(wb, "_external_links", None) or []
    if external:
        warning.append(
            {
                "type": "external_link",
                "count": len(external),
                "why": "存在外部工作簿引用，重存后缓存值可能失效",
            }
        )

    formulas = 0
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for cell in row:
                if isinstance(cell.value, str) and cell.value.startswith("="):
                    formulas += 1
    if formulas:
        warning.append(
            {
                "type": "formula_cache",
                "count": formulas,
                "why": "重存后公式无缓存值，预览器会显示空白，需重算或让 Excel 打开时计算",
            }
        )

    return {"blocking": blocking, "warning": warning}


def count_formulas(wb) -> int:
    total = 0
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for cell in row:
                if isinstance(cell.value, str) and cell.value.startswith("="):
                    total += 1
    return total


def find_recalc_script() -> Path | None:
    """按通用规则查找可用的 recalc.py（同根技能目录 / 环境变量指定）。"""
    candidates: list[Path] = []

    env = os.environ.get("EXCEL_RECALC_SCRIPT")
    if env:
        candidates.append(Path(env))

    # 从本脚本向上逐级查找同级安装的 xlsx 技能（如 ~/.claude/skills/{excel-studio,xlsx}）
    here = Path(__file__).resolve()
    for parent in here.parents:
        cand = parent / "xlsx" / "scripts" / "recalc.py"
        if cand.is_file():
            candidates.append(cand)
        cand2 = parent / "scripts" / "recalc.py"   # 与 beautify.py 同目录
        if cand2.is_file() and cand2 != here:
            candidates.append(cand2)
        if parent.name in ("skills", ".claude", ".agents"):
            break

    for path in candidates:
        if path.is_file():
            return path
    return None


def run_recalc(xlsx: Path) -> dict[str, Any]:
    script = find_recalc_script()
    if script is None:
        return {
            "status": "unavailable",
            "message": "未找到内置 recalc.py；已设置 fullCalcOnLoad，Excel/WPS 打开时会自动重算，但第三方预览器仍可能显示空白",
        }
    try:
        proc = subprocess.run(
            [sys.executable, str(script), str(xlsx), "60"],
            capture_output=True,
            text=True,
            timeout=240,
        )
    except subprocess.TimeoutExpired:
        return {"status": "error", "message": "recalc 超时（240s）"}
    except Exception as exc:  # pragma: no cover
        return {"status": "error", "message": f"recalc 调用失败：{exc}"}

    stdout = (proc.stdout or "").strip()
    try:
        payload = json.loads(stdout[stdout.index("{") :]) if "{" in stdout else {}
    except Exception:
        payload = {}
    if payload:
        return {"status": payload.get("status", "unknown"), "detail": payload}
    return {
        "status": "error",
        "message": (proc.stderr or stdout or "recalc 无输出").strip()[:800],
    }


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="对已有 Excel 做规则化美化")
    parser.add_argument("input", help="待美化的 .xlsx 路径")
    parser.add_argument("-o", "--output", help="输出路径，默认 <原名>_styled.xlsx")
    parser.add_argument("--theme", default=te.DEFAULT_THEME, choices=list(te.THEMES))
    parser.add_argument("--level", default="standard", choices=LEVELS)
    parser.add_argument("--sheet", action="append", help="只处理指定工作表（可多次传）")
    parser.add_argument(
        "--data-bars",
        help="对指定列加数据条，逗号分隔列字母（如 E,H）。数据条属于内容决策，脚本不会自动加",
    )
    parser.add_argument("--dry-run", action="store_true", help="只输出计划，不写文件")
    parser.add_argument("--force", action="store_true", help="忽略风险闸门强制继续")
    parser.add_argument("--recalc", action="store_true", help="保存后调用内置 recalc 补齐公式缓存")
    parser.add_argument(
        "--recalc-only",
        action="store_true",
        help="只补公式缓存值，不改任何样式、不另存文件（用于生成链路收尾）",
    )
    parser.add_argument("--report", help="把 JSON 报告同时写入该路径")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    src = Path(args.input).expanduser().resolve()
    if not src.is_file():
        print(json.dumps({"status": "error", "message": f"文件不存在：{src}"}, ensure_ascii=False))
        return 1

    out = Path(args.output).expanduser().resolve() if args.output else src.with_name(
        f"{src.stem}_styled{src.suffix or '.xlsx'}"
    )
    overwrite = out == src

    if args.recalc_only:
        result = run_recalc(src)
        payload = {"status": result.get("status", "error"), "file": str(src), "recalc": result}
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        if args.report:
            Path(args.report).write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        return 0 if result.get("status") == "success" else 1

    try:
        wb = load_workbook(src)
    except Exception as exc:
        print(json.dumps({"status": "error", "message": f"无法读取工作簿：{exc}"}, ensure_ascii=False))
        return 1

    risks = scan_risks(wb)
    if risks["blocking"] and not args.force:
        payload = {
            "status": "blocked",
            "input": str(src),
            "risks": risks,
            "route": "manual-edit-in-excel-or-wps",
            "message": "该工作簿含图表/图片/透视表，openpyxl 往返会破坏它们。改用 Excel/WPS 手动微调；确需强制重排样式时加 --force。",
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        if args.report:
            Path(args.report).write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        return 2

    options = dict(LEVEL_OPTIONS[args.level])
    skip = set(args.sheet or [])
    unknown = skip - set(wb.sheetnames)
    if unknown:
        print(json.dumps({"status": "error", "message": f"工作表不存在：{sorted(unknown)}"}, ensure_ascii=False))
        return 1

    plan: list[dict[str, Any]] = []
    for ws in wb.worksheets:
        if skip and ws.title not in skip:
            continue
        layout = te.detect_layout(ws)
        if layout.reason == "empty":
            plan.append({"sheet": ws.title, "skipped": "empty"})
            continue
        planned_formats: dict[str, str] = {}
        for col in range(layout.first_col, layout.last_col + 1):
            fmt = te.guess_number_format(ws, layout, col)
            if fmt:
                planned_formats[te.get_column_letter(col)] = fmt
        plan.append(
            {
                "sheet": ws.title,
                "detect": layout.reason,
                "header_row": layout.header_row,
                "title_rows": list(layout.title_rows),
                "data_rows": layout.data_rows,
                "columns": layout.columns,
                "total_rows": list(layout.total_rows),
                "planned_formats": planned_formats,
            }
        )

    if args.dry_run:
        payload = {
            "status": "dry_run",
            "input": str(src),
            "theme": args.theme,
            "level": args.level,
            "risks": risks,
            "plan": plan,
        }
        text = json.dumps(payload, ensure_ascii=False, indent=2)
        print(text)
        if args.report:
            Path(args.report).write_text(text, encoding="utf-8")
        return 0

    theme = te.get_theme(args.theme)
    applied: list[dict[str, Any]] = []
    for ws in wb.worksheets:
        if skip and ws.title not in skip:
            continue
        try:
            applied.append(te.style_sheet(ws, theme, **options))
        except Exception as exc:
            applied.append({"sheet": ws.title, "error": str(exc)})

    charts = te.apply_chart_palette(wb, theme) if args.level != "conservative" else 0
    if args.level != "conservative":
        te.set_default_font(wb, theme)

    bars: list[str] = []
    if args.data_bars:
        from openpyxl.utils import column_index_from_string

        wanted = [c.strip().upper() for c in args.data_bars.split(",") if c.strip()]
        for ws in wb.worksheets:
            if skip and ws.title not in skip:
                continue
            layout = te.detect_layout(ws)
            if layout.reason == "empty":
                continue
            for letter in wanted:
                try:
                    index = column_index_from_string(letter)
                except ValueError:
                    continue
                if not (layout.first_col <= index <= layout.last_col) or layout.data_rows <= 0:
                    continue
                rng = f"{letter}{layout.first_data_row}:{letter}{layout.last_data_row}"
                te.add_data_bar(ws, rng, theme)
                bars.append(f"{ws.title}!{rng}")
    try:
        wb.calculation.fullCalcOnLoad = True
    except Exception:
        pass

    if overwrite:
        backup = src.with_suffix(f"{src.suffix}.bak")
        try:
            shutil.copy2(src, backup)
        except Exception as exc:
            print(json.dumps({"status": "error", "message": f"备份失败，已中止：{exc}"}, ensure_ascii=False))
            return 1
    else:
        backup = None

    out.parent.mkdir(parents=True, exist_ok=True)
    try:
        wb.save(out)
    except Exception as exc:
        print(json.dumps({"status": "error", "message": f"保存失败：{exc}"}, ensure_ascii=False))
        return 1

    formulas = count_formulas(wb)
    recalc = {"status": "skipped", "message": "工作簿无公式"}
    if formulas:
        recalc = run_recalc(out) if args.recalc else {
            "status": "pending",
            "message": "重存后公式无缓存值，第三方预览器会显示空白。加 --recalc 补齐，或依赖 fullCalcOnLoad 让 Excel/WPS 打开时重算",
        }

    payload = {
        "status": "ok",
        "input": str(src),
        "output": str(out),
        "backup": str(backup) if backup else None,
        "theme": args.theme,
        "level": args.level,
        "charts_recolored": charts,
        "data_bars": bars,
        "formula_cells": formulas,
        "recalc": recalc,
        "risks": risks,
        "sheets": applied,
    }
    text = json.dumps(payload, ensure_ascii=False, indent=2)
    print(text)
    if args.report:
        Path(args.report).write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
