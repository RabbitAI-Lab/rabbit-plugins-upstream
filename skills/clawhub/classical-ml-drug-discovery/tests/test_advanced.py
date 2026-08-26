#!/usr/bin/env python3
"""End-to-end tests for the advanced subcommands added in v1.3.0:
analyze, conformal, ensemble, select, interpret."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

try:
    import pandas as pd
    import rdkit  # noqa: F401
except ImportError as exc:  # pragma: no cover
    raise unittest.SkipTest(f"Optional dependency missing: {exc}")

ROOT = Path(__file__).resolve().parent.parent
CLI = ROOT / "scripts" / "qsar_pipeline.py"

AROMATIC = [
    "c1ccccc1", "Cc1ccccc1", "CCc1ccccc1", "Oc1ccccc1", "COc1ccccc1",
    "Nc1ccccc1", "Fc1ccccc1", "Clc1ccccc1", "Brc1ccccc1", "O=C(O)c1ccccc1",
    "N#Cc1ccccc1", "CC(=O)c1ccccc1", "c1ccc2ccccc2c1", "c1ccncc1", "c1ccoc1",
    "c1ccsc1", "CCOc1ccccc1", "O=C(N)c1ccccc1", "CC(C)c1ccccc1", "CSc1ccccc1",
]
ALIPHATIC = [
    "CC", "CCC", "CCCC", "CCCCC", "CCCCCC", "CCO", "CCCO", "CCCCO",
    "CCN", "CCCN", "CC(=O)O", "CCC(=O)O", "CCOC", "CCOCC", "CC(C)C",
    "CC(C)CO", "C1CCCCC1", "C1CCOCC1", "C1CCNCC1", "NCCO",
]


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(CLI), *args], text=True,
                          capture_output=True, check=False)


def tidy(proc: subprocess.CompletedProcess[str]) -> str:
    return (proc.stdout + proc.stderr).strip()


class AdvancedPipelineTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory(prefix="classical-advanced-")
        self.work = Path(self.tmp.name)
        rows = [{"smiles": s, "activity": "active"} for s in AROMATIC] + [
            {"smiles": s, "activity": "inactive"} for s in ALIPHATIC
        ]
        self.train_csv = self.work / "train.csv"
        pd.DataFrame(rows).to_csv(self.train_csv, index=False)
        self.lib_csv = self.work / "library.csv"
        pd.DataFrame({"smiles": ["CCc1ccccc1", "CCCO", "c1ncccc1", "Cc1ccc(O)cc1",
                                 "CCCCCCC", "COc1ccccc1", "CC(C)CO", "Oc1ccccc1",
                                 "CN1CCCCC1", "CCCCO"]}).to_csv(self.lib_csv, index=False)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _train(self, models: list[str], out: Path) -> dict:
        proc = run_cli("train", "--input", str(self.train_csv), "--smiles-column", "smiles",
                       "--target-column", "activity", "--task", "classification",
                       "--positive-label", "active", "--split", "random", "--models", *models,
                       "--fast", "--cv-folds", "2", "--n-jobs", "1", "--fp-bits", "256",
                       "--output-dir", str(out))
        self.assertEqual(proc.returncode, 0, msg=tidy(proc))
        return json.loads((out / "metrics.json").read_text())

    def test_analyze(self) -> None:
        out = self.work / "analysis"
        proc = run_cli("analyze", "--input", str(self.train_csv), "--smiles-column", "smiles",
                       "--target-column", "activity", "--task", "classification",
                       "--output-dir", str(out), "--sample", "100")
        self.assertEqual(proc.returncode, 0, msg=tidy(proc))
        summary = json.loads((out / "analysis.json").read_text())
        self.assertEqual(summary["valid_rows"], 40)
        self.assertGreaterEqual(summary["unique_canonical_smiles"], 38)
        self.assertGreater(summary["scaffold_diversity_ratio"], 0.0)
        self.assertIn("imbalance_ratio", summary["target"])
        self.assertTrue((out / "dataset_layout.csv").is_file())

    def test_conformal_classification(self) -> None:
        model_dir = self.work / "model"
        self._train(["rf"], model_dir)
        # calibrate on the training CSV itself (in-sample; just for coverage mechanics)
        out = self.work / "conf.csv"
        proc = run_cli("conformal", "--model", str(model_dir / "model.joblib"),
                       "--trust-model", "--calibration", str(self.train_csv),
                       "--smiles-column", "smiles", "--target-column", "activity",
                       "--task", "classification", "--alpha", "0.1", "--query", str(self.lib_csv),
                       "--query-smiles-column", "smiles", "--output", str(out))
        self.assertEqual(proc.returncode, 0, msg=tidy(proc))
        df = pd.read_csv(out)
        self.assertTrue({"prediction_set", "set_size"}.issubset(df.columns))
        self.assertEqual(len(df), 10)
        rep = json.loads((out.with_suffix(".conformal.json")).read_text())
        self.assertEqual(rep["task"], "classification")
        self.assertTrue(0.0 <= rep["calibration_empirical_coverage"] <= 1.0)

    def test_conformal_regression(self) -> None:
        # build a regression dataset (logS-like values)
        rows = [{"smiles": s, "logS": float(i % 10) - 3.0} for i, s in enumerate(AROMATIC + ALIPHATIC)]
        reg_csv = self.work / "reg.csv"
        pd.DataFrame(rows).to_csv(reg_csv, index=False)
        model_dir = self.work / "regmodel"
        proc = run_cli("train", "--input", str(reg_csv), "--smiles-column", "smiles",
                       "--target-column", "logS", "--task", "regression",
                       "--split", "random", "--models", "rf", "--fast", "--cv-folds", "2",
                       "--n-jobs", "1", "--fp-bits", "256", "--output-dir", str(model_dir))
        self.assertEqual(proc.returncode, 0, msg=tidy(proc))
        lib = self.work / "reglib.csv"
        pd.DataFrame({"smiles": ["Cc1ccccc1", "CCCO", "c1ncccc1", "CCO", "CCC"]}).to_csv(lib, index=False)
        out = self.work / "reg_iv.csv"
        proc = run_cli("conformal", "--model", str(model_dir / "model.joblib"), "--trust-model",
                       "--calibration", str(reg_csv), "--smiles-column", "smiles",
                       "--target-column", "logS", "--task", "regression", "--alpha", "0.1",
                       "--query", str(lib), "--query-smiles-column", "smiles", "--output", str(out))
        self.assertEqual(proc.returncode, 0, msg=tidy(proc))
        df = pd.read_csv(out)
        self.assertTrue({"set_lower", "set_upper"}.issubset(df.columns))
        self.assertEqual(len(df), 5)

    def test_ensemble(self) -> None:
        m1 = self.work / "m_rf"; m2 = self.work / "m_svm"
        self._train(["rf"], m1); self._train(["svm"], m2)
        p1 = self.work / "p1.csv"; p2 = self.work / "p2.csv"
        for model_dir, out in ((m1, p1), (m2, p2)):
            proc = run_cli("predict", "--model", str(model_dir / "model.joblib"), "--trust-model",
                           "--input", str(self.lib_csv), "--smiles-column", "smiles",
                           "--output", str(out))
            self.assertEqual(proc.returncode, 0, msg=tidy(proc))
        out_dir = self.work / "ens"
        proc = run_cli("ensemble", "--predictions", str(p1), str(p2),
                       "--score-column", "positive_probability", "--task", "classification",
                       "--output-dir", str(out_dir))
        self.assertEqual(proc.returncode, 0, msg=tidy(proc))
        df = pd.read_csv(out_dir / "consensus_predictions.csv")
        self.assertIn("consensus_score", df.columns)
        self.assertIn("consensus_std", df.columns)
        self.assertGreaterEqual(df["n_models"].iloc[0], 2)
        metrics = json.loads((out_dir / "consensus_metrics.json").read_text())
        self.assertEqual(metrics["n_models"], 2)

    def test_select(self) -> None:
        model_dir = self.work / "m_sel"
        self._train(["rf"], model_dir)
        lib = self.work / "sel_lib.csv"
        pd.DataFrame({"smiles": ["CCc1ccccc1", "CCCO", "c1ncccc1", "Cc1ccc(O)cc1", "CCCCCCC",
                                 "COc1ccccc1", "CC(C)CO", "Oc1ccccc1", "CN1CCCCC1", "CCCCO",
                                 "c1ccncc1", "c1ccoc1"]}).to_csv(lib, index=False)
        preds = self.work / "sel_preds.csv"
        proc = run_cli("predict", "--model", str(model_dir / "model.joblib"), "--trust-model",
                       "--input", str(lib), "--smiles-column", "smiles", "--output", str(preds))
        self.assertEqual(proc.returncode, 0, msg=tidy(proc))
        out = self.work / "shortlist.csv"
        proc = run_cli("select", "--predictions", str(preds), "--budget", "5",
                       "--output", str(out))
        self.assertEqual(proc.returncode, 0, msg=tidy(proc))
        df = pd.read_csv(out)
        self.assertEqual(len(df), 5)
        self.assertIn("selection_rank", df.columns)
        self.assertIn("pairwise_mean_similarity", df.columns)

    def test_interpret(self) -> None:
        model_dir = self.work / "m_int"
        self._train(["rf"], model_dir)
        out = self.work / "interp"
        proc = run_cli("interpret", "--model", str(model_dir / "model.joblib"), "--trust-model",
                       "--data", str(self.train_csv), "--smiles-column", "smiles",
                       "--target-column", "activity", "--output-dir", str(out), "--top-n", "10")
        self.assertEqual(proc.returncode, 0, msg=tidy(proc))
        imp = pd.read_csv(out / "feature_importance.csv")
        self.assertGreaterEqual(len(imp), 20)
        summ = json.loads((out / "interpretation.json").read_text())
        self.assertEqual(summ["importance_method"], "permutation")


if __name__ == "__main__":
    unittest.main(verbosity=2)
