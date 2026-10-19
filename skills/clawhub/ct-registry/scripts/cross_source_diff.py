#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cross_source_diff.py - Same-trial cross-registry field consistency check.

Idea transplant (P21 define.xml <-> dataset two-way consistency): once two
registry records are established as THE SAME TRIAL, their registered fields
should agree. Disagreement (status drift, enrollment gap, endpoint change not
synced) is exactly what breaks de-duplication confidence and control-design
benchmarking. ct-registry's aggregate.py already decides "is it the same
trial" (MinHash/LSH + embedded-registry-number bridging); this tool answers
the next question aggregate.py does not touch: "given same-trial groups, which
fields disagree across sources?"

This module is deliberately INDEPENDENT of aggregate.py's clustering: it
re-derives same-trial groups from the normalized.json alone, so it can audit
any snapshot (including ones aggregated long ago).

Grouping strategy (union of both signals):
  1. embedded registry numbers -- scan the record's raw/text fields for
     NCT/ISRCTN/DRKS/EUCTR/ChiCTR ids; any shared id links two records;
  2. fuzzy title -- normalized-title token Jaccard >= --title-jaccard (default
     0.7) AND non-empty condition overlap. Titles alone are risky; the
     condition-overlap guard keeps precision high.

Field diff scope: status, phase, sponsor, enrollment, primary_outcome,
start_date, conditions (Jaccard). Fields that are source-limited (see
docs/registry_record_schema.md) are excluded from the comparison for that
record -- an ISRCTN enrollment=None is N/A, not a contradiction.

Usage:
    python scripts/cross_source_diff.py --in normalized.json [--out-json diff.json] [--out-md diff.md]
                                         [--title-jaccard 0.7] [--min-group 2]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict

_ID_RES = [
    ("NCT", re.compile(r"NCT\d{8}", re.I)),
    ("ISRCTN", re.compile(r"ISRCTN\d+", re.I)),
    ("DRKS", re.compile(r"DRKS\d+", re.I)),
    ("EUCTR", re.compile(r"\b\d{4}-\d{6}-\d{2}\b")),
    ("ChiCTR", re.compile(r"ChiCTR[0-9A-Za-z\-]+")),
]

_DIFF_FIELDS = ["status", "phase", "sponsor", "enrollment",
                "primary_outcome", "start_date"]


def _tok(s):
    if not s:
        return frozenset()
    if isinstance(s, list):
        s = " ".join(str(x) for x in s)
    return frozenset(re.findall(r"[a-z0-9\u4e00-\u9fff]+", str(s).lower()))


def _jaccard(a, b):
    if not a or not b:
        return 0.0
    inter = len(a & b)
    return inter / (len(a) + len(b) - inter)


def _txt(v):
    if v is None:
        return ""
    if isinstance(v, list):
        return "; ".join(str(x).strip() for x in v if str(x).strip())
    return str(v).strip()


def _record_ids(rec):
    """Registry ids referenced anywhere in the record (id field + raw blob)."""
    ids = set()
    rid = _txt(rec.get("registry_id"))
    if rid:
        ids.add(rid.upper())
    blob = rec.get("raw")
    if not isinstance(blob, str):
        blob = json.dumps(rec, ensure_ascii=False)
    for name, rx in _ID_RES:
        for m in rx.findall(blob or ""):
            ids.add(m.upper())
    return ids


def _conditions(rec):
    """Token-level condition set -- string-level sets are too brittle across
    registries ('Non-Small Cell Lung Cancer' vs 'Non-small cell lung carcinoma'
    would never intersect as whole strings)."""
    c = rec.get("conditions")
    if isinstance(c, list):
        return _tok(" ".join(str(x) for x in c))
    return _tok(_txt(c))


def build_groups(recs, title_jaccard):
    """Union-find over embedded ids and fuzzy title+condition matches."""
    parent = list(range(len(recs)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def union(i, j):
        ri, rj = find(i), find(j)
        if ri != rj:
            parent[rj] = ri

    # signal 1: shared embedded registry ids
    by_id = defaultdict(list)
    rec_ids = []
    for i, r in enumerate(recs):
        ids = _record_ids(r)
        rec_ids.append(ids)
        for rid in ids:
            by_id[rid].append(i)
    for idxs in by_id.values():
        for k in idxs[1:]:
            union(idxs[0], k)

    # signal 2: fuzzy title + condition overlap
    toks = [_tok(r.get("title")) for r in recs]
    conds = [_conditions(r) for r in recs]
    for i in range(len(recs)):
        for j in range(i + 1, len(recs)):
            if find(i) == find(j):
                continue
            if not (toks[i] and toks[j]):
                continue
            if _jaccard(toks[i], toks[j]) >= title_jaccard and (conds[i] & conds[j]):
                union(i, j)

    groups = defaultdict(list)
    for i in range(len(recs)):
        groups[find(i)].append(i)
    return [idxs for idxs in groups.values() if len(idxs) >= 2]


def diff_group(recs, idxs):
    """Diff the fields of one same-trial group; skip source-limited fields."""
    members = [recs[i] for i in idxs]
    srcs = sorted({(r.get("source") or "?").upper() for r in members})
    out = {"sources": srcs, "registry_ids": [_txt(r.get("registry_id")) or "?" for r in members],
           "diffs": []}
    for f in _DIFF_FIELDS:
        # exclude only the members whose source path cannot provide the field
        # (docs/registry_record_schema.md); the remaining members are compared
        # as usual -- one limited member must not silence the whole group.
        comparable = [r for r in members
                      if f not in (r.get("source_limited_fields") or [])]
        if len(comparable) < 2:
            continue
        vals = {(_txt(r.get(f)) or "") for r in comparable}
        vals.discard("")
        if len(vals) > 1:
            out["diffs"].append({"field": f,
                                 "values": {(r.get("source") or "?") + ":" + (_txt(r.get("registry_id")) or "?"):
                                            _txt(r.get(f)) or "(empty)"
                                            for r in comparable}})
    conds_avail = [_conditions(r) for r in members if _conditions(r)]
    if len(conds_avail) >= 2:
        jac = _jaccard(conds_avail[0], conds_avail[1])
        if jac < 0.5:
            out["diffs"].append({"field": "conditions(jaccard)",
                                 "values": {"pair_jaccard": round(jac, 2)}})
    out["n_diffs"] = len(out["diffs"])
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description="same-trial cross-source field consistency")
    ap.add_argument("--in", dest="inp", required=True, help="normalized.json path")
    ap.add_argument("--out-json", default=None)
    ap.add_argument("--out-md", default=None)
    ap.add_argument("--title-jaccard", type=float, default=0.7)
    args = ap.parse_args(argv)

    with open(args.inp, encoding="utf-8") as f:
        data = json.load(f)
    recs = data if isinstance(data, list) else next(
        data[k] for k in ("records", "normalized", "trials") if isinstance(data.get(k), list))

    groups = build_groups(recs, args.title_jaccard)
    # keep only genuinely cross-source groups
    cross = []
    for idxs in groups:
        srcs = {(recs[i].get("source") or "?").upper() for i in idxs}
        if len(srcs) >= 2:
            cross.append(diff_group(recs, idxs))
    cross.sort(key=lambda g: -g["n_diffs"])

    inconsistent = [g for g in cross if g["n_diffs"] > 0]
    summary = {"records": len(recs), "cross_source_groups": len(cross),
               "groups_with_field_conflicts": len(inconsistent),
               "total_field_conflicts": sum(g["n_diffs"] for g in cross)}

    payload = {"schema": "ct-registry/cross_source_diff/v1", "input": args.inp,
               "summary": summary, "groups": cross}
    if args.out_json:
        with open(args.out_json, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
    if args.out_md:
        L = ["# Cross-Source Same-Trial Field Consistency Report", ""]
        L.append(f"- Records: {summary['records']} | cross-source groups: "
                 f"{summary['cross_source_groups']} | groups with conflicts: "
                 f"**{summary['groups_with_field_conflicts']}**")
        L.append("")
        for g in cross:
            if not g["n_diffs"]:
                continue
            L.append(f"## {' / '.join(g['registry_ids'])}  ({' + '.join(g['sources'])})")
            for d in g["diffs"]:
                vals = " | ".join(f"{k}: `{v}`" for k, v in d["values"].items())
                L.append(f"- **{d['field']}** — {vals}")
            L.append("")
        with open(args.out_md, "w", encoding="utf-8") as f:
            f.write("\n".join(L))

    print(json.dumps(summary, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
