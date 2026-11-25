#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""skill-improver：把评测整改清单变成可执行改造。

硬边界：只补「原本就该有的元信息」，绝不伪造能力。
"""
import argparse
import io
import json
import os
import re
import subprocess
import sys

DEFAULT_REVIEWER = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),)

AUTO_KEYS = {"licensing:no-license", "discoverable:no-ai-index",
             "discoverable:no-triggers", "discoverable:no-links",
             "discoverable:no-tags"}

STOP = {"when", "this", "that", "with", "your", "from", "have", "been", "they",
        "will", "also", "into", "such", "more", "than", "then", "them", "which",
        "should", "using", "used", "there", "their", "about", "after", "before"}


def rd(p):
    return io.open(p, encoding="utf-8").read() if os.path.exists(p) else ""


def wr(p, s):
    io.open(p, "w", encoding="utf-8", newline="\n").write(s)


def fm_of(root):
    body = rd(os.path.join(root, "SKILL.md"))
    m = re.match(r"^---\n(.*?)\n---\n", body, re.S)
    if not m:
        return {}, body
    y = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            y[k.strip()] = v.strip().strip('"').strip("'")
    return y, body


def find_reviewer(explicit):
    if explicit:
        return explicit if os.path.exists(explicit) else None
    here = os.path.dirname(os.path.abspath(__file__))
    pkg_root = os.path.dirname(here)
    sib = os.path.join(os.path.dirname(pkg_root), "lgd-skill-review", "scripts", "review.py")
    return sib if os.path.exists(sib) else None


def fix_license(root, fm):
    p = os.path.join(root, "LICENSE")
    if os.path.exists(p):
        return None
    author = fm.get("author") or "the authors"
    wr(p, "MIT License\n\nCopyright (c) 2026 %s\n\n"
           "Permission is hereby granted, free of charge, to any person obtaining a copy\n"
           "of this software and associated documentation files (the \"Software\"), to deal\n"
           "in the Software without restriction, including without limitation the rights\n"
           "to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
           "copies of the Software, and to permit persons to whom the Software is\n"
           "furnished to do so, subject to the following conditions:\n\n"
           "The above copyright notice and this permission notice shall be included in all\n"
           "copies or substantial portions of the Software.\n\n"
           "THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND.\n" % author)
    return "写入 LICENSE（MIT，作者取自 frontmatter 的 author）"


def fix_ai_index(root, fm):
    p = os.path.join(root, "ai-index.json")
    if os.path.exists(p):
        return None
    desc = fm.get("description") or fm.get("description_zh") or ""
    name = fm.get("name") or os.path.basename(root)
    intents = []
    for seg in re.split(r"[;；。]", desc):
        seg = seg.strip()
        if 4 <= len(seg) <= 60:
            intents.append(seg)
    d = {"name": name, "version": fm.get("version", "0.0.0"),
         "summary": desc[:200],
         "intents": intents[:12] or ["use this skill"],
         "triggers": [name],
         "_generated_by": "skill-improver（从 frontmatter 推导，intents 待人工校订）"}
    wr(p, json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    return "生成 ai-index.json（%d 条 intents，已标注待校订）" % len(d["intents"])


def fix_tags(root, fm, body):
    body = rd(os.path.join(root, "SKILL.md"))
    fm, _ = fm_of(root)
    cur = fm.get("tags", "")
    if len([t for t in cur.split(",") if t.strip()]) >= 3:
        return None
    name = fm.get("name") or os.path.basename(root)
    desc = fm.get("description") or fm.get("description_en") or ""
    cand = [name]
    for w in re.findall(r"[A-Za-z][A-Za-z0-9\-]{5,}", desc):
        wl = w.lower().strip("-")
        if wl in STOP or wl in [c.lower() for c in cand]:
            continue
        cand.append(wl)
        if len(cand) >= 4:
            break
    if len(cand) < 3:
        return None
    tags = ", ".join(cand[:4])
    if cur:
        body2 = re.sub(r"(?m)^tags:.*$", "tags: " + tags, body, count=1)
    else:
        m = re.match(r"^---\n(.*?)\n---\n", body, re.S)
        if not m:
            return None
        body2 = "---\n" + m.group(1) + "\ntags: " + tags + "\n---\n" + body[m.end():]
    wr(os.path.join(root, "SKILL.md"), body2)
    return "补 tags（%s）" % tags


def fix_triggers(root, fm, body):
    body = rd(os.path.join(root, "SKILL.md"))
    if re.search(r"(?m)^#+\s*(Triggers|触发)", body):
        return None
    desc = fm.get("description") or fm.get("description_zh") or ""
    quoted = re.findall(r"「(.{2,30}?)」|\"(.{4,40}?)\"", desc)
    words = [a or b for a, b in quoted][:8]
    if not words:
        words = [w.strip() for w in re.split(r"[，,;；。]", desc)
                 if 2 <= len(w.strip()) <= 60][:8]
    if not words:
        return None
    lines = ["", "## Triggers", "", "适用场景（当用户这样说时启用）：", ""]
    for w in words:
        lines.append("- " + w.strip())
    lines.append("")
    wr(os.path.join(root, "SKILL.md"), body.rstrip() + "\n" + "\n".join(lines))
    return "追加 Triggers 段（%d 条，取自 description）" % len(words)


def fix_links(root, fm, body, siblings):
    body = rd(os.path.join(root, "SKILL.md"))
    if re.search(r"同系列|生态|系列技能", body):
        return None
    if not siblings:
        return None
    lines = ["", "## Related skills", "",
             "本技能属于**同系列技能**，可与下列包组合使用：", ""]
    for s in siblings:
        lines.append("- `%s` — 同系列技能，见同目录兄弟包" % s)
    lines.append("")
    wr(os.path.join(root, "SKILL.md"), body.rstrip() + "\n" + "\n".join(lines))
    return "追加 Related skills 段（%d 个，含「同系列」标识）" % len(siblings)


def fix_doc_drift(root, actions):
    """移除「声明了但没实现」的示例行，留下不含参数名的说明行。"""
    flags = set()
    for a in actions:
        if a.get("key", "").startswith("block:declared_command"):
            for f in re.findall(r"--([a-z0-9\-]+)", a.get("issue", "")):
                flags.add(f)
    if not flags:
        return []
    p = os.path.join(root, "SKILL.md")
    lines = rd(p).splitlines()
    note = ("# [skill-improver] 此处原有一处示例使用了尚未实现的参数，已移除；"
            "实现后请恢复原示例。")
    changed = []
    for i, ln in enumerate(lines):
        if ln.strip() == note:
            continue
        if any(("--" + f) in ln for f in flags):
            lines[i] = note
            changed.append(i + 1)
    if changed:
        wr(p, "\n".join(lines) + "\n")
    return changed


def run_review(reviewer, root):
    p = subprocess.run([sys.executable, reviewer, root, "--run", "--json"],
                       capture_output=True, text=True, encoding="utf-8", timeout=300)
    try:
        obj = json.loads(p.stdout)
    except Exception:
        return None
    return obj


def brief(obj):
    d = (obj or {}).get("data") or {}
    return d.get("total", -1), d.get("verdict", "?"), d.get("actions", [])


def main():
    ap = argparse.ArgumentParser(
        prog="improve.py",
        description="把评测整改清单变成可执行改造。tools: scan（只诊断）、apply（执行改造）")
    sub = ap.add_subparsers(dest="cmd")
    p_scan = sub.add_parser("scan", help="只诊断，不写任何文件")
    p_apply = sub.add_parser("apply", help="执行改造并复测")
    for p in (p_scan, p_apply):
        p.add_argument("package", help="被改造的技能包目录")
        p.add_argument("--fix-doc-drift", action="store_true",
                       help="移除声明了但未实现的示例行（改动既有内容，默认关闭）")
        p.add_argument("--siblings", default="", help="同系列包名，逗号分隔，用于生成互链")
        p.add_argument("--reviewer", default=None, help="评测器脚本路径，默认按同系列约定探测")

    argv = sys.argv[1:]
    if not argv or argv[0] not in ("scan", "apply"):
        argv = ["scan"] + argv
    a = ap.parse_args(argv)

    root = os.path.abspath(a.package)
    if not os.path.isdir(root) or not os.path.exists(os.path.join(root, "SKILL.md")):
        sys.exit("不是可评测的技能包（缺 SKILL.md）：%s" % root)

    reviewer = find_reviewer(a.reviewer)
    if not reviewer:
        sys.exit("找不到评测器。请用 --reviewer 指定 lgd-skill-review/scripts/review.py")

    obj = run_review(reviewer, root)
    if obj is None:
        sys.exit("评测器输出无法解析")
    before, vb, actions = brief(obj)
    fm, body = fm_of(root)

    print("基线：结构制 %d/100 %s" % (before, vb))
    print("整改项 %d 条\n" % len(actions))

    auto, manual = [], []
    for act in actions:
        k = act.get("key", "")
        (auto if k in AUTO_KEYS else manual).append((k, act.get("issue", "")[:70]))

    print("可自动补（%d）：" % len(auto))
    for k, i in auto:
        print("  - %-30s %s" % (k, i))
    print("必须人工（%d）：" % len(manual))
    for k, i in manual:
        print("  - %-30s %s" % (k, i))

    if a.cmd != "apply":
        print("\n（当前是 scan，未改动任何文件；执行改造请用 apply）")
        return

    print("\n执行改造：")
    siblings = [x.strip() for x in a.siblings.split(",") if x.strip()]
    for k, _ in auto:
        if k == "licensing:no-license":
            r = fix_license(root, fm)
        elif k == "discoverable:no-ai-index":
            r = fix_ai_index(root, fm)
        elif k == "discoverable:no-tags":
            r = fix_tags(root, fm, body)
        elif k == "discoverable:no-triggers":
            r = fix_triggers(root, fm, body)
        elif k == "discoverable:no-links":
            r = fix_links(root, fm, body, siblings)
        else:
            r = None
        if r:
            print("  ✓ " + r)

    if a.fix_doc_drift:
        ch = fix_doc_drift(root, actions)
        if ch:
            print("  ✓ 移除未实现参数的示例行：第 %s 行（留了说明行）"
                  % ", ".join(str(x) for x in ch))

    obj2 = run_review(reviewer, root)
    after, va, _ = brief(obj2)
    print("\n复测：结构制 %d/100 %s  →  %d/100 %s   (%+d)"
          % (before, vb, after, va, after - before))
    print("\n仍必须人工的 %d 项未动——自动改造只补元信息，不伪造能力。" % len(manual))


if __name__ == "__main__":
    main()
