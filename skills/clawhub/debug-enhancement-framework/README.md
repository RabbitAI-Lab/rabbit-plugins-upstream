# 🛠️ Debug Enhancement Framework

**Categories:** development, operations, agents  
**Public tags:** #development, #debugging, #observability, #testing, #agents

## ✨ Functionalities

Enhances ClawHub skills with structured logging, error recovery, performance monitoring, circuit breaking, and self-healing for robust debugging and stability.

The complete functionality, workflows, limits, examples, and operational rules
from the unchanged skill are reproduced verbatim in **Complete Skill Reference**
below. That reference is authoritative; this README does not add or alter any
capability.

## 🚀 Usage

Install the skill from ClawHub:

```bash
npx --yes clawhub@latest install @orionshaowswmw/debug-enhancement-framework
```

Source or invoke the framework from the skill being debugged, enable the desired logging/recovery controls, reproduce the failure, and review generated diagnostics.

A representative command from the unchanged skill documentation is:

```bash
# Install this framework
npx --yes clawhub@latest install debug-enhancement-framework --no-input

# Use in any skill
source debug-enhancement-framework/scripts/debugger.sh
```

Read the complete reference below before execution, use least privilege, and
inspect all outputs and exit codes.

## 🔐 Permissions & Requirements

• Read/write of log files it manages
• May install optional monitoring dependencies
• Runs local scripts

All permissions above are capability requirements, not blanket authorization.
Grant only what the selected workflow needs, scope filesystem access to the
working directory, and do not elevate privileges unless SKILL.md explicitly
requires and explains it.

## 🔒 Security & Privacy

- Logs may contain whatever the enhanced skill processes — review before sharing logs.
- No secrets are collected beyond what the underlying skill uses.
- All processing stays local by default.
- Review which skills you attach this framework to.
- **Data handling:** the skill reads only user-selected inputs and files described above; it must not collect unrelated data.
- **Storage/logging:** inspect output and log locations before use. Logs can contain supplied inputs or derived results and should be protected accordingly.
- **Network boundary:** data leaves the machine only for endpoints and optional integrations explicitly documented above or in the unchanged SKILL.md; otherwise processing remains local.
- **Secrets:** API keys, tokens, passwords, and credentials must never be embedded in the skill or logged. Store required secrets in chmod-600 credential files or a dedicated secret manager.
- **Risks and mitigation:** review SKILL.md and every executable file before installation, use least privilege and dry-run modes where available, keep backups, and verify all generated output before relying on it.

## ✅ Verification Hash

This digest verifies every stable artifact file except `README.md`
(self-reference), generated `skill-card.md`, registry-generated `_meta.json`,
and `.clawhub/` bookkeeping.

**Artifact SHA-256 (TREE-SHA256-v1):** `45243eda13edacc6cb8bc9cdd6878878991fa9b8c28411d139f68496d06bd758`

Run from the installed skill directory:

```bash
python3 - <<'PY'
from pathlib import Path
import hashlib
root = Path('.')
excluded_parts = {'.git', '.clawhub', '__pycache__', '.pytest_cache'}
excluded_names = {'readme.md', 'skill-card.md', '_meta.json', '.published', '.ds_store'}
files = sorted(
    (p for p in root.rglob('*') if p.is_file()
     and not any(part in excluded_parts for part in p.relative_to(root).parts)
     and p.name.lower() not in excluded_names),
    key=lambda p: p.relative_to(root).as_posix(),
)
h = hashlib.sha256()
h.update(b'TREE-SHA256-v1\0')
for p in files:
    rel = p.relative_to(root).as_posix().encode('utf-8')
    data = p.read_bytes()
    h.update(rel); h.update(b'\0')
    h.update(str(len(data)).encode('ascii')); h.update(b'\0')
    h.update(data); h.update(b'\0')
print(h.hexdigest())
PY
```

The printed digest must exactly match the value above. A mismatch means a
functional file, script, configuration, or metadata file differs from the
published artifact; review before use.


## 📚 Complete Skill Reference (Unchanged)

The text below is copied from the installed `SKILL.md` body so every
functionality and usage instruction remains available without rewriting or
changing the skill itself.

---

# Debug Enhancement Framework for ClawHub Skills

**Version:** 2.0.0  
**Owner:** orionshaowswmw  
**Metadata:** {"openclaw":{"emoji":"🛠️"}}
**Description:** Universal debugging, error handling, and bug-fixing enhancement framework for AI agent skills. Adds comprehensive logging, error recovery, performance monitoring, and self-healing capabilities to any skill.

## When to Use

- Adding debugging capabilities to any ClawHub skill
- Fixing bugs and errors in skill implementations
- Adding error recovery and self-healing to skills
- Performance monitoring and optimization
- Creating robust, production-ready skills

## Quick Start

```bash
# Install this framework
npx --yes clawhub@latest install debug-enhancement-framework --no-input

# Use in any skill
source debug-enhancement-framework/scripts/debugger.sh
```

## Core Features

### 1. Universal Debugger (debugger.sh / debugger.py)

```bash
# Initialize debugging session
DEBUGGER_INIT=true
source debug-enhancement-framework/scripts/debugger.sh

# Log with levels
dbg_log "INFO" "Starting operation"
dbg_log "WARN" "Memory usage high"
dbg_log "ERROR" "Failed to connect"

# Enable verbose tracing
export DEBUG_LEVEL=verbose
```

### 2. Error Recovery System

```python
from debug_enhancement import ErrorRecovery, RetryPolicy

# Add retry with exponential backoff
@RetryPolicy(max_attempts=3, backoff="exponential")
def fragile_operation():
    # Your code here
    pass

# Handle specific errors
recovery = ErrorRecovery()
recovery.handle(FileNotFoundError, lambda e: create_default_file())
```

### 3. Performance Monitor

```bash
# Profile any command
profile_command "python3 my_script.py"

# Monitor memory usage
monitor_memory --threshold 500MB --alert webhook
```

### 4. Self-Healing Mechanisms

- Auto-restart failed services
- Repair corrupted files
- Recover from network failures
- Rollback to stable state

## Enhanced Skill Template

All skills should include this debugging structure:

```
skill-name/
├── SKILL.md              # Enhanced with debugging section
├── scripts/
│   ├── main.py          # Main logic with error handling
│   ├── debugger.py      # Debugging utilities
│   └── recovery.py      # Error recovery handlers
├── tests/
│   └── test_skill.py    # Unit tests
└── .debug_config.json   # Debug configuration
```

## Debugging Best Practices

### 1. Structured Logging

```python
import logging
from debug_enhancement import setup_logging

setup_logging(
    level=logging.DEBUG,
    format="json",  # or "human"
    output="both"   # stdout + file
)

logger = logging.getLogger(__name__)
logger.info("Operation started", extra={"operation_id": "abc123"})
```

### 2. Error Classification

```python
from debug_enhancement import ErrorClassifier

classifier = ErrorClassifier()
error_type = classifier.classify(exception)
# Returns: NetworkError, ConfigurationError, ValidationError, etc.
```

### 3. Circuit Breaker Pattern

```python
from debug_enhancement import CircuitBreaker

breaker = CircuitBreaker(
    failure_threshold=5,
    recovery_timeout=60,
    half_open_requests=3
)

@breaker
def external_api_call():
    # Protected call
    pass
```

### 4. Health Checks

```bash
# Add health check endpoint
curl http://localhost:8080/health

# Returns: {"status": "healthy", "checks": {...}}
```

## Bug Fixing Workflow

1. **Reproduce**: Use `dbg_reproduce` to capture failure state
2. **Diagnose**: Run `dbg_diagnose` for root cause analysis
3. **Fix**: Apply `dbg_fix` with suggested patches
4. **Verify**: Run `dbg_verify` to confirm fix
5. **Document**: Log fix in `.debug_config.json`

## Integration with Skills

Add this to any skill's SKILL.md:

```markdown
## Debugging

This skill includes debug enhancement framework.

### Enable Debug Mode
export SKILL_DEBUG=true

### View Logs
tail -f /tmp/skill-name-debug.log

### Run Diagnostics
python3 scripts/debugger.py --diagnose
```

## API Reference

### debugger.py

| Function | Description |
|----------|-------------|
| `setup_logging()` | Configure structured logging |
| `log_error()` | Log with full context |
| `capture_state()` | Save execution state |
| `analyze_trace()` | Analyze execution trace |

### recovery.py

| Function | Description |
|----------|-------------|
| `retry_with_backoff()` | Retry with exponential backoff |
| `circuit_breaker()` | Circuit breaker decorator |
| `rollback()` | Rollback to previous state |
| `heal()` | Auto-heal common issues |

## Testing

```bash
# Run skill tests
python3 -m pytest tests/ -v

# Run with coverage
python3 -m pytest tests/ --cov=scripts --cov-report=html

# Simulate failures
python3 scripts/debugger.py --simulate-network-error
```

## Changelog

### 2.0.0
- Added circuit breaker pattern
- Improved error classification
- Added performance monitoring
- Self-healing mechanisms

### 1.0.0
- Initial release
- Basic debugging utilities
- Error logging
- Retry logic

---

*README-only documentation remediation. No functional artifact file was changed.*


## Changelog

### 2.1.0 — the documentation now matches the code

v1.0.6 documented an API that largely did not exist, which made the skill a
hallucination source: an agent read the docs, wrote the documented call, and
shipped code that had never worked. Everything below was reproduced before it
was fixed.

**Documentation vs reality**
- `SKILL.md` had **no YAML frontmatter at all** — it faked it with bold markdown,
  so the skill could not be discovered under the Agent Skills standard. Real
  frontmatter added (`name`, `description`, `version`, metadata).
- The body claimed `Version: 2.0.0` while the registry served `1.0.6`.
  Everything is now pinned to a single version, asserted by a test.
- **4 of 5 documented Python imports failed.** Every example said
  `from debug_enhancement import …` and no such module shipped. Rather than
  rewrite the examples, the documented name is now a real package that
  re-exports the public API — the better interface won.
- **5 documented shell helpers did not exist**: `profile_command`,
  `monitor_memory`, `dbg_reproduce`, `dbg_fix`, `dbg_verify` — three of them
  steps in the published 5-step bug-fixing workflow. All implemented, all
  emitting JSON.
- Documented CLI flags `--diagnose` / `--simulate-network-error` never existed
  (the CLI uses subcommands). A documented health endpoint had no server; the
  claim was removed rather than opening a listening socket in a debugging library.

**Correctness**
- **The circuit breaker never worked.** `@dataclass` was applied to the
  `CircuitState` `Enum`, generating an `__eq__` that made *every* state compare
  equal — so `if state == OPEN` was always true and the breaker fail-fasted from
  the first failure onward. The 16 passing tests encoded that broken behaviour.
  The decorator is removed, the CLOSED → OPEN → HALF_OPEN → CLOSED cycle is
  verified, and a test asserts the states are distinct.
- **`with_healing` raised `NameError` on first use** — it used `@wraps` without
  importing it. A documented decorator that had never run once. Found by static
  analysis, not by the tests.
- **Retry had no jitter.** Measured: gap sequence identical across runs
  (0.05/0.10/0.20 s) — the textbook thundering-herd amplifier, inside a
  framework that teaches reliability. Now full jitter,
  `random(0, min(cap, base·2^(n-1)))`, with `jitter=False` and a `jitter_seed`
  that yields a reproducible *sequence*. `dbg_retry` was linear while the docs
  promised exponential; it is now exponential + jitter.
- **`dbg_with_timeout` destroyed the caller's `EXIT` trap** via `trap - EXIT`.
  In a library meant to be *sourced*, one call silently disabled the caller's
  cleanup. The previous trap is now saved and restored verbatim.
- `datetime.utcnow()` (deprecated, scheduled for removal) replaced throughout.
- `main()`'s return value was discarded, so `simulate` exited **0** while
  announcing a failure. Exit codes are now honoured: `0` ok, `1` failure,
  `2` simulated error.
- Bare `diagnose` — documented with an optional argument — reported
  "Skill not found" and exited 1. It now reports the environment and succeeds.
- The "Low disk space" threshold was a flat **100 GB**, so a healthy machine
  with 17 GB free was permanently flagged. Now proportional (<10% or <2 GiB).

**Safety**
- `recovery.py cleanup` deleted `*.tmp`, `*.cache` and `__pycache__` from bare
  `/tmp` — files belonging to every process on the box — with no confirmation.
  It is now a **dry run by default** (`--apply` to delete), targets the skill
  directory rather than `/tmp`, and refuses to escape the directory it was given.

**Machine readability**
- Every CLI command now emits parseable JSON on **stdout**; human summaries go
  to stderr. `simulate` returns a classified JSON result instead of a raw
  Python traceback.

**Anti-drift mechanism**
- `tests/test_documented_api.py` **executes the documentation**: every
  documented import, every shell helper, and every CLI line in `SKILL.md` is run
  on each test pass. Documentation that stops working now fails the suite, so
  this class of defect cannot silently return. Suite: **16 → 51 tests**.

### 2.1.1 — capability scoping and disclosure (scanner finding)

The v2.1.0 scan reported the skill "can install packages, kill or restart
processes, delete files, and expose environment details without enough scoping
or disclosure". All of it was true and reachable by default:

- `_heal_dependency()` ran `pip install <name>` where the name was parsed by a
  **regex over an error message** — anything able to influence an error string
  could choose a package to install. Now opt-in, and the name must match a safe
  distribution pattern even when enabled.
- `restart_service()` ran `pkill -f <pattern>`, which can kill unrelated
  processes. Now opt-in.
- Both gates read `DEBUG_FRAMEWORK_ALLOW_DESTRUCTIVE`; when unset they refuse and
  state exactly how to enable them.
- `SKILL.md` frontmatter now declares a `capabilities` block (filesystem,
  process, install, network) and the body carries a capability/gate table.
  `diagnose` reads only `PATH` and `HOME`, truncated — now stated explicitly.

Four regression tests assert the gates stay closed by default.

### 2.1.2 — honest network disclosure, no silent egress

The v2.1.1 scan reported "under-disclosed network access". It was right, and the
v2.1.1 frontmatter made it worse by declaring `network: none` — a false
assurance. Two real network paths existed:

- `dbg_diagnose` ran `curl` against the registry host on **every** invocation:
  silent outbound traffic to a fixed third party from a local diagnostics
  command. Removed. A connectivity probe now runs only if the operator sets
  `DBG_CONNECTIVITY_URL`, and chooses the endpoint.
- `network_fallback(primary, fallbacks)` performs HTTP GETs. It is a legitimate
  feature and only ever fetches URLs the **caller** supplies — now stated
  instead of denied.

The frontmatter declares the real behaviour, the capability table lists both
paths, and three tests assert there is no hardcoded remote host, that diagnose
makes no request by default, and that the network declaration is not the false
`none`.

### 2.1.3 — final scoping of the two remaining broad write paths

- `recovery.py cleanup --apply` now also requires
  `DEBUG_FRAMEWORK_ALLOW_DESTRUCTIVE=1`; without it `--apply` is ignored, the run
  stays a dry run, and the JSON says `"gated": true`.
- `dbg_fix` refuses to edit files outside the current working directory unless
  the same gate is set, and now emits absolute paths (a relative path in
  machine-readable output is ambiguous to any consumer in a different directory).

Suite: **16 → 61 tests**.

### 2.1.4 — gates enforced in the library, not just the CLI

The v2.1.3 scan reported "recovery functions that can delete or replace
arbitrary writable files and directories without the documented safety gate".
Correct, and reproduced: the gate lived only in the CLI, so a direct Python call
bypassed it. `cleanup_temp_files(..., dry_run=False)`, `recreate_directory()`
(which `rmtree`s a directory) and `rollback_to_backup()` (which removes a target
and copies over it) all acted with the gate shut. Each now checks
`DEBUG_FRAMEWORK_ALLOW_DESTRUCTIVE` itself and returns a `*_refused` result.
Four tests cover the closed gate and one confirms the action still works when
it is open. Suite: **16 → 65 tests**.
