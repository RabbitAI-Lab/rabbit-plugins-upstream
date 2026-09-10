#!/usr/bin/env python3
"""
_io.py — UTF-8-safe I/O primitives shared by every script in this skill.

WHY THIS EXISTS (v2.1.0, reproduced bugs — see CHANGELOG):

  1. Under a non-UTF-8 locale (`LC_ALL=C`, common in cron, Docker `scratch`
     images, CI runners and systemd units) Python picks ASCII for stdout.
     Printing Persian/Arabic/CJK then raised `UnicodeEncodeError` and killed
     the script — in a skill that advertises multilingual support.

  2. `open(path)` with no `encoding=` inherits that same locale, so a state
     file written on a UTF-8 box failed to READ on an ASCII box.

  3. `json.dump(...)` without `ensure_ascii=False` stores Persian as `\\uXXXX`
     escapes — measured ~4x larger state files for non-Latin scripts.

  4. `json.load(open(p))` never closes the handle (ResourceWarning / fd leak
     in long-lived agent processes).

Everything here is stdlib-only and import-safe: no side effects beyond the
explicit `utf8_io()` call, which is idempotent.
"""
from __future__ import annotations

import json
import os
import sys
import tempfile
from typing import Any

__all__ = ["utf8_io", "sanitize", "jload", "jdump", "jdumps", "atomic_write", "emit"]

_CONFIGURED = False


def sanitize(s: Any) -> Any:
    """Repair lone surrogates so the string can always be UTF-8 encoded.

    Under a non-UTF-8 locale CPython decodes `sys.argv` with the
    `surrogateescape` handler, so a Persian argument arrives as unpaired
    surrogates. Any later `.encode("utf-8")` — hashing a prompt fingerprint,
    writing state, printing — then dies with:

        UnicodeEncodeError: surrogates not allowed

    This is an INPUT-side crash, distinct from the stdout crash `utf8_io()`
    fixes. Round-tripping through `surrogateescape` recovers the original
    bytes and `replace` guarantees the result is encodable.
    """
    if not isinstance(s, str):
        return s
    try:
        s.encode("utf-8")
        return s
    except UnicodeEncodeError:
        pass
    try:
        # Recovers the original bytes for the DC80-DCFF escape range that
        # CPython uses when decoding argv/filenames under a non-UTF-8 locale.
        return s.encode("utf-8", "surrogateescape").decode("utf-8", "replace")
    except UnicodeEncodeError:
        # A lone surrogate OUTSIDE the escape range (e.g. U+D800 pasted into a
        # prompt) cannot be surrogateescape-encoded either. "replace" always
        # succeeds, so the function is total: it can never raise.
        return s.encode("utf-8", "replace").decode("utf-8", "replace")


def utf8_io() -> None:
    """Force stdout/stderr to UTF-8 and repair argv so non-ASCII can't crash.

    Idempotent and defensive: `reconfigure` exists on Python 3.7+, but a
    stream may be a pipe, a StringIO under test, or already detached. Any
    failure is swallowed — degraded output beats a traceback.
    """
    global _CONFIGURED
    if _CONFIGURED:
        return
    _CONFIGURED = True
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[attr-defined]
        except Exception:
            pass
    try:  # repair surrogate-escaped CLI arguments in place, once, for every script
        sys.argv[:] = [sanitize(a) for a in sys.argv]
    except Exception:
        pass


def jload(path: str, default: Any = None) -> Any:
    """Read JSON as UTF-8, closing the handle. Returns `default` on any error.

    Tolerates a truncated/corrupt state file (e.g. the sandbox was wiped
    mid-write) instead of crashing the caller's turn.
    """
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except Exception:
        return default


def jdumps(obj: Any, *, compact: bool = False) -> str:
    """Serialise to JSON text. `compact=True` emits minified single-line JSON.

    Minified output is materially cheaper for a consuming model: indentation
    and newlines are pure token overhead once a machine, not a human, reads it.
    """
    if compact:
        return json.dumps(obj, ensure_ascii=False, separators=(",", ":"), default=str)
    return json.dumps(obj, ensure_ascii=False, indent=2, default=str)


def jdump(obj: Any, path: str) -> None:
    """Atomically write JSON as UTF-8 with real (non-escaped) characters."""
    atomic_write(path, json.dumps(obj, ensure_ascii=False, indent=2, default=str))


def atomic_write(path: str, text: str) -> None:
    """Write `text` to `path` atomically (tmp file + os.replace), UTF-8.

    Atomic so a crash or a sandbox wipe mid-write can never leave a
    half-written state file that poisons every later turn.
    """
    d = os.path.dirname(os.path.abspath(path)) or "."
    os.makedirs(d, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=d, prefix=".tmp_", suffix=".json")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(text)
        try:                       # owner-only: state can be conversation-derived
            os.chmod(tmp, 0o600)
        except OSError:
            pass
        os.replace(tmp, path)
    except Exception:
        try:
            os.unlink(tmp)
        except Exception:
            pass
        raise


def emit(obj: Any, human: str = "", *, as_json: bool = False, compact: bool = False) -> None:
    """Print either the machine bundle or the human line, always UTF-8-safe."""
    utf8_io()
    if as_json:
        print(jdumps(obj, compact=compact))
    elif human:
        print(human)
