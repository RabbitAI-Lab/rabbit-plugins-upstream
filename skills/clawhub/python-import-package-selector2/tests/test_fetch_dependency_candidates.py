import sys
import unittest
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = ROOT_DIR / "scripts"

sys.path.insert(0, str(SCRIPTS_DIR))

from fetch_dependency_candidates import fetch_dependency_candidates  # noqa: E402


class TestPythonDependencyCandidateFetcher(unittest.TestCase):
    def assert_candidate_shape(self, item):
        self.assertIn("package_id", item)
        self.assertIn("package_name", item)
        self.assertIn("import_statement", item)
        self.assertIn("capability_summary", item)
        self.assertIn("best_for", item)
        self.assertNotIn("candidate_type", item)

    def test_tabular_query_returns_candidate_payload(self):
        query = (
            "I need to convert a table-like dataset into a list of rows while "
            "preserving column names and values. Which Python package should I import?"
        )
        result = fetch_dependency_candidates(
            query=query,
            top_k=3,
        )

        self.assertEqual(
            result["skill_name"],
            "python-dependency-candidate-fetcher",
        )
        self.assertEqual(
            result["skill_version"],
            "base_v0.1-apibench-python-dependency",
        )
        self.assertEqual(
            result["source"],
            "apibench_python_dependency_candidates",
        )
        self.assertEqual(result["dataset_variant"], "all50_5candidates_v1")
        self.assertEqual(result["scenario"], "python_import_package_selection")
        self.assertEqual(result["query_id"], "PY001")
        self.assertEqual(result["query"], query)
        self.assertEqual(result["match_type"], "exact")
        self.assertEqual(result["top_k"], 3)
        self.assertEqual(len(result["candidates"]), 3)
        self.assertEqual(
            [item["package_name"] for item in result["candidates"]],
            ["pandas", "dask", "polars"],
        )

        self.assertNotIn("gold_api", result)
        self.assertNotIn("gold_dependency", result)

        for item in result["candidates"]:
            self.assert_candidate_shape(item)

    def test_query_normalization_works(self):
        result = fetch_dependency_candidates(
            query=(
                "  i need to convert a table-like dataset into a list of rows while "
                "preserving column names and values. which python package should i import?  "
            ),
            top_k=4,
        )

        self.assertEqual(result["query_id"], "PY001")
        self.assertEqual(result["match_type"], "normalized")
        self.assertEqual(len(result["candidates"]), 4)

    def test_top_k_caps_returned_candidates(self):
        result = fetch_dependency_candidates(
            query=(
                "I need to calculate the mean value for each group in a table. "
                "Which Python package should I import?"
            ),
            top_k=2,
        )

        self.assertEqual(result["top_k"], 2)
        self.assertEqual(len(result["candidates"]), 2)
        self.assertEqual(result["candidates"][0]["package_name"], "pandas")
        self.assertEqual(result["candidates"][1]["package_name"], "dask")

    def test_empty_query_should_fail(self):
        with self.assertRaises(ValueError):
            fetch_dependency_candidates(query="", top_k=5)

    def test_invalid_top_k_should_fail(self):
        with self.assertRaises(ValueError):
            fetch_dependency_candidates(
                query=(
                    "I need to convert a table-like dataset into a list of rows while "
                    "preserving column names and values. Which Python package should I import?"
                ),
                top_k=0,
            )

    def test_unsupported_query_should_fail(self):
        with self.assertRaises(ValueError):
            fetch_dependency_candidates(
                query="How to make an async HTTP request in Python?",
                top_k=5,
            )


if __name__ == "__main__":
    unittest.main()
