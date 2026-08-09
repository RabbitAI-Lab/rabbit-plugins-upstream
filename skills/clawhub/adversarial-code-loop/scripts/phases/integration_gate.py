"""
INTEGRATION GATE: manifest-driven cross-repo test runner.

Reads the manifest written by P14 (``scripts/repos.manifest.yaml``) — one
entry per adversarial-* skill repo with its ``test_cmd`` — and runs each
repo's test command as a subprocess. Every run is bounded by a per-repo
timeout (manifest ``timeout``, default 120s) and an overall wall-clock budget
(default 300s) shared across all repos. A timeout kills the whole process
group so a hung test runner cannot leave orphan children behind.

``run_integration_gate(workspace_root) -> {"per_repo": [...], "gate_passed":
bool, "gate_duration_s": float}``.

P16: a failing gate is an infrastructure failure, not a code-quality
rejection -- the cross-repo test run itself could not be verified clean, so
``integration_gate_exit_code`` maps it to the stable ``EXIT_INFRA`` CI
contract (:data:`adversarial_common.runner.CI_EXIT_INFRASTRUCTURE`) rather
than a REJECT/blocking code.
"""
import os
import select
import signal
import subprocess
import time

import yaml

from adversarial_common import runner

__all__ = ["run_integration_gate", "integration_gate_exit_code"]

DEFAULT_REPO_TIMEOUT = 120
DEFAULT_GLOBAL_TIMEOUT = 300
MAX_OUTPUT_CHARS = 32 * 1024
_TRUNCATION_MARKER = "\n... [output truncated] ...\n"

_HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_MANIFEST_PATH = os.path.join(os.path.dirname(_HERE), "repos.manifest.yaml")


def _load_manifest(manifest_path: str) -> list:
    with open(manifest_path, "r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or []
    if not isinstance(data, list):
        raise ValueError(f"manifest must be a list of repo entries: {manifest_path}")
    return data


def _drain_once(fd, chunks: list, total_len: int, truncated: bool) -> tuple:
    """Read a single chunk from ``fd``, keeping at most MAX_OUTPUT_CHARS.

    Reads happen in fixed-size chunks so a noisy command's output is bounded
    in memory as it arrives, rather than being buffered in full before a
    truncation pass. Returns ``(eof, total_len, truncated)``.
    """
    data = os.read(fd, 65536)
    if not data:
        return True, total_len, truncated
    if total_len < MAX_OUTPUT_CHARS:
        room = MAX_OUTPUT_CHARS - total_len
        chunks.append(data[:room])
        if len(data) > room:
            truncated = True
    else:
        truncated = True
    total_len += len(data)
    return False, total_len, truncated


def _run_repo(name: str, cwd: str, test_cmd: str, timeout: float) -> dict:
    start = time.monotonic()
    try:
        proc = subprocess.Popen(
            ["/bin/bash", "-c", test_cmd],
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            start_new_session=True,
        )
    except OSError as exc:
        return {
            "name": name, "status": "fail", "duration": time.monotonic() - start,
            "output": str(exc), "output_truncated": False, "timed_out": False,
        }

    deadline = start + max(timeout, 0)
    fd = proc.stdout.fileno()
    chunks: list = []
    total_len = 0
    truncated = False
    timed_out = False
    try:
        while True:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                timed_out = True
                break
            ready, _, _ = select.select([fd], [], [], remaining)
            if not ready:
                continue
            eof, total_len, truncated = _drain_once(fd, chunks, total_len, truncated)
            if eof:
                break
    finally:
        if timed_out:
            try:
                os.killpg(proc.pid, signal.SIGKILL)
            except (ProcessLookupError, OSError):
                pass
            # Drain whatever the process had already written before the kill,
            # still bounded by the same cap.
            try:
                while True:
                    eof, total_len, truncated = _drain_once(fd, chunks, total_len, truncated)
                    if eof:
                        break
            except OSError:
                pass
        proc.stdout.close()
        proc.wait()

    output = b"".join(chunks).decode("utf-8", errors="replace")
    if truncated:
        output += _TRUNCATION_MARKER
    status = "fail" if timed_out or proc.returncode != 0 else "pass"
    return {
        "name": name,
        "status": status,
        "duration": time.monotonic() - start,
        "output": output,
        "output_truncated": truncated,
        "timed_out": timed_out,
    }


def run_integration_gate(
    workspace_root: str,
    manifest_path: str = DEFAULT_MANIFEST_PATH,
    global_timeout: float = DEFAULT_GLOBAL_TIMEOUT,
) -> dict:
    """Run every repo's ``test_cmd`` from the manifest and aggregate a verdict.

    Repos run sequentially, each in its own process group. A per-repo timeout
    (manifest-configured, default 120s) is additionally clamped to whatever
    remains of ``global_timeout`` (default 300s) so no single hung repo (or
    long tail of repos) can blow the overall budget.

    Returns ``{"per_repo": [{"name", "status", "duration",
    "output_truncated", ...}], "gate_passed": bool, "gate_duration_s":
    float}`` -- the last two fields are the exact shape promised on
    final.json's ``integration_gate`` field (R1, P16).
    """
    entries = _load_manifest(manifest_path)

    gate_start = time.monotonic()
    per_repo = []
    deadline = gate_start + global_timeout
    for entry in entries:
        name = entry["name"]
        repo_path = os.path.join(workspace_root, entry.get("path", name))
        test_cmd = entry["test_cmd"]
        repo_timeout = entry.get("timeout", DEFAULT_REPO_TIMEOUT)

        remaining = deadline - time.monotonic()
        if remaining <= 0:
            per_repo.append({
                "name": name, "status": "fail", "duration": 0.0,
                "output": "global integration-gate timeout exceeded",
                "output_truncated": False, "timed_out": True,
            })
            continue

        per_repo.append(
            _run_repo(name, repo_path, test_cmd, min(repo_timeout, remaining))
        )

    gate_passed = bool(per_repo) and all(r["status"] == "pass" for r in per_repo)
    return {
        "per_repo": per_repo,
        "gate_passed": gate_passed,
        "gate_duration_s": time.monotonic() - gate_start,
    }


def integration_gate_exit_code(result: dict) -> int:
    """Map a :func:`run_integration_gate` result to the stable CI exit code.

    A failing gate means the cross-repo test run could not be verified
    clean -- that is infrastructure, not a code-quality rejection -- so a
    failure always maps to ``CI_EXIT_INFRASTRUCTURE`` (R1, P16), never the
    blocking/REJECT code a review verdict would use.
    """
    return (
        runner.CI_EXIT_CLEAN if result.get("gate_passed")
        else runner.CI_EXIT_INFRASTRUCTURE
    )
