#!/usr/bin/env python3
"""Meeting Notes → Action extractor.

Deterministic extraction of decisions, action items (owner + deadline +
confidence), and open questions from raw meeting notes or chat-style
transcripts. Supports carryover tracking from a previous meeting's JSON.
Outputs: terminal digest, JSON, Markdown minutes, summary email draft.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, timedelta
from pathlib import Path

# ---------------------------------------------------------------------------
# Normalization
# ---------------------------------------------------------------------------

MONTHS = {m.lower(): i + 1 for i, m in enumerate(
    ["January", "February", "March", "April", "May", "June", "July",
     "August", "September", "October", "November", "December"])}
WEEKDAYS = ["monday", "tuesday", "wednesday", "thursday", "friday",
            "saturday", "sunday"]

ROLE_ALIASES = {"pm": "role:PM", "tl": "role:TechLead", "tech lead": "role:TechLead",
                "design": "role:Design", "designer": "role:Design",
                "legal": "role:Legal", "marketing": "role:Marketing",
                "sales": "role:Sales", "backend": "role:Backend",
                "frontend": "role:Frontend", "devops": "role:DevOps",
                "qa": "role:QA"}

COMMIT_VERBS = re.compile(
    r"\b(will|'ll|shall|should|is going to|are going to|agreed to|"
    r"committed to|needs to|has to)\b", re.I)
WEAK_VERBS = re.compile(r"\b(should probably|consider|think about|maybe)\b", re.I)
DECISION_TRIGGERS = re.compile(
    r"\b(we\s+)?(decided|agreed\s+(on|to)|chose|settled\s+on|going\s+with|"
    r"approved|rejected|green.?light(?:ed)?|sign(?:ed)?\s+off|deferred|"
    r"postponed|cancelled)\b", re.I)
QUESTION_TRIGGERS = re.compile(
    r"\b(TBD|open question|unresolved|we don'?t know|need to figure out)\b|"
    r"\?\s*$", re.I)
DONE_MARKERS = re.compile(
    r"\b(done|sent|shipped|completed|finished|delivered)\b", re.I)

TS_PREFIX = re.compile(r"^(\[?\d{1,2}:\d{2}(?::\d{2})?\]?\s+)")
SPEAKER_PREFIX = re.compile(r"^([A-Z][\w.'-]*(?:\s[A-Z][\w.'-]*){0,2}):\s+")
LIST_BULLET = re.compile(r"^[-*•]\s+(?:\[( |x|X)\]\s+)?|^(\[( |x|X)\]\s+)")

SECTION_HEAD = re.compile(
    r"^(action items?|next steps?|follow.?ups?|todos?|homework)\s*:\s*$", re.I)


# ---------------------------------------------------------------------------
# Date parsing
# ---------------------------------------------------------------------------


def parse_date_expr(expr: str, meeting: date) -> tuple[str | None, str]:
    """Return (iso_date, note) for a natural-language date expression."""
    e = expr.strip().rstrip(".,;").lower()
    iso = lambda d: d.isoformat()

    m = re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", e)
    if m:
        return e, "absolute"
    m = re.fullmatch(r"(\d{1,2})/(\d{1,2})/(\d{4})", e)
    if m:
        return iso(date(int(m.group(3)), int(m.group(1)), int(m.group(2)))), "mdy"
    m = re.fullmatch(r"(\d{1,2})\.(\d{1,2})\.(\d{4})", e)
    if m:
        return iso(date(int(m.group(3)), int(m.group(2)), int(m.group(1)))), "dmy"
    m = re.fullmatch(r"(\w+)\s+(\d{1,2})(?:st|nd|rd|th)?", e)
    if m and m.group(1) in MONTHS:
        try:
            return iso(date(meeting.year, MONTHS[m.group(1)], int(m.group(2)))), "month-day"
        except ValueError:
            pass
    if e in ("today", "eod", "cob", "asap", "a.s.a.p", "urgent"):
        return iso(meeting), "relative-today"
    if e == "tomorrow":
        return iso(meeting + timedelta(days=1)), "relative"
    if e == "next week":
        days_ahead = (7 - meeting.weekday()) % 7 or 7
        return iso(meeting + timedelta(days=days_ahead)), "relative"
    m = re.fullmatch(r"next\s+(" + "|".join(WEEKDAYS) + r")", e)
    if m:
        target = WEEKDAYS.index(m.group(1))
        days = (target - meeting.weekday()) % 7
        if days == 0:
            days = 7
        return iso(meeting + timedelta(days=days)), "next-weekday"
    m = re.fullmatch(r"(?:by\s+)?(" + "|".join(WEEKDAYS) + r")", e)
    if m:
        target = WEEKDAYS.index(m.group(1))
        days = (target - meeting.weekday()) % 7
        return iso(meeting + timedelta(days=days)), "weekday"
    if e in ("end of week", "end of the week", "eow"):
        days = (4 - meeting.weekday()) % 7
        return iso(meeting + timedelta(days=days)), "eow"
    if e in ("end of month", "end of the month"):
        if meeting.month == 12:
            nxt = date(meeting.year + 1, 1, 1)
        else:
            nxt = date(meeting.year, meeting.month + 1, 1)
        return iso(nxt - timedelta(days=1)), "eom"
    if e in ("end of quarter", "end of the quarter"):
        q_end_month = ((meeting.month - 1) // 3) * 3 + 3
        nxt = (date(meeting.year + 1, 1, 1) if q_end_month == 12
               else date(meeting.year, q_end_month + 1, 1))
        return iso(nxt - timedelta(days=1)), "eoq"
    m = re.fullmatch(r"in\s+(\d+)\s*(day|week|month)s?", e)
    if m:
        n, unit = int(m.group(1)), m.group(2)
        d = meeting + timedelta(days=n if unit == "day" else
                                7 * n if unit == "week" else 30 * n)
        return iso(d), "relative-n"
    return None, "unparsed"


DATE_EXTRACTORS = [
    re.compile(r"\b(?:by|due|before|deadline[: ]|deliver(?:ed)?\s+on)\s+"
               r"((?:\d{4}-\d{2}-\d{2})|(?:\d{1,2}[/.]\d{1,2}[/.]\d{4})|"
               r"(?:next\s+\w+)|(?:(?:the\s+)?end\s+of\s+(?:the\s+)?(?:week|month|quarter))|"
               r"(?:in\s+\d+\s+(?:day|week|month)s?)|"
               r"(?:today|tomorrow|next week|EOD|COB|ASAP|a\.s\.a\.p|urgent)|"
               r"(?:\w+\s+\d{1,2}(?:st|nd|rd|th)?)|"
               r"(monday|tuesday|wednesday|thursday|friday|saturday|sunday))\b", re.I),
]


def extract_deadline(text: str, meeting: date):
    for rx in DATE_EXTRACTORS:
        m = rx.search(text)
        if m:
            iso, note = parse_date_expr(m.group(1), meeting)
            return iso, m.group(1), note
    return None, None, None


# ---------------------------------------------------------------------------
# Owner resolution
# ---------------------------------------------------------------------------


def find_owner(clause: str, speaker: str | None,
               delegated: bool = False) -> str | None:
    # @handles
    m = re.search(r"@(\w+)", clause)
    if m:
        return m.group(1)
    # assigned to X
    m = re.search(r"\bassign(?:ed|ment)?\s+to\s+([A-Z][\w.'-]*)", clause)
    if m:
        return m.group(1)
    # Name before commit verb: "Sarah will ..." (anywhere in the clause)
    m = re.search(r"(?:^|[:.;]\s*|\.\s+|!\s+)"
                  r"([A-Z][\w.'-]*(?:\s[A-Z][\w.'-]*)?)\s+"
                  r"(?:'ll|will|shall|should|is going to|are going to|"
                  r"agreed to|committed to|needs to|has to)\b", clause)
    if m:
        name = m.group(1)
        if name.lower() in ("we", "they", "it", "the team", "everyone"):
            return "team"
        return name
    # role alias
    for alias, role in ROLE_ALIASES.items():
        if re.search(rf"\b{re.escape(alias)}\b", clause, re.I):
            return role
    # "I'll" / "I will" with speaker context
    if re.search(r"\b(I'll|I will|I can|I am going to|I'm going to)\b", clause):
        return speaker or "speaker?"
    # delegation/question to the line's speaker: "Tom: can you review ...?"
    if delegated and speaker:
        return speaker
    return None


# ---------------------------------------------------------------------------
# Extraction
# ---------------------------------------------------------------------------


def jaccard(a: str, b: str) -> float:
    stop = {"the", "a", "an", "to", "of", "and", "for", "on", "in", "with",
            "by", "our", "we", "is", "are", "be", "will"}
    ta = {w for w in re.findall(r"\w+", a.lower()) if w not in stop}
    tb = {w for w in re.findall(r"\w+", b.lower()) if w not in stop}
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / len(ta | tb)


def extract(notes: str, meeting: date, title: str = "Meeting") -> dict:
    decisions, actions, questions = [], [], []
    section_mode = False

    for lineno, raw in enumerate(notes.splitlines(), 1):
        line = TS_PREFIX.sub("", raw.rstrip())
        speaker = None
        sp = SPEAKER_PREFIX.match(line)
        if sp:
            speaker = sp.group(1)
            line = line[sp.end():]
        lm = LIST_BULLET.match(line)
        checked = None
        if lm:
            checked = lm.group(1) or lm.group(3)
            line = line[lm.end():]
        stripped = line.strip()
        if not stripped:
            section_mode = False
            continue

        if SECTION_HEAD.match(stripped):
            section_mode = True
            continue
        if stripped.endswith(":") and len(stripped) < 40 and not section_mode:
            continue  # other section header

        in_list = bool(lm) or section_mode
        clauses = re.split(r"(?<=[.!?])\s+", stripped)

        for clause in clauses:
            cl = clause.strip()
            if not cl:
                continue
            is_questionish = bool(QUESTION_TRIGGERS.search(cl)) or cl.endswith("?")

            # decisions
            dm = DECISION_TRIGGERS.search(cl)
            if dm and not is_questionish and not re.search(
                    r"\b(discussed|talked about|debated)\b", cl, re.I):
                decisions.append({"text": cl, "line": lineno})
                continue

            # completed checkboxes → carryover closer markers
            if checked == "x" or (speaker and DONE_MARKERS.search(cl) and
                                  COMMIT_VERBS.search(cl) is None):
                actions.append({"description": cl, "owner": None, "due": None,
                                "due_raw": None, "confidence": 1.0,
                                "flags": ["done"], "source_line": lineno,
                                "duplicates": 0, "done": True})
                continue

            # weak verbs → low confidence action or nothing
            weak = WEAK_VERBS.search(cl)
            committed = COMMIT_VERBS.search(cl) and not \
                re.search(r"\b(won'?t|will not)\b", cl, re.I)

            delegated = re.search(r"\b(can you|could you|please)\b", cl, re.I)
            if committed or (in_list and len(cl) > 8) or delegated or \
                    re.search(r"\bfollow\s?up\b", cl, re.I):
                owner = find_owner(cl, speaker, delegated=bool(delegated))
                due, due_raw, note = extract_deadline(cl, meeting)
                weak = WEAK_VERBS.search(cl)
                conf = 0.95
                flags = []
                if weak:
                    conf, flags = 0.4, ["review: weak commitment wording"]
                elif delegated:
                    conf, flags = 0.6, ["confirm acceptance"]
                elif not owner:
                    flags.append("needs owner")
                elif owner == "speaker?":
                    flags.append("unresolved speaker")
                if due is None and due_raw:
                    flags.append(f"unparsed date: '{due_raw}'")
                if is_questionish and delegated:
                    pass  # keep as question-flagged action
                elif is_questionish and not committed and not lm:
                    # Only demote to a question when the clause has no
                    # bullet/checkbox of its own — a bulleted question
                    # form was written into a list deliberately.
                    questions.append({"text": cl, "line": lineno})
                    continue
                # clean description: strip leading owner+verb
                desc = re.sub(
                    r"^[A-Z][\w.'-]*(?:\s[A-Z][\w.'-]*)?\s+"
                    r"(?:'ll|will|shall|should|is going to|are going to|"
                    r"agreed to|committed to|needs to|has to)\s+", "", cl)
                desc = re.sub(r"^- ", "", desc)
                actions.append({
                    "description": desc if len(desc) > 3 else cl,
                    "owner": owner, "due": due, "due_raw": due_raw,
                    "confidence": conf, "flags": flags,
                    "source_line": lineno, "duplicates": 0})
            elif is_questionish:
                questions.append({"text": cl, "line": lineno})

    # dedup
    merged = []
    for a in actions:
        if a.get("done"):
            merged.append(a)
            continue
        for b in merged:
            if not b.get("done") and jaccard(a["description"], b["description"]) >= 0.8 \
                    and (a["owner"] in (None, b["owner"]) or b["owner"] is None):
                b["duplicates"] += 1
                if a["owner"]:
                    b["owner"] = a["owner"]
                if a["due"] and (not b["due"] or a["due"] < b["due"]):
                    b["due"], b["due_raw"] = a["due"], a["due_raw"]
                b["confidence"] = max(b["confidence"], a["confidence"])
                break
        else:
            merged.append(a)

    return {"meeting": {"title": title, "date": meeting.isoformat()},
            "decisions": decisions,
            "actions": [a for a in merged if not a.get("done")],
            "completed_in_notes": [a["description"] for a in merged if a.get("done")],
            "questions": questions}


# ---------------------------------------------------------------------------
# Carryover
# ---------------------------------------------------------------------------


def carryover(current: dict, previous: dict) -> list[dict]:
    prev_actions = [a for a in previous.get("actions", [])
                    if not a.get("flags") or "done" not in a.get("flags", [])]
    done_texts = current.get("completed_in_notes", []) + \
        [a["description"] for a in current.get("actions", [])
         if "done" in a.get("flags", [])]
    carried = []
    prev_age = previous.get("meeting", {}).get("carry_count", 1)
    for pa in prev_actions:
        if any(jaccard(pa["description"], d) >= 0.7 for d in done_texts):
            continue  # closed
        age = prev_age + 1 if any(jaccard(pa["description"], c["description"]) >= 0.7
                                  for c in previous.get("carryover", [])) else 1
        carried.append({"description": pa["description"], "owner": pa["owner"],
                        "due": pa["due"], "age_meetings": age,
                        "stale": age >= 3,
                        "note": "blocked or dead — decide explicitly" if age >= 3 else ""})
    return carried


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------


def render_digest(res: dict, carried: list) -> str:
    out = []
    a = out.append
    m = res["meeting"]
    a("=" * 60)
    a(f" MEETING DIGEST — {m['title']} ({m['date']})")
    a("=" * 60)
    a(f" Decisions: {len(res['decisions'])}   Actions: {len(res['actions'])}"
      f"   Open questions: {len(res['questions'])}")
    if res["decisions"]:
        a("\n DECISIONS")
        for i, d in enumerate(res["decisions"], 1):
            a(f"  {i}. {d['text']}  (line {d['line']})")
    if res["actions"]:
        a("\n ACTION ITEMS")
        for i, it in enumerate(res["actions"], 1):
            owner = it["owner"] or "—"
            due = it["due"] or (f"'{it['due_raw']}'" if it["due_raw"] else "no date")
            flags = f"  [{'; '.join(it['flags'])}]" if it["flags"] else ""
            dup = f" (+{it['duplicates']} dup)" if it["duplicates"] else ""
            a(f"  {i}. {it['description']}")
            a(f"     owner: {owner}   due: {due}   conf: {it['confidence']:.2f}{dup}{flags}")
    if res["questions"]:
        a("\n OPEN QUESTIONS")
        for q in res["questions"]:
            a(f"  ? {q['text']}  (line {q['line']})")
    if carried:
        a("\n CARRYOVER (unfinished from previous)")
        for c in carried:
            stale = " ⚠ STALE" if c["stale"] else ""
            a(f"  → {c['description']}  [{c['age_meetings']} meeting(s) old]{stale}"
              + (f"  {c['note']}" if c["note"] else ""))
    review = [it for it in res["actions"] if it["confidence"] < 0.6 or it["flags"]]
    if review:
        a(f"\n ⚠ {len(review)} item(s) need human review before distribution.")
    a("=" * 60)
    return "\n".join(out)


def render_minutes(res: dict, carried: list) -> str:
    m = res["meeting"]
    lines = [f"# Minutes — {m['title']}",
             f"**Date:** {m['date']} · **Items:** "
             f"{len(res['actions'])} actions, {len(res['decisions'])} decisions, "
             f"{len(res['questions'])} open questions", ""]
    if res["decisions"]:
        lines.append("## Decisions")
        lines += [f"{i}. {d['text']} (line {d['line']})"
                  for i, d in enumerate(res["decisions"], 1)]
        lines.append("")
    if res["actions"]:
        lines += ["## Action Items",
                  "| # | Action | Owner | Due | Flags |",
                  "|---|--------|-------|-----|-------|"]
        for i, it in enumerate(res["actions"], 1):
            lines.append(f"| {i} | {it['description'][:80]} | "
                         f"{it['owner'] or 'Unassigned'} | "
                         f"{it['due'] or (it['due_raw'] or '—')} | "
                         f"{'; '.join(it['flags']) or '—'} |")
        lines.append("")
    if res["questions"]:
        lines += ["## Open Questions"] + \
                 [f"- {q['text']} (line {q['line']})" for q in res["questions"]] + [""]
    if carried:
        lines += ["## Carryover from previous meeting"] + \
                 [f"- {c['description']} ({c['age_meetings']} meeting(s) old"
                  + (" — STALE, decide" if c["stale"] else "") + ")"
                  for c in carried] + [""]
    return "\n".join(lines)


def render_email(res: dict, carried: list) -> str:
    m = res["meeting"]
    lines = [f"Subject: [{m['title']} {m['date']}] Decisions + your action items",
             "", f"Team — summary from {m['title']} on {m['date']}.", ""]
    if res["decisions"]:
        lines += ["DECISIONS"] + \
                 [f"• {d['text']}" for d in res["decisions"]] + [""]
    by_owner = {}
    for it in res["actions"]:
        by_owner.setdefault(it["owner"] or "Unassigned", []).append(it)
    if by_owner:
        lines.append("YOUR ACTION ITEMS")
        for owner, items in by_owner.items():
            lines.append(f"→ {owner}")
            for i, it in enumerate(items, 1):
                due = f" — by {it['due']}" if it["due"] else ""
                conf = " (please confirm)" if "confirm acceptance" in it["flags"] else ""
                lines.append(f"  {i}. {it['description']}{due}{conf}")
        lines.append("")
    if "Unassigned" in by_owner and len(by_owner) > 1:
        pass
    if res["questions"]:
        lines += ["OPEN QUESTIONS"] + \
                 [f"• {q['text']}" for q in res["questions"]] + [""]
    if carried:
        lines += ["CARRIED OVER (still open from last time)"] + \
                 [f"• {c['description']}" for c in carried] + [""]
    lines += ["Full minutes attached. Reply with corrections within 24h; "
              "otherwise this stands as our record."]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Extract decisions, action items, and questions from "
                    "meeting notes.")
    ap.add_argument("notes", type=Path, help="notes file (txt/md)")
    ap.add_argument("--meeting-date", default=None,
                    help="YYYY-MM-DD (default: today; needed for relative dates)")
    ap.add_argument("--title", default="Meeting")
    ap.add_argument("--previous", type=Path,
                    help="previous meeting JSON for carryover")
    ap.add_argument("--json", type=Path)
    ap.add_argument("--minutes", type=Path)
    ap.add_argument("--email", type=Path)
    args = ap.parse_args()

    meeting = (date.fromisoformat(args.meeting_date)
               if args.meeting_date else date.today())
    notes = args.notes.read_text(encoding="utf-8")
    res = extract(notes, meeting, args.title)

    carried = []
    if args.previous:
        prev = json.loads(args.previous.read_text(encoding="utf-8"))
        carried = carryover(res, prev)
        res["carryover"] = carried

    print(render_digest(res, carried))

    if args.json:
        args.json.write_text(json.dumps(res, indent=2, ensure_ascii=False))
        print(f"\nJSON      → {args.json}")
    if args.minutes:
        args.minutes.write_text(render_minutes(res, carried))
        print(f"Minutes   → {args.minutes}")
    if args.email:
        args.email.write_text(render_email(res, carried))
        print(f"Email     → {args.email}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
