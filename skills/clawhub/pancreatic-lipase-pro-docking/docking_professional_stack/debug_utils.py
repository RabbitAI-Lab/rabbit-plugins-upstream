#!/usr/bin/env python3
"""debug_utils.py — debugging & observability toolkit for the hPL docking stack.

Best practices implemented (audit 2026-08-03; sources: Python logging docs,
exception-handling guides, PEP 8, scientific-software FAIR practices):

1. Structured logging with levels + timestamps (not scattered prints).
2. Domain-specific exception classes chained with `raise ... from e` so the
   original traceback survives (no silent context loss).
3. Fail-fast validation helpers for inputs and internal invariants.
4. Global exception hook: any uncaught exception is logged with a full
   traceback (no silent failures).
5. Environment self-check (`--check` mode) printing versions of every tool
   and module — the first thing to run when a job misbehaves.
6. Reproducibility: every run records versions.json (python, vina, rdkit,
   meeko, gemmi, numpy) + the full command line next to its results.
7. run_cmd: every external command is logged; on failure the exact command
   plus stdout/stderr tails are logged for reproduction.
"""
import json
import logging
import os
import shutil
import subprocess
import sys
import traceback
from pathlib import Path

LOG = logging.getLogger("hpl")


# --- domain exceptions -------------------------------------------------------
class DockingError(Exception):
    """Base error for the docking pipeline (fail-closed)."""


class PrepError(DockingError):
    """Ligand/receptor preparation failed."""


class ConfigError(DockingError):
    """Bad configuration / environment (missing tool, bad file)."""


class ValidationError(DockingError):
    """Input validation failed (fail fast before expensive compute)."""


# --- logging setup -----------------------------------------------------------
def setup_logging(debug=False, log_file=None, name="hpl"):
    """Configure module loggers; console (stderr) + optional file handler."""
    logger = logging.getLogger(name)
    level = logging.DEBUG if debug else logging.INFO
    logger.setLevel(level)
    fmt = "%(asctime)s | %(levelname)-7s | %(message)s"
    formatter = logging.Formatter(fmt, datefmt="%Y-%m-%d %H:%M:%S")
    if not logger.handlers:
        sh = logging.StreamHandler(sys.stderr)
        sh.setFormatter(formatter)
        logger.addHandler(sh)
    if log_file:
        Path(log_file).parent.mkdir(parents=True, exist_ok=True)
        fh = logging.FileHandler(log_file, encoding="utf-8")
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    logging.captureWarnings(True)
    return logger


def install_exception_hook(logger=None):
    """Global sys.excepthook: log any uncaught exception with full traceback."""
    lg = logger or LOG

    def hook(exc_type, exc_value, exc_tb):
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc_value, exc_tb)
            return
        msg = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
        lg.error("UNCAUGHT EXCEPTION:\n%s", msg)

    sys.excepthook = hook


# --- validation helpers ------------------------------------------------------
def require(cond, message, exc=ValidationError):
    """Fail fast with a domain-specific error when cond is False."""
    if not cond:
        raise exc(message)


def require_file(path, what="path"):
    p = Path(path)
    if not p.exists():
        raise ConfigError(f"{what} not found: {p}")
    if p.stat().st_size == 0:
        raise ConfigError(f"{what} is empty: {p}")
    return p


# --- environment self-check --------------------------------------------------
def env_check(extra=None):
    """Diagnostic report of the runtime environment (for --check / bug reports)."""
    report = {"python": sys.version.split()[0],
              "script": Path(sys.argv[0]).name,
              "cwd": os.getcwd()}
    for binname in ("vina", "obabel", "mk_prepare_receptor.py", "mk_prepare_ligand.py"):
        report[binname] = shutil.which(binname) or None
    for mod in ("rdkit", "meeko", "gemmi", "numpy", "scipy", "matplotlib", "pytest"):
        try:
            m = __import__(mod)
            report[mod] = getattr(m, "__version__", "present")
        except Exception as e:
            report[mod] = f"MISSING ({type(e).__name__})"
    if extra:
        report.update(extra)
    return report


def print_env_check(extra=None):
    """Pretty-print env_check() (exit code 0 if all critical tools present)."""
    rep = env_check(extra)
    critical = ("vina", "rdkit", "meeko", "gemmi")
    ok = True
    print("=== environment self-check ===")
    for k, v in rep.items():
        mark = ""
        if k in critical:
            if v is None or str(v).startswith("MISSING"):
                mark = "  <-- REQUIRED"
                ok = False
            else:
                mark = "  ✓"
        print(f"  {k:22s} {v}{mark}")
    print("RESULT:", "OK" if ok else "PROBLEM — see missing REQUIRED entries")
    return 0 if ok else 1


# --- process execution with logging ------------------------------------------
def run_cmd(cmd, timeout=None, cwd=None, logger=None, check=True):
    """Run a subprocess; log the command; on failure log full context and
    raise DockingError (fail-closed) with the exact command for reproduction."""
    lg = logger or LOG
    cmdstr = " ".join(map(str, cmd))
    lg.info("RUN: %s", cmdstr)
    try:
        p = subprocess.run(cmd, text=True, capture_output=True, timeout=timeout, cwd=cwd)
    except subprocess.TimeoutExpired as e:
        lg.error("TIMEOUT after %ss: %s", timeout, cmdstr)
        raise DockingError(f"command timed out after {timeout}s: {cmdstr}") from e
    except OSError as e:
        lg.error("OSERROR running: %s (%s)", cmdstr, e)
        raise DockingError(f"could not execute: {cmdstr} ({e})") from e
    if p.returncode != 0:
        lg.error("FAILED rc=%s: %s\n  stdout tail: %s\n  stderr tail: %s",
                 p.returncode, cmdstr, p.stdout[-400:].strip(), p.stderr[-400:].strip())
        if check:
            raise DockingError(f"command failed (rc={p.returncode}): {cmdstr}\n"
                               f"stderr: {p.stderr[-400:].strip()}")
    return p.returncode, p.stdout, p.stderr


# --- reproducibility ---------------------------------------------------------
def record_versions(outdir, extra=None):
    """Write versions.json (env + extra params) next to results."""
    out = Path(outdir) / "versions.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    data = env_check(extra)
    out.write_text(json.dumps(data, indent=2))
    LOG.info("reproducibility record written: %s", out)
    return out
