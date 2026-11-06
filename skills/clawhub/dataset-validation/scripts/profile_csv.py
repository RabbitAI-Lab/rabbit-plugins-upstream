#!/usr/bin/env python3
"""Read-only structural CSV profile. This does not establish factual validity."""
import argparse
import collections
import csv
import hashlib
import json
from pathlib import Path

def profile(path, keys=(), required=()):
    path = Path(path)
    raw = path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    text = raw.decode("utf-8-sig")
    import io
    reader = csv.reader(io.StringIO(text, newline=""), strict=True)
    try:
        headers = next(reader)
    except StopIteration:
        raise ValueError("empty file")
    if not headers or any(not h.strip() for h in headers):
        raise ValueError("empty column name")
    if len(headers) != len(set(headers)):
        raise ValueError("duplicate column name")
    unknown = (set(keys) | set(required)) - set(headers)
    if unknown:
        raise ValueError("columns absent: " + ", ".join(sorted(unknown)))
    rows = []
    for values in reader:
        if not values:
            continue
        if len(values) != len(headers):
            raise ValueError(f"record {len(rows)+1}: expected {len(headers)} fields, found {len(values)}")
        rows.append(dict(zip(headers, values)))
    groups = collections.defaultdict(list)
    exact = collections.defaultdict(list)
    missing_keys = []
    for number, row in enumerate(rows, 1):
        exact[tuple(row[h] for h in headers)].append(number)
        if keys:
            values = tuple(row[k] for k in keys)
            if any(not v.strip() for v in values):
                missing_keys.append(number)
            else:
                groups[values].append(number)
    return {
        "file": path.name, "sha256": digest, "record_count": len(rows),
        "columns": headers,
        "blank_counts": {h: sum(not r[h].strip() for r in rows) for h in headers},
        "required_blank_records": {h: [i for i,r in enumerate(rows,1) if not r[h].strip()] for h in required},
        "key": list(keys), "missing_key_records": missing_keys,
        "duplicate_key_groups": [{"key": list(k), "records": v} for k,v in groups.items() if len(v)>1],
        "exact_duplicate_groups": [v for v in exact.values() if len(v)>1],
        "limits": "Structural profile only. Original strings preserved; no semantic, source-truth or population-coverage validation."
    }

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file")
    parser.add_argument("--key", nargs="+", default=[])
    parser.add_argument("--required", nargs="+", default=[])
    args = parser.parse_args()
    try:
        result = profile(args.csv_file, args.key, args.required)
    except (OSError, UnicodeError, ValueError, csv.Error) as exc:
        parser.exit(2, str(exc)+"\n")
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()

