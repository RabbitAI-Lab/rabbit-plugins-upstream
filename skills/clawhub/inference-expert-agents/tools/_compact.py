#!/usr/bin/env python3
"""_compact.py — token-efficient JSON re-encoder (v2.1, v2.2 keys mode).

Every tool in this skill prints human-fluent JSON (indent 2). When a MACHINE is
the consumer, pipe through this to strip whitespace (~15-25% fewer tokens):

    python3 tools/inference_scorecard.py ... | python3 tools/_compact.py

--keys goes further: dict keys become k0, k1, ... under a "__compact__" header
(deeper cut for big payloads); --expand restores the original losslessly.
"""
import argparse
import json
import sys

HEADER = "__compact__"


def _collect(node, freq):
    if isinstance(node, dict):
        for k, v in node.items():
            freq[k] = freq.get(k, 0) + 1
            _collect(v, freq)
    elif isinstance(node, list):
        for v in node:
            _collect(v, freq)


def compact_keys(doc):
    freq = {}
    _collect(doc, freq)
    keys = sorted(freq, key=lambda k: (-freq[k], k))
    fwd = {k: f"k{i}" for i, k in enumerate(keys)}

    def walk(o):
        if isinstance(o, dict):
            return {fwd[k]: walk(v) for k, v in o.items()}
        if isinstance(o, list):
            return [walk(v) for v in o]
        return o

    return {HEADER: {"v": 1, "keys": keys}, "data": walk(doc)}


def expand_keys(doc):
    if not isinstance(doc, dict) or HEADER not in doc:
        raise ValueError("not a --keys document (missing __compact__ header)")
    keys = doc[HEADER].get("keys") if isinstance(doc[HEADER], dict) else None
    if not isinstance(keys, list):
        raise ValueError("compacted header malformed (keys not a list)")
    rev = {f"k{i}": k for i, k in enumerate(keys)}

    def walk(o):
        if isinstance(o, dict):
            return {rev.get(k, k): walk(v) for k, v in o.items()}
        if isinstance(o, list):
            return [walk(v) for v in o]
        return o

    return walk(doc.get("data"))


def main(argv=None):
    ap = argparse.ArgumentParser(prog="_compact.py")
    ap.add_argument("--keys", action="store_true",
                    help="short-key header map mode (deeper cut; restore with --expand)")
    ap.add_argument("--expand", action="store_true", help="restore a --keys document")
    a = ap.parse_args(argv)
    try:
        obj = json.load(sys.stdin)
    except Exception as e:
        print(json.dumps({"error": f"invalid JSON on stdin: {e}"}))
        return 2
    try:
        out = expand_keys(obj) if a.expand else (compact_keys(obj) if a.keys else obj)
    except (ValueError, RecursionError) as e:
        print(json.dumps({"error": f"transform failed: {e}"}))
        return 2
    print(json.dumps(out, separators=(",", ":"), ensure_ascii=False))
    return 0

if __name__ == "__main__":
    sys.exit(main())
