"""CLI-level tests for validate_results.py and build_report.py (no docking needed)."""
import csv
import json
import subprocess
import sys
from pathlib import Path


_here = Path(__file__).resolve().parent.parent
_cands = [
    _here,                                                     # tests/ inside the stack root (payload layout)
    _here / "stack" / "docking_professional_stack",            # dev layout
]
STACK = next((c for c in _cands if (c / "multi_site_docking.py").exists()), _cands[0])
PY = sys.executable


def make_results(path, rows, header=None):
    header = header or ["name", "site", "status", "score", "mw", "rotb", "time_s"]
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


def test_validate_pass(tmp_path):
    rows = [[f"mol{i}", site, "ok", -7.5, 250, 4, 3.0]
            for i in range(3) for site in
            ["catalytic_triad", "oxyanion_hole", "lid", "hydrophobic_pocket", "colipase_cterm"]]
    make_results(tmp_path / "r.csv", rows)
    r = subprocess.run([PY, str(STACK / "validate_results.py"),
                        "--results", str(tmp_path / "r.csv"), "--sites", "5"],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    assert "RESULT: PASS" in r.stdout


def test_validate_catches_silent_fake(tmp_path):
    """Rows marked ok without a score must FAIL (fail-closed)."""
    rows = [["mol1", "catalytic_triad", "ok", "", 250, 4, 3.0]]
    make_results(tmp_path / "r.csv", rows)
    r = subprocess.run([PY, str(STACK / "validate_results.py"),
                        "--results", str(tmp_path / "r.csv")],
                       capture_output=True, text=True)
    assert r.returncode == 2
    assert "silent fake" in r.stdout


def test_validate_catches_implausible_score(tmp_path):
    rows = [["mol1", "catalytic_triad", "ok", "-55.3", 250, 4, 3.0]]
    make_results(tmp_path / "r.csv", rows)
    r = subprocess.run([PY, str(STACK / "validate_results.py"),
                        "--results", str(tmp_path / "r.csv")],
                       capture_output=True, text=True)
    assert r.returncode == 2
    assert "implausible" in r.stdout.lower() or "fail-closed" in r.stdout


def test_validate_requires_sites_coverage(tmp_path):
    rows = [["mol1", "catalytic_triad", "ok", -7.5, 250, 4, 3.0]]
    make_results(tmp_path / "r.csv", rows)
    r = subprocess.run([PY, str(STACK / "validate_results.py"),
                        "--results", str(tmp_path / "r.csv"), "--sites", "5"],
                       capture_output=True, text=True)
    assert r.returncode == 2
    assert "1/5" in r.stdout


def test_build_report_sections(tmp_path):
    rows = [["Quercetin", "catalytic_triad", "ok", -9.7, 302, 1, 5.0],
            ["Quercetin", "oxyanion_hole", "ok", -9.2, 302, 1, 5.0],
            ["Luteolin", "catalytic_triad", "ok", -9.6, 286, 1, 5.0]]
    make_results(tmp_path / "r.csv", rows)
    sites = {"catalytic_triad": {"center": [1, 2, 3], "box": 20, "note": "n"},
             "oxyanion_hole": {"center": [1, 2, 4], "box": 18, "note": "n"}}
    (tmp_path / "sites.json").write_text(json.dumps(sites))
    out = tmp_path / "REPORT.md"
    r = subprocess.run([PY, str(STACK / "build_report.py"),
                        "--results", str(tmp_path / "r.csv"),
                        "--sites-file", str(tmp_path / "sites.json"),
                        "-o", str(out)],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    text = out.read_text()
    assert "# hPL Pancreatic Lipase Virtual Screen" in text
    assert "Quercetin" in text
    assert "## Global top 20" in text
    assert "### catalytic_triad" in text
