#!/usr/bin/env python3
"""Flag common AI-slop and punctuation patterns in prose drafts.

This is a warning tool, not a quality oracle. It reports phrase-level and
structural signals. Use --strict to fail on high-severity findings or a no-em-
dash violation.
"""

from __future__ import annotations

import argparse
import re
import statistics
from pathlib import Path
from typing import Iterable

PATTERNS: list[tuple[str, str, str]] = [
    (r"\bin today['’]s (?:fast-paced|rapidly changing|ever-changing|digital|world)\b", "high", "generic opening"),
    (r"\b(?:rapidly|ever)[ -]evolving landscape\b", "high", "generic trend framing"),
    (r"\bnavigate (?:this|the) (?:complex )?landscape\b", "medium", "canned trend language"),
    (r"\bdelve(?:s|d|ing)?\b", "medium", "canned AI vocabulary"),
    (r"\bgame[- ]changer\b", "medium", "unsupported hype"),
    (r"\bparadigm shift\b", "medium", "unsupported grand claim"),
    (r"\btransformative\b", "low", "verify the named transformation"),
    (r"\bunlock(?:s|ed|ing)?\b", "low", "vague promise"),
    (r"\bseamless(?:ly)?\b", "low", "unnamed quality claim"),
    (r"\brobust\b", "low", "unnamed quality claim"),
    (r"\bat its core\b", "medium", "canned transition"),
    (r"\bit is (?:important|worth) to note\b", "medium", "canned transition"),
    (r"\bthe future is (?:here|now)\b", "high", "unearned futurism"),
    (r"\bwhether you(?:'re| are) (?:a )?(?:beginner|seasoned|expert)\b", "high", "generic audience address"),
    (r"\bthis is not just (?:about|a|an)\b", "medium", "synthetic profundity"),
    (r"\bmore than just\b", "medium", "synthetic profundity"),
    (r"\b(?:everyone|no one|nobody|always|never|inevitable|inevitably)\b", "low", "absolute claim; verify or qualify"),
    (r"\bthe industry (?:agrees|knows|is demanding|has realized)\b", "high", "invented consensus"),
    (r"\b(?:best[- ]in[- ]class|market[- ]leading|industry[- ]leading)\b", "medium", "promotional superiority claim; require evidence"),
    (r"\btrusted by (?:thousands|millions|teams|developers|companies)\b", "medium", "promotional social-proof claim; source or remove"),
    (r"\bcutting[- ]edge\b", "medium", "generic marketing claim"),
    (r"\brevolutionary\b", "medium", "generic marketing claim"),
    (r"\b(?:the|a) leading (?:platform|solution|provider|tool)\b", "medium", "vendor-positioning language"),
    (r"\bdevelopers (?:want|need|demand|hate|love)\b", "low", "broad audience claim; add evidence or scope"),
    (r"\bleverage\b", "low", "check for vague business usage"),
    (r"\bin conclusion\b", "medium", "mechanical conclusion"),
    (r"\bthe possibilities are endless\b", "high", "empty inspirational claim"),
    (r"\bembrace (?:the|this) (?:change|future|shift)\b", "high", "generic motivational ending"),
    (r"\bthe choice is ours\b", "high", "generic motivational ending"),
]

NOT_BUT = re.compile(r"\bnot\s+[^.!?;:]{1,100}\s+but\s+", re.IGNORECASE)
HEADING = re.compile(r"^#{1,6}\s+")
BULLET = re.compile(r"^\s*(?:[-*+] |\d+[.)] )")
EM_DASH = "\u2014"


def iter_findings(lines: list[str]) -> Iterable[tuple[int, str, str, str]]:
    for number, line in enumerate(lines, start=1):
        for pattern, severity, label in PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                yield number, severity, label, line.strip()
        if NOT_BUT.search(line):
            yield number, "low", "not-X-but-Y construction; ensure the contrast is earned", line.strip()
        if EM_DASH in line:
            count = line.count(EM_DASH)
            yield number, "low", f"em dash usage ({count}); check style and repetition", line.strip()


def paragraph_word_counts(text: str) -> list[int]:
    paragraphs = [
        p.strip()
        for p in re.split(r"\n\s*\n", text)
        if p.strip() and not p.lstrip().startswith("#") and not BULLET.match(p)
    ]
    return [len(re.findall(r"\b[\w'’-]+\b", p)) for p in paragraphs]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("draft", type=Path, help="Markdown or text draft to inspect")
    parser.add_argument("--strict", action="store_true", help="Exit 1 for high-severity findings")
    parser.add_argument("--no-em-dash", action="store_true", help="Treat any em dash as an error")
    args = parser.parse_args()

    try:
        text = args.draft.read_text(encoding="utf-8")
    except OSError as exc:
        parser.error(str(exc))

    lines = text.splitlines()
    findings = list(iter_findings(lines))
    words = re.findall(r"\b[\w'’-]+\b", text)
    headings = sum(bool(HEADING.match(line)) for line in lines)
    bullets = sum(bool(BULLET.match(line)) for line in lines)
    counts = paragraph_word_counts(text)
    em_dash_count = text.count(EM_DASH)
    double_hyphen_count = len(re.findall(r"\s--\s", text))

    print(f"Draft: {args.draft}")
    print(
        f"Words: {len(words)} | Paragraphs: {len(counts)} | Headings: {headings} | "
        f"Bullets: {bullets} | Em dashes: {em_dash_count} | Spaced --: {double_hyphen_count}"
    )

    structural: list[tuple[str, str]] = []
    if words and headings > max(6, len(words) // 180):
        structural.append(("medium", "many headings for the draft length; check for fragmented content-shape"))
    if words and bullets > max(8, len(words) // 12):
        structural.append(("medium", "bullet-heavy draft; check whether examples or prose should carry the argument"))
    if len(counts) >= 6 and statistics.pstdev(counts) < 6:
        structural.append(("low", "paragraph lengths are unusually uniform; inspect for synthetic cadence"))
    if double_hyphen_count:
        structural.append(("medium", "spaced double hyphens may be em-dash substitutes"))

    for severity, message in structural:
        print(f"[{severity}] structural: {message}")

    if not findings:
        print(
            "No phrase-level slop warnings found. This does not verify originality, information gain, "
            "audience value, factual support, argument, voice, or ending."
        )
    else:
        for line_number, severity, label, excerpt in findings:
            clipped = excerpt if len(excerpt) <= 180 else excerpt[:177] + "..."
            print(f"[{severity}] line {line_number}: {label}: {clipped}")

    severity_counts = {
        level: sum(1 for _, severity, _, _ in findings if severity == level)
        for level in ("high", "medium", "low")
    }
    print(
        f"Findings: high={severity_counts['high']} medium={severity_counts['medium']} "
        f"low={severity_counts['low']}"
    )

    failed = args.strict and severity_counts["high"] > 0
    if args.no_em_dash and (em_dash_count > 0 or double_hyphen_count > 0):
        print("ERROR: no-em-dash mode failed")
        failed = True
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
