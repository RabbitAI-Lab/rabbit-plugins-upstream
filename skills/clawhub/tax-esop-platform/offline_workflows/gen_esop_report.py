#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 ESOP 专题报告：调用闭环引擎产出完整 Markdown，并转 HTML 便于预览。"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from esop_tax_workflow import esop_report  # noqa

OUT_DIR = os.path.join(HERE, "..", "..", "..", "outputs")
os.makedirs(OUT_DIR, exist_ok=True)


def md_to_html(md: str) -> str:
    lines = md.split("\n")
    n = len(lines)
    out = []
    i = 0

    def inline(s: str) -> str:
        s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        return s

    while i < n:
        line = lines[i]
        # 表格
        if line.startswith("|") and i + 1 < n and re.match(r"^\|[\s\-:|]+\|$", lines[i + 1]):
            header = [c.strip() for c in line.strip().strip("|").split("|")]
            i += 2
            rows = []
            while i < n and lines[i].startswith("|") and lines[i].strip() != "":
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            out.append('<table class="rpt"><thead><tr>')
            out.append("".join(f"<th>{inline(c)}</th>" for c in header))
            out.append("</tr></thead><tbody>")
            for r in rows:
                out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
            out.append("</tbody></table>")
            continue
        # 标题
        m = re.match(r"^(#{1,4})\s+(.*)$", line)
        if m:
            lvl = len(m.group(1))
            out.append(f"<h{lvl}>{inline(m.group(2))}</h{lvl}>")
            i += 1
            continue
        # 分隔线
        if line.strip() == "---":
            out.append("<hr/>")
            i += 1
            continue
        # 引用块（合并连续 > 行）
        if line.startswith(">"):
            buf = []
            while i < n and lines[i].startswith(">"):
                buf.append(re.sub(r"^>\s?", "", lines[i]))
                i += 1
            out.append('<blockquote>' + " ".join(inline(b) for b in buf) + "</blockquote>")
            continue
        # 列表
        if line.startswith("- "):
            buf = []
            while i < n and lines[i].startswith("- "):
                buf.append(re.sub(r"^- ", "", lines[i]))
                i += 1
            out.append("<ul>" + "".join(f"<li>{inline(b)}</li>" for b in buf) + "</ul>")
            continue
        # 空行
        if line.strip() == "":
            i += 1
            continue
        # 普通段落
        out.append(f"<p>{inline(line)}</p>")
        i += 1

    return "\n".join(out)


CSS = """
* { box-sizing: border-box; }
body { font-family: "Microsoft YaHei","PingFang SC",system-ui,sans-serif;
  color:#1f2933; background:#f5f7fa; margin:0; padding:32px; }
.wrap { max-width:920px; margin:0 auto; background:#fff; padding:40px 48px;
  border-radius:12px; box-shadow:0 2px 16px rgba(0,0,0,.08); }
h1 { color:#0b5cab; border-bottom:3px solid #0b5cab; padding-bottom:12px; }
h2 { color:#0b5cab; margin-top:32px; border-left:5px solid #0b5cab; padding-left:12px; }
h3 { color:#1f3a5f; }
table.rpt { border-collapse:collapse; width:100%; margin:16px 0; font-size:14px; }
table.rpt th, table.rpt td { border:1px solid #c9d6e3; padding:8px 10px; text-align:left; }
table.rpt th { background:#e8f0fb; color:#0b3d6e; font-weight:600; }
table.rpt tr:nth-child(even) td { background:#f7fafc; }
blockquote { background:#fff8e6; border-left:4px solid #f0a500; margin:16px 0;
  padding:12px 16px; color:#6b5600; border-radius:0 6px 6px 0; }
ul { padding-left:22px; }
li { margin:6px 0; }
hr { border:none; border-top:1px solid #e0e6ed; margin:24px 0; }
.warn { color:#b00020; }
"""

HTML_TPL = """<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><style>{css}</style></head>
<body><div class="wrap">{body}</div></body></html>"""


def main():
    metrics = {"P": 1000, "r_c": 0.25, "G": 500, "company": "示例主体公司"}
    data = esop_report(metrics)
    md = data["report_markdown"]
    title = "员工持股平台投资分回利润税务分析对比专项报告"

    md_path = os.path.join(OUT_DIR, "esop_tax_report.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md)
    print("[OK] markdown ->", md_path)

    html = HTML_TPL.format(title=title, css=CSS, body=md_to_html(md))
    html_path = os.path.join(OUT_DIR, "esop_tax_report.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("[OK] html     ->", html_path)

    rec = data["recommendation"]
    print("[SUMMARY] 最优选择:", rec["primary"])
    if data["transfer"]:
        tr = data["transfer"]
        print("[SUMMARY] 转让环节 有限公司 %.0f%% vs 有限合伙 %.0f%% (省 %.0f 个百分点)" % (
            tr["company_form"]["total_rate"] * 100,
            tr["partnership_form"]["total_rate"] * 100,
            tr["delta_rate"] * 100))


if __name__ == "__main__":
    main()
