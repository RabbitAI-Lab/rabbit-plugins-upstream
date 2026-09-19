#!/usr/bin/env python3
"""tool_guards.py — tool-call validation, strict structured outputs, and
Assert/Suggest retry semantics (F13, F36, F37, F38).

- validate: check a tool call against a declared spec (name declared, required
  args, types, enums, no undeclared args).
- schema: validate JSON data against a minimal JSON-Schema subset (type,
  required, enum, additionalProperties, properties, items) — strict-output
  contract for verdict objects.
- retry-semantics: DSPy-style Assert (halt after R retries) vs Suggest (warn
  and continue).
Stdlib-only, read-only.
"""
import argparse, json, sys

TYPES = {"string": str, "number": (int, float), "integer": int,
         "boolean": bool, "object": dict, "array": list, "null": type(None)}

def _jload(s):
    try:
        with open(s, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return json.loads(s)

def check_tool(spec, call):
    errs = []
    tools = {t["name"]: t for t in spec.get("tools", [])}
    name = call.get("name")
    if name not in tools:
        return {"ok": False, "errors": [f"hallucinated tool '{name}' — not in declared set (F37)"]}
    t = tools[name]
    args = call.get("args", {})
    declared = set((t.get("args") or {}).keys())
    for k in args:
        if declared and k not in declared:
            errs.append(f"undeclared argument '{k}' (strict additionalProperties)")
    for k, rule in (t.get("args") or {}).items():
        if k not in args:
            if rule.get("required"):
                errs.append(f"missing required argument '{k}'")
            continue
        v = args[k]
        ty = rule.get("type")
        if ty and ty in TYPES and not isinstance(v, TYPES[ty]) or (ty == "integer" and isinstance(v, bool)):
            errs.append(f"arg '{k}' expected {ty}, got {type(v).__name__}")
        if "enum" in rule and v not in rule["enum"]:
            errs.append(f"arg '{k}' not in enum {rule['enum']}")
    return {"ok": not errs, "errors": errs,
            "action": "execute" if not errs else "reject and re-ask the model with these errors"}

def check_schema(schema, data, path="$"):
    errs = []
    ty = schema.get("type")
    if ty and ty in TYPES and not isinstance(data, TYPES[ty]):
        return [f"{path}: expected {ty}, got {type(data).__name__}"]
    if "enum" in schema and data not in schema["enum"]:
        errs.append(f"{path}: {data!r} not in enum {schema['enum']}")
    if isinstance(data, dict):
        props = schema.get("properties", {})
        for r in schema.get("required", []):
            if r not in data:
                errs.append(f"{path}: missing required property '{r}'")
        if schema.get("additionalProperties") is False:
            for k in data:
                if k not in props:
                    errs.append(f"{path}: additional property '{k}' not allowed (strict mode)")
        for k, v in data.items():
            if k in props:
                errs.extend(check_schema(props[k], v, f"{path}.{k}"))
    if isinstance(data, list) and "items" in schema:
        for i, v in enumerate(data):
            errs.extend(check_schema(schema["items"], v, f"{path}[{i}]"))
    return errs

# v2.1.0: shared clean-error contract — never traceback ({"error":...} + exit 2)
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from _common import clean_errors


@clean_errors
def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    v = sub.add_parser("validate")
    v.add_argument("--spec", required=True)
    v.add_argument("--call", required=True)
    r = sub.add_parser("retry-semantics")
    r.add_argument("--constraint", choices=["assert", "suggest"], required=True)
    r.add_argument("--attempts", type=int, default=1)
    r.add_argument("--max-retries", type=int, default=3)
    s = sub.add_parser("schema")
    s.add_argument("--schema", required=True)
    s.add_argument("--data", required=True)
    a = ap.parse_args()
    if a.cmd == "validate":
        print(json.dumps(check_tool(_jload(a.spec), _jload(a.call)), indent=2))
        return 0
    if a.cmd == "retry-semantics":
        exhausted = a.attempts >= a.max_retries
        hard = a.constraint == "assert"
        print(json.dumps({
            "constraint": a.constraint, "attempts": a.attempts, "max_retries": a.max_retries,
            "decision": ("halt pipeline" if exhausted and hard else
                         "retry with error appended to prompt" if not exhausted else
                         "log warning and continue (Suggest is non-binding)"),
            "grounding": "DSPy Assertions (arXiv:2312.13382): Assert=hard, Suggest=soft"}))
        return 0
    errs = check_schema(_jload(a.schema), _jload(a.data))
    print(json.dumps({"ok": not errs, "errors": errs}, indent=2))
    return 0

if __name__ == "__main__":
    sys.exit(main())
