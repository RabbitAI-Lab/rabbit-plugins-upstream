#!/usr/bin/env python3
"""
Skill Manager Audit Script
扫描所有 skill 目录，检测问题并生成结构化报告。
用法: python audit.py [--user <path>] [--project <path>] [--json] [--fix]
"""

import os
import sys
import json
import re
import argparse
from pathlib import Path
from collections import defaultdict

# Fix encoding issues on Windows
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

def parse_frontmatter(filepath):
    """解析 SKILL.md 的 YAML frontmatter（简易解析器，无需 pyyaml）"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return None

    # 匹配 frontmatter
    fm_match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        return None

    fm_text = fm_match.group(1)
    result = {}
    current_key = None

    for line in fm_text.split('\n'):
        # 跳过空行和注释
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue

        # 检查是否是新的 key: value
        kv_match = re.match(r'^(\w[\w-]*)\s*:\s*(.*)', line)
        if kv_match:
            current_key = kv_match.group(1)
            value = kv_match.group(2).strip()
            # 去除引号
            if value and value[0] in '"\'' and value[-1] in '"\'"':
                value = value[1:-1]
            result[current_key] = value
            continue

        # 多行值（缩进行）
        if current_key and line.startswith(' ') and current_key in result:
            result[current_key] += ' ' + stripped

    return result


def scan_directory(skill_dir, source_name):
    """扫描一个 skill 目录，返回 skill 列表"""
    skills = []
    if not os.path.isdir(skill_dir):
        return skills

    for entry in sorted(os.listdir(skill_dir)):
        entry_path = os.path.join(skill_dir, entry)

        # 跳过非目录
        if not os.path.isdir(entry_path):
            continue

        # 跳过隐藏目录
        if entry.startswith('.'):
            continue

        skill = {
            'dir_name': entry,
            'path': entry_path,
            'source': source_name,
            'issues': [],
            'level': 'ok',
        }

        # 检查 SKILL.md
        skill_md = os.path.join(entry_path, 'SKILL.md')
        if not os.path.exists(skill_md):
            skill['issues'].append({
                'severity': 'P0',
                'type': 'missing_skill_md',
                'message': '缺少 SKILL.md — 目录可能已损坏',
            })
            skill['level'] = 'P0'
            skills.append(skill)
            continue

        # 解析 frontmatter
        fm = parse_frontmatter(skill_md)
        skill['frontmatter'] = fm or {}

        if fm:
            skill['name'] = fm.get('name', entry)
            skill['version'] = fm.get('version', '?')
            skill['description'] = (fm.get('description', '') or '')[:100]
            skill['agent_created'] = fm.get('agent_created', '').lower() in ('true', 'yes', '1')

            # P1: 缺少 agent_created
            if not skill['agent_created']:
                skill['issues'].append({
                    'severity': 'P1',
                    'type': 'missing_agent_created',
                    'message': '缺少 agent_created: true，后续可能无法通过 SkillManage 管理',
                })
        else:
            skill['name'] = entry
            skill['version'] = '?'
            skill['description'] = '(无法解析 frontmatter)'
            skill['agent_created'] = False
            skill['issues'].append({
                'severity': 'P1',
                'type': 'bad_frontmatter',
                'message': 'SKILL.md frontmatter 格式异常或无法解析',
            })

        # P2: 缺少 description
        if not skill.get('description') or skill['description'] in ('', '?', '(无法解析 frontmatter)'):
            skill['issues'].append({
                'severity': 'P2',
                'type': 'missing_description',
                'message': '缺少 description 字段',
            })

        # P2: 版本号异常
        if skill.get('version') == '?':
            skill['issues'].append({
                'severity': 'P2',
                'type': 'missing_version',
                'message': '版本号缺失',
            })

        # 检查附加资源
        has_scripts = os.path.isdir(os.path.join(entry_path, 'scripts'))
        has_references = os.path.isdir(os.path.join(entry_path, 'references'))
        has_assets = os.path.isdir(os.path.join(entry_path, 'assets'))
        has_meta = os.path.exists(os.path.join(entry_path, '_skillhub_meta.json')) or \
                   os.path.exists(os.path.join(entry_path, '_knot_meta.json'))
        skill['resources'] = {
            'scripts': has_scripts,
            'references': has_references,
            'assets': has_assets,
            'marketplace_meta': has_meta,
        }

        # 推断来源类型
        if has_meta:
            skill['source_type'] = 'marketplace'
        elif skill.get('agent_created'):
            skill['source_type'] = 'agent'
        else:
            skill['source_type'] = 'unknown'

        # P1: 数字 ID 目录名
        if re.match(r'^skill_\d+$', entry):
            skill['source_type'] = 'marketplace'
            skill['issues'].append({
                'severity': 'P1',
                'type': 'numeric_id_dir',
                'message': f'目录名为数字 ID ({entry})，不便识别。可通过 frontmatter name 字段确认实际名称',
            })

        # P1: .backup 后缀
        if entry.endswith('.backup'):
            skill['issues'].append({
                'severity': 'P1',
                'type': 'backup_dir',
                'message': f'目录名含 .backup ({entry})，疑似手动备份，可能与主版本冲突',
            })

        # 确定最高严重级别
        severities = [i['severity'] for i in skill['issues']]
        if 'P0' in severities:
            skill['level'] = 'P0'
        elif 'P1' in severities:
            skill['level'] = 'P1'
        elif 'P2' in severities:
            skill['level'] = 'P2'

        skills.append(skill)

    return skills


def check_duplicates(all_skills):
    """检测重复 skill（按 name 分组）"""
    name_map = defaultdict(list)
    for s in all_skills:
        name = s.get('name', s['dir_name'])
        name_map[name].append(s)

    duplicates = {}
    for name, skills in name_map.items():
        if len(skills) > 1:
            duplicates[name] = skills

    return duplicates


def check_orphan_files(skill_dir):
    """检查 skill 根目录下的遗留文件"""
    issues = []
    if not os.path.isdir(skill_dir):
        return issues

    for entry in os.listdir(skill_dir):
        entry_path = os.path.join(skill_dir, entry)
        if entry.endswith('.zip'):
            size = os.path.getsize(entry_path)
            size_mb = size / (1024 * 1024)
            issues.append({
                'severity': 'P1',
                'type': 'orphan_zip',
                'path': entry_path,
                'message': f'遗留 .zip 文件: {entry} ({size_mb:.1f} MB)',
            })

    return issues


def audit(user_path='~/.workbuddy/skills/', project_path=None, output_json=False):
    """主审计函数"""
    user_path = os.path.expanduser(user_path)

    all_skills = []
    all_issues = []

    # 扫描用户级
    user_skills = scan_directory(user_path, '用户级')
    all_skills.extend(user_skills)

    # 扫描项目级
    if project_path and os.path.isdir(project_path):
        proj_skills = scan_directory(project_path, '项目级')
        all_skills.extend(proj_skills)

    # 检查遗留文件
    orphan_issues = check_orphan_files(user_path)
    all_issues.extend(orphan_issues)

    # 检查重复
    duplicates = check_duplicates(all_skills)
    for name, skills in duplicates.items():
        paths = [f"{s['source']}/{s['dir_name']}" for s in skills]
        all_issues.append({
            'severity': 'P0',
            'type': 'duplicate_skill',
            'name': name,
            'paths': paths,
            'message': f'重复 Skill: {name} — 出现在 {", ".join(paths)}',
        })

    # 汇总各 skill 的问题
    for s in all_skills:
        all_issues.extend(s['issues'])

    # 按严重度分组
    p0 = [i for i in all_issues if i['severity'] == 'P0']
    p1 = [i for i in all_issues if i['severity'] == 'P1']
    p2 = [i for i in all_issues if i['severity'] == 'P2']

    result = {
        'summary': {
            'total_skills': len(all_skills),
            'total_issues': len(all_issues),
            'p0_count': len(p0),
            'p1_count': len(p1),
            'p2_count': len(p2),
            'ok_count': sum(1 for s in all_skills if s['level'] == 'ok'),
            'duplicate_groups': len(duplicates),
        },
        'duplicates': {name: [{'source': s['source'], 'path': s['dir_name']} for s in sk] for name, sk in duplicates.items()},
        'issues': {
            'P0': p0,
            'P1': p1,
            'P2': p2,
        },
        'skills': [
            {
                'name': s.get('name', s['dir_name']),
                'dir_name': s['dir_name'],
                'version': s.get('version', '?'),
                'source': s['source'],
                'source_type': s.get('source_type', 'unknown'),
                'description': s.get('description', ''),
                'agent_created': s.get('agent_created', False),
                'level': s['level'],
                'resources': s.get('resources', {}),
                'issues': s.get('issues', []),
            }
            for s in all_skills
        ],
    }

    return result


def print_report(result):
    """打印人类可读的审计报告（纯 ASCII 安全输出）"""
    s = result['summary']

    lines = []
    lines.append("")
    lines.append("=" * 64)
    lines.append("  [Skill Audit Report]")
    lines.append("=" * 64)
    lines.append("")
    lines.append(f"  Total: {s['total_skills']} skills")
    lines.append(f"     [P0] Critical: {s['p0_count']}  |  [P1] Warning: {s['p1_count']}  |  [P2] Suggestion: {s['p2_count']}  |  [OK] Clean: {s['ok_count']}")
    lines.append("")

    # P0
    if result['issues']['P0']:
        lines.append("  ## [P0] Critical Issues")
        lines.append("")
        for i, issue in enumerate(result['issues']['P0'], 1):
            lines.append(f"  {i}. {issue['message']}")
        lines.append("")

    # P1
    if result['issues']['P1']:
        lines.append("  ## [P1] Warnings")
        lines.append("")
        for i, issue in enumerate(result['issues']['P1'], 1):
            lines.append(f"  {i}. {issue['message']}")
        lines.append("")

    # P2
    if result['issues']['P2']:
        lines.append("  ## [P2] Suggestions")
        lines.append("")
        for i, issue in enumerate(result['issues']['P2'], 1):
            lines.append(f"  {i}. {issue['message']}")
        lines.append("")

    # Skill list
    lines.append("  ## Skill List")
    lines.append("")
    level_icons = {'ok': '[OK]', 'P2': '[P2]', 'P1': '[P1]', 'P0': '[P0]'}
    for sk in result['skills']:
        icon = level_icons.get(sk['level'], '[??]')
        name = sk['name'][:30]
        ver = sk['version'][:8]
        src_tag = {'agent': '(agent)', 'marketplace': '(market)', 'unknown': '(?)'}.get(sk['source_type'], '?')
        resources = []
        r = sk.get('resources', {})
        if r.get('scripts'): resources.append('[scripts]')
        if r.get('references'): resources.append('[refs]')
        if r.get('assets'): resources.append('[assets]')
        res_str = ' '.join(resources) if resources else '-'
        lines.append(f"  {icon} {name:30s} v{ver:8s} {src_tag} {res_str}")
    lines.append("")

    if result['issues']['P0']:
        lines.append("  WARNING: P0 critical issues found. Use --fix to auto-fix known issues.")
    elif result['issues']['P1']:
        lines.append("  NOTE: P1 warnings found. Consider fixing to keep skill library healthy.")
    else:
        lines.append("  All skills healthy!")

    lines.append("")

    # Print safely
    for line in lines:
        try:
            print(line)
        except UnicodeEncodeError:
            print(line.encode('ascii', errors='replace').decode('ascii'))


def main():
    parser = argparse.ArgumentParser(description='Skill Manager Audit Tool')
    parser.add_argument('--user', default='~/.workbuddy/skills/', help='用户级 skill 目录')
    parser.add_argument('--project', default=None, help='项目级 skill 目录')
    parser.add_argument('--json', action='store_true', help='输出 JSON 格式')
    parser.add_argument('--fix', action='store_true', help='自动修复已知问题')
    args = parser.parse_args()

    result = audit(args.user, args.project, args.json)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print_report(result)


if __name__ == '__main__':
    main()
