"""Tests for the HTTrack CLI wrapper."""
import subprocess
from pathlib import Path

import pytest

from src.crawler.httrack_config import HTTrackMirrorConfig
from src.crawler.httrack_engine import HTTrackMirrorEngine


def _make_config(tmp_path: Path) -> HTTrackMirrorConfig:
    return HTTrackMirrorConfig(
        supplier_id=1, project_name="test_supplier",
        urls=["https://example.com"], output_dir=str(tmp_path / "test_supplier"),
    )


@pytest.mark.skipif(subprocess.run(["which", "httrack"], capture_output=True).returncode != 0,
                    reason="httrack not installed")
def test_engine_verifies_httrack(tmp_path):
    engine = HTTrackMirrorEngine(base_dir=str(tmp_path))
    assert engine is not None


def test_build_command_initial():
    cfg = _make_config(Path("/tmp/x"))
    cmd = cfg.to_flags(update=False)
    assert cmd[0] == "httrack"
    assert "https://example.com" in cmd
    assert "-O" in cmd
    assert "--depth=5" in cmd
    assert "--max-rate=25000" in cmd
    assert "+*.pdf" in cmd
    assert "-*.jpg" in cmd
    assert "--robots=2" in cmd
    assert "--connection-per-second=2.0" in cmd
    assert "-F" in cmd            # identifiable user agent
    assert "-q" in cmd
    # --depth and -r are the same httrack option; only one is emitted
    assert "-r5" not in cmd


def test_build_command_update():
    cfg = _make_config(Path("/tmp/x"))
    cmd = cfg.to_flags(update=True)
    assert "--update" in cmd
    assert "-O" in cmd
    # change detection is post-run (hts-changes.json / hts-cache/new.lst),
    # not a CLI flag on this httrack version
    assert "-%X" not in cmd


@pytest.mark.skipif(subprocess.run(["which", "httrack"], capture_output=True).returncode != 0,
                    reason="httrack not installed")
def test_mirror_roundtrip(tmp_path):
    engine = HTTrackMirrorEngine(base_dir=str(tmp_path))
    cfg = HTTrackMirrorConfig(
        supplier_id=1, project_name="example", urls=["https://example.com"],
        output_dir=str(tmp_path / "example"), depth=1, sockets=2, max_time=60,
    )
    stats = engine.mirror_supplier(cfg)
    assert stats["return_code"] == 0
    assert stats["total_files"] >= 1


# ── v2.9: graceful degradation without httrack ─────────────────────────────
def test_mirror_graceful_when_httrack_missing(tmp_path):
    from src.crawler.httrack_config import HTTrackMirrorConfig
    eng = HTTrackMirrorEngine(str(tmp_path), require_httrack=False)
    eng.httrack_bin = None  # simulate missing binary
    cfg = HTTrackMirrorConfig(supplier_id=1, project_name="t",
                              urls=["https://x.com"], output_dir=str(tmp_path / "out"))
    r = eng.mirror_supplier(cfg)
    assert r["return_code"] == 127
    assert r["error"] == "httrack-not-installed"
    assert r["html_files"] == 0
    assert r["total_files"] == 0


def test_build_command_uses_resolved_binary(tmp_path):
    from src.crawler.httrack_config import HTTrackMirrorConfig
    eng = HTTrackMirrorEngine(str(tmp_path), require_httrack=False)
    eng.httrack_bin = "/custom/httrack"
    cfg = HTTrackMirrorConfig(supplier_id=1, project_name="t",
                              urls=["https://x.com"], output_dir=str(tmp_path / "out"))
    cmd = eng.build_command(cfg)
    assert cmd[0] == "/custom/httrack"


def test_require_httrack_true_raises_only_when_missing(tmp_path, monkeypatch):
    import shutil
    orig = shutil.which
    monkeypatch.setattr(shutil, "which", lambda name: None)  # pretend nothing installed
    import pytest
    with pytest.raises(RuntimeError):
        HTTrackMirrorEngine(str(tmp_path), require_httrack=True)
    monkeypatch.setattr(shutil, "which", orig)
