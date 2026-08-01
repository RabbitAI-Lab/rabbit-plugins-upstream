---
name: uuid-gen
description: Generate UUIDs (v4) or short random base36 IDs on demand. Use when you need unique identifiers for records, filenames, test data, primary keys, slugs, tokens, or any situation that calls for a fresh random ID. Supports both standard UUIDs and shorter human-friendly IDs.
---

# UUID / ID Generator

Generate one or more unique identifiers using the bundled script.

## Quick start

```bash
python3 scripts/gen_id.py                 # one UUID v4, e.g. 3f0a8b...
python3 scripts/gen_id.py --count 5       # five UUID v4s
python3 scripts/gen_id.py --short         # one 10-char base36 id, e.g. k7m2p9xq1w
python3 scripts/gen_id.py --short --length 16 --count 3
```

## When to use which

- **UUID v4** (default): 128-bit, globally unique, ideal for database PKs, distributed systems, anything where collision risk must be effectively zero.
- **Short base36** (`--short`): shorter, URL-safe, case-insensitive. Good for slugs, invite codes, filenames, test fixtures. Default length 10 (~52 bits of entropy); increase `--length` for lower collision odds.

## Notes

- IDs are generated with `uuid.uuid4()` and `secrets.choice`, both cryptographically random.
- The script has no third-party dependencies; it runs on any Python 3.7+.
- Resolve `scripts/gen_id.py` relative to this skill's directory.
