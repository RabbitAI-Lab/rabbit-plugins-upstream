"""debug_enhancement — the public API of the Debug Enhancement Framework.

WHY THIS PACKAGE EXISTS (v2.1.0):

Every Python example in SKILL.md told agents to write::

    from debug_enhancement import ErrorRecovery, RetryPolicy

...and that import raised ``ModuleNotFoundError``, because the code actually
lived in ``scripts/debugger.py`` and ``scripts/recovery.py``. Four of the five
documented imports failed. A skill whose documentation cannot be executed is a
hallucination generator: an agent reads it, writes the documented call, and
ships code that has never worked.

Two ways to fix that: rewrite every example, or make the documented import
real. This package does the second, because the documented name is the better
public API — it hides the file layout, so `scripts/` can be reorganised without
breaking a single consumer.

Usage (add the skill root to sys.path, then import normally)::

    import sys; sys.path.insert(0, "/path/to/debug-enhancement-framework")
    from debug_enhancement import RetryPolicy, CircuitBreaker, setup_logging

Every name re-exported here is covered by ``tests/test_documented_api.py``,
which executes the documented examples so this file can never drift again.
"""

from __future__ import annotations

import os as _os
import sys as _sys

_HERE = _os.path.dirname(_os.path.abspath(__file__))
_SCRIPTS = _os.path.join(_os.path.dirname(_HERE), "scripts")
if _SCRIPTS not in _sys.path:
    _sys.path.insert(0, _SCRIPTS)

from debugger import (  # noqa: E402
    CircuitBreaker,
    CircuitBreakerError,
    CircuitState,
    ClassifiedError,
    ErrorClassifier,
    ErrorRecovery,
    ErrorType,
    JSONFormatter,
    PerformanceMonitor,
    RetryPolicy,
    StateCapture,
    diagnose_environment,
    run_diagnostics,
    setup_logging,
)
from recovery import (  # noqa: E402
    AutoHealer,
    RecoveryResult,
    RecoveryStrategies,
    with_healing,
)

__version__ = "2.1.4"

__all__ = [
    # logging
    "setup_logging",
    "JSONFormatter",
    # error classification
    "ErrorClassifier",
    "ClassifiedError",
    "ErrorType",
    # resilience
    "RetryPolicy",
    "CircuitBreaker",
    "CircuitBreakerError",
    "CircuitState",
    "ErrorRecovery",
    # observability
    "PerformanceMonitor",
    "StateCapture",
    "diagnose_environment",
    "run_diagnostics",
    # healing
    "AutoHealer",
    "RecoveryStrategies",
    "RecoveryResult",
    "with_healing",
    "__version__",
]
