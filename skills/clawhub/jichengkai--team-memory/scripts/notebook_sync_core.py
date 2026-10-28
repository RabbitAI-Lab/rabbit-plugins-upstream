from __future__ import annotations

import base64
import binascii
import hashlib
import json
import os
import re
import socket
import uuid
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Iterable

from team_memory_paths import TeamMemoryPathError, TeamMemoryWriteLock
from memory_events import EVENT_ID_PATTERN


NOTEBOOK_CONFIG = ".team-memory-notebook.json"
NOTEBOOK_SCHEMA_VERSION = "2.0"
SYNC_DIR = ".sync"
STATE_FILE = "state.json"
LEGACY_MANIFEST_KIND = "team-memory-manifest-v1"
LEGACY_CONTROL_KIND = "team-memory-control-v1"
MANIFEST_KIND = "team-memory-manifest-v2"
CONTROL_KIND = "team-memory-control-v2"
SOURCE_KIND = "team-memory-source-v1"
MAX_MARKDOWN_BYTES = 350_000
SYNC_TOP_LEVEL = {
    "members",
    "stakeholders",
    "upward",
    "company",
    "tasks",
    "archive",
    "insights",
    "manager",
    "sources",
}
EVENT_ID_RE = re.compile(rf"\[({EVENT_ID_PATTERN})\]")
TASK_ID_RE = re.compile(r"^##\s+(TASK-[A-Z0-9-]+)\b", re.MULTILINE)
YEAR_HEADING_RE = re.compile(r"^###\s+(20\d{2})[-年]", re.MULTILINE)


class NotebookSyncError(RuntimeError):
    pass


def utc_now() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z")


def normalize_markdown(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    return text.rstrip("\n") + "\n"


def content_hash(text: str) -> str:
    return hashlib.sha256(normalize_markdown(text).encode("utf-8")).hexdigest()


def bytes_hash(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def file_id(path: str) -> str:
    return hashlib.sha256(path.encode("utf-8")).hexdigest()[:20]


def encode_json_page(payload: dict[str, Any], heading: str) -> str:
    return normalize_markdown(
        f"# {heading}\n\n"
        "此页面由 Team Memory 同步器维护，请勿手工修改下面的 JSON。\n\n"
        "```json\n"
        f"{json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)}\n"
        "```\n"
    )


def decode_json_page(markdown: str, expected_kind: str) -> dict[str, Any]:
    matches = re.findall(r"```json\s*\n(.*?)\n```", markdown, flags=re.DOTALL)
    for raw in matches:
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if isinstance(payload, dict) and payload.get("kind") == expected_kind:
            return payload
    raise NotebookSyncError(f"在线页面缺少有效的 {expected_kind} JSON 数据。")


def config_path(skill_dir: Path) -> Path:
    return skill_dir / NOTEBOOK_CONFIG


def sync_dir(data_dir: Path) -> Path:
    return data_dir / SYNC_DIR


def default_state() -> dict[str, Any]:
    return {
        "schema-version": NOTEBOOK_SCHEMA_VERSION,
        "machine-id": f"{socket.gethostname()}-{uuid.uuid4().hex[:10]}",
        "last-sync-at": None,
        "last-remote-revision": 0,
        "files": {},
        "conflicts": {},
        "deletions": {},
        "pending-local": [],
    }


def load_json(path: Path, default: dict[str, Any] | None = None) -> dict[str, Any]:
    if not path.exists():
        return dict(default or {})
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise NotebookSyncError(f"JSON 文件无法解析: {path} ({exc})") from exc
    if not isinstance(payload, dict):
        raise NotebookSyncError(f"JSON 文件顶层必须是对象: {path}")
    return payload


def atomic_write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    temporary.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(temporary, path)


def load_config(skill_dir: Path, required: bool = True) -> dict[str, Any] | None:
    path = config_path(skill_dir)
    if not path.exists():
        if required:
            raise NotebookSyncError("尚未连接在线笔记。请先运行 notebook-sync.py connect。")
        return None
    config = load_json(path)
    if config.get("notebook-schema-version") not in {"1.0", NOTEBOOK_SCHEMA_VERSION}:
        raise NotebookSyncError("在线笔记配置版本不受支持。")
    if config.get("provider") not in {"notion", "flowus"}:
        raise NotebookSyncError("在线笔记 provider 必须是 notion 或 flowus。")
    if config.get("mode") not in {"backup", "bidirectional"}:
        raise NotebookSyncError("在线笔记 mode 必须是 backup 或 bidirectional。")
    return config


def load_state(data_dir: Path) -> dict[str, Any]:
    path = sync_dir(data_dir) / STATE_FILE
    state = load_json(path, default_state())
    baseline = default_state()
    for key, value in baseline.items():
        state.setdefault(key, value)
    return state


def save_state(data_dir: Path, state: dict[str, Any]) -> None:
    atomic_write_json(sync_dir(data_dir) / STATE_FILE, state)


def relative_sync_path(path: Path, skill_dir: Path, data_dir: Path) -> str:
    if path.resolve() == (skill_dir / "skill-config.yaml").resolve():
        return "skill-config.yaml"
    return f"data/{path.resolve().relative_to(data_dir.resolve())}"


def discover_sync_files(skill_dir: Path, data_dir: Path) -> dict[str, Path]:
    found: dict[str, Path] = {}
    def confined(path: Path, root: Path) -> None:
        try:
            path.resolve().relative_to(root.resolve())
        except ValueError as exc:
            raise NotebookSyncError(f"同步路径通过符号链接越出允许的数据根: {path}") from exc
    skill_config = skill_dir / "skill-config.yaml"
    if skill_config.is_file():
        confined(skill_config, skill_dir)
        found["skill-config.yaml"] = skill_config

    overview = data_dir / "team-memory-overview.md"
    if overview.is_file():
        confined(overview, data_dir)
        found["data/team-memory-overview.md"] = overview

    for top in sorted(SYNC_TOP_LEVEL):
        root = data_dir / top
        if not root.exists():
            continue
        confined(root, data_dir)
        for path in sorted(root.rglob("*.md")):
            if not path.is_file():
                continue
            confined(path, data_dir)
            rel_parts = path.relative_to(data_dir).parts
            if any(part.startswith(".") for part in rel_parts):
                continue
            if rel_parts[:2] == ("archive", "pending-deletions"):
                continue
            found[f"data/{path.relative_to(data_dir)}"] = path
    return found


def unsupported_markdown(text: str) -> list[str]:
    findings: list[str] = []
    patterns = {
        "HTML 标签": r"<(?!https?://)[A-Za-z][^>]*>",
        "Notion/FlowUs 嵌入标记": r"<(?:unknown|mention|page|database)\b",
    }
    for label, pattern in patterns.items():
        if re.search(pattern, text, flags=re.IGNORECASE):
            findings.append(label)
    return findings


@dataclass
class MarkdownPart:
    name: str
    content: str


def source_payload_parts(path: str, raw: bytes, max_bytes: int = 120_000) -> list[MarkdownPart]:
    """Store source bytes independently of the provider's Markdown rendering."""
    if type(max_bytes) is not int or max_bytes < 1 or max_bytes > 120_000:
        raise NotebookSyncError("原文分片大小必须在 1–120000 字节之间。")
    chunks = [raw[idx:idx + max_bytes] for idx in range(0, len(raw), max_bytes)] or [b""]
    result: list[MarkdownPart] = []
    for idx, chunk in enumerate(chunks):
        payload = {
            "kind": SOURCE_KIND, "path": path, "order": idx, "count": len(chunks),
            "file-byte-length": len(raw), "file-sha256": bytes_hash(raw),
            "chunk-byte-length": len(chunk), "chunk-sha256": bytes_hash(chunk),
            "data": base64.b64encode(chunk).decode("ascii"),
        }
        result.append(MarkdownPart(f"source-{idx + 1:03d}", encode_json_page(payload, "Team Memory 原文恢复载荷")))
    return result


def decode_source_payload(path: str, descriptor: dict[str, Any], pages: list[str]) -> bytes:
    if descriptor.get("encoding") != "base64-v1":
        raise NotebookSyncError("原文载荷编码版本不受支持。")
    if type(descriptor.get("byte-length")) is not int or descriptor["byte-length"] < 0:
        raise NotebookSyncError("原文载荷文件长度必须是非负整数。")
    if not isinstance(descriptor.get("sha256"), str) or not re.fullmatch(r"[0-9a-f]{64}", descriptor["sha256"]):
        raise NotebookSyncError("原文载荷 SHA-256 格式无效。")
    parts = descriptor.get("parts")
    if not isinstance(parts, list) or not parts or len(parts) != len(pages):
        raise NotebookSyncError("原文载荷分片缺失或数量不一致。")
    ids = [str(item.get("page-id", "")) for item in parts if isinstance(item, dict)]
    if len(ids) != len(parts) or not all(ids) or len(set(ids)) != len(ids):
        raise NotebookSyncError("原文载荷包含无效或重复页面 ID。")
    names = [item.get("name") for item in parts]
    if not all(isinstance(name, str) and name for name in names) or len(set(names)) != len(names):
        raise NotebookSyncError("原文载荷分片名称无效或重复。")
    if any(type(item.get("order")) is not int for item in parts) or [item.get("order") for item in parts] != list(range(len(parts))):
        raise NotebookSyncError("原文载荷分片顺序不连续。")
    chunks: list[bytes] = []
    for idx, markdown in enumerate(pages):
        payload = decode_json_page(markdown, SOURCE_KIND)
        for key in ("order", "count", "file-byte-length", "chunk-byte-length"):
            if type(payload.get(key)) is not int or payload[key] < (1 if key == "count" else 0):
                raise NotebookSyncError("原文载荷顺序、分片数或长度不是有效整数。")
        if (payload.get("path") != path or payload.get("order") != idx
                or payload.get("count") != len(parts)
                or payload.get("file-byte-length") != descriptor.get("byte-length")
                or payload.get("file-sha256") != descriptor.get("sha256")):
            raise NotebookSyncError("原文载荷路径、分片顺序或文件摘要不一致。")
        try:
            chunk = base64.b64decode(payload["data"], validate=True)
        except (KeyError, ValueError, TypeError, binascii.Error) as exc:
            raise NotebookSyncError("原文载荷包含无效 Base64。") from exc
        if len(chunk) != payload.get("chunk-byte-length") or bytes_hash(chunk) != payload.get("chunk-sha256"):
            raise NotebookSyncError("原文载荷分片长度或 SHA-256 校验失败。")
        chunks.append(chunk)
    raw = b"".join(chunks)
    if len(raw) != descriptor.get("byte-length") or bytes_hash(raw) != descriptor.get("sha256"):
        raise NotebookSyncError("原文载荷文件长度或 SHA-256 校验失败。")
    return raw


def safe_display_markdown(content: str) -> str:
    if not unsupported_markdown(content):
        return content
    longest = max((len(item) for item in re.findall(r"`+", content)), default=0)
    fence = "`" * max(3, longest + 1)
    return f"# 原文展示\n\n以下内容以纯文本显示；完整原文保存在恢复载荷中。\n\n{fence}text\n{content.rstrip(chr(10))}\n{fence}\n"


def _split_utf8(text: str, max_bytes: int) -> list[str]:
    if max_bytes < 4:
        raise NotebookSyncError("Markdown 分片上限至少需要 4 字节。")
    chunks: list[str] = []
    buffer: list[str] = []
    size = 0
    for char in text:
        encoded = len(char.encode("utf-8"))
        if buffer and size + encoded > max_bytes:
            chunks.append("".join(buffer))
            buffer = []
            size = 0
        buffer.append(char)
        size += encoded
    if buffer:
        chunks.append("".join(buffer))
    return chunks


def _split_units(units: list[str], max_bytes: int) -> list[str]:
    chunks: list[str] = []
    buffer = ""
    for unit in units:
        candidates = _split_utf8(unit, max_bytes) if len(unit.encode("utf-8")) > max_bytes else [unit]
        for candidate in candidates:
            if buffer and len((buffer + candidate).encode("utf-8")) > max_bytes:
                chunks.append(buffer)
                buffer = ""
            buffer += candidate
    if buffer:
        chunks.append(buffer)
    return chunks


def _named_parts(chunks: list[str], prefix: str) -> list[MarkdownPart]:
    return [MarkdownPart(name=f"{prefix}-{idx:03d}", content=chunk) for idx, chunk in enumerate(chunks, start=1)]


def _timeline_parts(text: str, max_bytes: int) -> list[MarkdownPart]:
    matches = list(YEAR_HEADING_RE.finditer(text))
    if not matches:
        return []
    preamble = text[: matches[0].start()]
    grouped: list[tuple[str, list[str]]] = []
    for idx, match in enumerate(matches):
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        year = match.group(1)
        section = text[match.start() : end]
        if grouped and grouped[-1][0] == year:
            grouped[-1][1].append(section)
        else:
            grouped.append((year, [section]))
    parts: list[MarkdownPart] = []
    for group_idx, (year, sections) in enumerate(grouped, start=1):
        if group_idx == 1 and preamble:
            sections[0] = preamble + sections[0]
        units: list[str] = []
        for section in sections:
            if len(section.encode("utf-8")) <= max_bytes:
                units.append(section)
                continue
            event_starts = [match.start() for match in re.finditer(rf"(?m)^####\s+.*\[{EVENT_ID_PATTERN}\]\s*$", section)]
            if not event_starts:
                units.extend(section.splitlines(keepends=True))
                continue
            if event_starts[0] > 0:
                units.append(section[: event_starts[0]])
            for event_idx, start in enumerate(event_starts):
                end = event_starts[event_idx + 1] if event_idx + 1 < len(event_starts) else len(section)
                units.append(section[start:end])
        chunks = _split_units(units, max_bytes)
        for chunk_idx, chunk in enumerate(chunks, start=1):
            parts.append(MarkdownPart(f"year-{year}-{group_idx:03d}-{chunk_idx:03d}", chunk))
    return parts


def _section_parts(text: str, max_bytes: int) -> list[MarkdownPart]:
    matches = list(re.finditer(r"^##\s+(.+)$", text, flags=re.MULTILINE))
    if not matches:
        return []
    preamble = text[: matches[0].start()]
    parts: list[MarkdownPart] = []
    for idx, match in enumerate(matches, start=1):
        end = matches[idx].start() if idx < len(matches) else len(text)
        section = text[match.start() : end]
        if idx == 1 and preamble:
            section = preamble + section
        title_hash = hashlib.sha256(match.group(1).encode("utf-8")).hexdigest()[:8]
        for chunk_idx, chunk in enumerate(_split_units(section.splitlines(keepends=True), max_bytes), start=1):
            parts.append(MarkdownPart(f"section-{idx:03d}-{title_hash}-{chunk_idx:03d}", chunk))
    return parts


def split_markdown(path: str, text: str, max_bytes: int = MAX_MARKDOWN_BYTES) -> list[MarkdownPart]:
    text = normalize_markdown(text)
    if len(text.encode("utf-8")) <= max_bytes:
        return [MarkdownPart(name="main", content=text)]

    if path.endswith("timeline.md"):
        year_parts = _timeline_parts(text, max_bytes)
        if year_parts:
            return year_parts

    section_parts = _section_parts(text, max_bytes)
    if section_parts:
        return section_parts
    return _named_parts(_split_units(text.splitlines(keepends=True), max_bytes), "part")


def join_markdown(parts: Iterable[MarkdownPart]) -> str:
    return normalize_markdown("".join(part.content for part in parts))


def extract_record_blocks(text: str) -> tuple[str, dict[str, str], list[str]]:
    marker = re.compile(rf"(?m)^(?=####\s+.*\[{EVENT_ID_PATTERN}\]\s*$|##\s+TASK-[A-Z0-9-]+\b)")
    starts = [match.start() for match in marker.finditer(text)]
    if not starts:
        return normalize_markdown(text), {}, []
    prefix = text[: starts[0]]
    blocks: dict[str, str] = {}
    order: list[str] = []
    for idx, start in enumerate(starts):
        end = starts[idx + 1] if idx + 1 < len(starts) else len(text)
        block = normalize_markdown(text[start:end])
        match = EVENT_ID_RE.search(block) or TASK_ID_RE.search(block)
        if not match:
            continue
        record_id = match.group(1)
        if record_id in blocks:
            raise NotebookSyncError(f"文件内存在重复记录 ID: {record_id}")
        blocks[record_id] = block
        order.append(record_id)
    return normalize_markdown(prefix), blocks, order


def merge_append_only(base: str, local: str, remote: str) -> str | None:
    try:
        base_prefix, base_blocks, base_order = extract_record_blocks(base)
        local_prefix, local_blocks, local_order = extract_record_blocks(local)
        remote_prefix, remote_blocks, remote_order = extract_record_blocks(remote)
    except NotebookSyncError:
        return None
    if not base_blocks or local_prefix != base_prefix or remote_prefix != base_prefix:
        return None
    for record_id, base_block in base_blocks.items():
        if local_blocks.get(record_id) != base_block or remote_blocks.get(record_id) != base_block:
            return None
    combined = dict(base_blocks)
    for record_id in set(local_blocks) | set(remote_blocks):
        local_block = local_blocks.get(record_id)
        remote_block = remote_blocks.get(record_id)
        if local_block is not None and remote_block is not None and local_block != remote_block:
            return None
        combined[record_id] = local_block if local_block is not None else str(remote_block)

    def sort_key(record_id: str) -> tuple[str, str, str]:
        block = combined[record_id]
        date_match = re.search(r"-(\d{8})-", record_id)
        time_match = re.search(r"^####\s+(\d{2}:\d{2})", block)
        return (date_match.group(1) if date_match else "", time_match.group(1) if time_match else "", record_id)

    order = sorted(combined, key=sort_key, reverse=True)
    return normalize_markdown(base_prefix + "".join(combined[item] for item in order))


@dataclass
class SyncAction:
    path: str
    action: str
    reason: str
    local_content: str | None = None
    remote_content: str | None = None
    merged_content: str | None = None
    source_bytes: bytes | None = None


def decide_action(
    path: str,
    local_content: str | None,
    remote_content: str | None,
    file_state: dict[str, Any] | None,
    mode: str,
) -> SyncAction:
    if local_content is None and remote_content is None:
        return SyncAction(path, "noop", "两端均不存在")
    if local_content is not None and remote_content is not None and content_hash(local_content) == content_hash(remote_content):
        current_hash = content_hash(local_content)
        action = (
            "baseline"
            if file_state is None
            or current_hash != file_state.get("local-hash")
            or current_hash != file_state.get("remote-hash")
            else "noop"
        )
        return SyncAction(path, action, "两端内容一致，刷新共同基线", local_content, remote_content)
    if file_state is None:
        if local_content is not None and remote_content is None:
            return SyncAction(path, "push-create", "仅本地存在", local_content=local_content)
        if remote_content is not None and local_content is None:
            action = "pull-create" if mode == "bidirectional" else "remote-drift"
            return SyncAction(path, action, "仅在线存在", remote_content=remote_content)
        if local_content is not None and remote_content is not None:
            if content_hash(local_content) == content_hash(remote_content):
                return SyncAction(path, "baseline", "首次建立共同基线", local_content, remote_content)
            return SyncAction(path, "conflict", "两端在无共同基线时均有不同内容", local_content, remote_content)

    state = file_state or {}
    local_changed = local_content is not None and content_hash(local_content) != state.get("local-hash")
    remote_changed = remote_content is not None and content_hash(remote_content) != state.get("remote-hash")
    local_deleted = local_content is None and state.get("local-hash") is not None
    remote_deleted = remote_content is None and state.get("remote-hash") is not None

    if local_deleted or remote_deleted:
        origin = "local" if local_deleted else "remote"
        return SyncAction(path, "tombstone", f"检测到{origin}端删除", local_content, remote_content)
    if not local_changed and not remote_changed:
        return SyncAction(path, "noop", "无变化", local_content, remote_content)
    if local_changed and not remote_changed:
        return SyncAction(path, "push", "仅本地变化", local_content, remote_content)
    if remote_changed and not local_changed:
        action = "pull" if mode == "bidirectional" else "remote-drift"
        return SyncAction(path, action, "仅在线变化", local_content, remote_content)

    base_path = state.get("base-local-path")
    base = state.get("base-local")
    if base is None and base_path:
        base = ""
    if base is not None and local_content is not None and remote_content is not None:
        merged = merge_append_only(str(base), local_content, remote_content)
        if merged is not None:
            return SyncAction(path, "merge", "双方仅新增不冲突记录", local_content, remote_content, merged)
    return SyncAction(path, "conflict", "双方修改且无法安全自动合并", local_content, remote_content)


def new_manifest(repository_id: str, folders: dict[str, str]) -> dict[str, Any]:
    return {
        "kind": MANIFEST_KIND,
        "notebook-schema-version": NOTEBOOK_SCHEMA_VERSION,
        "repository-id": repository_id,
        "revision": 0,
        "manifest-write-sequence": 0,
        "updated-at": utc_now(),
        "transaction": None,
        "cleanup-pending": [],
        "folders": folders,
        "files": {},
        "deletions": {},
        "conflicts": {},
    }


def conflict_id(path: str) -> str:
    return f"CONFLICT-{datetime.now().strftime('%Y%m%d-%H%M%S')}-{file_id(path)[:8]}-{uuid.uuid4().hex[:6]}"


def deletion_id(path: str) -> str:
    return f"DELETE-{datetime.now().strftime('%Y%m%d-%H%M%S')}-{file_id(path)[:8]}-{uuid.uuid4().hex[:6]}"


def write_conflict(data_dir: Path, action: SyncAction, base: str | None) -> tuple[str, Path]:
    identifier = conflict_id(action.path)
    root = sync_dir(data_dir) / "conflicts" / identifier
    root.mkdir(parents=True, exist_ok=False)
    (root / "local.md").write_bytes(action.source_bytes if action.source_bytes is not None else (action.local_content or "").encode("utf-8"))
    (root / "remote.md").write_bytes((action.remote_content or "").encode("utf-8"))
    (root / "base.md").write_bytes((base or "").encode("utf-8"))
    atomic_write_json(
        root / "meta.json",
        {"id": identifier, "path": action.path, "created-at": utc_now(), "status": "open", "reason": action.reason},
    )
    return identifier, root


def base_paths(data_dir: Path, path: str) -> tuple[Path, Path]:
    base_dir = sync_dir(data_dir) / "bases"
    identifier = file_id(path)
    return base_dir / f"{identifier}.local.md", base_dir / f"{identifier}.remote.md"


def save_bases(data_dir: Path, path: str, local_content: str, remote_content: str) -> dict[str, str]:
    local_path, remote_path = base_paths(data_dir, path)
    local_path.parent.mkdir(parents=True, exist_ok=True)
    local_path.write_text(normalize_markdown(local_content), encoding="utf-8")
    remote_path.write_text(normalize_markdown(remote_content), encoding="utf-8")
    return {
        "base-local-path": str(local_path.relative_to(data_dir)),
        "base-remote-path": str(remote_path.relative_to(data_dir)),
    }


def read_base(data_dir: Path, file_state: dict[str, Any], side: str = "local") -> str | None:
    raw = file_state.get(f"base-{side}-path")
    if not raw:
        return None
    path = data_dir / str(raw)
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")


class LocalSyncLock(TeamMemoryWriteLock):
    def __enter__(self) -> "LocalSyncLock":
        try:
            super().__enter__()
        except TeamMemoryPathError as exc:
            raise NotebookSyncError(str(exc)) from exc
        return self
