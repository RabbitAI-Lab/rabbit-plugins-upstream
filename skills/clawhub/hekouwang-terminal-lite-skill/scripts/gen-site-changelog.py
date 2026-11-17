#!/usr/bin/env python3
"""gen-site-changelog.py — 把 CHANGELOG-OSS.md 转成 docs/changelog.html 的更新日志条目。

用途：
  解析 CHANGELOG-OSS.md 的 `## [x.y.z] · 标题` 小节与其下的 `- ` 列表项，转成
  <h2> / <ul><li> 片段（无列表的正文段转 <p>；反引号转 <code>；其余 markdown
  语法不处理），写入 docs/changelog.html 中
  <!-- BEGIN:GENERATED:CHANGELOG --> … <!-- END:GENERATED:CHANGELOG -->（或
  <!-- END -->）标记之间。CHANGELOG-OSS.md 是唯一真相源，公开页只是它的镜像。

什么时候重跑（防漂移）：
  往 CHANGELOG-OSS.md 加了新版本小节或改了条目之后，重跑一次让公开页跟上：
      python3 scripts/gen-site-changelog.py            # 原地重写标记间内容
      python3 scripts/gen-site-changelog.py --check    # 只检查，不一致 exit 1
  ⛔ 标记不存在时直接报错退出，绝不盲写 —— 标记由 HTML 维护方负责插入。
"""

import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "CHANGELOG-OSS.md"
TARGET = ROOT / "docs" / "changelog.html"

BEGIN = "<!-- BEGIN:GENERATED:CHANGELOG -->"
ENDS = ("<!-- END:GENERATED:CHANGELOG -->", "<!-- END -->")

SEC_RE = re.compile(r"^## \[([0-9][^\]]*)\]\s*·\s*(.+?)\s*$")


def inline(md: str) -> str:
    """HTML 转义 + 反引号转 <code>；其余 markdown 语法不处理。"""
    out = html.escape(md, quote=False)
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", out)


def parse(md: str) -> list[str]:
    blocks: list[str] = []
    title: tuple[str, str] | None = None  # (版本, 标题)
    items: list[str] = []
    paras: list[str] = []

    def flush():
        nonlocal title, items, paras
        if not title:
            return
        parts = [f"<h2>{inline(title[0])} · {inline(title[1])}</h2>"]
        if items:
            parts.append("<ul>")
            parts += [f"<li>{inline(i)}</li>" for i in items]
            parts.append("</ul>")
        for p in paras:
            parts.append(f"<p>{inline(p)}</p>")
        blocks.append("\n".join(parts))
        items, paras = [], []

    for line in md.splitlines():
        m = SEC_RE.match(line.strip())
        if m:
            flush()
            title = (m.group(1), m.group(2))
        elif title and line.startswith("- "):
            items.append(line[2:].strip())
        elif title and line.strip() and not line.startswith((">", "---", "#")):
            paras.append(line.strip())
    flush()
    return blocks


def generate() -> str:
    return "\n\n".join(parse(SRC.read_text(encoding="utf-8")))


def locate(src: str) -> tuple[int, int] | None:
    b = src.find(BEGIN)
    if b == -1:
        return None
    b += len(BEGIN)
    for end in ENDS:
        e = src.find(end, b)
        if e != -1:
            return b, e
    return None


def main() -> int:
    src = TARGET.read_text(encoding="utf-8")
    block = generate()
    span = locate(src)
    if "--check" in sys.argv[1:]:
        if span is None:
            print(f"✗ {TARGET.relative_to(ROOT)} 缺少 {BEGIN} / 结束标记 —— 先插标记再跑 --check")
            return 1
        if src[span[0]:span[1]].strip() == block.strip():
            print(f"✓ {TARGET.relative_to(ROOT)} 更新日志与 CHANGELOG-OSS.md 一致")
            return 0
        print(f"✗ {TARGET.relative_to(ROOT)} 更新日志与 CHANGELOG-OSS.md 不一致 —— 重跑 scripts/gen-site-changelog.py 重写")
        return 1

    if span is None:
        print(f"✗ {TARGET.relative_to(ROOT)} 缺少 {BEGIN} / 结束标记，拒绝盲写 —— 标记由 HTML 维护方插入", file=sys.stderr)
        return 1
    out = src[:span[0]] + "\n" + block + "\n" + src[span[1]:]
    TARGET.write_text(out, encoding="utf-8")
    n = block.count("<h2>")
    print(f"✓ 已重写 {TARGET.relative_to(ROOT)} 标记间内容（{n} 个版本小节）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
