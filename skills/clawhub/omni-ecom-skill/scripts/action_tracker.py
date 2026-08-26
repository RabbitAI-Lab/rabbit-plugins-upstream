#!/usr/bin/env python3
"""Track proposed e-commerce actions, approvals, execution and outcomes.

The tracker is deliberately deterministic and fail-closed: an action that needs
approval cannot become executable, and an executed action cannot become verified
without an outcome record.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ACTION_ID_RE = re.compile(r"^A[A-Za-z0-9._-]{2,80}$")
RUN_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{2,80}$")
STATUSES = {
    "proposed", "pending_approval", "approved", "rejected", "scheduled",
    "executed", "verified", "rolled_back", "blocked",
}
TERMINAL = {"rejected", "verified", "rolled_back", "blocked"}


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def json_dump(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json_dump(payload), encoding="utf-8")
    temporary.replace(path)


def load_action(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise ValueError(f"行动记录不存在: {path}")
    payload = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(payload, dict):
        raise ValueError("行动记录根对象必须是 JSON 对象")
    if payload.get("schema_version") != "1.0":
        raise ValueError("行动记录 schema_version 必须为 1.0")
    if payload.get("status") not in STATUSES:
        raise ValueError("行动记录 status 无效")
    if not ACTION_ID_RE.fullmatch(str(payload.get("action_id", ""))):
        raise ValueError("action_id 必须以 A 开头且只含安全字符")
    return payload


def events_path(action_path: Path) -> Path:
    return action_path.with_suffix(".events.jsonl")


def append_event(path: Path, action: dict[str, Any], event_type: str, actor: str, **details: Any) -> dict[str, Any]:
    event: dict[str, Any] = {
        "at": now(),
        "type": event_type,
        "actor": actor,
        "action_id": action["action_id"],
        "from_status": details.pop("from_status", None),
        "to_status": details.pop("to_status", action.get("status")),
    }
    event.update({key: value for key, value in details.items() if value is not None})
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, ensure_ascii=False) + "\n")
    return event


def update_run_refs(run_dir: Path, key: str, path: Path) -> None:
    """Best-effort write-back into the run ledger without overwriting old refs."""
    run_path = run_dir / "run.json"
    if not run_path.is_file():
        return
    record = json.loads(run_path.read_text(encoding="utf-8-sig"))
    if not isinstance(record, dict):
        return
    try:
        reference = str(path.resolve().relative_to(run_dir.resolve())).replace("\\", "/")
    except ValueError:
        reference = path.name
    refs = record.setdefault(key, [])
    if reference not in refs:
        refs.append(reference)
    record["updated_at"] = now()
    write_json(run_path, record)


def find_run_dir(path: Path) -> Path:
    for parent in (path.parent, *path.parents):
        if (parent / "run.json").is_file():
            return parent
    return path.parent


def set_status(action: dict[str, Any], target: str) -> None:
    action["status"] = target
    at = now()
    if target == "executed":
        action["executed_at"] = at
    if target == "verified":
        action["verified_at"] = at


def action_path_from_args(args: argparse.Namespace) -> Path:
    return Path(args.action_file).resolve()


def create(args: argparse.Namespace) -> int:
    if not ACTION_ID_RE.fullmatch(args.action_id):
        raise ValueError("action_id 必须以 A 开头且只含安全字符")
    if not RUN_ID_RE.fullmatch(args.run_id):
        raise ValueError("run_id 包含不安全字符或长度不合法")
    run_dir = Path(args.root).resolve()
    if not run_dir.is_dir():
        raise ValueError(f"运行目录不存在: {run_dir}")
    output = Path(args.output).resolve() if args.output else run_dir / "approvals" / f"{args.action_id}.json"
    if output.exists():
        raise ValueError(f"不覆盖已有行动记录: {output}")
    required = bool(args.approval_required)
    at = now()
    action: dict[str, Any] = {
        "schema_version": "1.0",
        "action_id": args.action_id,
        "run_id": args.run_id,
        "client_scope": args.client_scope,
        "priority": args.priority,
        "action": args.action,
        "owner": args.owner,
        "target": args.target,
        "baseline": args.baseline or "",
        "acceptance": args.acceptance,
        "stop_condition": args.stop_condition,
        "approval_required": required,
        "approval_state": "pending" if required else "not_required",
        "status": "pending_approval" if required else "proposed",
        "proposed_at": at,
        "approved_at": None,
        "executed_at": None,
        "verified_at": None,
        "outcome": None,
        "source_ids": args.source_id or [],
        "artifact_refs": args.artifact_ref or [],
        "events_file": events_path(output).name,
    }
    write_json(output, action)
    update_run_refs(run_dir, "action_refs", output)
    event = append_event(events_path(output), action, "action_proposed", args.actor, to_status=action["status"], approval_required=required)
    print(json_dump({"status": "PASS", "action_file": str(output), "action": action, "event": event}), end="")
    return 0


def approval_record_path(action_path: Path, action_id: str) -> Path:
    return action_path.with_name(f"{action_id}.approval.json")


def approve(args: argparse.Namespace) -> int:
    path = action_path_from_args(args)
    action = load_action(path)
    if not action.get("approval_required"):
        raise ValueError("该行动未要求审批，不能伪造审批记录")
    if action["status"] != "pending_approval":
        raise ValueError(f"只有 pending_approval 可以审批，当前为 {action['status']}")
    decision = args.decision
    at = now()
    old = action["status"]
    action["approval_state"] = decision
    action["status"] = "approved" if decision == "approved" else "rejected"
    if decision == "approved":
        action["approved_at"] = at
    approval_id = f"AP{action['action_id'][1:]}"
    approval = {
        "schema_version": "1.0",
        "approval_id": approval_id,
        "action_id": action["action_id"],
        "run_id": action["run_id"],
        "client_scope": action["client_scope"],
        "state": decision,
        "actor": args.approver,
        "reason": args.reason or "",
        "decided_at": at,
    }
    approval_path = approval_record_path(path, action["action_id"])
    write_json(approval_path, approval)
    write_json(path, action)
    update_run_refs(find_run_dir(path), "approval_refs", approval_path)
    event = append_event(events_path(path), action, "approval_decided", args.approver, from_status=old, to_status=action["status"], decision=decision, reason=args.reason or "")
    print(json_dump({"status": "PASS", "action_file": str(path), "approval_file": str(approval_path), "action": action, "event": event}), end="")
    return 0


def can_transition(action: dict[str, Any], target: str) -> None:
    current = action["status"]
    if target not in STATUSES:
        raise ValueError(f"非法目标状态: {target}")
    if current in TERMINAL and target != "blocked":
        raise ValueError(f"终态 {current} 不得继续流转")
    if target == "approved":
        raise ValueError("approved 必须通过 approve 命令产生")
    if target == "executed" and action.get("approval_required") and action.get("approval_state") != "approved":
        raise ValueError("审批未通过，不能进入 executed")
    if target in {"scheduled", "executed"} and action.get("approval_state") == "rejected":
        raise ValueError("已拒绝的行动不能执行")
    allowed: dict[str, set[str]] = {
        "proposed": {"pending_approval", "scheduled", "blocked"},
        "pending_approval": {"blocked"},
        "approved": {"scheduled", "executed", "blocked"},
        "scheduled": {"executed", "blocked"},
        "executed": {"blocked", "rolled_back"},
        "rejected": set(),
        "verified": set(),
        "rolled_back": set(),
        "blocked": set(),
    }
    if target not in allowed.get(current, set()):
        raise ValueError(f"不允许的状态流转: {current} -> {target}")


def transition(args: argparse.Namespace) -> int:
    path = action_path_from_args(args)
    action = load_action(path)
    can_transition(action, args.status)
    old = action["status"]
    set_status(action, args.status)
    if args.status in {"blocked", "rolled_back"} and not args.reason:
        raise ValueError("blocked/rolled_back 必须提供 reason")
    if args.reason:
        action["last_reason"] = args.reason
    write_json(path, action)
    update_run_refs(find_run_dir(path), "outcome_refs", events_path(path))
    event = append_event(events_path(path), action, "status_changed", args.actor, from_status=old, to_status=args.status, reason=args.reason or "")
    print(json_dump({"status": "PASS", "action_file": str(path), "action": action, "event": event}), end="")
    return 0


def outcome(args: argparse.Namespace) -> int:
    path = action_path_from_args(args)
    action = load_action(path)
    if action["status"] != "executed":
        raise ValueError(f"只有 executed 可以写回结果，当前为 {action['status']}")
    at = now()
    action["outcome"] = {
        "result": args.result,
        "actual": args.actual,
        "metric": args.metric,
        "window": args.window,
        "notes": args.notes or "",
        "observed_at": at,
    }
    if args.result == "met":
        target = "verified"
        action["verified_at"] = at
    elif args.result == "not_met":
        target = "rolled_back"
        action["verified_at"] = at
        action["last_reason"] = args.notes or "验收未达标"
    else:
        target = "blocked"
        action["last_reason"] = args.notes or "结果不可判定，等待补证据"
    old = action["status"]
    action["status"] = target
    write_json(path, action)
    event = append_event(events_path(path), action, "outcome_recorded", args.actor, from_status=old, to_status=target, result=args.result, metric=args.metric, window=args.window)
    print(json_dump({"status": "PASS", "action_file": str(path), "action": action, "event": event}), end="")
    return 0


def show(args: argparse.Namespace) -> int:
    path = action_path_from_args(args)
    action = load_action(path)
    events = []
    event_file = events_path(path)
    if event_file.is_file():
        for line in event_file.read_text(encoding="utf-8-sig").splitlines():
            if line.strip():
                events.append(json.loads(line))
    print(json_dump({"action": action, "events": events}), end="")
    return 0


def list_actions(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    directory = root / "approvals"
    items = []
    if directory.is_dir():
        for path in sorted(directory.glob("A*.json")):
            if path.name.endswith(".approval.json"):
                continue
            try:
                item = load_action(path)
            except ValueError:
                continue
            if args.status and item.get("status") != args.status:
                continue
            items.append({"action_id": item["action_id"], "status": item["status"], "approval_state": item["approval_state"], "priority": item["priority"], "action": item["action"], "file": str(path)})
    print(json_dump({"status": "PASS", "count": len(items), "actions": items}), end="")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="omni-ecom 行动审批与结果回写台账")
    sub = parser.add_subparsers(dest="command", required=True)
    create_p = sub.add_parser("create")
    create_p.add_argument("--root", required=True, help="run 目录")
    create_p.add_argument("--action-id", required=True)
    create_p.add_argument("--run-id", required=True)
    create_p.add_argument("--client-scope", required=True)
    create_p.add_argument("--priority", choices=["P0", "P1", "P2"], required=True)
    create_p.add_argument("--action", required=True)
    create_p.add_argument("--owner", required=True)
    create_p.add_argument("--target", required=True)
    create_p.add_argument("--baseline")
    create_p.add_argument("--acceptance", required=True)
    create_p.add_argument("--stop-condition", required=True)
    create_p.add_argument("--approval-required", action="store_true")
    create_p.add_argument("--source-id", action="append")
    create_p.add_argument("--artifact-ref", action="append")
    create_p.add_argument("--actor", default="omni-ecom")
    create_p.add_argument("--output")

    approve_p = sub.add_parser("approve")
    approve_p.add_argument("--action-file", required=True)
    approve_p.add_argument("--approver", required=True)
    approve_p.add_argument("--decision", choices=["approved", "rejected"], required=True)
    approve_p.add_argument("--reason")

    transition_p = sub.add_parser("transition")
    transition_p.add_argument("--action-file", required=True)
    transition_p.add_argument("--status", choices=sorted(STATUSES), required=True)
    transition_p.add_argument("--actor", default="omni-ecom")
    transition_p.add_argument("--reason")

    outcome_p = sub.add_parser("outcome")
    outcome_p.add_argument("--action-file", required=True)
    outcome_p.add_argument("--result", choices=["met", "not_met", "inconclusive"], required=True)
    outcome_p.add_argument("--actual", required=True)
    outcome_p.add_argument("--metric", required=True)
    outcome_p.add_argument("--window", required=True)
    outcome_p.add_argument("--notes")
    outcome_p.add_argument("--actor", default="omni-ecom")

    show_p = sub.add_parser("show")
    show_p.add_argument("--action-file", required=True)
    list_p = sub.add_parser("list")
    list_p.add_argument("--root", required=True)
    list_p.add_argument("--status", choices=sorted(STATUSES))

    args = parser.parse_args()
    try:
        if args.command == "create":
            return create(args)
        if args.command == "approve":
            return approve(args)
        if args.command == "transition":
            return transition(args)
        if args.command == "outcome":
            return outcome(args)
        if args.command == "show":
            return show(args)
        return list_actions(args)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json_dump({"status": "FAIL", "error": str(exc)}), file=sys.stderr, end="")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
