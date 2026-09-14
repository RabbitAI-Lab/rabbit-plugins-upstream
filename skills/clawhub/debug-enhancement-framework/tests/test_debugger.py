#!/usr/bin/env python3
"""Tests for Debug Enhancement Framework."""

import os
import sys
import tempfile
import unittest
from pathlib import Path
from datetime import datetime, timezone

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from debugger import (
    ErrorClassifier, ClassifiedError, ErrorType,
    setup_logging, RetryPolicy, CircuitBreaker, CircuitState, CircuitBreakerError,
    PerformanceMonitor, StateCapture, diagnose_environment, run_diagnostics
)
from recovery import RecoveryStrategies, AutoHealer

class TestErrorClassifier(unittest.TestCase):
    def test_network_error(self):
        err = ErrorClassifier.classify(ConnectionError("connection refused"))
        self.assertEqual(err.error_type, ErrorType.NETWORK)
    
    def test_timeout_error(self):
        err = ErrorClassifier.classify(TimeoutError("timed out"))
        self.assertEqual(err.error_type, ErrorType.TIMEOUT)
    
    def test_validation_error(self):
        err = ErrorClassifier.classify(ValueError("invalid input"))
        self.assertEqual(err.error_type, ErrorType.VALIDATION)
    
    def test_permission_error(self):
        err = ErrorClassifier.classify(PermissionError("access denied"))
        self.assertEqual(err.error_type, ErrorType.PERMISSION)
    
    def test_unknown_error(self):
        err = ErrorClassifier.classify(Exception("something"))
        self.assertEqual(err.error_type, ErrorType.UNKNOWN)

class TestRetryPolicy(unittest.TestCase):
    def test_successful_first_try(self):
        call_count = 0
        
        @RetryPolicy(max_attempts=3)
        def succeeds():
            nonlocal call_count
            call_count += 1
            return "success"
        
        result = succeeds()
        self.assertEqual(result, "success")
        self.assertEqual(call_count, 1)
    
    def test_retries_on_failure(self):
        call_count = 0
        
        @RetryPolicy(max_attempts=3, retry_on=(RuntimeError,))
        def fails_then_succeeds():
            nonlocal call_count
            call_count += 1
            if call_count < 3:
                raise RuntimeError("temporary failure")
            return "success"
        
        result = fails_then_succeeds()
        self.assertEqual(result, "success")
        self.assertEqual(call_count, 3)

class TestCircuitBreaker(unittest.TestCase):
    def test_closes_on_success(self):
        breaker = CircuitBreaker(failure_threshold=3)
        
        @breaker
        def succeeds():
            return "ok"
        
        result = succeeds()
        self.assertEqual(result, "ok")
        self.assertEqual(breaker.state, CircuitState.CLOSED)
    
    def test_opens_on_failure(self):
        breaker = CircuitBreaker(failure_threshold=2)
        
        @breaker
        def fails():
            raise RuntimeError("fail")
        
        # First failure
        with self.assertRaises(RuntimeError):
            fails()
        self.assertEqual(breaker.state, CircuitState.CLOSED)
        self.assertEqual(breaker.failure_count, 1)
        
        # BUG FIXED (v2.1.0): this used to assert CircuitBreakerError on the
        # SECOND call. That passed only because @dataclass had been applied to
        # the CircuitState Enum, which generated an __eq__ making EVERY state
        # compare equal - so `if self.state == CircuitState.OPEN` was always
        # true and the breaker fail-fasted from the first failure onward. The
        # state machine was inert and this test encoded the broken behaviour.
        # Correct semantics: the call that crosses the threshold still
        # propagates the underlying error and OPENS the circuit; only the NEXT
        # call fails fast.
        with self.assertRaises(RuntimeError):
            fails()
        self.assertEqual(breaker.failure_count, 2)
        self.assertEqual(breaker.state, CircuitState.OPEN)

        # third call: now it fails fast without invoking the function
        with self.assertRaises(CircuitBreakerError):
            fails()
        self.assertEqual(breaker.state, CircuitState.OPEN)

    def test_states_are_distinct(self):
        """Regression: @dataclass on the Enum made all members compare equal."""
        self.assertNotEqual(CircuitState.CLOSED, CircuitState.OPEN)
        self.assertNotEqual(CircuitState.OPEN, CircuitState.HALF_OPEN)
        self.assertNotEqual(CircuitState.CLOSED, CircuitState.HALF_OPEN)
        self.assertFalse(hasattr(CircuitState, "__dataclass_fields__"),
                         "CircuitState must not be a dataclass")

    def test_open_circuit_does_not_invoke_the_function(self):
        """Fail-fast must actually skip the protected call."""
        breaker = CircuitBreaker(failure_threshold=1, recovery_timeout=60.0)
        calls = {"n": 0}

        @breaker
        def fails():
            calls["n"] += 1
            raise RuntimeError("fail")

        with self.assertRaises(RuntimeError):
            fails()
        self.assertEqual(calls["n"], 1)
        with self.assertRaises(CircuitBreakerError):
            fails()
        self.assertEqual(calls["n"], 1, "open circuit still invoked the function")
    
    def test_half_open_transition(self):
        breaker = CircuitBreaker(
            failure_threshold=2,
            recovery_timeout=0.1,
            half_open_success_threshold=1
        )
        
        @breaker
        def flaky():
            if breaker._half_open_calls == 0:
                raise RuntimeError("fail")
            return "ok"
        
        for _ in range(2):
            try:
                flaky()
            except RuntimeError:
                pass
        
        self.assertEqual(breaker.state, CircuitState.OPEN)
        
        import time
        time.sleep(0.2)
        
        result = flaky()
        self.assertEqual(result, "ok")
        self.assertEqual(breaker.state, CircuitState.CLOSED)

class TestPerformanceMonitor(unittest.TestCase):
    def test_measure_decorator(self):
        monitor = PerformanceMonitor()
        
        @monitor.measure("test_func")
        def slow_func():
            import time
            time.sleep(0.01)
            return "result"
        
        result = slow_func()
        self.assertEqual(result, "result")
        
        stats = monitor.get_stats("test_func")
        self.assertIn("duration", stats)
        self.assertGreater(stats["duration"]["total"], 0)

class TestStateCapture(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_capture_state(self):
        capture = StateCapture(capture_dir=self.temp_dir)
        
        state = {"key": "value", "number": 42}
        filepath = capture.capture("test", state)
        
        self.assertTrue(os.path.exists(filepath))
        self.assertTrue(filepath.startswith(self.temp_dir))
        
        with open(filepath) as f:
            import json
            data = json.load(f)
        
        self.assertEqual(data["name"], "test")
        self.assertEqual(data["state"]["key"], "value")

class TestDiagnoseEnvironment(unittest.TestCase):
    def test_diagnose_returns_dict(self):
        result = diagnose_environment()
        self.assertIsInstance(result, dict)
        self.assertIn("python_version", result)
        self.assertIn("platform", result)
        self.assertIn("issues", result)

class TestRecoveryStrategies(unittest.TestCase):
    def test_cleanup_temp_files(self):
        temp_dir = tempfile.mkdtemp()
        try:
            Path(temp_dir, "test.tmp").touch()
            Path(temp_dir, "test.cache").touch()
            
            result = RecoveryStrategies.cleanup_temp_files(
                ["*.tmp", "*.cache"],
                [temp_dir]
            )
            
            self.assertTrue(result.success)
            self.assertGreater(result.recovery_time, 0)
        finally:
            import shutil
            shutil.rmtree(temp_dir, ignore_errors=True)

class TestAutoHealer(unittest.TestCase):
    def test_heal_network_error(self):
        healer = AutoHealer("test-skill")
        
        try:
            raise ConnectionError("network failed")
        except Exception as e:
            result = healer.heal(e)
            self.assertTrue(result.success)
    
    def test_health_report(self):
        healer = AutoHealer("test-skill")
        report = healer.get_health_report()
        
        self.assertEqual(report["skill"], "test-skill")
        self.assertEqual(report["total_healing_attempts"], 0)
        self.assertEqual(report["success_rate"], 0)

if __name__ == "__main__":
    unittest.main()
