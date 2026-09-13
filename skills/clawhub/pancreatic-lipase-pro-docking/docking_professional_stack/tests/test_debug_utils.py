"""Tests for debug_utils.py — logging, exceptions, env-check, run_cmd."""
import sys

import debug_utils as du


def test_domain_exceptions_hierarchy():
    assert issubclass(du.PrepError, du.DockingError)
    assert issubclass(du.ConfigError, du.DockingError)
    assert issubclass(du.ValidationError, du.DockingError)
    assert issubclass(du.DockingError, Exception)


def test_require_passes_and_fails():
    du.require(True, "ok")
    try:
        du.require(False, "boom", exc=du.ValidationError)
        assert False, "should have raised"
    except du.ValidationError as e:
        assert "boom" in str(e)


def test_require_file(tmp_path):
    f = tmp_path / "x.csv"
    f.write_text("a,b\n1,2\n")
    assert du.require_file(f) == f
    try:
        du.require_file(tmp_path / "missing.csv")
        assert False
    except du.ConfigError:
        pass
    empty = tmp_path / "empty.csv"
    empty.write_text("")
    try:
        du.require_file(empty)
        assert False
    except du.ConfigError:
        pass


def test_setup_logging_file(tmp_path):
    logf = tmp_path / "run.log"
    lg = du.setup_logging(debug=True, log_file=str(logf))
    lg.info("hello %d", 42)
    # flush handlers
    for h in lg.handlers:
        h.flush()
    content = logf.read_text()
    assert "hello 42" in content
    assert "INFO" in content


def test_exception_hook_logs(caplog):
    """The global hook must log uncaught exceptions (no silent failures)."""
    du.setup_logging(debug=True)
    du.install_exception_hook()
    try:
        raise ValueError("simulated crash")
    except ValueError:
        exc_type, exc_value, exc_tb = sys.exc_info()
    import logging
    with caplog.at_level(logging.ERROR, logger="hpl"):
        sys.excepthook(exc_type, exc_value, exc_tb)
    assert "UNCAUGHT EXCEPTION" in caplog.text
    assert "simulated crash" in caplog.text


def test_run_cmd_failure_raises():
    try:
        du.run_cmd([sys.executable, "-c", "raise SystemExit(3)"])
        assert False, "should raise DockingError"
    except du.DockingError as e:
        assert "rc=3" in str(e)




def test_env_check_keys():
    rep = du.env_check()
    for key in ("python", "vina", "rdkit", "meeko", "gemmi", "numpy"):
        assert key in rep


def test_run_cmd_ok():
    rc, out, err = du.run_cmd([sys.executable, "-c", "print('hi')"], check=False)
    assert rc == 0
    assert "hi" in out


def test_record_versions(tmp_path):
    out = du.record_versions(tmp_path, {"seed": 42})
    import json
    d = json.loads(out.read_text())
    assert d["seed"] == 42
    assert "python" in d
