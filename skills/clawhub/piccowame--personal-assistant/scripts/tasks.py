#!/usr/bin/env python3
"""Task & activity-calendar engine for admin-assistant.

Every task lives on a day of the *activity calendar*. When a pending task is
dragged/dropped (rescheduled) to a later date it is automatically inserted into
that day's activity calendar and a reminder is computed for 6 hours before the
deadline (configurable). Completion is a checkmark state machine:
complete | pending | reschedule.

Commands
--------
  add       "Title" [--due DATE] [--time HH:MM] [--category C] [--priority P]
            [--notes TEXT] [--reminder-hours N] [--no-reminder]
  list      [--date DATE] [--all] [--status S] [--category C] [--json]
  show      ID [--json]
  done      ID            alias: complete
  pending   ID
  reschedule ID --to DATE [--time HH:MM]   alias: drag ID --to DATE
  check     ID --state complete|pending|reschedule [--to DATE] [--time HH:MM]
  today     [--date DATE]
  calendar  [--date DATE] [--write]        regenerate markdown calendar
  reminders [--date DATE] [--all]
  cron-plan [--date DATE]                 ready-to-register one-shot reminders
  report
  delete    ID

Environment: ADMIN_ASSIST_HOME (data dir), ADMIN_ASSIST_TZ (default Asia/Shanghai)
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timedelta

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import (  # noqa: E402
    append_log,
    data_home,
    fail,
    fpath,
    iso,
    load,
    new_id,
    now,
    out,
    parse_date,
    parse_time,
    save,
    today,
)

FILE = "tasks.json"
CATEGORIES = {"admin", "work", "personal", "doc", "health", "meeting", "finance", "travel"}
STATUSES = {"pending", "in_progress", "complete", "cancelled"}
DEFAULT_REMINDER_HOURS = 6


# ------------------------------------------------------------------ storage
def load_tasks() -> list[dict]:
    return load(FILE, [])


def save_tasks(tasks: list[dict]) -> None:
    save(FILE, tasks)


def find(tasks: list[dict], tid: str) -> dict:
    tid = (tid or "").strip().lower()
    exact = [t for t in tasks if t["id"] == tid]
    if exact:
        return exact[0]
    pref = [t for t in tasks if t["id"].startswith(tid)]
    if len(pref) == 1:
        return pref[0]
    if len(pref) > 1:
        fail(f"ambiguous id {tid!r}: {', '.join(t['id'] for t in pref)}")
    fail(f"no task with id {tid!r}")


# ------------------------------------------------------------------ core
def due_dt(task: dict) -> datetime | None:
    if not task.get("due_date"):
        return None
    d = parse_date(task["due_date"])
    t = parse_time(task.get("due_time") or "09:00")
    return datetime.combine(d, t, tzinfo=None).replace(tzinfo=now().tzinfo)


def reminder_dt(task: dict) -> datetime | None:
    dd = due_dt(task)
    if dd is None:
        return None
    hours = task.get("reminder_hours")
    if hours is None:
        return None
    return dd - timedelta(hours=float(hours))


def recompute(task: dict) -> dict:
    """Refresh derived fields (reminder_at, reminder_iso) after edits."""
    rd = reminder_dt(task)
    task["reminder_at"] = iso(rd) if rd else None
    task["updated"] = iso(now())
    return task


def make_task(args) -> dict:
    t = now()
    due_date = None
    due_time = args.time
    if args.due:
        due_date = parse_date(args.due).isoformat()
    if due_date and not due_time:
        due_time = "09:00"
    rem_hours = None if args.no_reminder else (args.reminder_hours or DEFAULT_REMINDER_HOURS)
    task = {
        "id": new_id("tsk", load_tasks()),
        "title": args.title.strip(),
        "category": (args.category or "work").lower(),
        "priority": (args.priority or "P2").upper(),
        "due_date": due_date,
        "due_time": due_time,
        "status": "pending",
        "notes": args.notes or "",
        "reminder_hours": rem_hours,
        "reminder_registered": False,
        "source": args.source if hasattr(args, "source") else "manual",
        "created": iso(t),
        "updated": iso(t),
        "history": [{"at": iso(t), "event": "created"}],
    }
    return recompute(task)


def write_calendar_day(d: str) -> str:
    """Render (and persist) the activity calendar for ISO date d. Returns path."""
    tasks = [t for t in load_tasks() if t.get("due_date") == d and t.get("status") != "cancelled"]
    tasks.sort(key=lambda t: (t.get("due_time") or "99:99", t.get("priority", "P9")))
    day = parse_date(d)
    lines = [
        f"# Activity Calendar — {day.strftime('%A %d %B %Y')}",
        "",
        f"_Generated {iso(now())} · {len(tasks)} scheduled item(s)_",
        "",
        "| Time | Priority | Status | ID | Task | Category | Reminder |",
        "|------|----------|--------|----|------|----------|----------|",
    ]
    for t in tasks:
        rd = reminder_dt(t)
        rem = rd.strftime("%d %b %H:%M") if rd else "—"
        lines.append(
            f"| {t.get('due_time') or 'all-day'} | {t.get('priority','')} | "
            f"{status_mark(t['status'])} {t['status']} | `{t['id']}` | {t['title']} | "
            f"{t.get('category','')} | {rem} |"
        )
    lines += ["", "## Notes", ""]
    any_notes = False
    for t in tasks:
        if t.get("notes"):
            lines.append(f"- **{t['title']}** (`{t['id']}`): {t['notes']}")
            any_notes = True
    if not any_notes:
        lines.append("_No notes for this day._")
    lines.append("")
    p = fpath("calendar", f"{d}.md")
    with open(p, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    return p


def status_mark(status: str) -> str:
    return {"complete": "✅", "pending": "⬜", "in_progress": "🟨", "cancelled": "🚫"}.get(status, "▫️")


# ------------------------------------------------------------------ render
def row(t: dict) -> str:
    due = f"{t['due_date']} {t.get('due_time') or ''}".strip() if t.get("due_date") else "no due date"
    rd = reminder_dt(t)
    rem = f" · ⏰ {rd.strftime('%m-%d %H:%M')}" if rd else ""
    return (
        f"{status_mark(t['status'])} `{t['id']}` [{t.get('priority','')}] "
        f"{t['title']}  —  {t.get('category','')} · due {due}{rem}"
    )


# ------------------------------------------------------------------ commands
def cmd_add(args) -> int:
    tasks = load_tasks()
    task = make_task(args)
    tasks.append(task)
    save_tasks(tasks)
    append_log("task-events.jsonl", {"event": "add", "id": task["id"], "title": task["title"]})
    out(f"✅ Created {task['id']}: {task['title']}")
    if task.get("due_date"):
        out(f"   Due       : {task['due_date']} {task.get('due_time') or ''}".rstrip())
        rd = reminder_dt(task)
        if rd:
            out(f"   Reminder  : {iso(rd)}  (deadline − {task['reminder_hours']}h)")
        out(f"   Calendar  : {write_calendar_day(task['due_date'])}")
    else:
        out("   Reminder  : none (no due date)")
    if args.json:
        out(json.dumps(task, ensure_ascii=False, indent=2))
    return 0


def _filter(tasks, args, date_only=False):
    if date_only and getattr(args, "date", None):
        d = parse_date(args.date).isoformat()
        tasks = [t for t in tasks if t.get("due_date") == d]
    if getattr(args, "status", None):
        tasks = [t for t in tasks if t["status"] == args.status]
    if getattr(args, "category", None):
        tasks = [t for t in tasks if t.get("category") == args.category.lower()]
    return tasks


def cmd_list(args) -> int:
    tasks = load_tasks()
    if not args.all and not getattr(args, "date", None):
        tasks = [t for t in tasks if t["status"] != "complete"]
    tasks = _filter(tasks, args, date_only=True)
    tasks.sort(key=lambda t: (t.get("due_date") or "9999", t.get("due_time") or "99:99"))
    if args.json:
        out(json.dumps(tasks, ensure_ascii=False, indent=2))
        return 0
    if not tasks:
        out("No matching tasks.")
        return 0
    for t in tasks:
        out(row(t))
    out("")
    out(f"{len(tasks)} task(s) · data: {data_home()}")
    return 0


def cmd_show(args) -> int:
    t = find(load_tasks(), args.id)
    if args.json:
        out(json.dumps(t, ensure_ascii=False, indent=2))
        return 0
    rd = reminder_dt(t)
    out(f"Task      : {t['title']}")
    out(f"ID        : {t['id']}")
    out(f"Status    : {status_mark(t['status'])} {t['status']}")
    out(f"Priority  : {t.get('priority')}")
    out(f"Category  : {t.get('category')}")
    out(f"Due       : {(t.get('due_date') or '-') } {t.get('due_time') or ''}".rstrip())
    out(f"Reminder  : {iso(rd) if rd else '-'} (registered={t.get('reminder_registered')})")
    out(f"Notes     : {t.get('notes') or '-'}")
    out(f"Created   : {t.get('created')}   Updated: {t.get('updated')}")
    out("History   :")
    for h in t.get("history", []):
        out(f"  - {h.get('at')}: {h.get('event')}")
    return 0


def _set_state(task: dict, state: str, args) -> None:
    t = now()
    if state == "complete":
        task["status"] = "complete"
        task["completed_at"] = iso(t)
        task["history"].append({"at": iso(t), "event": "checked → complete"})
    elif state == "pending":
        task["status"] = "pending"
        task.pop("completed_at", None)
        task["history"].append({"at": iso(t), "event": "checked → pending"})
    elif state == "reschedule":
        if not getattr(args, "to", None):
            fail("reschedule requires --to DATE")
        old = f"{task.get('due_date')} {task.get('due_time') or ''}".strip()
        task["due_date"] = parse_date(args.to).isoformat()
        if getattr(args, "time", None):
            task["due_time"] = args.time
        elif not task.get("due_time"):
            task["due_time"] = "09:00"
        task["status"] = "pending"
        task["reminder_registered"] = False
        task["rescheduled_from"] = old
        task["history"].append(
            {"at": iso(t), "event": f"dragged/dropped: {old or '-'} → {task['due_date']} {task.get('due_time')}"}
        )
        recompute(task)
        write_calendar_day(task["due_date"])
    elif state in ("in_progress", "cancelled"):
        task["status"] = state
        task["history"].append({"at": iso(t), "event": f"checked → {state}"})


def cmd_state(args) -> int:
    tasks = load_tasks()
    task = find(tasks, args.id)
    _set_state(task, args.state if hasattr(args, "state") else args.cmd, args)
    recompute(task)
    save_tasks(tasks)
    append_log("task-events.jsonl", {"event": f"state:{args.cmd}", "id": task["id"], "status": task["status"]})
    out(f"{status_mark(task['status'])} {task['id']} → {task['status']}")
    if args.state == "reschedule":
        out(f"   New due  : {task['due_date']} {task.get('due_time')}")
        rd = reminder_dt(task)
        if rd:
            out(f"   Reminder : {iso(rd)}  (deadline − {task['reminder_hours']}h)")
            out(f"   Calendar : {write_calendar_day(task['due_date'])}")
            out("   ACTION   : register one-shot reminder with `cron-plan`")
    return 0


def cmd_today(args) -> int:
    d = parse_date(args.date or "today").isoformat()
    p = write_calendar_day(d)
    with open(p, encoding="utf-8") as fh:
        out(fh.read())
    return 0


def cmd_calendar(args) -> int:
    d = parse_date(args.date or "today").isoformat()
    p = write_calendar_day(d)
    out(f"Activity calendar written: {p}")
    return 0


def cmd_reminders(args) -> int:
    tasks = load_tasks()
    rows = []
    for t in tasks:
        rd = reminder_dt(t)
        if rd is None or t["status"] == "complete":
            continue
        rows.append((rd, t))
    if getattr(args, "date", None):
        d = parse_date(args.date).isoformat()
        rows = [(r, t) for r, t in rows if r.date().isoformat() == d]
    rows.sort(key=lambda x: x[0])
    if args.json:
        out(json.dumps(
            [{"id": t["id"], "title": t["title"], "reminder_at": iso(r),
              "due": f"{t.get('due_date')} {t.get('due_time')}",
              "registered": t.get("reminder_registered")} for r, t in rows],
            ensure_ascii=False, indent=2))
        return 0
    if not rows:
        out("No pending reminders.")
        return 0
    for r, t in rows:
        flag = "✔" if t.get("reminder_registered") else " "
        out(f"[{flag}] {iso(r)}  {t['id']}  {t['title']}  (due {t.get('due_date')} {t.get('due_time')})")
    out("")
    out(f"{len(rows)} reminder(s). [✔ = already registered as a cron job]")
    return 0


def cmd_cron_plan(args) -> int:
    tasks = load_tasks()
    rows = []
    cutoff = now() - timedelta(hours=1)
    for t in tasks:
        rd = reminder_dt(t)
        if rd is None or t.get("reminder_registered") or t["status"] == "complete":
            continue
        if rd < cutoff:
            continue
        if getattr(args, "date", None):
            d = parse_date(args.date).isoformat()
            if rd.date().isoformat() != d:
                continue
        rows.append((rd, t))
    rows.sort(key=lambda x: x[0])
    if not rows:
        out("No un-registered reminders to schedule.")
        return 0
    out("# Register each block with the `cron` tool (action=add).")
    for rd, t in rows:
        due = f"{t.get('due_date')} {t.get('due_time')}"
        text = (
            f"⏰ REMINDER (6h before deadline): \"{t['title']}\" is due at {due}. "
            f"Task id {t['id']}. Use the admin-assistant skill to act on it or reschedule."
        )
        out("")
        out(f"--- {t['id']} ---")
        out(json.dumps({
            "name": f"Reminder: {t['title'][:40]}",
            "schedule": {"kind": "at", "at": rd.isoformat(timespec="seconds")},
            "payload": {"kind": "systemEvent", "text": text},
            "sessionTarget": "main",
            "deleteAfterRun": True,
        }, ensure_ascii=False, indent=2))
    out("")
    out("# After registering, run: tasks.py mark-registered ID  (for each id)")
    return 0


def cmd_mark_registered(args) -> int:
    tasks = load_tasks()
    task = find(tasks, args.id)
    task["reminder_registered"] = True
    task["history"].append({"at": iso(now()), "event": "reminder cron registered"})
    save_tasks(tasks)
    out(f"✔ {task['id']} marked as reminder-registered")
    return 0


def cmd_report(_args) -> int:
    tasks = load_tasks()
    by_status: dict[str, int] = {}
    for t in tasks:
        by_status[t["status"]] = by_status.get(t["status"], 0) + 1
    today_d = today().isoformat()
    todays = [t for t in tasks if t.get("due_date") == today_d]
    overdue = [t for t in tasks if t.get("due_date") and t["due_date"] < today_d and t["status"] != "complete"]
    upcoming = sorted(
        [t for t in tasks if t.get("due_date") and t["due_date"] > today_d and t["status"] != "complete"],
        key=lambda t: t["due_date"],
    )[:10]
    out("📊 ADMIN ASSISTANT — TASK REPORT")
    out(f"   Data home : {data_home()}")
    out(f"   Total     : {len(tasks)}")
    for k in sorted(by_status):
        out(f"   {k:<12}: {by_status[k]}")
    out("")
    out(f"📅 Today ({today_d}) — {len(todays)} item(s)")
    for t in todays:
        out("   " + row(t))
    out("")
    out(f"⚠️  Overdue — {len(overdue)} item(s)")
    for t in overdue:
        out("   " + row(t))
    out("")
    out(f"⏭  Upcoming — {len(upcoming)} item(s)")
    for t in upcoming:
        out("   " + row(t))
    return 0


def cmd_delete(args) -> int:
    tasks = load_tasks()
    task = find(tasks, args.id)
    tasks.remove(task)
    save_tasks(tasks)
    out(f"🗑  deleted {task['id']} ({task['title']})")
    return 0


# ------------------------------------------------------------------ parser
def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="tasks.py", description="Task & activity-calendar engine")
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("add", help="create a task")
    a.add_argument("title")
    a.add_argument("--due", help="YYYY-MM-DD | today | tomorrow | +3")
    a.add_argument("--time", help="HH:MM deadline time")
    a.add_argument("--category", default="work", choices=sorted(CATEGORIES))
    a.add_argument("--priority", default="P2", choices=["P1", "P2", "P3"])
    a.add_argument("--notes", default="")
    a.add_argument("--reminder-hours", type=float, default=None)
    a.add_argument("--no-reminder", action="store_true")
    a.add_argument("--json", action="store_true")
    a.set_defaults(func=cmd_add)

    l = sub.add_parser("list", help="list tasks")
    l.add_argument("--date")
    l.add_argument("--all", action="store_true")
    l.add_argument("--status", choices=sorted(STATUSES))
    l.add_argument("--category", choices=sorted(CATEGORIES))
    l.add_argument("--json", action="store_true")
    l.set_defaults(func=cmd_list)

    s = sub.add_parser("show", help="task detail")
    s.add_argument("id")
    s.add_argument("--json", action="store_true")
    s.set_defaults(func=cmd_show)

    for name in ("done", "complete", "pending", "in_progress", "cancelled"):
        c = sub.add_parser(name)
        c.add_argument("id")
        c.set_defaults(func=cmd_state, state={
            "done": "complete", "complete": "complete", "pending": "pending",
            "in_progress": "in_progress", "cancelled": "cancelled"}[name])

    for name in ("reschedule", "drag"):
        r = sub.add_parser(name, help="move task to a new date (drag & drop)")
        r.add_argument("id")
        r.add_argument("--to", required=True)
        r.add_argument("--time")
        r.set_defaults(func=cmd_state, state="reschedule")

    k = sub.add_parser("check", help="checkmark action: complete|pending|reschedule")
    k.add_argument("id")
    k.add_argument("--state", required=True,
                   choices=["complete", "pending", "reschedule", "in_progress", "cancelled"])
    k.add_argument("--to")
    k.add_argument("--time")
    k.set_defaults(func=cmd_state)

    t = sub.add_parser("today", help="print today's activity calendar")
    t.add_argument("--date")
    t.set_defaults(func=cmd_today)

    c = sub.add_parser("calendar", help="regenerate activity calendar markdown")
    c.add_argument("--date")
    c.set_defaults(func=cmd_calendar)

    rm = sub.add_parser("reminders", help="list pending reminders")
    rm.add_argument("--date")
    rm.add_argument("--json", action="store_true")
    rm.set_defaults(func=cmd_reminders)

    cp = sub.add_parser("cron-plan", help="emit cron payloads for un-registered reminders")
    cp.add_argument("--date")
    cp.set_defaults(func=cmd_cron_plan)

    mr = sub.add_parser("mark-registered", help="mark reminder as registered in cron")
    mr.add_argument("id")
    mr.set_defaults(func=cmd_mark_registered)

    sub.add_parser("report", help="status report").set_defaults(func=cmd_report)

    d = sub.add_parser("delete")
    d.add_argument("id")
    d.set_defaults(func=cmd_delete)
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
