#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""meme-digger: 生成单文件 Meme 百科 HTML 页。

用法:
    python make_report.py <工作目录> --out <输出.html> [--title <自定义标题>]

输入: 工作目录下的 报告-*.md (必) + 00~06 分文件(可选) + images/(自动内嵌 base64)
输出: 单个自包含 HTML 文件(内联 CSS、图片 base64 内嵌，零外部依赖)

Markdown 子集: # ## ### #### | 表格 | > 引用 | -/* 列表 | 1. 有序列表
               | ![alt](路径或URL) | **粗体** | [文字](链接) | `代码`
"""
import sys
import os
import re
import base64
import datetime
import html as html_mod

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

EMOJI = {
    "起源": "🌱", "出处": "🌱", "时间线": "🕰", "含义": "💡", "用法": "💬",
    "例句": "🗣", "梗图": "🖼", "衍生": "🌿", "相关": "🌿", "数据": "📊",
    "信源": "🔗", "注意": "⚠️", "概括": "📌", "待考证": "❓",
}


def inline_image(src: str, base_dir: str) -> str:
    """本地图片转 base64 data URI；http(s) 图片原样返回。"""
    if src.startswith(("http://", "https://", "//")):
        if src.startswith("//"):
            return "https:" + src
        return src
    p = src if os.path.isabs(src) else os.path.join(base_dir, src)
    if not os.path.exists(p):
        return ""
    ext = os.path.splitext(p)[1].lower().lstrip(".")
    mime = {"jpg": "image/jpeg", "jpeg": "image/jpeg", "png": "image/png",
            "gif": "image/gif", "webp": "image/webp"}.get(ext, "image/jpeg")
    try:
        with open(p, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
        return f"data:{mime};base64,{b64}"
    except Exception:
        return ""


def inline_text(s: str) -> str:
    """行内格式: **粗体** [链接](url) `代码`"""
    s = html_mod.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)",
               lambda m: f'<a href="{html_mod.escape(m.group(2))}" target="_blank" rel="noopener">{m.group(1)}</a>', s)
    return s


def parse_markdown(text: str, base_dir: str):
    """返回结构化块列表: (type, html_or_data)。"""
    blocks, cur_table, cur_quote, cur_ul, cur_ol = [], [], [], [], []
    in_gallery = False

    def flush():
        if cur_table:
            rows = []
            for i, cells in enumerate(cur_table):
                tag = "th" if i == 0 else "td"
                rows.append("<tr>" + "".join(f"<{tag}>{inline_text(c)}</{tag}>" for c in cells) + "</tr>")
            blocks.append(("table", "<table>" + "".join(rows) + "</table>"))
            cur_table.clear()
        if cur_quote:
            blocks.append(("quote", "".join(cur_quote)))
            cur_quote.clear()
        if cur_ul:
            blocks.append(("ul", "<ul>" + "".join(cur_ul) + "</ul>"))
            cur_ul.clear()
        if cur_ol:
            blocks.append(("ol", "<ol>" + "".join(cur_ol) + "</ol>"))
            cur_ol.clear()

    for raw in text.splitlines():
        line = raw.rstrip()
        if not line.strip():
            flush()
            continue
        # 表格
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
                continue
            cur_table.append(cells)
            continue
        flush()
        # 标题
        m = re.match(r"^(#{1,4})\s+(.*)$", line)
        if m:
            level = len(m.group(1))
            title = m.group(2)
            if level >= 2:
                in_gallery = ("梗图" in title)  # 只在进入新节时重设
            anchor = re.sub(r"[^\w\u4e00-\u9fff]+", "-", title).strip("-")
            icon = next((v for k, v in EMOJI.items() if k in title), "")
            blocks.append(("h", (level, f"{icon} {title}", anchor)))
            continue
        # 引用
        if line.startswith(">"):
            cur_quote.append(f"<blockquote>{inline_text(line.lstrip('>').strip())}</blockquote>")
            continue
        # 列表
        m = re.match(r"^(\s*)[-*]\s+(.*)$", line)
        if m:
            indent = len(m.group(1)) // 2
            if indent == 0:
                cur_ul.append(f"<li>{inline_text(m.group(2))}</li>")
            else:
                cur_ul.append(f"<li class=\"sub\">{inline_text(m.group(2))}</li>")
            continue
        m = re.match(r"^(\s*)\d+\.\s+(.*)$", line)
        if m:
            cur_ol.append(f"<li>{inline_text(m.group(2))}</li>")
            continue
        # 图片
        m = re.match(r"^!\[([^\]]*)\]\(([^)]+)\)\s*(.*)$", line)
        if m:
            alt, src, cap = m.group(1), m.group(2), m.group(3).strip()
            data = inline_image(src, base_dir)
            if data:
                img = (f'<figure class="{"meme" if in_gallery else "img"}">'
                       f'<img src="{data}" alt="{html_mod.escape(alt)}" loading="lazy">'
                       + (f"<figcaption>{inline_text(cap)}</figcaption>" if cap else "")
                       + "</figure>")
                blocks.append(("img", img))
            continue
        # 分隔线
        if re.fullmatch(r"-{3,}", line):
            blocks.append(("hr", "<hr>"))
            continue
        # 普通段落
        blocks.append(("p", f"<p>{inline_text(line)}</p>"))
    flush()
    return blocks


def build_timeline(blocks):
    items = []
    for t, d in blocks:
        if t == "ul":
            for m in re.finditer(r"<li>(?:<strong>)?(\d{4}(?:[-/]\d{1,2})?(?:[-/]\d{1,2})?)[^<]*(?:</strong>)?[:：]?\s*(.*?)</li>", d):
                items.append((m.group(1), re.sub(r"<[^>]+>", "", m.group(2))))
        elif t == "p":
            for m in re.finditer(r"(\d{4}[-/]\d{1,2}(?:[-/]\d{1,2})?)[:：]?\s*([^<]+)", d):
                items.append((m.group(1), m.group(2).strip()))
    return items


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    workdir = sys.argv[1]
    out = None
    title = None
    for i, a in enumerate(sys.argv[2:]):
        if a == "--out" and i + 2 < len(sys.argv): out = sys.argv[i + 3]
        if a == "--title" and i + 2 < len(sys.argv): title = sys.argv[i + 3]
    if not out:
        print("!! 缺少 --out 参数")
        sys.exit(1)

    # 找到报告 md
    report_md = None
    for f in sorted(os.listdir(workdir)):
        if f.startswith("报告-") and f.endswith(".md"):
            report_md = os.path.join(workdir, f)
            break
    if not report_md:
        cands = [f for f in os.listdir(workdir) if f.endswith(".md")]
        if cands:
            report_md = os.path.join(workdir, sorted(cands)[-1])
    if not report_md:
        print(f"!! {workdir} 下没有报告 md 文件")
        sys.exit(1)

    with open(report_md, encoding="utf-8") as f:
        text = f.read()
    blocks = parse_markdown(text, workdir)

    # 提取元信息
    if not title:
        m = re.search(r"^#\s*「(.+?)」", text, re.M)
        title = m.group(1) if m else os.path.basename(workdir)
    summary = next((re.sub(r"<[^>]+>", "", d) for t, d in blocks
                    if t == "p" and d.startswith("<p>")), "")
    timeline = build_timeline(blocks)
    first_date = timeline[0][0] if timeline else ""
    last_date = timeline[-1][0] if timeline else ""
    n_img = sum(1 for t, d in blocks if t == "img" and "meme" in d)

    # 组装正文
    body = []
    toc_items = []
    for t, d in blocks:
        if t == "h":
            level, htitle, anchor = d
            if level == 1:
                continue  # 标题单独渲染
            tag = f"h{level}"
            if level == 2:
                toc_items.append(f'<li><a href="#{anchor}">{htitle}</a></li>')
            body.append(f'<{tag} id="{anchor}" class="section">{"</"+tag+">" if False else ""}')
            # 手动拼: <h2 id=.. class=section>…</h2>
            body[-1] = f'<{tag} id="{anchor}" class="section">{htitle}</{tag}>'
        elif t == "table":
            body.append(d)
        elif t == "quote":
            body.append(d)
        elif t == "ul":
            body.append(d)
        elif t == "ol":
            body.append(d)
        elif t == "img":
            body.append(d)
        elif t == "hr":
            body.append(d)
        elif t == "p":
            body.append(d)
    body_html = "\n".join(body)

    hero_script = """<script>
(function(){
  var reduceMotion=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;var t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}}
  var rnd=mulberry32(42),svg=document.getElementById('hero-lowpoly');
  if(svg){var s='',pts=[];for(var i=0;i<14;i++){pts.push([rnd()*1000,80+rnd()*300])}
    for(var j=1;j<pts.length-1;j++){var col=['232,98,12','214,69,69','194,161,133'][Math.floor(rnd()*3)];
      s+='<polygon points="0,0 '+pts[j][0]+','+pts[j][1]+' '+pts[j+1][0]+','+pts[j+1][1]+'" fill="rgba('+col+',0.10)"/>';
      s+='<polygon points="1000,0 '+pts[j][0]+','+pts[j][1]+' '+pts[j+1][0]+','+pts[j+1][1]+'" fill="rgba('+col+',0.07)"/>';}
    svg.innerHTML=s;}
  var cv=document.getElementById('hero-particles');
  if(cv&&!reduceMotion){var ctx=cv.getContext('2d'),W,H,ps=[];
    function rs(){W=cv.width=cv.offsetWidth;H=cv.height=cv.offsetHeight}rs();addEventListener('resize',rs);
    for(var k=0;k<40;k++){ps.push({x:Math.random()*W,y:Math.random()*H,r:.6+Math.random()*1.6,v:.15+Math.random()*.4,o:.08+Math.random()*.2})}
    (function tick(){ctx.clearRect(0,0,W,H);for(var i=0;i<ps.length;i++){var p=ps[i];p.y-=p.v;p.x+=Math.sin((p.y+p.x)/60)*.15;if(p.y<-4){p.y=H+4;p.x=Math.random()*W}
      ctx.beginPath();ctx.arc(p.x,p.y,p.r,0,7);ctx.fillStyle='rgba(232,98,12,'+p.o+')';ctx.fill();}requestAnimationFrame(tick);})();}
})();
</script>"""

    css = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "..", "templates", "encyclopedia.css"),
               encoding="utf-8").read()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    html_doc = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html_mod.escape(title)} - Meme 百科</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>{css}</style>
</head>
<body>
<header class="hero">
  <canvas id="hero-particles"></canvas>
  <svg class="lowpoly" id="hero-lowpoly" viewBox="0 0 1000 400" preserveAspectRatio="xMidYMid slice" aria-hidden="true"></svg>
  <div class="hero-inner">
    <p class="kicker">MEME DIGGER · 网络梗百科</p>
    <h1>「{html_mod.escape(title)}」</h1>
    <p class="summary">{summary}</p>
    <div class="chips">
      <span class="chip">🌱 最早记录: {first_date or '待考证'}</span>
      <span class="chip">🔥 活跃至: {last_date or '—'}</span>
      <span class="chip">🖼 梗图 {n_img} 张</span>
      <span class="chip">🕐 生成于 {now}</span>
    </div>
  </div>
</header>
<div class="layout">
  <nav class="toc">
    <h3>目录</h3>
    <ul>{''.join(toc_items)}</ul>
    <div class="toc-note">📌 本页由 meme-digger 自动生成<br>单文件 · 图片内嵌 · 可离线阅读</div>
  </nav>
  <main class="content">
{body_html}
    <footer class="footer">
      <hr>
      <p>生成工具: meme-digger skill · 数据来源: B站/贴吧/评论 · 本页为单文件自包含 HTML，图片已 base64 内嵌。</p>
      <p>⚠️ 梗科普仅供参考，争议内容请以原始信源为准。</p>
    </footer>
  </main>
</div>
{hero_script}
</body>
</html>"""

    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html_doc)
    print(f"✅ 已生成: {out}  ({os.path.getsize(out)//1024} KB)")
    print(f"   标题: {title} | 梗图: {n_img} | 时间线: {len(timeline)} 条")


if __name__ == "__main__":
    main()
