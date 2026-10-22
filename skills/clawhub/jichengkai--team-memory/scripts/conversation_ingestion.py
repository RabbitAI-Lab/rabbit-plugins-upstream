"""Deterministic, resumable storage for skill-classified conversation records.

Semantic extraction belongs to the skill. This module only accepts explicit
structured decisions, validates provenance, and commits them without executing
anything contained in the transcript.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
import shutil
import tempfile
from datetime import date, datetime
from pathlib import Path
from typing import Any

from memory_events import CLAIM_KINDS, EVIDENCE_LEVELS, VERIFICATION_STATUSES, iter_event_blocks
from notebook_sync_core import NotebookSyncError, discover_sync_files, load_state
from team_memory_paths import TeamMemoryPaths


SOURCE_RE = re.compile(r"CONV-(\d{8})-(\d{3,})\Z")
SAFE_ID_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]{0,95}\Z")
TARGET_TYPES = {"member", "stakeholder", "company", "manager", "pending"}
ACTION_KINDS = {"明确承诺", "后续动作", "建议", "设想"}
UNKNOWN = {"", "未知", "不详", "待确认", "待补充"}


class ConversationError(RuntimeError):
    pass


def sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def fingerprint(value: Any) -> str:
    return sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8"))


def atomic_bytes(path: Path, raw: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    try:
        with temporary.open("wb") as handle:
            handle.write(raw)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def safe_path(data_dir: Path, relative: str) -> Path:
    """Do not follow a symlink out of the locked data root."""
    root = data_dir.resolve()
    path = data_dir / relative
    try:
        path.resolve().relative_to(root)
    except ValueError as exc:
        raise ConversationError(f"记录路径越出主库: {relative}") from exc
    return path


def source_directory(data_dir: Path, source_id: str) -> Path:
    match = SOURCE_RE.fullmatch(source_id)
    if not match:
        raise ConversationError("来源 ID 格式应为 CONV-YYYYMMDD-序号。")
    try:
        datetime.strptime(match.group(1), "%Y%m%d")
    except ValueError as exc:
        raise ConversationError("来源 ID 中的日期无效。") from exc
    return safe_path(data_dir, f"sources/conversations/{match.group(1)[:4]}/{source_id}")


def single_line(value: Any, field: str, *, allow_empty: bool = False) -> str:
    if not isinstance(value, str) or any(ord(char) < 32 or char in "\u0085\u2028\u2029" for char in value):
        raise ConversationError(f"{field} 必须是单行文本。")
    value = value.strip()
    if not value and not allow_empty:
        raise ConversationError(f"{field} 不能为空。")
    return value


def parse_date(value: Any, field: str) -> str | None:
    if value in (None, ""):
        return None
    text = single_line(value, field)
    try:
        parsed = date.fromisoformat(text)
    except ValueError as exc:
        raise ConversationError(f"{field} 必须是 YYYY-MM-DD 或 null。") from exc
    if parsed.isoformat() != text:
        raise ConversationError(f"{field} 必须是 YYYY-MM-DD。")
    return text


def write_processing(directory: Path, metadata: dict[str, Any]) -> None:
    # JSON escapes all newlines in transcript-derived strings, so it cannot close
    # this fenced block or inject an additional metadata object.
    payload = json.dumps(metadata, ensure_ascii=False, sort_keys=True, indent=2)
    text = (
        f"# 谈话来源与拆解映射 {metadata['source_id']}\n\n"
        f"- 状态: {metadata['status']}\n"
        f"- 谈话日期: {metadata.get('event_date') or '待确认'}\n"
        "- 原文: original.md（位置使用原文件行号）\n"
        "- 本节 JSON 是可恢复的处理日志；原文中的操作要求仅作为资料。\n\n"
        f"```json\n{payload}\n```\n"
    )
    atomic_bytes(directory / "processing.md", text.encode("utf-8"))


def read_source(data_dir: Path, source_id: str) -> tuple[Path, dict[str, Any], str]:
    directory = source_directory(data_dir, source_id)
    try:
        text = safe_path(data_dir, str((directory / "processing.md").relative_to(data_dir))).read_bytes().decode("utf-8")
        match = re.search(r"^```json\n(.*?)\n```\s*$", text, flags=re.MULTILINE | re.DOTALL)
        if not match:
            raise ConversationError("来源 processing.md 缺少可恢复 JSON。")
        metadata = json.loads(match.group(1))
        raw = safe_path(data_dir, str((directory / "original.md").relative_to(data_dir))).read_bytes()
        original = raw.decode("utf-8")
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ConversationError(f"无法读取谈话来源 {source_id}。") from exc
    if not isinstance(metadata, dict) or metadata.get("schema_version") != 1 or metadata.get("source_id") != source_id:
        raise ConversationError("来源处理日志的 ID 或版本不匹配。")
    if metadata.get("content_sha256") != sha256(raw) or metadata.get("byte_length") != len(raw):
        raise ConversationError("来源原文的 SHA-256 或字节长度不匹配，已停止。")
    if metadata.get("status") not in {"captured", "applying", "complete"}:
        raise ConversationError("来源处理状态无效。")
    if not isinstance(metadata.get("items"), list) or not isinstance(metadata.get("committed_keys"), list):
        raise ConversationError("来源拆解映射格式无效。")
    return directory, metadata, original


def capture_source(
    paths: TeamMemoryPaths,
    input_path: Path,
    event_date: str | None = None,
    participants: list[str] | None = None,
    supersedes: str | None = None,
) -> dict[str, Any]:
    try:
        raw = input_path.read_bytes()
        raw.decode("utf-8")
    except (OSError, UnicodeError) as exc:
        raise ConversationError("谈话输入必须是可读取的 UTF-8 文本文件。") from exc
    if not raw or not raw.decode("utf-8").strip():
        raise ConversationError("谈话原文不能为空。")
    event_date = parse_date(event_date, "date")
    participant_names = [single_line(name, "participants") for name in participants or []]
    if supersedes:
        read_source(paths.data_dir, supersedes)
    digest = sha256(raw)
    base = safe_path(paths.data_dir, "sources/conversations")
    if base.exists():
        for file in sorted(base.glob("*/*/processing.md")):
            _, existing, _ = read_source(paths.data_dir, file.parent.name)
            if existing["content_sha256"] == digest:
                return {"source_id": existing["source_id"], "duplicate": True, "status": existing["status"], "source_dir": str(file.parent)}
    recorded = datetime.now().astimezone()
    day = (event_date or recorded.date().isoformat()).replace("-", "")
    sequence = 1
    while source_directory(paths.data_dir, f"CONV-{day}-{sequence:03d}").exists():
        sequence += 1
    source_id = f"CONV-{day}-{sequence:03d}"
    directory = source_directory(paths.data_dir, source_id)
    directory.parent.mkdir(parents=True, exist_ok=True)
    metadata: dict[str, Any] = {
        "schema_version": 1,
        "source_id": source_id,
        "content_sha256": digest,
        "byte_length": len(raw),
        "captured_at": recorded.isoformat(timespec="seconds"),
        "event_date": event_date,
        "participants": list(dict.fromkeys(participant_names)),
        "supersedes": supersedes,
        "status": "captured",
        "items": [],
        "committed_keys": [],
        "extraction_sha256": None,
    }
    # Publish original + metadata as one directory rename. A process killed
    # before publication leaves only an ignored temporary directory, so retry
    # can use the same ID rather than accepting an incomplete source.
    staging_base = safe_path(paths.data_dir, ".sync/conversation-capture")
    staging_base.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=f".{source_id}.", dir=staging_base))
    try:
        atomic_bytes(staging / "original.md", raw)
        write_processing(staging, metadata)
        os.replace(staging, directory)
    finally:
        if staging.exists():
            shutil.rmtree(staging)
    return {"source_id": source_id, "duplicate": False, "status": "captured", "source_dir": str(directory)}


def normalize_item(data_dir: Path, metadata: dict[str, Any], original: str, raw: Any) -> dict[str, Any]:
    if not isinstance(raw, dict):
        raise ConversationError("items 中每项必须是 JSON 对象。")
    required = {"key", "target_type", "title", "body", "speaker", "claim_kind", "source_span", "evidence_level", "verification_status", "actions"}
    missing = required - raw.keys()
    if missing:
        raise ConversationError(f"拆解项缺少字段: {', '.join(sorted(missing))}")
    key = single_line(raw["key"], "key")
    if len(key) > 128:
        raise ConversationError("key 最长 128 字符。")
    target_type = single_line(raw["target_type"], "target_type")
    if target_type not in TARGET_TYPES:
        raise ConversationError("target_type 无效。")
    target_id = single_line(raw.get("target_id") or "", "target_id", allow_empty=True)
    if target_id and not SAFE_ID_RE.fullmatch(target_id):
        raise ConversationError("target_id 只能包含字母、数字、连字符和下划线，不能包含路径。")
    title = single_line(raw["title"], "title")
    if not isinstance(raw["body"], str) or not raw["body"].strip():
        raise ConversationError("body 必须是非空文本。")
    body = raw["body"].strip()
    speaker = single_line(raw["speaker"], "speaker", allow_empty=True)
    claim = single_line(raw["claim_kind"], "claim_kind")
    if claim not in CLAIM_KINDS:
        raise ConversationError("claim_kind 无效。")
    span = raw["source_span"]
    if not isinstance(span, list) or len(span) != 2 or any(type(value) is not int for value in span):
        raise ConversationError("source_span 必须是两个整数的数组，按 original.md 的 1 起始行号。")
    if not 1 <= span[0] <= span[1] <= len(original.splitlines()):
        raise ConversationError("source_span 越出谈话原文行号范围。")
    event_date = parse_date(raw.get("event_date"), "event_date") or parse_date(metadata.get("event_date"), "来源日期")
    evidence = single_line(raw["evidence_level"], "evidence_level")
    verification = single_line(raw["verification_status"], "verification_status")
    if evidence not in EVIDENCE_LEVELS or verification not in VERIFICATION_STATUSES:
        raise ConversationError("证据等级或核实状态无效。")
    if claim == "对方陈述" and verification in {"已确认", "已闭环"}:
        raise ConversationError("对方陈述不能自动设为已确认或已闭环；请保留未核实、待补充或部分确认。")
    if claim == "对方陈述" and evidence in {"事实", "结论"}:
        raise ConversationError("对方陈述的证据等级请使用线索或反馈；独立核实后另行更新。")
    if not isinstance(raw["actions"], list):
        raise ConversationError("actions 必须是数组。")
    actions: list[dict[str, str]] = []
    for action in raw["actions"]:
        if not isinstance(action, dict) or not isinstance(action.get("kind"), str) or action["kind"] not in ACTION_KINDS:
            raise ConversationError("action.kind 必须是明确承诺、后续动作、建议或设想。")
        text = single_line(action.get("text"), "action.text")
        if re.search(r"(?:来源|source)\s*[:：]|\[(?:OBS|DLG|FBK|CMP|REF)-", text, flags=re.IGNORECASE):
            raise ConversationError("action.text 不能伪造来源事件标识。")
        priority = action.get("priority", "中")
        if not isinstance(priority, str) or priority not in {"高", "中", "低"}:
            raise ConversationError("action.priority 必须是高、中或低。")
        normalized_action = {"kind": action["kind"], "text": text, "priority": priority}
        if normalized_action not in actions:
            actions.append(normalized_action)
    requested_target = {"target_type": target_type, "target_id": target_id}
    pending: list[str] = []
    if not event_date:
        pending.append("谈话或事件日期待确认")
    if speaker in UNKNOWN:
        pending.append("说话人身份待确认")
    if target_type == "pending":
        pending.append("内容归属待确认")
    elif target_type in {"member", "stakeholder"}:
        prefix = "member-" if target_type == "member" else "stakeholder-"
        base = "members" if target_type == "member" else "stakeholders"
        if not target_id.startswith(prefix) or not safe_path(data_dir, f"{base}/{target_id}").is_dir():
            pending.append("目标身份尚未匹配到现有档案")
    elif target_id and target_id != target_type:
        raise ConversationError(f"{target_type} 的 target_id 应为 {target_type} 或省略。")
    # Reflections retain their original subject, but never become a person's
    # performance fact, rating, or independently counted observation.
    if claim in {"用户判断", "AI推断"}:
        target_type, target_id = "manager", "manager"
        if evidence in {"事实", "结论"}:
            evidence = "线索"
    elif target_type in {"company", "manager"}:
        target_id = target_type
    prefix = {"member": "OBS" if claim == "用户观察" else "DLG", "stakeholder": "FBK", "company": "CMP", "manager": "REF"}.get(target_type)
    event_id = None if pending else f"{prefix}-{event_date.replace('-', '')}-{sha256((metadata['source_id'] + ':' + key).encode('utf-8'))[:12].upper()}"
    target_file = None
    if not pending:
        target_file = {
            "member": f"members/{target_id}/timeline.md",
            "stakeholder": f"stakeholders/{target_id}/timeline.md",
            "company": "company/timeline.md",
            "manager": "manager/reflections.md",
        }[target_type]
        safe_path(data_dir, target_file)
    feedback_type = single_line(raw.get("feedback_type") or "沟通记录", "feedback_type")
    if feedback_type not in {"需求", "投诉", "认可", "风险", "建议", "沟通记录"}:
        raise ConversationError("feedback_type 必须是需求、投诉、认可、风险、建议或沟通记录。")
    return {
        "key": key, "target_type": target_type, "target_id": target_id,
        "requested_target": requested_target, "title": title, "body": body,
        "speaker": speaker, "claim_kind": claim, "source_span": span,
        "event_date": event_date, "evidence_level": evidence,
        "verification_status": verification, "actions": actions,
        "feedback_type": feedback_type if target_type == "stakeholder" else "",
        "event_id": event_id, "target_file": target_file, "pending_reasons": pending,
    }


def render_event(source_id: str, item: dict[str, Any], supersedes: str | None = None) -> str:
    start, end = item["source_span"]
    span = str(start) if start == end else f"{start}-{end}"
    body_label = "思考" if item["target_type"] == "manager" else "事实描述"
    lines = [
        f"### {item['event_date']}", "", f"#### {item['title']} [{item['event_id']}]", "",
        f"**{body_label}**:", *["> " + line for line in item["body"].splitlines()], "",
        f"**来源ID**: {source_id}", f"**来源位置**: {span}", f"**说话人**: {item['speaker']}",
        f"**信息性质**: {item['claim_kind']}", f"**证据等级**: {item['evidence_level']}",
        f"**核实状态**: {item['verification_status']}", "**主记录**:",
    ]
    if item["target_type"] == "stakeholder":
        lines.extend([f"**反馈类型**: {item['feedback_type']}", f"**来源方**: {item['speaker']}"])
    requested = item["requested_target"]
    if requested["target_type"] != item["target_type"]:
        lines.append(f"**关联对象**: {requested['target_type']}:{requested['target_id']}")
    if supersedes:
        lines.append(f"**修订来源**: {supersedes}（保留前版，当前资料不重复累计为独立证明）")
    for kinds, label in [({"明确承诺", "后续动作"}, "追踪项"), ({"建议", "设想"}, "建议与设想")]:
        actions = [action for action in item["actions"] if action["kind"] in kinds]
        if actions:
            lines.extend(["", f"**{label}**:"])
            for action in actions:
                if label == "追踪项":
                    lines.append(f"- [ ] {action['priority']}: {action['text']}（来源: {item['event_id']}）")
                else:
                    lines.append(f"- {action['kind']}: {action['text']}")
    return "\n".join(lines).rstrip() + "\n"


def insert_chronologically(text: str, event: str, event_date: str) -> str:
    """Insert a dated block without rewriting or reordering existing content."""
    headings: list[tuple[int, str]] = []
    boundaries: list[int] = []
    timeline_start: int | None = None
    fence = ""
    offset = 0
    for line in text.splitlines(keepends=True):
        stripped = line.strip()
        fence_match = re.match(r"^(`{3,}|~{3,})", stripped)
        if fence_match:
            token = fence_match.group(1)
            if not fence:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = ""
        elif not fence:
            match = re.match(r"^###\s+(\d{4}-\d{2}-\d{2})(?:\s|$)", stripped)
            if match:
                headings.append((offset, match.group(1)))
            elif re.match(r"^#{1,2}\s", stripped):
                boundaries.append(offset)
                if stripped.startswith("## ") and "时间轴" in stripped:
                    timeline_start = offset + len(line)
        offset += len(line)
    position = len(text)
    for index, existing_date in headings:
        if event_date >= existing_date:
            position = index
            break
    else:
        if headings:
            position = next((index for index in boundaries if index > headings[-1][0]), len(text))
        elif timeline_start is not None:
            position = timeline_start
    before, after = text[:position], text[position:]
    separator = "" if before.endswith(("\n\n", "\r\n\r\n")) else "\n" if before.endswith("\n") else "\n\n"
    return before + separator + event + ("\n" if after else "") + after


def append_once(data_dir: Path, source_id: str, item: dict[str, Any], committed: bool, supersedes: str | None) -> bool:
    path = safe_path(data_dir, item["target_file"])
    text = path.read_bytes().decode("utf-8") if path.exists() else "# 记忆时间轴\n"
    matches = [block for block in iter_event_blocks(path) if block.event_id == item["event_id"]]
    if matches:
        if len(matches) != 1:
            raise ConversationError(f"发现重复事件 ID: {item['event_id']}")
        if committed:
            return False
        expected_lines = render_event(source_id, item, supersedes).splitlines()[2:]
        actual_lines = matches[0].lines
        if "\n".join(actual_lines).rstrip() != "\n".join(expected_lines).rstrip():
            raise ConversationError(f"未完成的导入事件已被修改，保留原内容并停止: {item['event_id']}")
        return False
    if committed:
        raise ConversationError(f"已提交事件缺失，保留用户改动并停止: {item['event_id']}")
    new = insert_chronologically(text, render_event(source_id, item, supersedes), item["event_date"])
    atomic_bytes(path, new.encode("utf-8"))
    return True


def append_summary(data_dir: Path, source_id: str, item: dict[str, Any]) -> None:
    path = safe_path(data_dir, str(Path(item["target_file"]).parent / "distill.md"))
    text = path.read_bytes().decode("utf-8") if path.exists() else "# 来源摘要\n"
    marker = f"<!-- conversation-summary:{source_id}:{item['event_id']} -->"
    if marker in text:
        return
    summary = re.sub(r"\s+", " ", item["body"])[:180]
    note = (
        f"\n{marker}\n\n### 谈话记录摘录 {item['event_date']}\n\n"
        f"> {item['title']}：{summary}\n\n"
        f"信息性质：{item['claim_kind']}；核实状态：{item['verification_status']}。"
        f"来源：{source_id}；事件：[{item['event_id']}]({Path(item['target_file']).name})。\n"
    )
    atomic_bytes(path, (text + note).encode("utf-8"))


def write_pending(directory: Path, metadata: dict[str, Any]) -> None:
    items = [item for item in metadata["items"] if item["pending_reasons"]]
    path = directory / "pending.md"
    lines = ["# 谈话拆解待确认", "", "待确认项不生成正式事件或任务；确认后用同一个 key 重新提交。", ""]
    for item in items:
        lines.extend([f"## {item['title']}", "", f"- 稳定键: {item['key']}", f"- 待确认: {'；'.join(item['pending_reasons'])}",
                      f"- 原文位置: {item['source_span'][0]}-{item['source_span'][1]}", "",
                      *["> " + line for line in item["body"].splitlines()], ""])
    if not items:
        lines.append("无待确认项。")
    # Only replace this generated view's marked area; keep hand-written notes
    # before or after it. The complete recovery data lives in processing.md.
    start = f"<!-- conversation-pending:{metadata['source_id']}:start -->"
    end = f"<!-- conversation-pending:{metadata['source_id']}:end -->"
    generated = start + "\n" + "\n".join(lines) + "\n" + end + "\n"
    existing = path.read_bytes().decode("utf-8") if path.exists() else ""
    if start in existing and end in existing and existing.index(start) < existing.index(end):
        before = existing[:existing.index(start)]
        after = existing[existing.index(end) + len(end):]
        text = before + generated.rstrip("\n") + after
    else:
        text = existing + ("\n\n" if existing else "") + generated
    atomic_bytes(path, text.encode("utf-8"))


def refresh_derived(paths: TeamMemoryPaths) -> None:
    command = [sys.executable, str(paths.skill_dir / "scripts" / "sync-tasks.py"), "--skill-dir", str(paths.skill_dir)]
    completed = subprocess.run(command, check=False, capture_output=True, text=True)
    if completed.returncode:
        raise ConversationError("原文与分类记录已保存，但待办或索引刷新失败；请用相同拆解重试。")


def attempt_backup(paths: TeamMemoryPaths) -> str:
    config_path = paths.skill_dir / ".team-memory-notebook.json"
    if not config_path.exists():
        return "未连接云端备份"
    if os.environ.get("TEAM_MEMORY_WRITE_LOCK_HELD") == "1":
        return "云端待备份（本地保存成功；上层命令仍持有写锁，请在其结束后同步）"
    try:
        config = json.loads(config_path.read_text(encoding="utf-8"))
        if config.get("mode") != "backup":
            return "已保存本地；当前连接为双向模式，请按已有同步流程处理"
        result = subprocess.run(
            [sys.executable, str(paths.skill_dir / "scripts" / "notebook-sync.py"), "--skill-dir", str(paths.skill_dir), "sync"],
            capture_output=True, text=True, check=False, timeout=60,
        )
        if result.returncode:
            return "云端待备份（本地保存成功；连接、网络或云端校验未通过）"
        state = load_state(paths.data_dir)
        files = state.get("files", {})
        if (not state.get("last-sync-at")
                or any(item.get("status") == "open" for item in state.get("conflicts", {}).values())
                or any(files.get(name, {}).get("local-byte-hash") != sha256(file.read_bytes())
                       for name, file in discover_sync_files(paths.skill_dir, paths.data_dir).items())):
            return "云端待备份（本地保存成功；仍有待处理冲突或未完成上传的正文）"
        return "云端备份成功"
    except (OSError, ValueError, TypeError, AttributeError, NotebookSyncError, subprocess.TimeoutExpired):
        # Do not print raw subprocess/API errors: a provider may include tokens.
        return "云端待备份（本地保存成功；备份连接不可用或超时）"


def apply_source(paths: TeamMemoryPaths, source_id: str, extraction: Any, *, dry_run: bool = False) -> dict[str, Any]:
    directory, metadata, original = read_source(paths.data_dir, source_id)
    if not isinstance(extraction, dict) or extraction.get("source_id") != source_id:
        raise ConversationError("拆解 JSON 必须包含与 --source-id 相同的 source_id。")
    if extraction.get("content_sha256", metadata["content_sha256"]) != metadata["content_sha256"]:
        raise ConversationError("拆解 JSON 的来源 SHA-256 不匹配。")
    if not isinstance(extraction.get("items"), list):
        raise ConversationError("拆解 JSON 必须包含 items 数组。")
    normalized = [normalize_item(paths.data_dir, metadata, original, raw) for raw in extraction["items"]]
    keys = [item["key"] for item in normalized]
    if len(keys) != len(set(keys)):
        raise ConversationError("同一来源的拆解 key 不能重复。")
    previous = {item["key"]: item for item in metadata["items"]}
    committed = set(metadata["committed_keys"])
    for item in normalized:
        key = item["key"]
        if key in previous and (key in committed or (metadata["status"] == "applying" and not previous[key]["pending_reasons"])):
            if fingerprint(previous[key]) != fingerprint(item):
                raise ConversationError(f"稳定键 {key} 已提交或正在提交，不能改写；新信息请使用新 key 或新修订来源。")
        previous[key] = item
    items = [previous[key] for key in sorted(previous)]
    result: dict[str, Any] = {"source_id": source_id, "dry_run": dry_run, "new_records": 0,
                              "existing_records": len(committed), "pending": sum(bool(item["pending_reasons"]) for item in items)}
    if dry_run:
        result["new_records"] = sum(not item["pending_reasons"] and item["key"] not in committed for item in items)
        result["items"] = items
        return result
    metadata.update({"status": "applying", "items": items, "extraction_sha256": fingerprint(items)})
    # Write the journal before any derived event. Per-file atomic replacement,
    # stable IDs, and committed_keys make every interruption safely resumable.
    write_processing(directory, metadata)
    for item in items:
        if item["pending_reasons"]:
            continue
        created = append_once(paths.data_dir, source_id, item, item["key"] in committed, metadata.get("supersedes"))
        result["new_records"] += int(created)
        if item["key"] not in committed:
            committed.add(item["key"])
            metadata["committed_keys"] = sorted(committed)
            write_processing(directory, metadata)
        append_summary(paths.data_dir, source_id, item)
    write_pending(directory, metadata)
    refresh_derived(paths)
    metadata["status"] = "complete"
    write_processing(directory, metadata)
    result["status"] = "complete"
    return result
