#!/usr/bin/env python3
"""Cold Email Writer

Flags US compliance risks in a draft for cold email writer.

Parameters for this build:
{
  "rules": [
    {
      "label": "physical postal address",
      "pattern": "\\b\\d{5}(-\\d{4})?\\b"
    },
    {
      "label": "opt-out mechanism",
      "pattern": "(?i)unsubscribe|opt[ -]?out|remove me|stop receiving"
    },
    {
      "label": "fake reply or forward prefix",
      "pattern": "(?i)^\\s*(re|fwd|fw)\\s*:"
    },
    {
      "label": "guarantee or risk-free claim",
      "pattern": "(?i)guaranteed|risk[- ]free"
    },
    {
      "label": "unsubstantiated superlative",
      "pattern": "(?i)\\bbest\\b|#1\\b|number one|world-class"
    },
    {
      "label": "unearned credential",
      "pattern": "(?i)certified|accredited|award-winning|as seen on"
    }
  ]
}

Usage:
    python3 cold_email_writer.py --input <file> --out <dir>
"""

import argparse
import os
import re
import sys

TITLE = "Cold Email Writer"


def read_flat(path):
    """Read a small YAML-ish file: `key: value`, `- item` lists, '#' comments."""
    data, key = {}, None
    try:
        raw = open(path, encoding="utf-8", errors="replace").read()
    except OSError as exc:
        raise SystemExit(f"cannot read {path}: {exc}")
    for line in raw.splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        stripped = line.strip()
        if stripped.startswith("- "):
            if key is None:
                continue
            data.setdefault(key, [])
            if isinstance(data[key], list):
                data[key].append(stripped[2:].strip().strip('"').strip("'"))
            continue
        if ":" in stripped:
            name, _, value = stripped.partition(":")
            name, value = name.strip(), value.strip().strip('"').strip("'")
            if value == "":
                data[name] = []
                key = name
            else:
                data[name] = value
                key = None
    return data


def read_csv(path):
    import csv
    with open(path, newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle))


def write_out(out_dir, name, lines):
    import os
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, name)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines) + "\n")
    print(f"wrote {path}")
    return path


RULES = [{"label": "physical postal address", "pattern": "\\b\\d{5}(-\\d{4})?\\b"}, {"label": "opt-out mechanism", "pattern": "(?i)unsubscribe|opt[ -]?out|remove me|stop receiving"}, {"label": "fake reply or forward prefix", "pattern": "(?i)^\\s*(re|fwd|fw)\\s*:"}, {"label": "guarantee or risk-free claim", "pattern": "(?i)guaranteed|risk[- ]free"}, {"label": "unsubstantiated superlative", "pattern": "(?i)\\bbest\\b|#1\\b|number one|world-class"}, {"label": "unearned credential", "pattern": "(?i)certified|accredited|award-winning|as seen on"}]


def run(input_path, out_dir):
    text = open(input_path, encoding="utf-8", errors="replace").read()
    lines = text.splitlines()
    report = [f"# {TITLE} compliance check", "", f"source: {input_path}", ""]
    hits = []
    for number, line in enumerate(lines, 1):
        low = line.lower()
        for rule in RULES:
            pattern = str(rule.get("pattern", "")).lower()
            if pattern and pattern in low:
                hits.append((number, rule.get("label", pattern), line.strip()[:120]))
    if hits:
        report.append("## Flags")
        for number, label, snippet in hits:
            report.append(f"- line {number} - {label}: {snippet}")
    else:
        report.append("## No flags")
    report.append("")
    report.append("A flag is a prompt for a human, not a verdict. Fix the wording, then re-run.")
    report.append("")
    report.append("## Guardrails to keep")
    for rule_text in ["Never send the email or connect to a mail server; a rep sends from the company's own mailbox.", "Never use harvested, guessed or bought email addresses, and never guess a personal address from a name pattern.", "Never invent a metric, a customer name or a mutual connection to make the email sound personal."]:
        report.append(f"- {rule_text}")
    write_out(out_dir, "compliance-check.md", report)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--input", required=True, help="input file for this job")
    parser.add_argument("--out", default="./out", help="output directory")
    args = parser.parse_args()
    os.makedirs(args.out, exist_ok=True)
    run(args.input, args.out)


if __name__ == "__main__":
    main()
