#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""mesh_normalize.py - Concept-level condition normalization toward MeSH.

Why (P2): registry condition fields are free text in different languages
("非小细胞肺癌" / "NSCLC" / "Non-Small Cell Lung Cancer"), so cross-source and
cross-skill comparability suffers. The keyword-level term_map (references/
term_map.json) solves search-term translation; THIS tool solves concept-level
aggregation using scripts/mesh_map.json (starter curated map, grows over time).

The tool is honest about coverage: it reports the mapped share and emits the
top unmapped condition terms as suggestions (--emit-suggestions) so the map
can be grown deliberately instead of silently guessing.

Usage:
    python scripts/mesh_normalize.py --in normalized.json [--out-md mesh.md] [--out-json mesh.json]
                                      [--emit-suggestions suggestions.json] [--top 20]
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_MAP = os.path.join(HERE, "mesh_map.json")


def _norm(s):
    return re.sub(r"\s+", " ", str(s).strip().lower())


def load_map(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    # index: normalized label/synonym -> concept
    idx = {}
    for c in data.get("concepts", []):
        terms = [c.get("label_en"), c.get("label_zh")] + list(c.get("synonyms") or [])
        for t in terms:
            if t:
                idx[_norm(t)] = c
    return data, idx


def match(condition, idx):
    """Exact-term match first, then containment (longest key wins)."""
    c = _norm(condition)
    if not c:
        return None
    if c in idx:
        return idx[c]
    hits = [k for k in idx if k and (k in c or c in k)]
    if not hits:
        return None
    best = max(hits, key=len)
    return idx[best]


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
    ap = argparse.ArgumentParser(description="MeSH concept normalization for "
                                             "registry condition terms")
    ap.add_argument("--in", dest="inp", required=True)
    ap.add_argument("--map", default=DEFAULT_MAP, help="mesh_map.json path")
    ap.add_argument("--out-json", default=None)
    ap.add_argument("--out-md", default=None)
    ap.add_argument("--emit-suggestions", default=None,
                    help="write top unmapped condition terms as JSON for map growth")
    ap.add_argument("--top", type=int, default=20)
    args = ap.parse_args(argv)

    data, idx = load_map(args.map)
    recs = load_records(args.inp)

    cond_counter = Counter()          # raw condition term -> count
    mapped_counter = Counter()        # mesh id -> count
    unmapped = Counter()
    for r in recs:
        conds = r.get("conditions")
        if isinstance(conds, str):
            conds = [x.strip() for x in re.split(r"[;；]", conds) if x.strip()]
        for c in conds or []:
            c = str(c).strip()
            if not c:
                continue
            cond_counter[c] += 1
            m = match(c, idx)
            if m:
                mapped_counter[f'{m["mesh_id"]} {m["label_en"]} ({m["label_zh"]})'] += 1
            else:
                unmapped[_norm(c)] += 1

    total = sum(cond_counter.values())
    mapped = sum(mapped_counter.values())
    summary = {"records": len(recs), "condition_terms": total,
               "mapped_terms": mapped,
               "coverage": round(mapped / total, 3) if total else 0.0,
               "map_size": len(idx)}

    payload = {"schema": "ct-registry/mesh_normalize/v0.1.0",
               "summary": summary,
               "mapped": mapped_counter.most_common(),
               "unmapped_top": unmapped.most_common(args.top)}
    if args.out_json:
        with open(args.out_json, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
    if args.emit_suggestions:
        with open(args.emit_suggestions, "w", encoding="utf-8") as f:
            json.dump({"schema": "ct-registry/mesh_map_suggestions/v0.1.0",
                       "note": "candidate condition terms missing from mesh_map.json; "
                               "review and add with authoritative MeSH UIDs only",
                       "candidates": unmapped.most_common(args.top)},
                      f, ensure_ascii=False, indent=2)
    if args.out_md:
        L = ["# MeSH Concept Normalization Report", ""]
        L.append(f"- Condition terms: {total} | mapped: **{mapped}** "
                 f"(coverage {summary['coverage']:.0%}) | map size: {len(idx)} concepts")
        L.append("")
        L.append("## Mapped concepts")
        for k, c in mapped_counter.most_common():
            L.append(f"- {k}: {c}")
        L.append("")
        L.append("## Top unmapped terms (map-growth candidates)")
        for k, c in unmapped.most_common(args.top):
            L.append(f"- {k}: {c}")
        with open(args.out_md, "w", encoding="utf-8") as f:
            f.write("\n".join(L))

    print(json.dumps(summary, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
