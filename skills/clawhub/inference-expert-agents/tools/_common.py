#!/usr/bin/env python3
"""_common.py — shared internal helpers for inference-expert-agents tools (v2.1.0).

Import pattern inside tools/ (sibling scripts, NOT a package — same as mcp_server.py):
    import os as _os, sys as _sys
    _sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
    from _common import clean_errors

CLI contract: every tool emits a single JSON object on stdout and exits 0 on
success, 2 on usage/input/state errors — never a raw traceback. Achieve it by
decorating main() (additive; happy paths are untouched):

    @clean_errors
    def main():
        ...
"""
import functools
import json


def fail(message, code=2, hint=None):
    """Print a clean {"error": ...} object (plus an actionable "hint" when given)."""
    obj = {"error": message}
    if hint:
        obj["hint"] = hint
    print(json.dumps(obj))
    return code


def clean_errors(func):
    """Decorator: anything escaping main() becomes {"error": ...} + exit 2.

    Catches Exception (OSError, ValueError incl. JSON errors, KeyError on
    malformed inputs, ...). SystemExit/KeyboardInterrupt pass through so
    argparse usage errors and Ctrl-C keep their native behavior.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (SystemExit, KeyboardInterrupt):
            raise
        except Exception as exc:  # noqa: BLE001 — CLI contract: JSON errors only
            return fail(f"{type(exc).__name__}: {exc}")

    return wrapper
