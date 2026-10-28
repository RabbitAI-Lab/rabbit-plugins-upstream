#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path

from notebook_providers import ProviderError, provider_from_config, resolve_token
from notebook_sync_core import (
    LEGACY_MANIFEST_KIND,
    MANIFEST_KIND,
    NotebookSyncError,
    content_hash,
    decode_json_page,
    decode_source_payload,
    discover_sync_files,
    load_config as load_notebook_config,
    load_state as load_notebook_state,
    unsupported_markdown,
)
from memory_events import (
    CLAIM_KINDS, EVIDENCE_LEVELS, EVENT_ID_PATTERN, VERIFICATION_STATUSES,
    iter_event_blocks, provenance_fields,
)
from task_utils import is_task_placeholder, parse_config_members, parse_tasks_md
from team_memory_paths import (
    TeamMemoryPathError,
    candidate_data_dirs,
    data_stats,
    print_warnings,
    read_config_data_path,
    read_root_lock,
    rel_path,
    resolve_paths,
    resolve_skill_dir,
    same_path,
)


EVENT_RE = re.compile(rf"^####\s+.+\s+\[({EVENT_ID_PATTERN})\]\s*$")
FIELD_RE = re.compile(r"^\*\*(?P<label>[^*]+)\*\*:\s*(?P<value>.*)$")


def check_yaml_safety(path: Path) -> list[str]:
    if not path.exists():
        return [f"- 必须修复：配置文件不存在 `{path}`"]
    findings: list[str] = []
    top_level: dict[str, int] = {}
    for line_no, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), start=1):
        if "\t" in line:
            findings.append(f"- 必须修复：配置第 {line_no} 行含制表符，标准 YAML 解析器会拒绝。")
            continue
        stripped = line.lstrip(" ")
        if stripped and not stripped.startswith("#") and (len(line) - len(stripped)) % 2:
            findings.append(f"- 必须修复：配置第 {line_no} 行缩进不是 2 个空格的倍数。")
        if not stripped or stripped.startswith("#"):
            continue
        candidate = stripped[2:].strip() if stripped.startswith("- ") else stripped
        if ":" not in candidate:
            findings.append(f"- 必须修复：配置第 {line_no} 行不是可安全识别的 key/value。")
        if len(line) == len(stripped):
            match = re.match(r"^([A-Za-z0-9_-]+):", stripped)
            if not match:
                findings.append(f"- 必须修复：配置第 {line_no} 行顶层 key 格式无法安全解析。")
            elif match.group(1) in top_level:
                findings.append(
                    f"- 必须修复：配置顶层 key `{match.group(1)}` 在第 {top_level[match.group(1)]} 和 {line_no} 行重复。"
                )
            else:
                top_level[match.group(1)] = line_no
    return findings


def report_path_for(skill_dir: Path, data_dir: Path | None) -> Path:
    base = data_dir if data_dir and data_dir.exists() else skill_dir
    reports_dir = base / ".reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    return reports_dir / f"doctor-report-{stamp}.md"


def write_report(skill_dir: Path, primary_data_dir: Path | None, lines: list[str]) -> Path:
    path = report_path_for(skill_dir, primary_data_dir)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def field_value(lines: list[str], label: str) -> str:
    values: list[str] = []
    for line in lines:
        match = FIELD_RE.match(line.strip())
        if match and match.group("label") == label:
            values.append(match.group("value").strip())
    return " / ".join(values)


def scan_timeline(path: Path, data_dir: Path, owner_type: str, owner_id: str) -> list[dict[str, object]]:
    source_file = rel_path(path, data_dir)
    return [
        {
            "event_id": block.event_id,
            "event_key": f"{source_file}:{block.event_id}",
            "owner_type": owner_type,
            "owner_id": owner_id,
            "source_file": source_file,
            "source_line": block.line,
            "title": block.title,
            "feedback_type": field_value(block.lines, "反馈类型"),
            "related_members": field_value(block.lines, "涉及成员"),
            "related_event": field_value(block.lines, "关联事件"),
            "raw": "\n".join(block.lines),
            **provenance_fields(block.lines),
        }
        for block in iter_event_blocks(path)
    ]


def collect_markdown_events(data_dir: Path) -> list[dict[str, object]]:
    events: list[dict[str, object]] = []
    members_dir = data_dir / "members"
    if members_dir.exists():
        for child in sorted(members_dir.iterdir()):
            if child.is_dir() and child.name.startswith("member-"):
                events.extend(scan_timeline(child / "timeline.md", data_dir, "member", child.name))
            elif child.is_file() and child.name.endswith("-时间轴.md"):
                events.extend(scan_timeline(child, data_dir, "member", child.name.removesuffix("-时间轴.md")))
    stakeholders_dir = data_dir / "stakeholders"
    if stakeholders_dir.exists():
        for child in sorted(stakeholders_dir.iterdir()):
            if child.is_dir() and child.name.startswith("stakeholder-"):
                events.extend(scan_timeline(child / "timeline.md", data_dir, "stakeholder", child.name))
    events.extend(scan_timeline(data_dir / "company" / "timeline.md", data_dir, "company", "company"))
    events.extend(scan_timeline(data_dir / "manager" / "reflections.md", data_dir, "manager", "manager"))
    return events


def check_source_provenance(data_dir: Path, events: list[dict[str, object]]) -> list[str]:
    findings: list[str] = []
    sources: dict[str, tuple[Path, int, dict[str, object]]] = {}
    for processing in sorted((data_dir / "sources" / "conversations").glob("*/*/processing.md")):
        location = rel_path(processing, data_dir)
        matches = re.findall(r"```json\s*\n(.*?)\n```", processing.read_text(encoding="utf-8", errors="replace"), re.DOTALL)
        try:
            metadata = json.loads(matches[0]) if matches else None
            if not isinstance(metadata, dict):
                raise ValueError("缺少 JSON 对象")
            source_id = str(metadata.get("source_id", ""))
            if not source_id or source_id != processing.parent.name:
                raise ValueError("来源ID与目录不一致")
            if source_id in sources:
                raise ValueError("来源ID重复")
            original = processing.parent / "original.md"
            raw = original.read_bytes()
            if hashlib.sha256(raw).hexdigest() != metadata.get("content_sha256", metadata.get("raw_sha256")):
                raise ValueError("原文 SHA-256 不匹配")
            if "byte_length" in metadata and metadata["byte_length"] != len(raw):
                raise ValueError("原文字节数不匹配")
            sources[source_id] = (original, len(raw.decode("utf-8").splitlines()), metadata)
        except (OSError, UnicodeError, ValueError, TypeError) as exc:
            findings.append(f"- 必须修复：谈话来源元数据无效 `{location}`: {exc}")
    for original in sorted((data_dir / "sources" / "conversations").glob("*/*/original.md")):
        if not (original.parent / "processing.md").is_file():
            findings.append(f"- 必须修复：谈话原文缺少 processing.md: `{rel_path(original, data_dir)}`")

    event_by_key = {str(event["event_key"]): event for event in events}
    for source_id, (original, _, metadata) in sources.items():
        status = metadata.get("status")
        if status == "applying":
            findings.append(f"- 谈话 `{source_id}` 拆解写入未完成，重新运行原导入计划以恢复；原文已保留。")
        if status != "complete":
            continue
        items = metadata.get("items", [])
        committed_keys = metadata.get("committed_keys", [])
        if not isinstance(items, list) or not isinstance(committed_keys, list):
            findings.append(f"- 必须修复：谈话拆解映射格式错误 `{source_id}`")
            continue
        by_key = {item.get("key"): item for item in items if isinstance(item, dict) and isinstance(item.get("key"), str)}
        for key in committed_keys:
            item = by_key.get(str(key))
            if not item or not item.get("event_id") or not item.get("target_file"):
                findings.append(f"- 必须修复：谈话已提交项目缺少派生映射 `{source_id}` / `{key}`")
                continue
            event_key = f"{item['target_file']}:{item['event_id']}"
            event = event_by_key.get(event_key)
            if not event or event.get("source_id") != source_id:
                findings.append(f"- 必须修复：谈话拆解映射未找到对应派生事件 `{source_id}` -> `{event_key}`")
    for event in events:
        location = f"{event['source_file']}:{event['source_line']} `{event['event_id']}`"
        source_id = str(event.get("source_id", ""))
        new_record = str(event["event_id"]).startswith(("CMP-", "REF-")) or bool(source_id)
        for key, label, allowed in [
            ("claim_kind", "信息性质", CLAIM_KINDS),
            ("evidence_level", "证据等级", EVIDENCE_LEVELS),
            ("verification_status", "核实状态", VERIFICATION_STATUSES),
        ]:
            value = str(event.get(key, ""))
            if (new_record and not value) or (value and value not in allowed):
                findings.append(f"- 必须修复：{label}缺失或不支持 `{value}`: {location}")
        if source_id:
            if source_id not in sources:
                findings.append(f"- 必须修复：来源ID找不到完整原文 `{source_id}`: {location}")
            else:
                span = re.fullmatch(r"(\d+)(?:-(\d+))?", str(event.get("source_span", "")))
                start = int(span.group(1)) if span else 0
                end = int(span.group(2) or span.group(1)) if span else 0
                if not (1 <= start <= end <= sources[source_id][1]):
                    findings.append(f"- 必须修复：来源位置超出原文或格式错误: {location}")
            if not str(event.get("speaker", "")).strip():
                findings.append(f"- 必须修复：派生记录缺少说话人: {location}")
        elif event.get("source_span"):
            findings.append(f"- 必须修复：来源位置存在但缺少来源ID: {location}")
        if (event.get("claim_kind") == "对方陈述" and event.get("evidence_level") in {"事实", "结论"}
                and event.get("verification_status") not in {"已确认", "已闭环"}):
            findings.append(f"- 必须修复：未核实的对方陈述被标为事实或结论: {location}")
        canonical = str(event.get("canonical_event_key", ""))
        if canonical and canonical not in event_by_key:
            findings.append(f"- 必须修复：主记录不存在 `{canonical}`: {location}")
        seen = {str(event["event_key"])}
        while canonical and canonical in event_by_key:
            if canonical in seen:
                findings.append(f"- 必须修复：主记录引用形成循环: {location}")
                break
            seen.add(canonical)
            canonical = str(event_by_key[canonical].get("canonical_event_key", ""))
    return findings


def check_data_consistency(data_dir: Path, config_path: Path | None = None) -> list[str]:
    events = collect_markdown_events(data_dir)
    event_ids = {str(event["event_id"]) for event in events}
    event_key_groups: dict[str, list[dict[str, object]]] = defaultdict(list)
    event_id_groups: dict[str, list[dict[str, object]]] = defaultdict(list)
    for event in events:
        event_key_groups[str(event["event_key"])].append(event)
        event_id_groups[str(event["event_id"])].append(event)
    lines: list[str] = ["", "## 数据一致性检查", ""]
    findings: list[str] = []

    configured_members = parse_config_members(config_path or data_dir.parent / "skill-config.yaml")
    member_dirs = {
        child.name
        for child in (data_dir / "members").glob("member-*")
        if child.is_dir()
    }
    missing_config = sorted(member_dirs - set(configured_members))
    if missing_config:
        findings.append(f"- 必须修复：成员目录未登记到 skill-config.yaml: `{', '.join(missing_config)}`")

    duplicate_keys = sorted(event_key for event_key, group in event_key_groups.items() if len(group) > 1)
    if duplicate_keys:
        findings.append(f"- 必须修复：同一文件内重复事件 ID {len(duplicate_keys)} 个；这些记录会产生相同 event_key。")
        for event_key in duplicate_keys[:10]:
            locations = [
                f"{event['source_file']}:{event['source_line']}"
                for event in event_key_groups[event_key]
            ]
            findings.append(f"  - `{event_key}`: {', '.join(locations)}")

    cross_file_duplicate_ids = sorted(
        event_id
        for event_id, group in event_id_groups.items()
        if len({str(event["source_file"]) for event in group}) > 1
    )
    if cross_file_duplicate_ids:
        findings.append(
            f"- 发现跨文件重复事件 ID {len(cross_file_duplicate_ids)} 个；索引会用 event_key 区分，但人工引用时需留意。"
        )
        for event_id in cross_file_duplicate_ids[:10]:
            locations = [
                f"{event['source_file']}:{event['source_line']}"
                for event in event_id_groups[event_id]
            ]
            findings.append(f"  - `{event_id}`: {', '.join(locations)}")

    for event in events:
        if not str(event["event_id"]).startswith("FBK-"):
            continue
        missing = [
            label
            for label, key in [("反馈类型", "feedback_type"), ("证据等级", "evidence_level"), ("核实状态", "verification_status")]
            if not str(event.get(key, "")).strip()
        ]
        if missing:
            findings.append(
                f"- `FBK` 缺少必填字段 {', '.join(missing)}: {event['source_file']}:{event['source_line']} `{event['event_id']}`"
            )
        related_members = str(event.get("related_members", "")).strip()
        if related_members:
            back_refs = [
                item
                for item in events
                if item["owner_type"] == "member" and str(event["event_id"]) in str(item.get("related_event", ""))
            ]
            if not back_refs:
                findings.append(
                    f"- `FBK` 涉及成员但未发现成员侧关联记录: {event['source_file']}:{event['source_line']} `{event['event_id']}`"
                )

    for event in events:
        refs = re.findall(EVENT_ID_PATTERN, str(event.get("related_event", "")))
        for ref in refs:
            if ref not in event_ids:
                findings.append(
                    f"- 关联事件不存在: {event['source_file']}:{event['source_line']} `{event['event_id']}` -> `{ref}`"
                )
        if (event.get("owner_type") == "member" and any(ref.startswith("FBK-") for ref in refs)
                and not event.get("canonical_event_key") and "关联" not in str(event.get("title", ""))):
            findings.append(
                f"- 成员记录引用了反馈但未标明独立观察或关联摘要，请确认来源关系: {event['source_file']}:{event['source_line']} `{event['event_id']}`"
            )

    findings.extend(check_source_provenance(data_dir, events))

    task_file = data_dir / "tasks" / "tasks.md"
    tasks = parse_tasks_md(task_file)
    for task in tasks:
        if is_task_placeholder(task.body or task.title):
            findings.append(f"- 历史待办 `{task.task_id}` 来自占位内容 `{task.body or task.title}`，请清理。")
        for source_event in task.source_events:
            if source_event and source_event != "无" and source_event not in event_ids:
                findings.append(f"- 待办 `{task.task_id}` 来源事件不存在: `{source_event}`")
        for source_file in task.source_files:
            raw_path = source_file.split(":", 1)[0]
            if raw_path and raw_path != "无" and not (data_dir / raw_path).exists():
                findings.append(f"- 待办 `{task.task_id}` 来源文件不存在: `{source_file}`")

    low_evidence_patterns = ["证据等级**: 线索", "证据等级**: 反馈", "线索级", "反馈级"]
    members_dir = data_dir / "members"
    if members_dir.exists():
        for distill in members_dir.glob("member-*/distill.md"):
            text = distill.read_text(encoding="utf-8", errors="replace")
            if any(pattern in text for pattern in low_evidence_patterns):
                findings.append(f"- 成员蒸馏中出现低证据等级内容，请确认未作为长期结论: {rel_path(distill, data_dir)}")

    if findings:
        lines.extend(findings)
    else:
        lines.append("未发现明显一致性问题。")
    return lines


def check_online_notebook(skill_dir: Path, data_dir: Path, online: bool) -> list[str]:
    lines = ["", "## 在线笔记同步检查", ""]
    try:
        config = load_notebook_config(skill_dir, required=False)
    except NotebookSyncError as exc:
        return lines + [f"- 配置错误: {exc}"]
    if not config:
        return lines + ["- 状态: 关闭；现有本地工作流不受影响。"]

    lines.extend(
        [
            f"- 平台: `{config.get('provider')}`",
            f"- 模式: `{config.get('mode')}`",
            f"- 仓库 ID: `{config.get('repository-id')}`",
            f"- 远端根页面: `{config.get('remote', {}).get('root-page-id', '缺失')}`",
            f"- 定时同步: `{'开启' if config.get('schedule', {}).get('enabled') else '关闭'}`",
        ]
    )
    remote = config.get("remote", {})
    required_ids = ["root-page-id", "manifest-page-id", "lock-page-id", "previous-folder-id"]
    missing = [key for key in required_ids if not remote.get(key)]
    if missing:
        lines.append(f"- 必须修复：配置缺少远端 ID: `{', '.join(missing)}`")

    credential = config.get("credential", {})
    if online:
        try:
            resolve_token(config)
            lines.append("- 凭据: 可读取（未显示内容）")
        except ProviderError as exc:
            lines.append(f"- 必须修复：凭据错误: {exc}")
    elif credential.get("type") == "env":
        name = str(credential.get("name", ""))
        lines.append(f"- 凭据引用: 环境变量 `{name}`（{'当前存在' if os.environ.get(name) else '当前未设置'}）")
    else:
        lines.append("- 凭据引用: macOS 钥匙串（未读取内容）")

    state = load_notebook_state(data_dir)
    open_conflicts = [item for item in state.get("conflicts", {}).values() if item.get("status") == "open"]
    pending_deletions = [item for item in state.get("deletions", {}).values() if item.get("status") == "pending"]
    lines.append(f"- 开放冲突: {len(open_conflicts)}")
    lines.append(f"- 待确认删除: {len(pending_deletions)}")
    lines.append(f"- 待同步离线写入: {len(state.get('pending-local', []))}")
    lines.append(f"- 上次同步: `{state.get('last-sync-at') or '从未'}`")

    unsupported: list[str] = []
    for path, source in discover_sync_files(skill_dir, data_dir).items():
        findings = unsupported_markdown(source.read_text(encoding="utf-8", errors="replace"))
        if findings:
            unsupported.append(f"`{path}`: {', '.join(findings)}")
    if unsupported:
        lines.append("- 以下本地内容将以纯文本展示，原文仍正常备份：")
        lines.extend(f"  - {item}" for item in unsupported)

    if not online:
        lines.append("- 远端实时检查: 未执行；使用 `doctor.py --online` 验证 API、manifest 和事务状态。")
        return lines
    try:
        provider = provider_from_config(config)
        provider.verify()
        manifest_candidates: list[tuple[int, int, dict[str, object]]] = []
        manifest_failures: list[str] = []
        manifest_ids = [str(remote["manifest-page-id"])]
        if remote.get("manifest-shadow-page-id"):
            manifest_ids.append(str(remote["manifest-shadow-page-id"]))
        else:
            lines.append("- manifest 备用槽: 未登记；下次 sync 会自动发现或创建。")
        for manifest_id in dict.fromkeys(manifest_ids):
            try:
                page = provider.read_page(manifest_id)
                if page.truncated or page.unknown_block_ids:
                    raise NotebookSyncError("页面不完整或含未知块")
                try:
                    candidate = decode_json_page(page.markdown, MANIFEST_KIND)
                except NotebookSyncError:
                    candidate = decode_json_page(page.markdown, LEGACY_MANIFEST_KIND)
                manifest_candidates.append(
                    (
                        int(candidate.get("manifest-write-sequence", 0)),
                        int(candidate.get("revision", 0)),
                        candidate,
                    )
                )
            except (NotebookSyncError, ProviderError, TypeError, ValueError) as exc:
                manifest_failures.append(f"{manifest_id}: {exc}")
        if not manifest_candidates:
            lines.append("- 必须修复：远端 manifest 无可用完整副本: " + "; ".join(manifest_failures))
            return lines
        legacy_candidates = [item for item in manifest_candidates if item[2].get("kind") == LEGACY_MANIFEST_KIND]
        if legacy_candidates:
            if any(item[2].get("kind") == MANIFEST_KIND and not item[2].get("migration-pending") for item in manifest_candidates):
                return lines + ["- 必须修复：新旧 manifest 混用且缺少升级屏障，请停止普通写入并核对远端状态。"]
            manifest_candidates = legacy_candidates
            lines.append("- 旧版备份协议：可恢复渲染副本；新版 sync 将安全升级并补齐原文载荷。")
        newest_key = max((item[0], item[1]) for item in manifest_candidates)
        newest = [item for item in manifest_candidates if (item[0], item[1]) == newest_key]
        if any(item[2] != newest[0][2] for item in newest[1:]):
            lines.append("- 必须修复：manifest 主槽与备用槽的最新写序号相同但内容不同，必须先人工核对。")
            return lines
        _, _, manifest = newest[0]
        if manifest_failures:
            lines.append("- manifest 冗余性降级，仍有一个可用副本: " + "; ".join(manifest_failures))
        if manifest.get("repository-id") != config.get("repository-id"):
            lines.append("- 必须修复：远端 manifest 的仓库 ID 与本地不一致。")
        else:
            lines.append(f"- 远端 manifest: 正常，修订 `{manifest.get('revision', 0)}`")
        if manifest.get("transaction"):
            lines.append(f"- 必须修复：未完成远端事务: `{manifest['transaction'].get('id', 'unknown')}`；下次 sync 将先回滚。")
        cleanup_pending = manifest.get("cleanup-pending", [])
        if cleanup_pending:
            lines.append(f"- 已提交但待清理的远端旧页: {len(cleanup_pending)}")
        missing_entries = [path for path, item in manifest.get("files", {}).items() if not item.get("parts") and not item.get("tombstone")]
        if missing_entries:
            lines.append(f"- manifest 中缺少页面分片的文件: `{', '.join(missing_entries[:10])}`")
        page_owners: dict[str, str] = {}
        page_findings: list[str] = []
        drifted: list[str] = []
        for path, item in manifest.get("files", {}).items():
            for version_key in ("source", "previous-source"):
                source = item.get(version_key)
                if source:
                    try:
                        pages = []
                        for part in source.get("parts", []):
                            page = provider.read_page(str(part.get("page-id", "")))
                            if page.truncated or page.unknown_block_ids:
                                raise NotebookSyncError("载荷页不完整或含未知块")
                            pages.append(page.markdown)
                        decode_source_payload(path, source, pages)
                    except (NotebookSyncError, ProviderError, KeyError, TypeError, AttributeError) as exc:
                        page_findings.append(f"`{path}` 的 {version_key} 原文校验失败: {exc}")
                elif version_key == "source" and item.get("source-fidelity") != "legacy-rendered" and manifest.get("kind") == MANIFEST_KIND:
                    page_findings.append(f"`{path}` 缺少必需的原文恢复载荷")
            if item.get("tombstone"):
                pending = [
                    deletion
                    for deletion in manifest.get("deletions", {}).values()
                    if deletion.get("path") == path and deletion.get("status") == "pending"
                ]
                if not pending:
                    page_findings.append(f"`{path}` 有墓碑但缺少待确认删除记录")
                continue
            parts = list(item.get("parts", []))
            names = [str(part.get("name", "main")) for part in parts]
            if len(names) != len(set(names)):
                page_findings.append(f"`{path}` 含重复分片名")
            orders = [part.get("order") for part in parts]
            try:
                invalid_order = any(order is not None for order in orders) and (
                    any(order is None for order in orders)
                    or sorted(int(order) for order in orders) != list(range(len(parts)))
                )
            except (TypeError, ValueError):
                invalid_order = True
            if invalid_order:
                page_findings.append(f"`{path}` 分片顺序号不连续")
            independent_previous = list(item.get("previous-parts", []))
            for part in item.get("parts", []):
                page_id = str(part.get("page-id") or "")
                if not page_id:
                    page_findings.append(f"`{path}` 有分片缺少 page-id")
                    continue
                if not independent_previous and not part.get("previous-page-id"):
                    page_findings.append(f"`{path}` 分片 `{part.get('name', 'main')}` 缺少上一版页面")
                if page_id in page_owners and page_owners[page_id] != path:
                    page_findings.append(f"页面 `{page_id}` 同时映射到 `{page_owners[page_id]}` 和 `{path}`")
                    continue
                page_owners[page_id] = path
                remote_part = provider.read_page(page_id)
                if remote_part.truncated or remote_part.unknown_block_ids:
                    page_findings.append(f"`{path}` 分片 `{part.get('name', 'main')}` 被截断或含未知块")
                    continue
                expected_hash = part.get("remote-hash")
                if expected_hash and content_hash(remote_part.markdown) != expected_hash:
                    drifted.append(f"`{path}` / `{part.get('name', 'main')}`")
            for part in independent_previous:
                previous_page_id = str(part.get("page-id") or "")
                if not previous_page_id:
                    page_findings.append(f"`{path}` 的上一版分片缺少 page-id")
                    continue
                owner = f"{path}#previous"
                if previous_page_id in page_owners and page_owners[previous_page_id] != owner:
                    page_findings.append(f"页面 `{previous_page_id}` 被重复映射")
                    continue
                page_owners[previous_page_id] = owner
                previous_page = provider.read_page(previous_page_id)
                if previous_page.truncated or previous_page.unknown_block_ids:
                    page_findings.append(f"`{path}` 的上一版分片被截断或含未知块")
        if page_findings:
            lines.append("- 必须修复：远端内容完整性问题：")
            lines.extend(f"  - {item}" for item in page_findings[:20])
        else:
            lines.append(f"- 远端内容分片: 已检查 {len(page_owners)} 个，未发现截断或重复映射")
        if drifted:
            lines.append(f"- 在线内容与已提交摘要不同（可能是正常在线编辑，sync 时将三方比较）: {', '.join(drifted[:20])}")
    except (NotebookSyncError, ProviderError, KeyError) as exc:
        lines.append(f"- 必须修复：远端实时检查失败: {exc}")
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(description="Check Team Memory root lock, data paths, and duplicate data directories.")
    parser.add_argument("--skill-dir", default=None, help="team-memory skill directory")
    parser.add_argument("--online", action="store_true", help="also verify notebook API, remote manifest, and transaction state")
    args = parser.parse_args()

    skill_dir = resolve_skill_dir(args.skill_dir)
    lock = read_root_lock(skill_dir)
    primary_data_dir: Path | None = None
    lock_error = ""
    paths = None

    try:
        paths = resolve_paths(skill_dir, require_lock=bool(lock), allow_missing_data=True)
        primary_data_dir = paths.data_dir
    except TeamMemoryPathError as exc:
        lock_error = str(exc)

    candidates = candidate_data_dirs(skill_dir)
    lines: list[str] = [
        "# Team Memory 主库检查报告",
        "",
        f"- 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"- Skill 目录: `{skill_dir}`",
        f"- 主库锁定文件: `{skill_dir / '.team-memory-root.json'}`",
        f"- 锁定状态: {'已锁定' if lock else '未锁定'}",
    ]

    if primary_data_dir:
        members, events, primary_ids = data_stats(primary_data_dir)
        lines.extend(
            [
                f"- 当前主库: `{primary_data_dir}`",
                f"- 主库成员数: {members}",
                f"- 主库事件总数: {events}",
                f"- 主库唯一事件 ID 数: {len(primary_ids)}",
            ]
        )
    else:
        primary_ids = set()
        lines.append("- 当前主库: 未确认")

    config_data_path = read_config_data_path(skill_dir / "skill-config.yaml")
    yaml_findings = check_yaml_safety(skill_dir / "skill-config.yaml")
    if yaml_findings:
        lines.extend(["", "## 配置语法检查", ""])
        lines.extend(yaml_findings)
    if config_data_path:
        lines.append(f"- skill-config.yaml data-path: `{config_data_path}`")
    if lock_error:
        lines.extend(["", "## 锁定/配置问题", "", f"- {lock_error}"])
    if paths and paths.warnings:
        lines.extend(["", "## 警告", ""])
        lines.extend(f"- {item}" for item in paths.warnings)

    lines.extend(["", "## 候选数据目录", ""])
    if not candidates:
        lines.append("未发现任何候选数据目录。")
    else:
        lines.extend(["| 位置 | 成员数 | 事件总数 | 唯一事件 ID 数 | 是否主库 |", "|---|---:|---:|---:|---|"])
        for candidate in candidates:
            is_primary = primary_data_dir is not None and same_path(candidate.data_dir, primary_data_dir)
            lines.append(
                f"| `{candidate.data_dir}` | {candidate.members} | {candidate.events} | {candidate.unique_event_ids} | {'是' if is_primary else '否'} |"
            )

    if primary_data_dir and len(candidates) > 1:
        lines.extend(["", "## 多目录差异", ""])
        for candidate in candidates:
            if same_path(candidate.data_dir, primary_data_dir):
                continue
            _, _, ids = data_stats(candidate.data_dir)
            duplicate_ids = sorted(primary_ids.intersection(ids))
            primary_only = sorted(primary_ids - ids)
            candidate_only = sorted(ids - primary_ids)
            lines.extend(
                [
                    f"### {candidate.data_dir}",
                    f"- 与主库重复事件 ID: {len(duplicate_ids)}",
                    f"- 只在主库的事件 ID: {len(primary_only)}",
                    f"- 只在该目录的事件 ID: {len(candidate_only)}",
                ]
            )
            if duplicate_ids:
                lines.append(f"- 重复样例: `{', '.join(duplicate_ids[:10])}`")
            if candidate_only:
                lines.append(f"- 该目录独有样例: `{', '.join(candidate_only[:10])}`")

    if primary_data_dir and primary_data_dir.exists():
        lines.extend(check_data_consistency(primary_data_dir, paths.config_path if paths else None))
        lines.extend(check_online_notebook(skill_dir, primary_data_dir, args.online))

    lines.extend(
        [
            "",
            "## 建议",
            "",
            "- 没有主库锁定文件时，不要写入；先运行 `scripts/init.sh` 或 `scripts/adopt-data.py`。",
            "- 发现多套数据时，不要自动合并；先确认哪一套是主库。",
            "- SQLite/JSONL 只作为可重建索引，Markdown 才是可信源。",
        ]
    )

    report_path = write_report(skill_dir, primary_data_dir, lines)
    if paths:
        print_warnings(paths.warnings)
    print(f"检查报告: {report_path}")
    if primary_data_dir:
        print(f"当前主库: {primary_data_dir}")
    if lock_error:
        print(f"ERROR: {lock_error}")
        return 1
    if candidates:
        print("候选数据目录:")
        for candidate in candidates:
            marker = " (主库)" if primary_data_dir and same_path(candidate.data_dir, primary_data_dir) else ""
            print(
                f"- {candidate.data_dir}{marker}: 成员 {candidate.members}, "
                f"事件 {candidate.events}, 唯一事件 ID {candidate.unique_event_ids}"
            )
    fatal_findings = [line for line in lines if line.startswith("- 必须修复：")]
    if fatal_findings:
        print(f"ERROR: 发现 {len(fatal_findings)} 个必须修复项，详见报告。")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
