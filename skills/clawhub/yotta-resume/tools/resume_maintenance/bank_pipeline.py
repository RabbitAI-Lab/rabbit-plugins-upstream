#!/usr/bin/env python3
"""Candidate review, validation, apply, and rollback for yotta-resume."""

import copy
import datetime as dt
import json
import os
import re
import tempfile
from pathlib import Path

import source_watch
from contract_validate import validate_contracts


SCHEMA_VERSION = "1.0"
SKILL_VERSION = "0.2.0"
REQUIRED_CONFIRMATIONS = ("facts", "role", "level", "boundary", "rights")
_SEMVER_RE = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
    r"(?:-([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?$"
)
_PHONE_RE = re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)")
_EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")


class BankPipelineError(Exception):
    """A controlled bank candidate failure."""

    def __init__(self, message, exit_code=7):
        super().__init__(message)
        self.exit_code = exit_code


def _parse_date(value, label):
    if not isinstance(value, str):
        raise BankPipelineError("{}必须是 ISO 日期。".format(label), exit_code=5)
    try:
        return dt.date.fromisoformat(value)
    except ValueError as error:
        raise BankPipelineError(
            "{}不是有效日期：{}".format(label, value),
            exit_code=5,
        ) from error


def _parse_timestamp(value, label):
    if not isinstance(value, str):
        raise BankPipelineError("{}必须是 ISO 时间。".format(label), exit_code=5)
    try:
        return dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as error:
        raise BankPipelineError(
            "{}不是有效时间：{}".format(label, value),
            exit_code=5,
        ) from error


def _mask_contact(text):
    text = _PHONE_RE.sub("[电话]", text)
    return _EMAIL_RE.sub("[邮箱]", text)


def _parse_semver(value):
    if not isinstance(value, str):
        raise BankPipelineError("版本号必须是字符串。", exit_code=5)
    match = _SEMVER_RE.fullmatch(value)
    if not match:
        raise BankPipelineError("版本号不是有效 SemVer：{}".format(value), exit_code=5)
    major, minor, patch, prerelease = match.groups()
    pre_parts = []
    if prerelease:
        for part in prerelease.split("."):
            pre_parts.append((0, int(part)) if part.isdigit() else (1, part))
    return int(major), int(minor), int(patch), pre_parts


def _compare_semver(left, right):
    left_core = left[:3]
    right_core = right[:3]
    if left_core != right_core:
        return 1 if left_core > right_core else -1
    left_pre = left[3]
    right_pre = right[3]
    if not left_pre and not right_pre:
        return 0
    if not left_pre:
        return 1
    if not right_pre:
        return -1
    for left_part, right_part in zip(left_pre, right_pre):
        if left_part == right_part:
            continue
        if left_part[0] != right_part[0]:
            return 1 if left_part[0] > right_part[0] else -1
        return 1 if left_part[1] > right_part[1] else -1
    if len(left_pre) == len(right_pre):
        return 0
    return 1 if len(left_pre) > len(right_pre) else -1


def _question_hash(question):
    filtered = {
        key: value
        for key, value in question.items()
        if key != "content_hash"
    }
    return source_watch._canonical_hash(filtered)


def _read_json(path, label):
    try:
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise BankPipelineError("{}不存在：{}".format(label, path), exit_code=3) from error
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise BankPipelineError("{}无法读取：{}".format(label, error), exit_code=5) from error
    if not isinstance(payload, dict):
        raise BankPipelineError("{}格式无效：根节点必须是对象。".format(label), exit_code=5)
    return payload


def _data_dir(root):
    base = Path(root)
    if (base / "data" / "question-bank.json").is_file():
        return base / "data"
    return base


def _load_candidate(path):
    candidate = Path(path)
    manifest_path = candidate / "manifest.json"
    manifest = _read_json(manifest_path, "候选 manifest")
    records = manifest.get("files")
    if not isinstance(records, list) or not records:
        raise BankPipelineError("候选 manifest 缺少 files。", exit_code=7)
    seen = set()
    for record in records:
        if not isinstance(record, dict):
            raise BankPipelineError("候选 manifest 文件记录无效。", exit_code=7)
        name = record.get("path")
        if (
            not isinstance(name, str)
            or not name
            or name in seen
            or Path(name).name != name
            or name in {"manifest.json", "review.json", "validation.json"}
        ):
            raise BankPipelineError(
                "候选 manifest 包含非法路径：{}".format(name),
                exit_code=7,
            )
        seen.add(name)
        target = candidate / name
        if not target.is_file():
            raise BankPipelineError("候选文件不存在：{}".format(name), exit_code=7)
        if target.stat().st_size != record.get("size"):
            raise BankPipelineError("候选文件大小不一致：{}".format(name), exit_code=7)
        if source_watch._sha256_file(target) != record.get("sha256"):
            raise BankPipelineError("候选文件哈希不一致：{}".format(name), exit_code=7)
    return candidate, manifest


def _candidate_sha256(manifest):
    return source_watch._canonical_hash(manifest)


def probe_state_support():
    """Check candidate and history writes can be performed atomically."""
    with tempfile.TemporaryDirectory(prefix="yotta-resume-bank-doctor-") as tmp:
        root = Path(tmp)
        first = root / "candidate.json"
        second = root / "snapshot.json"
        source_watch._write_bytes_atomic(first, b'{"ok":true}\n')
        source_watch._write_bytes_atomic(second, first.read_bytes())
        return (
            first.read_bytes() == b'{"ok":true}\n'
            and second.read_bytes() == first.read_bytes()
        )


def _find_question(questions, question_id):
    for question in questions:
        if question.get("question_id") == question_id:
            return question
    return None


def _load_patches(path):
    if path is None:
        return {"add": [], "modify": [], "retire": []}
    payload = _read_json(path, "题库补丁")
    result = {}
    for key in ("add", "modify", "retire"):
        value = payload.get(key, [])
        if not isinstance(value, list):
            raise BankPipelineError("题库补丁 {} 必须是数组。".format(key), exit_code=5)
        result[key] = value
    unknown = set(payload) - {"add", "modify", "retire"}
    if unknown:
        raise BankPipelineError(
            "题库补丁包含未知字段：{}".format(", ".join(sorted(unknown))),
            exit_code=5,
        )
    return result


def _apply_patches(base_bank, patches, today):
    candidate = copy.deepcopy(base_bank)
    questions = candidate.get("questions")
    if not isinstance(questions, list):
        raise BankPipelineError("正式题库缺少 questions 数组。", exit_code=5)
    by_id = {
        item.get("question_id"): item
        for item in questions
        if isinstance(item, dict) and item.get("question_id")
    }
    touched = set()

    for item in patches["modify"]:
        if not isinstance(item, dict):
            raise BankPipelineError("modify 条目必须是对象。", exit_code=5)
        question_id = item.get("question_id")
        updates = item.get("set")
        if question_id not in by_id:
            raise BankPipelineError(
                "要修改的题目不存在：{}".format(question_id),
                exit_code=5,
            )
        if not isinstance(updates, dict) or not updates:
            raise BankPipelineError(
                "题目 {} 的 set 必须是非空对象。".format(question_id),
                exit_code=5,
            )
        forbidden = set(updates) & {"question_id", "content_hash"}
        if forbidden:
            raise BankPipelineError(
                "题目 {} 不允许修改字段：{}".format(
                    question_id,
                    ", ".join(sorted(forbidden)),
                ),
                exit_code=5,
            )
        by_id[question_id].update(updates)
        by_id[question_id]["last_verified_at"] = today
        touched.add(question_id)

    for item in patches["add"]:
        if not isinstance(item, dict):
            raise BankPipelineError("add 条目必须是对象。", exit_code=5)
        question_id = item.get("question_id")
        if not isinstance(question_id, str) or not question_id:
            raise BankPipelineError("新增题目缺少 question_id。", exit_code=5)
        if question_id in by_id:
            raise BankPipelineError("新增题目 ID 已存在：{}".format(question_id), exit_code=5)
        question = copy.deepcopy(item)
        question.pop("content_hash", None)
        question.setdefault("status", "active")
        question.setdefault("last_verified_at", today)
        question.setdefault("stale_after_days", 180)
        questions.append(question)
        by_id[question_id] = question
        touched.add(question_id)

    for item in patches["retire"]:
        question_id = item.get("question_id") if isinstance(item, dict) else item
        if question_id not in by_id:
            raise BankPipelineError(
                "要退役的题目不存在：{}".format(question_id),
                exit_code=5,
            )
        by_id[question_id]["status"] = "retired"
        by_id[question_id]["last_verified_at"] = today
        touched.add(question_id)

    for question_id in touched:
        by_id[question_id]["content_hash"] = _question_hash(by_id[question_id])
    return candidate, touched


def _question_diff(base_questions, candidate_questions):
    base = {item["question_id"]: item for item in base_questions}
    candidate = {item["question_id"]: item for item in candidate_questions}
    changes = []
    for question_id in sorted(set(base) | set(candidate)):
        before = base.get(question_id)
        after = candidate.get(question_id)
        if before is None:
            change_type = "added"
        elif after is None:
            change_type = "removed"
        elif before != after:
            change_type = (
                "retired"
                if before.get("status") != "retired" and after.get("status") == "retired"
                else "modified"
            )
        else:
            continue
        changes.append({
            "question_id": question_id,
            "change_type": change_type,
            "before_hash": before.get("content_hash") if before else None,
            "after_hash": after.get("content_hash") if after else None,
            "before_status": before.get("status") if before else None,
            "after_status": after.get("status") if after else None,
        })
    return changes


def _render_review(candidate_id, source_diff, question_diff):
    lines = [
        "# 元简题库候选复核",
        "",
        "候选：`{}`".format(candidate_id),
        "",
        "## 来源变化",
        "",
    ]
    if source_diff["sources"]:
        for item in source_diff["sources"]:
            lines.append("- `{}`：{}".format(item["source_id"], item["change_type"]))
    else:
        lines.append("- 无来源差异。")
    lines.extend(["", "## 题目变化", ""])
    if question_diff:
        for item in question_diff:
            lines.append(
                "- `{}`：{}".format(item["question_id"], item["change_type"])
            )
    else:
        lines.append("- 题目内容未变化。")
    lines.extend([
        "",
        "## 人工复核硬闸门",
        "",
        "- [ ] facts：来源事实已核对",
        "- [ ] role：岗位族适配已核对",
        "- [ ] level：职级适配已核对",
        "- [ ] boundary：答案边界和安全表述已核对",
        "- [ ] rights：来源许可、引用方式和允许使用范围已核对",
        "",
    ])
    return "\n".join(lines)


def _manifest(candidate_id, created_at, base_bank_version, target_bank_version, diff, files):
    records = []
    for name, path in sorted(files.items()):
        records.append({
            "path": name,
            "size": path.stat().st_size,
            "sha256": source_watch._sha256_file(path),
        })
    return {
        "schema_version": SCHEMA_VERSION,
        "candidate_id": candidate_id,
        "created_at": created_at,
        "base_skill_version": SKILL_VERSION,
        "target_skill_version": SKILL_VERSION,
        "base_bank_version": base_bank_version,
        "target_bank_version": target_bank_version,
        "source_ids": [item["source_id"] for item in diff["sources"]],
        "source_change_count": len(diff["sources"]),
        "question_change_count": len(diff["questions"]),
        "files": records,
    }


def review_candidate(
    candidate_dir,
    reviewer,
    decision,
    review_notes_path,
    confirmations,
    reviewed_at=None,
):
    reviewed_at = reviewed_at or dt.datetime.now(dt.timezone.utc).replace(
        microsecond=0,
    ).isoformat().replace("+00:00", "Z")
    reviewed_dt = _parse_timestamp(reviewed_at, "reviewed_at")
    candidate, manifest = _load_candidate(candidate_dir)
    created_date = _parse_date(manifest.get("created_at"), "候选 created_at")
    if reviewed_dt.date() < created_date:
        raise BankPipelineError("复核时间不能早于候选生成时间。", exit_code=7)

    if decision not in {"approve", "reject"}:
        raise BankPipelineError("复核决策只能是 approve 或 reject。", exit_code=2)
    if not isinstance(reviewer, str) or not reviewer.strip():
        raise BankPipelineError("复核人标签不能为空。", exit_code=2)
    reviewer = reviewer.strip()
    if len(reviewer) > 100 or any(ord(char) < 32 for char in reviewer):
        raise BankPipelineError("复核人标签包含非法字符。", exit_code=2)

    notes_path = Path(review_notes_path)
    try:
        notes = notes_path.read_text(encoding="utf-8").strip()
    except FileNotFoundError as error:
        raise BankPipelineError(
            "复核备注不存在：{}".format(notes_path),
            exit_code=3,
        ) from error
    except (OSError, UnicodeDecodeError) as error:
        raise BankPipelineError(
            "复核备注无法读取：{}".format(error),
            exit_code=5,
        ) from error
    if not notes:
        raise BankPipelineError("复核备注不能为空。", exit_code=2)
    if len(notes) > 20000:
        raise BankPipelineError("复核备注过长。", exit_code=2)
    notes = _mask_contact(notes)

    if isinstance(confirmations, str):
        confirmation_values = {
            item.strip() for item in confirmations.split(",") if item.strip()
        }
    else:
        confirmation_values = {
            item for item in confirmations if isinstance(item, str) and item
        }
    unknown = confirmation_values - set(REQUIRED_CONFIRMATIONS)
    if unknown:
        raise BankPipelineError(
            "未知复核确认项：{}".format(", ".join(sorted(unknown))),
            exit_code=2,
        )
    if decision == "approve":
        missing = set(REQUIRED_CONFIRMATIONS) - confirmation_values
        if missing:
            raise BankPipelineError(
                "复核缺少确认项：{}".format(", ".join(sorted(missing))),
                exit_code=7,
            )

    review = {
        "schema_version": SCHEMA_VERSION,
        "candidate_id": manifest["candidate_id"],
        "candidate_sha256": _candidate_sha256(manifest),
        "decision": decision,
        "reviewer": reviewer,
        "reviewed_at": reviewed_at,
        "notes": notes,
        "confirmations": [
            item for item in REQUIRED_CONFIRMATIONS if item in confirmation_values
        ],
    }
    source_watch._write_json_atomic(candidate / "review.json", review)
    return {
        "ok": True,
        "candidate": str(candidate),
        "decision": decision,
        "candidate_sha256": review["candidate_sha256"],
    }


def _load_review(candidate, manifest):
    path = candidate / "review.json"
    review = _read_json(path, "人工复核")
    if review.get("decision") != "approve":
        raise BankPipelineError("候选尚未获得 approve 复核。", exit_code=7)
    if review.get("candidate_sha256") != _candidate_sha256(manifest):
        raise BankPipelineError("复核绑定的候选哈希不一致。", exit_code=7)
    missing = set(REQUIRED_CONFIRMATIONS) - set(review.get("confirmations", []))
    if missing:
        raise BankPipelineError(
            "复核缺少确认项：{}".format(", ".join(sorted(missing))),
            exit_code=7,
        )
    return review


def _copy_data_tree(source, target):
    import shutil

    shutil.copytree(
        source,
        target,
        ignore=shutil.ignore_patterns("history"),
    )


def _apply_candidate_to_data(candidate, manifest, source_data, target_data):
    _copy_data_tree(source_data, target_data)
    replacements = {
        "source-registry.json": "source-registry.candidate.json",
        "source-watch-state.json": "source-watch-state.candidate.json",
        "question-bank.json": "question-bank.candidate.json",
    }
    record_paths = {item["path"] for item in manifest.get("files", [])}
    for target_name, candidate_name in replacements.items():
        if candidate_name not in record_paths:
            raise BankPipelineError(
                "候选缺少文件：{}".format(candidate_name),
                exit_code=7,
            )
        target_path = target_data / target_name
        source_watch._write_text_atomic(
            target_path,
            (candidate / candidate_name).read_text(encoding="utf-8"),
        )


def _snapshot_id(now, candidate_sha256):
    timestamp = now.astimezone(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return "{}-{}".format(timestamp, candidate_sha256[:8])


def _snapshot_record(snapshot_dir, snapshot_id, status, created_at):
    files = []
    for name in (
        "source-registry.json",
        "source-watch-state.json",
        "question-bank.json",
    ):
        path = snapshot_dir / name
        files.append({
            "path": name,
            "size": path.stat().st_size,
            "sha256": source_watch._sha256_file(path),
        })
    manifest = {
        "schema_version": SCHEMA_VERSION,
        "snapshot_id": snapshot_id,
        "status": status,
        "created_at": created_at,
        "files": files,
    }
    source_watch._write_json_atomic(snapshot_dir / "manifest.json", manifest)
    return manifest


def _write_history_snapshot(data_dir, snapshot_id, status, created_at=None):
    history = data_dir / "history"
    history.mkdir(parents=True, exist_ok=True)
    target = history / snapshot_id
    if target.exists():
        raise BankPipelineError("历史快照已存在：{}".format(snapshot_id), exit_code=7)
    stage = Path(tempfile.mkdtemp(prefix=".snapshot-", dir=str(history)))
    try:
        for name in (
            "source-registry.json",
            "source-watch-state.json",
            "question-bank.json",
        ):
            source_watch._write_bytes_atomic(
                stage / name,
                (data_dir / name).read_bytes(),
            )
        manifest = _snapshot_record(
            stage,
            snapshot_id,
            status,
            created_at
            or dt.datetime.now(dt.timezone.utc).replace(
                microsecond=0,
            ).isoformat().replace("+00:00", "Z"),
        )
        source_watch._replace_path(stage, target)
        return target, manifest
    except Exception:
        import shutil

        shutil.rmtree(str(stage), ignore_errors=True)
        raise


def _load_history_snapshot(data_dir, snapshot_id):
    if (
        not isinstance(snapshot_id, str)
        or not snapshot_id
        or Path(snapshot_id).name != snapshot_id
        or snapshot_id in {".", ".."}
    ):
        raise BankPipelineError("历史快照 ID 非法。", exit_code=7)
    directory = data_dir / "history" / snapshot_id
    manifest = _read_json(directory / "manifest.json", "历史快照 manifest")
    if manifest.get("snapshot_id") != snapshot_id:
        raise BankPipelineError("历史快照 ID 与 manifest 不一致。", exit_code=7)
    records = manifest.get("files")
    if not isinstance(records, list) or len(records) != 3:
        raise BankPipelineError("历史快照 manifest 文件数量无效。", exit_code=7)
    seen = set()
    for record in records:
        name = record.get("path")
        if name not in {
            "source-registry.json",
            "source-watch-state.json",
            "question-bank.json",
        } or name in seen:
            raise BankPipelineError("历史快照包含非法文件。", exit_code=7)
        seen.add(name)
        path = directory / name
        if not path.is_file():
            raise BankPipelineError("历史快照文件缺失：{}".format(name), exit_code=7)
        if path.stat().st_size != record.get("size"):
            raise BankPipelineError("历史快照文件大小不一致：{}".format(name), exit_code=7)
        if source_watch._sha256_file(path) != record.get("sha256"):
            raise BankPipelineError("历史快照文件哈希不一致：{}".format(name), exit_code=7)
    return directory, manifest


def _read_current_files(data_dir):
    return {
        name: (data_dir / name).read_bytes()
        for name in (
            "source-registry.json",
            "source-watch-state.json",
            "question-bank.json",
        )
    }


def _restore_bytes(data_dir, payloads):
    for name, payload in payloads.items():
        source_watch._write_bytes_atomic(data_dir / name, payload)


def _replace_from_candidate(candidate, data_dir):
    for target_name, candidate_name in (
        ("source-registry.json", "source-registry.candidate.json"),
        ("source-watch-state.json", "source-watch-state.candidate.json"),
        ("question-bank.json", "question-bank.candidate.json"),
    ):
        source_watch._write_text_atomic(
            data_dir / target_name,
            (candidate / candidate_name).read_text(encoding="utf-8"),
        )


def _require_validation(candidate, manifest):
    validation = _read_json(candidate / "validation.json", "候选校验报告")
    if validation.get("ok") is not True:
        raise BankPipelineError("候选校验未通过。", exit_code=7)
    if validation.get("candidate_sha256") != _candidate_sha256(manifest):
        raise BankPipelineError("校验报告绑定的候选哈希不一致。", exit_code=7)
    if validation.get("review_sha256") != source_watch._sha256_file(
        candidate / "review.json"
    ):
        raise BankPipelineError("校验报告绑定的人工复核哈希不一致。", exit_code=7)
    return validation


def validate_candidate(candidate_dir, data_root, today=None):
    current = str(today or dt.date.today().isoformat())
    _parse_date(current, "today")
    data_dir = _data_dir(data_root)
    candidate, manifest = _load_candidate(candidate_dir)
    review = _load_review(candidate, manifest)
    candidate_bank = _read_json(
        candidate / "question-bank.candidate.json",
        "题库候选",
    )
    active_questions = [
        item
        for item in candidate_bank.get("questions", [])
        if isinstance(item, dict) and item.get("status") == "active"
    ]
    if len(active_questions) < 162:
        raise BankPipelineError(
            "候选至少需要保留 162 道 active 题目，当前 {} 道。".format(
                len(active_questions)
            ),
            exit_code=7,
        )
    if candidate_bank.get("bank_version") != manifest.get("target_bank_version"):
        raise BankPipelineError("候选题库版本与 manifest 不一致。", exit_code=7)
    official_bank = _read_json(data_dir / "question-bank.json", "正式题库")
    if manifest.get("base_bank_version") != official_bank.get("bank_version"):
        raise BankPipelineError(
            "候选基线版本与正式题库不一致，不能应用或校验。",
            exit_code=7,
        )
    if _compare_semver(
        _parse_semver(manifest.get("target_bank_version")),
        _parse_semver(manifest.get("base_bank_version")),
    ) <= 0:
        raise BankPipelineError("候选目标版本必须大于基线版本。", exit_code=7)

    with tempfile.TemporaryDirectory(prefix="yotta-resume-bank-validate-") as tmp:
        temp_data = Path(tmp) / "data"
        _apply_candidate_to_data(candidate, manifest, data_dir, temp_data)
        contract_report = validate_contracts(temp_data, current)

    if not contract_report.get("ok"):
        errors = "; ".join(
            "[{}] {}: {}".format(
                item.get("code"),
                item.get("path"),
                item.get("message"),
            )
            for item in contract_report.get("errors", [])
        )
        raise BankPipelineError(
            "候选契约校验失败：{}".format(errors),
            exit_code=6,
        )

    validation = {
        "schema_version": SCHEMA_VERSION,
        "ok": True,
        "validated_at": current,
        "candidate_id": manifest["candidate_id"],
        "candidate_sha256": _candidate_sha256(manifest),
        "review_sha256": source_watch._sha256_file(candidate / "review.json"),
        "checked_files": contract_report["checked_files"],
        "question_count": contract_report["question_count"],
        "source_count": contract_report["source_count"],
        "watch_state_count": contract_report["watch_state_count"],
        "bank_version": manifest["target_bank_version"],
        "reviewer": review["reviewer"],
    }
    source_watch._write_json_atomic(candidate / "validation.json", validation)
    return dict(validation, candidate=str(candidate))


def apply_candidate(candidate_dir, data_root, today=None, now=None):
    current = str(today or dt.date.today().isoformat())
    _parse_date(current, "today")
    now_value = now or dt.datetime.now(dt.timezone.utc).replace(
        microsecond=0,
    ).isoformat().replace("+00:00", "Z")
    now_dt = _parse_timestamp(now_value, "now")
    data_dir = _data_dir(data_root)
    candidate, manifest = _load_candidate(candidate_dir)
    _require_validation(candidate, manifest)

    validation = validate_candidate(candidate, data_dir, today=current)
    candidate_sha = validation["candidate_sha256"]
    snapshot_id = _snapshot_id(now_dt, candidate_sha)
    snapshot_dir, _ = _write_history_snapshot(
        data_dir,
        snapshot_id,
        "pre-apply",
        now_value,
    )
    current_files = _read_current_files(data_dir)
    try:
        _replace_from_candidate(candidate, data_dir)
        report = validate_contracts(data_dir, current)
        if not report.get("ok") or report.get("checked_files") != 15:
            raise BankPipelineError(
                "应用后契约校验失败。",
                exit_code=6,
            )
        applied_bank = _read_json(data_dir / "question-bank.json", "应用后题库")
        if applied_bank.get("bank_version") != manifest.get("target_bank_version"):
            raise BankPipelineError("应用后题库版本不一致。", exit_code=7)
    except Exception:
        _restore_bytes(data_dir, current_files)
        raise

    applied = {
        "schema_version": SCHEMA_VERSION,
        "ok": True,
        "applied_at": now_value,
        "snapshot_id": snapshot_id,
        "candidate_id": manifest["candidate_id"],
        "candidate_sha256": candidate_sha,
        "bank_version": manifest["target_bank_version"],
        "checked_files": report["checked_files"],
        "question_count": report["question_count"],
    }
    source_watch._write_json_atomic(snapshot_dir / "applied.json", applied)
    return dict(applied, history_path=str(snapshot_dir))


def rollback(snapshot_id, data_root, today=None, now=None):
    current = str(today or dt.date.today().isoformat())
    _parse_date(current, "today")
    now_value = now or dt.datetime.now(dt.timezone.utc).replace(
        microsecond=0,
    ).isoformat().replace("+00:00", "Z")
    now_dt = _parse_timestamp(now_value, "now")
    data_dir = _data_dir(data_root)
    snapshot_dir, snapshot_manifest = _load_history_snapshot(data_dir, snapshot_id)
    current_files = _read_current_files(data_dir)
    backup_id = "rollback-backup-{}-{}".format(
        now_dt.strftime("%Y%m%dT%H%M%SZ"),
        snapshot_id[-8:],
    )
    _write_history_snapshot(data_dir, backup_id, "pre-rollback", now_value)
    try:
        for name in (
            "source-registry.json",
            "source-watch-state.json",
            "question-bank.json",
        ):
            source_watch._write_bytes_atomic(
                data_dir / name,
                (snapshot_dir / name).read_bytes(),
            )
        report = validate_contracts(data_dir, current)
        if not report.get("ok") or report.get("checked_files") != 15:
            raise BankPipelineError("回滚后契约校验失败。", exit_code=6)
    except Exception:
        _restore_bytes(data_dir, current_files)
        raise

    record = {
        "schema_version": SCHEMA_VERSION,
        "ok": True,
        "rolled_back_at": now_value,
        "snapshot_id": snapshot_id,
        "rollback_backup_id": backup_id,
        "checked_files": report["checked_files"],
        "question_count": report["question_count"],
        "snapshot_status": snapshot_manifest.get("status"),
    }
    source_watch._write_json_atomic(snapshot_dir / "rollback.json", record)
    return dict(record, history_path=str(snapshot_dir))


def propose_candidate(
    data_root,
    source_candidate_dir,
    patches_path,
    out_dir,
    target_version,
    today=None,
):
    created_at = str(today or dt.date.today().isoformat())
    _parse_date(created_at, "today")
    target_semver = _parse_semver(target_version)
    data_dir = _data_dir(data_root)
    source_candidate, source_manifest = _load_candidate(source_candidate_dir)
    registry_candidate = _read_json(
        source_candidate / "source-registry.candidate.json",
        "来源候选",
    )
    state_candidate = _read_json(
        source_candidate / "source-watch-state.candidate.json",
        "来源指纹候选",
    )
    source_diff = _read_json(source_candidate / "diff.json", "来源差异")
    bank = _read_json(data_dir / "question-bank.json", "正式题库")
    base_version = bank.get("bank_version")
    if _compare_semver(target_semver, _parse_semver(base_version)) <= 0:
        raise BankPipelineError(
            "目标题库版本必须大于当前版本 {}".format(base_version),
            exit_code=5,
        )
    patches = _load_patches(patches_path)
    candidate_bank, touched = _apply_patches(bank, patches, created_at)
    candidate_bank["bank_version"] = target_version
    candidate_bank["generated_at"] = created_at
    question_diff = _question_diff(bank["questions"], candidate_bank["questions"])
    candidate_id = "bank-" + source_watch._canonical_hash({
        "source_candidate": source_manifest,
        "base_version": base_version,
        "target_version": target_version,
        "patches": patches,
    })[:16]

    def writer(stage):
        paths = {
            "source-registry.candidate.json": stage / "source-registry.candidate.json",
            "source-watch-state.candidate.json": stage / "source-watch-state.candidate.json",
            "question-bank.candidate.json": stage / "question-bank.candidate.json",
            "diff.json": stage / "diff.json",
            "review.md": stage / "review.md",
        }
        source_watch._write_json_atomic(
            paths["source-registry.candidate.json"],
            registry_candidate,
        )
        source_watch._write_json_atomic(
            paths["source-watch-state.candidate.json"],
            state_candidate,
        )
        source_watch._write_json_atomic(
            paths["question-bank.candidate.json"],
            candidate_bank,
        )
        diff = {
            "schema_version": SCHEMA_VERSION,
            "generated_at": created_at,
            "sources": source_diff.get("sources", []),
            "questions": question_diff,
            "risks": source_diff.get("risks", []),
        }
        source_watch._write_json_atomic(paths["diff.json"], diff)
        source_watch._write_text_atomic(
            paths["review.md"],
            _render_review(candidate_id, diff, question_diff),
        )
        manifest = _manifest(
            candidate_id,
            created_at,
            base_version,
            target_version,
            diff,
            paths,
        )
        source_watch._write_json_atomic(stage / "manifest.json", manifest)
        return {
            "ok": True,
            "candidate": str(out_dir),
            "candidate_id": candidate_id,
            "base_bank_version": base_version,
            "target_bank_version": target_version,
            "source_change_count": len(diff["sources"]),
            "question_change_count": len(question_diff),
            "touched_question_count": len(touched),
        }

    return source_watch._commit_candidate(out_dir, writer)

