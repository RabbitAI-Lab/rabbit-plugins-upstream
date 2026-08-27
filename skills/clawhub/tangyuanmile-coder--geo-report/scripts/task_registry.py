#!/usr/bin/env python3
"""Maintain and search local AIDSO diagnosis manifests without network calls."""

from __future__ import annotations

import argparse
from contextlib import contextmanager
from decimal import Decimal, InvalidOperation
import json
import os
import sys
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Optional

from plan_diagnosis import compute_plan_digest


JOB_STATUSES = {
    "PLANNED",
    "RESERVED",
    "SUBMITTED",
    "ING",
    "SUCCESS",
    "FAILED",
    "UNKNOWN",
}
CONFIRMATION_TEXT = "确认执行"
RECOVERY_SOURCE_TYPES = {
    "aidso_task_record",
    "aidso_audit_log",
    "aidso_billing_record",
}
RECOVERY_MATCH_FIELDS = {
    "diagnosis_id",
    "task_name",
    "platform_code",
    "mode",
    "prompt",
    "created_at",
}


def now_text() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def is_within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
    except ValueError:
        return False
    return True


def workspace_path(
    path: Path,
    label: str,
    *,
    required_root: Optional[Path] = None,
    must_exist: bool = False,
) -> Path:
    workspace = Path.cwd().resolve()
    candidate = path if path.is_absolute() else workspace / path
    try:
        resolved = candidate.resolve(strict=must_exist)
    except OSError as exc:
        raise ValueError(f"{label}无法解析：{exc}") from exc
    if not is_within(resolved, workspace):
        raise ValueError(f"{label}必须位于当前工作区内")
    if required_root is not None:
        root = (workspace / required_root).resolve()
        if not is_within(root, workspace):
            raise ValueError(f"{label}的规定目录不得通过符号链接逃逸工作区")
        if not is_within(resolved, root):
            raise ValueError(
                f"{label}必须位于当前工作区 {required_root.as_posix()}/ 下"
            )
    return resolved


def manifest_path(path: Path) -> Path:
    return workspace_path(
        path,
        "manifest",
        required_root=Path(".aidso-geo/tasks"),
        must_exist=True,
    )


def load_manifest(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"无法读取 manifest {path}: {exc}") from exc
    if not isinstance(value, dict) or "diagnosis_id" not in value or "jobs" not in value:
        raise ValueError(f"不是有效的诊断 manifest：{path}")
    return value


def atomic_write(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent, text=True)
    try:
        with os.fdopen(handle, "w", encoding="utf-8") as stream:
            json.dump(value, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
        os.replace(temp_name, path)
    except Exception:
        try:
            os.unlink(temp_name)
        except OSError:
            pass
        raise


@contextmanager
def manifest_lock(path: Path):
    """Serialize paid-state transitions without relying on platform-specific locks."""
    lock_path = path.with_name(f".{path.name}.lock")
    try:
        descriptor = os.open(str(lock_path), os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as exc:
        raise ValueError(f"manifest 正在被其他操作占用：{path}") from exc
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
            stream.write(f"pid={os.getpid()} time={now_text()}\n")
        yield
    finally:
        try:
            lock_path.unlink()
        except FileNotFoundError:
            pass


def get_job(manifest: dict, job_id: str) -> dict:
    for job in manifest.get("jobs", []):
        if job.get("job_id") == job_id:
            return job
    raise ValueError(f"找不到 job_id：{job_id}")


def summarize(path: Path, manifest: dict) -> dict:
    counts: dict[str, int] = {}
    for job in manifest.get("jobs", []):
        status = str(job.get("status") or "UNKNOWN").upper()
        counts[status] = counts.get(status, 0) + 1
    return {
        "path": str(path.resolve()),
        "diagnosis_id": manifest.get("diagnosis_id"),
        "task_name": manifest.get("task_name"),
        "status": manifest.get("status"),
        "report_path": manifest.get("plan", {}).get("report_path"),
        "total_points": manifest.get("estimate", {}).get("total_points"),
        "job_counts": counts,
    }


def canonical_positive_quote(manifest: dict) -> str:
    estimate = manifest.get("estimate")
    if not isinstance(estimate, dict):
        raise ValueError("manifest 缺少确认报价")
    raw = estimate.get("quoted_total_points")
    if not isinstance(raw, str) or not raw:
        raise ValueError("确认报价必须是非空的规范正数")
    try:
        value = Decimal(raw)
    except InvalidOperation as exc:
        raise ValueError("确认报价必须是规范十进制数") from exc
    if not value.is_finite() or value <= 0:
        raise ValueError("确认报价必须大于 0")
    canonical = format(value.normalize(), "f")
    if canonical == "-0":
        canonical = "0"
    if raw != canonical:
        raise ValueError(f"确认报价必须使用规范格式：{canonical}")
    atomic_calls = estimate.get("atomic_calls")
    jobs = manifest.get("jobs")
    if (
        isinstance(atomic_calls, bool)
        or not isinstance(atomic_calls, int)
        or atomic_calls < 1
        or not isinstance(jobs, list)
        or atomic_calls != len(jobs)
    ):
        raise ValueError("原子调用数必须是正整数且与 jobs 数量一致")
    return raw


def authorization_details(manifest: dict) -> dict:
    stored_digest = str(manifest.get("plan_digest") or "")
    if not stored_digest:
        raise ValueError("manifest 缺少计划摘要，必须重新规划并确认")
    current_digest = compute_plan_digest(manifest)
    if current_digest != stored_digest:
        raise ValueError("当前计划或报价已变更，原确认失效，必须重新确认")

    quoted_points = canonical_positive_quote(manifest)
    confirmation = manifest.get("confirmation")
    if not isinstance(confirmation, dict) or not manifest.get("confirmed_at"):
        raise ValueError("任务尚未确认，不得绑定付费请求")
    if confirmation.get("text") != CONFIRMATION_TEXT:
        raise ValueError("确认文本不是精确的“确认执行”")
    if confirmation.get("plan_digest") != stored_digest:
        raise ValueError("确认摘要已过期或与当前计划不匹配")
    if str(confirmation.get("quoted_points") or "") != quoted_points:
        raise ValueError("确认报价与当前报价不匹配")
    if confirmation.get("confirmed_at") != manifest.get("confirmed_at"):
        raise ValueError("确认时间不匹配，必须重新确认")
    return {
        "authorized": True,
        "plan_digest": stored_digest,
        "quoted_points": quoted_points,
        "confirmed_at": manifest["confirmed_at"],
    }


def parse_recovery_evidence(raw: str) -> dict:
    try:
        evidence = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError("recovery evidence 必须是结构化 JSON 对象") from exc
    required = {"source_type", "record_reference", "checked_at", "matched_fields"}
    if not isinstance(evidence, dict) or set(evidence) != required:
        raise ValueError(
            "recovery evidence 必须且只能包含 source_type、record_reference、checked_at、matched_fields"
        )
    source_type = evidence.get("source_type")
    if source_type not in RECOVERY_SOURCE_TYPES:
        raise ValueError("recovery evidence 的 source_type 不是允许的爱搜权威记录")
    record_reference = evidence.get("record_reference")
    if not isinstance(record_reference, str) or len(record_reference.strip()) < 8:
        raise ValueError("recovery evidence 缺少可审计的 record_reference")
    checked_at = evidence.get("checked_at")
    if not isinstance(checked_at, str):
        raise ValueError("recovery evidence 缺少 checked_at")
    try:
        parsed_time = datetime.fromisoformat(checked_at)
    except ValueError as exc:
        raise ValueError("recovery evidence 的 checked_at 必须是 ISO-8601") from exc
    if parsed_time.tzinfo is None:
        raise ValueError("recovery evidence 的 checked_at 必须包含时区")
    matched_fields = evidence.get("matched_fields")
    if (
        not isinstance(matched_fields, list)
        or len(matched_fields) < 2
        or any(not isinstance(item, str) for item in matched_fields)
        or len(set(matched_fields)) != len(matched_fields)
        or not set(matched_fields).issubset(RECOVERY_MATCH_FIELDS)
        or not set(matched_fields).intersection({"diagnosis_id", "task_name"})
        or not set(matched_fields).intersection({"platform_code", "mode", "prompt"})
    ):
        raise ValueError(
            "recovery evidence 的 matched_fields 必须用任务标识和调用范围至少各核对一项"
        )
    return {
        "source_type": source_type,
        "record_reference": record_reference.strip(),
        "checked_at": checked_at,
        "matched_fields": matched_fields,
    }


def command_mark_confirmed(args: argparse.Namespace) -> dict:
    path = manifest_path(args.manifest)
    with manifest_lock(path):
        manifest = load_manifest(path)
        if args.confirmation_text != CONFIRMATION_TEXT:
            raise ValueError("必须提供精确确认文本“确认执行”")
        current_digest = compute_plan_digest(manifest)
        if not manifest.get("plan_digest") or manifest.get("plan_digest") != current_digest:
            raise ValueError("当前计划或报价已变更，请重新生成确认卡")
        if args.plan_digest != current_digest:
            raise ValueError("提供的计划摘要与当前计划不匹配")
        quoted_points = canonical_positive_quote(manifest)
        if args.quoted_points != quoted_points:
            raise ValueError("提供的报价积分与当前报价不匹配")
        confirmed_at = now_text()
        manifest["confirmed_at"] = confirmed_at
        manifest["confirmation"] = {
            "text": args.confirmation_text,
            "plan_digest": args.plan_digest,
            "quoted_points": args.quoted_points,
            "confirmed_at": confirmed_at,
        }
        manifest["status"] = "CONFIRMED"
        atomic_write(path, manifest)
        result = summarize(path, manifest)
        result.update(authorization_details(manifest))
        return result


def command_authorize(args: argparse.Namespace) -> dict:
    path = manifest_path(args.manifest)
    with manifest_lock(path):
        manifest = load_manifest(path)
        authorization = authorization_details(manifest)
        job = get_job(manifest, args.job_id)
        if job.get("request_id"):
            raise ValueError(f"{args.job_id} 已绑定请求，不得再次授权付费创建")
        status = str(job.get("status") or "PLANNED").upper()
        if status != "PLANNED":
            raise ValueError(
                f"{args.job_id} 当前状态为 {status}，只有 PLANNED job 可授权"
            )
        job["status"] = "RESERVED"
        job["reserved_at"] = now_text()
        job["reservation_plan_digest"] = authorization["plan_digest"]
        manifest["status"] = "PARTIAL"
        atomic_write(path, manifest)
        result = summarize(path, manifest)
        result.update(authorization)
        result["authorized_job_id"] = args.job_id
        return result


def command_bind(args: argparse.Namespace) -> dict:
    path = manifest_path(args.manifest)
    with manifest_lock(path):
        manifest = load_manifest(path)
        authorization = authorization_details(manifest)
        request_id = args.request_id.strip()
        if not request_id:
            raise ValueError(f"{args.job_id} 的 request_id 为空")
        job = get_job(manifest, args.job_id)
        existing = job.get("request_id")
        if existing:
            if existing != request_id:
                raise ValueError(f"{args.job_id} 已绑定其他 request_id：{existing}")
            return summarize(path, manifest)
        if str(job.get("status") or "").upper() != "RESERVED":
            raise ValueError(f"{args.job_id} 未通过一次性 authorize 预留")
        if job.get("reservation_plan_digest") != authorization["plan_digest"]:
            raise ValueError(f"{args.job_id} 的预留摘要已失效，必须人工核查")
        job["request_id"] = request_id
        job["status"] = "SUBMITTED"
        job["submitted_at"] = job.get("submitted_at") or now_text()
        manifest["submitted_at"] = manifest.get("submitted_at") or now_text()
        submitted = sum(1 for item in manifest["jobs"] if item.get("request_id"))
        manifest["status"] = (
            "SUBMITTED" if submitted == len(manifest["jobs"]) else "PARTIAL"
        )
        atomic_write(path, manifest)
        return summarize(path, manifest)


def command_bind_batch(args: argparse.Namespace) -> dict:
    path = manifest_path(args.manifest)
    bindings_path = workspace_path(args.bindings, "bindings", must_exist=True)
    try:
        bindings = json.loads(bindings_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"无法读取 bindings：{exc}") from exc
    if not isinstance(bindings, dict):
        raise ValueError("bindings 必须是 {job_id: request_id} 对象")
    with manifest_lock(path):
        manifest = load_manifest(path)
        authorization = authorization_details(manifest)
        prepared = []
        for job_id, request_id in bindings.items():
            job = get_job(manifest, str(job_id))
            request_id = str(request_id).strip()
            if not request_id:
                raise ValueError(f"{job_id} 的 request_id 为空")
            existing = job.get("request_id")
            if existing and existing != request_id:
                raise ValueError(f"{job_id} 已绑定其他 request_id：{existing}")
            if not existing and str(job.get("status") or "").upper() != "RESERVED":
                raise ValueError(f"{job_id} 未通过一次性 authorize 预留")
            if (
                not existing
                and job.get("reservation_plan_digest") != authorization["plan_digest"]
            ):
                raise ValueError(f"{job_id} 的预留摘要已失效，必须人工核查")
            prepared.append((job, request_id))
        for job, request_id in prepared:
            if not job.get("request_id"):
                job["request_id"] = request_id
                job["status"] = "SUBMITTED"
                job["submitted_at"] = job.get("submitted_at") or now_text()
        manifest["submitted_at"] = manifest.get("submitted_at") or now_text()
        submitted = sum(1 for item in manifest["jobs"] if item.get("request_id"))
        manifest["status"] = (
            "SUBMITTED" if submitted == len(manifest["jobs"]) else "PARTIAL"
        )
        atomic_write(path, manifest)
        return summarize(path, manifest)


def command_mark_ambiguous(args: argparse.Namespace) -> dict:
    path = manifest_path(args.manifest)
    detail = args.detail.strip()
    if not detail:
        raise ValueError("不明确结果必须记录非空 detail")
    with manifest_lock(path):
        manifest = load_manifest(path)
        authorization = authorization_details(manifest)
        job = get_job(manifest, args.job_id)
        if str(job.get("status") or "").upper() != "RESERVED":
            raise ValueError(f"{args.job_id} 未处于 RESERVED 状态")
        if job.get("reservation_plan_digest") != authorization["plan_digest"]:
            raise ValueError(f"{args.job_id} 的预留摘要已失效，必须人工核查")
        job["status"] = "UNKNOWN"
        job["ambiguous_at"] = now_text()
        job["ambiguity_detail"] = detail
        manifest["status"] = "PARTIAL"
        atomic_write(path, manifest)
        return summarize(path, manifest)


def command_bind_recovered(args: argparse.Namespace) -> dict:
    path = manifest_path(args.manifest)
    request_id = args.request_id.strip()
    if not request_id:
        raise ValueError(f"{args.job_id} 的 recovered request_id 为空")
    evidence = parse_recovery_evidence(args.evidence.strip())
    with manifest_lock(path):
        manifest = load_manifest(path)
        authorization_details(manifest)
        job = get_job(manifest, args.job_id)
        if job.get("request_id"):
            raise ValueError(f"{args.job_id} 已绑定 request_id")
        if (
            str(job.get("status") or "").upper() != "UNKNOWN"
            or not job.get("ambiguous_at")
        ):
            raise ValueError(
                f"{args.job_id} 只有记录过不明确创建结果后才能 bind-recovered"
            )
        job["request_id"] = request_id
        job["status"] = "SUBMITTED"
        job["recovered_at"] = now_text()
        job["recovery_evidence"] = evidence
        job["submitted_at"] = job.get("submitted_at") or job["recovered_at"]
        manifest["submitted_at"] = manifest.get("submitted_at") or job["recovered_at"]
        submitted = sum(1 for item in manifest["jobs"] if item.get("request_id"))
        manifest["status"] = (
            "SUBMITTED" if submitted == len(manifest["jobs"]) else "PARTIAL"
        )
        atomic_write(path, manifest)
        return summarize(path, manifest)


def command_job_status(args: argparse.Namespace) -> dict:
    status = args.status.upper()
    if status not in JOB_STATUSES:
        raise ValueError(f"无效 job 状态：{status}")
    if status in {"PLANNED", "RESERVED", "SUBMITTED", "UNKNOWN"}:
        raise ValueError(f"不能通过 job-status 设置受保护状态：{status}")
    path = manifest_path(args.manifest)
    with manifest_lock(path):
        manifest = load_manifest(path)
        job = get_job(manifest, args.job_id)
        current = str(job.get("status") or "UNKNOWN").upper()
        request_id = str(job.get("request_id") or "").strip()
        if not request_id or current not in {"SUBMITTED", "ING", "SUCCESS", "FAILED"}:
            raise ValueError(
                f"{args.job_id} 没有已绑定的提交记录，不得更新远程任务状态"
            )
        if current in {"SUCCESS", "FAILED"} and status != current:
            raise ValueError(f"{args.job_id} 已是终态 {current}，不得改写为 {status}")
        job["status"] = status
        job["status_checked_at"] = now_text()
        statuses = [
            str(item.get("status") or "UNKNOWN").upper()
            for item in manifest["jobs"]
        ]
        if statuses and all(item == "SUCCESS" for item in statuses):
            manifest["status"] = "SUCCESS"
        elif statuses and all(item in {"SUCCESS", "FAILED"} for item in statuses):
            manifest["status"] = "FAILED"
        elif any(item == "ING" for item in statuses):
            manifest["status"] = "ING"
        else:
            manifest["status"] = "PARTIAL"
        atomic_write(path, manifest)
        return summarize(path, manifest)


def command_summary(args: argparse.Namespace) -> dict:
    path = manifest_path(args.manifest)
    manifest = load_manifest(path)
    return summarize(path, manifest)


def command_find(args: argparse.Namespace) -> dict:
    query = args.query.strip()
    if not query:
        raise ValueError("任务查询标识不得为空")
    registry_dir = (Path.cwd().resolve() / ".aidso-geo" / "tasks").resolve()
    if not is_within(registry_dir, Path.cwd().resolve()):
        raise ValueError("任务注册表目录通过符号链接逃逸工作区")
    matches = []
    for candidate in sorted(registry_dir.rglob("*.json")) if registry_dir.is_dir() else []:
        try:
            path = manifest_path(candidate)
            manifest = load_manifest(path)
        except ValueError:
            continue
        identifiers = {str(manifest.get("diagnosis_id") or ""), str(manifest.get("task_name") or "")}
        identifiers.update(str(job.get("request_id") or "") for job in manifest.get("jobs", []))
        if query in identifiers:
            matches.append(summarize(path, manifest))
    if not matches:
        raise ValueError(f"未找到任务：{query}")
    if len(matches) > 1:
        raise ValueError(f"查询命中 {len(matches)} 个任务，请使用诊断 ID 或原子 reqId")
    return matches[0]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    p = subparsers.add_parser("mark-confirmed")
    p.add_argument("manifest", type=Path)
    p.add_argument("--confirmation-text", required=True)
    p.add_argument("--plan-digest", required=True)
    p.add_argument("--quoted-points", required=True)
    p.set_defaults(handler=command_mark_confirmed)

    p = subparsers.add_parser("authorize")
    p.add_argument("manifest", type=Path)
    p.add_argument("job_id")
    p.set_defaults(handler=command_authorize)

    p = subparsers.add_parser("bind")
    p.add_argument("manifest", type=Path)
    p.add_argument("job_id")
    p.add_argument("request_id")
    p.set_defaults(handler=command_bind)

    p = subparsers.add_parser("bind-batch")
    p.add_argument("manifest", type=Path)
    p.add_argument("bindings", type=Path)
    p.set_defaults(handler=command_bind_batch)

    p = subparsers.add_parser("mark-ambiguous")
    p.add_argument("manifest", type=Path)
    p.add_argument("job_id")
    p.add_argument("--detail", required=True)
    p.set_defaults(handler=command_mark_ambiguous)

    p = subparsers.add_parser("bind-recovered")
    p.add_argument("manifest", type=Path)
    p.add_argument("job_id")
    p.add_argument("request_id")
    p.add_argument("--evidence", required=True)
    p.set_defaults(handler=command_bind_recovered)

    p = subparsers.add_parser("job-status")
    p.add_argument("manifest", type=Path)
    p.add_argument("job_id")
    p.add_argument("status")
    p.set_defaults(handler=command_job_status)

    p = subparsers.add_parser("summary")
    p.add_argument("manifest", type=Path)
    p.set_defaults(handler=command_summary)

    p = subparsers.add_parser("find")
    p.add_argument("query")
    p.set_defaults(handler=command_find)

    args = parser.parse_args()
    try:
        print(json.dumps(args.handler(args), ensure_ascii=False, indent=2))
        return 0
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
