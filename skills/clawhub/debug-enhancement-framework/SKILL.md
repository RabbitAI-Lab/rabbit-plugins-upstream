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
