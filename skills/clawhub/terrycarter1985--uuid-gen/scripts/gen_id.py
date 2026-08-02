#!/usr/bin/env python3
"""Generate one or more UUIDs (v4) or short base36 IDs.

Usage:
    gen_id.py                     # one UUID v4
    gen_id.py --count 5           # five UUID v4s
    gen_id.py --short             # one 10-char base36 id
    gen_id.py --short --length 16 # one 16-char base36 id
"""
import argparse, secrets, string, sys, uuid

ALPHABET = string.ascii_lowercase + string.digits  # base36-ish

def short_id(length: int) -> str:
    return "".join(secrets.choice(ALPHABET) for _ in range(length))

def main() -> int:
    p = argparse.ArgumentParser(description="Generate UUIDs or short random IDs")
    p.add_argument("--count", type=int, default=1, help="number of IDs to generate")
    p.add_argument("--short", action="store_true", help="generate short base36 id instead of UUID")
    p.add_argument("--length", type=int, default=10, help="length for --short ids (default 10)")
    args = p.parse_args()

    for _ in range(args.count):
        if args.short:
            print(short_id(args.length))
        else:
            print(uuid.uuid4())
    return 0

if __name__ == "__main__":
    sys.exit(main())
