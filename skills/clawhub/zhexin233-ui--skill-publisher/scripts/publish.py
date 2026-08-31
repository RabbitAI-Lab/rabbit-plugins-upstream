#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ClawHub 技能一键发布器 —— 自动化脚本。

流程：校验本地技能包 → 生成中文 PDF 说明 → 发布到 ClawHub → 截图留证 → 汇总输出。
依赖：reportlab（中文用内置 STSong-Light 字体）、clawhub CLI（node）、node + agent-browser（截图）。

Windows 兼容性说明：
- 不再直接 `subprocess(["clawhub", ...])`——Windows 上没有该可执行文件（只有 .bin 下的
  sh 脚本与 node 入口），且 Git Bash 会把 `~`/POSIX 路径翻译出问题。改为定位
  `clawhub/bin/clawdhub.js`，用 `node` 调起（node 接受正斜杠路径，跨平台）。
- 截图优先用 `agent-browser`（node 版，本环境已装），回退到 Python Playwright。
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

SKILL_FILE = "SKILL.md"


def parse_frontmatter(text: str) -> dict:
    """解析 SKILL.md 的 YAML frontmatter（轻量实现，覆盖常见字段）。"""
    meta = {}
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            block = text[3:end].strip()
            for line in block.splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    v = v.strip()
                    if v.startswith("[") and v.endswith("]"):
                        v = [x.strip() for x in v[1:-1].split(",") if x.strip()]
                    meta[k.strip()] = v
    return meta


def validate_skill(skill_dir: Path) -> dict:
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        raise SystemExit(f"✗ 缺少 SKILL.md：{skill_md}")
    text = skill_md.read_text(encoding="utf-8")
    meta = parse_frontmatter(text)
    for field in ("name", "description", "version"):
        if field not in meta:
            print(f"⚠️ frontmatter 缺少字段：{field}")
    print(f"✓ 校验通过：{meta.get('name', '?')} v{meta.get('version', '?')}")
    return meta


def build_pdf(skill_dir: Path, meta: dict, out_path: Path, owner: str = "", slug: str = ""):
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import mm
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.cidfonts import UnicodeCIDFont
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted

    pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
    styles = getSampleStyleSheet()
    base = ParagraphStyle("cn", parent=styles["Normal"], fontName="STSong-Light",
                          fontSize=11, leading=18, spaceAfter=6)
    title = ParagraphStyle("t", parent=base, fontSize=18, spaceAfter=10)
    h2 = ParagraphStyle("h2", parent=base, fontSize=13, spaceBefore=10, spaceAfter=4)
    h3 = ParagraphStyle("h3", parent=base, fontSize=12, spaceBefore=6, spaceAfter=3)
    code = ParagraphStyle("code", parent=base, fontName="STSong-Light", fontSize=9,
                          leading=13, backColor="#f4f4f4", borderPadding=6, spaceAfter=8)

    story = []
    story.append(Paragraph(f"技能说明文档 —— {meta.get('name', '未命名')}", title))
    meta_bits = []
    if meta.get("version"):
        meta_bits.append(f"<b>版本：</b>{meta['version']}")
    if meta.get("slug"):
        meta_bits.append(f"<b>Slug：</b>{meta['slug']}")
    elif slug:
        meta_bits.append(f"<b>Slug：</b>{slug}")
    if meta.get("tags"):
        meta_bits.append(f"<b>标签：</b>{', '.join(meta['tags'])}")
    if meta_bits:
        story.append(Paragraph("　".join(meta_bits), base))
    story.append(Spacer(1, 6))

    # 简介：取自 SKILL.md frontmatter 的 description
    if meta.get("description"):
        story.append(Paragraph("简介", h2))
        story.append(Paragraph(_esc_md(meta["description"]), base))

    # 正文：渲染 SKILL.md 的 Markdown 主体（而非写死发布器文案）
    body = _skill_body(skill_dir / SKILL_FILE)
    if body.strip():
        story.append(Paragraph("详细说明", h2))
        story += _md_to_flowables(body, base, h2, h3, code)

    # 留证信息（仅对已发布技能有意义）
    if owner:
        story.append(Paragraph("发布留证信息", h2))
        story.append(Paragraph(f"发布者账号：<b>@{owner}</b>", base))
        story.append(Paragraph("技能展示网址（已发布生效）：", base))
        story.append(Preformatted(f"https://clawhub.ai/{owner}/skills/{slug}", code))
        story.append(Paragraph("技能已成功发布，页面可公开访问并可通过 npx claw skills install 安装。", base))

    # 发布页截图
    shot = skill_dir / "dist" / "clawhub-page.png"
    if shot.exists():
        story.append(Paragraph("发布页截图留证", h2))
        try:
            from reportlab.platypus import Image
            story.append(Image(str(shot), width=170 * mm, height=95 * mm, kind="proportional"))
        except Exception:
            story.append(Paragraph(f"截图文件：{shot}", base))

    doc = SimpleDocTemplate(str(out_path), pagesize=A4,
                            leftMargin=18 * mm, rightMargin=18 * mm)
    doc.build(story)
    print(f"✓ PDF 已生成：{out_path}")


def _skill_body(skill_md: Path) -> str:
    """读取 SKILL.md 并返回 frontmatter 之后的 Markdown 正文。"""
    if not skill_md.exists():
        return ""
    text = skill_md.read_text(encoding="utf-8")
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4:].strip("\n")
    return text.strip("\n")


def _clean(text: str) -> str:
    """把 STSong-Light（GB 编码）不支持的符号替换为可渲染的等价字符，避免 PDF 出现黑块 ■。

    STSong-Light 覆盖 GB2312/GBK 中文字符与 ASCII，但不含 •、→、×、✓、✅、
    ★、… 及弯引号等符号。
    """
    for k, v in _SANITIZE.items():
        text = text.replace(k, v)
    return text


_SANITIZE = {
    "\u2022": "\u00b7",   # • 项目符号 -> 间隔号·（GB 内含）
    "\u2192": "->",       # → 箭头 -> 文本箭头
    "\u00d7": "x",        # × 乘号 -> x
    "\u2705": "[OK]",     # ✅
    "\u2713": "[OK]",     # ✓
    "\u2605": "*",        # ★
    "\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"',  # 弯引号 -> 直引号
    "\u2026": "...",      # … 省略号
}


def _esc_md(text: str) -> str:
    """转义 XML 特殊字符，并把 **粗体** 与 `行内代码` 转为 reportlab 标记。"""
    text = _clean(text)
    t = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    # 行内代码用红色区分（不再用 Courier，因其不含中文字形会出黑块）
    t = re.sub(r"`([^`]+?)`", r'<font color="#b00020">\1</font>', t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    return t


def _md_to_flowables(text: str, base, h2, h3, code):
    """把 SKILL.md 正文（轻量 Markdown）转成 reportlab flowables。

    支持：## / ### 标题、> 引用、-/* 列表、``` 代码块、| 表格 |、普通段落。
    表格与代码块用等宽 Preformatted 呈现，保证可读且不依赖复杂排版。
    """
    from reportlab.platypus import Paragraph, Preformatted
    story = []
    lines = text.splitlines()
    n = len(lines)
    i = 0
    in_code = False
    code_buf = []

    def flush_code():
        if code_buf:
            story.append(Preformatted(_clean("\n".join(code_buf)), code))
            code_buf.clear()

    while i < n:
        line = lines[i]
        s = line.strip()
        # 代码块围栏：切换状态
        if s.startswith("```"):
            if in_code:
                flush_code()
            in_code = not in_code
            i += 1
            continue
        if in_code:
            code_buf.append(line)
            i += 1
            continue
        if not s:
            i += 1
            continue
        if s.startswith("### "):
            story.append(Paragraph(_esc_md(s[4:]), h3)); i += 1; continue
        if s.startswith("## "):
            story.append(Paragraph(_esc_md(s[3:]), h2)); i += 1; continue
        if s.startswith("# "):
            story.append(Paragraph(_esc_md(s[2:]), h2)); i += 1; continue
        if s.startswith("> "):
            story.append(Paragraph(_esc_md(s[2:]), base)); i += 1; continue
        if s.startswith("- ") or s.startswith("* "):
            story.append(Paragraph("· " + _esc_md(s[2:]), base)); i += 1; continue
        if s.startswith("|") and s.endswith("|"):
            tbl = []
            while i < n and lines[i].strip().startswith("|"):
                row = lines[i].strip()
                if not re.match(r"^\|[\s:|\-]+\|$", row):  # 跳过分隔行
                    tbl.append(row)
                i += 1
            if tbl:
                story.append(Preformatted(_clean("\n".join(tbl)), code))
            continue
        # 普通段落：合并连续的非特殊行
        para = [s]
        j = i + 1
        while j < n:
            nx = lines[j].strip()
            if nx and not nx.startswith(("#", "-", "*", ">", "|", "```")) \
                    and not re.match(r"^\|[\s:|\-]+\|$", nx):
                para.append(nx); j += 1
            else:
                break
        story.append(Paragraph(_esc_md(" ".join(para)), base))
        i = j
    flush_code()
    return story


def ensure_ignore(skill_dir: Path):
    """发布前确保 .clawhubignore 存在并排除构建产物。

    ClawHub 会自动读取 .clawhubignore / .clawdhubignore / .gitignore 排除文件，
    但其 publish 命令没有 --exclude 参数，因此需自行维护忽略规则，避免把
    dist/（PDF、截图等生成产物）随包上传。
    """
    ignore_file = skill_dir / ".clawhubignore"
    default_entries = ["dist/", "*.pdf", "*.png", "*.jpg", "*.jpeg",
                       "node_modules/", ".venv/", "__pycache__/"]
    if ignore_file.exists():
        lines = [l.strip() for l in ignore_file.read_text(encoding="utf-8").splitlines()
                 if l.strip()]
    else:
        lines = []
    added = False
    for entry in default_entries:
        if entry not in lines:
            lines.append(entry)
            added = True
    ignore_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
    verb = "更新" if added else "已存在"
    print(f"✓ .clawhubignore {verb}，已排除：{', '.join(default_entries)}")


def _resolve_node() -> str:
    """定位 node 可执行文件（优先 PATH，再回退常见隔离目录）。"""
    node = shutil.which("node")
    if node:
        return node
    candidates = [
        Path.home() / ".workbuddy" / "binaries" / "node" / "versions" / "22.22.2" / "node.exe",
        Path.home() / ".workbuddy" / "binaries" / "node" / "versions" / "22.22.2" / "bin" / "node",
    ]
    for c in candidates:
        if c.exists():
            return str(c)
    raise SystemExit("✗ 找不到 node，请先安装 Node.js 或将 node 加入 PATH")


def _npm_global_root() -> Path | None:
    """返回 npm 全局模块根（含 clawhub / agent-browser）。"""
    try:
        node = _resolve_node()
        out = subprocess.run([node, "-e",
                              "console.log(require('child_process').execSync('npm root -g').toString().trim())"],
                             capture_output=True, text=True, timeout=30)
        if out.returncode == 0 and out.stdout.strip():
            return Path(out.stdout.strip())
    except Exception:
        pass
    return None


def _resolve_pkg_entry(pkg: str, jsfile: str):
    """跨平台定位一个 npm 包的 JS 入口（如 clawhub/bin/clawdhub.js）。

    返回 (node_path, js_entry_path)；找不到返回 (node, None)。
    """
    node = _resolve_node()
    roots = []
    g = _npm_global_root()
    if g:
        roots.append(g)
    # 已知隔离 workspace
    ws = Path.home() / ".workbuddy" / "binaries" / "node" / "workspace" / "node_modules"
    if ws.exists():
        roots.append(ws)
    # 从 PATH 上的可执行文件反推（clawhub 命令）
    exe = shutil.which(pkg)
    if exe:
        p = Path(exe).resolve()
        for parent in (p.parent, p.parent.parent):
            cand = parent / "node_modules" / pkg / "bin" / jsfile
            if cand.exists():
                roots.insert(0, cand.parent.parent)
                break
    for r in roots:
        entry = r / pkg / "bin" / jsfile
        if entry.exists():
            return node, str(entry)
    return node, None


def publish(skill_dir: Path, slug: str, name: str, token: str, tags: str, version: str):
    node, cli = _resolve_pkg_entry("clawhub", "clawdhub.js")
    if not cli:
        raise SystemExit("✗ 找不到 clawhub 安装（请先 npm install -g clawhub，或在 node workspace 中安装）")
    # 用 node 调起 JS 入口，跨平台且避开 Git Bash 的 /c/ 路径翻译坑
    cmd = [node, cli, "skill", "publish", str(skill_dir),
           "--slug", slug, "--name", name, "--version", version, "--json"]
    if tags:
        cmd += ["--tags", tags]
    env = dict(os.environ)
    if token:
        env["CLAWHUB_TOKEN"] = token
    res = subprocess.run(cmd, capture_output=True, text=True, env=env)
    print(res.stdout)
    if res.returncode != 0:
        print(res.stderr, file=sys.stderr)
        raise SystemExit("✗ 发布失败（可能需要先 clawhub login --token <TOKEN>）")
    try:
        data = json.loads(res.stdout)
        return data.get("url") or f"https://clawhub.ai/<owner>/skills/{slug}"
    except json.JSONDecodeError:
        return f"https://clawhub.ai/<owner>/skills/{slug}"


def _screenshot_with_agent_browser(node: str, ab_js: str, url: str, out_path: Path):
    """用 agent-browser（node）打开页面并截图。

    注意：浏览器运行时必须关掉本地代理（否则 Chromium 报 ERR_NO_SUPPORTED_PROXIES）；
    open 与 screenshot 顺序执行，agent-browser 通过本地状态保持浏览器会话。
    """
    env = dict(os.environ)
    env.pop("HTTPS_PROXY", None)
    env.pop("HTTP_PROXY", None)
    r1 = subprocess.run([node, ab_js, "open", url],
                        capture_output=True, text=True, env=env)
    if r1.returncode != 0:
        print(r1.stderr, file=sys.stderr)
        raise RuntimeError("agent-browser open 失败")
    time.sleep(3)  # 等待页面加载
    r2 = subprocess.run([node, ab_js, "screenshot", str(out_path)],
                        capture_output=True, text=True, env=env)
    if r2.returncode != 0:
        print(r2.stderr, file=sys.stderr)
        raise RuntimeError("agent-browser screenshot 失败")


def screenshot(url: str, out_path: Path):
    # 统一解析为绝对路径：agent-browser 对相对路径的解析在不同 cwd 下不可靠
    out_path = Path(out_path).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    # 优先用 agent-browser（node 版，本环境已装）
    node, ab_js = _resolve_pkg_entry("agent-browser", "agent-browser.js")
    if node and ab_js:
        try:
            _screenshot_with_agent_browser(node, ab_js, url, out_path)
            print(f"✓ 截图已保存：{out_path}")
            return out_path
        except Exception as e:
            print(f"⚠️ agent-browser 截图失败（{e}），尝试回退 Playwright", file=sys.stderr)
    # 回退：Python Playwright
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("⚠️ 未安装 agent-browser 或 Playwright，跳过截图"
              "（可选：npm i -g agent-browser 或 pip install playwright && playwright install chromium）")
        return None
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url, wait_until="networkidle")
        page.screenshot(path=str(out_path), full_page=True)
        browser.close()
    print(f"✓ 截图已保存：{out_path}")
    return out_path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skill", required=True)
    ap.add_argument("--slug", default="")
    ap.add_argument("--name", default="")
    ap.add_argument("--token", default="")
    ap.add_argument("--tags", default="clawhub,publish,automation")
    ap.add_argument("--version", default="")
    ap.add_argument("--owner", default="")
    ap.add_argument("--pdf-only", action="store_true")
    args = ap.parse_args()

    skill_dir = Path(args.skill)
    meta = validate_skill(skill_dir)
    slug = args.slug or meta.get("slug", "my-skill")
    name = args.name or meta.get("name", slug)
    version = args.version or meta.get("version") or "1.0.0"

    out_dir = skill_dir / "dist"
    out_dir.mkdir(exist_ok=True)
    pdf_path = out_dir / f"{slug}.pdf"
    build_pdf(skill_dir, meta, pdf_path, owner=args.owner, slug=slug)

    if args.pdf_only:
        print("✓ 已仅生成 PDF（--pdf-only）。")
        return

    ensure_ignore(skill_dir)
    url = publish(skill_dir, slug, name, args.token, args.tags, version)
    print(f"🔗 技能网址：{url}")
    shot = Path(str(out_dir / "clawhub-page.png"))
    screenshot(url, shot)


if __name__ == "__main__":
    main()
