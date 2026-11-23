#!/usr/bin/env python3
"""SkillMedic 自身一致性自检。

一条命令跑完，退出码非 0 表示存在必须修复的问题：
    python tools/check_consistency.py

检查项：
1. 版本号单一事实源——SKILL.md / manifest / CHANGELOG 首条必须一致
2. frontmatter 必填字段与 description 三件套
3. 零 emoji（项目硬性规范）
4. references/ 每篇都被 SKILL.md 引用（防悬空文件永不被读到）
5. chunk-index.yaml 声明的文件都存在
6. SKILL.md 篇幅区间
"""

import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 项目零 emoji 规范：覆盖常见表情与状态符号
EMOJI_RE = re.compile(
    "[\U0001F300-\U0001FAFF\u2600-\u27BF\uFE0F\u2B00-\u2BFF]"
    "|[\u2705\u274C\u26A0\u2B1C\u2714\u2716\u2B50\u26A1]"
)

fails = []
warns = []


def read(rel):
    with io.open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()


def check_version():
    skill_md = read("SKILL.md")
    m = re.search(r"^version:\s*(\S+)", skill_md, re.M)
    if not m:
        fails.append("SKILL.md frontmatter 缺 version")
        return
    ver = m.group(1).strip()

    manifest = read(os.path.join("1-manifest", "skill-manifest.yaml"))
    m2 = re.search(r"^version:\s*(\S+)", manifest, re.M)
    if not m2:
        fails.append("manifest 缺 version")
    elif m2.group(1).strip() != ver:
        fails.append(f"版本不一致：SKILL.md={ver} manifest={m2.group(1).strip()}")

    changelog = read("CHANGELOG.md")
    m3 = re.search(r"^##\s*v(\d+\.\d+\.\d+)", changelog, re.M)
    if not m3:
        fails.append("CHANGELOG 首条版本号解析失败")
    elif m3.group(1) != ver:
        fails.append(f"版本不一致：SKILL.md={ver} CHANGELOG=v{m3.group(1)}")

    return ver


def check_frontmatter():
    content = read("SKILL.md")
    block = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not block:
        fails.append("SKILL.md 缺 frontmatter")
        return
    fm = block.group(1)
    for key in ("name", "version", "description", "license"):
        if not re.search(rf"^{key}:\s*\S", fm, re.M):
            fails.append(f"frontmatter 缺 {key}")
    if "Use when" not in fm:
        fails.append("description 缺触发场景标记 Use when")
    if "Skip for" not in fm:
        fails.append("description 缺排除边界标记 Skip for")


def check_emoji():
    hits = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in (".git", "__pycache__", "tests")]
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            p = os.path.join(dirpath, fn)
            with io.open(p, encoding="utf-8") as f:
                for i, line in enumerate(f, 1):
                    if EMOJI_RE.search(line):
                        rel = os.path.relpath(p, ROOT).replace("\\", "/")
                        hits.append(f"{rel}:{i}")
    for h in hits:
        fails.append(f"emoji 残留 {h}")


def check_references():
    skill_md = read("SKILL.md")
    ref_dir = os.path.join(ROOT, "references")
    if not os.path.isdir(ref_dir):
        return
    for fn in sorted(os.listdir(ref_dir)):
        if not fn.endswith(".md"):
            continue
        if fn not in skill_md:
            fails.append(f"references/{fn} 未在 SKILL.md 中被引用，永远不会被读到")


def check_chunks():
    idx = os.path.join(ROOT, "SKILL.chunks", "chunk-index.yaml")
    if not os.path.isfile(idx):
        warns.append("无 chunk-index.yaml")
        return
    with io.open(idx, encoding="utf-8") as f:
        text = f.read()
    for fn in re.findall(r'file:\s*"([^"]+)"', text):
        p = os.path.join(ROOT, "SKILL.chunks", fn)
        if not os.path.isfile(p):
            fails.append(f"chunk-index 声明的 {fn} 不存在")


def check_length():
    n = len(read("SKILL.md").splitlines())
    if n > 400:
        fails.append(f"SKILL.md {n} 行，超过 400 行上限，应下沉细节")
    elif n > 350:
        warns.append(f"SKILL.md {n} 行，超过建议区间 150-350")
    elif n < 150:
        warns.append(f"SKILL.md 仅 {n} 行，确认是否缺少必需指令")


def main():
    ver = check_version()
    check_frontmatter()
    check_emoji()
    check_references()
    check_chunks()
    check_length()

    print(f"SkillMedic 自检（version={ver}）")
    print("=" * 46)
    for w in warns:
        print(f"[WARN] {w}")
    for f in fails:
        print(f"[FAIL] {f}")
    if not fails and not warns:
        print("[PASS] 全部检查通过")
    elif not fails:
        print(f"\nPASS（{len(warns)} 项 WARN，需人工判断）")
    else:
        print(f"\nFAIL（{len(fails)} 项必须修复）")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
