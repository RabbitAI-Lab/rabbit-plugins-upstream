"""Tests for CLI interface."""

import os
import sys
import tempfile
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import rs_index_calc


class TestCLI:
    """Test command-line interface."""

    def test_version(self, capsys):
        """Test version flag."""
        import sys
        old_argv = sys.argv
        try:
            sys.argv = ["rs-index-calc"]
            with pytest.raises(SystemExit) as exc_info:
                rs_index_calc.main()
            assert exc_info.value.code == 0
        finally:
            sys.argv = old_argv

    def test_help(self, capsys):
        """Test help output."""
        sys.argv = ["rs-index-calc", "--help"]
        with pytest.raises(SystemExit) as exc_info:
            rs_index_calc.main()
        assert exc_info.value.code == 0

    def test_missing_input(self):
        """Test missing input file error."""
        sys.argv = ["rs-index-calc", "nonexistent.tif", "NDVI"]
        with pytest.raises(SystemExit) as exc_info:
            rs_index_calc.main()
        assert exc_info.value.code == 1

    def test_no_index_no_batch(self):
        """Test no index specified."""
        with tempfile.NamedTemporaryFile(suffix=".tif", delete=False) as f:
            f.write(b"dummy")
            temp_path = f.name
        try:
            sys.argv = ["rs-index-calc", temp_path]
            with pytest.raises(SystemExit) as exc_info:
                rs_index_calc.main()
            assert exc_info.value.code == 1
        finally:
            os.unlink(temp_path)

    def test_supported_indices_list(self):
        """Test all supported indices are listed."""
        indices = rs_index_calc.INDEX_FORMULAS
        assert len(indices) == 10
        assert "NDVI" in indices
        assert "NDBI" in indices
        assert "NDWI" in indices
        assert "EVI" in indices
        assert "SAVI" in indices
        assert "MNDWI" in indices
        assert "AWEI" in indices
        assert "NBR" in indices
        assert "BSI" in indices
        assert "UI" in indices

    def test_index_formula_structure(self):
        """Test index formula structure."""
        for name, info in rs_index_calc.INDEX_FORMULAS.items():
            assert "bands" in info, f"{name} missing 'bands'"
            assert "formula" in info, f"{name} missing 'formula'"
            assert isinstance(info["bands"], list), f"{name} 'bands' should be list"
            assert len(info["bands"]) >= 2, f"{name} should have at least 2 bands"

    def test_band_aliases_coverage(self):
        """Test band aliases cover all standard bands."""
        expected_bands = ["red", "green", "blue", "nir", "swir1", "swir2"]
        for band in expected_bands:
            assert band in rs_index_calc.BAND_ALIASES, f"Missing alias for {band}"

    def test_help_includes_qa_flag(self):
        """Phase 5: --qa should be in --help output."""
        import subprocess
        script = os.path.join(os.path.dirname(__file__), "..", "rs-index-calc.py")
        result = subprocess.run(
            [sys.executable, script, "--help"],
            capture_output=True, text=True, timeout=10,
        )
        assert "--qa" in result.stdout


class TestQaSummary:
    """Phase 5: --qa sidecar summary tests for rs-index-calc."""

    def test_write_qa_summary_single(self, tmp_path):
        """write_qa_summary should record input / index / output for a single run."""
        import json as _json
        import argparse as _ap
        qa_path = str(tmp_path / "run.qa.json")
        args = _ap.Namespace(
            input="input.tif", index="NDVI", output="out.tif",
            batch=False, batch_dir=None, formula=None,
        )
        rs_index_calc.write_qa_summary(
            qa_path, args, "single",
            [{"index": "NDVI", "output": "out.tif", "ok": True}],
        )
        assert os.path.exists(qa_path)
        data = _json.load(open(qa_path, encoding="utf-8"))
        assert data["skill"] == "rs-index-calc"
        assert data["run_kind"] == "single"
        assert data["input"] == "input.tif"
        assert data["index"] == "NDVI"
        assert data["output"] == "out.tif"
        assert data["computed_indices"] == ["NDVI"]
        assert data["n_ok"] == 1
        assert data["n_err"] == 0
        assert "timestamp" in data
        assert "version" in data

    def test_write_qa_summary_batch(self, tmp_path):
        """write_qa_summary should aggregate computed indices for a batch run."""
        import json as _json
        import argparse as _ap
        qa_path = str(tmp_path / "run.qa.json")
        args = _ap.Namespace(
            input="scene.tif", index=None, output=None,
            batch=True, batch_dir=None, formula=None,
        )
        results = [
            {"index": "NDVI", "output": "scene_NDVI.tif", "ok": True},
            {"index": "NDBI", "output": "scene_NDBI.tif", "ok": True},
            {"index": "NDWI", "error": "no green band", "ok": False},
        ]
        rs_index_calc.write_qa_summary(qa_path, args, "batch", results)
        data = _json.load(open(qa_path, encoding="utf-8"))
        assert data["run_kind"] == "batch"
        assert data["batch"] is True
        assert sorted(data["computed_indices"]) == ["NDBI", "NDVI", "NDWI"]
        assert data["n_ok"] == 2
        assert data["n_err"] == 1
        assert data["errors"] == ["no green band"]
        assert len(data["outputs"]) == 2

    def test_write_qa_summary_creates_parent_dir(self, tmp_path):
        """write_qa_summary should create the parent directory if missing."""
        import json as _json
        import argparse as _ap
        qa_path = str(tmp_path / "subdir" / "deep" / "run.qa.json")
        args = _ap.Namespace(
            input="x.tif", index="NDVI", output=None,
            batch=False, batch_dir=None, formula=None,
        )
        rs_index_calc.write_qa_summary(
            qa_path, args, "single", [{"index": "NDVI", "ok": True}],
        )
        assert os.path.exists(qa_path)
        data = _json.load(open(qa_path, encoding="utf-8"))
        assert data["input"] == "x.tif"


# ---------------------------------------------------------------------------
# Phase 6 — --format {text, json} for --list-indices
# ---------------------------------------------------------------------------


class TestFormatFlag:
    """`--format text|json` should control --list-indices output format."""

    def test_help_lists_format_flag(self):
        """`--help` should advertise the new --format flag."""
        import subprocess
        script = os.path.join(os.path.dirname(__file__), "..", "rs-index-calc.py")
        result = subprocess.run(
            [sys.executable, script, "--help"],
            capture_output=True, text=True, timeout=10,
        )
        assert "--format" in result.stdout
        # Choices should be visible
        assert "text" in result.stdout
        assert "json" in result.stdout

    def test_print_index_list_text_default(self, capsys):
        """Default --list-indices should print a human-readable text list."""
        rs_index_calc._print_index_list("text")
        out = capsys.readouterr().out
        # Should mention each supported index name
        for name in ("NDVI", "NDBI", "NDWI", "EVI", "SAVI", "MNDWI",
                     "AWEI", "NBR", "BSI", "UI"):
            assert name in out, f"missing {name} in text list"
        # Header phrase
        assert "Available indices" in out

    def test_print_index_list_json(self, capsys):
        """`--list-indices --format json` should produce parseable JSON."""
        import json as _json
        rs_index_calc._print_index_list("json")
        out = capsys.readouterr().out
        data = _json.loads(out)
        assert "indices" in data and isinstance(data["indices"], list)
        assert data["count"] == 10
        names = {idx["name"] for idx in data["indices"]}
        assert "NDVI" in names
        assert "EVI" in names
        # Each entry should have bands + formula
        ndvi = next(i for i in data["indices"] if i["name"] == "NDVI")
        assert "bands" in ndvi and "formula" in ndvi
        assert "nir" in ndvi["bands"]
        assert "red" in ndvi["bands"]
        assert "(NIR - RED)" in ndvi["formula"]

    def test_cli_list_indices_text(self):
        """Subprocess: `rs-index-calc --list-indices` (default text) should list all indices."""
        import subprocess
        script = os.path.join(os.path.dirname(__file__), "..", "rs-index-calc.py")
        result = subprocess.run(
            [sys.executable, script, "--list-indices"],
            capture_output=True, text=True, timeout=10,
        )
        assert result.returncode == 0
        assert "NDVI" in result.stdout
        assert "Available indices" in result.stdout

    def test_cli_list_indices_json(self):
        """Subprocess: `rs-index-calc --list-indices --format json` should produce JSON."""
        import subprocess
        import json as _json
        script = os.path.join(os.path.dirname(__file__), "..", "rs-index-calc.py")
        result = subprocess.run(
            [sys.executable, script, "--list-indices", "--format", "json"],
            capture_output=True, text=True, timeout=10,
        )
        assert result.returncode == 0
        data = _json.loads(result.stdout)
        assert data["count"] == 10

    def test_cli_list_indices_format_rejects_invalid(self):
        """`--format yaml` should be rejected by argparse."""
        import subprocess
        script = os.path.join(os.path.dirname(__file__), "..", "rs-index-calc.py")
        result = subprocess.run(
            [sys.executable, script, "--list-indices", "--format", "yaml"],
            capture_output=True, text=True, timeout=10,
        )
        assert result.returncode != 0
