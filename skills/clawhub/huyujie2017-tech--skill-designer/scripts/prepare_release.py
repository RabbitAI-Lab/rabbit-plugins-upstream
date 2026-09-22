#!/usr/bin/env python3
"""
prepare_release.py — 发布前置转换：把源 SKILL.md 转成 skillhub publish 可接受的发布版

背景（2026-08-31 实战踩坑）：
  skillhub CLI v2026.8.5 的 frontmatter 解析器是 PoC 级，只认「单行 key: value」和
  「key: [a, b]」列表，两个硬约束：
    1. 必须显式含 slug + displayName + SemVer version（_validate_metadata 缺一 die）
    2. description 必须单行——`description: |` 多行块会被解析成字面值 "|"，内容全丢
  而 WorkBuddy 规范（validate_skill.py）用 name + 允许多行 description（| 块更可读）。

  两者契约不同，不能复用同一份 SKILL.md。本脚本从源 SKILL.md 生成一份「发布版」，
  不改源文件，产物写到 dist 发布包，供 skillhub publish 使用。

用法：
    python scripts/prepare_release.py                # 读源 SKILL.md，改写 dist/skill-designer/SKILL.md
    python scripts/prepare_release.py --source-only  # 只打印将生成的发布版 frontmatter，不落盘
    python scripts/prepare_release.py --sync-dist    # 同时按「发布白名单」把源文件同步进 dist

退出码：0 = 成功；1 = 源 frontmatter 解析失败。

发布白名单（v3.12.0 起）：
  只同步 SKILL.md（发布版转换）+ 白名单文件/目录。以下**永不进包**：
  - CHANGELOG*.md（编写过程保密，仅本地留存）
  - bp/（本地工作蓝图）、outputs/ 测试夹具与 .bak（仅白名单点名的 2 份背书文档进包）
  - __pycache__ / *.pyc（SkillHub 拒收二进制）
"""

import argparse
import re
import shutil
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from errors import enable_utf8  # noqa: E402

enable_utf8()  # Windows GBK 控制台下保证中文（含 stderr 报错）不乱码

ROOT = Path(__file__).resolve().parent.parent
DIST_DIR = ROOT / "dist" / "skill-designer"

# 发布白名单：文件逐个点名 + 整目录 + glob。不在名单内的一律不进 dist。
WHITELIST_FILES = [
    "config.json",
    # CHANGELOG.md / CHANGELOG-archive.md 不进发布包（编写过程保密，仅本地留存）
    "outputs/baseline-vs-with-skill.md",
    "outputs/design-to-publish-loop.md",
]
WHITELIST_DIRS = ["references", "example", "library"]
# library/ 必须随包（v3.18.0 阶段 1 起）——理由链：
#   ① references/*.md（共 13 份）已降级为 library/*.json 的**生成物**；
#   ② `knowledge verify` 的 C5 要「md 逐字节等于权威源渲染结果」；
#   ③ 权威源不进包 ⇒ 装机副本的 C5 根本跑不起来（E013 会报「权威源缺失」）；
#   ④ 那就是「源仓库全绿、装机副本空跑」的门禁降级，违反不变量 I4（门禁只增不减）；
#   ⑤ 同时离线完备（I1）也要求现场能重编译——否则现场那份 md 事实上成了不可编辑的孤本。
# 例外：library/staging/ 是吸收流水线 S0 的**隔离区**（开发态草稿），不随包发布。
WHITELIST_EXCLUDE_DIRS = {"staging"}
WHITELIST_GLOBS = ["scripts/*.py", "scripts/*.json"]

# 发布固定坐标（与 config.json 对齐；slug 与 name 不同是历史遗留，保持一致避免开新坑）
# 展示名：优先取源 SKILL.md 的 name-zh（唯一事实源），缺失时才回退到下面的常量。
# 历史教训（2.20.3）：这里曾写死旧展示名，导致手工改名后一跑本脚本就被悄悄回滚。
SLUG = "high-quality-skill-guidance"
DISPLAY_NAME = "高质量skill设计指南"
CATEGORY = "ai-agent"


def parse_frontmatter(text: str):
    """解析 YAML frontmatter（--- 包裹），返回 (fields_dict, body)。兼容多行 description。"""
    m = re.match(r"^---[ \t]*\r?\n(.*?)\r?\n---\r?\n?(.*)$", text, re.DOTALL)
    if not m:
        return None, None
    block, body = m.group(1), m.group(2)
    fields: dict[str, str] = {}
    lines = block.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        km = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$", line)
        if not km:
            i += 1
            continue
        key, val = km.group(1), km.group(2).strip()
        # description 多行块：| 或 >，后续缩进行收集
        if key == "description" and (val == "|" or val == ">" or val.startswith("|") or val.startswith(">")):
            collected = []
            j = i + 1
            while j < len(lines) and (lines[j].startswith("  ") or lines[j].startswith("\t") or not lines[j].strip()):
                if lines[j].strip():
                    collected.append(lines[j].strip())
                j += 1
            fields[key] = "\n".join(collected)
            i = j
            continue
        # 简单标量或列表
        if val.startswith("[") and val.endswith("]"):
            fields[key] = val
        else:
            fields[key] = val.strip().strip('"').strip("'")
        i += 1
    return fields, body


def flatten_description(desc: str) -> str:
    """把多行 description 压成单行（用空格连接），去掉换行。"""
    return re.sub(r"\s*\n\s*", " ", desc).strip()


def make_summary(desc: str) -> str:
    """从 description 生成一句简短 summary（取第一句，截断到首个句号/换行）。"""
    s = desc.strip()
    for sep in ("。", ".", "\n"):
        idx = s.find(sep)
        if idx > 0:
            s = s[:idx + 1]
            break
    # 去掉句中可能残留的换行，控制长度
    s = re.sub(r"\s*\n\s*", " ", s).strip()
    return s


def build_release_frontmatter(fields: dict) -> str:
    """生成发布版 frontmatter：注入 slug/displayName/category，description 单行。

    注意：skillhub CLI 的 _strip_yaml_scalar 只剥首尾引号、不理解 \" 转义，
    因此用单引号包裹（源 description 内只有双引号、无单引号），内部双引号原样保留。
    """
    desc = flatten_description(fields.get("description", ""))
    summary = make_summary(desc)
    out = []
    out.append("---")
    out.append(f"slug: {SLUG}")
    # 展示名单一事实源 = 源 SKILL.md 的 name-zh；源缺该键时才用常量回退
    display_name = fields.get("name-zh", "").strip() or DISPLAY_NAME
    out.append(f"displayName: {display_name}")
    # 服务端额外要求 name 字段（本地 CLI 校验不查，但服务端 SKILL_MD_FRONTMATTER_MISSING 会拒）
    name = fields.get("name", "").strip() or SLUG
    out.append(f"name: {name}")
    out.append(f"version: {fields.get('version', '').strip()}")
    # 单行 + 单引号包裹：内部双引号不转义，避免 CLI 解析出 \"
    out.append(f"description: '{desc}'")
    out.append(f"summary: '{summary}'")
    # 保留其余字段（排除已单独处理的，以及 skillhub 不需要/会冲突的 name 字段）
    skip = {"slug", "displayName", "version", "description", "summary", "name", "name-zh",
            "display-name", "homepage", "argument-hint"}
    order_hint = ["license", "category", "tags", "allowed-tools", "author", "stability", "agent_created"]
    emitted = set()
    for key in order_hint:
        if key in fields and key not in skip and key not in emitted:
            val = fields[key]
            out.append(f"{key}: {val}")
            emitted.add(key)
    # 其余字段按原顺序补
    for key, val in fields.items():
        if key in skip or key in emitted:
            continue
        out.append(f"{key}: {val}")
    # 比 emitted（已发出的**键**）而非 fields 的值：
    # 原写法 `if CATEGORY not in fields` 比的是值，"ai-agent" 永远不是键 → 恒真 → 源里已有 category 时必然重复注入
    if "category" not in emitted:
        out.append(f"category: {CATEGORY}")
    out.append("---")
    return "\n".join(out)


def sync_dist() -> tuple[int, list[str]]:
    """按发布白名单把源文件同步进 dist（幂等：重跑只覆盖变更）。返回 (数量, 相对路径清单)。"""
    copied: list[str] = []
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    targets: list[Path] = []
    for rel in WHITELIST_FILES:
        p = ROOT / rel
        if p.is_file():
            targets.append(p)
    for d in WHITELIST_DIRS:
        base = ROOT / d
        if base.is_dir():
            targets += [p for p in base.rglob("*")
                        if p.is_file() and "__pycache__" not in p.parts
                        and not any(part.startswith("_archive") for part in p.parts)
                        and not (WHITELIST_EXCLUDE_DIRS & set(p.relative_to(base).parts))]
    for pat in WHITELIST_GLOBS:
        targets += [p for p in ROOT.glob(pat) if p.is_file()]
    for src in targets:
        rel = src.relative_to(ROOT)
        dst = DIST_DIR / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        copied.append(str(rel))
    return len(copied), copied


def main() -> int:
    ap = argparse.ArgumentParser(description="发布前置转换：源 SKILL.md → skillhub 发布版")
    ap.add_argument("--source-only", action="store_true", help="只打印将生成的发布版 frontmatter，不落盘")
    ap.add_argument("--sync-dist", action="store_true",
                    help="同时按发布白名单同步源文件进 dist（bp//outputs 夹具/CHANGELOG 不进包）")
    args = ap.parse_args()

    src = ROOT / "SKILL.md"
    text = src.read_text(encoding="utf-8")
    fields, body = parse_frontmatter(text)
    if fields is None:
        print("[prepare_release] 源 SKILL.md frontmatter 解析失败", file=sys.stderr)
        return 1

    fm = build_release_frontmatter(fields)
    release_md = fm + "\n" + body.lstrip("\n")

    if args.source_only:
        print(release_md[:2000])
        return 0

    dst = ROOT / "dist" / "skill-designer" / "SKILL.md"
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(release_md, encoding="utf-8")
    print(f"[prepare_release] 已生成发布版 SKILL.md：{dst}")
    display_name = fields.get("name-zh", "").strip() or DISPLAY_NAME
    print(f"  slug={SLUG}  displayName={display_name}  version={fields.get('version','?').strip()}")
    print(f"  description 单行化：{len(flatten_description(fields.get('description','')))} 字符")

    if args.sync_dist:
        n, files = sync_dist()
        print(f"  [sync-dist] 白名单同步：{n} 个文件已进 dist（bp/ / outputs 夹具 / CHANGELOG 不进包）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
