#!/usr/bin/env python3
"""Autonomous admin-operations driver for admin-assistant.

Wraps the admin duty catalog (references/admin-catalog.json) and turns it into
actionable work: daily agendas, category checklists, and a prioritised
autonomous work order that the agent executes without being asked.

Commands
--------
  catalog  [--category ID] [--automation LEVEL] [--cadence C] [--json]
  checklist CATEGORY_ID
  plan     [--date DATE] [--all]          duties due on a given day
  auto     [--dry-run] [--json]           prioritised autonomous work order
  search   KEYWORD
  stats
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import date, datetime, timedelta

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import data_home, fail, fpath, iso, load, now, out, parse_date, today  # noqa: E402

CATALOG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "references", "admin-catalog.json")
QUARTER_MONTHS = {1, 4, 7, 10}


def catalog() -> dict:
    if not os.path.exists(CATALOG_PATH):
        fail(f"catalog not found at {CATALOG_PATH}")
    with open(CATALOG_PATH, encoding="utf-8") as fh:
        return json.load(fh)


def flatten(cat: dict) -> list[dict]:
    rows = []
    for c in cat["categories"]:
        for it in c["items"]:
            rows.append({
                **it,
                "category_id": c["id"],
                "category": c["name"],
                "automation": it.get("automation", c.get("automation", "assisted")),
            })
    return rows


def due_on(item: dict, d: date) -> bool:
    cad = item.get("cadence", "on-demand")
    if cad in ("daily", "continuous"):
        return True
    if cad == "weekly":
        return d.weekday() == 0  # Monday
    if cad == "monthly":
        return d.day == 1
    if cad == "quarterly":
        return d.day == 1 and d.month in QUARTER_MONTHS
    if cad == "annual":
        return d.day == 1 and d.month == 1
    return False  # on-demand


def auto_level(item: dict) -> str:
    return item.get("automation", "assisted")


def cmd_catalog(args) -> int:
    cat = catalog()
    rows = flatten(cat)
    if args.category:
        rows = [r for r in rows if r["category_id"] == args.category]
    if args.automation:
        rows = [r for r in rows if r["automation"] == args.automation]
    if args.cadence:
        rows = [r for r in rows if r.get("cadence") == args.cadence]
    if args.json:
        out(json.dumps(rows, ensure_ascii=False, indent=2))
        return 0
    current = None
    for r in rows:
        if r["category_id"] != current:
            current = r["category_id"]
            out("")
            out(f"## {r['category']}  ({r['category_id']})  [{r['automation']}]")
        icon = {"autonomous": "🤖", "assisted": "🤝", "manual": "🙋"}.get(r["automation"], "▫️")
        out(f"  {icon} `{r['id']}` [{r.get('cadence',''):<10}] {r['title']}")
    out("")
    out(f"{len(rows)} duty(ies) across {len(cat['categories'])} categories · "
        f"🤖 autonomous  🤝 assisted  🙋 manual")
    return 0


def cmd_checklist(args) -> int:
    cat = catalog()
    match = [c for c in cat["categories"] if c["id"] == args.category or c["name"].lower() == args.category.lower()]
    if not match:
        fail(f"unknown category {args.category!r}; try `admin.py catalog`")
    c = match[0]
    out(f"# Checklist — {c['name']}  [{c.get('automation')}]")
    out("")
    for it in c["items"]:
        icon = {"autonomous": "🤖", "assisted": "🤝", "manual": "🙋"}.get(
            it.get("automation", c.get("automation")), "▫️")
        out(f"- [ ] {icon} `{it['id']}` {it['title']}  _(cadence: {it.get('cadence','on-demand')})_")
    out("")
    out(f"Procedure notes: see references/admin-playbook.md → section '{c['name']}'")
    return 0


def cmd_plan(args) -> int:
    d = parse_date(args.date) if args.date else today()
    rows = [r for r in flatten(catalog()) if args.all or due_on(r, d)]
    rows.sort(key=lambda r: (r["category"], r["id"]))
    out(f"# ADMIN AGENDA — {d.strftime('%A %d %B %Y')}")
    out("")
    if not rows:
        out("No scheduled admin duties for this date.")
        return 0
    by_cat: dict[str, list[dict]] = {}
    for r in rows:
        by_cat.setdefault(r["category"], []).append(r)
    for name, items in by_cat.items():
        out(f"## {name}")
        for it in items:
            icon = {"autonomous": "🤖", "assisted": "🤝", "manual": "🙋"}.get(it["automation"], "▫️")
            out(f"- [ ] {icon} `{it['id']}` {it['title']}")
        out("")
    auto = sum(1 for r in rows if r["automation"] == "autonomous")
    out(f"{len(rows)} duty(ies) · {auto} can be executed autonomously by the agent")
    return 0


def _task_pipeline() -> list[tuple[int, str]]:
    items: list[tuple[int, str]] = []
    tasks = load("tasks.json", [])
    docs = load("documents.json", [])
    tdy = today().isoformat()
    overdue = [t for t in tasks if t.get("due_date") and t["due_date"] < tdy and t["status"] != "complete"]
    for t in sorted(overdue, key=lambda x: x["due_date"]):
        items.append((100, f"OVERDUE task `{t['id']}` {t['title']} (due {t['due_date']}) — act or reschedule"))
    due_today = [t for t in tasks if t.get("due_date") == tdy and t["status"] not in ("complete", "cancelled")]
    for t in due_today:
        items.append((80, f"DUE TODAY `{t['id']}` {t['title']} at {t.get('due_time') or 'all-day'}"))
    unreg = [t for t in tasks if t.get("reminder_at") and not t.get("reminder_registered")
             and t["status"] != "complete"
             and t["reminder_at"] >= iso(now() - timedelta(hours=1))]
    for t in unreg:
        items.append((70, f"Register 6h-prior reminder for `{t['id']}` (fire at {t['reminder_at']})"))
    stuck = [d for d in docs if d.get("stage") in ("idea", "draft", "review")
             and d.get("updated", "")[:10] < (today() - timedelta(days=2)).isoformat()]
    for d in stuck:
        items.append((60, f"Document `{d['id']}` {d['title']} stuck in '{d['stage']}' for >2 days"))
    due_docs = [d for d in docs if d.get("due_date") and d["due_date"] <= (today() + timedelta(days=3)).isoformat()
                and d["stage"] not in ("issued", "sent", "filed")]
    for d in due_docs:
        items.append((75, f"Document `{d['id']}` {d['title']} due {d['due_date']} (stage {d['stage']})"))
    return items


def cmd_auto(args) -> int:
    work = _task_pipeline()
    # scheduled admin duties for today that the agent can run autonomously
    for r in flatten(catalog()):
        if due_on(r, today()) and r["automation"] == "autonomous":
            work.append((50, f"Autonomous duty `{r['id']}` {r['title']} ({r['category']})"))
    work.sort(key=lambda x: -x[0])
    if args.json:
        out(json.dumps([{"priority": p, "action": a} for p, a in work], ensure_ascii=False, indent=2))
        return 0
    out("🤖 AUTONOMOUS ADMIN WORK ORDER")
    out(f"   Generated {iso(now())}   Data: {data_home()}")
    out("")
    if not work:
        out("✅ Nothing pending. All admin work is under control.")
        return 0
    for i, (p, a) in enumerate(work, 1):
        tag = "🔴" if p >= 80 else "🟠" if p >= 60 else "🟢"
        out(f"{i:>3}. {tag} [{p:>3}] {a}")
    out("")
    out(f"{len(work)} action(s). Execute top-down; anything requiring human approval is 'assisted' — draft it and ask.")
    if args.dry_run:
        out("(dry-run: no files changed)")
    return 0


def cmd_search(args) -> int:
    kw = args.keyword.lower()
    hits = [r for r in flatten(catalog()) if kw in r["title"].lower() or kw in r["category"].lower()
            or kw in r["id"].lower()]
    if not hits:
        out(f"No admin duty matches {args.keyword!r}.")
        return 0
    for r in hits:
        out(f"  `{r['id']}` [{r['automation']}/{r.get('cadence')}] {r['title']}  — {r['category']}")
    return 0


def cmd_stats(_args) -> int:
    cat = catalog()
    rows = flatten(cat)
    levels: dict[str, int] = {}
    cadences: dict[str, int] = {}
    for r in rows:
        levels[r["automation"]] = levels.get(r["automation"], 0) + 1
        cadences[r.get("cadence", "on-demand")] = cadences.get(r.get("cadence", "on-demand"), 0) + 1
    out("📊 ADMIN DUTY CATALOG STATS")
    out(f"   Categories : {len(cat['categories'])}")
    out(f"   Duties     : {len(rows)}")
    out("   Automation :")
    for k, v in sorted(levels.items()):
        pct = 100 * v / len(rows)
        out(f"      {k:<12}: {v:>3}  ({pct:.0f}%)")
    out("   Cadence    :")
    for k, v in sorted(cadences.items(), key=lambda x: -x[1]):
        out(f"      {k:<12}: {v:>3}")
    auto = levels.get("autonomous", 0)
    out("")
    out(f"   → {auto}/{len(rows)} duties ({100*auto/len(rows):.0f}%) can be executed autonomously.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="admin.py")
    sub = p.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("catalog")
    c.add_argument("--category")
    c.add_argument("--automation", choices=["autonomous", "assisted", "manual"])
    c.add_argument("--cadence")
    c.add_argument("--json", action="store_true")
    c.set_defaults(func=cmd_catalog)

    k = sub.add_parser("checklist")
    k.add_argument("category")
    k.set_defaults(func=cmd_checklist)

    pl = sub.add_parser("plan")
    pl.add_argument("--date")
    pl.add_argument("--all", action="store_true")
    pl.set_defaults(func=cmd_plan)

    a = sub.add_parser("auto")
    a.add_argument("--dry-run", action="store_true")
    a.add_argument("--json", action="store_true")
    a.set_defaults(func=cmd_auto)

    s = sub.add_parser("search")
    s.add_argument("keyword")
    s.set_defaults(func=cmd_search)

    sub.add_parser("stats").set_defaults(func=cmd_stats)
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
