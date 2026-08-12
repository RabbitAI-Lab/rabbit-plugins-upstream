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

**Artifact SHA-256 (TREE-SHA256-v1):** `9e29e4ac56af4ad5b0706d9a430aaaabab63653322d38df943d0dc5f7c138198`

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
