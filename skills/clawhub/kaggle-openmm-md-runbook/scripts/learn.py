#!/usr/bin/env python3
"""learn.py — schema-validated, append-only lesson log for the skill (safe self-improvement).

Design (human-in-the-loop):
  * Agents may APPEND new lessons discovered while debugging (symptom/fix/confidence).
  * Nothing may edit or delete existing entries — the log is append-only.
  * confidence=verified requires --human-approved (an explicit human confirmation).
  * Entries are promoted into registry/traps.json or registry/errors.json ONLY by a
    human at publish time (new skill version) — never automatically.

Usage:
  learn.py add --symptom "..." --fix "..." [--cause "..."] \
               [--confidence hypothesis|observed|verified] [--source "who"] [--human-approved]
  learn.py list [--json]
  learn.py verify                 (re-validate every logged line; exit 1 if any broken)
  learn.py export                 (promotion-ready JSON array for human review)
  learn.py --selftest             (fixture run inside a temp skill copy)
Exit codes: 0 ok, 1 validation/not-found, 2 usage, 3 selftest failure.
"""
import argparse
import datetime
import re
import json
import os
import shutil
import subprocess
import sys
import tempfile

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG = os.path.join(SKILL_DIR, "registry", "lessons.jsonl")
SCHEMA = os.path.join(SKILL_DIR, "registry", "lessons.schema.json")
CONF = ("hypothesis", "observed", "verified")

def _schema():
    with open(SCHEMA, encoding="utf-8") as fh:
        return json.load(fh)

def _entries(path=LOG):
    """Return [(lineno, entry_dict_or_None)]. A corrupt (non-JSON) line yields
    (lineno, None) instead of crashing, so `verify` can REPORT it."""
    out = []
    if not os.path.isfile(path):
        return out
    with open(path, encoding="utf-8") as fh:
        for i, ln in enumerate(fh, 1):
            ln = ln.strip()
            if not ln:
                continue
            try:
                out.append((i, json.loads(ln)))
            except json.JSONDecodeError:
                out.append((i, None))
    return out

def _next_id(entries):
    """Next LSN-#### = max numeric suffix + 1 (robust against corrupt lines)."""
    hi = 0
    for _, e in entries:
        if isinstance(e, dict):
            m = re.fullmatch(r"LSN-(\d+)", str(e.get("id", "")))
            if m:
                hi = max(hi, int(m.group(1)))
    return f"LSN-{hi + 1:04d}"

def _validate(e, schema, idx, seen_ids):
    errs = []
    for k in schema["required"]:
        if k not in e or e[k] is None or not str(e[k]).strip():
            errs.append(f"missing required field: {k}")
    if "id" in e:
        if not (isinstance(e["id"], str) and e["id"].startswith("LSN-")):
            errs.append(f"id must look like LSN-#### (got {e['id']!r})")
        elif e["id"] in seen_ids:
            errs.append(f"duplicate id {e['id']}")
        else:
            seen_ids.add(e["id"])
    if "confidence" in e and e["confidence"] not in schema["confidence_enum"]:
        errs.append(f"confidence must be one of {schema['confidence_enum']}")
    extra = [k for k in e if k not in schema["required"] + schema["optional"]]
    if extra:
        errs.append(f"unknown fields: {extra}")
    if idx is not None and isinstance(e.get("confidence"), str):
        pass
    return errs

def cmd_add(a, schema):
    conf = a.confidence
    if conf == "verified" and not a.human_approved:
        print("refused: confidence=verified requires --human-approved (human-in-the-loop)",
              file=sys.stderr)
        return 1
    existing = _entries()
    e = {
        "id": _next_id(existing),
        "date": datetime.date.today().isoformat(),
        "symptom": a.symptom.strip(),
        "fix": a.fix.strip(),
    }
    if a.cause:
        e["root_cause"] = a.cause.strip()
    if a.source:
        e["source"] = a.source.strip()
    e["confidence"] = conf
    errs = _validate(e, schema, None, {x["id"] for _, x in existing if isinstance(x, dict)})
    if errs:
        print("validation failed:", "; ".join(errs), file=sys.stderr)
        return 1
    with open(LOG, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(e, ensure_ascii=False) + "\n")
    print(f"appended {e['id']} (confidence={conf}). Promotion to traps.json/errors.json "
          "happens only via a human publish — see SKILL.md 'Self-improvement loop'.")
    return 0

def cmd_list(a, schema):
    es = _entries()
    if a.json:
        print(json.dumps([e for _, e in es], indent=1, ensure_ascii=False))
    else:
        for i, e in es:
            if e is None:
                print(f"line {i}: <corrupt line, not JSON> — run: learn.py verify")
                continue
            print(f"{e['id']} [{e.get('confidence','hypothesis')}] {e['date']} | {e['symptom']}")
            print(f"   fix: {e['fix']}")
        if not es:
            print("(no lessons logged yet)")
    return 0

def cmd_verify(a, schema):
    es = _entries()
    bad = 0
    seen = set()
    for i, e in es:
        if e is None:
            bad += 1
            print(f"line {i}: INVALID — not valid JSON")
            continue
        errs = _validate(e, schema, i, seen)
        if errs:
            bad += 1
            print(f"line {i}: INVALID — {'; '.join(errs)}")
    print(f"verify: {len(es)} entries, {bad} invalid")
    return 1 if bad else 0

def cmd_export(a, schema):
    es = [e for _, e in _entries()]
    print(json.dumps({"review": "promote only after human verification",
                      "suggested_target": {"traps": "registry/traps.json", "errors": "registry/errors.json"},
                      "lessons": es}, indent=1, ensure_ascii=False))
    return 0

def selftest():
    tmp = tempfile.mkdtemp(prefix="learn_selftest_")
    try:
        shutil.copytree(os.path.join(SKILL_DIR, "registry"), os.path.join(tmp, "registry"))
        env = dict(os.environ)
        # point the script at the temp skill by faking __file__ location via copy
        tscripts = os.path.join(tmp, "scripts")
        os.makedirs(tscripts, exist_ok=True)
        shutil.copy(os.path.abspath(__file__), tscripts)
        script = os.path.join(tscripts, os.path.basename(__file__))
        def run(*args):
            return subprocess.run([sys.executable, script, *args],
                                  capture_output=True, text=True)
        r1 = run("add", "--symptom", "NaN after swapping water to TIP3P",
                 "--fix", "use amber19/opc.xml per this kernel family", "--source", "selftest")
        assert r1.returncode == 0 and "LSN-0001" in r1.stdout, r1.stdout + r1.stderr
        r2 = run("add", "--symptom", "x", "--fix", "y", "--confidence", "verified")
        assert r2.returncode == 1 and "human-approved" in r2.stderr, r2.stdout + r2.stderr
        r3 = run("verify")
        assert r3.returncode == 0, r3.stdout + r3.stderr
        # corrupt one line -> verify must fail and add must refuse nothing (append only)
        log = os.path.join(tmp, "registry", "lessons.jsonl")
        with open(log, "a") as fh:
            fh.write('{"id":"LSN-0001","date":"x"}\n')   # duplicate + missing fields
        r4 = run("verify")
        assert r4.returncode == 1, r4.stdout + r4.stderr
        # non-JSON garbage line -> verify must REPORT it (not crash), add must survive it
        with open(log, "w", encoding="utf-8") as fh:
            fh.write('{"id":"LSN-0001","date":"d","symptom":"s","fix":"f"}\n{garbage\n')
        r4b = run("verify")
        assert r4b.returncode == 1 and "not valid JSON" in r4b.stdout, r4b.stdout + r4b.stderr
        r4c = run("add", "--symptom", "s2", "--fix", "f2")
        assert r4c.returncode == 0 and "LSN-0002" in r4c.stdout, r4c.stdout + r4c.stderr
        r4d = run("list")
        assert r4d.returncode == 0 and "corrupt line" in r4d.stdout, r4d.stdout + r4d.stderr
        r5 = run("export", )
        assert r5.returncode == 0 and "suggested_target" in r5.stdout, r5.stdout
        print("LEARN SELFTEST OK (add/validate/human-gate/verify/export)")
        return 0
    except AssertionError as e:
        print(f"LEARN SELFTEST FAIL: {e}", file=sys.stderr)
        return 3
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

def main(argv=None):
    ap = argparse.ArgumentParser(description="Append-only lesson log for the skill")
    ap.add_argument("--selftest", action="store_true")
    sub = ap.add_subparsers(dest="cmd")
    addp = sub.add_parser("add")
    addp.add_argument("--symptom", required=True)
    addp.add_argument("--fix", required=True)
    addp.add_argument("--cause", default="")
    addp.add_argument("--confidence", default="hypothesis", choices=CONF)
    addp.add_argument("--source", default="")
    addp.add_argument("--human-approved", action="store_true")
    lp = sub.add_parser("list"); lp.add_argument("--json", action="store_true")
    sub.add_parser("verify")
    sub.add_parser("export")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    schema = _schema()
    if a.cmd == "add":
        return cmd_add(a, schema)
    if a.cmd == "list":
        return cmd_list(a, schema)
    if a.cmd == "verify":
        return cmd_verify(a, schema)
    if a.cmd == "export":
        return cmd_export(a, schema)
    ap.print_help()
    return 2

if __name__ == "__main__":
    sys.exit(main())
