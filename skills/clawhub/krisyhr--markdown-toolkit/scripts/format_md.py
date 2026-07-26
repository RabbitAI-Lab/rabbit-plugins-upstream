#!/usr/bin/env python3
"""
Markdown 排版工具箱 - 核心格式化脚本

用法: python3 format_md.py <命令> <文件路径> [选项]

命令:
  fix-spacing    中英文间加空格 + 标点修正
  to-wechat      转换为微信公众号格式 (输出 HTML)
  table-to-csv   提取 Markdown 表格并转为 CSV
  csv-to-table   将 CSV 转回 Markdown 表格
  stats          字数统计
  toc            生成目录
  check-links    提取链接
"""

import sys
import re
import csv
import io
from pathlib import Path


# ─── 1. 中英文间距 ─────────────────────────────────

def fix_cn_en_spacing(text: str) -> str:
    """中英文间加空格 + 全角半角标点修正"""
    # 中文后接英文/数字: 加空格
    text = re.sub(r'([\u4e00-\u9fff])([a-zA-Z0-9@#$%&])', r'\1 \2', text)
    # 英文/数字后接中文: 加空格
    text = re.sub(r'([a-zA-Z0-9}])([\u4e00-\u9fff])', r'\1 \2', text)
    # 中文括号修正: 英文内容用半角括号，中文内容用全角
    # 中文后接半角括号 → 全角
    text = re.sub(r'([\u4e00-\u9fff])\(', r'\1（', text)
    text = re.sub(r'\)([\u4e00-\u9fff])', r'）\1', text)
    # 中文后接半角冒号 → 全角
    text = re.sub(r'([\u4e00-\u9fff]):', r'\1：', text)
    # 连续多个空格合并为一个
    text = re.sub(r'  +', ' ', text)
    return text


# ─── 2. 微信公众号转换 ───────────────────────────

def md_to_wechat(md_text: str) -> str:
    """将 Markdown 转换为微信公众号可用的 HTML"""

    lines = md_text.split('\n')
    html_parts = []
    in_code_block = False
    code_buffer = []

    for line in lines:
        # 代码块
        if line.startswith('```'):
            if in_code_block:
                html_parts.append(_format_code_block('\n'.join(code_buffer)))
                code_buffer = []
                in_code_block = False
            else:
                in_code_block = True
            continue

        if in_code_block:
            code_buffer.append(line)
            continue

        stripped = line.strip()

        # 空行
        if not stripped:
            continue

        # 标题
        h_match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if h_match:
            level = len(h_match.group(1))
            title = _inline_format(h_match.group(2))
            size_map = {1: 24, 2: 20, 3: 18, 4: 16, 5: 15, 6: 14}
            html_parts.append(
                f'<h{level} style="font-size: {size_map[level]}px; '
                f'font-weight: bold; margin: 16px 0 8px 0;">{title}</h{level}>'
            )
            continue

        # 分割线
        if re.match(r'^---+\s*$', stripped):
            html_parts.append('<hr style="border: none; border-top: 1px solid #ddd; margin: 16px 0;" />')
            continue

        # 引用块
        if line.startswith('> '):
            content = _inline_format(line[2:])
            html_parts.append(
                f'<blockquote style="border-left: 3px solid #07c160; '
                f'margin: 8px 0; padding: 4px 12px; color: #666;">'
                f'{content}</blockquote>'
            )
            continue

        # 普通段落
        html_parts.append(f'<p>{_inline_format(line)}</p>')

    html_parts.append('')

    html = (
        '<section style="padding: 0 8px; font-size: 15px; line-height: 1.75; '
        'letter-spacing: 0.5px; color: #333;">'
        + ''.join(html_parts)
        + '</section>'
    )
    return html


def _inline_format(text: str) -> str:
    """行内格式化: 加粗、斜体、链接、行内代码"""
    # 加粗 **text**
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # 斜体 *text*
    text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', text)
    # 行内代码 `code`
    text = re.sub(r'`([^`]+)`', r'<code style="background: #f5f5f5; padding: 2px 4px; border-radius: 3px; font-size: 14px;">\1</code>', text)
    # 链接 [text](url)
    text = re.sub(
        r'\[([^\]]+)\]\(([^)]+)\)',
        r'<a href="\2" style="color: #07c160; text-decoration: none;">\1</a>',
        text
    )
    return text


def _format_code_block(code: str) -> str:
    """格式化代码块为微信样式"""
    escaped = code.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return (
        f'<pre style="background: #f7f7f7; border-radius: 4px; '
        f'padding: 12px; font-size: 13px; line-height: 1.5; '
        f'overflow-x: auto; margin: 8px 0;">'
        f'<code>{escaped}</code></pre>'
    )


# ─── 3. 表格 ↔ CSV ──────────────────────────────

def extract_tables(md_text: str) -> list:
    """提取 Markdown 中的所有表格，返回列表 of list of list"""
    tables = []
    lines = md_text.split('\n')
    i = 0
    while i < len(lines):
        if '|' in lines[i] and i + 1 < len(lines) and re.match(r'^\s*[\|\-\s:]+\s*$', lines[i+1]):
            # 找到表头行和分隔行
            header = _parse_table_row(lines[i])
            sep = lines[i+1]
            # 读取数据行
            rows = [header]
            j = i + 2
            while j < len(lines) and '|' in lines[j]:
                rows.append(_parse_table_row(lines[j]))
                j += 1
            tables.append(rows)
            i = j
        else:
            i += 1
    return tables


def _parse_table_row(line: str) -> list:
    """解析一行 Markdown 表格"""
    cells = [c.strip() for c in line.split('|')]
    # 去掉首尾空单元格（| 在行首行尾）
    if cells and not cells[0]:
        cells = cells[1:]
    if cells and not cells[-1]:
        cells = cells[:-1]
    return cells


def tables_to_csv(md_text: str) -> list:
    """将 Markdown 表格转为 CSV 字符串列表"""
    tables = extract_tables(md_text)
    results = []
    for i, rows in enumerate(tables, 1):
        output = io.StringIO()
        writer = csv.writer(output)
        for row in rows:
            writer.writerow(row)
        results.append({
            'table_index': i,
            'csv': output.getvalue().strip(),
            'rows': len(rows),
            'cols': len(rows[0]) if rows else 0,
        })
    return results


def csv_to_table(csv_text: str) -> str:
    """将 CSV 文本转为 Markdown 表格"""
    reader = csv.reader(io.StringIO(csv_text))
    rows = list(reader)
    if not rows:
        return ""

    # 计算每列最大宽度
    col_widths = []
    for row in rows:
        while len(col_widths) < len(row):
            col_widths.append(0)
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(cell.strip()))

    lines = []
    # 表头
    header = '| ' + ' | '.join(c.strip().ljust(col_widths[i]) for i, c in enumerate(rows[0])) + ' |'
    lines.append(header)
    # 分隔行
    sep = '|-' + '-|-'.join('-' * w for w in col_widths) + '-|'
    lines.append(sep)
    # 数据行
    for row in rows[1:]:
        padded = row + [''] * (len(col_widths) - len(row))
        line = '| ' + ' | '.join(c.strip().ljust(col_widths[i]) for i, c in enumerate(padded)) + ' |'
        lines.append(line)

    return '\n'.join(lines)


# ─── 4. 统计 ────────────────────────────────────

def stats(text: str) -> dict:
    """字数统计"""
    text_no_code = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    return {
        'total_chars': len(text_no_code),
        'chinese_chars': len(re.findall(r'[\u4e00-\u9fff]', text_no_code)),
        'english_words': len(re.findall(r'[a-zA-Z]+', text_no_code)),
        'lines': text_no_code.count('\n') + 1,
        'paragraphs': len([p for p in text_no_code.split('\n\n') if p.strip()]),
    }


# ─── 5. 目录 ────────────────────────────────────

def generate_toc(text: str) -> str:
    """根据标题生成目录"""
    toc_lines = []
    for line in text.split('\n'):
        m = re.match(r'^(#{1,6})\s+(.+)$', line)
        if m:
            level = len(m.group(1)) - 1
            title = m.group(2).strip()
            indent = '  ' * level
            anchor = re.sub(r'[^\w\u4e00-\u9fff]', '-', title).lower()
            toc_lines.append(f'{indent}- [{title}](#{anchor})')
    return '\n'.join(toc_lines) if toc_lines else "(没有找到标题)"


# ─── 6. 链接 ────────────────────────────────────

def extract_links(text: str) -> list:
    """提取所有 Markdown 链接"""
    links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', text)
    return [{'text': t, 'url': u} for t, u in links]


# ─── 主入口 ─────────────────────────────────────

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(f"用法: {sys.argv[0]} <命令> <文件路径> [选项]")
        print("命令: fix-spacing, to-wechat, table-to-csv, csv-to-table, stats, toc, check-links")
        sys.exit(1)

    cmd = sys.argv[1]
    path = Path(sys.argv[2])

    if not path.exists():
        print(f"文件不存在: {path}")
        sys.exit(1)

    text = path.read_text(encoding='utf-8')

    if cmd == 'fix-spacing':
        result = fix_cn_en_spacing(text)
        out_path = path.with_stem(path.stem + '.formatted')
        Path(out_path).write_text(result, encoding='utf-8')
        print(f"✅ 中英文间距修复完成: {out_path}")

    elif cmd == 'to-wechat':
        html = md_to_wechat(text)
        out_path = path.with_suffix('.wechat.html')
        Path(out_path).write_text(html, encoding='utf-8')
        print(f"✅ 微信公众号格式已生成: {out_path}")

    elif cmd == 'table-to-csv':
        results = tables_to_csv(text)
        if not results:
            print("(没有找到 Markdown 表格)")
        else:
            for r in results:
                out_path = path.with_stem(f"{path.stem}.table{r['table_index']}").with_suffix('.csv')
                Path(out_path).write_text(r['csv'], encoding='utf-8')
                print(f"  ✅ 表格 {r['table_index']} ({r['rows']}×{r['cols']}): {out_path}")

    elif cmd == 'csv-to-table':
        csv_text = path.read_text(encoding='utf-8')
        table = csv_to_table(csv_text)
        out_path = path.with_suffix('.md')
        Path(out_path).write_text(table, encoding='utf-8')
        print(f"✅ CSV 已转为 Markdown 表格: {out_path}")

    elif cmd == 'stats':
        s = stats(text)
        for k, v in s.items():
            print(f"  {k}: {v}")

    elif cmd == 'toc':
        print(generate_toc(text))

    elif cmd == 'check-links':
        links = extract_links(text)
        if links:
            for l in links:
                print(f"  [{l['text']}]({l['url']})")
            print(f"\n共 {len(links)} 个链接")
        else:
            print("(没有找到链接)")

    else:
        print(f"未知命令: {cmd}")
        sys.exit(1)
