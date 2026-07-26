#!/usr/bin/env python3
"""
e2e-delivery session helper — 保证埋点完整性（timestamps / durationMs / phase 状态 / 事件流全都写对）。

Skill 里所有对 ~/.claude/e2e-sessions/<id>.json 的写入都应该走这个脚本，
不要再用 inline python 手工拼 JSON——durationMs / startedAt 那些字段太容易漏写。

用法示例（$SF = session file path，如 ~/.claude/e2e-sessions/951526.json）：

  # 初始化
  python3 session.py init $SF --workitem-id 951526 --workitem-type task \\
    --workitem-title "xxx" --workitem-url "..." --workspace-id 60

  # 阶段
  python3 session.py phase-start $SF prepare
  python3 session.py phase-end   $SF prepare

  # 步骤（自动计算 durationMs）
  python3 session.py step-start $SF prepare get_workitem --action "ee-cli pingcode workitem get 951526"
  python3 session.py step-end   $SF prepare get_workitem --result success

  # 步骤失败
  python3 session.py step-end   $SF verify deploy_to_test --result failure --error "image_tag 不能为空"

  # 人工阻塞（自动计算 waitDurationMs）
  python3 session.py gate-wait   $SF verify deploy_to_test --reason "手动网页部署"
  python3 session.py gate-resume $SF verify deploy_to_test

  # 能力标记
  python3 session.py cap-add $SF --ai get_workitem
  python3 session.py cap-add $SF --human deploy_to_test --cli-missing "ci run 部署参数透传"

  # 结构化字段直接设置
  python3 session.py set $SF --path repo.branch --value feature/xxx
  python3 session.py set $SF --path mr --value '{"iid":388,"url":"...","state":"opened"}' --json

  # 完成
  python3 session.py done $SF

  # 展示当前进度（人类可读）
  python3 session.py show $SF
"""

import argparse
import json
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

TZ = timezone(timedelta(hours=8))
PHASES = ["prepare", "develop", "submit", "verify", "deliver"]


def now_iso():
    return datetime.now(TZ).replace(microsecond=0).isoformat()


def parse_ts(s):
    return datetime.fromisoformat(s)


def load(path):
    return json.loads(Path(path).read_text())


def save(path, data):
    data["updatedAt"] = now_iso()
    Path(path).write_text(json.dumps(data, ensure_ascii=False, indent=2))


def add_event(data, ev_type, phase=None, step=None, **fields):
    ev = {
        "timestamp": now_iso(),
        "type": ev_type,
        "phase": phase,
        "step": step,
        "action": fields.get("action"),
        "result": fields.get("result"),
        "durationMs": fields.get("durationMs"),
        "errorMessage": fields.get("errorMessage"),
        "notes": fields.get("notes"),
    }
    for extra in ("reason", "resumedAt", "waitDurationMs", "request", "response"):
        if extra in fields:
            ev[extra] = fields[extra]
    data["events"].append(ev)
    return ev


def cmd_init(args):
    ts = now_iso()
    session_id = f"e2e-{args.workitem_id}-{datetime.now(TZ).strftime('%Y%m%d-%H%M')}"
    data = {
        "sessionId": session_id,
        "workItem": {
            "id": int(args.workitem_id),
            "type": args.workitem_type,
            "title": args.workitem_title,
            "url": args.workitem_url,
            "workspaceId": int(args.workspace_id) if args.workspace_id else None,
            "createdBySkill": args.created_by_skill,
        },
        "repo": {},
        "status": "in_progress",
        "currentPhase": "prepare",
        "currentStep": None,
        "startedAt": ts,
        "updatedAt": ts,
        "completedAt": None,
        "phases": [
            {"name": p, "status": "pending", "startedAt": None, "completedAt": None, "durationMs": None}
            for p in PHASES
        ],
        "events": [],
        "capabilities": {"aiCompleted": [], "humanRequired": [], "cliMissing": []},
        "mr": None,
        "testSubmission": None,
        "report": {"localPath": None, "redocShortcutId": None, "testReportLocalPath": None, "testReportShortcutId": None},
    }
    Path(args.file).write_text(json.dumps(data, ensure_ascii=False, indent=2))
    print(f"session created: {args.file}")
    print(f"sessionId: {session_id}")


def cmd_phase_start(args):
    data = load(args.file)
    phase = args.phase
    ts = now_iso()
    for p in data["phases"]:
        if p["name"] == phase:
            p["status"] = "in_progress"
            p["startedAt"] = ts
    data["currentPhase"] = phase
    data["currentStep"] = None
    add_event(data, "phase_started", phase=phase)
    save(args.file, data)
    print(f"phase_started: {phase}")


def cmd_phase_end(args):
    data = load(args.file)
    phase = args.phase
    ts = now_iso()
    duration_ms = None
    for p in data["phases"]:
        if p["name"] == phase:
            p["status"] = "completed"
            p["completedAt"] = ts
            if p.get("startedAt"):
                duration_ms = int((parse_ts(ts) - parse_ts(p["startedAt"])).total_seconds() * 1000)
                p["durationMs"] = duration_ms
    add_event(data, "phase_completed", phase=phase, durationMs=duration_ms, result="success")
    save(args.file, data)
    print(f"phase_completed: {phase} ({duration_ms} ms)")


def cmd_step_start(args):
    data = load(args.file)
    data["currentStep"] = args.step
    add_event(data, "step_started", phase=args.phase, step=args.step, action=args.action, notes=args.notes)
    save(args.file, data)
    print(f"step_started: {args.phase}/{args.step}")


def cmd_step_end(args):
    data = load(args.file)
    # 反查最后一条 step_started（相同 phase/step）
    duration_ms = None
    for ev in reversed(data["events"]):
        if ev["type"] == "step_started" and ev["phase"] == args.phase and ev["step"] == args.step:
            duration_ms = int((parse_ts(now_iso()) - parse_ts(ev["timestamp"])).total_seconds() * 1000)
            break
    ev_type = "step_failed" if args.result == "failure" else "step_completed"
    add_event(
        data,
        ev_type,
        phase=args.phase,
        step=args.step,
        action=args.action,
        result=args.result,
        durationMs=duration_ms,
        errorMessage=args.error,
        notes=args.notes,
    )
    save(args.file, data)
    print(f"{ev_type}: {args.phase}/{args.step} ({duration_ms} ms)")


def cmd_gate_wait(args):
    data = load(args.file)
    add_event(data, "human_gate_waiting", phase=args.phase, step=args.step, reason=args.reason, notes=args.notes)
    save(args.file, data)
    print(f"human_gate_waiting: {args.phase}/{args.step}")


def cmd_gate_resume(args):
    data = load(args.file)
    ts = now_iso()
    wait_duration_ms = None
    for ev in reversed(data["events"]):
        if ev["type"] == "human_gate_waiting" and ev["phase"] == args.phase and ev["step"] == args.step:
            wait_duration_ms = int((parse_ts(ts) - parse_ts(ev["timestamp"])).total_seconds() * 1000)
            break
    add_event(
        data,
        "human_gate_resumed",
        phase=args.phase,
        step=args.step,
        resumedAt=ts,
        waitDurationMs=wait_duration_ms,
        notes=args.notes,
    )
    save(args.file, data)
    print(f"human_gate_resumed: {args.phase}/{args.step} (waited {wait_duration_ms} ms)")


def cmd_verification(args):
    data = load(args.file)
    fields = {"request": args.request, "response": args.response, "result": args.result, "notes": args.notes}
    add_event(data, "verification", phase="verify", step="functional_test", action=args.scenario, **fields)
    save(args.file, data)
    print(f"verification: {args.scenario} = {args.result}")


def cmd_cap_add(args):
    data = load(args.file)
    caps = data["capabilities"]
    for k, target in [("ai", "aiCompleted"), ("human", "humanRequired"), ("cli_missing", "cliMissing")]:
        v = getattr(args, k)
        if v and v not in caps[target]:
            caps[target].append(v)
    save(args.file, data)
    print("capabilities updated")


def cmd_cap_remove(args):
    data = load(args.file)
    caps = data["capabilities"]
    for k, target in [("ai", "aiCompleted"), ("human", "humanRequired"), ("cli_missing", "cliMissing")]:
        v = getattr(args, k)
        if v and v in caps[target]:
            caps[target].remove(v)
    save(args.file, data)
    print("capabilities updated")


def cmd_set(args):
    data = load(args.file)
    value = json.loads(args.value) if args.json else args.value
    # 按点分路径设置
    parts = args.path.split(".")
    node = data
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = value
    save(args.file, data)
    print(f"set: {args.path} = {value}")


def cmd_done(args):
    data = load(args.file)
    ts = now_iso()
    data["status"] = "completed"
    data["currentPhase"] = "done"
    data["currentStep"] = None
    data["completedAt"] = ts
    save(args.file, data)
    print(f"session completed at {ts}")


def cmd_show(args):
    data = load(args.file)
    print(f"# session {data['sessionId']}")
    print(f"status: {data['status']}, currentPhase: {data['currentPhase']}, currentStep: {data['currentStep']}")
    wi = data.get("workItem") or {}
    print(f"workItem: #{wi.get('id')} ({wi.get('type')}) {wi.get('title')}")
    print("phases:")
    for p in data["phases"]:
        dur = f" ({p['durationMs']} ms)" if p.get("durationMs") else ""
        print(f"  {p['name']}: {p['status']}{dur}")
    print(f"events: {len(data['events'])}")
    caps = data["capabilities"]
    print(f"aiCompleted: {len(caps['aiCompleted'])} items")
    print(f"humanRequired: {caps['humanRequired']}")
    print(f"cliMissing: {caps['cliMissing']}")


def build_parser():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)

    i = sub.add_parser("init")
    i.add_argument("file")
    i.add_argument("--workitem-id", required=True)
    i.add_argument("--workitem-type", default="task", choices=["task", "bug", "subtask"])
    i.add_argument("--workitem-title", required=True)
    i.add_argument("--workitem-url", required=True)
    i.add_argument("--workspace-id")
    i.add_argument("--created-by-skill", action="store_true")
    i.set_defaults(func=cmd_init)

    for name, fn in [("phase-start", cmd_phase_start), ("phase-end", cmd_phase_end)]:
        x = sub.add_parser(name)
        x.add_argument("file")
        x.add_argument("phase", choices=PHASES)
        x.set_defaults(func=fn)

    ss = sub.add_parser("step-start")
    ss.add_argument("file"); ss.add_argument("phase"); ss.add_argument("step")
    ss.add_argument("--action"); ss.add_argument("--notes")
    ss.set_defaults(func=cmd_step_start)

    se = sub.add_parser("step-end")
    se.add_argument("file"); se.add_argument("phase"); se.add_argument("step")
    se.add_argument("--action")
    se.add_argument("--result", default="success", choices=["success", "failure", "skipped"])
    se.add_argument("--error"); se.add_argument("--notes")
    se.set_defaults(func=cmd_step_end)

    gw = sub.add_parser("gate-wait")
    gw.add_argument("file"); gw.add_argument("phase"); gw.add_argument("step")
    gw.add_argument("--reason", required=True); gw.add_argument("--notes")
    gw.set_defaults(func=cmd_gate_wait)

    gr = sub.add_parser("gate-resume")
    gr.add_argument("file"); gr.add_argument("phase"); gr.add_argument("step")
    gr.add_argument("--notes")
    gr.set_defaults(func=cmd_gate_resume)

    v = sub.add_parser("verification")
    v.add_argument("file"); v.add_argument("scenario")
    v.add_argument("--request", required=True); v.add_argument("--response", required=True)
    v.add_argument("--result", default="success", choices=["success", "failure"])
    v.add_argument("--notes")
    v.set_defaults(func=cmd_verification)

    ca = sub.add_parser("cap-add")
    ca.add_argument("file")
    ca.add_argument("--ai"); ca.add_argument("--human"); ca.add_argument("--cli-missing")
    ca.set_defaults(func=cmd_cap_add)

    cr = sub.add_parser("cap-remove")
    cr.add_argument("file")
    cr.add_argument("--ai"); cr.add_argument("--human"); cr.add_argument("--cli-missing")
    cr.set_defaults(func=cmd_cap_remove)

    st = sub.add_parser("set")
    st.add_argument("file"); st.add_argument("--path", required=True)
    st.add_argument("--value", required=True); st.add_argument("--json", action="store_true")
    st.set_defaults(func=cmd_set)

    d = sub.add_parser("done"); d.add_argument("file"); d.set_defaults(func=cmd_done)
    sh = sub.add_parser("show"); sh.add_argument("file"); sh.set_defaults(func=cmd_show)

    return p


if __name__ == "__main__":
    args = build_parser().parse_args()
    args.func(args)
