# -*- coding: utf-8 -*-
"""Verify a month's 施工日志 for format + page-number continuity.

Usage:
    <docx-venv-python> verify_month.py 2026 9
    <docx-venv-python> verify_month.py 2026 7 --dir "C:/Users/hi/Desktop/自动日志/7月份"

Checks per file:
  - page number == 43 + (date - 2026-05-20).days
  - page numbers strictly consecutive across the month
  - date cell matches "YYYY年 MM月 DD日 星期X" with the correct weekday
  - Row 4 / Row 5 are each exactly ONE paragraph (soft \\n breaks, not add_paragraph)
  - every non-empty run is 11pt with eastAsia=宋体
  - row heights == [400, 360, 400, 400, 7000, 4500] twips
  - document body == ['p', 'tbl', 'sectPr']  (no stray signature paragraphs)
  - Row 5 ends with the 项目技术负责人 + 施工记录 block

Exit code 0 = all present files pass. Non-zero = something needs attention.

NOTE: some legacy files (e.g. 2026-07-01..03, 07-07..09 — 工程桩统计-style logs) legitimately
use a multi-paragraph Row 4/5 structure. They will report non-1 paragraph counts. That is
pre-existing, not a regression; use --only to restrict the check to files you just generated.
"""
import argparse
import calendar
import os
import sys
from datetime import date

from docx import Document
from docx.oxml.ns import qn

WD = '一二三四五六日'
PAGE_BASE_DATE = date(2026, 5, 20)
PAGE_BASE_NUM = 43
EXPECTED_HEIGHTS = [400, 360, 400, 400, 7000, 4500]
EXPECTED_BODY = ['p', 'tbl', 'sectPr']


def expected_page(d):
    return PAGE_BASE_NUM + (d - PAGE_BASE_DATE).days


def inspect(path, d):
    """Return (dict_of_checks, page_number_or_None)."""
    doc = Document(path)
    tb = doc.tables[0]
    chk = {}

    raw_page = tb.rows[0].cells[3].text.strip()
    try:
        page = int(raw_page)
    except ValueError:
        page = None
    chk['page'] = (page == expected_page(d))

    ds = tb.rows[2].cells[1].text.strip()
    chk['date'] = (f'{d.day:02d}日' in ds) and (f'星期{WD[d.weekday()]}' in ds)

    chk['r4_single_para'] = len(tb.rows[4].cells[0].paragraphs) == 1
    chk['r5_single_para'] = len(tb.rows[5].cells[0].paragraphs) == 1

    sizes, fonts = set(), set()
    for row in tb.rows:
        for cell in row.cells:
            for para in cell.paragraphs:
                for run in para.runs:
                    if not run.text:
                        continue
                    sizes.add(run.font.size.pt if run.font.size else None)
                    # explicit find() — truth-testing rPr/rFonts emits FutureWarning
                    # on newer lxml and can misreport valid elements as falsy
                    rpr = run._element.find(qn('w:rPr'))
                    if rpr is not None:
                        rf = rpr.find(qn('w:rFonts'))
                        if rf is not None:
                            fonts.add(rf.get(qn('w:eastAsia')))
    chk['font_11pt'] = sizes == {11.0}
    chk['font_songti'] = fonts == {'宋体'}

    heights = [r.height.twips if r.height else None for r in tb.rows]
    chk['row_heights'] = heights == EXPECTED_HEIGHTS

    body = [c.tag.split('}')[1] for c in doc.element.body]
    chk['body_structure'] = body == EXPECTED_BODY

    r5 = tb.rows[5].cells[0].text
    chk['signature'] = ('项目技术负责人' in r5) and (f'施工记录：{d.year}年{d.month:02d}月{d.day:02d}日' in r5)

    return chk, page


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('year', type=int)
    ap.add_argument('month', type=int)
    ap.add_argument('--dir', default=None, help='override folder path')
    ap.add_argument('--only', default=None,
                    help='comma-separated days to check, e.g. 17,25,28,30')
    args = ap.parse_args()

    folder = args.dir or f'C:/Users/hi/Desktop/自动日志/{args.month}月份'
    only = {int(x) for x in args.only.split(',')} if args.only else None

    ndays = calendar.monthrange(args.year, args.month)[1]
    prev_page = None
    all_ok = True
    missing = []

    print(f'{"date":<9}{"page":<12}{"status"}')
    print('-' * 58)

    for day in range(1, ndays + 1):
        if only and day not in only:
            continue
        d = date(args.year, args.month, day)
        path = os.path.join(folder, f'施工日志_{d:%Y%m%d}.docx')
        if not os.path.exists(path):
            missing.append(f'{d:%Y-%m-%d}')
            print(f'{d:%m-%d}     {"-":<12}MISSING')
            continue

        chk, page = inspect(path, d)
        if prev_page is not None and page is not None and page != prev_page + 1:
            chk['page_consecutive'] = False
        prev_page = page

        failed = [k for k, v in chk.items() if not v]
        if failed:
            all_ok = False
            print(f'{d:%m-%d}     {page!s:<12}FAIL  {failed}')
        else:
            print(f'{d:%m-%d}     {page!s:<12}ok')

    print('-' * 58)
    if missing:
        print(f'missing files ({len(missing)}): {", ".join(missing)}')
        print('  -> classify before backfilling; see references/backfill-and-gap-audit.md')
    print('RESULT:', 'all checked files pass' if all_ok else 'problems found (see FAIL rows)')
    return 0 if all_ok else 1


if __name__ == '__main__':
    sys.exit(main())
