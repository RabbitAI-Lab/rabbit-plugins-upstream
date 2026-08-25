#!/usr/bin/env python3
"""Create and append an auditable, client-scoped run record."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


STATUSES = {
    "created", "intake", "data_blocked", "analyzing", "draft_diagnosis",
    "ready_for_review", "approved", "executed", "verified", "failed",
}
RUN_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{2,80}$")


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def safe_run_id(value: str) -> str:
    if not RUN_ID_RE.fullmatch(value):
        raise ValueError("run_id 只能包含字母、数字、点、下划线和短横线")
    return value


def write_json(path: Path, payload: dict) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def load_record(run_dir: Path) -> dict:
    path = run_dir / "run.json"
    if not path.is_file():
        raise ValueError(f"运行记录不存在: {path}")
    return json.loads(path.read_text(encoding="utf-8-sig"))


def init_run(args: argparse.Namespace) -> int:
    run_id = safe_run_id(args.run_id)
    root = Path(args.root).resolve()
    run_dir = root / run_id
    if run_dir.exists():
        raise ValueError(f"运行目录已存在，不覆盖旧记录: {run_dir}")
    root.mkdir(parents=True, exist_ok=True)
    for name in ("inputs", "outputs", "evidence", "approvals", "artifacts"):
        (run_dir / name).mkdir(parents=True, exist_ok=False)
    record = {
        "schema_version": "1.0",
        "run_id": run_id,
        "client_scope": args.client_scope,
        "package_version": args.package_version,
        "created_at": now(),
        "updated_at": now(),
        "status": "created",
        "paths": {
            "inputs": "inputs",
            "outputs": "outputs",
            "evidence": "evidence",
            "approvals": "approvals",
            "artifacts": "artifacts",
            "events": "events.jsonl",
        },
        "input_manifest": [],
        "artifact_refs": [],
        "approval_refs": [],
        "action_refs": [],
        "outcome_refs": [],
        "report_refs": [],
        "connector_call_refs": [],
        "readback_refs": [],
        "model_route_refs": [],
    }
    write_json(run_dir / "run.json", record)
    (run_dir / "events.jsonl").write_text(json.dumps({"at": now(), "type": "run_created", "status": "created"}, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PASS", "run_dir": str(run_dir), "run_id": run_id}, ensure_ascii=False, indent=2))
    return 0


def append_event(args: argparse.Namespace) -> int:
    run_dir = Path(args.run_dir).resolve()
    record = load_record(run_dir)
    event = {"at": now(), "type": args.type, "stage": args.stage, "actor": args.actor, "status": args.status}
    if args.details:
        event["details"] = json.loads(args.details)
    with (run_dir / "events.jsonl").open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, ensure_ascii=False) + "\n")
    record["updated_at"] = event["at"]
    write_json(run_dir / "run.json", record)
    print(json.dumps({"status": "PASS", "event": event}, ensure_ascii=False, indent=2))
    return 0


def set_status(args: argparse.Namespace) -> int:
    if args.status not in STATUSES:
        raise ValueError(f"非法状态: {args.status}")
    run_dir = Path(args.run_dir).resolve()
    record = load_record(run_dir)
    old = record.get("status")
    record["status"] = args.status
    record["updated_at"] = now()
    write_json(run_dir / "run.json", record)
    with (run_dir / "events.jsonl").open("a", encoding="utf-8") as handle:
        handle.write(json.dumps({"at": record["updated_at"], "type": "status_changed", "from": old, "to": args.status}, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "PASS", "from": old, "to": args.status}, ensure_ascii=False, indent=2))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="创建和维护 omni-ecom 运行账本")
    sub = parser.add_subparsers(dest="command", required=True)
    init = sub.add_parser("init")
    init.add_argument("--root", required=True)
    init.add_argument("--run-id", required=True)
    init.add_argument("--client-scope", required=True)
    init.add_argument("--package-version", required=True)
    event = sub.add_parser("event")
    event.add_argument("--run-dir", required=True)
    event.add_argument("--type", required=True)
    event.add_argument("--stage", required=True)
    event.add_argument("--actor", required=True)
    event.add_argument("--status", required=True)
    event.add_argument("--details")
    status = sub.add_parser("status")
    status.add_argument("--run-dir", required=True)
    status.add_argument("--status", required=True)
    show = sub.add_parser("show")
    show.add_argument("--run-dir", required=True)
    args = parser.parse_args()
    try:
        if args.command == "init":
            return init_run(args)
        if args.command == "event":
            return append_event(args)
        if args.command == "status":
            return set_status(args)
        print(json.dumps(load_record(Path(args.run_dir).resolve()), ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
