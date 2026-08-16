#!/usr/bin/env python3
"""Validate a translator-pro glossary JSON file."""
import json
import sys
from pathlib import Path

REQUIRED_FIELDS = {"source", "target", "source_lang", "target_lang"}
VALID_LANGS = {"en", "zh-CN", "es"}

def validate(path: str) -> int:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, list):
        print(f"ERROR: Glossary must be a JSON array, got {type(data).__name__}")
        return 1
    errors = 0
    for i, entry in enumerate(data):
        if not isinstance(entry, dict):
            print(f"ERROR: Entry {i} is not an object")
            errors += 1
            continue
        missing = REQUIRED_FIELDS - set(entry.keys())
        if missing:
            print(f"ERROR: Entry {i} missing fields: {missing}")
            errors += 1
        for lang_field in ("source_lang", "target_lang"):
            if lang_field in entry and entry[lang_field] not in VALID_LANGS:
                print(f"ERROR: Entry {i} has invalid {lang_field}: {entry[lang_field]}")
                errors += 1
        if "context" in entry and entry["context"] not in {"business", "legal", "casual", "technical"}:
            print(f"WARN: Entry {i} has unusual context: {entry['context']}")
    if errors == 0:
        print(f"OK: {len(data)} glossary entries validated")
    return 1 if errors else 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: validate_glossary.py <glossary.json>")
        sys.exit(2)
    sys.exit(validate(sys.argv[1]))