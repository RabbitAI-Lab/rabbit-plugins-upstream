#!/usr/bin/env python3
"""selfcheck.py — calibration memory + drift detection for the hPL docking stack.

This is the skill's self-improvement layer. Docking stacks rot silently: a new
Vina build, a new RDKit tautomer rule, a different CPU count or a changed box
definition all move scores by a few tenths of a kcal/mol without erroring. The
skill previously had NO mechanism to notice. selfcheck.py gives it one.

  HOW IT WORKS
    Dock a fixed pair of reference ligands (ibuprofen, caffeine) at the
    catalytic site, compare against the stored calibration baseline, and record
    the run in a persistent history file. Drift beyond tolerance is an error,
    not a warning.

  COMMANDS
    run       dock the reference set and compare with the baseline
    baseline  overwrite the baseline with the current stack's numbers
    history   print recorded runs (newest last)
    show      print the active baseline

  EXIT CODES
    0 within tolerance · 1 DRIFT detected · 3 could not run · 2 bad usage

  Last stdout line is always one JSON object. Parse that.

Tolerance defaults to 0.5 kcal/mol, which is Vina's own documented scoring
reproducibility band — tighter than that and you flag noise, looser and you
miss real regressions.
"""
from __future__ import annotations

import argparse
import csv
import json
import platform
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
STACK_CANDIDATES = [
    HERE.parent / "docking_professional_stack",
    HERE.parent,
    Path.cwd() / "docking_professional_stack",
    Path.cwd(),
]
CAL_DIR = HERE.parent / "calibration"
BASELINE = CAL_DIR / "baseline.json"
HISTORY = CAL_DIR / "history.jsonl"

# Reference ligands: one anionic flexible acid, one neutral rigid heterocycle.
# Between them they exercise protonation, stereo enumeration and rigid docking.
REFERENCE_SET = {
    "ibuprofen": "CC(C)Cc1ccc(cc1)C(C)C(=O)O",
    "caffeine": "Cn1c(=O)c2c(ncn2C)n(C)c1=O",
}
REFERENCE_SITE = "catalytic_triad"
DEFAULT_TOL = 0.5


def emit(ok: bool, code: int, **kw):
    print(json.dumps({"ok": ok, "exit": code, **kw}, default=str))
    sys.exit(code)


def log(m):
    print(f"[selfcheck] {m}", file=sys.stderr, flush=True)


def find_stack(explicit: str | None) -> Path:
    cands = [Path(explicit)] if explicit else STACK_CANDIDATES
    for c in cands:
        if (c / "multi_site_docking.py").exists():
            return c.resolve()
    emit(False, 3, error="cannot locate docking_professional_stack "
                         "(pass --stack)", tried=[str(c) for c in cands])


def env_fingerprint(stack: Path, python: str) -> dict:
    """Record what could plausibly change a score."""
    fp = {"python": platform.python_version(), "platform": platform.platform()}
    # Look for vina next to the interpreter first: the reference docking runs
    # with `python`, whose env owns the vina binary, but PATH here may not.
    # (Without this the fingerprint said "unavailable" even on a working stack,
    # which defeats the point of recording it.)
    import shutil as _sh
    vina_bin = (_sh.which("vina")
                or str(Path(python).parent / "vina") if Path(python).parent.joinpath("vina").exists()
                else _sh.which("vina"))
    try:
        v = subprocess.run([vina_bin or "vina", "--version"],
                           capture_output=True, text=True, timeout=30)
        line = (v.stdout or v.stderr).strip().splitlines()
        fp["vina"] = line[0][:80] if line else "unknown"
        fp["vina_path"] = vina_bin or "vina(PATH)"
    except Exception:  # noqa: BLE001
        fp["vina"] = "unavailable"
    for mod in ("rdkit", "meeko", "numpy"):
        try:
            r = subprocess.run(
                [python, "-c", f"import {mod},sys; "
                               f"print(getattr({mod},'__version__','?'))"],
                capture_output=True, text=True, timeout=60)
            fp[mod] = r.stdout.strip() or "?"
        except Exception:  # noqa: BLE001
            fp[mod] = "unavailable"
    return fp


def dock_reference(stack: Path, python: str, workdir: Path, precision: str) -> dict:
    """Dock the reference set; return {ligand: score} at the reference site."""
    workdir.mkdir(parents=True, exist_ok=True)
    lig = workdir / "reference_ligands.csv"
    with open(lig, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["name", "smiles"])
        for n, s in REFERENCE_SET.items():
            w.writerow([n, s])
    out = workdir / "ref_results"
    cmd = [python, str(stack / "multi_site_docking.py"),
           "--ligands", str(lig), "--precision", precision,
           "--workers", "2", "--outdir", str(out)]
    log("docking reference set: " + " ".join(cmd))
    t0 = time.time()
    p = subprocess.run(cmd, cwd=str(stack), capture_output=True, text=True, timeout=7200)
    if p.returncode != 0:
        emit(False, 3, error="reference docking failed",
             stderr=p.stderr[-1500:], stdout=p.stdout[-800:])
    res = out / "results_all_sites.csv"
    if not res.exists():
        emit(False, 3, error=f"no results produced at {res}")
    scores = {}
    for r in csv.DictReader(open(res)):
        if r.get("site") == REFERENCE_SITE and r.get("status") == "ok":
            try:
                scores[r["name"]] = float(r["score"])
            except (TypeError, ValueError):
                pass
    if len(scores) != len(REFERENCE_SET):
        emit(False, 3, error="reference set incomplete", got=scores)
    return {"scores": scores, "wall_s": round(time.time() - t0, 1)}


def cmd_run(args):
    stack = find_stack(args.stack)
    python = args.python or sys.executable
    if not BASELINE.exists() and not args.write_baseline:
        emit(False, 3, error=f"no baseline at {BASELINE}; "
                             f"create one with: selfcheck.py baseline")
    obs = dock_reference(stack, python, Path(args.workdir), args.precision)
    fp = env_fingerprint(stack, python)
    record = {
        "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "scores": obs["scores"], "wall_s": obs["wall_s"],
        "precision": args.precision, "env": fp,
    }
    CAL_DIR.mkdir(parents=True, exist_ok=True)
    with open(HISTORY, "a") as f:
        f.write(json.dumps(record) + "\n")

    base = json.loads(BASELINE.read_text())
    tol = args.tolerance
    deltas, drifted = {}, []
    for name, got in obs["scores"].items():
        exp = base.get("scores", {}).get(name)
        if exp is None:
            continue
        d = round(got - exp, 3)
        deltas[name] = {"baseline": exp, "observed": got, "delta": d,
                        "within_tol": abs(d) <= tol}
        if abs(d) > tol:
            drifted.append(name)
    ok = not drifted
    emit(ok, 0 if ok else 1,
         deltas=deltas, tolerance=tol, drifted=drifted, wall_s=obs["wall_s"],
         env=fp, history=str(HISTORY),
         verdict="calibrated" if ok else "DRIFT — scores moved beyond tolerance",
         advice=None if ok else
         "Do NOT publish results from this stack until explained. Compare `env` "
         "against the baseline env: a changed vina/rdkit/meeko version is the "
         "usual cause. If the new stack is genuinely better, re-baseline "
         "deliberately with `selfcheck.py baseline`.")


def cmd_baseline(args):
    stack = find_stack(args.stack)
    python = args.python or sys.executable
    obs = dock_reference(stack, python, Path(args.workdir), args.precision)
    CAL_DIR.mkdir(parents=True, exist_ok=True)
    payload = {
        "created": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "site": REFERENCE_SITE, "precision": args.precision,
        "ligands": REFERENCE_SET, "scores": obs["scores"],
        "env": env_fingerprint(stack, python),
        "note": "Baseline for drift detection. Regenerate deliberately, never "
                "to silence a failing selfcheck.",
    }
    BASELINE.write_text(json.dumps(payload, indent=2))
    emit(True, 0, wrote=str(BASELINE), scores=obs["scores"], wall_s=obs["wall_s"])


def cmd_history(args):
    if not HISTORY.exists():
        emit(True, 0, runs=[], note="no history yet")
    runs = [json.loads(l) for l in HISTORY.read_text().splitlines() if l.strip()]
    for r in runs[-args.limit:]:
        log(f"{r['ts']}  {r['scores']}  ({r.get('wall_s')}s)")
    emit(True, 0, n_runs=len(runs), shown=runs[-args.limit:])


def cmd_show(args):
    if not BASELINE.exists():
        emit(False, 3, error=f"no baseline at {BASELINE}")
    emit(True, 0, baseline=json.loads(BASELINE.read_text()))


def main():
    ap = argparse.ArgumentParser(description="Calibration + drift detection.")
    ap.add_argument("command", choices=["run", "baseline", "history", "show"])
    ap.add_argument("--stack")
    ap.add_argument("--python", help="interpreter that has rdkit/meeko/vina")
    ap.add_argument("--workdir", default="selfcheck_work")
    ap.add_argument("--precision", default="fast", choices=["fast", "balanced", "max"])
    ap.add_argument("--tolerance", type=float, default=DEFAULT_TOL,
                    help="kcal/mol drift allowed (default 0.5 = Vina's own band)")
    ap.add_argument("--write-baseline", action="store_true")
    ap.add_argument("--limit", type=int, default=10)
    args = ap.parse_args()
    {"run": cmd_run, "baseline": cmd_baseline,
     "history": cmd_history, "show": cmd_show}[args.command](args)


if __name__ == "__main__":
    main()
