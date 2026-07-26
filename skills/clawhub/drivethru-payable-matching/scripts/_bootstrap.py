"""Self-bootstrap paymatch.py's Python dependencies with ``uv``.

Why this exists
---------------
The skill declares its deps in ``SKILL.md`` frontmatter
(``metadata.openclaw.install.uv``) for hosts that honor it. **Not every host
does** — and a user may run the script directly — so the agent hit
``ModuleNotFoundError: No module named 'anyio'`` (anyio ships with ``mcp``) and
could not run at all. This makes the script self-contained instead: on a missing
import we build a cached virtualenv in the skill data dir with ``uv`` and re-exec
into it. Steady state is a few ``find_spec`` probes (near-zero) — only the
*first* run in a fresh container pays the install, and it lands in the
persistent data dir, so later runs are a no-op.

Everything is ensured **up front**, before any MCP work, so the script never
re-execs mid-run (which would restart an in-flight Odoo MCP session).

Usage (top of paymatch.py, BEFORE importing anyio / mcp / fitz)::

    import _bootstrap
    _bootstrap.ensure()
    import anyio                 # now guaranteed importable
    from mcp import ClientSession
"""

from __future__ import annotations

import importlib.util
import os
import shutil
import subprocess
import sys
from pathlib import Path

# Everything paymatch.py needs at runtime: the MCP transport (``mcp`` pulls in
# ``anyio``) plus the PDF text/render stack. Kept in one tier and ensured up
# front so a single re-exec covers every action.
REQUIREMENTS = ["mcp>=1.9.0", "pymupdf>=1.24", "pypdf>=4.0"]

# (label, [importable module names that satisfy it]). ``anyio`` rides in with
# ``mcp``; PyMuPDF exposes both ``pymupdf`` (new) and ``fitz`` (classic).
_PROBE = [
    ("mcp", ["mcp"]),
    ("anyio", ["anyio"]),
    ("pymupdf", ["pymupdf", "fitz"]),
    ("pypdf", ["pypdf"]),
]


def _data_dir() -> Path:
    env = (os.getenv("PAYMATCH_DATA_DIR") or "").strip()
    if env:
        return Path(env).expanduser()
    return Path.home() / ".drivethru" / "paymatch"


_VENV = _data_dir() / ".venv"


def _venv_python() -> Path:
    if os.name == "nt":
        return _VENV / "Scripts" / "python.exe"
    return _VENV / "bin" / "python"


def _in_our_venv() -> bool:
    try:
        return Path(sys.prefix).resolve() == _VENV.resolve()
    except OSError:
        return False


def _importable(names: list[str]) -> bool:
    for n in names:
        try:
            if importlib.util.find_spec(n) is not None:
                return True
        except (ImportError, ValueError):
            continue
    return False


def _missing() -> list[str]:
    return [label for label, mods in _PROBE if not _importable(mods)]


def ensure() -> None:
    """Guarantee paymatch's deps import; install them via ``uv`` if not.

    No-op when the host already provides them (zero overhead — the common case
    on hosts that honor ``install.uv``). Otherwise create/reuse a cached venv in
    the data dir, install into it, and re-exec the current command inside it so
    the imports resolve on the second entry.
    """
    if not _missing():
        return

    # We already re-exec'd into our managed venv and deps *still* aren't
    # importable — the install genuinely failed; don't loop forever.
    if _in_our_venv():
        raise SystemExit(
            "ERROR: paymatch dependencies still missing after bootstrap ("
            + ", ".join(_missing())
            + "). Install manually with:  uv pip install "
            + " ".join(REQUIREMENTS)
        )

    uv = shutil.which("uv")
    if not uv:
        raise SystemExit(
            "ERROR: paymatch needs Python packages ["
            + ", ".join(_missing())
            + "] and `uv` is not on PATH. Install uv "
            "(https://docs.astral.sh/uv/) or run:  pip install "
            + " ".join(REQUIREMENTS)
        )

    py = _venv_python()
    # uv chatter goes to stderr so the script's JSON stdout stays clean.
    if not py.exists():
        _VENV.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run([uv, "venv", str(_VENV)], check=True, stdout=sys.stderr)
    subprocess.run(
        [uv, "pip", "install", "--python", str(py), *REQUIREMENTS],
        check=True,
        stdout=sys.stderr,
    )

    # Re-run the exact same command under the venv interpreter; on that second
    # entry ensure() finds everything present and returns immediately.
    os.execv(str(py), [str(py), *sys.argv])
