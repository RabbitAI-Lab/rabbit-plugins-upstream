#!/usr/bin/env python3
"""record_run.py — build (and optionally append) a self-improvement run record.

DEFAULT: prints one validated JSONL record to stdout and writes NOTHING —
the operator/agent decides what to do with it. Only with an explicit --out FILE
does this script append (append-only: never overwrites, deletes, or truncates;
creates the file only at the path the operator gave).

exit 0 = record built/recorded · exit 1 = input error
"""
import argparse
import datetime
import hashlib
import json
import os
import sys


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--brief-hash", required=True, help="sha256 prefix (>=8 hex) of the brief text")
    ap.add_argument("--iterations", type=int, required=True, choices=[1, 2, 3])
    ap.add_argument("--guardian", required=True, choices=["PASS", "FAIL"])
    ap.add_argument("--critic", default="", help="one-line most valuable critic fix")
    ap.add_argument("--pack", help="path to the final prompt pack JSON")
    ap.add_argument("--rating", type=int, choices=[1, 2, 3, 4, 5], help="operator rating if given")
    ap.add_argument("--out", help="explicit opt-in: append the record to this JSONL file")
    args = ap.parse_args()

    rec = {
        "ts": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "brief_hash": args.brief_hash[:16],
        "iterations": args.iterations,
        "guardian": args.guardian,
        "critic_note": args.critic[:200],
    }
    if args.rating:
        rec["operator_rating"] = args.rating
    if args.pack:
        try:
            with open(args.pack, "r", encoding="utf-8") as fh:
                rec["final_pack"] = json.load(fh)
        except Exception as e:
            print(json.dumps({"recorded": False, "error": f"cannot read pack: {e}"}))
            sys.exit(1)
    blob = json.dumps(rec, sort_keys=True)
    rec["run_id"] = hashlib.sha256(blob.encode()).hexdigest()[:12]

    line = json.dumps(rec)
    if not args.out:
        print(line)  # stdout only — no file written
        print(json.dumps({"recorded": False, "stdout_only": True, "run_id": rec["run_id"],
                          "note": "pass --out FILE to append (opt-in)"}), file=sys.stderr)
        sys.exit(0)
    path = os.path.abspath(args.out)
    parent = os.path.dirname(path)
    if not os.path.isdir(parent):
        print(json.dumps({"recorded": False, "error": f"directory does not exist: {parent}"}))
        sys.exit(1)
    if os.path.isdir(path):
        print(json.dumps({"recorded": False, "error": "out path is a directory"}))
        sys.exit(1)
    with open(path, "a", encoding="utf-8") as fh:  # append-only, never truncates
        fh.write(line + "\n")
    with open(path, "r", encoding="utf-8") as fh:
        n = sum(1 for l in fh if l.strip())
    print(json.dumps({"recorded": True, "run_id": rec["run_id"], "file": path, "total_runs": n}))


if __name__ == "__main__":
    main()
