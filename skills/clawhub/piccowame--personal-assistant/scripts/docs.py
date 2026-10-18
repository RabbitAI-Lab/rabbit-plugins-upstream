#!/usr/bin/env python3
"""Document-drafting tracker for admin-assistant.

Every document that has to be drafted/typed/reviewed is registered here with a
type, owner, due date and drafting status:
  idea → draft → review → approved → issued/sent → filed

Commands
--------
  add "Title" [--type T] [--due DATE] [--owner NAME] [--audience X]
      [--notes TEXT] [--priority P] [--source TEXT]
  list [--status S] [--type T] [--all] [--json]
  show ID
  status ID --set STAGE [--notes TEXT]     advance the drafting stage
  due [--days N]                            documents due within N days
  pending                                   not yet issued/sent
  file ID                                   mark as filed (final stage)
  delete ID
  report

Stages: idea | draft | review | approved | issued | sent | filed
Types : memo | letter | email | report | minutes | policy | sop | contract |
        form | notice | presentation | spreadsheet | other
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import timedelta

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import (  # noqa: E402
    append_log, data_home, fail, fpath, iso, load, new_id, now, out,
    parse_date, save, today,
)

FILE = "documents.json"
STAGES = ["idea", "draft", "review", "approved", "issued", "sent", "filed"]
TYPES = ["memo", "letter", "email", "report", "minutes", "policy", "sop",
         "contract", "form", "notice", "presentation", "spreadsheet", "other"]
DONE_STAGES = {"issued", "sent", "filed"}


def load_docs() -> list[dict]:
    return load(FILE, [])


def save_docs(docs: list[dict]) -> None:
    save(FILE, docs)


def find(docs: list[dict], did: str) -> dict:
    did = (did or "").strip().lower()
    exact = [d for d in docs if d["id"] == did]
    if exact:
        return exact[0]
    pref = [d for d in docs if d["id"].startswith(did)]
    if len(pref) == 1:
        return pref[0]
    if len(pref) > 1:
        fail(f"ambiguous id {did!r}: {', '.join(d['id'] for d in pref)}")
    fail(f"no document with id {did!r}")


def stage_icon(stage: str) -> str:
    return {"idea": "💡", "draft": "✏️", "review": "🔍", "approved": "👍",
            "issued": "📤", "sent": "📨", "filed": "🗄️"}.get(stage, "▫️")


def cmd_add(args) -> int:
    docs = load_docs()
    t = now()
    doc = {
        "id": new_id("doc", docs),
        "title": args.title.strip(),
        "type": (args.type or "other").lower(),
        "stage": "idea",
        "owner": args.owner or "",
        "audience": args.audience or "",
        "due_date": parse_date(args.due).isoformat() if args.due else None,
        "priority": (args.priority or "P2").upper(),
        "notes": args.notes or "",
        "source": args.source or "",
        "file_path": None,
        "created": iso(t),
        "updated": iso(t),
        "history": [{"at": iso(t), "event": "registered for drafting (stage=idea)"}],
    }
    docs.append(doc)
    save_docs(docs)
    append_log("doc-events.jsonl", {"event": "add", "id": doc["id"], "title": doc["title"]})
    out(f"📝 Registered {doc['id']}: {doc['title']}")
    out(f"   Type : {doc['type']}   Stage: 💡 idea   Due: {doc['due_date'] or '-'}")
    out("   Next : run `docs.py status <id> --set draft` once drafting starts.")
    return 0


def cmd_list(args) -> int:
    docs = load_docs()
    if not args.all:
        docs = [d for d in docs if d["stage"] not in DONE_STAGES]
    if args.status:
        docs = [d for d in docs if d["stage"] == args.status]
    if args.type:
        docs = [d for d in docs if d["type"] == args.type.lower()]
    docs.sort(key=lambda d: (d.get("due_date") or "9999-99-99", d.get("priority", "P9")))
    if args.json:
        out(json.dumps(docs, ensure_ascii=False, indent=2))
        return 0
    if not docs:
        out("No matching documents.")
        return 0
    for d in docs:
        due = f" · due {d['due_date']}" if d.get("due_date") else ""
        owner = f" · {d['owner']}" if d.get("owner") else ""
        out(f"{stage_icon(d['stage'])} `{d['id']}` [{d.get('priority')}] {d['title']} "
            f"— {d['type']} · {d['stage']}{due}{owner}")
    out(f"\n{len(docs)} document(s) · data: {data_home()}")
    return 0


def cmd_show(args) -> int:
    d = find(load_docs(), args.id)
    if args.json:
        out(json.dumps(d, ensure_ascii=False, indent=2))
        return 0
    out(f"Document : {d['title']}")
    out(f"ID       : {d['id']}")
    out(f"Type     : {d['type']}")
    out(f"Stage    : {stage_icon(d['stage'])} {d['stage']}  (next: "
        f"{STAGES[STAGES.index(d['stage']) + 1] if d['stage'] != STAGES[-1] else '—'})")
    out(f"Owner    : {d.get('owner') or '-'}   Audience: {d.get('audience') or '-'}")
    out(f"Due      : {d.get('due_date') or '-'}   Priority: {d.get('priority')}")
    out(f"Source   : {d.get('source') or '-'}   File: {d.get('file_path') or '-'}")
    out(f"Notes    : {d.get('notes') or '-'}")
    out("History  :")
    for h in d.get("history", []):
        out(f"  - {h.get('at')}: {h.get('event')}")
    return 0


def cmd_status(args) -> int:
    docs = load_docs()
    d = find(docs, args.id)
    stage = args.set.lower()
    if stage not in STAGES:
        fail(f"unknown stage {stage!r}; valid: {', '.join(STAGES)}")
    t = now()
    d["stage"] = stage
    if args.notes:
        d["notes"] = (d.get("notes", "") + f"\n[{t.date()}] {args.notes}").strip()
    d["updated"] = iso(t)
    d["history"].append({"at": iso(t), "event": f"stage → {stage}" + (f" · {args.notes}" if args.notes else "")})
    save_docs(docs)
    append_log("doc-events.jsonl", {"event": "stage", "id": d["id"], "stage": stage})
    out(f"{stage_icon(stage)} {d['id']} → {stage}")
    if stage in ("draft", "review"):
        out("   ACTION: draft/review content — see references/admin-playbook.md for templates.")
    return 0


def cmd_due(args) -> int:
    days = args.days
    cutoff = (today() + timedelta(days=days)).isoformat()
    docs = [d for d in load_docs()
            if d.get("due_date") and d["due_date"] <= cutoff and d["stage"] not in DONE_STAGES]
    docs.sort(key=lambda d: d["due_date"])
    if not docs:
        out(f"No documents due within {days} day(s).")
        return 0
    for d in docs:
        out(f"{stage_icon(d['stage'])} {d['due_date']}  `{d['id']}`  {d['title']}  [{d['stage']}]")
    return 0


def cmd_pending(_args) -> int:
    docs = [d for d in load_docs() if d["stage"] not in DONE_STAGES]
    docs.sort(key=lambda d: (d["stage"], d.get("due_date") or "9999"))
    if not docs:
        out("Nothing pending — all documents issued/filed. 🎉")
        return 0
    for d in docs:
        out(f"{stage_icon(d['stage'])} `{d['id']}` {d['title']} — {d['stage']} (type: {d['type']})")
    out(f"\n{len(docs)} document(s) awaiting completion.")
    return 0


def cmd_file(args) -> int:
    args.set = "filed"
    args.notes = args.notes if hasattr(args, "notes") else None
    return cmd_status(args)


def cmd_delete(args) -> int:
    docs = load_docs()
    d = find(docs, args.id)
    docs.remove(d)
    save_docs(docs)
    out(f"🗑  deleted {d['id']} ({d['title']})")
    return 0


def cmd_report(_args) -> int:
    docs = load_docs()
    counts: dict[str, int] = {}
    for d in docs:
        counts[d["stage"]] = counts.get(d["stage"], 0) + 1
    out("📊 DOCUMENT DRAFTING REPORT")
    out(f"   Data home : {data_home()}")
    out(f"   Total     : {len(docs)}")
    for s in STAGES:
        if s in counts:
            out(f"   {stage_icon(s)} {s:<9}: {counts[s]}")
    out("")
    overdue = [d for d in docs if d.get("due_date") and d["due_date"] < today().isoformat()
               and d["stage"] not in DONE_STAGES]
    out(f"⚠️  Overdue documents: {len(overdue)}")
    for d in overdue:
        out(f"   {d['due_date']}  `{d['id']}`  {d['title']}  [{d['stage']}]")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="docs.py")
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("add")
    a.add_argument("title")
    a.add_argument("--type", choices=TYPES, default="other")
    a.add_argument("--due")
    a.add_argument("--owner")
    a.add_argument("--audience")
    a.add_argument("--notes", default="")
    a.add_argument("--priority", choices=["P1", "P2", "P3"], default="P2")
    a.add_argument("--source", help="where the request came from (email, meeting, chat...)")
    a.set_defaults(func=cmd_add)

    l = sub.add_parser("list")
    l.add_argument("--status", choices=STAGES)
    l.add_argument("--type", choices=TYPES)
    l.add_argument("--all", action="store_true")
    l.add_argument("--json", action="store_true")
    l.set_defaults(func=cmd_list)

    s = sub.add_parser("show")
    s.add_argument("id")
    s.add_argument("--json", action="store_true")
    s.set_defaults(func=cmd_show)

    st = sub.add_parser("status")
    st.add_argument("id")
    st.add_argument("--set", required=True, choices=STAGES)
    st.add_argument("--notes")
    st.set_defaults(func=cmd_status)

    du = sub.add_parser("due")
    du.add_argument("--days", type=int, default=7)
    du.set_defaults(func=cmd_due)

    sub.add_parser("pending").set_defaults(func=cmd_pending)

    f = sub.add_parser("file")
    f.add_argument("id")
    f.add_argument("--notes")
    f.set_defaults(func=cmd_file)

    d = sub.add_parser("delete")
    d.add_argument("id")
    d.set_defaults(func=cmd_delete)

    sub.add_parser("report").set_defaults(func=cmd_report)
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
