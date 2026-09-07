---
name: debug-enhancement-framework
description: >
  Adds structured JSON logging, error classification, retry with exponential
  backoff and full jitter, circuit breaking, performance profiling, state
  capture, and auto-healing to any skill or script, in Python and Bash. Use when
  a skill or agent needs debugging, error recovery, resilience against flaky
  network or rate-limited calls, thundering-herd-safe retries, crash diagnostics,
  performance profiling, memory monitoring, or a reproduce-diagnose-fix-verify
  workflow for an existing bug.
version: 2.1.4
categories: [development, operations, agents]
topics: [debugging, observability, error-recovery, resilience, testing]
metadata:
  openclaw:
    emoji: "🛠️"
    requires:
      bins: [python3, bash]
      python: []
    capabilities:
      filesystem: "reads user-supplied paths; writes logs and state captures; dbg_fix edits a named file in place (with a .dbgbak backup); cleanup deletes ONLY with --apply"
      process: "restart_service runs pkill -f and respawns a command - OPT-IN via DEBUG_FRAMEWORK_ALLOW_DESTRUCTIVE"
      install: "auto-heal may run pip install for a missing module - OPT-IN via DEBUG_FRAMEWORK_ALLOW_DESTRUCTIVE, and the name must be a safe distribution name"
      network: "no unsolicited traffic. network_fallback() fetches URLs the CALLER supplies; dbg_diagnose performs a connectivity probe ONLY if DBG_CONNECTIVITY_URL is set. Nothing is sent anywhere by default."
      environment: "diagnose reports PATH and HOME (truncated) and, in the bash dbg_diagnose, a process list from ps"
---

# 🛠️ Debug Enhancement Framework

Structured logging, resilient retries, circuit breaking, and auto-healing for
any skill. **Python 3.8+ and Bash, stdlib only — nothing to pip-install.**

> Every command and import on this page is executed by
> `tests/test_documented_api.py` on every run. If an example here stops working,
> the test suite fails. Documentation cannot drift from the code.

## Use when

Adding debugging or error recovery to a skill · retrying flaky network or
rate-limited calls safely · protecting against a failing dependency · profiling
a slow command · capturing crash state · diagnosing an environment · walking a
bug through reproduce → diagnose → fix → verify.

## Python API

Put the **skill root** on `sys.path`, then import the public package:

```python
import sys; sys.path.insert(0, "/path/to/debug-enhancement-framework")
from debug_enhancement import RetryPolicy, CircuitBreaker, ErrorClassifier, setup_logging
```

| Import | What it does |
|---|---|
| `setup_logging(level, format, output)` | structured logging; `format="json"` or `"human"` |
| `ErrorClassifier.classify(exc)` | → `ClassifiedError` with an `ErrorType` (NETWORK, TIMEOUT, VALIDATION, PERMISSION, …) |
| `RetryPolicy(...)` | decorator: retry with exponential backoff + **full jitter** |
| `CircuitBreaker(...)` | decorator: fail fast while a dependency is down; CLOSED → OPEN → HALF_OPEN |
| `ErrorRecovery()` | register per-exception-type handlers |
| `PerformanceMonitor()` | time and record operations |
| `StateCapture()` | persist execution state for postmortem |
| `AutoHealer`, `RecoveryStrategies`, `with_healing` | auto-heal known failure classes |
| `diagnose_environment()`, `run_diagnostics(name)` | environment/skill diagnostics |

### Retry — always jittered

```python
from debug_enhancement import RetryPolicy

@RetryPolicy(max_attempts=3, initial_delay=1.0, max_delay=60.0)
def fragile():
    ...
```

Delay is **full jitter**: `random(0, min(max_delay, initial_delay * 2**(attempt-1)))`.
Plain exponential backoff makes every client retry in lock-step and is the
classic thundering-herd amplifier — so jitter is **on by default**. Pass
`jitter=False` only to reproduce a legacy timing bug, and `jitter_seed=N` for
deterministic tests. `RetryPolicy.compute_delay(attempt)` is public so you can
assert on it. VALIDATION errors are never retried.

### Circuit breaker

```python
from debug_enhancement import CircuitBreaker
breaker = CircuitBreaker(failure_threshold=5, recovery_timeout=60.0)
```

## Bash API

```bash
source scripts/debugger.sh          # sets up logging + an ERR handler
```

| Function | Purpose |
|---|---|
| `dbg_log LEVEL MSG` · `dbg_info/warn/error/debug/fatal` | structured log lines |
| `dbg_retry ATTEMPTS BASE_DELAY "cmd"` | retry, exponential + full jitter (cap `$DBG_RETRY_MAX_DELAY`, default 60) |
| `dbg_with_timeout SECS "cmd"` | run with a timeout; **preserves your EXIT trap** |
| `dbg_time_command "cmd"` · `profile_command "cmd"` | timing; `profile_command` emits JSON incl. peak RSS |
| `monitor_memory [--threshold MB] [--pid PID]` | JSON RSS report, warns past threshold |
| `dbg_capture_state` · `dbg_diagnose` | snapshot state / environment report |
| `dbg_reproduce "cmd"` → `dbg_diagnose` → `dbg_fix FILE SED_EXPR` → `dbg_verify "cmd" [rc]` | the 4-step bug workflow; `dbg_fix` writes a `.dbgbak` backup and rolls back on failure |
| `dbg_simulate_error network\|timeout\|validation\|permission` | inject a failure for testing |

`dbg_retry` and `dbg_with_timeout` take a **command string** and `eval` it — pass
only strings you control, never unsanitised input.

## CLI

```bash
python3 scripts/debugger.py diagnose [SKILL]        # environment + skill diagnostics
python3 scripts/debugger.py list-captures [--skill S]
python3 scripts/debugger.py report                  # performance report
python3 scripts/debugger.py simulate network|timeout|validation|permission
python3 scripts/recovery.py heal "error message"
python3 scripts/recovery.py health
python3 scripts/recovery.py cleanup [--skill S] [--apply]   # DRY RUN unless --apply
```

All emit JSON on stdout. Exit code `0` = success, non-zero = failure.

## Hard rules for the agent using this skill

1. **Never invent an API.** Only the names in the tables above exist. If you
   need something else, read `scripts/debugger.py` — do not guess a function
   name because it sounds plausible.
2. **Never disable jitter** to make timing "predictable" in production; use
   `jitter_seed` in tests instead.
3. **Never retry a non-idempotent operation** without an idempotency key, and
   never retry validation/permission errors — they will fail again.
4. **Report what the tool returned**, not what you expected. Every command emits
   JSON; quote the field rather than paraphrasing it.
5. **`dbg_fix` edits files in place.** It backs up to `.dbgbak`, but confirm the
   target before running it, and never point it at a path you did not verify.
6. **`recovery.py cleanup` is a DRY RUN by default.** It only lists what it
   would remove. Deletion requires `--apply`; never add `--apply` on a path you
   have not inspected, and never run it against a shared directory.

## Capabilities and their gates

This is a debugging framework, so it can do disruptive things. Every disruptive
action is **off by default** and states how to enable it.

| Action | Default | To enable |
|---|---|---|
| Read files, write logs / state captures | allowed | — |
| `dbg_fix FILE EXPR` — edits a file in place | allowed **only inside the working directory**, writes `FILE.dbgbak` first | `DEBUG_FRAMEWORK_ALLOW_DESTRUCTIVE=1` to edit elsewhere |
| `recovery.py cleanup` — deletes temp files | **dry run**, deletes nothing | `--apply` **and** `DEBUG_FRAMEWORK_ALLOW_DESTRUCTIVE=1` |
| `restart_service()` — `pkill -f` + respawn | **refused** | `export DEBUG_FRAMEWORK_ALLOW_DESTRUCTIVE=1` |
| auto-heal `pip install <missing module>` | **refused** | same env var, **and** the package name must match `^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$` |
| `network_fallback(url, fallbacks)` — HTTP GET | allowed, but only URLs **you pass in** | — |
| `dbg_diagnose` connectivity probe | **no request made** | set `DBG_CONNECTIVITY_URL` |
| Unsolicited/telemetry traffic | never sent | not available |
| `recreate_directory()` — rmtree + recreate | **refused** | `DEBUG_FRAMEWORK_ALLOW_DESTRUCTIVE=1` |
| `rollback_to_backup()` — replaces a target path | **refused** | `DEBUG_FRAMEWORK_ALLOW_DESTRUCTIVE=1` |

Gates are enforced **inside the library functions**, not only in the CLI, so
calling the Python API directly cannot bypass them.

The package name for auto-install is parsed out of an *error message*, so it is
treated as untrusted input and validated even when the gate is open.
`diagnose` reports `PATH` and `HOME` (truncated to 100 chars) — no other
environment variables are read or emitted. The bash `dbg_diagnose` additionally
prints a `ps` process list locally. Earlier versions silently curled
`clawhub.ai` on every diagnose; that phone-home is gone.

## Verify

```bash
python3 -m pytest tests/ -q          # unit + documented-API tests
python3 tests/test_documented_api.py # executes every example on this page
```

Deeper notes: `README.md` (security, permissions, artifact hash).
