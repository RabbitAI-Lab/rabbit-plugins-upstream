from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any


LOCK_FILE = ".team-memory-root.json"
SCHEMA_VERSION = "2.2"
LEGACY_ROOTS = [
    Path.home() / ".config" / "opencode" / "skills" / "team-memory",
    Path.home() / ".openclaw" / "workspace" / "skills" / "team-memory",
]


class TeamMemoryPathError(RuntimeError):
    pass


@dataclass
class CandidateDataDir:
    label: str
    skill_dir: Path
    data_dir: Path
    members: int = 0
    events: int = 0
    unique_event_ids: int = 0


@dataclass
class TeamMemoryPaths:
    skill_dir: Path
    data_dir: Path
    config_path: Path
    lock_path: Path
    warnings: list[str] = field(default_factory=list)


def now_stamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def script_skill_dir() -> Path:
    return Path(__file__).resolve().parents[1]


def resolve_skill_dir(explicit: str | Path | None = None) -> Path:
    if explicit:
        return Path(explicit).expanduser().resolve()
    env_skill_dir = os.environ.get("TEAM_MEMORY_DIR")
    if env_skill_dir:
        return Path(env_skill_dir).expanduser().resolve()
    cwd = Path.cwd().resolve()
    if (cwd / "SKILL.md").exists():
        return cwd
    return script_skill_dir().resolve()


def rel_path(path: Path, base: Path) -> str:
    try:
        return str(path.resolve().relative_to(base.resolve()))
    except ValueError:
        return str(path.resolve())


def portable_data_path(skill_dir: Path, data_dir: Path) -> str:
    try:
        return str(data_dir.resolve().relative_to(skill_dir.resolve()))
    except ValueError:
        return str(data_dir.resolve())


def resolve_data_path(raw: str, skill_dir: Path) -> Path:
    expanded = Path(os.path.expandvars(raw)).expanduser()
    if expanded.is_absolute():
        return expanded.resolve()
    return (skill_dir / expanded).resolve()


def same_path(left: Path, right: Path) -> bool:
    return left.expanduser().resolve() == right.expanduser().resolve()


def read_root_lock(skill_dir: Path) -> dict[str, Any] | None:
    path = skill_dir / LOCK_FILE
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise TeamMemoryPathError(f"主库锁定文件无法解析: {path} ({exc})") from exc


def write_root_lock(skill_dir: Path, data_dir: Path, reason: str) -> Path:
    skill_dir = skill_dir.resolve()
    data_dir = data_dir.resolve()
    path = skill_dir / LOCK_FILE
    existing = read_root_lock(skill_dir)
    created_at = existing.get("created-at") if existing else now_stamp()
    payload = {
        "schema-version": SCHEMA_VERSION,
        "created-at": created_at,
        "updated-at": now_stamp(),
        "skill-root": str(skill_dir),
        "data-dir": portable_data_path(skill_dir, data_dir),
        "data-dir-resolved": str(data_dir),
        "source-of-truth": "markdown",
        "machine-index": ["data/.index/events.jsonl", "data/.index/tasks.jsonl", "data/.index/team-memory.sqlite"],
        "note": reason,
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path


def read_config_data_path(config_path: Path) -> str | None:
    if not config_path.exists():
        return None
    in_settings = False
    settings_indent: int | None = None
    for line in config_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        indent = len(line) - len(line.lstrip(" "))
        if re.match(r"^settings:\s*$", stripped):
            in_settings = True
            settings_indent = indent
            continue
        if in_settings and settings_indent is not None and indent <= settings_indent and not line.startswith(" "):
            in_settings = False
        if in_settings and stripped.startswith("data-path:"):
            raw = stripped.split(":", 1)[1].strip()
            if (raw.startswith('"') and raw.endswith('"')) or (raw.startswith("'") and raw.endswith("'")):
                raw = raw[1:-1]
            return raw
    return None


def update_config_data_path(config_path: Path, skill_dir: Path, data_dir: Path) -> bool:
    if not config_path.exists():
        return False
    value = portable_data_path(skill_dir, data_dir)
    lines = config_path.read_text(encoding="utf-8").splitlines()
    output: list[str] = []
    in_settings = False
    settings_indent: int | None = None
    replaced = False
    inserted = False

    for idx, line in enumerate(lines):
        stripped = line.strip()
        indent = len(line) - len(line.lstrip(" "))
        if re.match(r"^settings:\s*$", stripped):
            in_settings = True
            settings_indent = indent
            output.append(line)
            continue
        if in_settings and settings_indent is not None and indent <= settings_indent and stripped and not line.startswith(" "):
            if not replaced and not inserted:
                output.append(f"  data-path: \"{value}\"")
                inserted = True
            in_settings = False
        if in_settings and stripped.startswith("data-path:"):
            output.append(f"{line[:indent]}data-path: \"{value}\"")
            replaced = True
            continue
        output.append(line)

    if in_settings and not replaced and not inserted:
        output.append(f"  data-path: \"{value}\"")
        inserted = True
    if not any(re.match(r"^settings:\s*$", line.strip()) for line in lines):
        output.extend(["", "settings:", f"  data-path: \"{value}\""])
        inserted = True

    if replaced or inserted:
        config_path.write_text("\n".join(output) + "\n", encoding="utf-8")
    return replaced or inserted


def event_ids_from_timeline(path: Path) -> list[str]:
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8", errors="replace")
    return re.findall(r"\[((?:OBS|DLG|FBK)-[A-Z0-9-]+)\]", text)


def data_stats(data_dir: Path) -> tuple[int, int, set[str]]:
    members_dir = data_dir / "members"
    member_keys: set[str] = set()
    event_ids: set[str] = set()
    event_count = 0
    if members_dir.exists():
        for child in members_dir.iterdir():
            if child.is_dir() and child.name.startswith("member-"):
                member_keys.add(child.name)
                ids = event_ids_from_timeline(child / "timeline.md")
                event_count += len(ids)
                event_ids.update(ids)
            elif child.is_file() and child.name.endswith("-时间轴.md"):
                member_keys.add(child.name.removesuffix("-时间轴.md"))
                ids = event_ids_from_timeline(child)
                event_count += len(ids)
                event_ids.update(ids)
    stakeholders_dir = data_dir / "stakeholders"
    if stakeholders_dir.exists():
        for child in stakeholders_dir.iterdir():
            if child.is_dir() and child.name.startswith("stakeholder-"):
                ids = event_ids_from_timeline(child / "timeline.md")
                event_count += len(ids)
                event_ids.update(ids)
    return len(member_keys), event_count, event_ids


def has_data_content(data_dir: Path) -> bool:
    members, events, _ = data_stats(data_dir)
    if members or events:
        return True
    return any((data_dir / name).exists() for name in ["members", "stakeholders", "import", "upward", "company"])


def candidate_data_dirs(skill_dir: Path) -> list[CandidateDataDir]:
    raw: list[tuple[str, Path]] = [("当前 skill/data", skill_dir / "data")]
    env_data = os.environ.get("TEAM_MEMORY_DATA_DIR")
    if env_data:
        raw.append(("TEAM_MEMORY_DATA_DIR", Path(env_data).expanduser()))
    for root in LEGACY_ROOTS:
        raw.append((f"兼容候选 {root}", root / "data"))

    seen: set[Path] = set()
    candidates: list[CandidateDataDir] = []
    for label, data_dir in raw:
        data_dir = data_dir.resolve()
        if data_dir in seen or not data_dir.exists():
            continue
        seen.add(data_dir)
        members, events, event_ids = data_stats(data_dir)
        candidates.append(
            CandidateDataDir(
                label=label,
                skill_dir=data_dir.parent,
                data_dir=data_dir,
                members=members,
                events=events,
                unique_event_ids=len(event_ids),
            )
        )
    return candidates


def validate_config_data_path(config_path: Path, skill_dir: Path, data_dir: Path) -> None:
    raw = read_config_data_path(config_path)
    if not raw:
        return
    configured = resolve_data_path(raw, skill_dir)
    if not same_path(configured, data_dir):
        raise TeamMemoryPathError(
            "skill-config.yaml 的 settings.data-path 与主库锁定文件冲突。\n"
            f"- config data-path: {raw} -> {configured}\n"
            f"- locked data-dir: {data_dir}\n"
            "请先运行 scripts/doctor.py 检查，再用 scripts/adopt-data.py 固定唯一主库。"
        )


def resolve_paths(
    explicit_skill_dir: str | Path | None = None,
    require_lock: bool = True,
    allow_missing_data: bool = False,
) -> TeamMemoryPaths:
    skill_dir = resolve_skill_dir(explicit_skill_dir)
    lock_path = skill_dir / LOCK_FILE
    config_path = skill_dir / "skill-config.yaml"
    lock = read_root_lock(skill_dir)

    if not lock:
        if require_lock:
            raise TeamMemoryPathError(
                f"缺少主库锁定文件: {lock_path}\n"
                "为避免写错位置，已停止。首次使用请运行 scripts/init.sh；"
                "已有 data/ 时请运行 scripts/adopt-data.py。"
            )
        data_dir = (skill_dir / "data").resolve()
    else:
        raw_data_dir = lock.get("data-dir")
        if not raw_data_dir:
            raise TeamMemoryPathError(f"主库锁定文件缺少 data-dir: {lock_path}")
        data_dir = resolve_data_path(str(raw_data_dir), skill_dir)

    if not data_dir.exists() and not allow_missing_data:
        raise TeamMemoryPathError(f"主数据目录不存在: {data_dir}")

    validate_config_data_path(config_path, skill_dir, data_dir)

    warnings: list[str] = []
    for candidate in candidate_data_dirs(skill_dir):
        if same_path(candidate.data_dir, data_dir):
            continue
        if candidate.members or candidate.events:
            warnings.append(
                "发现另一套 Team Memory 数据，当前脚本不会使用它: "
                f"{candidate.data_dir}（成员 {candidate.members}，事件 {candidate.events}，唯一事件 ID {candidate.unique_event_ids}）"
            )

    return TeamMemoryPaths(
        skill_dir=skill_dir,
        data_dir=data_dir,
        config_path=config_path,
        lock_path=lock_path,
        warnings=warnings,
    )


def print_warnings(warnings: list[str]) -> None:
    for warning in warnings:
        print(f"WARNING: {warning}", file=os.sys.stderr)
