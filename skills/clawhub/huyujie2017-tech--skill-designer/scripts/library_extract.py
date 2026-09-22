#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""library_extract.py — 阶段1 迁移工具：markdown（人工维护）→ 结构化权威源

定位（读完再动）
────────────────────────────────────────────────────────────────────
这是 **ADR-001 阶段 1 措施 1.1 的一次性迁移工具**：把三份「人工维护的 markdown」
抽取为 `library/*.json` 权威源，并把 markdown 的**静态骨架**（说明文字 / 表头 /
索引表 / 映射表）原样切出为 `library/skeleton/*.md`（生成段替换为占位符）。

迁移完成后：
  · **权威源 = library/*.json**（内容），`references/*.md` 降级为**生成物**；
  · 本文件退化为「对照工具」——只在需要回溯旧排版时用，**不进主流程**。

为什么不手抄静态段
────────────────────────────────────────────────────────────────────
静态段（怎么用 / 标签体系 / 旧编号映射 / 准入判据 / 注入协议）合计上万字。
**手抄 = 引入人为笔误**（项目已有的教训：人工同步必然漂移）。
故本工具**按区域切分**：生成段 → 占位符，其余字节原样保留 ⇒ 静态段零损失、可机器复核。

schema（无损原则）
────────────────────────────────────────────────────────────────────
条目 = **结构化元数据 + 原样正文 body**。正文一律原样保存，**不拆字段重组**——
实测条目的正文高度不规则（含表格 / 嵌套列表 / 合并说明段 / 行内加粗被误判为字段），
任何「拆开再拼回」的写法都会丢信息（R5 风险）。元数据只用于索引与检索。

用法
────────────────────────────────────────────────────────────────────
    python scripts/library_extract.py            # 抽取并写 library/
    python scripts/library_extract.py --dry-run  # 只报数，不落盘
"""

from __future__ import annotations

import io
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from knowledge import (  # noqa: E402
    BLOCK_IDS, BLOCK_NAMES, LIBRARY_REL, LESSONS_REL, PRINCIPLES_REL, RE_SHARD,
    SHARD_FMT, RE_DP_HEAD, RE_ENTRY_HEAD, RE_L_HEAD, parse_fields, read_text,
    slice_body, norm_body, first_sentence,
)

LIB_REL = Path("library")
SKEL_REL = LIB_REL / "skeleton"

# 分片头部模板：**手写而非机械替换**。理由：机械把 "B10"→占位、"复盘"→占位 会在
# 「跨任务**复盘**规则（见 ../lessons.md）」这句里误伤——该词在此处不是格名。
# 8 行模板手写 + 全量 diff 复核，比正则替换安全。
SHARD_HEADER_TMPL = """---
加载条件: 引导到 {block} {name}、或按主题命中本格条目时（由 design-blocks-library 索引跳入）。
核心主题: {block} {name} 的设计条目分片（D-NNN 编号，属 design-blocks-library 单一编号空间）
命中标签: [设计条目, {block}, {name}, 积木盘点]
不回答: 逐格引导话术（见 ../designer-guide.md）；跨任务复盘规则（见 ../lessons.md）
---

# {block} {name} — 设计条目分片

> 本片是 [design-blocks-library.md](../design-blocks-library.md)（双索引视图 + 旧编号映射）的**内容分片**，编号同属一个 D-NNN 空间。共 {count} 条（{id_list}）。

{body}
"""


def find_root() -> Path:
    return Path(__file__).resolve().parent.parent


# ───────────────────────────── 正文切片 ─────────────────────────────

def _entry_body(text: str, pos: int) -> str:
    """取条目正文（norm_body 规范化）。pos = 标题行起始偏移。"""
    return norm_body(slice_body(text, pos))


def extract_entries(root: Path) -> list[dict]:
    out: list[dict] = []
    for i, block_id in enumerate(BLOCK_IDS, start=1):
        p = root / RE_SHARD / SHARD_FMT.format(i)
        text = read_text(p)
        for m in RE_ENTRY_HEAD.finditer(text):
            body = _entry_body(text, m.start())
            f = parse_fields(body)
            themes = re.findall(r"\bT(\d{1,2})\b", f.get("主题", "")) or \
                re.findall(r"\bT(\d{1,2})\b", f.get("落位", ""))
            if not themes:      # 兜底：从落位字段的「主题」段取
                themes = re.findall(r"\bT(\d{1,2})\b", f.get("落位", ""))
            tags = re.findall(r"`([^`]+)`", f.get("标签", ""))
            out.append({
                "id": m.group(1),
                "block": block_id,
                "themes": [f"T{t}" for t in dict.fromkeys(themes)],
                "title": m.group(2).strip(),
                "tags": [t.strip() for t in tags if t.strip()],
                "origin": first_sentence(f.get("来源", ""), 120),
                "explains": [],
                "body": body,
            })
    return out


def extract_principles(root: Path) -> list[dict]:
    text = read_text(root / PRINCIPLES_REL)
    out: list[dict] = []
    for m in RE_DP_HEAD.finditer(text):
        body = _entry_body(text, m.start())
        f = parse_fields(body)
        blocks = list(dict.fromkeys(re.findall(r"\bB\d{2}\b", f.get("落地要点", ""))))
        explains = list(dict.fromkeys(re.findall(r"\bD-\d{3}\b", f.get("来源", ""))))
        out.append({
            "id": m.group(1),
            "blocks": blocks,
            "title": m.group(2).strip(),
            "tags": [t.strip() for t in re.split(r"[/、]", f.get("适用场景", "").split("触发信号")[0].lstrip("标签 ").strip()) if t.strip()],
            "origin": first_sentence(f.get("来源", ""), 120),
            "explains": explains,
            "body": body,
        })
    return out


RE_LESSON_STATE = re.compile(r"^-\s*(引用|最近命中|回流)\s*[：:]\s*(.*)$")


def split_lesson_state(body: str) -> tuple[str, dict]:
    """把 **机器状态行**（引用 / 最近命中 / 回流）从正文剥离 → (干净正文, 状态字段)。

    为什么必须在权威源里剥掉（DP-209 权威源唯一化）：
      这些行是 tick 写回的**状态**，不是知识内容。留在 body 里，`refs` 字段与正文的
      「- 引用：N」就是同一事实的两份副本——tick 改一处、渲染读另一处，
      「计数加了但显示没变」在结构上就可能发生。改成「状态=字段、正文=纯知识」后，
      md 完全由字段派生，副本消失。

    幂等：对已经剥离过的正文再跑一次，结果不变（状态行不存在 → 全部保留）。
    """
    st = {"refs": 0, "lastHit": "", "reflow": ""}
    kept: list[str] = []
    for ln in body.split("\n"):
        m = RE_LESSON_STATE.match(ln.strip())
        if not m:
            kept.append(ln)
            continue
        key, val = m.group(1), m.group(2).strip()
        if key == "引用":
            st["refs"] = int(val) if val.isdigit() else 0
        elif key == "最近命中":
            st["lastHit"] = val
        else:
            st["reflow"] = val
    return "\n".join(kept).rstrip(), st


def extract_lessons(root: Path) -> list[dict]:
    text = read_text(root / LESSONS_REL)
    out: list[dict] = []
    for m in RE_L_HEAD.finditer(text):
        raw_body = _entry_body(text, m.start())
        body, st = split_lesson_state(raw_body)
        f = parse_fields(body)
        blocks = list(dict.fromkeys(re.findall(r"\bB\d{2}\b", f.get("触发格", ""))))
        origin = first_sentence(f.get("来源", ""), 120)
        origin = RE_LESSON_STATE.sub("", origin).strip().rstrip("。 ").strip()
        out.append({
            "id": m.group(1),
            "blocks": blocks,
            "title": m.group(2).strip(),
            "origin": origin,
            **st,
            "body": body,
        })
    return out


# ───────────────────────────── 骨架切分 ─────────────────────────────

def _cut(text: str, start_marker: str, end_marker: str) -> tuple[str, str, str]:
    """把 [start_marker, end_marker) 区间换成占位符，返回 (前, 区间, 后)。

    区间内**只保留动态行**、静态行（标题 / 表头 / 分隔线）留下——见调用处按行处理。
    """
    i = text.index(start_marker)
    j = text.index(end_marker, i)
    return text[:i], text[i:j], text[j:]


def skeleton_library(root: Path) -> str:
    """lib 骨架：**逐行最小替换**（只换数据格，不换整表）。

    为什么不做整表替换：视图二的「解决什么」列是**静态文案**，不是派生数据。
    整表替换会把它变成生成物——凭空扩大编译器的责任面（静态文案一旦被生成，
    以后改一句话要改代码）。逐格替换后 diff 精确落在「ID 列表」上，评审范围最小。
    """
    t = read_text(root / LIBRARY_REL)

    # ① 视图一·计数行：只换末尾的条数
    t = re.sub(r"^(\| \*\*(B\d\d)[^*]*\*\* \| \[[^\]]+\]\([^)]+\) \| )\d+( \|)$",
               lambda m: f"{m.group(1)}{{{{{m.group(2)}_COUNT}}}}{m.group(3)}", t, flags=re.M)
    # ② 视图一·ID 行：只换 ID 列表
    t = re.sub(r"^(\| \*\*(B\d\d)\*\* \| ).+( \|)$",
               lambda m: f"{m.group(1)}{{{{{m.group(2)}_IDS}}}}{m.group(3)}", t, flags=re.M)
    # ③ 视图二·主题行：只换 ID 列表，保留「解决什么」
    t = re.sub(r"^(\| \*\*(T\d+)[^*]*\*\* \| ).+?( \| .+)$",
               lambda m: f"{m.group(1)}{{{{{m.group(2)}_IDS}}}}{m.group(3)}", t, flags=re.M)
    # ④ 条目速查表：整表生成（四列全部来自权威源，无静态列）
    t = _replace_table_body(t, "| ID | 名称 | 落位 | 主题 |", "{{QUICK_ROWS}}")
    return t


def _replace_table_body(t: str, header_line: str, placeholder: str) -> str:
    """把以 header_line 开头的表格的**数据行**整段换成占位符（表头与分隔线保留）。"""
    i = t.index(header_line)
    nl1 = t.index("\n", i)          # 表头行末
    nl2 = t.index("\n", nl1 + 1)    # |---| 分隔行末
    j = nl2 + 1
    while j < len(t) and t[j] == "|":
        j = t.index("\n", j) + 1
    return t[:nl2 + 1] + placeholder + "\n" + t[j:]


def skeleton_principles(root: Path) -> str:
    """principles 骨架：**只生成速查表的「支撑条目」列**。

    为什么不整表生成：另外三列是**人工润色的短版本**，与条目区不是派生关系——
    例如 DP-101 速查表「来源」写 `memory-manager-v2`，条目区写 `memory-manager-v2-3.9.0
    的设计切片；支撑条目 …`；「原则（一句话）」也是润色过的（不是 title 或概述首句）。
    整表生成会**丢掉这些文案**（= 功能减弱）。

    唯一真正的派生列是「支撑条目」，而且它现在用的是**旧编号缩写**（`D-027 404 405 407 409`
    即 A-404→D-028 等）——这正是「人工维护派生视图」的漂移源。改由 explains 生成新编号后，
    旧编号映射表仍保留供反查，但速查表不再依赖它。
    """
    text = read_text(root / PRINCIPLES_REL)
    out_lines = []
    for line in text.split("\n"):
        m = re.match(r"^\| (DP-\d{3}) \|", line)
        if m:
            cells = line.split("|")          # ['', ' DP-001 ', ' … ', ' … ', ' … ', ' … ', '']
            if len(cells) >= 7:
                cells[4] = f" {{{{DP{m.group(1)[3:]}_SUPPORTS}}}} "   # 第4列（支撑条目）
                line = "|".join(cells)
        out_lines.append(line)
    t = "\n".join(out_lines)
    i = t.index("## 条目区")
    j = t.index("## 归档区")
    return t[:i] + "## 条目区\n\n{{DP_BODIES}}\n\n" + t[j:]


def skeleton_lessons(root: Path) -> str:
    text = read_text(root / LESSONS_REL)
    i = text.index("## 条目区")
    j = text.index("## 归档区")
    return text[:i] + "## 条目区\n\n{{LESSON_BODIES}}\n\n" + text[j:]


# ───────────────────────────── id 明细压缩 ─────────────────────────────

def compress_ids(ids: list[str]) -> str:
    """连续编号压缩成区间：D-001…D-010、D-127、D-129。

    分片头部原文就是这个形态（`D-001~D-010、**D-127**、…`），复现它可让 diff 最小；
    同时**去掉加粗**——加粗是「新条目」的视觉标记，而它正是本项目 grep 漏匹配的
    坑源头（记忆里记过）；新条目信息改由 CHANGELOG 与 ID 区间本身承载。
    """
    def num(s: str) -> int:
        return int(re.sub(r"\D", "", s))

    prefix = "D-"
    rendered: list[str] = []
    i = 0
    while i < len(ids):
        j = i
        while j + 1 < len(ids) and num(ids[j + 1]) == num(ids[j]) + 1:
            j += 1
        if j - i >= 2:
            rendered.append(f"{ids[i]}~{ids[j]}")
        elif j - i == 1:
            rendered.extend([ids[i], ids[j]])
        else:
            rendered.append(ids[i])
        i = j + 1
    return "、".join(rendered)


# ───────────────────────────── 主流程 ─────────────────────────────

def main(argv=None) -> int:
    dry = "--dry-run" in (argv or sys.argv)
    root = find_root()
    lib = root / LIB_REL
    skel = root / SKEL_REL

    entries = extract_entries(root)
    principles = extract_principles(root)
    lessons = extract_lessons(root)

    print("=== 抽取结果 ===")
    print(f"  entries    {len(entries):>4} 条")
    print(f"  principles {len(principles):>4} 条")
    print(f"  lessons    {len(lessons):>4} 条")
    for i, b in enumerate(BLOCK_IDS, start=1):
        n = sum(1 for e in entries if e["block"] == b)
        print(f"    {b} {BLOCK_NAMES[b]:<4} {n:>3}")

    # 头部「共 N 条（明细）」的 id_list 复核
    print("\n=== 分片头部 id 明细压缩复核（应与原文一致，除加粗）===")
    for i, b in enumerate(BLOCK_IDS, start=1):
        ids = [e["id"] for e in entries if e["block"] == b]
        print(f"    {b} 共 {len(ids)} 条（{compress_ids(ids)}）")

    if dry:
        print("\n[dry-run] 未落盘")
        return 0

    lib.mkdir(parents=True, exist_ok=True)
    skel.mkdir(parents=True, exist_ok=True)

    def dump(name: str, obj) -> None:
        p = lib / name
        with io.open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps(obj, ensure_ascii=False, indent=1) + "\n")
        print(f"  ✅ {p.relative_to(root)}  {p.stat().st_size / 1024:.1f} KB")

    print("\n=== 写权威源 ===")
    dump("entries.json", {"schemaVersion": "1.0", "kind": "entry", "entries": entries})
    dump("principles.json", {"schemaVersion": "1.0", "kind": "principle", "entries": principles})
    dump("lessons.json", {"schemaVersion": "1.0", "kind": "lesson", "entries": lessons})

    print("\n=== 写骨架（静态段原样保留，生成段占位）===")
    (skel / "design-blocks-library.md").write_text(skeleton_library(root), encoding="utf-8", newline="\n")
    print("  ✅ library/skeleton/design-blocks-library.md")
    (skel / "design-principles-library.md").write_text(skeleton_principles(root), encoding="utf-8", newline="\n")
    print("  ✅ library/skeleton/design-principles-library.md")
    (skel / "lessons.md").write_text(skeleton_lessons(root), encoding="utf-8", newline="\n")
    print("  ✅ library/skeleton/lessons.md")
    (skel / "shard.md").write_text(SHARD_HEADER_TMPL, encoding="utf-8", newline="\n")
    print("  ✅ library/skeleton/shard.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
