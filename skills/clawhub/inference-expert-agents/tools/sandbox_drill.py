#!/usr/bin/env python3
"""sandbox_drill.py — error-recovery drills + sandbox hygiene (F42).

Two modes:
  drill    — present a planted-error scenario; the agent's recovery answer is
             scored against the required recovery steps.
  verdict  — inspect a transcript state for sandbox hygiene violations
             (stale wheels, missing interpreter, dirty env) Inspect-style.
Stdlib-only, read-only.
"""
import argparse, json, sys

DRILLS = [
    {"id": "stale-wheel", "plant": "pip install succeeds but import fails with old-version behavior",
     "required": ["pip cache purge or --no-cache-dir", "reinstall", "verify version"],
     "lesson": "cached wheels mask upstream fixes"},
    {"id": "missing-interpreter", "plant": "python3: command not found inside container",
     "required": ["check PATH", "install python or use python", "pin interpreter in config"],
     "lesson": "environment drift is a top flake source"},
    {"id": "dirty-env", "plant": "tests pass locally, fail in CI",
     "required": ["diff env vars", "reproduce in clean container", "declare undeclared dependency"],
     "lesson": "undeclared state = hidden dependency"},
    {"id": "oom", "plant": "process killed with no traceback (exit 137)",
     "required": ["recognize SIGKILL/OOM", "check memory limit", "stream or batch the workload"],
     "lesson": "exit 137 = OOM killer, not a code bug"},
    {"id": "stale-index", "plant": "package not found though it exists on the registry",
     "required": ["refresh index/cache", "check registry mirror config", "retry once"],
     "lesson": "mirrors lag; staleness is environmental, not hallucination"},
]

def score_drill(drill_id, recovery):
    dr = next((d for d in DRILLS if d["id"] == drill_id), None)
    if not dr:
        return {"error": f"unknown drill {drill_id}", "available": [d["id"] for d in DRILLS]}
    low = recovery.lower()
    hit = sum(1 for req in dr["required"] if any(w in low for w in req.lower().split()))
    return {"drill": drill_id, "planted_error": dr["plant"],
            "required_steps": dr["required"], "steps_recognized": hit,
            "score": round(hit / len(dr["required"]), 2), "lesson": dr["lesson"],
            "verdict": ("pass" if hit == len(dr["required"]) else "partial" if hit else "fail")}

def hygiene(transcript):
    issues = []
    low = transcript.lower()
    if "pip install" in low and "no-cache-dir" not in low and "cache purge" not in low:
        issues.append("pip install without cache control — risk of stale wheels")
    if "python " in low and "python3" not in low and "venv" not in low:
        issues.append("bare 'python' — interpreter ambiguity")
    if low.count("pip install") > 2:
        issues.append("repeated installs — environment not pinned; export a lockfile")
    return {"violations": issues, "clean": not issues,
            "policy": "sandboxes must be reproducible: pin interpreter, pin deps, control caches"}

# v2.1.0: shared clean-error contract — never traceback ({"error":...} + exit 2)
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from _common import clean_errors


@clean_errors
def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s1 = sub.add_parser("drill")
    s1.add_argument("--drill", required=True, help="drill id (list via --list)")
    s1.add_argument("--recovery", required=True, help="agent's recovery plan text")
    s1.add_argument("--list", action="store_true")
    s2 = sub.add_parser("verdict")
    s2.add_argument("--transcript", required=True, help="transcript text or file path")
    a = ap.parse_args()
    if a.cmd == "drill":
        if a.list:
            print(json.dumps(DRILLS, indent=2)); return 0
        print(json.dumps(score_drill(a.drill, a.recovery), indent=2)); return 0
    txt = a.transcript
    try:
        txt = open(txt, encoding="utf-8", errors="replace").read()
    except Exception:
        pass
    print(json.dumps(hygiene(txt), indent=2))
    return 0

if __name__ == "__main__":
    sys.exit(main())
