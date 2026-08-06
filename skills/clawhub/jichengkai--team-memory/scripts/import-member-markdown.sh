#!/usr/bin/env bash

# Team Memory v2.6.0 - Markdown 历史记录导入脚本
# 默认 dry-run；加 --apply 才写入成员 timeline.md。

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export PYTHONPATH="$SCRIPT_DIR:${PYTHONPATH:-}"

python3 - "$@" <<'PY'
from __future__ import annotations

import argparse
import hashlib
import re
import shutil
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path

from team_memory_paths import TeamMemoryPathError, print_warnings, resolve_paths


WEEKDAYS = "一二三四五六日"


@dataclass
class Member:
    member_id: str
    name: str
    alias: str = ""
    role: str = ""
    level: str = ""
    team: str = ""
    join_date: str = ""


@dataclass
class SourceRecord:
    member_id: str
    source_file: Path
    source_line: int
    record_date: str
    title: str
    lines: list[str]
    fingerprint: str = ""
    event_id: str = ""
    duplicate_reason: str = ""


@dataclass
class ParseResult:
    records: list[SourceRecord] = field(default_factory=list)
    undated_blocks: list[str] = field(default_factory=list)
    invalid_dates: list[str] = field(default_factory=list)


def clean_value(raw: str) -> str:
    raw = raw.split("#", 1)[0].strip()
    if (raw.startswith('"') and raw.endswith('"')) or (raw.startswith("'") and raw.endswith("'")):
        return raw[1:-1]
    return raw


def parse_config(config_path: Path) -> tuple[list[Member], dict[str, str], list[str]]:
    text = config_path.read_text(encoding="utf-8")
    members: list[Member] = []
    shortcuts: dict[str, str] = {}
    errors: list[str] = []
    current: dict[str, str] | None = None
    in_members = False
    in_shortcuts = False

    def finish_current() -> None:
        nonlocal current
        if not current:
            return
        member_id = current.get("id", "")
        name = current.get("name", "")
        if not member_id or not name:
            errors.append(f"成员配置缺少 id 或 name: {current}")
        else:
            members.append(
                Member(
                    member_id=member_id,
                    name=name,
                    alias=current.get("alias", ""),
                    role=current.get("role", ""),
                    level=current.get("level", ""),
                    team=current.get("team", ""),
                    join_date=current.get("join-date", ""),
                )
            )
        current = None

    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        is_top_level = bool(line) and not line[0].isspace()
        if is_top_level and re.match(r"^[A-Za-z0-9_-]+:", stripped) and not stripped.startswith("- "):
            section = stripped.split(":", 1)[0]
            if section != "members":
                finish_current()
            in_members = section == "members"
            in_shortcuts = section == "shortcuts"
            continue
        if in_members:
            if stripped.startswith("- "):
                finish_current()
                current = {}
                rest = stripped[2:].strip()
                if ":" in rest:
                    key, value = rest.split(":", 1)
                    current[key.strip()] = clean_value(value)
                continue
            if current is not None and ":" in stripped:
                key, value = stripped.split(":", 1)
                current[key.strip()] = clean_value(value)
        elif in_shortcuts and ":" in stripped:
            key, value = stripped.split(":", 1)
            shortcuts[clean_value(key)] = clean_value(value)

    finish_current()

    member_ids = {member.member_id for member in members}
    for shortcut, member_id in shortcuts.items():
        if member_id not in member_ids:
            errors.append(f"快捷输入 {shortcut} 指向不存在的成员 {member_id}")

    return members, shortcuts, errors


def build_lookup(members: list[Member], shortcuts: dict[str, str]) -> tuple[dict[str, str], list[str]]:
    lookup: dict[str, str] = {}
    errors: list[str] = []

    def add(token: str, member_id: str) -> None:
        token = token.strip()
        if not token:
            return
        old = lookup.get(token)
        if old and old != member_id:
            errors.append(f"成员匹配关键字冲突: {token} 同时指向 {old} 和 {member_id}")
            return
        lookup[token] = member_id

    for member in members:
        add(member.member_id, member.member_id)
        add(member.name, member.member_id)
        add(member.alias, member.member_id)
    for shortcut, member_id in shortcuts.items():
        add(shortcut, member_id)

    return lookup, errors


def rel_path(path: Path, base: Path) -> str:
    try:
        return str(path.resolve().relative_to(base.resolve()))
    except ValueError:
        return str(path)


DATE_PATTERNS = [
    re.compile(r"(?P<year>19\d{2}|20\d{2})[-/.](?P<month>\d{1,2})[-/.](?P<day>\d{1,2})"),
    re.compile(r"(?P<year>19\d{2}|20\d{2})年(?P<month>\d{1,2})月(?P<day>\d{1,2})日"),
]


def normalize_match(match: re.Match[str]) -> tuple[str | None, str]:
    raw = match.group(0)
    try:
        parsed = date(int(match.group("year")), int(match.group("month")), int(match.group("day")))
    except ValueError:
        return None, raw
    return parsed.isoformat(), raw


def find_record_start(line: str) -> tuple[str | None, str | None, str | None]:
    stripped = line.strip()
    if not stripped:
        return None, None, None

    is_heading = bool(re.match(r"^#{1,6}\s+", stripped))
    search_text = stripped
    anchored = re.sub(r"^(?:[-*+]\s+|>\s+)*", "", stripped)

    for pattern in DATE_PATTERNS:
        match = pattern.search(search_text) if is_heading else pattern.match(anchored)
        if not match:
            continue
        normalized, raw = normalize_match(match)
        if normalized is None:
            return None, raw, f"无效日期: {raw}"
        return normalized, raw, None
    return None, None, None


def strip_markdown(raw: str) -> str:
    text = raw.strip()
    text = re.sub(r"^#{1,6}\s*", "", text)
    text = re.sub(r"^(?:[-*+]\s+|>\s+)*", "", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return text.strip()


def compact_text(lines: list[str], limit: int = 160) -> str:
    text = " ".join(strip_markdown(line) for line in lines)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return text or "历史导入记录"
    return text[: limit - 1].rstrip() + "…"


def make_title(start_line: str, date_text: str, lines: list[str]) -> str:
    title = strip_markdown(start_line).replace(date_text, "")
    title = re.sub(r"[（(]周[一二三四五六日天][）)]", "", title)
    title = title.strip(" -:：|｜—\t")
    if not title:
        for line in lines[1:]:
            candidate = strip_markdown(line)
            if candidate:
                title = candidate
                break
    title = re.sub(r"\s+", " ", title).strip()
    if not title:
        title = "历史导入记录"
    if len(title) > 48:
        title = title[:47].rstrip() + "…"
    return title


def meaningful_undated(lines: list[str]) -> list[str]:
    meaningful: list[str] = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if re.match(r"^#{1,2}\s+.+$", stripped):
            continue
        if stripped in {"---", "***"}:
            continue
        meaningful.append(strip_markdown(stripped))
    return meaningful


def extract_records(path: Path, member_id: str) -> ParseResult:
    result = ParseResult()
    lines = path.read_text(encoding="utf-8").splitlines()
    current_date: str | None = None
    current_date_text = ""
    current_start_line = 0
    current_lines: list[str] = []
    leading_lines: list[str] = []

    def finish_current() -> None:
        nonlocal current_date, current_date_text, current_start_line, current_lines
        if current_date is None:
            return
        title = make_title(current_lines[0], current_date_text, current_lines)
        result.records.append(
            SourceRecord(
                member_id=member_id,
                source_file=path,
                source_line=current_start_line,
                record_date=current_date,
                title=title,
                lines=list(current_lines),
            )
        )
        current_date = None
        current_date_text = ""
        current_start_line = 0
        current_lines = []

    for line_no, line in enumerate(lines, start=1):
        normalized_date, date_text, error = find_record_start(line)
        if error:
            result.invalid_dates.append(f"{path}:{line_no} {error}")
        if normalized_date:
            finish_current()
            current_date = normalized_date
            current_date_text = date_text or normalized_date
            current_start_line = line_no
            current_lines = [line]
            continue
        if current_date is None:
            leading_lines.append(line)
        else:
            current_lines.append(line)

    finish_current()

    undated = meaningful_undated(leading_lines)
    if undated:
        preview = " / ".join(undated[:3])
        result.undated_blocks.append(f"{path}: 文件开头存在未归入日期的内容：{preview}")
    return result


def resolve_member_for_file(
    path: Path,
    input_dir: Path,
    forced_member: str | None,
    lookup: dict[str, str],
    members_by_id: dict[str, Member],
) -> tuple[str | None, str | None]:
    if forced_member:
        return forced_member, None

    rel = path.relative_to(input_dir)
    tokens: list[str] = []
    if len(rel.parts) > 1:
        tokens.append(rel.parts[0])
    tokens.append(path.stem)

    for token in tokens:
        member_id = lookup.get(token)
        if member_id:
            return member_id, None

    contains_matches: set[str] = set()
    haystacks = [path.stem]
    if len(rel.parts) > 1:
        haystacks.append(rel.parts[0])
    for token, member_id in lookup.items():
        if len(token) < 2:
            continue
        if any(token in haystack for haystack in haystacks):
            contains_matches.add(member_id)

    if len(contains_matches) == 1:
        return next(iter(contains_matches)), None
    if len(contains_matches) > 1:
        return None, f"{path}: 文件名或目录名命中多个成员，需改成 member-id/name/alias 目录"
    return None, f"{path}: 无法从目录名或文件名匹配成员"


def build_fingerprint(record: SourceRecord, skill_dir: Path) -> str:
    body = "\n".join(record.lines)
    body_hash = hashlib.sha256(re.sub(r"\s+", " ", body).strip().encode("utf-8")).hexdigest()[:16]
    seed = "|".join(
        [
            record.member_id,
            record.record_date,
            record.title,
            rel_path(record.source_file, skill_dir),
            body_hash,
        ]
    )
    return hashlib.sha256(seed.encode("utf-8")).hexdigest()[:20]


def timeline_path(data_dir: Path, member_id: str) -> Path:
    return data_dir / "members" / member_id / "timeline.md"


def existing_import_state(text: str) -> tuple[set[str], dict[str, int]]:
    fingerprints = set(re.findall(r"import-fingerprint:\s*([0-9a-f]{12,64})", text))
    max_by_date: dict[str, int] = {}
    for match in re.finditer(r"OBS-(\d{8})-IMPORT-(\d{3})", text):
        ymd, number = match.groups()
        date_key = f"{ymd[0:4]}-{ymd[4:6]}-{ymd[6:8]}"
        max_by_date[date_key] = max(max_by_date.get(date_key, 0), int(number))
    return fingerprints, max_by_date


def assign_events(
    records: list[SourceRecord],
    data_dir: Path,
    members_by_id: dict[str, Member],
) -> tuple[list[SourceRecord], list[SourceRecord], list[str]]:
    new_records: list[SourceRecord] = []
    duplicates: list[SourceRecord] = []
    errors: list[str] = []
    timeline_cache: dict[str, str] = {}
    existing_fingerprints: dict[str, set[str]] = {}
    max_id_by_member_date: dict[tuple[str, str], int] = {}
    seen_in_run: set[str] = set()

    for member_id in sorted({record.member_id for record in records}):
        path = timeline_path(data_dir, member_id)
        if not path.exists():
            errors.append(f"{member_id}: 缺少 timeline.md: {path}")
            continue
        text = path.read_text(encoding="utf-8")
        timeline_cache[member_id] = text
        fingerprints, max_by_date = existing_import_state(text)
        existing_fingerprints[member_id] = fingerprints
        for date_key, max_number in max_by_date.items():
            max_id_by_member_date[(member_id, date_key)] = max_number

    sorted_records = sorted(records, key=lambda item: (item.member_id, item.record_date, rel_path(item.source_file, data_dir), item.source_line))
    for record in sorted_records:
        if record.member_id not in members_by_id:
            errors.append(f"{record.member_id}: 成员不存在")
            continue
        if record.member_id not in timeline_cache:
            continue
        record.fingerprint = build_fingerprint(record, data_dir)
        run_key = f"{record.member_id}:{record.fingerprint}"
        if record.fingerprint in existing_fingerprints.get(record.member_id, set()):
            record.duplicate_reason = "timeline 中已存在相同导入指纹"
            duplicates.append(record)
            continue
        if run_key in seen_in_run:
            record.duplicate_reason = "本次输入中重复"
            duplicates.append(record)
            continue
        seen_in_run.add(run_key)
        key = (record.member_id, record.record_date)
        max_id_by_member_date[key] = max_id_by_member_date.get(key, 0) + 1
        ymd = record.record_date.replace("-", "")
        record.event_id = f"OBS-{ymd}-IMPORT-{max_id_by_member_date[key]:03d}"
        new_records.append(record)

    return new_records, duplicates, errors


def infer_tags(record: SourceRecord) -> str:
    text = "\n".join(record.lines)
    tags = ["#历史导入"]
    if re.search(r"MBTI|性格|偏好|类型", text, re.IGNORECASE):
        tags.append("#性格偏好")
    if re.search(r"期待|年度沟通|目标|OKR", text, re.IGNORECASE):
        tags.append("#年度期待")
    if re.search(r"问题|不足|改进|风险|关注", text, re.IGNORECASE):
        tags.append("#需关注")
    if re.search(r"我说|对.*说|反馈|1[:：]?1|沟通", text, re.IGNORECASE):
        tags.append("#沟通记录")
    return " ".join(dict.fromkeys(tags))


def blockquote(lines: list[str]) -> str:
    quoted = []
    for line in lines:
        quoted.append("> " + line if line.strip() else ">")
    return "\n".join(quoted) if quoted else "> "


def render_event(record: SourceRecord, data_dir: Path, import_time: str) -> str:
    snippet = compact_text(record.lines)
    source = rel_path(record.source_file, data_dir)
    return "\n".join(
        [
            f"#### 历史记录 - {record.title} [{record.event_id}]",
            f"**事件**: 历史导入记录：{snippet}",
            "**类别**: 历史证据",
            "**评价**: 未评级（历史导入）",
            f"**标签**: {infer_tags(record)}",
            "",
            "**来源**:",
            f"- 文件: `{source}`",
            f"- 行号: {record.source_line}",
            f"- 标题/片段: {record.title}",
            f"- 导入时间: {import_time}",
            "",
            "**原始记录**:",
            blockquote(record.lines),
            "",
            f"<!-- import-fingerprint: {record.fingerprint} -->",
            "",
        ]
    )


def find_timeline_bounds(lines: list[str]) -> tuple[int, int]:
    start = -1
    for idx, line in enumerate(lines):
        if re.match(r"^##\s+.*时间轴[（(]从新到旧[）)]", line.strip()):
            start = idx + 1
            break
    if start < 0:
        raise ValueError("未找到“时间轴（从新到旧）”标题")

    for idx in range(start, len(lines)):
        stripped = lines[idx].strip()
        if stripped.startswith("## ") and not stripped.startswith("### "):
            return start, idx

    for idx in range(start, len(lines)):
        if lines[idx].strip() != "---":
            continue
        lookahead = [line.strip() for line in lines[idx + 1 : idx + 5] if line.strip()]
        if lookahead and (lookahead[0].startswith("*创建于") or lookahead[0].startswith("*最后更新")):
            return start, idx

    return start, len(lines)


def weekday_heading(record_date: str) -> str:
    parsed = datetime.strptime(record_date, "%Y-%m-%d").date()
    return f"### {record_date}（周{WEEKDAYS[parsed.weekday()]}）"


def append_to_day_chunk(existing: str, rendered: str) -> str:
    base = existing.rstrip()
    separator = ""
    if base.endswith("---"):
        base = base[:-3].rstrip()
        separator = "\n\n---"
    return base + "\n\n" + rendered.rstrip() + separator + "\n"


def merge_timeline(text: str, records: list[SourceRecord], data_dir: Path, import_time: str) -> str:
    lines = text.splitlines(keepends=True)
    start, end = find_timeline_bounds(lines)
    section = "".join(lines[start:end])
    section_lines = section.splitlines(keepends=True)

    day_positions: list[tuple[int, str]] = []
    for idx, line in enumerate(section_lines):
        match = re.match(r"^###\s+(\d{4}-\d{2}-\d{2})", line.strip())
        if match:
            day_positions.append((idx, match.group(1)))

    day_chunks: dict[str, str] = {}
    if day_positions:
        preamble = "".join(section_lines[: day_positions[0][0]])
        for pos_idx, (line_idx, day) in enumerate(day_positions):
            next_idx = day_positions[pos_idx + 1][0] if pos_idx + 1 < len(day_positions) else len(section_lines)
            day_chunks[day] = "".join(section_lines[line_idx:next_idx]).rstrip() + "\n"
    else:
        preamble = section

    records_by_date: dict[str, list[SourceRecord]] = {}
    for record in records:
        records_by_date.setdefault(record.record_date, []).append(record)

    for record_date, date_records in records_by_date.items():
        rendered = "\n".join(render_event(record, data_dir, import_time).rstrip() for record in date_records).rstrip() + "\n"
        if record_date in day_chunks:
            day_chunks[record_date] = append_to_day_chunk(day_chunks[record_date], rendered)
        else:
            day_chunks[record_date] = weekday_heading(record_date) + "\n" + rendered

    ordered_days = sorted(day_chunks.keys(), reverse=True)
    new_section = preamble.rstrip()
    if new_section:
        new_section += "\n\n"
    day_parts: list[str] = []
    for day in ordered_days:
        day_parts.append(day_chunks[day].rstrip())
    new_section += "\n\n".join(day_parts) + "\n\n"

    return "".join(lines[:start]) + new_section + "".join(lines[end:])


def write_report(
    report_path: Path,
    mode: str,
    skill_dir: Path,
    input_dir: Path,
    generated_at: str,
    files: list[Path],
    new_records: list[SourceRecord],
    duplicates: list[SourceRecord],
    unmatched_files: list[str],
    undated_blocks: list[str],
    invalid_dates: list[str],
    assignment_errors: list[str],
) -> None:
    by_member: dict[str, list[SourceRecord]] = {}
    for record in new_records:
        by_member.setdefault(record.member_id, []).append(record)

    lines: list[str] = [
        "# Markdown 导入预览报告",
        "",
        f"- 模式: {mode}",
        f"- 生成时间: {generated_at}",
        f"- Skill 目录: `{skill_dir}`",
        f"- 输入目录: `{input_dir}`",
        f"- 扫描 Markdown 文件数: {len(files)}",
        f"- 将写入记录数: {len(new_records)}",
        f"- 疑似重复/已跳过记录数: {len(duplicates)}",
        "",
        "## 每个成员将导入多少条记录",
        "",
    ]

    if by_member:
        lines.extend(["| 成员 | 记录数 |", "|---|---:|"])
        for member_id in sorted(by_member):
            lines.append(f"| {member_id} | {len(by_member[member_id])} |")
    else:
        lines.append("无。")

    lines.extend(["", "## 将写入的事件 ID", ""])
    if new_records:
        for record in new_records:
            lines.append(
                f"- {record.member_id} {record.record_date} `{record.event_id}` "
                f"{record.title} （来源: `{rel_path(record.source_file, skill_dir)}:{record.source_line}`）"
            )
    else:
        lines.append("无。")

    lines.extend(["", "## 疑似重复记录", ""])
    if duplicates:
        for record in duplicates:
            lines.append(
                f"- {record.member_id} {record.record_date} {record.title} "
                f"（{record.duplicate_reason}，来源: `{rel_path(record.source_file, skill_dir)}:{record.source_line}`）"
            )
    else:
        lines.append("无。")

    lines.extend(["", "## 无法匹配成员的文件", ""])
    lines.extend(f"- {item}" for item in unmatched_files) if unmatched_files else lines.append("无。")

    lines.extend(["", "## 无法识别日期的段落", ""])
    lines.extend(f"- {item}" for item in undated_blocks) if undated_blocks else lines.append("无。")

    lines.extend(["", "## 无效日期", ""])
    lines.extend(f"- {item}" for item in invalid_dates) if invalid_dates else lines.append("无。")

    lines.extend(["", "## 其他校验问题", ""])
    lines.extend(f"- {item}" for item in assignment_errors) if assignment_errors else lines.append("无。")

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Import dated member Markdown records into Team Memory timelines.")
    parser.add_argument("--apply", action="store_true", help="write records after validation")
    parser.add_argument("--skill-dir", default=None, help="team-memory skill directory")
    parser.add_argument("--input-dir", default=None, help="Markdown input directory")
    parser.add_argument("--member", default=None, help="force all input files to one member id, e.g. member-001")
    args = parser.parse_args()

    try:
        paths = resolve_paths(args.skill_dir, require_lock=True)
    except TeamMemoryPathError as exc:
        print(f"ERROR: {exc}")
        return 1
    print_warnings(paths.warnings)
    skill_dir = paths.skill_dir
    data_dir = paths.data_dir
    if args.input_dir:
        input_dir = Path(args.input_dir).expanduser()
        if not input_dir.is_absolute():
            parts = input_dir.parts
            if parts and parts[0] == "data":
                input_dir = data_dir.joinpath(*parts[1:])
            else:
                input_dir = data_dir / input_dir
    else:
        input_dir = data_dir / "import" / "incoming"
    input_dir = input_dir.resolve()

    config_path = paths.config_path
    if not config_path.exists():
        print(f"ERROR: 缺少配置文件: {config_path}")
        return 1

    members, shortcuts, config_errors = parse_config(config_path)
    lookup, lookup_errors = build_lookup(members, shortcuts)
    members_by_id = {member.member_id: member for member in members}
    errors = config_errors + lookup_errors
    if args.member and args.member not in members_by_id:
        errors.append(f"--member 指向不存在的成员: {args.member}")
    if errors:
        print("ERROR: 配置校验失败")
        for error in errors:
            print(f"- {error}")
        return 1

    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    run_stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    report_path = data_dir / "import" / "reports" / f"import-report-{run_stamp}.md"
    mode = "apply" if args.apply else "dry-run"

    files = sorted(input_dir.rglob("*.md")) if input_dir.exists() else []
    unmatched_files: list[str] = []
    undated_blocks: list[str] = []
    invalid_dates: list[str] = []
    records: list[SourceRecord] = []

    for path in files:
        member_id, error = resolve_member_for_file(path, input_dir, args.member, lookup, members_by_id)
        if error or not member_id:
            unmatched_files.append(error or f"{path}: 无法匹配成员")
            continue
        parsed = extract_records(path, member_id)
        invalid_dates.extend(parsed.invalid_dates)
        undated_blocks.extend(parsed.undated_blocks)
        if not parsed.records:
            undated_blocks.append(f"{path}: 未找到任何可导入的带日期记录")
        records.extend(parsed.records)

    new_records, duplicates, assignment_errors = assign_events(records, data_dir, members_by_id)

    write_report(
        report_path=report_path,
        mode=mode,
        skill_dir=skill_dir,
        input_dir=input_dir,
        generated_at=generated_at,
        files=files,
        new_records=new_records,
        duplicates=duplicates,
        unmatched_files=unmatched_files,
        undated_blocks=undated_blocks,
        invalid_dates=invalid_dates,
        assignment_errors=assignment_errors,
    )

    print(f"已生成导入报告: {report_path}")
    if not input_dir.exists():
        print(f"输入目录不存在: {input_dir}")
        print("请按 data/import/incoming/member-001/*.md 放入旧 Markdown 后重试。")
        return 0
    if not files:
        print(f"没有发现 Markdown 文件: {input_dir}")
        return 0

    fatal_errors = unmatched_files + invalid_dates + assignment_errors
    fatal_no_date = [item for item in undated_blocks if "未找到任何可导入" in item]
    fatal_errors.extend(fatal_no_date)

    if args.apply and fatal_errors:
        print("ERROR: 校验未通过，未写入任何 timeline。详情见报告。")
        return 1

    if not args.apply:
        print("当前为 dry-run，未写入成员文件。确认报告后加 --apply 执行。")
        return 0

    if not new_records:
        print("没有新的记录需要写入。")
        return 0

    records_by_member: dict[str, list[SourceRecord]] = {}
    for record in new_records:
        records_by_member.setdefault(record.member_id, []).append(record)

    backup_dir = data_dir / ".backup" / f"import-{run_stamp}"
    backup_dir.mkdir(parents=True, exist_ok=False)

    for member_id, member_records in records_by_member.items():
        path = timeline_path(data_dir, member_id)
        backup_target = backup_dir / path.relative_to(data_dir)
        backup_target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, backup_target)
        original = path.read_text(encoding="utf-8")
        merged = merge_timeline(original, member_records, data_dir, generated_at)
        path.write_text(merged, encoding="utf-8")
        print(f"已写入 {member_id}: {len(member_records)} 条记录")

    print(f"导入完成。备份目录: {backup_dir}")
    return 0


raise SystemExit(main())
PY
