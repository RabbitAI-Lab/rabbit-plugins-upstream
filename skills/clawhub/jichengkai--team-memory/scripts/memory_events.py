"""Shared Markdown event/provenance rules; source transcripts are not events."""
from __future__ import annotations

import hashlib
import json
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator


EVENT_PREFIXES = "OBS|DLG|FBK|CMP|REF"
EVENT_ID_PATTERN = rf"(?:{EVENT_PREFIXES})-[A-Z0-9-]+"
EVENT_HEADING_RE = re.compile(rf"^####\s+(.+?)\s+\[({EVENT_ID_PATTERN})\]\s*$")
CLAIM_KINDS = {"对方陈述", "用户观察", "用户判断", "AI推断"}
EVIDENCE_LEVELS = {"线索", "反馈", "事实", "结论"}
VERIFICATION_STATUSES = {"未核实", "待补充", "部分确认", "已确认", "已闭环", "已撤销"}
PROVENANCE_LABELS = {
    "source_id": "来源ID",
    "source_span": "来源位置",
    "speaker": "说话人",
    "claim_kind": "信息性质",
    "canonical_event_key": "主记录",
    "evidence_level": "证据等级",
    "verification_status": "核实状态",
}


@dataclass
class EventBlock:
    event_id: str
    title: str
    date: str
    line: int
    lines: list[str]


def markdown_field(lines: list[str], label: str) -> str:
    pattern = re.compile(rf"^\*\*{re.escape(label)}\*\*\s*[:：]\s*(.*?)\s*$")
    return " / ".join(match.group(1) for line in lines if (match := pattern.match(line.strip())))


def provenance_fields(lines: list[str]) -> dict[str, str]:
    return {key: markdown_field(lines, label) for key, label in PROVENANCE_LABELS.items()}


def independent_evidence(event: dict[str, object]) -> bool:
    """Counts source observations/reports, never reflections or linked copies.

    This does not mean that a report has been independently verified as fact.
    """
    return not (
        event.get("canonical_event_key")
        or not bool(event.get("is_current_revision", True))
        or event.get("event_type") == "manager_reflection"
        or event.get("claim_kind") in {"用户判断", "AI推断"}
    )


def revision_supersessions(data_dir: Path) -> dict[str, str]:
    """Resolve explicit, committed same-key revisions without changing sources.

    An uncommitted item, missing derived event or ambiguous branch cannot retire
    an older event. A new item key is an independent addition to the source.
    """
    sources: dict[str, dict[str, object]] = {}
    for processing in (data_dir / "sources/conversations").glob("*/*/processing.md"):
        try:
            matches = re.findall(r"```json\s*\n(.*?)\n```", processing.read_text(encoding="utf-8"), re.DOTALL)
            metadata = json.loads(matches[0]) if matches else None
            if not isinstance(metadata, dict) or metadata.get("status") not in {"captured", "complete", "applying"}:
                continue
            if metadata.get("source_id") != processing.parent.name:
                continue
            original = (processing.parent / "original.md").read_bytes()
            if hashlib.sha256(original).hexdigest() != metadata.get("content_sha256", metadata.get("raw_sha256")):
                continue
            sources[processing.parent.name] = metadata
        except (OSError, UnicodeError, ValueError, TypeError):
            continue

    blocks_by_path: dict[str, dict[str, str]] = {}

    def committed_events(metadata: dict[str, object]) -> dict[str, str]:
        if metadata.get("status") not in {"applying", "complete"}:
            return {}
        items = metadata.get("items", [])
        committed = metadata.get("committed_keys", [])
        if not isinstance(items, list) or not isinstance(committed, list):
            return {}
        committed = {key for key in committed if isinstance(key, str)}
        result: dict[str, str] = {}
        for item in items:
            if not isinstance(item, dict) or not isinstance(item.get("key"), str) or item["key"] not in committed:
                continue
            relative, event_id = item.get("target_file"), item.get("event_id")
            if not isinstance(relative, str) or not isinstance(event_id, str):
                continue
            path = data_dir / relative
            if (not path.resolve().is_relative_to(data_dir.resolve())
                    or not relative.startswith(("members/", "stakeholders/", "company/", "manager/"))):
                continue
            if relative not in blocks_by_path:
                blocks_by_path[relative] = {
                    block.event_id: provenance_fields(block.lines)["source_id"]
                    for block in iter_event_blocks(path)
                }
            if blocks_by_path[relative].get(event_id) == metadata.get("source_id"):
                result[item["key"]] = f"{relative}:{event_id}"
        return result

    mappings = {source_id: committed_events(metadata) for source_id, metadata in sources.items()}
    candidates: dict[str, set[str]] = defaultdict(set)
    for source_id, metadata in sources.items():
        previous = metadata.get("supersedes")
        if not isinstance(previous, str) or previous not in sources:
            continue
        # Corrupt lineage cannot make both sides disappear from current views.
        seen = {source_id}
        ancestor: object = previous
        while isinstance(ancestor, str) and ancestor in sources and ancestor not in seen:
            seen.add(ancestor)
            ancestor = sources[ancestor].get("supersedes")
        if isinstance(ancestor, str) and ancestor in seen:
            continue
        for item_key, new_event in mappings[source_id].items():
            ancestor = previous
            old_event = ""
            while isinstance(ancestor, str) and ancestor in sources:
                old_event = mappings[ancestor].get(item_key, "")
                if old_event:
                    break
                ancestor = sources[ancestor].get("supersedes")
            if old_event and old_event != new_event:
                candidates[old_event].add(new_event)
    return {old: next(iter(new)) for old, new in candidates.items() if len(new) == 1}


def iter_event_blocks(path: Path) -> Iterator[EventBlock]:
    if not path.is_file():
        return
    current_date = ""
    block: EventBlock | None = None
    fence = ""
    for line_no, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        stripped = line.strip()
        fence_match = re.match(r"^(`{3,}|~{3,})", stripped)
        if fence_match:
            token = fence_match.group(1)
            if not fence:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = ""
            if block:
                block.lines.append(line)
            continue
        if fence:
            if block:
                block.lines.append(line)
            continue
        date_match = re.match(r"^###\s+(\d{4}-\d{2}-\d{2})", stripped)
        heading = EVENT_HEADING_RE.match(stripped)
        if stripped.startswith(("### ", "#### ")):
            if block:
                yield block
                block = None
            if stripped.startswith("### "):
                current_date = date_match.group(1) if date_match else ""
            if heading:
                block = EventBlock(heading.group(2), heading.group(1), current_date, line_no, [line])
        elif block:
            block.lines.append(line)
    if block:
        yield block


def ensure_management_layout(data_dir: Path) -> None:
    """Add new spaces without replacing any existing source or summary."""
    for directory in ["company", "manager", "sources/conversations"]:
        (data_dir / directory).mkdir(parents=True, exist_ok=True)
    defaults = {
        "company/timeline.md": "# 公司信息时间轴\n\n## 时间轴（从新到旧）\n",
        "company/distill.md": "# 公司信息蒸馏\n\n## 当前背景\n\n## 关键变化\n\n## 关联记录\n",
        "manager/reflections.md": "# 管理者思考与反思\n\n> 判断、假设和反思保留来源，不自动作为人员事实。\n\n## 时间轴（从新到旧）\n",
        "manager/distill.md": "# 管理者思考蒸馏\n\n## 当前思考\n\n## 待验证假设\n\n## 关联记录\n",
    }
    for relative, text in defaults.items():
        path = data_dir / relative
        if not path.exists():
            path.write_text(text, encoding="utf-8")
