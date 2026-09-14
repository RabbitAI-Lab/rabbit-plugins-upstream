#!/usr/bin/env python3
"""
memory-bench report schema — validate and preview a report before it is published.

submit.sh uploads the report file VERBATIM into a public pull request, so the
preview has to cover the whole file rather than a hand-picked set of fields. A
preview that summarises "retrieval metrics: yes" tells you nothing about what is
actually in retrieval_stats, and a field a future collector adds would ship
unseen. So this module does two things:

  1. Validates the report against the complete schema collect.py produces.
     An unknown key ANYWHERE is a hard refusal, not a note — an unknown key is
     exactly the case where something unreviewed would become public.
  2. Prints every leaf value that would be published, path by path.

Usage:
    python3 report_schema.py <report.json> [--contributor NAME]

Exit 0 if the report is publishable, 1 if not.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from rate import REDACTIONS  # same patterns that guard the external judge

# --- Spec vocabulary ---
#
# A spec is one of:
#   dict            — object with these keys; the key "*" matches any other key
#   ListOf(spec)    — list whose items all match spec
#   Opt(spec)       — the key may be absent
#   OneOf(a, b)     — matches any of the given specs
#   type / tuple    — isinstance check


class ListOf:
    def __init__(self, item):
        self.item = item


class Opt:
    def __init__(self, spec):
        self.spec = spec


class OneOf:
    def __init__(self, *specs):
        self.specs = specs


NUM = (int, float)
NUM_OR_NULL = (int, float, type(None))
# collect.py serialises with default=str, so a non-numeric DB value arrives as a
# string. Allowed here, then caught by the string rules below if it is prose.
COUNT = (int, float, str, type(None))

STATS = {"mean": NUM, "std": NUM, "min": NUM, "max": NUM, "n": int}

BY_CONFIG_ENTRY = {
    "strategy": str,
    "ablation": str,
    "query_count": int,
    "avg_score": Opt(STATS),
    "latency": Opt({"mean": NUM, "p50": NUM, "p95": NUM}),
    "rar": Opt(STATS),
    "mrr": Opt(STATS),
    "ndcg": Opt(STATS),
    "map": Opt(STATS),
    "precision_at_k": Opt(STATS),
    "hit_rate": Opt(STATS),
}

SCHEMA = {
    "schema_version": str,
    "collected_at": str,
    "collection_period_days": int,
    "contributor": str,
    "instance_id": str,
    "system": {
        "os": str,
        "arch": str,
        "python": str,
        "node": (str, type(None)),
    },
    "memory_stats": {
        "memories": {
            "total_active": int,
            "total_deleted": int,
            "type_distribution": {"*": COUNT},
            "age_distribution": {"*": COUNT},
            "strength_histogram": ListOf({"range": str, "count": int}),
            "importance_histogram": ListOf({"range": str, "count": int}),
            "embedding_coverage": NUM,
        },
        "associations": {"total": int, "type_distribution": {"*": COUNT}},
        "hierarchy": {"levels": {"*": COUNT}},
        "consolidation": {
            "recent_runs": ListOf({
                "timestamp": str,
                "processed": COUNT,
                "decayed": COUNT,
                "pruned": COUNT,
                "clusters": COUNT,
                "summaries": COUNT,
            }),
            "total_runs_in_period": int,
        },
        "sharing": {"total_shared": int},
    },
    "retrieval_stats": {
        "available": bool,
        "total_queries": Opt(int),
        "by_config": Opt({"*": BY_CONFIG_ENTRY}),
        "judge_methods": Opt(ListOf(str)),
        "algorithm_versions": Opt(ListOf(str)),
    },
    "token_stats": {
        "available": bool,
        "opted_in": Opt(bool),
        "*": {"total_tokens": NUM, "total_cost_usd": NUM, "sessions": NUM},
    },
    "longitudinal": {
        "prior_reports": int,
        "prior_dates": ListOf(str),
        "meets_minimum": bool,
    },
}

# A publishable report holds labels and numbers. Anything long or multi-line is
# prose, and prose in a stats report is memory content that got through.
MAX_STRING = 120
GITHUB_USER = re.compile(r"^[a-zA-Z0-9_-]+$")
# Timestamps, histogram ranges and version numbers are digits and separators
# only. They cannot be an address, a key or a path, but they DO trip the
# phone-number pattern — and a warning that fires on every single report is a
# warning nobody reads. Length and newline rules still apply to them.
STRUCTURED_SCALAR = re.compile(r"^[\d\s:.,\-+TZ/|]+$")


def _typename(spec):
    if isinstance(spec, tuple):
        return "/".join(t.__name__ for t in spec)
    return getattr(spec, "__name__", str(spec))


def validate(node, spec=SCHEMA, path="", errors=None):
    """Collect every schema violation. Returns the error list."""
    if errors is None:
        errors = []

    if isinstance(spec, Opt):
        return validate(node, spec.spec, path, errors)

    if isinstance(spec, OneOf):
        for s in spec.specs:
            if not validate(node, s, path, []):
                return errors
        errors.append(f"{path}: matches none of the allowed shapes")
        return errors

    if isinstance(spec, ListOf):
        if not isinstance(node, list):
            errors.append(f"{path}: expected a list, got {type(node).__name__}")
            return errors
        for i, item in enumerate(node):
            validate(item, spec.item, f"{path}[{i}]", errors)
        return errors

    if isinstance(spec, dict):
        if not isinstance(node, dict):
            errors.append(f"{path}: expected an object, got {type(node).__name__}")
            return errors
        wildcard = spec.get("*")
        for key, value in node.items():
            sub = f"{path}.{key}" if path else key
            if key in spec and key != "*":
                validate(value, spec[key], sub, errors)
            elif wildcard is not None:
                validate(value, wildcard, sub, errors)
            else:
                errors.append(
                    f"{sub}: unknown field — it would be published unreviewed")
        for key, sub_spec in spec.items():
            if key == "*" or isinstance(sub_spec, Opt):
                continue
            if key not in node:
                errors.append(f"{path}.{key}: required field is missing" if path
                              else f"{key}: required field is missing")
        return errors

    if not isinstance(node, spec):
        errors.append(
            f"{path}: expected {_typename(spec)}, got {type(node).__name__}")
    return errors


def walk(node, path=""):
    """Yield (path, value) for every leaf in the report."""
    if isinstance(node, dict):
        for key, value in node.items():
            yield from walk(value, f"{path}.{key}" if path else key)
    elif isinstance(node, list):
        if not node:
            yield path, []
        for i, item in enumerate(node):
            yield from walk(item, f"{path}[{i}]")
    else:
        yield path, node


def walk_strings(node, path=""):
    """Yield (path, text) for every string that would be published — keys too.

    Keys are yielded as the real object rather than recovered from the path
    string: type_distribution keys come from the database, and one containing
    a dot (an address, a dotted label) would be split across path segments and
    scanned in harmless-looking pieces.
    """
    if isinstance(node, dict):
        for key, value in node.items():
            sub = f"{path}.{key}" if path else key
            yield sub, str(key)
            yield from walk_strings(value, sub)
    elif isinstance(node, list):
        for i, item in enumerate(node):
            yield from walk_strings(item, f"{path}[{i}]")
    elif isinstance(node, str):
        yield path, node


def check_strings(report):
    """Scan every string in the report — keys included. Returns (errors, warnings)."""
    errors, warnings = [], []
    for where, text in walk_strings(report):
        if len(text) > MAX_STRING:
            errors.append(
                f"{where}: string is {len(text)} chars (max {MAX_STRING}) — "
                "reads like content, not a label")
        if "\n" in text:
            errors.append(f"{where}: string contains a newline — reads like content")
        if STRUCTURED_SCALAR.match(text):
            continue
        for pattern, placeholder in REDACTIONS:
            if pattern.search(text):
                warnings.append(
                    f"{where}: looks like {placeholder.strip('[]')} — read this "
                    "field before publishing")
    # The same finding on many fields should read as one line, not a wall.
    return list(dict.fromkeys(errors)), list(dict.fromkeys(warnings))


def check_report(report, contributor=None):
    """Full check. Returns (errors, warnings)."""
    errors = validate(report)
    string_errors, warnings = check_strings(report)
    errors += string_errors

    name = report.get("contributor")
    if isinstance(name, str):
        if not GITHUB_USER.match(name):
            errors.append(f"contributor: '{name}' is not a valid GitHub username")
        if contributor and contributor != name:
            errors.append(
                f"contributor: report says '{name}' but you passed "
                f"'{contributor}' — the PR would attribute it to someone else")
    return errors, warnings


def render_preview(report, report_path, errors, warnings):
    """Print every field that would become public. No summarising."""
    out = []
    out.append("  Every field below is uploaded verbatim if you continue:")
    out.append("")
    n_fields = 0
    for path, value in walk(report):
        rendered = json.dumps(value, ensure_ascii=False, default=str)
        out.append(f"    {path:<58} {rendered}")
        n_fields += 1
    out.append("")
    out.append(f"  {n_fields} fields, validated against the full schema.")
    out.append(f"  Source file: {report_path}")

    if warnings:
        out.append("")
        out.append("  ⚠️  WORTH A SECOND LOOK:")
        for w in warnings:
            out.append(f"     • {w}")
    if errors:
        out.append("")
        out.append("  ❌ SCHEMA ERRORS — refusing to publish:")
        for e in errors:
            out.append(f"     • {e}")
    return "\n".join(out)


def main():
    import argparse
    parser = argparse.ArgumentParser(
        description="Validate and preview a memory-bench report before publishing")
    parser.add_argument("report")
    parser.add_argument("--contributor", default=None)
    args = parser.parse_args()

    try:
        report = json.loads(Path(args.report).read_text())
    except (OSError, json.JSONDecodeError) as e:
        print(f"  ❌ Cannot read report: {e}")
        return 1
    if not isinstance(report, dict):
        print("  ❌ Report is not a JSON object")
        return 1

    errors, warnings = check_report(report, args.contributor)
    print(render_preview(report, args.report, errors, warnings))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
