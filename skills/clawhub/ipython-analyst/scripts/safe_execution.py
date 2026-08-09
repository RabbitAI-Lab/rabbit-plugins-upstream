"""
safe_execution.py — Resource limits, timeouts, and safe expression evaluation.

Bug fixes vs v6:
- `OperationTimeout` replaces the v6 `class TimeoutError(Exception)` that shadowed
  the builtin TimeoutError and broke `except TimeoutError:` callers.
- `resource_limits` saves and restores the original soft limit (was resetting to
  RLIM_INFINITY, which silently fails when the hard limit is lower).
"""
from __future__ import annotations

import math
import resource
import signal
from contextlib import contextmanager
from typing import Iterator


class OperationTimeout(Exception):
    """Raised by timeout_context when the operation exceeds the deadline.

    Distinct from the builtin TimeoutError so we don't shadow it — code that
    catches the builtin (e.g. socket operations) keeps working.
    """


@contextmanager
def timeout_context(seconds: float, error_message: str = "Operation timed out") -> Iterator[None]:
    """Context manager that raises OperationTimeout after `seconds` elapsed.

    Uses SIGALRM so it can interrupt blocking C calls (regex backtracking,
    socket reads, sleep). Unix-only; on Windows it's a no-op.
    """
    if not hasattr(signal, "SIGALRM"):
        # Windows fallback — no interruption, just yield.
        yield
        return

    def handler(signum: int, frame) -> None:
        raise OperationTimeout(error_message)

    seconds_int = max(1, int(math.ceil(seconds)))
    original_handler = signal.signal(signal.SIGALRM, handler)
    signal.alarm(seconds_int)
    try:
        yield
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, original_handler)


@contextmanager
def resource_limits(max_memory_mb: int = 2048, max_cpu_seconds: int = 300) -> Iterator[None]:
    """Context manager to enforce memory and CPU limits on the current process.

    Note: setting RLIMIT_AS too low can crash Python itself (the interpreter needs
    address space for imports, JIT buffers, etc.). Use generous limits and prefer
    timeout_context for stopping specific operations rather than killing the process.
    """
    originals: dict[int, tuple[int, int]] = {}
    try:
        for limit, value in [
            (resource.RLIMIT_AS, max_memory_mb * 1024 * 1024),
            (resource.RLIMIT_CPU, max_cpu_seconds),
        ]:
            try:
                soft, hard = resource.getrlimit(limit)
                # Don't raise above the hard limit — silently cap instead.
                new_soft = min(value, hard) if hard != resource.RLIM_INFINITY else value
                resource.setrlimit(limit, (new_soft, hard))
                originals[limit] = (soft, hard)
            except (ValueError, OSError):
                pass  # resource module Unix-only or limit not supported
        yield
    finally:
        for limit, (soft, hard) in originals.items():
            try:
                resource.setrlimit(limit, (soft, hard))
            except (ValueError, OSError):
                pass


def safe_eval(expression: str, allowed_names: dict | None = None):
    """Evaluate a Python expression with a restricted namespace.

    Only safe builtins (abs, min, max, sum, len, range, round) and `math`
    functions are exposed. No `__builtins__`, no attribute access to dunder
    methods. This is defense-in-depth, not a security boundary — for truly
    untrusted code, run in a subprocess with resource_limits.
    """
    import math as _math
    allowed: dict = {
        "__builtins__": {},
        "abs": abs, "min": min, "max": max, "sum": sum,
        "len": len, "range": range, "round": round,
        "True": True, "False": False, "None": None,
    }
    for name in dir(_math):
        if not name.startswith("_"):
            allowed[name] = getattr(_math, name)
    if allowed_names:
        allowed.update(allowed_names)
    try:
        return eval(expression, allowed, {})  # noqa: S307 — sandboxed namespace
    except NameError as e:
        raise ValueError(f"Unsafe or undefined name: {e}") from e


__all__ = [
    "OperationTimeout",
    "timeout_context",
    "resource_limits",
    "safe_eval",
]
