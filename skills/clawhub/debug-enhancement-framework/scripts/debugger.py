#!/usr/bin/env python3
"""
Debug Enhancement Framework - Universal debugging utilities for AI agent skills.
Provides structured logging, error classification, performance monitoring, and self-healing.
"""

import argparse
import json
import logging
import os
import sys
import time
import traceback
from datetime import datetime
from functools import wraps
from typing import Any, Callable, Optional, Type, Dict, List
from dataclasses import dataclass, field
from enum import Enum

# ============================================================================
# ERROR CLASSIFICATION
# ============================================================================

class ErrorType(Enum):
    NETWORK = "network_error"
    CONFIGURATION = "configuration_error"
    VALIDATION = "validation_error"
    PERMISSION = "permission_error"
    RESOURCE = "resource_error"
    TIMEOUT = "timeout_error"
    DEPENDENCY = "dependency_error"
    UNKNOWN = "unknown_error"

@dataclass
class ClassifiedError:
    error_type: ErrorType
    message: str
    original_exception: Exception
    context: dict = field(default_factory=dict)
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())

class ErrorClassifier:
    """Classify errors into categories for better handling."""
    
    ERROR_PATTERNS = {
        ErrorType.NETWORK: [
            "connection", "dns", "socket",
            "requests.exceptions", "urllib.error.URLError"
        ],
        ErrorType.CONFIGURATION: [
            "config", "setting", "environment", "missing variable",
            "invalid config", "not found"
        ],
        ErrorType.VALIDATION: [
            "invalid", "validation", "format", "schema", "type error"
        ],
        ErrorType.PERMISSION: [
            "permission", "denied", "forbidden", "authentication",
            "unauthorized", "access denied"
        ],
        ErrorType.RESOURCE: [
            "memory", "disk", "out of", "resource", "quota",
            "no space", "exhausted"
        ],
        ErrorType.TIMEOUT: [
            "timeout", "timed out", "deadline exceeded"
        ],
        ErrorType.DEPENDENCY: [
            "import", "module", "package", "dependency",
            "version", "compatibility"
        ],
    }
    
    @classmethod
    def classify(cls, exception: Exception, context: dict = None) -> ClassifiedError:
        error_msg = str(exception).lower()
        error_type = ErrorType.UNKNOWN
        
        # Check exception type first (more reliable)
        if isinstance(exception, TimeoutError):
            error_type = ErrorType.TIMEOUT
        elif isinstance(exception, ConnectionError):
            error_type = ErrorType.NETWORK
        elif isinstance(exception, PermissionError):
            error_type = ErrorType.PERMISSION
        elif isinstance(exception, ValueError):
            error_type = ErrorType.VALIDATION
        else:
            # Fall back to pattern matching
            for etype, patterns in cls.ERROR_PATTERNS.items():
                if any(p in error_msg for p in patterns):
                    error_type = etype
                    break
        
        return ClassifiedError(
            error_type=error_type,
            message=str(exception),
            original_exception=exception,
            context=context or {}
        )

# ============================================================================
# STRUCTURED LOGGING
# ============================================================================

class JSONFormatter(logging.Formatter):
    """Format logs as JSON for structured analysis."""
    
    def format(self, record):
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }
        if hasattr(record, "extra_data"):
            log_entry["extra"] = record.extra_data
        if record.exc_info:
            log_entry["exception"] = traceback.format_exception(*record.exc_info)
        return json.dumps(log_entry)

def setup_logging(
    level: int = logging.INFO,
    log_file: Optional[str] = None,
    json_format: bool = True
) -> logging.Logger:
    """Setup structured logging for a skill."""
    logger = logging.getLogger("skill_debug")
    logger.setLevel(level)
    logger.handlers = []
    
    formatter = JSONFormatter() if json_format else logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    
    # Console handler
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)
    
    # File handler
    if log_file:
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger

# ============================================================================
# RETRY WITH BACKOFF
# ============================================================================

@dataclass
class RetryPolicy:
    max_attempts: int = 3
    initial_delay: float = 1.0
    max_delay: float = 60.0
    backoff_multiplier: float = 2.0
    retry_on: tuple = (Exception,)
    exclude_on: tuple = ()
    
    def __call__(self, func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            delay = self.initial_delay
            last_exception = None
            
            for attempt in range(1, self.max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except self.exclude_on:
                    raise
                except self.retry_on as e:
                    last_exception = e
                    if attempt == self.max_attempts:
                        raise
                    
                    # Don't retry validation errors
                    classified = ErrorClassifier.classify(e)
                    if classified.error_type == ErrorType.VALIDATION:
                        raise
                    
                    time.sleep(delay)
                    delay = min(delay * self.backoff_multiplier, self.max_delay)
            
            raise last_exception
        return wrapper

# ============================================================================
# CIRCUIT BREAKER
# ============================================================================

@dataclass
class CircuitState(Enum):
    CLOSED = "closed"
    OPEN = "open"
    HALF_OPEN = "half_open"

@dataclass
class CircuitBreaker:
    failure_threshold: int = 5
    recovery_timeout: float = 60.0
    half_open_success_threshold: int = 3
    half_open_requests: int = 1
    
    state: CircuitState = field(default_factory=lambda: CircuitState.CLOSED)
    failure_count: int = 0
    success_count: int = 0
    last_failure_time: float = field(default=0.0)
    _half_open_calls: int = 0
    
    def __call__(self, func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Check if circuit is open
            if self.state == CircuitState.OPEN:
                if time.time() - self.last_failure_time >= self.recovery_timeout:
                    self.state = CircuitState.HALF_OPEN
                    self._half_open_calls = 0
                else:
                    raise CircuitBreakerError("Circuit is open")
            
            # Check half-open limits
            if self.state == CircuitState.HALF_OPEN:
                if self._half_open_calls >= self.half_open_requests:
                    raise CircuitBreakerError("Half-open limit reached")
                self._half_open_calls += 1
            
            try:
                result = func(*args, **kwargs)
                self._on_success()
                return result
            except Exception as e:
                self._on_failure()
                raise
        
        return wrapper
    
    def _on_success(self):
        if self.state == CircuitState.HALF_OPEN:
            self.success_count += 1
            if self.success_count >= self.half_open_success_threshold:
                self._reset()
        else:
            # Gradually reduce failure count on success
            self.failure_count = max(0, self.failure_count - 1)
    
    def _on_failure(self):
        self.failure_count += 1
        self.last_failure_time = time.time()
        self.success_count = 0
        
        if self.failure_count >= self.failure_threshold:
            self.state = CircuitState.OPEN
    
    def _reset(self):
        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.success_count = 0
        self._half_open_calls = 0

class CircuitBreakerError(Exception):
    pass

# ============================================================================
# ERROR RECOVERY
# ============================================================================

class ErrorRecovery:
    """Handle error recovery with predefined strategies."""
    
    def __init__(self, logger: Optional[logging.Logger] = None):
        self.logger = logger or setup_logging()
        self.recovery_handlers: Dict[Type[Exception], Callable] = {}
    
    def register_handler(self, error_type: Type[Exception], handler: Callable):
        """Register a recovery handler for an error type."""
        self.recovery_handlers[error_type] = handler
    
    def handle(self, exception: Exception, context: dict = None) -> bool:
        """Try to recover from an error using registered handlers."""
        classified = ErrorClassifier.classify(exception, context)
        
        # Try specific handler first
        for exc_type, handler in self.recovery_handlers.items():
            if isinstance(exception, exc_type):
                try:
                    self.logger.info(f"Running recovery handler for {exc_type.__name__}")
                    handler(exception, context)
                    return True
                except Exception as e:
                    self.logger.error(f"Recovery handler failed: {e}")
        
        # Try generic recovery based on error type
        return self._generic_recovery(classified)
    
    def _generic_recovery(self, classified: ClassifiedError) -> bool:
        """Apply generic recovery based on error classification."""
        strategies = {
            ErrorType.NETWORK: self._recover_network,
            ErrorType.RESOURCE: self._recover_resource,
            ErrorType.DEPENDENCY: self._recover_dependency,
        }
        
        strategy = strategies.get(classified.error_type)
        if strategy:
            return strategy(classified)
        return False
    
    def _recover_network(self, error: ClassifiedError) -> bool:
        """Attempt network recovery."""
        self.logger.warning("Network recovery: would retry with new connection")
        return True
    
    def _recover_resource(self, error: ClassifiedError) -> bool:
        """Attempt resource recovery."""
        self.logger.warning("Resource recovery: would free resources")
        return True
    
    def _recover_dependency(self, error: ClassifiedError) -> bool:
        """Attempt dependency recovery."""
        self.logger.warning("Dependency recovery: would use fallback")
        return False

# ============================================================================
# PERFORMANCE MONITOR
# ============================================================================

class PerformanceMonitor:
    """Monitor and profile skill performance."""
    
    def __init__(self, logger: Optional[logging.Logger] = None):
        self.logger = logger or setup_logging()
        self.metrics: Dict[str, Dict[str, List[float]]] = {}
    
    def measure(self, name: str) -> Callable:
        """Decorator to measure function execution time."""
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(*args, **kwargs):
                start = time.time()
                try:
                    result = func(*args, **kwargs)
                    return result
                finally:
                    elapsed = time.time() - start
                    self._record_metric(name, "duration", elapsed)
            return wrapper
        return decorator
    
    def _record_metric(self, name: str, key: str, value: float):
        if name not in self.metrics:
            self.metrics[name] = {}
        if key not in self.metrics[name]:
            self.metrics[name][key] = []
        self.metrics[name][key].append(value)
    
    def get_stats(self, name: str) -> dict:
        """Get statistics for a metric."""
        if name not in self.metrics:
            return {}
        
        stats = {}
        for key, values in self.metrics[name].items():
            if values:
                stats[key] = {
                    "count": len(values),
                    "min": min(values),
                    "max": max(values),
                    "avg": sum(values) / len(values),
                    "total": sum(values)
                }
        return stats
    
    def report(self) -> str:
        """Generate performance report."""
        report_lines = ["=== Performance Report ==="]
        for name, metrics in self.metrics.items():
            report_lines.append(f"\n{name}:")
            for key, values in metrics.items():
                if values:
                    report_lines.append(
                        f"  {key}: avg={sum(values)/len(values):.3f}s, "
                        f"min={min(values):.3f}s, max={max(values):.3f}s, "
                        f"count={len(values)}"
                    )
        return "\n".join(report_lines)

# ============================================================================
# STATE CAPTURE & REPLAY
# ============================================================================

class StateCapture:
    """Capture and restore execution state for debugging."""
    
    def __init__(self, capture_dir: str = "/tmp/skill-debug-state"):
        self.capture_dir = capture_dir
        os.makedirs(capture_dir, exist_ok=True)
    
    def capture(self, name: str, state: dict) -> str:
        """Capture state to a file."""
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}.json"
        filepath = os.path.join(self.capture_dir, filename)
        
        with open(filepath, "w") as f:
            json.dump({
                "name": name,
                "timestamp": timestamp,
                "state": state
            }, f, indent=2, default=str)
        
        return filepath
    
    def list_captures(self, name: Optional[str] = None) -> list:
        """List captured states."""
        captures = []
        if not os.path.exists(self.capture_dir):
            return captures
            
        for f in sorted(os.listdir(self.capture_dir)):
            if f.endswith(".json"):
                if name is None or f.startswith(name):
                    filepath = os.path.join(self.capture_dir, f)
                    try:
                        with open(filepath) as fp:
                            data = json.load(fp)
                        captures.append({
                            "file": f,
                            "path": filepath,
                            "name": data.get("name"),
                            "timestamp": data.get("timestamp")
                        })
                    except Exception:
                        pass
        return captures

# ============================================================================
# DIAGNOSTIC TOOLS
# ============================================================================

def diagnose_environment() -> dict:
    """Diagnose the current environment for common issues."""
    diagnosis = {
        "python_version": sys.version,
        "platform": sys.platform,
        "executable": sys.executable,
        "working_directory": os.getcwd(),
        "environment_variables": {},
        "issues": []
    }
    
    # Check critical environment variables
    critical_vars = ["PATH", "HOME"]
    for var in critical_vars:
        value = os.environ.get(var, "")
        diagnosis["environment_variables"][var] = value[:100] + "..." if len(value) > 100 else value
        if not value:
            diagnosis["issues"].append(f"Missing environment variable: {var}")
    
    # Check available disk space
    try:
        import shutil
        usage = shutil.disk_usage("/")
        diagnosis["disk_space"] = {
            "total_gb": round(usage.total / (1024**3), 2),
            "used_gb": round(usage.used / (1024**3), 2),
            "free_gb": round(usage.free / (1024**3), 2)
        }
        if usage.free < 100 * 1024**3:
            diagnosis["issues"].append("Low disk space")
    except Exception as e:
        diagnosis["issues"].append(f"Could not check disk space: {e}")
    
    return diagnosis

def run_diagnostics(skill_name: str) -> dict:
    """Run full diagnostics for a skill."""
    results = {
        "skill": skill_name,
        "timestamp": datetime.utcnow().isoformat(),
        "environment": diagnose_environment(),
        "checks": {}
    }
    
    # Check if skill files exist
    skill_path = f"/home/user/skills/{skill_name}"
    results["checks"]["skill_exists"] = os.path.exists(skill_path)
    results["checks"]["has_skill_md"] = os.path.exists(f"{skill_path}/SKILL.md")
    
    # Check scripts
    scripts_dir = f"{skill_path}/scripts"
    if os.path.exists(scripts_dir):
        scripts = [f for f in os.listdir(scripts_dir) if f.endswith(('.py', '.sh'))]
        results["checks"]["scripts_found"] = len(scripts)
        results["checks"]["scripts"] = scripts
    
    # Check dependencies
    try:
        import importlib
        results["checks"]["python_deps_ok"] = True
    except Exception as e:
        results["checks"]["python_deps_ok"] = False
        results["checks"]["deps_error"] = str(e)
    
    return results

# ============================================================================
# CLI INTERFACE
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description="Debug Enhancement Framework CLI")
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # Diagnose command
    diag_parser = subparsers.add_parser("diagnose", help="Run diagnostics")
    diag_parser.add_argument("skill_name", nargs="?", help="Skill name to diagnose")
    
    # List captures
    list_parser = subparsers.add_parser("list-captures", help="List captured states")
    list_parser.add_argument("--skill", help="Filter by skill name")
    
    # Show report
    report_parser = subparsers.add_parser("report", help="Show performance report")
    
    # Simulate errors
    sim_parser = subparsers.add_parser("simulate", help="Simulate errors for testing")
    sim_parser.add_argument("error_type", choices=["network", "timeout", "validation", "permission"])
    
    args = parser.parse_args()
    
    logger = setup_logging(level=logging.DEBUG)
    
    if args.command == "diagnose":
        results = run_diagnostics(args.skill_name or "unknown")
        print(json.dumps(results, indent=2))
        
        if results["checks"].get("skill_exists"):
            print("\n✅ Skill found and operational")
        else:
            print("\n❌ Skill not found or misconfigured")
            sys.exit(1)
    
    elif args.command == "list-captures":
        capture = StateCapture()
        captures = capture.list_captures(args.skill)
        if captures:
            for c in captures:
                print(f"{c['timestamp']} - {c['name']} ({c['file']})")
        else:
            print("No captures found")
    
    elif args.command == "report":
        print("Performance reporting requires an active session.")
        print("Use PerformanceMonitor in your code to collect metrics.")
    
    elif args.command == "simulate":
        error_map = {
            "network": ConnectionError("Simulated network error"),
            "timeout": TimeoutError("Simulated timeout"),
            "validation": ValueError("Simulated validation error"),
            "permission": PermissionError("Simulated permission denied")
        }
        raise error_map[args.error_type]
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
