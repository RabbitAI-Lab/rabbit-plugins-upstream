#!/usr/bin/env python3
"""
audit.py — skill-studio 元技能的病灶诊断器

与 validate.py 的分工（铁律第 2 条：强制力靠脚本不靠词汇）:
    validate.py — 发布前硬钳，FAIL 拒出包，检查项少而精（7 项）
    audit.py    — 诊断已有 skill 病灶，输出详细报告，检查项多而广，不拒出包只报告

适用场景（SOP 第 4 节审计入口）:
    - 「重构 skill」「审计 skill」「这个 skill 有问题」→ 跳过诊断，先跑 audit.py 拿病灶清单

用法:
    python audit.py <skill-folder>
    python audit.py <skill-folder> --json
    python audit.py <skill-folder> --severity error   # 只看 ERROR 级

退出码:
    0 = 无病灶
    1 = 有 ERROR 级病灶
    2 = 仅 WARNING / INFO

自举：本脚本含错误处理 + 关键数值注释（铁律第 13 条）。
"""

import sys
import os
import re
import json
import py_compile
from pathlib import Path

# === 常量（关键数值，铁律第 13 条要求注释说明原因）===
DESCRIPTION_MAX_CHARS = 80          # 比 Claude 官方 200 字符更严，metadata 常驻预算 ~100 词
SKILL_MD_WARN_LINES = 500           # 官方建议上限，超此警告
SKILL_MD_REJECT_LINES = 600         # 超此 ERROR，强制拆 references/
NAME_MAX_CHARS = 64                 # 官方 name 字段长度上限
REQUIRED_FRONTMATTER_FIELDS = {'name', 'description'}
AGENT_CREATED_KEY = 'agent_created'
RESERVED_WORDS = {'anthropic', 'claude', 'codebuddy', 'workbuddy'}
NON_VERB_PREFIXES = {'helps', 'is', 'this', 'a', 'an', 'the', 'it', 'are', 'was', 'were', 'help', 'helping'}

# description 路由公式关键词（缺则视为"写成简介不是路由条件"反模式）
ROUTE_FORMULA_KEYWORDS = ['当用户', '触发', '使用', '时使用', 'should be used', 'when']

# 设计哲学词（出现在 SKILL.md 正文视为反模式：哲学应挪 references/）
PHILOSOPHY_WORDS = ['本质是', '哲学', '为什么这么设计', '设计原理', '概念辨析', '底层逻辑',
                    '本质上', '哲学层', 'why we', 'rationale']

# 词汇强制（"MUST reject"/"必须拒绝"等，铁律第 2 条反模式：强制力应靠脚本）
VERBAL_FORCE_WORDS = ['MUST reject', '必须拒绝', 'MUST not', '禁止不', '一定要']

# 寒暄词（铁律第 12 条：面向 Claude 写作，不寒暄）
PLEASANTRY_WORDS = ['好问题', '很高兴帮你', '我来帮你', '让我为你', '当然可以',
                    'good question', 'glad to help', 'let me help']


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


def add_finding(findings, severity, check, message, fix=None):
    """追加一条病灶。severity: ERROR/WARNING/INFO。"""
    findings.append({
        "severity": severity,
        "check": check,
        "message": message,
        "fix": fix or "",
    })


def audit_frontmatter(fm, skill_dir_name, content, findings):
    """审计 frontmatter 格式与字段。"""
    if fm is None:
        add_finding(findings, "ERROR", "frontmatter.missing",
                    "frontmatter 不存在或格式错",
                    "补 YAML frontmatter，含 name + description + agent_created: true")
        return
    for field in REQUIRED_FRONTMATTER_FIELDS:
        if field not in fm:
            add_finding(findings, "ERROR", f"frontmatter.{field}.missing",
                        f"必填字段 {field} 缺失",
                        f"在 frontmatter 加 {field}: <值>")
        elif not fm[field]:
            add_finding(findings, "ERROR", f"frontmatter.{field}.empty",
                        f"字段 {field} 为空")
    if AGENT_CREATED_KEY not in fm:
        add_finding(findings, "WARNING", "frontmatter.agent_created.missing",
                    "缺 agent_created 字段，SkillManage 无法修改此 skill",
                    "加 agent_created: true")


def audit_name(fm, skill_dir_name, findings):
    """审计 name 命名规则。"""
    name = fm.get('name', '') if fm else ''
    if not name:
        return
    if name != skill_dir_name:
        add_finding(findings, "ERROR", "name.mismatch",
                    f"name='{name}' 与目录名='{skill_dir_name}' 不一致",
                    "改 name 或改目录名，二者必须一致")
    if len(name) > NAME_MAX_CHARS:
        add_finding(findings, "ERROR", "name.too_long",
                    f"name 长度 {len(name)} > {NAME_MAX_CHARS}")
    if not re.match(r'^[a-z0-9-]+$', name):
        add_finding(findings, "ERROR", "name.charset",
                    "name 只能用小写字母/数字/连字符")
    if name in RESERVED_WORDS:
        add_finding(findings, "ERROR", "name.reserved",
                    f"name 命中保留词黑名单: {name}")


def audit_description(fm, findings):
    """审计 description（路由条件不是简介）。"""
    desc = fm.get('description', '') if fm else ''
    if not desc:
        return

    # 1. 占位符（ERROR）
    placeholders = ['[todo', 'todo:', '[动词', '[关键词', '[场景',
                    'placeholder', '填入', '待填']
    desc_lower = desc.lower()
    for ph in placeholders:
        if ph in desc_lower:
            add_finding(findings, "ERROR", "description.placeholder",
                        f"description 含占位符 '{ph}'，未实际填写",
                        "用公式填实际值：动词+做什么+何时用，≤80字")
            break

    # 2. 超长（ERROR）
    if len(desc) > DESCRIPTION_MAX_CHARS:
        add_finding(findings, "ERROR", "description.too_long",
                    f"description 长度 {len(desc)} > {DESCRIPTION_MAX_CHARS}",
                    f"精简到 ≤{DESCRIPTION_MAX_CHARS} 字，详节挪 SKILL.md 正文")

    # 3. 非动词开头（WARNING）
    words = desc.split()
    first_word = words[0].lower().rstrip(',.') if words else ''
    if first_word in NON_VERB_PREFIXES:
        add_finding(findings, "WARNING", "description.non_verb",
                    f"description 未动词开头: '{first_word}'",
                    "改成动词开头（生成/诊断/审计/创建...）")

    # 4. 写成简介不是路由条件（WARNING，反模式核心）
    has_route_keyword = any(kw in desc_lower for kw in [k.lower() for k in ROUTE_FORMULA_KEYWORDS])
    if not has_route_keyword:
        add_finding(findings, "WARNING", "description.not_route",
                    "description 缺路由触发关键词，疑似写成简介而非路由条件",
                    "加'当用户提及[关键词]或[场景]时使用'类触发公式")

    # 5. 关键词密度过低（WARNING）
    if len(desc) < 10:
        add_finding(findings, "WARNING", "description.too_short",
                    "description 过短，可能缺触发关键词")


def audit_skill_md_content(skill_md_path, findings):
    """审计 SKILL.md 正文内容（行数/哲学/词汇强制/寒暄）。"""
    if not skill_md_path.exists():
        return
    try:
        with open(skill_md_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            content = ''.join(lines)
    except OSError as e:
        add_finding(findings, "ERROR", "skill_md.read", str(e))
        return

    # 1. 行数（ERROR/WARNING）
    line_count = len(lines)
    if line_count > SKILL_MD_REJECT_LINES:
        add_finding(findings, "ERROR", "skill_md.too_long",
                    f"SKILL.md {line_count} 行 > {SKILL_MD_REJECT_LINES}，重灾区",
                    f"拆 references/，正文压到 ≤{SKILL_MD_WARN_LINES} 行")
    elif line_count > SKILL_MD_WARN_LINES:
        add_finding(findings, "WARNING", "skill_md.long",
                    f"SKILL.md {line_count} 行 > {SKILL_MD_WARN_LINES}，建议拆 references/")

    content_lower = content.lower()

    # 2. 设计哲学词（WARNING：哲学应挪 references/，铁律第 5 条）
    for word in PHILOSOPHY_WORDS:
        if word.lower() in content_lower:
            add_finding(findings, "WARNING", "skill_md.philosophy",
                        f"SKILL.md 含设计哲学词 '{word}'，应挪 references/",
                        f"把 '{word}' 相关段落移到 references/architecture.md")
            break  # 一个即可提示

    # 3. 词汇强制（INFO：铁律第 2 条反模式，强制力应靠脚本）
    for word in VERBAL_FORCE_WORDS:
        if word.lower() in content_lower:
            add_finding(findings, "INFO", "skill_md.verbal_force",
                        f"SKILL.md 含词汇强制 '{word}'，铁律2要求强制力靠脚本",
                        "改成 scripts/validate.py 真校验，措辞可保留但别指望它")
            break

    # 4. 寒暄词（INFO：铁律第 12 条）
    for word in PLEASANTRY_WORDS:
        if word.lower() in content_lower:
            add_finding(findings, "INFO", "skill_md.pleasantry",
                        f"SKILL.md 含寒暄词 '{word}'，面向 Claude 写作不寒暄",
                        "删寒暄，直接给指令")
            break


def audit_references(skill_dir, content, findings):
    """审计 references/ 目录卫生。"""
    refs_dir = skill_dir / 'references'
    if not refs_dir.exists() or not refs_dir.is_dir():
        return

    refs = [f.name for f in refs_dir.iterdir()
            if f.is_file() and f.name.endswith('.md')]

    if not refs:
        # 空目录（可能有 .gitkeep）
        gitkeeps = list(refs_dir.glob('.gitkeep'))
        if gitkeeps:
            add_finding(findings, "WARNING", "references.empty_with_gitkeep",
                        "references/ 仅含 .gitkeep，建了未填内容",
                        "填实际内容后删 .gitkeep，或删整个目录")
        return

    # 1. 建了未引用
    unused = []
    for ref in refs:
        if ref not in content and ref.replace('.md', '') not in content:
            unused.append(ref)
    if unused:
        add_finding(findings, "WARNING", "references.unused",
                    f"references/ 建了未在 SKILL.md 引用: {unused}",
                    "在 SKILL.md 资源索引表加引用，或删未用文件")

    # 2. 引用但文件不存在（SKILL.md 提了文件名但文件没有）
    referenced = re.findall(r'references/([a-zA-Z0-9_-]+\.md)', content)
    for ref in referenced:
        if not (refs_dir / ref).exists():
            add_finding(findings, "ERROR", "references.broken_link",
                        f"SKILL.md 引用 references/{ref} 但文件不存在",
                        f"创建该文件，或删 SKILL.md 中的引用")


def audit_scripts(skill_dir, findings):
    """审计 scripts/ 目录卫生。"""
    scripts_dir = skill_dir / 'scripts'
    if not scripts_dir.exists() or not scripts_dir.is_dir():
        return

    # 1. 语法错（ERROR）
    for script in scripts_dir.glob('*.py'):
        try:
            py_compile.compile(str(script), doraise=True)
        except py_compile.PyCompileError as e:
            add_finding(findings, "ERROR", f"script.{script.name}.syntax",
                        f"脚本语法错: {e}")

    # 2. __pycache__ 残留（WARNING）
    pycache = scripts_dir / '__pycache__'
    if pycache.exists():
        add_finding(findings, "WARNING", "scripts.pycache_residual",
                    "scripts/__pycache__ 残留，不应入包",
                    "删 __pycache__，加 .gitignore")


def audit_dir_hygiene(skill_dir, findings):
    """审计目录卫生（.gitkeep 残留/空目录）。"""
    for d in ['references', 'assets', 'scripts']:
        sub = skill_dir / d
        if not sub.exists():
            continue
        files = [f for f in sub.iterdir() if f.name != '.gitkeep']
        gitkeep = sub / '.gitkeep'
        if gitkeep.exists() and files:
            add_finding(findings, "WARNING", f"dir.{d}.gitkeep_residual",
                        f"{d}/ 已有内容但 .gitkeep 未删",
                        f"删 {d}/.gitkeep")
        if not files and not gitkeep.exists():
            add_finding(findings, "WARNING", f"dir.{d}.empty",
                        f"{d}/ 空目录，建了未用",
                        "填内容或删目录")


def audit(skill_dir):
    """主审计函数。返回 findings 列表。"""
    findings = []
    skill_dir = Path(skill_dir).resolve()
    if not skill_dir.is_dir():
        add_finding(findings, "ERROR", "dir.missing", f"目录不存在: {skill_dir}")
        return findings

    skill_md_path = skill_dir / 'SKILL.md'
    if not skill_md_path.exists():
        add_finding(findings, "ERROR", "skill_md.missing", "SKILL.md 不存在")
        return findings

    try:
        content = skill_md_path.read_text(encoding='utf-8')
    except OSError as e:
        add_finding(findings, "ERROR", "skill_md.read", str(e))
        return findings

    fm, fm_err = parse_frontmatter(content)
    if fm_err:
        add_finding(findings, "ERROR", "frontmatter.parse", fm_err)

    audit_frontmatter(fm, skill_dir.name, content, findings)
    audit_name(fm, skill_dir.name, findings)
    audit_description(fm, findings)
    audit_skill_md_content(skill_md_path, findings)
    audit_references(skill_dir, content, findings)
    audit_scripts(skill_dir, findings)
    audit_dir_hygiene(skill_dir, findings)

    return findings


def print_report(skill_dir, findings, severity_filter=None):
    """打印文本报告。"""
    print(f"=== audit.py 病灶诊断报告: {skill_dir} ===\n")

    # 按严重度分组
    errors = [f for f in findings if f['severity'] == 'ERROR']
    warnings = [f for f in findings if f['severity'] == 'WARNING']
    infos = [f for f in findings if f['severity'] == 'INFO']

    print(f"汇总: {len(errors)} ERROR / {len(warnings)} WARNING / {len(infos)} INFO")
    print(f"总计: {len(findings)} 项病灶\n")

    def show_group(group, label):
        if not group:
            return
        if severity_filter and severity_filter.upper() != label:
            return
        print(f"--- {label} ({len(group)}) ---")
        for i, f in enumerate(group, 1):
            print(f"  [{i}] {f['check']}")
            print(f"      {f['message']}")
            if f['fix']:
                print(f"      修复: {f['fix']}")
        print()

    show_group(errors, "ERROR")
    show_group(warnings, "WARNING")
    show_group(infos, "INFO")

    if not findings:
        print("无病灶，skill 健康。")
    print()


def main():
    if len(sys.argv) < 2:
        print("用法: python audit.py <skill-folder> [--json] [--severity error|warning|info]")
        print("\n与 validate.py 区分:")
        print("  validate.py — 发布前硬钳，FAIL 拒出包，检查项少而精")
        print("  audit.py    — 诊断已有 skill 病灶，输出详细报告，不拒出包")
        sys.exit(1)

    skill_dir = sys.argv[1]
    json_only = '--json' in sys.argv
    severity_filter = None
    if '--severity' in sys.argv:
        idx = sys.argv.index('--severity')
        if idx + 1 < len(sys.argv):
            severity_filter = sys.argv[idx + 1]

    try:
        findings = audit(skill_dir)
    except Exception as e:
        print(f"AUDIT_CRASH: {e}", file=sys.stderr)
        sys.exit(1)

    if json_only:
        result = {
            "skill": skill_dir,
            "findings": findings,
            "summary": {
                "error": sum(1 for f in findings if f['severity'] == 'ERROR'),
                "warning": sum(1 for f in findings if f['severity'] == 'WARNING'),
                "info": sum(1 for f in findings if f['severity'] == 'INFO'),
            },
        }
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print_report(skill_dir, findings, severity_filter)

    # 退出码：0=无病灶，1=有 ERROR，2=仅 WARNING/INFO
    has_error = any(f['severity'] == 'ERROR' for f in findings)
    has_warning = any(f['severity'] in ('WARNING', 'INFO') for f in findings)
    if has_error:
        sys.exit(1)
    elif has_warning:
        sys.exit(2)
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()
