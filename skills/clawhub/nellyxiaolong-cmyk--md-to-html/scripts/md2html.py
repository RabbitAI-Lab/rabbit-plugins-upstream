#!/usr/bin/env python3
"""
md-to-html: Convert Markdown files to styled HTML pages.

Usage:
    python3 md2html.py <input.md> [output.html]

If output.html is omitted, defaults to <input>.html in the same directory.
"""

import sys
import os
import re
import html as html_module


def md_to_html(md_text):
    lines = md_text.split('\n')
    html_parts = []
    i = 0

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Horizontal rule
        if stripped == '---':
            html_parts.append('<hr>')
            i += 1
            continue

        # H1
        m = re.match(r'^# (.+)$', stripped)
        if m:
            html_parts.append(f'<h1>{html_module.escape(m.group(1))}</h1>')
            i += 1
            continue

        # H2
        m = re.match(r'^## (.+)$', stripped)
        if m:
            html_parts.append(f'<h2>{html_module.escape(m.group(1))}</h2>')
            i += 1
            continue

        # H3
        m = re.match(r'^### (.+)$', stripped)
        if m:
            html_parts.append(f'<h3>{html_module.escape(m.group(1))}</h3>')
            i += 1
            continue

        # H4
        m = re.match(r'^#### (.+)$', stripped)
        if m:
            html_parts.append(f'<h4>{html_module.escape(m.group(1))}</h4>')
            i += 1
            continue

        # Code block
        if stripped.startswith('```'):
            lang = stripped[3:].strip()
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code_lines.append(lines[i])
                i += 1
            i += 1  # skip closing ```
            code_content = '\n'.join(code_lines)
            html_parts.append(f'<pre><code>{html_module.escape(code_content)}</code></pre>')
            continue

        # Table
        if '|' in stripped:
            if re.match(r'^\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)*\|?$', stripped):
                i += 1
                continue

            table_rows = []
            while i < len(lines) and '|' in lines[i]:
                row_text = lines[i].strip()
                cells = [c.strip() for c in row_text.split('|')]
                if cells and cells[0] == '':
                    cells = cells[1:]
                if cells and cells[-1] == '':
                    cells = cells[:-1]
                table_rows.append(cells)
                i += 1

            if table_rows:
                html_parts.append('<table>')
                if len(table_rows) >= 1:
                    html_parts.append('  <thead>')
                    html_parts.append('    <tr>')
                    for cell in table_rows[0]:
                        html_parts.append(f'      <th>{render_inline(cell)}</th>')
                    html_parts.append('    </tr>')
                    html_parts.append('  </thead>')
                    if len(table_rows) > 1:
                        html_parts.append('  <tbody>')
                        for row in table_rows[1:]:
                            if all(re.match(r'^:?-+:?$', c.strip()) or c.strip() == '' for c in row):
                                continue
                            html_parts.append('    <tr>')
                            for cell in row:
                                html_parts.append(f'      <td>{render_inline(cell)}</td>')
                            html_parts.append('    </tr>')
                        html_parts.append('  </tbody>')
                html_parts.append('</table>')
            continue

        # Unordered list
        m = re.match(r'^(\s*)[-*]\s+(.+)$', stripped)
        if m:
            list_items = []
            while i < len(lines):
                m = re.match(r'^(\s*)[-*]\s+(.+)$', lines[i])
                if not m:
                    break
                list_items.append(m.group(2))
                i += 1
            html_parts.append('<ul>')
            for item in list_items:
                html_parts.append(f'  <li>{render_inline(item)}</li>')
            html_parts.append('</ul>')
            continue

        # Ordered list
        m = re.match(r'^\d+\.\s+(.+)$', stripped)
        if m:
            list_items = []
            while i < len(lines):
                m = re.match(r'^\d+\.\s+(.+)$', lines[i].strip())
                if not m:
                    break
                list_items.append(m.group(1))
                i += 1
            html_parts.append('<ol>')
            for item in list_items:
                html_parts.append(f'  <li>{render_inline(item)}</li>')
            html_parts.append('</ol>')
            continue

        # Blockquote
        if stripped.startswith('>'):
            quote_lines = []
            while i < len(lines) and lines[i].strip().startswith('>'):
                quote_lines.append(lines[i].strip()[1:].strip())
                i += 1
            html_parts.append('<blockquote>')
            html_parts.append(f'  <p>{render_inline(" ".join(quote_lines))}</p>')
            html_parts.append('</blockquote>')
            continue

        # Empty line
        if stripped == '':
            i += 1
            continue

        # Regular paragraph
        para_lines = []
        while i < len(lines) and lines[i].strip() != '' and not lines[i].strip().startswith('#') and not lines[i].strip().startswith('```') and not lines[i].strip().startswith('---') and not ('|' in lines[i] and lines[i].strip().startswith('|')) and not re.match(r'^(\s*)[-*]\s+', lines[i]) and not re.match(r'^\d+\.\s+', lines[i].strip()):
            para_lines.append(lines[i])
            i += 1

        para_text = ' '.join(para_lines).strip()
        if para_text:
            html_parts.append(f'<p>{render_inline(para_text)}</p>')
        continue

    return '\n'.join(html_parts)


def render_inline(text):
    """Render inline Markdown: bold, italic, code."""
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'__(.+?)__', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'`([^`]+?)`', r'<code>\1</code>', text)
    return text


def md_file_to_html(input_path, output_path=None):
    if output_path is None:
        base, _ = os.path.splitext(input_path)
        output_path = base + '.html'

    with open(input_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    body = md_to_html(md_content)

    # Extract title from first H1
    title_match = re.search(r'^# (.+)$', md_content, re.MULTILINE)
    title = title_match.group(1) if title_match else 'Document'

    html_doc = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html_module.escape(title)}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
            max-width: 960px;
            margin: 40px auto;
            padding: 0 24px;
            line-height: 1.7;
            color: #1f2937;
            background: #fff;
        }}
        h1 {{ font-size: 2rem; border-bottom: 2px solid #e5e7eb; padding-bottom: 0.5rem; margin-top: 2rem; }}
        h2 {{ font-size: 1.5rem; border-bottom: 1px solid #e5e7eb; padding-bottom: 0.3rem; margin-top: 1.8rem; }}
        h3 {{ font-size: 1.2rem; margin-top: 1.5rem; color: #374151; }}
        h4 {{ font-size: 1.05rem; margin-top: 1.2rem; color: #4b5563; }}
        table {{ border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.9rem; }}
        th, td {{ border: 1px solid #d1d5db; padding: 8px 12px; text-align: left; }}
        th {{ background: #f3f4f6; font-weight: 600; }}
        tr:nth-child(even) {{ background: #f9fafb; }}
        pre {{ background: #f3f4f6; padding: 16px; border-radius: 8px; overflow-x: auto; font-size: 0.9rem; }}
        code {{ font-family: "SF Mono", "Fira Code", "Consolas", monospace; background: #f3f4f6; padding: 2px 6px; border-radius: 4px; font-size: 0.9em; }}
        pre code {{ background: none; padding: 0; }}
        blockquote {{ border-left: 4px solid #3b82f6; margin: 0; padding-left: 16px; color: #4b5563; }}
        ul, ol {{ padding-left: 1.5rem; }}
        li {{ margin: 0.3rem 0; }}
        hr {{ border: none; border-top: 1px solid #e5e7eb; margin: 2rem 0; }}
        p {{ margin: 0.8rem 0; }}
    </style>
</head>
<body>
{body}
</body>
</html>'''

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_doc)

    return output_path


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 md2html.py <input.md> [output.html]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    result = md_file_to_html(input_file, output_file)
    print(f'✅ Converted: {result}')
