#!/usr/bin/env python3
"""
Skill Initializer - 创建符合 skill-studio 规范的 skill 骨架

Usage:
    init_skill.py <skill-name> --path <path> [--pattern <mode>] [--full]

Examples:
    init_skill.py my-skill --path ~/.workbuddy/skills
    init_skill.py api-expert --path skills/public --pattern tool-wrapper
    init_skill.py doc-pipeline --path skills/private --pattern pipeline
    init_skill.py report-gen --path skills/public --full

Patterns (决定建哪些目录，避免"建了不用"反模式):
    tool-wrapper  -> references/
    generator     -> references/ + assets/
    reviewer      -> references/
    inversion    -> assets/
    pipeline      -> references/ + assets/ + scripts/
    (none)        -> references/ (默认最常见)
    --full        -> 全建 references/ + assets/ + scripts/
"""
import sys
import re
from pathlib import Path

# pattern -> 目录映射（渐进式披露：只建该模式需要的目录）
PATTERN_DIRS = {
    "tool-wrapper": ["references"],
    "generator": ["references", "assets"],
    "reviewer": ["references"],
    "inversion": ["references", "assets"],
    "pipeline": ["references", "assets", "scripts"],
}

# pattern -> references 骨架文件（dogfood 改进点1：按 pattern 建对应骨架，引导用户填）
PATTERN_REFERENCES = {
    "generator": [(
        "output-contract.md",
        """# 输出契约

> Generator 模式核心：固定输出结构防漂移。填实际契约后删本 TODO。

## 输出维度（每条必填）

| 维度 | 字段 | 约束 | 示例 |
|---|---|---|---|
| 1. [TODO: 维度名] | [字段] | [约束] | [示例] |
| 2. [TODO] |  |  |  |

## 自检规则（输出前必跑）

- [ ] [TODO: 检查项1]
- [ ] [TODO: 检查项2]

## 典型分配（参考，非死公式）

- [TODO: 如有典型结构，列于此]
"""
    )],
    "reviewer": [(
        "checklist.md",
        """# 审查清单

> Reviewer 模式核心：证据4要素。填实际清单后删本 TODO。

## 证据4要素（每条 finding 必填）

| 要素 | 说明 |
|---|---|
| 位置 | 文件:行号 或 元素定位 |
| 严重度 | ERROR / WARN / INFO |
| 原因 | 为什么是问题 |
| 修复 | 怎么改 |

## 检查项

- [ ] [TODO: 检查项1]
- [ ] [TODO: 检查项2]
"""
    )],
    "inversion": [(
        "interview-script.md",
        """# 访谈脚本

> Inversion 模式核心：阶段化提问，防骚扰上限6。填实际脚本后删本 TODO。

## 阶段化提问（单次最多 6 个问题）

| 阶段 | 目的 | 问题 |
|---|---|---|
| 1. 澄清 | [TODO] | [TODO] |
| 2. 深挖 |  |  |
| 3. 确认 |  |  |

## 防骚扰

- 单次最多 6 个问题
- 用户可随时中断，不追问
"""
    )],
    "pipeline": [(
        "gate-spec.md",
        """# Gate 规格

> Pipeline 模式核心：门槛硬编码。填实际 Gate 后删本 TODO。

## 8要素公式

阶段 = 输入 → 处理 → Gate(硬编码) → 输出

## Gate 定义

| 阶段 | Gate | 判定 | 不通过则 |
|---|---|---|---|
| [TODO] | [TODO] | [TODO] | [TODO] |

## 硬编码 Gate（不靠 prompt 措辞）

- [TODO: 哪些 Gate 用脚本真校验，不靠词汇]
"""
    )],
}

# 保留词黑名单（与 validate.py 一致）
RESERVED = {"anthropic", "claude", "codebuddy", "workbuddy"}

# SKILL.md 行数警戒线（与 validate.py 一致）
WARN_LINES = 500
REJECT_LINES = 600


def safe_print(message):
    """Print message, handling emoji encoding on Windows."""
    try:
        print(message)
    except UnicodeEncodeError:
        import re as _re
        clean = _re.sub(r'[\U0001F300-\U0001F9FF]', '', message)
        print(clean.strip())


if sys.platform == 'win32':
    try:
        if hasattr(sys.stdout, 'reconfigure'):
            sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass


SKILL_TEMPLATE = """---
name: {skill_name}
description: [TODO: 动词开头+做什么+何时用。公式参考："当用户提及[关键词1]、[关键词2]或[场景]时使用"。≤80字]
agent_created: true
---

# {skill_title}

## 何时使用

[TODO: 1-2 句说明触发场景与关键词]

## 标准流程

[TODO: 编号步骤。复杂详节加载 references/，不塞进本文件]

1.
2.
3.

## 铁律

[TODO: 1 行/条，解释挪 references/]

-

## 资源索引

| 文件 | 内容 | 状态 |
|---|---|---|
| `references/` | [TODO] | ⏳ |

## 自举声明

本 SKILL.md 遵守 skill-studio 元技能规范：description ≤80 字+动词开头+关键词；正文 ≤500 行；详节挪 references/；铁律条目化。
"""


def validate_name(skill_name):
    """校验 skill 名称符合规范（与 validate.py 一致）。"""
    if len(skill_name) > 64:
        return False, f"名称超过 64 字符（实际 {len(skill_name)}）"
    if not re.match(r'^[a-z0-9-]+$', skill_name):
        return False, "名称只能含小写字母/数字/连字符"
    if skill_name.startswith('-') or skill_name.endswith('-') or '--' in skill_name:
        return False, "名称不能以连字符开头/结尾或含连续连字符"
    if skill_name in RESERVED:
        return False, f"名称 '{skill_name}' 是保留词"
    return True, "ok"


def title_case(skill_name):
    return ' '.join(w.capitalize() for w in skill_name.split('-'))


def init_skill(skill_name, path, pattern=None, full=False):
    """创建 skill 骨架。返回 skill_dir 或 None。"""
    # 名称校验
    ok, msg = validate_name(skill_name)
    if not ok:
        safe_print(f"❌ 名称校验失败：{msg}")
        safe_print("   规则：小写字母/数字/连字符，≤64 字符，与目录同名，无保留词")
        return None

    # 决定建哪些目录
    if full:
        dirs = ["references", "assets", "scripts"]
    elif pattern:
        if pattern not in PATTERN_DIRS:
            safe_print(f"❌ 未知 pattern: {pattern}")
            safe_print(f"   可选: {', '.join(PATTERN_DIRS.keys())}")
            return None
        dirs = PATTERN_DIRS[pattern]
    else:
        dirs = ["references"]  # 默认最常见

    skill_dir = Path(path).resolve() / skill_name

    # 目录已存在
    if skill_dir.exists():
        safe_print(f"❌ 目录已存在：{skill_dir}")
        return None

    # 创建主目录
    try:
        skill_dir.mkdir(parents=True, exist_ok=False)
        safe_print(f"✅ 创建 skill 目录：{skill_dir}")
    except Exception as e:
        safe_print(f"❌ 创建目录失败：{e}")
        return None

    # 创建 SKILL.md
    skill_title = title_case(skill_name)
    content = SKILL_TEMPLATE.format(skill_name=skill_name, skill_title=skill_title)
    try:
        (skill_dir / 'SKILL.md').write_text(content, encoding='utf-8')
        safe_print("✅ 创建 SKILL.md")
    except Exception as e:
        safe_print(f"❌ 创建 SKILL.md 失败：{e}")
        return None

    # 创建选定目录
    for d in dirs:
        sub = skill_dir / d
        sub.mkdir(exist_ok=True)

        # references/ 且 pattern 有骨架文件：建骨架（不建 .gitkeep）
        if d == 'references' and pattern and pattern in PATTERN_REFERENCES:
            for ref_name, ref_content in PATTERN_REFERENCES[pattern]:
                ref_path = sub / ref_name
                ref_path.write_text(ref_content, encoding='utf-8')
                safe_print(f"✅ 创建 {d}/{ref_name}（骨架，填内容后删 TODO）")
        else:
            # 其他目录建 .gitkeep 占位
            gitkeep = sub / '.gitkeep'
            gitkeep.write_text(
                f"# 占位文件。填入实际内容后删除此文件。\n"
                f"# pattern={pattern or 'default'} 决定建此目录。\n",
                encoding='utf-8'
            )
            safe_print(f"✅ 创建 {d}/")

    # 下一步指引（dogfood 改进点3：按实际建的 dirs 动态生成，不写死 references/assets/scripts/）
    safe_print(f"\n✅ Skill '{skill_name}' 初始化完成")
    safe_print("\n下一步：")
    safe_print("  1. 编辑 SKILL.md，填 TODO（description 用公式：动词+做什么+何时用，≤80字）")
    # 第2步按实际建的目录动态生成
    step2_parts = []
    if pattern and pattern in PATTERN_REFERENCES:
        ref_files = [name for name, _ in PATTERN_REFERENCES[pattern]]
        step2_parts.append(f"填 references/ 骨架文件（{', '.join(ref_files)}），删 TODO")
        # 骨架模式可能还建了 assets/（generator/inversion/pipeline），提示填
        non_ref_dirs = [d for d in dirs if d != 'references']
        if non_ref_dirs:
            step2_parts.append(f"在 {'/'.join(non_ref_dirs)}/ 填素材/模板，删 .gitkeep")
    else:
        # 无骨架 pattern 或默认：按实际建的目录提示
        step2_parts.append(f"在 {'/'.join(dirs)}/ 填实际内容，删 .gitkeep")
    safe_print("  2. " + "；".join(step2_parts))
    safe_print("  3. 运行 validate.py 校验：python validate.py " + str(skill_dir))
    safe_print("  4. 运行 package_skill.py 打包")

    return skill_dir


def main():
    args = sys.argv[1:]
    if len(args) < 3 or args[1] != '--path':
        print("Usage: init_skill.py <skill-name> --path <path> [--pattern <mode>] [--full]")
        print("\nPatterns: " + ", ".join(PATTERN_DIRS.keys()))
        print("\nExamples:")
        print("  init_skill.py my-skill --path ~/.workbuddy/skills")
        print("  init_skill.py api-expert --path skills/public --pattern tool-wrapper")
        print("  init_skill.py doc-pipeline --path skills/private --pattern pipeline")
        sys.exit(1)

    skill_name = args[0]
    path = args[2]
    pattern = None
    full = False

    # 解析可选参数
    for i in range(3, len(args)):
        if args[i] == '--pattern' and i + 1 < len(args):
            pattern = args[i + 1]
        elif args[i] == '--full':
            full = True

    safe_print(f"🚀 初始化 skill: {skill_name}")
    safe_print(f"   位置: {path}")
    if pattern:
        safe_print(f"   模式: {pattern}")
    print()

    result = init_skill(skill_name, path, pattern=pattern, full=full)
    sys.exit(0 if result else 1)


if __name__ == "__main__":
    main()
