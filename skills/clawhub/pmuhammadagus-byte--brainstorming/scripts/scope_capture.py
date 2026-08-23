#!/usr/bin/env python3
"""Capture brainstorming findings into a structured intent/scope summary.

Turns a freeform meeting of the mind into the agreed intent + constraints
that feed writing-plans. Pure input/output, no network, no destructive ops.

Usage (interactive):
  python3 scope_capture.py

Usage (file out):
  python3 scope_capture.py --out memory/brainstorm-oauth.md
"""
import argparse
import sys

SECTIONS = [
    ("Intent (what & why)", "intent", "What outcome do you want, and why?"),
    ("Requirements", "requirements", "Functional needs, constraints, non-negotiables:"),
    ("Options explored", "options", "2-3 approaches considered with trade-offs:"),
    ("In scope", "in_scope", "Explicitly included:"),
    ("Out of scope", "out_scope", "Explicitly excluded:"),
]


def ask(prompt):
    print(f"\n{prompt}")
    print("(type your answer, end with a blank line)")
    lines = []
    while True:
        try:
            line = input("> ")
        except EOFError:
            break
        if line.strip() == "":
            break
        lines.append(line)
    return "\n".join(lines).strip()


def main():
    p = argparse.ArgumentParser(description="Capture a brainstorming summary.")
    p.add_argument("--out", default=None, help="Write summary to this file")
    args = p.parse_args()

    answers = {}
    print("=== Brainstorming capture ===")
    for title, key, prompt in SECTIONS:
        answers[key] = ask(f"[{title}] {prompt}")

    out = ["# Brainstorm Summary", ""]
    for title, key, _ in SECTIONS:
        val = answers[key] or "_not captured_"
        out.append(f"## {title}")
        out.append(val)
        out.append("")

    content = "\n".join(out) + "\n"

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"\nWrote brainstorm summary to {args.out}", file=sys.stderr)
    else:
        sys.stdout.write(content)


if __name__ == "__main__":
    main()
