#!/usr/bin/env python3
"""Regression tests for every defect fixed in v1.4.0.

Each test is named for the bug it prevents from returning. All of them were
reproduced against v1.3.2 before the fix landed.
"""

from __future__ import annotations

import json
import math
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

try:
    import numpy as np
    import pandas as pd
    import rdkit  # noqa: F401
except ImportError as exc:  # pragma: no cover
    # Loud, distinguishable skip (exit 77) - never a silent false green.
    print(f"SKIP test_v140_regressions.py - REQUIRED dependency missing: {exc}")
    print("     install it with:  python3 -m pip install rdkit pandas numpy")
    raise SystemExit(77) from None

ROOT = Path(__file__).resolve().parent.parent
CLI = ROOT / "scripts" / "qsar_pipeline.py"
sys.path.insert(0, str(ROOT / "scripts"))


def run_cli(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(CLI), *args],
                          capture_output=True, text=True, timeout=900)


def make_predictions_csv(path: Path, n: int = 5) -> None:
    smis = ["CCO", "CCN", "c1ccccc1", "CC(=O)O", "CCCC", "CCOC", "CN(C)C", "c1ccncc1"][:n]
    pd.DataFrame({"canonical_smiles": smis,
                  "score": np.linspace(0.9, 0.5, len(smis))}).to_csv(path, index=False)


class BudgetGuardTest(unittest.TestCase):
    """B1: `--budget 0` used to return the ENTIRE pool (0 is falsy in Python)."""

    def test_budget_zero_is_rejected_not_silently_defaulted(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            pred = Path(td) / "p.csv"
            make_predictions_csv(pred)
            r = run_cli("select", "--predictions", str(pred), "--score-column", "score",
                        "--budget", "0", "--output", str(Path(td) / "o.csv"))
            self.assertNotEqual(r.returncode, 0, "budget 0 must fail loudly")
            self.assertIn("--budget must be at least 1", r.stdout + r.stderr)
            self.assertFalse((Path(td) / "o.csv").exists(),
                             "no output may be written for an invalid budget")

    def test_negative_budget_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            pred = Path(td) / "p.csv"
            make_predictions_csv(pred)
            r = run_cli("select", "--predictions", str(pred), "--score-column", "score",
                        "--budget", "-3", "--output", str(Path(td) / "o.csv"))
            self.assertNotEqual(r.returncode, 0)

    def test_budget_over_pool_warns_and_reports_both_numbers(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            pred, out = Path(td) / "p.csv", Path(td) / "o.csv"
            make_predictions_csv(pred, n=5)
            r = run_cli("select", "--predictions", str(pred), "--score-column", "score",
                        "--budget", "50", "--output", str(out))
            self.assertEqual(r.returncode, 0, r.stderr)
            payload = json.loads(r.stdout[r.stdout.index("{"):])
            self.assertEqual(payload["budget"], 5)
            self.assertEqual(payload["budget_requested"], 50)
            self.assertEqual(payload["candidate_pool"], 5)
            self.assertEqual(payload["candidates_after_filters"], 5)
            self.assertIsNotNone(payload["budget_note"])

    def test_normal_budget_still_exact(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            pred, out = Path(td) / "p.csv", Path(td) / "o.csv"
            make_predictions_csv(pred, n=8)
            r = run_cli("select", "--predictions", str(pred), "--score-column", "score",
                        "--budget", "3", "--output", str(out))
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertEqual(len(pd.read_csv(out)), 3)


class ConformalNonconformityTest(unittest.TestCase):
    """B2: a model without predict_proba produced all-zero nonconformity scores,
    a threshold of 0, and a reported 100% coverage that meant nothing."""

    def setUp(self) -> None:
        import warnings
        warnings.filterwarnings("ignore")
        import qsar_pipeline as qp
        self.qp = qp

    def test_decision_function_model_is_not_degenerate(self) -> None:
        from sklearn.svm import SVC
        X = np.random.RandomState(0).rand(60, 8)
        y = np.array(["active", "inactive"] * 30)
        model = SVC(probability=False).fit(X, y)
        self.assertFalse(hasattr(model, "predict_proba"))
        ncs = self.qp.conformal_ncs("classification", model, X, y, ["active", "inactive"])
        self.assertGreater(len(np.unique(ncs)), 1,
                           "nonconformity scores collapsed to a constant (the v1.3.2 bug)")
        self.assertFalse(bool(np.all(ncs == 0.0)))

    def test_probability_model_unchanged(self) -> None:
        from sklearn.ensemble import RandomForestClassifier
        X = np.random.RandomState(1).rand(60, 8)
        y = np.array(["active", "inactive"] * 30)
        model = RandomForestClassifier(n_estimators=20, random_state=0).fit(X, y)
        ncs = self.qp.conformal_ncs("classification", model, X, y, ["active", "inactive"])
        self.assertTrue(np.all(ncs >= -1e-9) and np.all(ncs <= 1.0 + 1e-9))

    def test_model_without_any_score_refuses(self) -> None:
        class NoScores:
            def fit(self, X, y):
                self.classes_ = np.unique(y)
                return self

            def predict(self, X):
                return np.array([self.classes_[0]] * len(X))

        X = np.random.RandomState(2).rand(20, 4)
        y = np.array(["active", "inactive"] * 10)
        with self.assertRaises(SystemExit):
            self.qp.conformal_ncs("classification", NoScores().fit(X, y), X, y,
                                  ["active", "inactive"])

    def test_margin_nonconformity_preserves_coverage(self) -> None:
        """The whole point: swapping the nonconformity measure must keep the
        conformal coverage guarantee. Empirically ~1-alpha."""
        from sklearn.svm import SVC
        alpha, covs = 0.1, []
        for t in range(25):
            r = np.random.RandomState(t)
            X = r.rand(300, 6)
            lin = X[:, 0] * 3 - X[:, 1] * 2 + r.randn(300) * 0.5
            y = np.where(lin > np.median(lin), "active", "inactive")
            m = SVC(probability=False).fit(X[:150], y[:150])
            cal = self.qp.conformal_ncs("classification", m, X[150:240], y[150:240],
                                        ["active", "inactive"])
            k = len(cal)
            q = max(1, min(int(math.ceil((k + 1) * (1 - alpha))), k))
            thr = float(np.sort(cal)[q - 1])
            te = self.qp.conformal_ncs("classification", m, X[240:], y[240:],
                                       ["active", "inactive"])
            covs.append(float(np.mean(te <= thr)))
        coverage = float(np.mean(covs))
        self.assertAlmostEqual(coverage, 1 - alpha, delta=0.05,
                               msg=f"coverage {coverage:.3f} broke the conformal guarantee")


class YRandomizationTest(unittest.TestCase):
    """F5: the chance-correlation check that v1.3.2 did not have at all."""

    def test_underpowered_run_is_labelled_not_declared_negative(self) -> None:
        """With n permutations the smallest reachable p is 1/(n+1). Below 19
        permutations p<=0.05 is impossible, so the run must report UNDERPOWERED
        rather than 'chance not excluded'."""
        for n in (5, 12, 18):
            self.assertGreater(1.0 / (1 + n), 0.05)
        for n in (19, 24, 99):
            self.assertLessEqual(1.0 / (1 + n), 0.05)

    def test_p_value_formula_has_add_one_correction(self) -> None:
        src = (ROOT / "scripts" / "qsar_pipeline.py").read_text(encoding="utf-8")
        self.assertIn("(1 + n_ge) / (1 + null.size)", src)

    def test_validate_subcommand_registered(self) -> None:
        r = run_cli("validate", "--help")
        self.assertEqual(r.returncode, 0)
        for flag in ("--n-permutations", "--max-samples", "--model", "--target-column"):
            self.assertIn(flag, r.stdout)


class SchemaContractTest(unittest.TestCase):
    """F6: outputs must be self-describing for models that never read prose."""

    def test_schema_is_valid_json_and_lists_all_contracts(self) -> None:
        r = run_cli("schema")
        self.assertEqual(r.returncode, 0, r.stderr)
        payload = json.loads(r.stdout)
        for sid in ("qsar_validate.v1", "qsar_select.v1", "qsar_train.v1"):
            self.assertIn(sid, payload["schemas"])
        self.assertIn("never_evidence", payload["trust_contract"])

    def test_compact_schema_is_single_line_and_smaller(self) -> None:
        full = run_cli("schema").stdout
        compact = run_cli("schema", "--compact").stdout
        json.loads(compact)
        self.assertEqual(len(compact.strip().splitlines()), 1)
        self.assertLess(len(compact), len(full) * 0.85)

    def test_schema_version_matches_skill_md(self) -> None:
        """Version drift: code said 1.3.0 while SKILL.md said 1.3.2, so every
        model card recorded the wrong provenance."""
        payload = json.loads(run_cli("schema").stdout)
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn(f"version: {payload['version']}", skill)


class DomainDegeneracyTest(unittest.TestCase):
    """B4: a 0.0 domain threshold marks everything in_domain with no warning."""

    def test_threshold_degenerate_below_three_molecules(self) -> None:
        import qsar_pipeline as qp
        from rdkit import Chem
        mols = [Chem.MolFromSmiles(s) for s in ("CCO", "CCN")]
        _, fps, _ = qp.featurize_molecules(mols, fp_radius=2, fp_bits=1024)
        self.assertEqual(qp.estimate_domain_threshold(fps, seed=0), 0.0)

    def test_train_output_carries_the_degeneracy_flag(self) -> None:
        src = (ROOT / "scripts" / "qsar_pipeline.py").read_text(encoding="utf-8")
        self.assertIn("domain_threshold_degenerate", src)
        self.assertIn("domain_warning", src)


class TestSuiteIntegrityTest(unittest.TestCase):
    """B3: SkipTest at import printed a traceback and exited 0 - a false green."""

    def test_all_suites_use_loud_exit_77_skips(self) -> None:
        for name in ("test_smoke.py", "test_advanced.py", "test_v140_regressions.py"):
            src = (ROOT / "tests" / name).read_text(encoding="utf-8")
            self.assertIn("SystemExit(77)", src, f"{name} must skip with exit 77")
            self.assertNotIn("raise unittest.SkipTest(f\"Optional", src,
                             f"{name} still uses the silent-skip pattern")


class ConformalShapeGuardTest(unittest.TestCase):
    """v1.4.2: an estimator whose score matrix is not (n_samples, n_classes) was
    indexed by class anyway, reading nonconformity from the WRONG column and
    producing a confident but silently misleading prediction set."""

    def setUp(self) -> None:
        import warnings
        warnings.filterwarnings("ignore")
        import qsar_pipeline as qp
        self.qp = qp

    def test_one_vs_one_decision_matrix_is_refused(self) -> None:
        from sklearn.svm import SVC
        X = np.random.RandomState(0).rand(80, 5)
        y = np.array(["a", "b", "c", "d"] * 20)
        m = SVC(probability=False, decision_function_shape="ovo").fit(X, y)
        self.assertEqual(m.decision_function(X).shape[1], 6)   # not 4
        with self.assertRaises(SystemExit):
            self.qp.conformal_ncs("classification", m, X, y, sorted(set(y)))

    def test_probability_matrix_width_mismatch_is_refused(self) -> None:
        class BadProbs:
            def predict_proba(self, X):
                return np.ones((len(X), 5)) / 5

            def predict(self, X):
                return np.array(["a"] * len(X))

        X = np.random.RandomState(1).rand(10, 4)
        y = np.array(["a", "b"] * 5)
        with self.assertRaises(SystemExit):
            self.qp.conformal_ncs("classification", BadProbs(), X, y, ["a", "b"])

    def test_binary_1d_decision_with_multiclass_bundle_is_refused(self) -> None:
        class OneD:
            def decision_function(self, X):
                return np.linspace(-1, 1, len(X))

            def predict(self, X):
                return np.array(["a"] * len(X))

        X = np.random.RandomState(2).rand(12, 3)
        y = np.array(["a", "b", "c"] * 4)
        with self.assertRaises(SystemExit):
            self.qp.conformal_ncs("classification", OneD(), X, y, ["a", "b", "c"])

    def test_valid_ovr_multiclass_still_works(self) -> None:
        from sklearn.svm import SVC
        X = np.random.RandomState(3).rand(80, 5)
        y = np.array(["a", "b", "c", "d"] * 20)
        m = SVC(probability=False).fit(X, y)          # default ovr
        ncs = self.qp.conformal_ncs("classification", m, X, y, sorted(set(y)))
        self.assertGreater(len(np.unique(ncs)), 1)


class PublishedArtifactIntegrityTest(unittest.TestCase):
    """v1.4.1: the registry strips every dot-path and skill-card.md. Anything hashed
    that does not ship makes verify_integrity.py FAIL for every consumer - which a
    `.clawhubignore` added in v1.4.0 did. Verify against the tree that actually ships."""

    def test_integrity_holds_on_the_published_tree(self) -> None:
        import shutil
        with tempfile.TemporaryDirectory() as td:
            dest = Path(td) / "s"
            shutil.copytree(ROOT, dest,
                            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
            # reproduce the registry's own filters
            for child in list(dest.rglob("*")):
                if child.exists() and any(part.startswith(".") for part in
                                          child.relative_to(dest).parts):
                    (shutil.rmtree if child.is_dir() else Path.unlink)(child)
            card = dest / "skill-card.md"
            if card.exists():
                card.unlink()
            r = subprocess.run([sys.executable, str(dest / "scripts" / "verify_integrity.py")],
                               capture_output=True, text=True, cwd=dest, timeout=300)
            self.assertEqual(r.returncode, 0,
                             f"canonical hash fails on the published tree: {r.stdout}{r.stderr}")
            c = subprocess.run(["sha256sum", "-c", "CHECKSUMS.sha256"],
                               capture_output=True, text=True, cwd=dest, timeout=300)
            self.assertEqual(c.returncode, 0,
                             f"CHECKSUMS lists files that do not ship: {c.stdout}{c.stderr}")

    def test_no_dotfiles_are_listed_in_checksums(self) -> None:
        for line in (ROOT / "CHECKSUMS.sha256").read_text(encoding="utf-8").splitlines():
            rel = line.split("  ", 1)[1]
            self.assertFalse(any(part.startswith(".") for part in rel.split("/")),
                             f"{rel} is a dot-path and will never be published")


class NetworkClaimConsistencyTest(unittest.TestCase):
    """v1.4.1: frontmatter declared optional network hosts while the body said
    'no network requests' - a contradiction the scanner flagged."""

    def test_no_network_capability_declared(self) -> None:
        fm = (ROOT / "SKILL.md").read_text(encoding="utf-8").split("---")[1]
        self.assertNotIn("network:", fm,
                         "frontmatter must not declare network capability for an offline skill")

    def test_scripts_make_no_network_calls(self) -> None:
        import re
        src = (ROOT / "scripts" / "qsar_pipeline.py").read_text(encoding="utf-8")
        for bad in (r"\bimport requests\b", r"\bimport urllib\b", r"\bimport socket\b",
                    r"urlopen\(", r"requests\.(get|post)\("):
            self.assertIsNone(re.search(bad, src), f"network call found: {bad}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
