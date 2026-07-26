#!/usr/bin/env python3
"""播客脚本与 shownotes 格式校验工具。

校验 script.md 和 notes.md 是否符合 README.md 规范，输出不合规项。

用法：
  python3 scripts/validate_podcast.py --script script.md
  python3 scripts/validate_podcast.py --notes notes.md
  python3 scripts/validate_podcast.py --script script.md --notes notes.md

退出码：0 = 全部通过，1 = 有不合规项
"""

import argparse
import re
import sys
from pathlib import Path
from typing import List, Tuple

sys.path.insert(0, str(Path(__file__).parent))
# 行级定义与解析层共享；校验器只负责"合不合规"，解析语义永远以 script_md 为准
from script_md import (SEGMENT_RE, is_known_speaker, is_narration,
                       parse_podcast_script)

# script.md 校验规则
SCRIPT_TITLE_RE = re.compile(r'^#\s+.+')  # 标题，不带"播客脚本:"前缀
# 标题格式 {English} -- {中文副标题}：左侧含拉丁字母，' -- ' 分隔
TITLE_FORMAT_RE = re.compile(r'^#\s+.*[A-Za-z].*\s--\s.+')
# 任意加粗说话人行（含 H2 收尾行），用于白名单外角色检查——
# 解析器接受任意角色名并静默按嘉宾音色合成，必须在这里拦住
ANY_SPEAKER_RE = re.compile(r'^(?:#{1,6}\s+)?\*\*([^*]+?)\*\*[：:]')
NARRATION_CLOSING = "好，回到对话。"
MAX_NARRATIONS = 4
SPEAKER_RE = re.compile(r'^\*\*(主持人|嘉宾|旁白|Host|Guest)\*\*[:：]\s*.+')
NARRATION_RE = re.compile(r'^\*\*旁白\*\*[:：]\s*.+')
CLOSING_RE = re.compile(r'感谢收听.*show\s*notes.*下期见|我们下期见')
OLD_TITLE_RE = re.compile(r'^#\s*播客脚本[：:]')
OLD_SEGMENT_RE = re.compile(r'^##\s+第.+段[：:]')

# notes.md 校验规则
NOTES_FIRST_LINE_RE = re.compile(r'^本期.+。.*一句话主线[：:].+')
TIMELINE_RE = re.compile(r'^-\s+\d{2}:\d{2}\s+.+')
SECTION_RE = re.compile(r'^\*\*(内容速览|时间轴|原文链接|延伸阅读)\*\*')


def validate_script(filepath: str) -> List[str]:
    """校验 script.md 格式，返回问题列表。"""
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    issues = []
    has_title = False
    has_closing = False
    segments = []
    narration_lines = []
    current_segment_line = -1

    for i, line in enumerate(lines):
        stripped = line.strip()

        # 标题检查
        if stripped.startswith("# ") and not stripped.startswith("## "):
            if OLD_TITLE_RE.match(stripped):
                issues.append(f"L{i+1}: 标题不应带'播客脚本:'前缀，直接用 '# {{标题}}'")
            elif not has_title and not TITLE_FORMAT_RE.match(stripped):
                issues.append(f"L{i+1}: 标题格式应为 '{{English title}} -- {{中文副标题}}'"
                              f"（' -- ' 分隔），当前: {stripped[:60]}")
            has_title = True

        # 白名单外角色检查（解析器会接受任意角色并静默用嘉宾音色合成）
        m_any = ANY_SPEAKER_RE.match(stripped)
        if m_any and not is_known_speaker(m_any.group(1)):
            issues.append(f"L{i+1}: 未知角色 '**{m_any.group(1)}**'——只允许 主持人/嘉宾/旁白，"
                          f"否则会静默落到嘉宾音色")

        # 分段检查
        m = SEGMENT_RE.match(stripped)
        if m:
            segments.append((i + 1, stripped))
            current_segment_line = i

        # 旧格式分段检查
        if OLD_SEGMENT_RE.match(stripped) and not m:
            issues.append(f"L{i+1}: 分段格式应为 '## 第 N 段 · 子标题'（用中点·分隔），当前: {stripped}")

        # 角色行检查
        if SPEAKER_RE.match(stripped):
            # 旁白不应在问答中间
            if NARRATION_RE.match(stripped):
                narration_lines.append((i + 1, current_segment_line))

        # 收尾检查
        if CLOSING_RE.search(stripped):
            has_closing = True

    if not has_title:
        issues.append("缺少标题行（# {title}）")

    if not has_closing:
        issues.append("缺少固定收尾句（'感谢收听，完整原文列表在 show notes 里。我们下期见'）")

    if not segments:
        issues.append("未找到任何分段（## 第 N 段 · 子标题）")

    # 旁白位置检查：旁白应出现在段落开头
    for narr_line, seg_line in narration_lines:
        if seg_line < 0:
            issues.append(f"L{narr_line}: 旁白出现在分段标题之前，应放在段落开头")
        # 检查旁白前是否有其他对话行（允许旁白紧跟分段标题）
        for j in range(seg_line, narr_line - 1):
            if SPEAKER_RE.match(lines[j].strip()) and not NARRATION_RE.match(lines[j].strip()):
                issues.append(f"L{narr_line}: 旁白应放在段落开头、对话开始之前，不应插在问答中间")
                break

    # ===== 台词级检查（用与合成完全相同的解析结果）=====
    segments = parse_podcast_script(filepath)

    narrations = [t for s, t in segments if is_narration(s)]
    if len(narrations) > MAX_NARRATIONS:
        issues.append(f"旁白 {len(narrations)} 段，超过每期上限 {MAX_NARRATIONS} 段——多了节目会碎")
    for t in narrations:
        if not t.rstrip().endswith(NARRATION_CLOSING):
            issues.append(f"旁白缺统一收束句'{NARRATION_CLOSING}'：{t[:40]}...")

    for s, t in segments:
        if "http://" in t or "https://" in t:
            issues.append(f"台词包含 URL（会被逐字朗读，EP12 教训）：{s}: {t[:60]}...")

    return issues


def validate_notes(filepath: str) -> List[str]:
    """校验 notes.md 格式，返回问题列表。"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    issues = []
    lines = content.strip().split("\n")

    # 首行导语检查
    if lines and not NOTES_FIRST_LINE_RE.match(lines[0].strip()):
        # 允许以图片或空行开头的情况
        first_text_line = ""
        for line in lines:
            stripped = line.strip()
            if stripped and not stripped.startswith("!["):
                first_text_line = stripped
                break
        if not NOTES_FIRST_LINE_RE.match(first_text_line):
            issues.append(f"首行应为 '本期{{导语}}。一句话主线：{{主线}}'，当前: {first_text_line[:60]}...")

    # 必需 section 检查
    has_summary = False
    has_timeline = False
    has_links = False
    for line in lines:
        stripped = line.strip()
        if stripped == "**内容速览**":
            has_summary = True
        elif stripped == "**时间轴**":
            has_timeline = True
        elif stripped in ("**原文链接**", "**延伸阅读**"):
            has_links = True

    if not has_summary:
        issues.append("缺少 **内容速览** section")
    if not has_links:
        issues.append("缺少 **原文链接** 或 **延伸阅读** section")

    # 时间轴格式检查（如果存在）
    if has_timeline:
        in_timeline = False
        timeline_count = 0
        for line in lines:
            stripped = line.strip()
            if stripped == "**时间轴**":
                in_timeline = True
                continue
            if in_timeline:
                if stripped.startswith("**") or (stripped and not stripped.startswith("-")):
                    break
                if TIMELINE_RE.match(stripped):
                    timeline_count += 1
        if timeline_count == 0:
            issues.append("**时间轴** section 下没有有效的时间轴条目（格式: - MM:SS 段落名）")

    # 不应有顶级标题
    for i, line in enumerate(lines):
        if line.strip().startswith("# ") and not line.strip().startswith("## "):
            issues.append(f"L{i+1}: notes.md 不应有顶级标题（#），首行直接是导语")
            break

    return issues


def main():
    parser = argparse.ArgumentParser(description="播客脚本与 shownotes 格式校验")
    parser.add_argument("--script", help="script.md 路径")
    parser.add_argument("--notes", help="notes.md 路径")
    args = parser.parse_args()

    if not args.script and not args.notes:
        parser.error("请至少指定 --script 或 --notes")

    all_issues = []

    if args.script:
        path = Path(args.script)
        if not path.exists():
            print(f"❌ 文件不存在: {args.script}", file=sys.stderr)
            sys.exit(1)
        print(f"校验 script.md: {args.script}")
        issues = validate_script(args.script)
        if issues:
            for issue in issues:
                print(f"  ⚠️ {issue}")
            all_issues.extend(issues)
        else:
            print("  ✅ script.md 格式全部通过")
        print()

    if args.notes:
        path = Path(args.notes)
        if not path.exists():
            print(f"❌ 文件不存在: {args.notes}", file=sys.stderr)
            sys.exit(1)
        print(f"校验 notes.md: {args.notes}")
        issues = validate_notes(args.notes)
        if issues:
            for issue in issues:
                print(f"  ⚠️ {issue}")
            all_issues.extend(issues)
        else:
            print("  ✅ notes.md 格式全部通过")
        print()

    if all_issues:
        print(f"共 {len(all_issues)} 个不合规项", file=sys.stderr)
        sys.exit(1)
    else:
        print("🎉 全部通过")
        sys.exit(0)


if __name__ == "__main__":
    main()
