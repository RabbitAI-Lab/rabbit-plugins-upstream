#!/usr/bin/env python3
"""mcp_server.py — expose the skill's core tools over the Model Context
Protocol (F35). stdio JSON-RPC 2.0, protocol version 2024-11-05.

  echo '...request...' | python3 mcp_server.py

Tools exposed: inference_triage, inference_scorecard, conformal_gate,
cache_lookup, certificate_validate. Sibling tools must sit in the same dir.

F38 gate (v2.1.0): every tools/call is structurally validated (known tool,
required args, no extra args); calls flagged wants_side_effects are refused
unless a human approved them in the transcript (all built-ins are
side-effect-free, so flagged calls are refused — run the CLI directly).
"""
import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

PROTOCOL = "2024-11-05"

def _read_skill_version():
    """Read version from ../SKILL.md frontmatter; fall back to 2.1.0."""
    try:
        with open(os.path.join(HERE, "..", "SKILL.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("version:"):
                    return line.split(":", 1)[1].strip()
    except OSError:
        pass
    return "2.1.0"

SKILL_VERSION = _read_skill_version()

TOOLS = [
    {"name": "inference_triage", "side_effects": False, "annotations": {"readOnlyHint": True},
     "description": "Classify query difficulty (trivial/standard/hard) and get a deliberation preset",
     "inputSchema": {"type": "object", "properties": {"text": {"type": "string"}},
                     "required": ["text"], "additionalProperties": False}},
    {"name": "inference_scorecard", "side_effects": False, "annotations": {"readOnlyHint": True},
     "description": "Score a candidate answer: verification coverage, uncertainty calibration, escalation match",
     "inputSchema": {"type": "object",
                     "properties": {"text": {"type": "string"},
                                    "difficulty": {"type": "string",
                                                   "enum": ["trivial", "standard", "hard"]}},
                     "required": ["text", "difficulty"], "additionalProperties": False}},
    {"name": "conformal_gate", "side_effects": False, "annotations": {"readOnlyHint": True},
     "description": "Accept/abstain/escalate decision for an uncertainty score given a calibrated threshold",
     "inputSchema": {"type": "object",
                     "properties": {"u": {"type": "number"}, "threshold": {"type": "number"},
                                    "escalate_above": {"type": "number"}},
                     "required": ["u", "threshold"], "additionalProperties": False}},
    {"name": "cache_lookup", "side_effects": False, "annotations": {"readOnlyHint": True},
     "description": "Exact/semantic cache lookup for a prompt (read-only)",
     "inputSchema": {"type": "object", "properties": {"prompt": {"type": "string"}},
                     "required": ["prompt"], "additionalProperties": False}},
    {"name": "certificate_validate", "side_effects": False, "annotations": {"readOnlyHint": True},
     "description": "Validate an answer certificate JSON",
     "inputSchema": {"type": "object", "properties": {"cert": {"type": "object"}},
                     "required": ["cert"], "additionalProperties": False}},
]

def handle_initialize(req):
    return {"protocolVersion": PROTOCOL,
            "capabilities": {"tools": {}},
            "serverInfo": {"name": "inference-expert-agents", "version": SKILL_VERSION}}

def _f38_check(name, args):
    """F38 gate: known tool, required args present, no extra args, approval."""
    spec = next((t for t in TOOLS if t["name"] == name), None)
    if spec is None:
        raise KeyError(name)
    schema = spec["inputSchema"]
    missing = [r for r in schema.get("required", []) if r not in args]
    if missing:
        raise ValueError(f"F38: missing required args for {name}: {missing}")
    allowed = set(schema.get("properties", {}))
    extra = [k for k in args if k not in allowed and k != "wants_side_effects"]
    if extra:
        raise ValueError(f"F38: unexpected args for {name}: {extra}")
    if args.get("wants_side_effects") and not spec.get("side_effects", False):
        raise PermissionError(
            f"F38 approval gate: '{name}' is side-effect-free; refusing a "
            "side-effecting call without explicit human approval in the transcript")
    return spec

def call_tool(name, args):
    _f38_check(name, args or {})
    from triage import triage
    if name == "inference_triage":
        return triage(args["text"])
    if name == "inference_scorecard":
        import inference_scorecard as sc
        return sc.score(args["text"], args.get("difficulty", "standard"))
    if name == "conformal_gate":
        th = args["threshold"]
        u = args["u"]
        out = {"decision": "accept" if u <= th else "abstain"}
        ea = args.get("escalate_above")
        if ea and u > th and u <= ea:
            out = {"decision": "escalate"}
        return out
    if name == "cache_lookup":
        import os as _os, cache_kit
        dbp = _os.environ.get("INFERENCE_EXPERT_CACHE_DB")
        if not dbp:
            return {"hit": False,
                    "note": "cache state is opt-in: set INFERENCE_EXPERT_CACHE_DB to a 0600 file to enable"}
        d = cache_kit.load(dbp)
        now = __import__("time").time()
        cache_kit.prune(d, 86400, 256, now)
        best, sim = None, 0.0
        for e in d["entries"]:
            s = 1.0 if e["prompt"] == args["prompt"] else cache_kit.jac(e["prompt"], args["prompt"])
            if s > sim:
                best, sim = e, s
        return {"hit": bool(best and sim >= 0.85), "similarity": round(sim, 3),
                "answer": best["answer"] if best and sim >= 0.85 else None}
    if name == "certificate_validate":
        import answer_certificate as ac
        return ac.validate(args["cert"])
    raise KeyError(name)

def handle(req):
    m = req.get("method", "")
    rid = req.get("id")
    if m == "initialize":
        return {"jsonrpc": "2.0", "id": rid, "result": handle_initialize(req)}
    if m == "notifications/initialized":
        return None
    if m == "tools/list":
        return {"jsonrpc": "2.0", "id": rid, "result": {"tools": TOOLS}}
    if m == "tools/call":
        p = req.get("params", {})
        try:
            out = {"content": [{"type": "text",
                                "text": json.dumps(call_tool(p.get("name"), p.get("arguments", {})))}]}
        except Exception as e:
            return {"jsonrpc": "2.0", "id": rid,
                    "result": {"content": [{"type": "text", "text": f"error: {e}"}], "isError": True}}
        return {"jsonrpc": "2.0", "id": rid, "result": out}
    if m == "ping":
        return {"jsonrpc": "2.0", "id": rid, "result": {}}
    if rid is not None:
        return {"jsonrpc": "2.0", "id": rid,
                "error": {"code": -32601, "message": f"method not found: {m}"}}
    return None

def main(argv=None):
    ap = argparse.ArgumentParser(
        prog="mcp_server.py",
        description="Expose inference-expert-agents tools over MCP (stdio JSON-RPC 2.0). "
                    "Reads requests on stdin, writes responses on stdout. "
                    "Tools: inference_triage, inference_scorecard, conformal_gate, "
                    "cache_lookup, certificate_validate.",
        epilog="F38 gate: calls are structurally validated; side-effecting calls "
               "(wants_side_effects) are refused without transcript approval.")
    ap.add_argument("--version", action="version", version=f"%(prog)s {SKILL_VERSION}")
    ap.parse_args(argv)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except json.JSONDecodeError:
            resp = {"jsonrpc": "2.0", "id": None,
                    "error": {"code": -32700, "message": "parse error"}}
            print(json.dumps(resp), flush=True)
            continue
        resp = handle(req)
        if resp is not None:
            print(json.dumps(resp), flush=True)

if __name__ == "__main__":
    main()
