#!/usr/bin/env python3
"""Batch audit a directory of skills.

Wraps vet.audit_skill over all subdirectories that contain SKILL.md.
Outputs a summary table + per-skill reports.

Usage:
    python3 batch_vet.py path/to/skills/
    python3 batch_vet.py path/to/skills/ --json
    python3 batch_vet.py path/to/skills/ --fail-on high  # exit 1 if any >= HIGH
"""
from __future__ import annotations
import argparse
import json
import sys
from dataclasses import asdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from vet import audit_skill, SEVERITY_LABELS  # noqa: E402
from score import SEVERITY_HIGH, SEVERITY_CRITICAL  # noqa: E402

SCORE_THRESHOLD = {"low": 16, "medium": 41, "high": 71, "critical": 100}


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("dir", help="Directory containing skill subfolders")
    p.add_argument("--json", action="store_true", help="Output JSON")
    p.add_argument("--fail-on", choices=["low", "medium", "high", "critical"],
                   help="Exit 1 if any skill at/above this tier")
    args = p.parse_args(argv)

    root = Path(args.dir).resolve()
    if not root.is_dir():
        print(f"Error: {root} is not a directory", file=sys.stderr)
        return 2

    results = []
    for sub in sorted(root.iterdir()):
        if sub.is_dir() and (sub / "SKILL.md").exists():
            try:
                results.append(audit_skill(sub))
            except Exception as e:
                print(f"Error auditing {sub}: {e}", file=sys.stderr)

    if args.json:
        print(json.dumps([asdict(r) for r in results], indent=2, ensure_ascii=False))
    else:
        print(f"\n📊 Batch Audit: {root}")
        print(f"   {len(results)} skills found\n")
        print(f"{'SKILL':<30} {'SCORE':>6}  {'LEVEL':<12} {'VERDICT'}")
        print("─" * 80)
        for r in results:
            print(f"{r.skill_name[:30]:<30} {r.risk_score:>4}/100  {r.severity_label:<12} {r.verdict}")
        print()

    if args.fail_on:
        threshold = SCORE_THRESHOLD[args.fail_on]
        failed = [r for r in results if r.risk_score >= threshold]
        if failed:
            print(f"❌ {len(failed)} skill(s) reached {args.fail_on} tier:", file=sys.stderr)
            for r in failed:
                print(f"   {r.skill_name}: {r.risk_score}/100", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
