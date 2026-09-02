#!/usr/bin/env python3
"""
validate.py — skill-studio 元技能的硬钳校验器

强制力靠脚本不靠词汇（铁律第 2 条）。FAIL 即退出码非 0。
自举：本脚本含错误处理 + 关键数值注释（铁律第 13 条）。

用法:
    python validate.py <skill-folder>
    python validate.py <skill-folder> --json

退出码:
    0 = 全部 PASS
    1 = 有 ERROR（拒出包）
    2 = 仅 WARNING（可出包但提示）
"""

import sys
import os
import re
import json
import py_compile
from pathlib import Path

# === 常量（关键数值，铁律第 13 条要求注释说明原因）===
DESCRIPTION_MAX_CHARS = 80          # 比 Claude 官方 200 字符更严，因 metadata 常驻预算仅 ~100 词
SKILL_MD_WARN_LINES = 500           # 官方建议上限，超此警告
SKILL_MD_REJECT_LINES = 600         # 超此拒出包，强制拆 references/
NAME_MAX_CHARS = 64                 # 官方 name 字段长度上限
RESERVED_WORDS = {                   # 品牌词黑名单，防冒充官方
    'anthropic', 'claude', 'codebuddy', 'workbuddy',
}
NON_VERB_PREFIXES = {                # description 非动词开头黑名单
    'helps', 'is', 'this', 'a', 'an', 'the', 'it', 'are', 'was', 'were',
    'help', 'helping',
}
REQUIRED_FRONTMATTER_FIELDS = {      # YAML frontmatter 必填字段
    'name', 'description',
}
AGENT_CREATED_KEY = 'agent_created'  # SkillManage 可改可删的标志，建议加


def parse_frontmatter(content):
    """手写 YAML frontmatter 解析，避免依赖 PyYAML。"""
    if not content.startswith('---'):
        return None, "missing frontmatter start '---'"
    parts = content.split('---', 2)
    if len(parts) < 3:
        return None, "missing frontmatter end '---'"
    fm_text = parts[1].strip()
    if not fm_text:
        return None, "empty frontmatter"
    result = {}
    for line in fm_text.split('\n'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if ':' not in line:
            continue
        key, _, value = line.partition(':')
        result[key.strip()] = value.strip().strip('"').strip("'")
    return result, None


def check_frontmatter(fm, errors, warnings):
    """校验 frontmatter 格式与必填字段。"""
    if fm is None:
        errors.append(("frontmatter", "MISSING", "frontmatter 不存在或格式错"))
        return
    for field in REQUIRED_FRONTMATTER_FIELDS:
        if field not in fm:
            errors.append((f"frontmatter.{field}", "MISSING", f"必填字段 {field} 缺失"))
        elif not fm[field]:
            errors.append((f"frontmatter.{field}", "EMPTY", f"字段 {field} 为空"))
    if AGENT_CREATED_KEY not in fm:
        warnings.append((AGENT_CREATED_KEY, "MISSING",
                         "建议加 agent_created: true 以便 SkillManage 修改"))


def check_name(fm, skill_dir_name, errors, warnings):
    """校验 name 命名规则。"""
    name = fm.get('name', '') if fm else ''
    if not name:
        return
    if name != skill_dir_name:
        errors.append(("name.match", "MISMATCH",
                       f"name='{name}' 与目录名='{skill_dir_name}' 不一致"))
    if len(name) > NAME_MAX_CHARS:
        errors.append(("name.length", "TOO_LONG",
                       f"name 长度 {len(name)} > {NAME_MAX_CHARS}"))
    if not re.match(r'^[a-z0-9-]+$', name):
        errors.append(("name.charset", "INVALID",
                        "name 只能用小写字母/数字/连字符"))
    if name in RESERVED_WORDS:
        errors.append(("name.reserved", "RESERVED",
                       f"name 命中保留词黑名单: {name}"))


def check_description(fm, errors, warnings):
    """校验 description 字符数 + 动词开头 + 关键词密度 + 占位符。"""
    desc = fm.get('description', '') if fm else ''
    if not desc:
        return
    # 占位符检测（ERROR）：未填的 TODO 模板=没写 description，铁律第3条
    # description 是路由条件不是简介，占位符直接拒出包
    placeholders = ['[todo', 'todo:', '[动词', '[关键词', '[场景', 'placeholder',
                    '填入', '待填', '<', '>']
    desc_lower = desc.lower()
    for ph in placeholders:
        if ph in desc_lower:
            errors.append(("description.placeholder", "TODO",
                          f"description 含占位符 '{ph}'，未实际填写，拒出包（铁律3：description 是路由条件）"))
            break  # 一个占位符触发即可
    if len(desc) > DESCRIPTION_MAX_CHARS:
        errors.append(("description.length", "TOO_LONG",
                       f"description 长度 {len(desc)} > {DESCRIPTION_MAX_CHARS}"))
    words = desc.split()
    first_word = words[0].lower().rstrip(',.') if words else ''
    if first_word in NON_VERB_PREFIXES:
        warnings.append(("description.verb", "NON_VERB",
                         f"description 未动词开头: '{first_word}'，应动词开头+关键词"))
    # 关键词密度启发：长度 <10 视为缺触发关键词
    if len(desc) < 10:
        warnings.append(("description.density", "TOO_SHORT",
                         "description 过短，可能缺触发关键词"))


def check_dependencies(fm, errors, warnings):
    """校验 dependencies 字段格式（如声明）。"""
    deps = fm.get('dependencies', '') if fm else ''
    if not deps:
        return
    # 简单格式校验：列表式应闭合
    if deps.startswith('[') and not deps.endswith(']'):
        errors.append(("dependencies.format", "INVALID",
                       "dependencies 列表未闭合"))


def check_skill_md_lines(skill_md_path, errors, warnings):
    """校验 SKILL.md 行数。"""
    if not skill_md_path.exists():
        errors.append(("skill_md.exists", "MISSING", "SKILL.md 不存在"))
        return
    try:
        with open(skill_md_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except OSError as e:
        errors.append(("skill_md.read", "ERROR", str(e)))
        return
    line_count = len(lines)
    if line_count > SKILL_MD_REJECT_LINES:
        errors.append(("skill_md.lines", "REJECT",
                       f"SKILL.md {line_count} 行 > {SKILL_MD_REJECT_LINES}，拒出包，拆 references/"))
    elif line_count > SKILL_MD_WARN_LINES:
        warnings.append(("skill_md.lines", "WARN",
                         f"SKILL.md {line_count} 行 > {SKILL_MD_WARN_LINES}，建议拆 references/"))


def check_references_used(skill_dir, skill_md_content, errors, warnings):
    """校验 references/ 是否被 SKILL.md 引用。"""
    refs_dir = skill_dir / 'references'
    if not refs_dir.exists() or not refs_dir.is_dir():
        return  # 无 references/ 目录不算错
    refs = [f.name for f in refs_dir.iterdir()
            if f.is_file() and f.name.endswith('.md')]
    if not refs:
        return  # 空目录不算错
    unused = []
    for ref in refs:
        # 检查 SKILL.md 是否提及该文件名或去后缀名
        if ref not in skill_md_content and ref.replace('.md', '') not in skill_md_content:
            unused.append(ref)
    if unused:
        warnings.append(("references.usage", "UNUSED",
                         f"references/ 建了未引用: {unused}"))


def check_scripts_lint(scripts_dir, errors, warnings):
    """快速 lint scripts/ 下的 Python 脚本。"""
    if not scripts_dir.exists() or not scripts_dir.is_dir():
        return
    for script in scripts_dir.glob('*.py'):
        try:
            py_compile.compile(str(script), doraise=True)
        except py_compile.PyCompileError as e:
            errors.append((f"script.{script.name}", "SYNTAX_ERROR", str(e)))


def validate(skill_dir):
    """主校验函数。返回 (errors, warnings)。"""
    errors = []
    warnings = []
    skill_dir = Path(skill_dir).resolve()
    if not skill_dir.is_dir():
        errors.append(("dir.exists", "MISSING", f"目录不存在: {skill_dir}"))
        return errors, warnings

    skill_md_path = skill_dir / 'SKILL.md'
    if not skill_md_path.exists():
        errors.append(("skill_md.exists", "MISSING", "SKILL.md 不存在"))
        return errors, warnings

    try:
        content = skill_md_path.read_text(encoding='utf-8')
    except OSError as e:
        errors.append(("skill_md.read", "ERROR", str(e)))
        return errors, warnings

    fm, fm_err = parse_frontmatter(content)
    if fm_err:
        errors.append(("frontmatter.parse", "ERROR", fm_err))

    check_frontmatter(fm, errors, warnings)
    check_name(fm, skill_dir.name, errors, warnings)
    check_description(fm, errors, warnings)
    check_dependencies(fm, errors, warnings)
    check_skill_md_lines(skill_md_path, errors, warnings)
    check_references_used(skill_dir, content, errors, warnings)
    check_scripts_lint(skill_dir / 'scripts', errors, warnings)

    return errors, warnings


def main():
    if len(sys.argv) < 2:
        print("用法: python validate.py <skill-folder> [--json]")
        sys.exit(1)
    skill_dir = sys.argv[1]
    json_only = '--json' in sys.argv

    try:
        errors, warnings = validate(skill_dir)
    except Exception as e:
        # 兜底错误处理（铁律第 13 条）
        print(f"VALIDATOR_CRASH: {e}", file=sys.stderr)
        sys.exit(1)

    result = {
        "skill": skill_dir,
        "errors": [{"check": e[0], "status": e[1], "message": e[2]} for e in errors],
        "warnings": [{"check": w[0], "status": w[1], "message": w[2]} for w in warnings],
        "summary": f"{len(errors)} error(s), {len(warnings)} warning(s)",
    }

    if json_only:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"=== validate.py 校验报告: {skill_dir} ===")
        print(f"\n{result['summary']}\n")
        if errors:
            print("ERRORS (拒出包):")
            for e in errors:
                print(f"  [ERROR] {e[0]} {e[1]}: {e[2]}")
        if warnings:
            print("\nWARNINGS (可出包但提示):")
            for w in warnings:
                print(f"  [WARN]  {w[0]} {w[1]}: {w[2]}")
        if not errors and not warnings:
            print("ALL PASS")
        print()

    # 退出码：0=PASS，1=有 ERROR，2=仅 WARNING
    if errors:
        sys.exit(1)
    elif warnings:
        sys.exit(2)
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()
