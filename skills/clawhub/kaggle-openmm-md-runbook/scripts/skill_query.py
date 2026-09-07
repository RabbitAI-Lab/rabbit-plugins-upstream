#!/usr/bin/env python3
"""skill_query.py — surgical fact retrieval for the kaggle-openmm-md-runbook skill.

Lets ANY consuming model (120B or 8B) fetch exactly the facts it needs instead of
reading 40 KB of prose: fewer tokens, fewer hallucinations, deterministic grounding.

Usage:
  skill_query.py list traps|rules|errors|params|gates
  skill_query.py trap TRAP-03            (exact ID lookup)
  skill_query.py rule R08                (exact ID lookup)
  skill_query.py error SEARCH_TEXT       (substring match over error patterns)
  skill_query.py param [dotted.key]      (whole params.json or one subtree)
  skill_query.py essence                 (ultra-compact briefing, ~120 lines)
  skill_query.py --json ...              (machine-readable output; default is text)

Exit codes: 0 = ok, 1 = not found, 2 = usage error. Reads only registry/*.json
inside the skill. No network, no writes, stdlib only.
"""
import json
import os
import re
import sys

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = os.path.join(SKILL_DIR, "registry")
VERSION = "1.1.0"

def _load(name):
    with open(os.path.join(REG, name), encoding="utf-8") as fh:
        return json.load(fh)

def _emit(obj, as_json):
    if as_json:
        print(json.dumps(obj, indent=1, ensure_ascii=False))
    elif isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, (dict, list)):
                print(f"{k}:")
                print(json.dumps(v, indent=1, ensure_ascii=False))
            else:
                print(f"{k}: {v}")
    else:
        print(obj if isinstance(obj, str) else json.dumps(obj, ensure_ascii=False))

def _one_line(e, fields):
    parts = [e.get("id", "?")]
    for f in fields:
        v = e.get(f)
        if v:
            parts.append(str(v))
        if len(parts) >= 3:
            break
    return " | ".join(parts)

GATES_BRIEF = [
 ("G01", "run.py identical to run_md.py"), ("G02", "kernel-metadata code_file == run.py"),
 ("G03", "no getState(getKineticEnergy=/getPotentialEnergy=) kwargs (8.3)"),
 ("G04", "restraint force per-stage rebuild pattern"), ("G05", "openmm=8.3.1 pinned"),
 ("G06", "CUDA_ARCH from nvidia-smi"), ("G07", "restraint refs = minimized coords"),
 ("G08", "RECELL shift inside solvate_opc"), ("G09", "XmlSerializer string-return style"),
 ("G10", "ligand.sdf V2000 atom count == 35"), ("G11", "ligand formula == C16H13N3O3"),
 ("G12", "protein Ca2+ HETATM present (chain Z)"), ("G13", "no bare /kaggle/input mounts"),
 ("G14", "no embedded credentials in run.py"), ("G15", "SelDCD constants (AKMA/CORD)"),
 ("G16", "HMR hydrogenMass set when dt=4fs"), ("G17", "amber19/opc.xml water forcefield"),
 ("G18", "removeCMMotion=False in forcefield kwargs"), ("G19", "checkpoint/resume writes present"),
 ("G20", "--accelerator advisory only (GPU is Kaggle-assigned)"),
]

def cmd_list(kind, as_json):
    data = {"traps": _load("traps.json"), "rules": _load("rules.json"),
            "errors": _load("errors.json")}.get(kind)
    if kind == "params":
        return _emit(list(_load("params.json").keys()), as_json) or 0
    if kind == "gates":
        return _emit([{"id": g, "name": n} for g, n in GATES_BRIEF], as_json) or 0
    if data is None:
        return None
    if as_json:
        _emit(data, True)
    else:
        key = {"traps": "title", "rules": "rule", "errors": "pattern"}[kind]
        for e in data:
            print(f"{e['id']} | {e[key]}")
    return 0

def cmd_lookup(kind, ident, as_json):
    fname, kind_plural = {"trap": ("traps.json", "traps"), "rule": ("rules.json", "rules")}[kind]
    raw = ident.upper().strip()
    num = re.sub(r"\D", "", raw)
    for e in _load(fname):
        eid = e["id"].upper()
        if eid == raw or (num and re.sub(r"\D", "", eid).lstrip("0") == num.lstrip("0")):
            _emit(e, as_json)
            return 0
    print(f"not found: {ident} (try: skill_query.py list {kind_plural})", file=sys.stderr)
    return 1

def cmd_error(text, as_json):
    needle = " ".join(text).lower() if isinstance(text, list) else text.lower()
    hits = [e for e in _load("errors.json")
            if needle in e["pattern"].lower() or needle in e["one_line_fix"].lower()]
    if not hits:
        print("no matching error entry — check runbook §10 chronology; if this is a NEW "
              "failure, record it via scripts/learn.py after solving", file=sys.stderr)
        return 1
    if as_json:
        _emit(hits, True)
    else:
        for e in hits:
            print(f"{e['id']} | {e['pattern']}")
            print(f"   fix: {e['one_line_fix']}  [{e['cause']}]")
    return 0

def cmd_param(path, as_json):
    p = _load("params.json")
    if path:
        cur = p
        for part in path[0].split("."):
            if isinstance(cur, dict) and part in cur:
                cur = cur[part]
            else:
                print(f"unknown param path: {path[0]} (top keys: {', '.join(p)})", file=sys.stderr)
                return 1
        _emit(cur, as_json)
    else:
        _emit(p, as_json)
    return 0

def cmd_essence(as_json):
    traps = _load("traps.json"); rules = _load("rules.json"); params = _load("params.json")
    if as_json:
        return _emit({"rules": rules, "traps": [{"id": t["id"], "title": t["title"], "fix": t["fix"]} for t in traps],
                      "budget": params["budget"], "healthy_markers": params["healthy_markers"]}, True) or 0
    print("ESSENCE kaggle-openmm-md-runbook v%s — deterministic facts only; cite IDs when answering." % VERSION)
    print("── NON-NEGOTIABLE RULES ──")
    for r in rules:
        print(f"{r['id']} [{r['severity']}] {r['rule']}  ({r['evidence']})")
    print("── TRAPS (id: title => fix) ──")
    for t in traps:
        print(f"{t['id']}: {t['title']}  =>  {t['fix']}")
    b = params["budget"]
    print("── BUDGET ──")
    print(f"session cap {b['session_wall_cap_h']}h · quota {b['weekly_quota_gpu_h']} GPU-h/wk · "
          f"100ns ~= {b['total_wall_h']}h ~= {b['sessions_needed']} sessions · ckpt every 50 ps")
    hm = params["healthy_markers"]
    print("── HEALTHY MARKERS ──")
    print(" · ".join(f"{k}={v}" for k, v in hm.items()))
    return 0

def main(argv=None):
    a = [x for x in (argv if argv is not None else sys.argv[1:])]
    as_json = "--json" in a
    a = [x for x in a if x != "--json"]
    if not a or a[0] in ("-h", "--help"):
        print(__doc__.strip())
        return 2
    cmd, rest = a[0], a[1:]
    try:
        if cmd == "list" and rest:
            rc = cmd_list(rest[0], as_json)
            if rc is not None:
                return rc
        elif cmd in ("trap", "rule") and rest:
            return cmd_lookup(cmd, rest[0], as_json)
        elif cmd == "error" and rest:
            return cmd_error(rest, as_json)
        elif cmd == "param":
            return cmd_param(rest, as_json)
        elif cmd == "essence":
            return cmd_essence(as_json)
        elif cmd == "version":
            print(VERSION)
            return 0
    except FileNotFoundError as e:
        print(f"registry file missing: {e} — reinstall the skill", file=sys.stderr)
        return 2
    except json.JSONDecodeError as e:
        print(f"registry file corrupt (invalid JSON): {e} — reinstall the skill", file=sys.stderr)
        return 2
    print(__doc__.strip(), file=sys.stderr)
    return 2

if __name__ == "__main__":
    try:
        sys.exit(main())
    except BrokenPipeError:
        # piping into head/grep: exit quietly like a well-behaved CLI
        _devnull = os.open(os.devnull, os.O_WRONLY)
        os.dup2(_devnull, sys.stdout.fileno())
        sys.exit(0)
