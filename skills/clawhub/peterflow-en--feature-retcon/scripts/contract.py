#!/usr/bin/env python3
"""Manage a local feature reconciliation contract and its reversible write-ahead journal."""

from __future__ import annotations

import argparse
import base64
import datetime as dt
import difflib
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import uuid


SCHEMA_VERSION = 1
CONTRACT_NAME = "RECONCILIATION.md"
JOURNAL_BEGIN = "<!-- feature-retcon:journal:begin -->"
JOURNAL_END = "<!-- feature-retcon:journal:end -->"
JOURNAL_MARKER = re.compile(rf"^({re.escape(JOURNAL_BEGIN)}|{re.escape(JOURNAL_END)})(?=\r?$)", re.MULTILINE)
MAX_EMBEDDED_PAYLOAD = 10 * 1024 * 1024
STAGES = ("requirements", "design", "tasks", "implementation", "validation")
STATUSES = ("executing", "paused", "blocked", "restoring", "restored", "ready_to_close")
ENTRY_STATUSES = ("prepared", "applied", "restored")
STATUS_TRANSITIONS = {
    "executing": {"paused", "blocked", "restoring"},
    "paused": {"executing", "blocked", "restoring"},
    "blocked": {"executing", "restoring"},
    "restoring": {"blocked"},
    "restored": {"blocked", "restoring"},
    "ready_to_close": {"executing", "blocked", "restoring"},
}

SENSITIVE_NAME_PATTERNS = (
    ("dotenv-file", re.compile(r"(^|/)\.env(?:\.|$)", re.IGNORECASE)),
    ("private-key-file", re.compile(r"(^|/)(?:id_[^/]+|[^/]+\.(?:pem|key|p12|pfx))$", re.IGNORECASE)),
    ("credential-file", re.compile(r"(?:credential|secret|token|password)", re.IGNORECASE)),
)
SENSITIVE_CONTENT_PATTERNS = (
    ("private-key-material", re.compile(rb"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("cloud-access-key", re.compile(rb"\bAKIA[0-9A-Z]{16}\b")),
    ("provider-token", re.compile(rb"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9_-]{20,})\b")),
    ("jwt-token", re.compile(rb"\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\b")),
    ("bearer-token", re.compile(rb"(?im)^\s*authorization\s*[:=]\s*bearer\s+\S+")),
    (
        "credential-assignment",
        re.compile(
            rb"(?im)^\s*(?:password|passwd|secret|client[_-]?secret|token|access[_-]?token|api[_-]?(?:key|token))\s*[:=]"
        ),
    ),
)


class ContractError(RuntimeError):
    """A contract error that can be reported without a traceback."""


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_scalar(value: object) -> str:
    return json.dumps(value, ensure_ascii=False)


def read_regular_file(path: Path) -> tuple[bytes, int]:
    if path.is_symlink():
        raise ContractError(f"Refusing to follow a symbolic link: {path}")
    if not path.is_file():
        raise ContractError(f"Expected a regular file: {path}")
    return path.read_bytes(), stat.S_IMODE(path.stat().st_mode)


def snapshot(path: Path) -> dict[str, object]:
    if not path.exists() and not path.is_symlink():
        return {"exists": False, "sha256": None, "mode": None}
    data, mode = read_regular_file(path)
    return {"exists": True, "sha256": sha256(data), "mode": mode, "data": data}


def public_snapshot(value: dict[str, object]) -> dict[str, object]:
    return {key: value.get(key) for key in ("exists", "sha256", "mode")}


def same_snapshot(left: dict[str, object], right: dict[str, object]) -> bool:
    return public_snapshot(left) == public_snapshot(right)


def encode_payload(data: bytes) -> str:
    return base64.b64encode(gzip.compress(data, compresslevel=9, mtime=0)).decode("ascii")


def decode_payload(payload: str) -> bytes:
    try:
        return gzip.decompress(base64.b64decode(payload.encode("ascii"), validate=True))
    except (ValueError, OSError, EOFError) as exc:
        raise ContractError("Cannot decode a damaged recovery payload") from exc


def detect_sensitive(path: Path, data: bytes | None) -> list[str]:
    normalized = path.as_posix()
    signals = [label for label, pattern in SENSITIVE_NAME_PATTERNS if pattern.search(normalized)]
    if data is not None:
        signals.extend(label for label, pattern in SENSITIVE_CONTENT_PATTERNS if pattern.search(data))
    return sorted(set(signals))


def reverse_diff(path: Path, new_data: bytes, original_data: bytes, sensitive: bool) -> str:
    if sensitive:
        return "[Readable diff omitted for sensitive content. Exact recovery data is retained.]"
    if max(len(new_data), len(original_data)) > 1024 * 1024:
        return "[Readable diff omitted for files over 1 MiB. Exact recovery data is retained.]"
    try:
        new_text = new_data.decode("utf-8").splitlines(keepends=True)
        old_text = original_data.decode("utf-8").splitlines(keepends=True)
    except UnicodeDecodeError:
        return "[Binary or non-UTF-8 file. Use the exact recovery data.]"
    return "".join(
        difflib.unified_diff(
            new_text,
            old_text,
            fromfile=f"{path} (after change)",
            tofile=f"{path} (before change)",
        )
    ) or "[Contents are unchanged. The file mode may have changed.]"


def parse_frontmatter(text: str) -> tuple[dict[str, object], int, int]:
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        raise ContractError("Contract has no YAML frontmatter")
    end = next((index for index in range(1, len(lines)) if lines[index].strip() == "---"), None)
    if end is None:
        raise ContractError("Unclosed YAML frontmatter in contract")
    values: dict[str, object] = {}
    for raw in lines[1:end]:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if ":" not in raw:
            raise ContractError(f"Cannot parse frontmatter line: {raw.strip()}")
        key, value = raw.split(":", 1)
        value = value.strip()
        if value in {"", "null", "~"}:
            parsed: object = None
        else:
            try:
                parsed = json.loads(value)
            except json.JSONDecodeError:
                parsed = value
        values[key.strip()] = parsed
    return values, 0, end


def journal_parts(text: str) -> tuple[str, str, str]:
    parts = JOURNAL_MARKER.split(text)
    if len(parts) != 5 or parts[1] != JOURNAL_BEGIN or parts[3] != JOURNAL_END:
        raise ContractError("Expected exactly one recovery journal block")
    return parts[0], parts[2], parts[4]


def extract_journal(text: str) -> dict[str, object]:
    _, block, _ = journal_parts(text)
    payload = block.strip()
    if payload.startswith("```json") and payload.endswith("```"):
        payload = payload[len("```json") : -len("```")].strip()
    try:
        journal = json.loads(payload)
    except json.JSONDecodeError as exc:
        raise ContractError("Recovery journal is invalid JSON") from exc
    if not isinstance(journal, dict):
        raise ContractError("Recovery journal must be a JSON object")
    return journal


def replace_journal(text: str, journal: dict[str, object]) -> str:
    rendered = json.dumps(journal, ensure_ascii=False, indent=2, sort_keys=True)
    before, _, after = journal_parts(text)
    return f"{before}{JOURNAL_BEGIN}\n```json\n{rendered}\n```\n{JOURNAL_END}{after}"


def set_frontmatter(text: str, key: str, value: object) -> str:
    lines = text.splitlines(keepends=True)
    _, _, end = parse_frontmatter(text)
    prefix = f"{key}:"
    replacement = f"{key}: {json_scalar(value)}\n"
    for index in range(1, end):
        if lines[index].startswith(prefix):
            lines[index] = replacement
            return "".join(lines)
    lines.insert(end, replacement)
    return "".join(lines)


def atomic_write(path: Path, data: bytes, mode: int, *, replace: bool = True) -> None:
    if path.parent.exists() and path.parent.is_symlink():
        raise ContractError(f"Refusing to write through a symlinked directory: {path.parent}")
    if not path.parent.is_dir():
        raise ContractError(f"Parent directory does not exist: {path.parent}")
    descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary_path = Path(temporary)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temporary_path, mode)
        if replace:
            os.replace(temporary_path, path)
        else:
            try:
                os.link(temporary_path, path)
            except FileExistsError as exc:
                raise ContractError(f"Destination already exists: {path}") from exc
    finally:
        if temporary_path.exists():
            temporary_path.unlink()


def write_contract(path: Path, text: str) -> None:
    atomic_write(path, text.encode("utf-8"), 0o600)


def load_contract(path_arg: str) -> tuple[Path, str, dict[str, object], dict[str, object]]:
    raw_path = Path(path_arg).expanduser().absolute()
    if raw_path.is_symlink():
        raise ContractError(f"Refusing to load a symlinked contract: {raw_path}")
    path = raw_path.resolve()
    if path != Path(os.path.abspath(raw_path)):
        raise ContractError(f"Refusing to load a contract through a redirected directory: {raw_path}")
    if path.name != CONTRACT_NAME:
        raise ContractError(f"The contract filename must be {CONTRACT_NAME}")
    if not path.is_file() or path.is_symlink():
        raise ContractError(f"Contract is missing or is not a regular file: {path}")
    text = path.read_text(encoding="utf-8")
    frontmatter, _, _ = parse_frontmatter(text)
    journal = extract_journal(text)
    authority = frontmatter.get("authority_root")
    if not isinstance(authority, str) or Path(authority) != path.parent:
        raise ContractError("Contract location differs from its recorded authority root")
    return path, text, frontmatter, journal


def save_contract(path: Path, text: str, journal: dict[str, object]) -> None:
    write_contract(path, replace_journal(text, journal))


def resolve_target(path_arg: str, writable_roots: list[str], *, recorded: bool = False) -> Path:
    raw_path = Path(path_arg).expanduser().absolute()
    if raw_path.is_symlink():
        raise ContractError(f"Refusing to follow a symbolic link: {raw_path}")
    path = raw_path.resolve(strict=False)
    if path != Path(os.path.abspath(raw_path)):
        raise ContractError(f"Refusing a symbolic link in the target path: {raw_path}")
    roots = [Path(root) for root in writable_roots]
    for root in roots:
        if root.is_symlink() or root.resolve() != root or not root.is_dir():
            raise ContractError(f"The authorized writable root moved or is unavailable: {root}")
    if recorded and path != raw_path:
        raise ContractError(f"The registered target location changed: {raw_path}")
    if not any(path == root or path.is_relative_to(root) for root in roots):
        raise ContractError(f"Target is outside the authorized writable roots: {path}")
    if path.name == CONTRACT_NAME:
        raise ContractError("The contract cannot journal itself")
    return path


def run_git(repo_hint: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[bytes]:
    try:
        result = subprocess.run(
            ["git", "-C", str(repo_hint), *args],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            env={**os.environ, "LC_ALL": "C"},
        )
    except OSError as exc:
        raise ContractError(f"Git is unavailable: {exc}") from exc
    if check and result.returncode != 0:
        message = result.stderr.decode("utf-8", errors="replace").strip()
        raise ContractError(f"Git read failed: {message or 'unknown error'}")
    return result


def git_root(path: Path) -> Path:
    hint = path if path.is_dir() else path.parent
    result = run_git(hint, "rev-parse", "--show-toplevel")
    return Path(result.stdout.decode("utf-8").strip()).resolve()


def observed_git_root(path: Path) -> Path | None:
    if shutil.which("git") is None:
        if any((parent / ".git").exists() for parent in (path, *path.parents)) or any(
            os.environ.get(name) for name in ("GIT_DIR", "GIT_WORK_TREE", "GIT_COMMON_DIR")
        ):
            raise ContractError("Git metadata exists but Git is unavailable to verify its state")
        return None
    result = run_git(path, "rev-parse", "--show-toplevel", check=False)
    if result.returncode == 0:
        return Path(result.stdout.decode("utf-8").strip()).resolve()
    if b"not a git repository" in result.stderr:
        return None
    raise ContractError("Cannot verify Git state: " + result.stderr.decode("utf-8", errors="replace").strip())


def git_blob(repo: Path, reference: str, path: Path) -> tuple[bytes, str]:
    try:
        relative = path.relative_to(repo).as_posix()
    except ValueError as exc:
        raise ContractError(f"File is outside the Git repository: {path}") from exc
    result = run_git(repo, "show", f"{reference}:{relative}")
    return result.stdout, relative


def git_commit(repo: Path, reference: str) -> str:
    if not reference or reference.startswith("-") or any(char in reference for char in "\r\n\x00"):
        raise ContractError("Invalid baseline_ref")
    result = run_git(repo, "rev-parse", "--verify", f"{reference}^{{commit}}")
    commit = result.stdout.decode("ascii", errors="strict").strip().lower()
    if re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", commit) is None:
        raise ContractError("baseline_ref did not resolve to an immutable Git commit")
    return commit


def contract_is_tracked(contract: Path, authority_root: Path) -> bool:
    repo = git_root(authority_root)
    try:
        relative = contract.relative_to(repo).as_posix()
    except ValueError as exc:
        raise ContractError(f"Contract is outside its declared Git repository: {contract}") from exc
    result = run_git(repo, "ls-files", "--stage", "--", relative)
    return bool(result.stdout.strip())


def require_snapshot(value: object, label: str) -> dict[str, object]:
    if not isinstance(value, dict):
        raise ContractError(f"{label} must be an object")
    exists = value.get("exists")
    digest = value.get("sha256")
    mode = value.get("mode")
    if not isinstance(exists, bool):
        raise ContractError(f"{label}.exists must be a boolean")
    if exists:
        if not isinstance(digest, str) or re.fullmatch(r"[0-9a-f]{64}", digest) is None:
            raise ContractError(f"Invalid {label}.sha256")
        if not isinstance(mode, int) or isinstance(mode, bool) or not 0 <= mode <= 0o7777:
            raise ContractError(f"Invalid {label}.mode")
    elif digest is not None or mode is not None:
        raise ContractError(f"{label} has no file: sha256 and mode must be null")
    return value


def require_schema(frontmatter: dict[str, object], journal: dict[str, object]) -> None:
    if type(frontmatter.get("schema_version")) is not int or frontmatter["schema_version"] != SCHEMA_VERSION:
        raise ContractError(f"Only schema_version {SCHEMA_VERSION} is supported")
    if frontmatter.get("status") not in STATUSES:
        raise ContractError("Invalid contract status")
    if frontmatter.get("target_stage") not in STAGES:
        raise ContractError("Invalid contract target_stage")
    if not isinstance(frontmatter.get("round_id"), str) or not frontmatter["round_id"].strip():
        raise ContractError("Contract round_id must be a nonempty string")
    authority = frontmatter.get("authority_root")
    if not isinstance(authority, str) or not Path(authority).is_absolute():
        raise ContractError("Contract authority_root must be an absolute path")
    if frontmatter.get("version_control") not in ("git", "none"):
        raise ContractError("Invalid contract version_control")
    baseline = frontmatter.get("baseline_ref")
    if baseline is not None and (
        not isinstance(baseline, str) or re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", baseline) is None
    ):
        raise ContractError("baseline_ref must be a frozen commit SHA or null")
    completion = frontmatter.get("completion_stage")
    if completion is not None and (
        completion not in STAGES or STAGES.index(completion) < STAGES.index(frontmatter["target_stage"])
    ):
        raise ContractError("completion_stage must cover target_stage")
    if type(journal.get("journal_version")) is not int or journal["journal_version"] != 1:
        raise ContractError("Unsupported recovery journal version")
    roots = journal.get("writable_roots")
    if not isinstance(roots, list) or not roots or not all(
        isinstance(root, str) and Path(root).is_absolute() for root in roots
    ):
        raise ContractError("Recovery journal has no writable_roots")
    entries = journal.get("entries")
    if not isinstance(entries, list):
        raise ContractError("Recovery journal has no entries")
    for index, entry in enumerate(entries, start=1):
        label = f"Journal entry J{index:04d}"
        if not isinstance(entry, dict):
            raise ContractError(f"{label} must be an object")
        if not isinstance(entry.get("id"), str):
            raise ContractError(f"Invalid {label}.id")
        if not isinstance(entry.get("path"), str) or not Path(str(entry["path"])).is_absolute():
            raise ContractError(f"{label}.path must be absolute")
        status_value = entry.get("status")
        if status_value not in ENTRY_STATUSES:
            raise ContractError(f"Invalid {label}.status")
        signals = entry.get("sensitive_signals")
        if not isinstance(signals, list) or not all(isinstance(signal, str) for signal in signals):
            raise ContractError(f"{label}.sensitive_signals must be an array of strings")
        if not isinstance(entry.get("sensitive_authorized"), bool):
            raise ContractError(f"{label}.sensitive_authorized must be a boolean")
        original = require_snapshot(entry.get("original"), f"{label}.original")
        if original.get("exists"):
            recovery = original.get("recovery")
            if recovery == "embed" and not isinstance(original.get("payload"), str):
                raise ContractError(f"Invalid {label}.original.payload")
            if recovery == "git" and not all(
                isinstance(original.get(key), str) for key in ("git_repo", "git_ref", "git_path")
            ):
                raise ContractError(f"Invalid Git recovery source for {label}.original")
            if recovery not in {"embed", "git"}:
                raise ContractError(f"Invalid {label}.original.recovery")
        elif original.get("recovery") != "none":
            raise ContractError(f"Invalid {label}.original.recovery")
        applied = entry.get("applied")
        if status_value == "applied" or applied is not None:
            require_snapshot(applied, f"{label}.applied")
    pending = journal.get("restore_pending")
    if pending is not None:
        remaining = [entry for entry in entries if entry["status"] != "restored"]
        if not isinstance(pending, str) or not remaining or pending != remaining[-1]["id"]:
            raise ContractError("Pending restoration must refer to the next entry in reverse order")
        if frontmatter["status"] not in ("restoring", "blocked"):
            raise ContractError("Pending restoration conflicts with the current state")


def resolve_entry_targets(entries: list[dict[str, object]], writable_roots: list[str]) -> list[Path]:
    return [resolve_target(str(entry["path"]), writable_roots, recorded=True) for entry in entries]


def original_bytes(entry: dict[str, object]) -> bytes:
    original = entry["original"]
    assert isinstance(original, dict)
    if not original.get("exists"):
        return b""
    recovery = original.get("recovery")
    if recovery == "embed":
        data = decode_payload(str(original.get("payload", "")))
    elif recovery == "git":
        repo = Path(str(original["git_repo"]))
        result = run_git(repo, "show", f"{original['git_ref']}:{original['git_path']}")
        data = result.stdout
    else:
        raise ContractError(f"Journal entry {entry.get('id')} has no recovery source")
    if sha256(data) != original.get("sha256"):
        raise ContractError(f"Recovery digest mismatch for journal entry {entry.get('id')}")
    return data


def expected_current(entries: list[dict[str, object]]) -> dict[str, object]:
    active = [entry for entry in entries if entry.get("status") != "restored"]
    if not active:
        return dict(entries[0]["original"])
    latest = active[-1]
    if latest.get("status") == "applied":
        return dict(latest["applied"])
    return dict(latest["original"])


def cmd_init(args: argparse.Namespace) -> dict[str, object]:
    if args.completion_stage and STAGES.index(args.completion_stage) < STAGES.index(args.target_stage):
        raise ContractError("completion_stage must cover target_stage")
    authority_root = Path(args.authority_root).expanduser().resolve()
    if not authority_root.is_dir():
        raise ContractError(f"Authority root does not exist: {authority_root}")
    roots = [Path(root).expanduser().resolve() for root in args.writable_root]
    if not roots or any(not root.is_dir() for root in roots):
        raise ContractError("Every writable root must be an existing directory")
    if not any(authority_root == root or authority_root.is_relative_to(root) for root in roots):
        raise ContractError("The authority root must lie within an authorized writable root")
    contract = authority_root / CONTRACT_NAME
    if contract.exists() or contract.is_symlink():
        raise ContractError(f"An unfinished round already exists: {contract}")
    repository = observed_git_root(authority_root)
    observed_version_control = "git" if repository is not None else "none"
    if observed_version_control != args.version_control:
        raise ContractError(
            f"version_control mismatch: declared {args.version_control}, observed {observed_version_control}"
        )
    baseline_ref = None
    if args.baseline_ref:
        if repository is None:
            raise ContractError("A workspace without Git cannot register a Git baseline")
        baseline_ref = git_commit(repository, args.baseline_ref)

    template = (Path(__file__).resolve().parents[1] / "assets" / CONTRACT_NAME).read_text(encoding="utf-8")
    created_at = now_iso()
    journal = {
        "journal_version": 1,
        "writable_roots": [str(root) for root in roots],
        "entries": [],
    }
    replacements = {
        "{{SCHEMA_VERSION}}": str(SCHEMA_VERSION),
        "{{ROUND_ID}}": json_scalar(args.round_id or str(uuid.uuid4())),
        "{{AUTHORITY_ROOT}}": json_scalar(str(authority_root)),
        "{{TARGET_STAGE}}": json_scalar(args.target_stage),
        "{{COMPLETION_STAGE}}": json_scalar(args.completion_stage),
        "{{CREATED_AT}}": json_scalar(created_at),
        "{{CONFIRMED_AT}}": json_scalar(args.confirmed_at or created_at),
        "{{VERSION_CONTROL}}": json_scalar(args.version_control),
        "{{BASELINE_REF}}": json_scalar(baseline_ref),
        "{{JOURNAL_JSON}}": json.dumps(journal, ensure_ascii=False, indent=2, sort_keys=True),
    }
    for marker, value in replacements.items():
        template = template.replace(marker, value)
    if "{{" in template or "}}" in template:
        raise ContractError("Unresolved placeholder in the contract template")
    atomic_write(contract, template.encode("utf-8"), 0o600, replace=False)
    return {"contract": str(contract), "status": "executing", "mode": "0600"}


def cmd_prepare(args: argparse.Namespace) -> dict[str, object]:
    contract, text, frontmatter, journal = load_contract(args.contract)
    require_schema(frontmatter, journal)
    if frontmatter["status"] != "executing":
        raise ContractError("Only executing rounds can prepare a write")
    target = resolve_target(args.path, list(journal["writable_roots"]))
    entries = list(journal["entries"])
    issues = verify_entry_chains(entries, list(journal["writable_roots"]))
    if issues:
        raise ContractError("Check existing journal and file inconsistencies before writing: " + "; ".join(issues))
    for entry in reversed(entries):
        if entry.get("path") == str(target) and entry.get("status") == "prepared":
            raise ContractError(f"A pending prepared entry already exists for {target}")

    before = snapshot(target)
    data = before.get("data") if before.get("exists") else None
    assert data is None or isinstance(data, bytes)
    signals = detect_sensitive(target, data)
    if signals and not args.allow_sensitive:
        raise ContractError(f"Sensitive content in {target}. Use --allow-sensitive only after per-file approval. Signals: {','.join(signals)}")

    original: dict[str, object] = public_snapshot(before)
    if before["exists"]:
        assert isinstance(data, bytes)
        if args.recovery_mode == "git":
            if frontmatter.get("version_control") != "git":
                raise ContractError("Git recovery mode requires a Git baseline contract")
            if not frontmatter.get("baseline_ref"):
                raise ContractError("No frozen Git baseline. Use embedded recovery to preserve the actual starting state")
            repo = git_root(target)
            baseline, relative = git_blob(repo, str(frontmatter.get("baseline_ref")), target)
            if baseline != data:
                raise ContractError("Current bytes differ from baseline_ref. Use embedded recovery")
            original.update(
                recovery="git",
                git_repo=str(repo),
                git_ref=str(frontmatter.get("baseline_ref")),
                git_path=relative,
            )
        else:
            payload = encode_payload(data)
            if len(payload.encode("ascii")) > MAX_EMBEDDED_PAYLOAD and not args.allow_large:
                raise ContractError(
                    f"Recovery payload exceeds 10 MiB for {target}. Use Git, narrow the scope or confirm --allow-large"
                )
            original.update(recovery="embed", payload=payload)
    else:
        original.update(recovery="none")

    entry = {
        "id": f"J{len(entries) + 1:04d}",
        "path": str(target),
        "prepared_at": now_iso(),
        "status": "prepared",
        "sensitive_signals": signals,
        "sensitive_authorized": bool(args.allow_sensitive),
        "original": original,
        "applied": None,
        "reverse_diff": None,
    }
    entries.append(entry)
    journal["entries"] = entries
    save_contract(contract, text, journal)
    return {"entry": entry["id"], "path": str(target), "status": "prepared", "sensitive_signals": signals}


def cmd_applied(args: argparse.Namespace) -> dict[str, object]:
    contract, text, frontmatter, journal = load_contract(args.contract)
    require_schema(frontmatter, journal)
    if frontmatter["status"] != "executing":
        raise ContractError("Only executing rounds can record an applied write")
    target = resolve_target(args.path, list(journal["writable_roots"]))
    entries = list(journal["entries"])
    entry = next(
        (item for item in reversed(entries) if item.get("path") == str(target) and item.get("status") == "prepared"),
        None,
    )
    if entry is None:
        raise ContractError(f"No prepared journal entry for {target}")
    after = snapshot(target)
    original = entry["original"]
    assert isinstance(original, dict)
    old_data = original_bytes(entry) if original.get("exists") else b""
    new_data = after.get("data") if after.get("exists") else b""
    assert isinstance(new_data, bytes)
    new_signals = detect_sensitive(target, new_data if after.get("exists") else None)
    all_signals = sorted(set(entry["sensitive_signals"]) | set(new_signals))
    entry["sensitive_signals"] = all_signals
    entry["applied"] = public_snapshot(after)
    entry["applied_at"] = now_iso()
    entry["reverse_diff"] = reverse_diff(target, new_data, old_data, bool(all_signals))
    entry["status"] = "applied"
    newly_sensitive = bool(new_signals) and not bool(entry.get("sensitive_authorized"))
    if newly_sensitive:
        text = set_frontmatter(text, "status", "blocked")
    save_contract(contract, text, journal)
    if newly_sensitive:
        raise ContractError(
            f"New sensitive content detected after writing {target}. The change is recorded and blocked pending per-file approval. "
            f"Signals: {','.join(new_signals)}"
        )
    return {"entry": entry["id"], "path": str(target), "status": "applied", "sha256": after.get("sha256")}


def cmd_status(args: argparse.Namespace) -> dict[str, object]:
    contract, text, frontmatter, journal = load_contract(args.contract)
    require_schema(frontmatter, journal)
    if args.set_status:
        current = str(frontmatter["status"])
        requested = args.set_status
        if requested not in STATUS_TRANSITIONS[current]:
            raise ContractError(f"Invalid state transition: {current} -> {requested}")
        if journal.get("restore_pending") is not None and requested not in ("restoring", "blocked"):
            raise ContractError("Resolve the interrupted restoration before resuming normal execution")
        text = set_frontmatter(text, "status", requested)
        write_contract(contract, text)
        frontmatter["status"] = requested
    counts: dict[str, int] = {}
    for entry in journal["entries"]:
        state = str(entry.get("status"))
        counts[state] = counts.get(state, 0) + 1
    return {
        "contract": str(contract),
        "round_id": frontmatter.get("round_id"),
        "status": frontmatter.get("status"),
        "target_stage": frontmatter.get("target_stage"),
        "completion_stage": frontmatter.get("completion_stage"),
        "closure_recorded": bool(journal.get("closure")),
        "entries": counts,
    }


def cmd_scope(args: argparse.Namespace) -> dict[str, object]:
    contract, text, frontmatter, journal = load_contract(args.contract)
    require_schema(frontmatter, journal)
    if frontmatter["status"] not in {"executing", "paused", "blocked"}:
        raise ContractError("Cannot adjust execution scope in the current state")
    completion = args.completion_stage or frontmatter.get("completion_stage")
    if completion not in STAGES or STAGES.index(completion) < STAGES.index(args.target_stage):
        raise ContractError("Specify a completion_stage that covers the execution target")
    previous = frontmatter.get("completion_stage")
    if previous and STAGES.index(completion) < STAGES.index(previous):
        raise ContractError("Cannot lower the completion stage. Preserve this round for remaining work or restoration")
    if not args.confirmation.strip():
        raise ContractError("Supply the user's confirmation text or its source location")
    roots = list(journal["writable_roots"])
    added_roots: list[str] = []
    for root_arg in args.writable_root or []:
        root = Path(root_arg).expanduser().resolve()
        if not root.is_dir():
            raise ContractError(f"Writable root does not exist: {root}")
        if str(root) not in roots:
            roots.append(str(root))
            added_roots.append(str(root))
    journal.setdefault("scope_changes", []).append({
        "at": now_iso(), "confirmation": args.confirmation,
        "previous_target": frontmatter["target_stage"], "target_stage": args.target_stage,
        "previous_completion": previous, "completion_stage": completion,
        "added_writable_roots": added_roots,
    })
    journal["writable_roots"] = roots
    text = set_frontmatter(text, "target_stage", args.target_stage)
    text = set_frontmatter(text, "completion_stage", completion)
    save_contract(contract, text, journal)
    return {"contract": str(contract), "target_stage": args.target_stage, "completion_stage": completion}


def restore_one(entry: dict[str, object], target: Path, *, retry_pending: bool = False) -> None:
    current = snapshot(target)
    original = entry["original"]
    assert isinstance(original, dict)
    status_value = entry.get("status")
    expected = entry.get("applied") if status_value == "applied" else entry.get("original")
    assert isinstance(expected, dict)
    if retry_pending and same_snapshot(current, original):
        return
    if not same_snapshot(current, expected):
        raise ContractError(f"External change detected. Restore stopped at {target}")
    if same_snapshot(current, original):
        return
    if original.get("exists"):
        data = original_bytes(entry)
        mode = int(original["mode"])
        atomic_write(target, data, mode)
    elif current.get("exists"):
        if target.is_symlink() or not target.is_file():
            raise ContractError(f"Refusing to remove a non-regular file: {target}")
        target.unlink()
    restored = snapshot(target)
    if not same_snapshot(restored, original):
        raise ContractError(f"Post-restore verification failed for {target}")


def preflight_restore(
    entries: list[dict[str, object]], targets: list[Path], pending_id: str | None = None
) -> list[Path]:
    """Simulate the complete reverse sequence before restoring any target."""
    simulated = {target: snapshot(target) for target in dict.fromkeys(targets)}
    missing_dirs: set[Path] = set()
    baselines: dict[Path, dict[str, object]] = {}
    for entry, target in zip(entries, targets):
        original = entry["original"]
        assert isinstance(original, dict)
        baselines.setdefault(target, original)
    for entry, target in reversed(list(zip(entries, targets))):
        if entry["status"] == "restored":
            continue
        current = simulated[target]
        original = entry["original"]
        expected = entry["applied"] if entry["status"] == "applied" else original
        assert isinstance(original, dict) and isinstance(expected, dict)
        retried = entry["id"] == pending_id and same_snapshot(current, original)
        if not retried and not same_snapshot(current, expected):
            raise ContractError(f"External change detected at {target}. No targets were restored")
        if not same_snapshot(original, current):
            for parent in target.parents:
                if parent.is_dir():
                    if not os.access(parent, os.W_OK | os.X_OK):
                        raise ContractError(f"Parent directory is not writable. No targets were restored: {parent}")
                    break
                if parent.exists() or parent in simulated:
                    raise ContractError(f"Original parent path is occupied or journaled as a file. No targets were restored: {parent}")
                missing_dirs.add(parent)
        simulated[target] = original
    for target, original in baselines.items():
        if not same_snapshot(simulated[target], original):
            raise ContractError(f"Previously restored file changed at {target}. No targets were restored")
    return sorted(missing_dirs, key=lambda path: len(path.parts))


def cmd_restore(args: argparse.Namespace) -> dict[str, object]:
    contract, text, frontmatter, journal = load_contract(args.contract)
    require_schema(frontmatter, journal)
    entries = list(journal["entries"])
    targets = resolve_entry_targets(entries, list(journal["writable_roots"]))
    if frontmatter["status"] != "restoring":
        text = set_frontmatter(text, "status", "restoring")
        write_contract(contract, text)
    restored_ids: list[str] = []
    try:
        issues = verify_entry_chains(entries, list(journal["writable_roots"]), check_current=False)
        if issues:
            raise ContractError("Journal verification failed before restoring any targets: " + "; ".join(issues))
        missing_dirs = preflight_restore(entries, targets, journal.get("restore_pending"))
        for directory in missing_dirs:
            try:
                directory.mkdir(mode=0o700)
            except OSError as exc:
                raise ContractError(f"Cannot recreate the original parent directory. No targets were restored: {directory}: {exc}") from exc
        for entry, target in reversed(list(zip(entries, targets))):
            if entry.get("status") == "restored":
                continue
            retry_pending = journal.get("restore_pending") == entry["id"]
            if not retry_pending:
                journal["restore_pending"] = entry["id"]
                _, latest_text, _, _ = load_contract(str(contract))
                save_contract(contract, latest_text, journal)
            restore_one(entry, target, retry_pending=retry_pending)
            entry["status"] = "restored"
            entry["restored_at"] = now_iso()
            journal.pop("restore_pending", None)
            restored_ids.append(str(entry["id"]))
            _, latest_text, _, _ = load_contract(str(contract))
            save_contract(contract, latest_text, journal)
    except ContractError:
        _, latest_text, _, _ = load_contract(str(contract))
        latest_text = set_frontmatter(latest_text, "status", "blocked")
        save_contract(contract, latest_text, journal)
        raise
    _, latest_text, _, _ = load_contract(str(contract))
    latest_text = set_frontmatter(latest_text, "status", "restored")
    journal.pop("closure", None)
    save_contract(contract, latest_text, journal)
    return {"contract": str(contract), "status": "restored", "restored": restored_ids}


def verify_entry_chains(
    entries: list[dict[str, object]], writable_roots: list[str], *, check_current: bool = True
) -> list[str]:
    issues: list[str] = []
    grouped: dict[str, list[dict[str, object]]] = {}
    for index, entry in enumerate(entries, start=1):
        expected_id = f"J{index:04d}"
        if entry.get("id") != expected_id:
            issues.append(f"Nonconsecutive journal ID. Expected {expected_id}")
        try:
            target = resolve_target(str(entry["path"]), writable_roots, recorded=True)
        except ContractError as exc:
            issues.append(str(exc))
            continue
        grouped.setdefault(str(target), []).append(entry)
    for path, path_entries in grouped.items():
        for previous, current in zip(path_entries, path_entries[1:]):
            if previous.get("applied") is None:
                issues.append(f"Previous entry has not been applied: {path}")
                continue
            if public_snapshot(dict(previous["applied"])) != public_snapshot(dict(current["original"])):
                issues.append(f"Broken journal chain for {path}")
        if check_current:
            expected = expected_current(path_entries)
            try:
                actual = snapshot(Path(path))
            except ContractError as exc:
                issues.append(str(exc))
                continue
            if not same_snapshot(actual, expected):
                issues.append(f"Current file state differs from its journal: {path}")
        for entry in path_entries:
            original = entry.get("original")
            if isinstance(original, dict) and original.get("exists"):
                try:
                    original_bytes(entry)
                except ContractError as exc:
                    issues.append(str(exc))
    return issues


def closure_fingerprint(text: str, journal: dict[str, object]) -> str:
    journal = dict(journal)
    journal.pop("closure", None)
    normalized = replace_journal(set_frontmatter(text, "status", "executing"), journal)
    return sha256(normalized.encode("utf-8"))


def closure_evidence(
    contract: Path, evidence_arg: str, frontmatter: dict[str, object], journal: dict[str, object]
) -> dict[str, object]:
    evidence_path = Path(evidence_arg).expanduser().absolute()
    data, _ = read_regular_file(evidence_path)
    if evidence_path.resolve() == contract:
        raise ContractError("Put closure evidence in a separate acceptance record")
    try:
        evidence = json.loads(data)
    except (ValueError, UnicodeError) as exc:
        raise ContractError("Closure evidence must be JSON") from exc
    if not isinstance(evidence, dict) or evidence.get("round_id") != frontmatter.get("round_id"):
        raise ContractError("Closure evidence round_id mismatch")
    if evidence.get("remaining_work") != []:
        raise ContractError("Closure evidence requires remaining_work: []. Keep the contract open while work remains")
    outcome = evidence.get("outcome")
    entries = journal["entries"]
    if outcome == "completed":
        completion = frontmatter.get("completion_stage")
        if completion not in STAGES:
            raise ContractError("Record the confirmed completion_stage with scope first")
        if frontmatter["target_stage"] != completion:
            raise ContractError("Execution reached its target but not the round endpoint. Pause and retain the contract")
        if evidence.get("completed_stage") != completion:
            raise ContractError("Evidence completed_stage falls short of the round endpoint")
        if frontmatter["status"] not in {"executing", "ready_to_close"}:
            raise ContractError("Cannot complete the round in the current state")
        if any(entry["status"] != "applied" for entry in entries):
            raise ContractError("All changes must be applied before completion")
        required = list(STAGES[:STAGES.index(completion) + 1]) + ["residuals", "watermark", "absorption"]
    elif outcome == "restored":
        if frontmatter["status"] not in {"restored", "ready_to_close"}:
            raise ContractError("Restore the files and recheck the baseline first")
        if any(entry["status"] != "restored" for entry in entries):
            raise ContractError("Journal entries still need restoration")
        required = ["baseline", "references", "absorption"]
    else:
        raise ContractError("Evidence outcome must be completed or restored")
    checks = evidence.get("checks")
    if not isinstance(checks, dict):
        raise ContractError("Closure evidence has no checks")
    files: dict[str, object] = {}
    for name in dict.fromkeys(required + list(checks)):
        check = checks.get(name)
        if not isinstance(check, dict) or check.get("result") != "pass":
            raise ContractError(f"Closure check failed: {name}")
        references = check.get("evidence")
        if not isinstance(references, list) or not references:
            raise ContractError(f"Missing evidence files for closure check: {name}")
        for reference in references:
            if not isinstance(reference, str) or not Path(reference).is_absolute():
                raise ContractError(f"Evidence path must be absolute: {name}")
            path = Path(reference)
            if path.resolve() in {contract, evidence_path.resolve()}:
                raise ContractError("Cite an independent authoritative artifact or acceptance record")
            content, _ = read_regular_file(path)
            if not content.strip():
                raise ContractError(f"Empty evidence file: {path}")
            files[str(path)] = public_snapshot(snapshot(path))
    return {"evidence_path": str(evidence_path), "evidence_sha256": sha256(data), "files": files}


def cmd_verify(args: argparse.Namespace) -> dict[str, object]:
    contract, text, frontmatter, journal = load_contract(args.contract)
    require_schema(frontmatter, journal)
    issues: list[str] = []
    mode = stat.S_IMODE(contract.stat().st_mode)
    if mode != 0o600:
        issues.append(f"Contract permissions must be 0600. Found {mode:04o}")
    authority_root = Path(str(frontmatter["authority_root"]))
    try:
        if observed_git_root(authority_root) is not None and contract_is_tracked(contract, authority_root):
            issues.append("Reconciliation contract is tracked or staged in Git")
    except ContractError as exc:
        issues.append(str(exc))
    entries = list(journal["entries"])
    issues.extend(verify_entry_chains(entries, list(journal["writable_roots"])))
    if any(entry.get("status") == "prepared" for entry in entries):
        issues.append("A write-ahead entry has not been applied")
    if journal.get("restore_pending") is not None:
        issues.append("A restore operation is pending confirmation")
    closure_issues: list[str] = []
    if frontmatter["status"] == "ready_to_close":
        certificate = journal.get("closure")
        try:
            if not isinstance(certificate, dict):
                raise ContractError("Closure evidence registration missing. Recheck this older ready_to_close record")
            if certificate.get("fingerprint") != closure_fingerprint(text, journal):
                raise ContractError("Contract changed after closure review. Verify again")
            current = closure_evidence(contract, str(certificate.get("evidence_path")), frontmatter, journal)
            if any(certificate.get(key) != value for key, value in current.items()):
                raise ContractError("Closure evidence changed. Verify again")
        except ContractError as exc:
            closure_issues.append(str(exc))
    if args.mark_ready:
        if issues:
            raise ContractError("Mechanical verification failed. Cannot mark ready_to_close")
        if frontmatter["status"] not in {"executing", "restored"}:
            raise ContractError(f"Cannot mark ready_to_close in state {frontmatter['status']}")
        if not args.evidence:
            raise ContractError("Supply --evidence to demonstrate completion in addition to mechanical validity")
        certificate = closure_evidence(contract, args.evidence, frontmatter, journal)
        certificate["fingerprint"] = closure_fingerprint(text, journal)
        journal["closure"] = certificate
        text = set_frontmatter(text, "status", "ready_to_close")
        text = replace_journal(text, journal)
        save_contract(contract, text, journal)
        frontmatter["status"] = "ready_to_close"
    return {
        "contract": str(contract),
        "status": frontmatter.get("status"),
        "valid": not issues,
        "issues": issues,
        "close_ready": frontmatter["status"] == "ready_to_close" and not issues and not closure_issues,
        "closure_issues": closure_issues,
        "entry_count": len(entries),
        "contract_sha256": sha256(text.encode("utf-8")),
    }


def load_recovery(path_arg: str) -> tuple[Path, str, dict[str, object], dict[str, object], str]:
    path = Path(path_arg).expanduser().absolute()
    data, mode = read_regular_file(path)
    if mode != 0o600:
        raise ContractError("Recovery archive permissions must be 0600")
    try:
        archive = json.loads(data)
    except (ValueError, UnicodeError) as exc:
        raise ContractError("Recovery archive must be JSON") from exc
    if not isinstance(archive, dict) or type(archive.get("recovery_version")) is not int or archive["recovery_version"] != 1:
        raise ContractError("Unsupported recovery archive version")
    text = archive.get("contract")
    if not isinstance(text, str) or archive.get("contract_sha256") != sha256(text.encode("utf-8")):
        raise ContractError("Recovery archive digest mismatch")
    outcome = archive.get("outcome")
    if outcome not in ("completed", "restored"):
        raise ContractError("Invalid recovery archive outcome")
    frontmatter, _, _ = parse_frontmatter(text)
    journal = extract_journal(text)
    require_schema(frontmatter, journal)
    certificate = journal.get("closure")
    if frontmatter["status"] != "ready_to_close" or not isinstance(certificate, dict):
        raise ContractError("Recovery archive is missing its closure registration")
    if certificate.get("fingerprint") != closure_fingerprint(text, journal):
        raise ContractError("Archived contract differs from its closure registration")
    expected_status = "applied" if outcome == "completed" else "restored"
    if any(entry["status"] != expected_status for entry in journal["entries"]):
        raise ContractError("Archived outcome conflicts with journal state")
    return path.resolve(), text, frontmatter, journal, outcome


def cmd_inspect_recovery(args: argparse.Namespace) -> dict[str, object]:
    path, _, frontmatter, journal, outcome = load_recovery(args.archive)
    return {
        "archive": str(path), "round_id": frontmatter["round_id"], "outcome": outcome,
        "authority_root": frontmatter["authority_root"], "writable_roots": journal["writable_roots"],
        "paths": list(dict.fromkeys(entry["path"] for entry in journal["entries"])),
        "entry_count": len(journal["entries"]),
    }


def cmd_reopen(args: argparse.Namespace) -> dict[str, object]:
    archive, text, frontmatter, journal, outcome = load_recovery(args.archive)
    if outcome != "completed":
        raise ContractError("This archive records a completed restoration and cannot undo the round again")
    if not args.confirmation.strip():
        raise ContractError("Record the current explicit authorization to undo")
    roots = [Path(root).expanduser().resolve() for root in args.writable_root]
    if any(not root.is_dir() for root in roots):
        raise ContractError("Currently authorized working roots must already exist")
    authority = Path(str(frontmatter["authority_root"]))
    if authority.is_symlink() or authority.resolve() != authority or not authority.is_dir():
        raise ContractError("Original authority root moved or is unavailable. Recovery paths remain bound to it")
    authority = authority.resolve()
    if not any(authority == root or authority.is_relative_to(root) for root in roots):
        raise ContractError("The original authority root is outside the current authorization")
    contract = authority / CONTRACT_NAME
    if contract.exists() or contract.is_symlink():
        raise ContractError("An active contract already exists. Preserving it")
    journal["writable_roots"] = [str(root) for root in roots]
    targets = resolve_entry_targets(journal["entries"], journal["writable_roots"])
    issues = verify_entry_chains(journal["entries"], journal["writable_roots"])
    if issues:
        raise ContractError("Recovery archive journal cannot be used: " + "; ".join(issues))
    preflight_restore(journal["entries"], targets)
    journal.pop("closure", None)
    text = set_frontmatter(text, "status", "restoring")
    text += f"\n## Authorization to undo a closed round\n\n- Recovery archive: {archive}\n- Confirmation: {args.confirmation.strip()}\n"
    atomic_write(contract, replace_journal(text, journal).encode("utf-8"), 0o600, replace=False)
    return {"contract": str(contract), "round_id": frontmatter["round_id"], "status": "restoring",
            "archive": str(archive), "targets_restored": False}


def cmd_close(args: argparse.Namespace) -> dict[str, object]:
    result = cmd_verify(argparse.Namespace(contract=args.contract, mark_ready=False))
    if not result["close_ready"]:
        raise ContractError("Closure checks failed. The contract stays open: " + "; ".join(result["issues"] + result["closure_issues"]))
    contract, text, frontmatter, journal = load_contract(str(result["contract"]))
    frozen_digest = sha256(text.encode("utf-8"))
    if frozen_digest != result["contract_sha256"]:
        raise ContractError("Closure inputs changed. The contract stays open")
    archive = resolve_target(args.archive, list(journal["writable_roots"]))
    targets = resolve_entry_targets(journal["entries"], list(journal["writable_roots"]))
    if archive in targets:
        raise ContractError("Recovery archive cannot occupy a target file path")
    if observed_git_root(archive.parent) is not None and contract_is_tracked(archive, archive.parent):
        raise ContractError("Recovery archive cannot be written to a tracked or staged path")
    evidence_data, _ = read_regular_file(Path(journal["closure"]["evidence_path"]))
    outcome = json.loads(evidence_data)["outcome"]
    payload = json.dumps({"recovery_version": 1, "outcome": outcome,
                          "contract_sha256": sha256(text.encode("utf-8")), "contract": text},
                         ensure_ascii=False, indent=2).encode("utf-8") + b"\n"
    if archive.exists():
        existing, mode = read_regular_file(archive)
        if existing != payload or mode != 0o600:
            raise ContractError("Recovery material already exists. Choose an unused archive path")
    else:
        atomic_write(archive, payload, 0o600, replace=False)
    rechecked = cmd_verify(argparse.Namespace(contract=str(contract), mark_ready=False))
    if not rechecked["close_ready"] or rechecked["contract_sha256"] != frozen_digest:
        raise ContractError("Inputs changed after archiving. The active contract stays open")
    contract.unlink()
    return {"contract": str(contract), "closed": True, "archive": str(archive), "outcome": outcome}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Create a private reconciliation contract with mode 0600")
    init_parser.add_argument("authority_root")
    init_parser.add_argument("--round-id")
    init_parser.add_argument("--target-stage", choices=STAGES, required=True)
    init_parser.add_argument("--completion-stage", choices=STAGES, help="Stage required for normal closure. Omit to leave normal closure disabled")
    init_parser.add_argument("--confirmed-at")
    init_parser.add_argument("--version-control", choices=("git", "none"), required=True)
    init_parser.add_argument("--baseline-ref")
    init_parser.add_argument("--writable-root", action="append", required=True)
    init_parser.set_defaults(handler=cmd_init)

    prepare_parser = subparsers.add_parser("prepare", help="Record the recoverable preimage before a write")
    prepare_parser.add_argument("contract")
    prepare_parser.add_argument("--path", required=True)
    prepare_parser.add_argument("--recovery-mode", choices=("embed", "git"), default="embed")
    prepare_parser.add_argument("--allow-sensitive", action="store_true")
    prepare_parser.add_argument("--allow-large", action="store_true")
    prepare_parser.set_defaults(handler=cmd_prepare)

    applied_parser = subparsers.add_parser("applied", help="Record post-write digests and reverse diff")
    applied_parser.add_argument("contract")
    applied_parser.add_argument("--path", required=True)
    applied_parser.set_defaults(handler=cmd_applied)

    status_parser = subparsers.add_parser("status", help="Inspect or update the control state")
    status_parser.add_argument("contract")
    status_parser.add_argument("--set", dest="set_status", choices=("executing", "paused", "blocked", "restoring"))
    status_parser.set_defaults(handler=cmd_status)

    scope_parser = subparsers.add_parser("scope", help="Record a confirmed execution limit and completion stage in this round")
    scope_parser.add_argument("contract")
    scope_parser.add_argument("--target-stage", choices=STAGES, required=True)
    scope_parser.add_argument("--completion-stage", choices=STAGES)
    scope_parser.add_argument("--confirmation", required=True)
    scope_parser.add_argument("--writable-root", action="append", help="Add a currently authorized writable root")
    scope_parser.set_defaults(handler=cmd_scope)

    restore_parser = subparsers.add_parser("restore", help="Restore all file changes in reverse order")
    restore_parser.add_argument("contract")
    restore_parser.set_defaults(handler=cmd_restore)

    verify_parser = subparsers.add_parser("verify", help="Check schema, journal chain, digests, permissions and Git state")
    verify_parser.add_argument("contract")
    verify_parser.add_argument("--mark-ready", action="store_true")
    verify_parser.add_argument("--evidence", help="Closure evidence JSON for this round")
    verify_parser.set_defaults(handler=cmd_verify)

    close_parser = subparsers.add_parser("close", help="Verify closure, preserve a recovery archive and close the contract")
    close_parser.add_argument("contract")
    close_parser.add_argument("--archive", required=True, help="Unused archive path under an authorized root with an existing parent")
    close_parser.set_defaults(handler=cmd_close)

    inspect_parser = subparsers.add_parser("inspect-recovery", help="Inspect the recovery archive identity and paths without printing payloads")
    inspect_parser.add_argument("archive")
    inspect_parser.set_defaults(handler=cmd_inspect_recovery)

    reopen_parser = subparsers.add_parser("reopen", help="Recreate the control record on explicit undo authorization, leaving target files alone")
    reopen_parser.add_argument("archive")
    reopen_parser.add_argument("--confirmation", required=True)
    reopen_parser.add_argument("--writable-root", action="append", required=True)
    reopen_parser.set_defaults(handler=cmd_reopen)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        result = args.handler(args)
    except (ContractError, OSError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2
    invalid = args.command == "verify" and (not result["valid"] or bool(result["closure_issues"]))
    print(json.dumps({"ok": not invalid, **result}, ensure_ascii=False, indent=2, sort_keys=True))
    return 2 if invalid else 0


if __name__ == "__main__":
    raise SystemExit(main())
