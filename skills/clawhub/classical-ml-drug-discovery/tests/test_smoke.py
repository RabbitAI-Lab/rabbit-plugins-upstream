#!/usr/bin/env python3
"""End-to-end smoke test for the local QSAR CLI."""

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
    raise unittest.SkipTest(f"Optional smoke-test dependency missing: {exc}")


ROOT = Path(__file__).resolve().parent.parent
CLI = ROOT / "scripts" / "qsar_pipeline.py"


AROMATIC = [
    "c1ccccc1",
    "Cc1ccccc1",
    "CCc1ccccc1",
    "Oc1ccccc1",
    "COc1ccccc1",
    "Nc1ccccc1",
    "N(C)c1ccccc1",
    "Fc1ccccc1",
    "Clc1ccccc1",
    "Brc1ccccc1",
    "O=C(O)c1ccccc1",
    "N#Cc1ccccc1",
    "CC(=O)c1ccccc1",
    "c1ccc2ccccc2c1",
    "c1ccncc1",
    "c1ccoc1",
    "c1ccsc1",
    "CCOc1ccccc1",
    "O=C(N)c1ccccc1",
    "CC(C)c1ccccc1",
]

ALIPHATIC = [
    "CC",
    "CCC",
    "CCCC",
    "CCCCC",
    "CCCCCC",
    "CCO",
    "CCCO",
    "CCCCO",
    "CCN",
    "CCCN",
    "CC(=O)O",
    "CCC(=O)O",
    "CCOC",
    "CCOCC",
    "CC(C)C",
    "CC(C)CO",
    "C1CCCCC1",
    "C1CCOCC1",
    "C1CCNCC1",
    "NCCO",
]


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    command = [sys.executable, str(CLI), *args]
    return subprocess.run(command, text=True, capture_output=True, check=False)


class PipelineSmokeTest(unittest.TestCase):
    def test_audit_train_predict(self) -> None:
        with tempfile.TemporaryDirectory(prefix="classical-ml-dd-") as temporary:
            work = Path(temporary)
            rows = [{"smiles": smi, "activity": "active"} for smi in AROMATIC] + [
                {"smiles": smi, "activity": "inactive"} for smi in ALIPHATIC
            ]
            rows.append({"smiles": AROMATIC[0], "activity": "active"})
            rows.append({"smiles": "not-a-smiles", "activity": "inactive"})
            train_csv = work / "train.csv"
            pd.DataFrame(rows).to_csv(train_csv, index=False)

            audit_dir = work / "audit"
            audit = run_cli(
                "audit",
                "--input",
                str(train_csv),
                "--smiles-column",
                "smiles",
                "--target-column",
                "activity",
                "--task",
                "classification",
                "--output-dir",
                str(audit_dir),
            )
            self.assertEqual(audit.returncode, 0, msg=audit.stderr + audit.stdout)
            audit_json = json.loads((audit_dir / "data_audit.json").read_text())
            self.assertEqual(audit_json["invalid_structure_rows"], 1)
            self.assertGreaterEqual(audit_json["duplicate_rows_collapsed"], 1)

            model_dir = work / "model"
            trained = run_cli(
                "train",
                "--input",
                str(train_csv),
                "--smiles-column",
                "smiles",
                "--target-column",
                "activity",
                "--task",
                "classification",
                "--positive-label",
                "active",
                "--split",
                "random",
                "--models",
                "rf",
                "svm",
                "gb",
                "--fast",
                "--cv-folds",
                "2",
                "--n-jobs",
                "1",
                "--fp-bits",
                "256",
                "--output-dir",
                str(model_dir),
            )
            self.assertEqual(trained.returncode, 0, msg=trained.stderr + trained.stdout)
            for name in [
                "model.joblib",
                "metrics.json",
                "test_predictions.csv",
                "split_assignments.csv",
                "data_audit.json",
                "model_card.md",
            ]:
                self.assertTrue((model_dir / name).is_file(), name)
            metrics = json.loads((model_dir / "metrics.json").read_text())
            self.assertIn(
                metrics["winner"], {"random_forest", "svm", "gradient_boosting"}
            )
            self.assertEqual(metrics["positive_label"], "active")
            self.assertEqual(
                metrics["selection_rule"],
                "highest inner-CV score; holdout did not choose model",
            )

            library_csv = work / "library.csv"
            pd.DataFrame(
                {
                    "smiles": [
                        "CCc1ccccc1",
                        "CCCO",
                        "c1ncccc1",
                        "broken-smiles",
                    ]
                }
            ).to_csv(library_csv, index=False)
            output_csv = work / "predictions.csv"
            predicted = run_cli(
                "predict",
                "--model",
                str(model_dir / "model.joblib"),
                "--trust-model",
                "--input",
                str(library_csv),
                "--smiles-column",
                "smiles",
                "--output",
                str(output_csv),
            )
            self.assertEqual(
                predicted.returncode, 0, msg=predicted.stderr + predicted.stdout
            )
            predictions = pd.read_csv(output_csv)
            self.assertEqual(len(predictions), 4)
            self.assertIn("nearest_training_similarity", predictions.columns)
            self.assertIn("applicability_domain", predictions.columns)
            self.assertEqual((predictions["status"] == "ok").sum(), 3)
            self.assertEqual((predictions["status"] != "ok").sum(), 1)

    def test_temporal_duplicate_guard_and_calibration(self) -> None:
        """A parent with a late replicate must not leak its aggregate into early training."""
        with tempfile.TemporaryDirectory(prefix="classical-ml-dd-time-") as temporary:
            work = Path(temporary)
            rows: list[dict[str, str]] = []
            for index, (active, inactive) in enumerate(zip(AROMATIC, ALIPHATIC)):
                rows.append(
                    {
                        "smiles": active,
                        "activity": "active",
                        "measured_at": (
                            pd.Timestamp("2024-01-01") + pd.Timedelta(days=2 * index)
                        )
                        .date()
                        .isoformat(),
                    }
                )
                rows.append(
                    {
                        "smiles": inactive,
                        "activity": "inactive",
                        "measured_at": (
                            pd.Timestamp("2024-01-01")
                            + pd.Timedelta(days=2 * index + 1)
                        )
                        .date()
                        .isoformat(),
                    }
                )
            # The first molecule has an identical late label. Its aggregate must carry the latest
            # timestamp and be held out, rather than inheriting the first row's early timestamp.
            rows.append(
                {
                    "smiles": AROMATIC[0],
                    "activity": "active",
                    "measured_at": "2024-02-15",
                }
            )
            train_csv = work / "temporal.csv"
            pd.DataFrame(rows).to_csv(train_csv, index=False)
            model_dir = work / "model"
            trained = run_cli(
                "train",
                "--input",
                str(train_csv),
                "--smiles-column",
                "smiles",
                "--target-column",
                "activity",
                "--task",
                "classification",
                "--positive-label",
                "active",
                "--split",
                "time",
                "--time-column",
                "measured_at",
                "--models",
                "rf",
                "--calibrate",
                "--fast",
                "--cv-folds",
                "3",
                "--n-jobs",
                "1",
                "--fp-bits",
                "128",
                "--output-dir",
                str(model_dir),
            )
            self.assertEqual(trained.returncode, 0, msg=trained.stderr + trained.stdout)
            audit = json.loads((model_dir / "data_audit.json").read_text())
            self.assertEqual(
                audit["temporal_parent_assignment"], "latest_source_timestamp"
            )
            assignments = pd.read_csv(model_dir / "split_assignments.csv")
            benzene = assignments.loc[
                assignments["canonical_smiles"] == "c1ccccc1"
            ].iloc[0]
            self.assertEqual(benzene["split"], "test")
            self.assertTrue(
                str(benzene["latest_source_timestamp"]).startswith("2024-02-15")
            )
            metrics = json.loads((model_dir / "metrics.json").read_text())
            self.assertTrue(metrics["models"]["random_forest"]["calibration_requested"])
            self.assertTrue(metrics["models"]["random_forest"]["calibration_applied"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
