"""Tests for hts-changes.json parsing."""
import shutil
from pathlib import Path

from conftest import FIXTURES
from src.crawler.httrack_engine import HTTrackMirrorEngine


def test_parse_changes_file(tmp_path: Path):
    mirror = tmp_path / "mirror"
    mirror.mkdir()
    shutil.copy(FIXTURES / "sample_hts_changes.json", mirror / "hts-changes.json")

    changes = HTTrackMirrorEngine.parse_changes(mirror / "hts-changes.json")
    assert changes["new"] == ["www.example-chem.ir/catalog/product-1.html"]
    assert changes["modified"] == ["www.example-chem.ir/catalog/product-2.html"]
    assert changes["unchanged"] == ["www.example-chem.ir/catalog/product-3.html"]
    assert changes["removed"] == ["www.example-chem.ir/catalog/product-4.html"]


def test_parse_missing_file():
    changes = HTTrackMirrorEngine.parse_changes(Path("/nonexistent/hts-changes.json"))
    assert changes == {"new": [], "modified": [], "unchanged": [], "removed": []}


def test_get_changed_files_falls_back_to_all(tmp_path: Path):
    from src.crawler.httrack_config import HTTrackMirrorConfig
    engine = HTTrackMirrorEngine(base_dir=str(tmp_path))
    cfg = HTTrackMirrorConfig(supplier_id=1, project_name="x", urls=["https://x.com"],
                              output_dir=str(tmp_path / "x"))
    files = engine.get_changed_files(cfg)  # no hts-changes.json -> all parseable (none)
    assert files == []
