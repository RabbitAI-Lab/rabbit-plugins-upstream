"""
gen_blueprint_fields.py — 蓝图字段清单的**单一事实源同步器**

背景（DP-204「能引用就别同步——人工同步纪律第三次修改必失效」）：
本 skill 长期存在「两套骨架」——
  · scripts/blocks.py 的 BLOCKS[].fields —— init 与 draft 两条路径共用，机器消费；
  · references/blueprint-template.md 每格的「填空字段」—— 人读模板。
两者内容各自演进 → 实测 **9/10 格存在漂移**（v3.10.0 探测）：v3.6.0 给模板 B01 加了
「资源约束三件套」、v3.7.0 给 B07 加了「④ 分发与安装」，**都没同步进 blocks.py**
→ G1 事故（改一侧忘另一侧）第三次复发。

解法不是再写一条「记得同步」的纪律，而是**建立生成关系**：
  **fields 的事实源 = blocks.py；模板的字段段由本脚本生成（标记包裹，勿手改）。**

用法：
    python scripts/gen_blueprint_fields.py --check     # 只报差异（CI/发布前用）
    python scripts/gen_blueprint_fields.py --write      # 按 blocks.py 重写模板字段段
    python scripts/gen_blueprint_fields.py --emit       # 打印将要写入的字段段（预览）

标记段格式（模板内）：
    <!-- FIELDS:01 BEGIN — 由 scripts/gen_blueprint_fields.py 从 blocks.py 生成，勿手改 -->
    - 前提：______（谁、在什么场景、需要什么）
    <!-- FIELDS:01 END -->
"""

import argparse
import io
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import blocks  # noqa: E402

TEMPLATE = ROOT / "references" / "blueprint-template.md"

BEGIN = "<!-- FIELDS:{bid} BEGIN — 由 scripts/gen_blueprint_fields.py 从 blocks.py 生成，勿手改 -->"
END = "<!-- FIELDS:{bid} END -->"


# ─── 模板侧解析：提取每格已有的字段前缀（用于 --check 比对） ───
def _strip_md(s: str) -> str:
    return s.replace("**", "").replace("`", "").strip()


def _prefix(line: str) -> str:
    """取字段前缀（第一个全角/半角冒号或括号之前），用于「是不是同一个字段」的比对。

    坑位记录：初版正则只写了半角 `:`，切不开中文全角 `：`（B01「资源约束：______」
    整串被当成前缀 → 与模板的「资源约束」判为两个字段，误报一片）。
    比对前统一去空白，避免「采用______模式 / 采用 ______ 模式」这类排版差异。
    """
    raw = line.strip()
    if raw.startswith("#") or raw.startswith("↳"):
        return ""                              # 小节标题 / 提示行：结构件，不是字段
    s = _strip_md(line)
    if re.match(r"^[-|\s:]+$", s):             # 表格分隔行 `|------|`
        return ""
    s = re.sub(r"^[-*]\s+", "", s)
    s = re.sub(r"^\d+[.)]\s+", "", s)          # 有序列表：B07 用 `1. **结构框架 archetype**：…`
    s = re.sub(r"^\|\s*", "", s)               # 表格行：| `## Workflow` | …
    s = s.split("|")[0].strip()                # 表格取第一列
    m = re.match(r"^([^：:（(]+)", s)
    return re.sub(r"\s+", "", m.group(1).strip()) if m else re.sub(r"\s+", "", s[:16])


def template_fields() -> dict[str, list[str]]:
    """按 `## NN-…` 分节，抓「填空字段」标题后的列表/表格行，遇示例段即停。"""
    text = io.open(TEMPLATE, encoding="utf-8").read()
    out: dict[str, list[str]] = {}
    cur = None
    in_fields = False
    in_fence = False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = re.match(r"^## (\d\d)-", line)
        if m:
            cur = m.group(1)
            out.setdefault(cur, [])
            in_fields = False
            continue
        if cur is None:
            continue
        if "填空字段" in line and line.strip().startswith("**"):
            in_fields = True
            continue
        if not in_fields:
            continue
        st = line.strip()
        if st.startswith("<!--"):
            continue                           # 标记段注释：不中断字段段解析
        if st.startswith("**示例") or st.startswith("**填写口径"):
            in_fields = False
            continue
        if not st:
            continue
        if re.match(r"^([-*]\s|\d+[.)]\s|\|)", st):
            if st.startswith("|") and "______" not in st:
                continue                       # 表格表头/分隔行不是字段
            p = _prefix(st)
            if p:
                out[cur].append(p)
        elif line[:1] in (" ", "\t") and st:
            # 缩进续行/子项（emit_block 对 ↳ 提示行与二级字段原样输出，不带 `- `）：
            # 视为字段段延续，只提取能提取的前缀，**绝不终止解析**。
            # 坑位记录：B07 的「   ↳ 建议写…」行曾在这里把 in_fields 置 False，
            # 导致该格从「② 五段章节骨架」起全部误报「模板缺」。
            p = _prefix(st)
            if p:
                out[cur].append(p)
        else:
            in_fields = False
    return out


def code_fields() -> dict[str, list[str]]:
    """代码侧字段前缀；跳过结构/提示行（_prefix 返回空串者）。"""
    return {b["file"][:2]: [p for p in (_prefix(f) for f in b["fields"]) if p]
            for b in blocks.BLOCKS}


def emit_block(b: dict) -> str:
    """生成一格的可读字段段（与 build_block 排版一致：# 小节标题与缩进子项不加 `- `）。"""
    lines = []
    for f in b["fields"]:
        if f.lstrip().startswith("#") or f[:1].isspace():
            lines.append(f)
        else:
            lines.append(f"- {f}")
    return "\n".join(lines)


def write_template() -> int:
    """按 blocks.py 重写（或首次插入）每格的字段标记段。"""
    text = io.open(TEMPLATE, encoding="utf-8").read()
    by_id = {b["file"][:2]: b for b in blocks.BLOCKS}
    changed = 0
    for bid, b in by_id.items():
        seg = f"{BEGIN.format(bid=bid)}\n{emit_block(b)}\n{END.format(bid=bid)}"
        pat = re.compile(
            re.escape(BEGIN.format(bid=bid)) + r".*?" + re.escape(END.format(bid=bid)),
            re.DOTALL,
        )
        if pat.search(text):
            text = pat.sub(lambda _: seg, text, count=1)
            changed += 1
        else:
            # 首次插入：放在该格「**填空字段**：」标题之后，并吃掉原有字段列表行
            m = re.search(rf"(^## {bid}-.*?\*\*填空字段\*\*[^\n]*\n)", text, re.M | re.DOTALL)
            if not m:
                print(f"  ⚠ B{bid} 未找到「填空字段」锚点，跳过")
                continue
            rest = text[m.end():]
            # 复杂格（字段段里夹着表格/代码块，如 B07）：不自动删，避免误伤填写口径
            head = rest[: rest.find("\n## ") if "\n## " in rest else len(rest)]
            if "```" in head or re.search(r"^\|", head, re.M):
                text = text[: m.end()] + "\n" + seg + "\n" + rest
                print(f"  ⚠ B{bid} 字段段含表格/代码块 → 已插入标记段，"
                      f"**原字段行需人工去重**（表格/代码块已保留作填写口径）")
            else:
                lines = rest.split("\n")
                i = 0
                while i < len(lines):
                    st = lines[i].strip()
                    if st == "" or re.match(r"^([-*]\s|\d+[.)]\s)", st) \
                            or (lines[i][:1] in (" ", "\t") and st):
                        i += 1
                    else:
                        break
                text = text[: m.end()] + "\n" + seg + "\n" + "\n".join(lines[i:])
            changed += 1
    io.open(TEMPLATE, "w", encoding="utf-8").write(text)
    print(f"已同步 {changed}/{len(by_id)} 格字段段 → {TEMPLATE.name}")
    return 0


def check() -> int:
    tf, cf = template_fields(), code_fields()
    diffs = 0
    print("=" * 68)
    print("蓝图字段一致性检查（模板 ↔ blocks.py）")
    print("=" * 68)
    for b in blocks.BLOCKS:
        bid = b["file"][:2]
        tpl, code = tf.get(bid, []), cf.get(bid, [])
        only_tpl = [x for x in tpl if x not in code]
        only_code = [x for x in code if x not in tpl]
        if not (only_tpl or only_code):
            continue
        diffs += 1
        print(f"\n[B{bid}] {b['title']}")
        for x in only_tpl:
            print(f"   仅模板有（blocks.py 缺）: {x}")
        for x in only_code:
            print(f"   仅 blocks.py 有（模板缺）: {x}")
    if diffs == 0:
        print("\n✅ 10 格字段清单一致")
        return 0
    print(f"\n❌ {diffs}/{len(blocks.BLOCKS)} 格存在漂移 → 改 blocks.py 后跑 --write 同步")
    return 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="只报差异")
    ap.add_argument("--write", action="store_true", help="按 blocks.py 重写模板字段段")
    ap.add_argument("--emit", action="store_true", help="预览将要生成的字段段")
    args = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    if args.emit:
        for b in blocks.BLOCKS:
            print(f"\n--- B{b['file'][:2]} ---")
            print(emit_block(b))
        return 0
    if args.write:
        return write_template()
    return check()


if __name__ == "__main__":
    sys.exit(main())
