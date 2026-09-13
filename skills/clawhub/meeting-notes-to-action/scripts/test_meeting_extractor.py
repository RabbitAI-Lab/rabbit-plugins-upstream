#!/usr/bin/env python3
"""Self-test for meeting_extractor.py — date parsing, owner resolution,
action/decision/question extraction, dedup, carryover, renderers."""

import json
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path

SCRIPT = Path(__file__).parent / "meeting_extractor.py"
sys.path.insert(0, str(SCRIPT.parent))
import meeting_extractor as me  # noqa: E402

D = date(2026, 8, 12)  # a Wednesday

SAMPLE = """Weekly product sync
10:01 Sarah: I'll send the revised deck to leadership by Friday.
10:03 Tom: can you review the vendor contract?
We decided to postpone the launch to Q4.
- Action items:
- set up Stripe payment sandbox, assigned to Priya by end of week
- draft the Q3 hiring plan
10:10 Maria: pricing for enterprise tier TBD?
[ ] call the datacenter about cooling
[x] ship the changelog
Follow up: Tom will schedule the pen test next Tuesday.
We discussed the migration. We agreed to freeze schema changes in September.
- Maybe consider a beta cohort?
Question: who owns the runbook?
"""

SAMPLE2 = """Follow-up sync
- ship the changelog (done)
- call the datacenter about cooling
Maria will draft the Q3 hiring plan by 2026-08-20.
"""


def run_on(text, *extra):
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f:
        f.write(text)
        p = Path(f.name)
    r = subprocess.run([sys.executable, str(SCRIPT), str(p),
                        "--meeting-date", "2026-08-12"] + list(extra),
                       capture_output=True, text=True)
    p.unlink()
    return r


def test_dates():
    assert me.parse_date_expr("2026-08-20", D)[0] == "2026-08-20"
    assert me.parse_date_expr("friday", D)[0] == "2026-08-14"
    assert me.parse_date_expr("next tuesday", D)[0] == "2026-08-18"
    assert me.parse_date_expr("next wednesday", D)[0] == "2026-08-19"
    assert me.parse_date_expr("today", D)[0] == "2026-08-12"
    assert me.parse_date_expr("tomorrow", D)[0] == "2026-08-13"
    assert me.parse_date_expr("end of week", D)[0] == "2026-08-14"
    assert me.parse_date_expr("end of month", D)[0] == "2026-08-31"
    assert me.parse_date_expr("in 2 weeks", D)[0] == "2026-08-26"
    assert me.parse_date_expr("08/20/2026", D)[0] == "2026-08-20"
    assert me.parse_date_expr("September 15", D)[0] == "2026-09-15"
    assert me.parse_date_expr("sometime eventually", D)[0] is None
    print("  natural-language dates ... OK")


def test_extract_actions():
    res = me.extract(SAMPLE, D, "sync")
    descs = " || ".join(a["description"] for a in res["actions"])
    owners = {a["owner"] for a in res["actions"]}
    assert any(a["owner"] == "Sarah" and "deck" in a["description"]
               for a in res["actions"]), res["actions"]
    assert any(a["owner"] == "Priya" and "sandbox" in a["description"]
               for a in res["actions"])
    assert any(a["owner"] == "Tom" and "pen test" in a["description"]
               for a in res["actions"])
    assert any(a["owner"] is None and "hiring plan" in a["description"]
               for a in res["actions"])
    assert any("needs owner" in a["flags"] or a["owner"] is None
               for a in res["actions"])
    # unchecked box extracted; checked box routed to completed
    assert any("cooling" in a["description"] for a in res["actions"])
    assert any("changelog" in c for c in res["completed_in_notes"])
    # question-delegation
    tom_q = [a for a in res["actions"] if "vendor contract" in a["description"]]
    assert tom_q and tom_q[0]["owner"] == "Tom" and \
        "confirm acceptance" in tom_q[0]["flags"]
    print("  action extraction ... OK")


def test_extract_decisions_questions():
    res = me.extract(SAMPLE, D, "sync")
    dtxt = " ".join(d["text"] for d in res["decisions"])
    assert "postpone" in dtxt
    assert "freeze schema" in dtxt          # "We agreed to"
    assert "discussed" not in dtxt.lower() or "migration. We agreed" in dtxt
    qtxt = " ".join(q["text"] for q in res["questions"])
    assert "TBD" in qtxt or "enterprise" in qtxt
    assert any("runbook" in q["text"] for q in res["questions"])
    # weak verb statement → low-confidence action; question form → question
    beta = [a for a in res["actions"] if "beta cohort" in a["description"]]
    assert beta and beta[0]["confidence"] <= 0.5, res["actions"]
    q2 = me.extract("Maybe consider a beta cohort?", D, "x")
    assert not [a for a in q2["actions"] if "beta" in a["description"]]
    print("  decisions + questions + weak-verb confidence ... OK")


def test_dedup():
    text = ("Sarah will update the roadmap by Friday.\n"
            "Sarah should update the roadmap by Friday.\n"
            "Someone should update the roadmap soon.\n")
    res = me.extract(text, D, "x")
    assert len(res["actions"]) <= 2, res["actions"]
    print("  deduplication ... OK")


def test_carryover():
    r1 = me.extract(SAMPLE, D, "sync")
    r2 = me.extract(SAMPLE2, date(2026, 8, 19), "sync2")
    carried = me.carryover(r2, r1)
    # changelog was done → closed; cooling still open → carried; hiring plan
    # reappears as new/done?
    caretxt = " ".join(c["description"] for c in carried)
    assert "cooling" in caretxt
    assert "changelog" not in caretxt
    assert all(c["age_meetings"] >= 1 for c in carried)
    print("  carryover ... OK")


def test_cli_outputs():
    with tempfile.TemporaryDirectory() as td:
        jf = Path(td) / "o.json"
        mf = Path(td) / "m.md"
        ef = Path(td) / "e.md"
        r = run_on(SAMPLE, "--title", "Product sync", "--json", str(jf),
                   "--minutes", str(mf), "--email", str(ef))
        assert r.returncode == 0, r.stderr
        assert "MEETING DIGEST" in r.stdout and "ACTION ITEMS" in r.stdout
        data = json.loads(jf.read_text())
        assert data["meeting"]["date"] == "2026-08-12"
        assert any(a["owner"] == "Sarah" for a in data["actions"])
        mins = mf.read_text()
        assert "## Decisions" in mins and "| 1 |" in mins
        email = ef.read_text()
        assert "Subject:" in email and "→ Sarah" in email
        # carryover via CLI
        pf = Path(td) / "prev.json"
        pf.write_text(json.dumps(data))
        r2 = run_on(SAMPLE2, "--previous", str(pf))
        assert r2.returncode == 0 and "CARRYOVER" in r2.stdout
    print("  CLI + JSON + minutes + email ... OK")


if __name__ == "__main__":
    test_dates()
    test_extract_actions()
    test_extract_decisions_questions()
    test_dedup()
    test_carryover()
    test_cli_outputs()
    print("\nALL TESTS PASSED ✅")
