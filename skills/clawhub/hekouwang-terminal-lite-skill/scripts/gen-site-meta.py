#!/usr/bin/env python3
"""gen-site-meta.py — 站点元数据三合一生成器（feed / badge / sitemap）。

用途：
  从仓库内的真相源（CHANGELOG-OSS.md、VERSION、docs/ 文件树）生成三份派生产物，
  让官网的订阅、版本角标、站点地图不必手维护：

  feed     读 CHANGELOG-OSS.md（解析规则与 gen-site-changelog.py 一致：
           `## [x.y.z] · 标题` 小节 + `- ` 列表项），生成 docs/feed.xml
           （Atom 1.0）。<id> 用站点根；<updated> 取全部条目日期的最新值；
           每条目 <link> 指向 changelog.html#版本号。条目日期取标题里的
           （YYYY-MM-DD），没写日期的条目按运行当天计。
  badge    读 VERSION，把 14 个 HTML（docs 下除 速查卡.html 的全部页面）
           页脚 <!-- BEGIN:GENERATED:VERSION --> … <!-- END:GENERATED:VERSION -->
           标记间内容重写为「会勇禾口王·终端工作台 vX.Y.Z」。标记缺失时自动
           插进页脚 <span class="brand"> 内末尾再写入。
  sitemap  重写 docs/sitemap.xml：URL 按 docs 下实际 html/md 推导
           （404.html 与 速查卡.html 不收录；*/index.html 写成目录 URL），
           lastmod 统一为运行当天。

什么时候重跑（防漂移）：
  改了 CHANGELOG-OSS.md、改了 VERSION、增删了 docs 下页面之后：
      python3 scripts/gen-site-meta.py            # 三件事全做（写文件）
      python3 scripts/gen-site-meta.py --check    # 三件事全查（只比对，不一致 exit 1）
      python3 scripts/gen-site-meta.py feed --check    # 也可分项跑
      python3 scripts/gen-site-meta.py badge --check
      python3 scripts/gen-site-meta.py sitemap --check
"""

import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import quote
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SITE = "https://huiyonghkw.github.io/hekouwang-terminal-lite-skill"

CHANGELOG_SRC = ROOT / "CHANGELOG-OSS.md"
FEED = DOCS / "feed.xml"
SITEMAP = DOCS / "sitemap.xml"
VERSION_FILE = ROOT / "VERSION"

BEGIN_VER = "<!-- BEGIN:GENERATED:VERSION -->"
END_VER = "<!-- END:GENERATED:VERSION -->"
BRAND_TEXT = "会勇禾口王·终端工作台"

# sitemap 不收录：404（错误页不应被收录）、速查卡（付费包 A4 打印页）。
SITEMAP_EXCLUDE = {"404.html", "速查卡.html"}

SEC_RE = re.compile(r"^## \[([0-9][^\]]*)\]\s*·\s*(.+?)\s*$")
DATE_RE = re.compile(r"(20\d{2}-\d{2}-\d{2})")


# ── feed ─────────────────────────────────────────────────────────────────────

def changelog_entries() -> list[dict]:
    """解析 CHANGELOG-OSS.md，返回 [{version, title, date, items}]。"""
    out: list[dict] = []
    cur: dict | None = None
    for line in CHANGELOG_SRC.read_text(encoding="utf-8").splitlines():
        m = SEC_RE.match(line.strip())
        if m:
            if cur:
                out.append(cur)
            title = m.group(2)
            dm = DATE_RE.search(title)
            cur = {
                "version": m.group(1),
                "title": title,
                "date": dm.group(1) if dm else date.today().isoformat(),
                "items": [],
            }
        elif cur and line.startswith("- "):
            cur["items"].append(line[2:].strip())
    if cur:
        out.append(cur)
    return out


def feed_xml() -> str:
    entries = changelog_entries()
    latest = max(e["date"] for e in entries) if entries else date.today().isoformat()
    lines = [
        '<?xml version="1.0" encoding="utf-8"?>',
        '<feed xmlns="http://www.w3.org/2005/Atom">',
        f"  <title>{escape(BRAND_TEXT + ' · 更新日志')}</title>",
        f"  <subtitle>{escape('公开版更新日志：只记你用得到的变化')}</subtitle>",
        f"  <id>{SITE}/</id>",
        f'  <link rel="alternate" href="{SITE}/changelog.html"/>',
        f'  <link rel="self" href="{SITE}/feed.xml"/>',
        f"  <updated>{latest}T00:00:00Z</updated>",
    ]
    for e in entries:
        url = f"{SITE}/changelog.html#{quote(e['version'])}"
        content = "".join(f"<li>{escape(i)}</li>" for i in e["items"])
        lines += [
            "  <entry>",
            f"    <id>{url}</id>",
            f"    <title>{escape(e['version'] + ' · ' + e['title'])}</title>",
            f'    <link rel="alternate" href="{url}"/>',
            f"    <updated>{e['date']}T00:00:00Z</updated>",
            f'    <content type="html">&lt;ul&gt;{content}&lt;/ul&gt;</content>',
            "  </entry>",
        ]
    lines.append("</feed>")
    return "\n".join(lines) + "\n"


def do_feed(check: bool) -> bool:
    want = feed_xml()
    if check:
        if FEED.exists() and FEED.read_text(encoding="utf-8") == want:
            print("✓ feed.xml 与 CHANGELOG-OSS.md 一致")
            return True
        print("✗ feed.xml 与 CHANGELOG-OSS.md 不一致 —— 重跑 scripts/gen-site-meta.py feed")
        return False
    FEED.write_text(want, encoding="utf-8")
    print(f"✓ 已生成 {FEED.relative_to(ROOT)}（{len(changelog_entries())} 个条目，updated={max(e['date'] for e in changelog_entries())}）")
    return True


# ── badge ────────────────────────────────────────────────────────────────────

def badge_pages() -> list[Path]:
    pages = sorted(DOCS.glob("*.html")) + sorted(DOCS.glob("*/*.html"))
    return [p for p in pages if p.name not in SITEMAP_EXCLUDE]


def badge_text(version: str) -> str:
    # 徽章只写版本号：产品名就在旁边 .brand 里，重复一遍会拼成病句。
    # 包一层 .ver-badge：不受 .en/.zh 双语显隐影响，样式见 site.css。
    return f'<span class="ver-badge">v{escape(version)}</span>'


def rewrite_badge(src: str, text: str, rel: str) -> tuple[str, bool]:
    """重写标记间内容；标记缺失则插进页脚 span.brand 末尾。返回 (新内容, 是否成功)。"""
    b = src.find(BEGIN_VER)
    if b != -1:
        e = src.find(END_VER, b)
        if e == -1:
            print(f"✗ {rel}: 有 {BEGIN_VER} 但缺结束标记", file=sys.stderr)
            return src, False
        return src[: b + len(BEGIN_VER)] + text + src[e:], True
    lines = src.splitlines(keepends=True)
    for i, line in enumerate(lines):
        if '© 2026 会勇禾口王 · MIT' in line:
            j = line.rfind("</p>")
            if j == -1:
                break
            tag = f"{BEGIN_VER}{text}{END_VER}"
            lines[i] = line[:j] + tag + line[j:]
            return "".join(lines), True
    print(f"✗ {rel}: 缺版本标记且页脚无 <span class=\"brand\">，拒绝盲写", file=sys.stderr)
    return src, False


def do_badge(check: bool) -> bool:
    version = VERSION_FILE.read_text(encoding="utf-8").strip()
    text = badge_text(version)
    ok = True
    for p in badge_pages():
        rel = str(p.relative_to(ROOT))
        src = p.read_text(encoding="utf-8")
        b = src.find(BEGIN_VER)
        if check:
            if b == -1:
                print(f"✗ {rel}: 缺 {BEGIN_VER} 标记")
                ok = False
                continue
            e = src.find(END_VER, b)
            if src[b + len(BEGIN_VER) : e] == text:
                print(f"✓ {rel}: 版本角标 = {text}")
            else:
                print(f"✗ {rel}: 版本角标与 VERSION ({version}) 不一致")
                ok = False
        else:
            new, good = rewrite_badge(src, text, rel)
            if not good:
                ok = False
                continue
            if new != src:
                p.write_text(new, encoding="utf-8")
                action = "重写" if b != -1 else "插入标记并写入"
                print(f"✓ {rel}: {action} → {text}")
    return ok


# ── sitemap ──────────────────────────────────────────────────────────────────

def sitemap_urls() -> list[str]:
    urls: list[str] = []
    htmls = sorted(DOCS.glob("*.html")) + sorted(DOCS.glob("*/*.html"))
    for p in htmls:
        if p.name in SITEMAP_EXCLUDE:
            continue
        rel = p.relative_to(DOCS).as_posix()
        if p.name == "index.html":
            parent = rel[: -len("index.html")]  # guide/index.html -> guide/
            urls.append(f"{SITE}/{parent}")
        else:
            urls.append(f"{SITE}/{rel}")
    for p in sorted(DOCS.glob("*.md")):
        urls.append(f"{SITE}/{p.name}")
    return urls


def sitemap_xml() -> str:
    today = date.today().isoformat()
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
        "  <!-- 404.html 不列入：错误页不应被搜索引擎收录。速查卡.html 为付费包 A4 打印页。 -->",
    ]
    for u in sitemap_urls():
        lines.append(f"  <url><loc>{u}</loc><lastmod>{today}</lastmod></url>")
    lines.append("</urlset>")
    return "\n".join(lines) + "\n"


def do_sitemap(check: bool) -> bool:
    want = sitemap_xml()
    if check:
        if SITEMAP.exists() and SITEMAP.read_text(encoding="utf-8") == want:
            print(f"✓ sitemap.xml 与 docs 文件树一致（{len(sitemap_urls())} 个 URL，lastmod={date.today().isoformat()}）")
            return True
        print("✗ sitemap.xml 与 docs 文件树不一致 —— 重跑 scripts/gen-site-meta.py sitemap")
        return False
    SITEMAP.write_text(want, encoding="utf-8")
    print(f"✓ 已重写 {SITEMAP.relative_to(ROOT)}（{len(sitemap_urls())} 个 URL，lastmod={date.today().isoformat()}）")
    return True


# ── 入口 ─────────────────────────────────────────────────────────────────────

SUBS = {"feed": do_feed, "badge": do_badge, "sitemap": do_sitemap}


def main() -> int:
    args = sys.argv[1:]
    check = "--check" in args
    subs = [a for a in args if a in SUBS]
    bad = [a for a in args if a not in SUBS and a != "--check"]
    if bad:
        print(f"用法: gen-site-meta.py [feed|badge|sitemap] [--check]（未知参数: {' '.join(bad)}）", file=sys.stderr)
        return 2
    if not subs:
        subs = list(SUBS)
    ok = all(SUBS[s](check) for s in subs)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
