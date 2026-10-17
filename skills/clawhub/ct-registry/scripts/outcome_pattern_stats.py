#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""outcome_pattern_stats.py - Primary-outcome pattern statistics.

Purpose (P2, feeds ct-protocol): aggregate WHAT primary endpoints trials in an
indication actually register, so endpoint selection for a new protocol is
evidence-based instead of habit-based. CT.gov Miner offers the same idea for
eligibility/outcome patterns; this tool covers the primary-outcome slice over
ct-registry's own normalized.json.

Buckets (keyword-driven, deliberately coarse -- the goal is a frequency
landscape, not a semantic classifier):
  OS / PFS-EFS-DFS / response(ORR/CR/PR) / safety-tolerability / PK-PD /
  biomarker-pathology / PRO-QoL / event-count-recur / other

Usage:
    python scripts/outcome_pattern_stats.py --in normalized.json [--out-md stats.md] [--out-json stats.json]
                                             [--top 15] [--by-condition "nsclc"]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict

_BUCKETS = [
    ("OS", r"overall survival|总生存|\bOS\b"),
    ("PFS/EFS/DFS", r"progression[- ]free|event[- ]free|disease[- ]free|无进展|无事件|无病生存"),
    ("Response", r"objective response|\bORR\b|complete response|partial response|缓解率|客观缓解|完全缓解"),
    ("Safety/Tolerability", r"adverse|safety|tolerab|安全性|不良事件|耐受"),
    ("PK/PD", r"pharmacokineti|\bAUC\b|Cmax|药代|药动"),
    ("Biomarker/Pathology", r"biomarker|patholog|分子|病理|生物标志"),
    ("PRO/QoL", r"quality of life|\bQoL\b|patient[- ]reported|生活质量|量表"),
    ("Event/Recurrence", r"recurrence|relapse|event rate|复发|事件发生率"),
]


def _bucket(text):
    low = str(text).lower()
    for name, pat in _BUCKETS:
        if re.search(pat, low, re.I):
            return name
    return "Other"


def _txt(v):
    if isinstance(v, list):
        return "; ".join(str(x).strip() for x in v if str(x).strip())
    return str(v).strip() if v else ""


def load_records(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, list):
        return data
    for k in ("records", "normalized", "trials"):
        if isinstance(data.get(k), list):
            return data[k]
    raise SystemExit(f"unrecognized normalized.json shape: {type(data)}")


def main(argv=None):
    ap = argparse.ArgumentParser(description="primary-outcome pattern statistics")
    ap.add_argument("--in", dest="inp", required=True)
    ap.add_argument("--out-json", default=None)
    ap.add_argument("--out-md", default=None)
    ap.add_argument("--top", type=int, default=15)
    ap.add_argument("--condition", default=None,
                    help="only records whose conditions contain this substring (case-insens)")
    args = ap.parse_args(argv)

    recs = load_records(args.inp)
    if args.condition:
        recs = [r for r in recs
                if args.condition.lower() in json.dumps(r.get("conditions", []), ensure_ascii=False).lower()]

    have, lack, limited = 0, 0, 0
    buckets = Counter()
    raw_texts = Counter()
    by_source = defaultdict(Counter)
    examples = defaultdict(list)
    for r in recs:
        po = _txt(r.get("primary_outcome"))
        if not po:
            if "primary_outcome" in (r.get("source_limited_fields") or []):
                limited += 1
            else:
                lack += 1
            continue
        have += 1
        src = (r.get("source") or "?").upper()
        b = _bucket(po)
        buckets[b] += 1
        by_source[src][b] += 1
        raw_texts[po] += 1
        if len(examples[b]) < 5:
            examples[b].append(f"[{src}] {_txt(r.get('registry_id'))}: {po[:110]}")

    summary = {"records_scoped": len(recs), "with_primary_outcome": have,
               "empty_not_limited": lack, "empty_source_limited": limited,
               "buckets": dict(buckets.most_common())}

    if args.out_json:
        with open(args.out_json, "w", encoding="utf-8") as f:
            json.dump({"schema": "ct-registry/outcome_pattern_stats/v1",
                       "summary": summary,
                       "top_raw": raw_texts.most_common(args.top),
                       "by_source": {k: dict(v) for k, v in by_source.items()},
                       "examples": dict(examples)},
                      f, ensure_ascii=False, indent=2)

    if args.out_md:
        L = ["# Primary-Outcome Pattern Statistics", ""]
        L.append(f"- Scoped records: {len(recs)} | with primary outcome: **{have}** "
                 f"(empty-not-limited {lack}, source-limited {limited})")
        L.append("")
        L.append("## Bucket distribution")
        L.append("")
        L.append("| Bucket | Count | Share |")
        L.append("|---|---|---|")
        for b, c in buckets.most_common():
            L.append(f"| {b} | {c} | {c / max(have, 1):.0%} |")
        L.append("")
        L.append("## Most frequent raw primary outcomes")
        L.append("")
        for t, c in raw_texts.most_common(args.top):
            L.append(f"- ({c}x) {t[:150]}")
        L.append("")
        L.append("## Examples per bucket")
        for b, exs in examples.items():
            L.append(f"### {b}")
            for e in exs:
                L.append(f"- {e}")
            L.append("")
        if args.out_md:
            with open(args.out_md, "w", encoding="utf-8") as f:
                f.write("\n".join(L))

    print(json.dumps(summary, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
