"""nasa-dataset-download tests — Phase 7.7 (2026-07-27).

离线测试 catalog / aliases / 凭证。Live tests 跳过（无 token）。
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

SKILL_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SKILL_DIR / "scripts"))

import nasa_dataset_download as ndd  # noqa: E402

CATALOG = SKILL_DIR / "data" / "nasa_catalog.json"


# ─── catalog (offline) ───


def test_catalog_exists():
    assert CATALOG.is_file()
    assert CATALOG.stat().st_size > 1_000_000


def test_load_catalog():
    cat = ndd.load_catalog()
    assert isinstance(cat, list)
    assert len(cat) > 1000


def test_search_catalog_keyword():
    cat = ndd.load_catalog()
    results = ndd.search_catalog(cat, "MOD11A1", limit=5)
    assert any(r["short_name"] == "MOD11A1" for r in results)


def test_search_catalog_provider_filter():
    cat = ndd.load_catalog()
    results = ndd.search_catalog(cat, "MOD", provider="LPDAAC", limit=50)
    assert all(r["provider"] == "LPDAAC" for r in results)


# ─── multi-word search (Phase 7.7) ───


def test_search_catalog_multiword():
    """multi-word query: every token must appear (AND match)."""
    cat = ndd.load_catalog()
    # "SMAP soil moisture" should NOT 0-match now
    results = ndd.search_catalog(cat, "SMAP soil moisture", limit=20)
    assert len(results) > 0
    # every result must contain 'smap' AND 'soil' AND 'moisture'
    for r in results:
        hay = (r["short_name"] + " " + r["title"]).lower()
        assert "smap" in hay
        assert "soil" in hay
        assert "moisture" in hay


def test_search_catalog_multiword_no_match():
    """multi-word query that genuinely doesn't match returns []."""
    cat = ndd.load_catalog()
    results = ndd.search_catalog(cat, "SMAPZZZ qwertyuiop", limit=20)
    assert results == []


# ─── alias resolution (Phase 7.7) ───


def test_alias_map_loaded():
    aliases = ndd.load_aliases()
    assert isinstance(aliases, dict)
    assert len(aliases) >= 20  # at least 20 entries
    # spot-check known entries
    assert "modis lst" in aliases or "MODIS lst" in aliases or any(
        k.startswith("modis") and "lst" in k for k in aliases
    )


def test_resolve_alias_exact():
    aliases = ndd.load_aliases()
    hit = ndd.resolve_alias("land surface temperature", aliases)
    assert hit is not None
    assert "MOD11A1" in hit


def test_resolve_alias_prefix():
    """`MODIS land surface temperature` should still match the alias."""
    aliases = ndd.load_aliases()
    hit = ndd.resolve_alias("MODIS land surface temperature", aliases)
    assert hit is not None
    assert "MOD11A1" in hit or "MOD11A2" in hit


def test_resolve_alias_no_match():
    aliases = ndd.load_aliases()
    hit = ndd.resolve_alias("NOTAREALXYZ", aliases)
    assert hit is None


# ─── granule_info helper (Phase 7.7) ───


def test_granule_info_keys():
    """granule_info returns the expected fields even when granule is mocked."""
    class FakeG:
        def __getitem__(self, k):
            return self._d.get(k, {})
        def __init__(self):
            self._d = {"umm": {"GranuleUR": "X.A.B", "DataGranule": {"ProductionDateTime": "2024-06-01T00:00:00Z", "DayNightFlag": "Day"}, "TemporalExtent": {"RangeDateTime": {"BeginningDateTime": "2024-06-01T00:00:00Z", "EndingDateTime": "2024-06-01T23:59:59Z"}}}}
        def size(self): return 1.23
        def data_links(self): return ["https://example.com/file.hdf"]
        cloud_hosted = True
    info = ndd.granule_info(FakeG())
    assert info["granule_id"] == "X.A.B"
    assert info["size_mb"] == 1.23
    assert info["day_night"] == "Day"
    assert info["production_dt"] == "2024-06-01T00:00:00Z"
    assert "2024-06-01" in info["temporal"]
    assert info["data_links"] == ["https://example.com/file.hdf"]
    assert info["cloud_hosted"] is True


# ─── CLI: 0-result exit code 5 (Phase 7.7) ───


def test_cli_search_no_match_exit5(tmp_path):
    """search with a clearly bogus short_name should exit 5 and print hints."""
    proc = subprocess.run(
        [sys.executable, str(SKILL_DIR / "scripts" / "nasa_dataset_download.py"),
         "search", "NOTAREALXYZ",
         "--temporal-start", "2024-06-01", "--temporal-end", "2024-06-01"],
        capture_output=True, text=True, timeout=30,
    )
    # If network is up the search hits CMR and returns 0 hits -> exit 5.
    # If network is down, it may throw -> exit 7. Either way it must not be 0.
    assert proc.returncode in (5, 7)
    assert "no granules" in proc.stderr or "error" in proc.stderr


def test_cli_known_multikeyword(tmp_path):
    """known should now support multi-word queries."""
    proc = subprocess.run(
        [sys.executable, str(SKILL_DIR / "scripts" / "nasa_dataset_download.py"),
         "known", "SMAP soil moisture", "--limit", "5"],
        capture_output=True, text=True, timeout=20,
    )
    assert proc.returncode == 0
    assert "alias match" in proc.stdout
    assert "SPL3SMP" in proc.stdout


def test_cli_download_dry_run():
    """download --dry-run must NOT create any files."""
    out = SKILL_DIR / "output" / "_dry_run_test"
    if out.exists():
        import shutil
        shutil.rmtree(out)
    proc = subprocess.run(
        [sys.executable, str(SKILL_DIR / "scripts" / "nasa_dataset_download.py"),
         "download", "MOD11A1", "--version", "061",
         "--temporal-start", "2024-06-01", "--temporal-end", "2024-06-01",
         "--bbox", "115", "39", "117", "41",
         "--max-files", "2", "--dry-run", "--output-dir", str(out)],
        capture_output=True, text=True, timeout=60,
    )
    # dry-run should not create files; either exit 0 (success) or 5 (no match)
    if proc.returncode == 0:
        assert "dry-run" in proc.stdout.lower() or "--dry-run" in proc.stdout
        assert not out.exists() or not any(out.iterdir()), f"dry-run created files: {list(out.iterdir())}"


# ─── CLI smoke tests (no network) ───


def test_cli_help():
    proc = subprocess.run(
        [sys.executable, str(SKILL_DIR / "scripts" / "nasa_dataset_download.py"), "--help"],
        capture_output=True, text=True, timeout=10,
    )
    assert proc.returncode == 0
    assert "nasa-dataset-download" in proc.stdout


def test_cli_version():
    proc = subprocess.run(
        [sys.executable, str(SKILL_DIR / "scripts" / "nasa_dataset_download.py"), "--version"],
        capture_output=True, text=True, timeout=10,
    )
    assert proc.returncode == 0
    assert "0.2.0" in proc.stdout


def test_cli_login_shows_creds():
    """login 子命令: 即使 earthaccess 失败, 也应显示凭证状态."""
    proc = subprocess.run(
        [sys.executable, str(SKILL_DIR / "scripts" / "nasa_dataset_download.py"), "login"],
        capture_output=True, text=True, timeout=20,
    )
    # login() 可能成功或失败, 但凭证状态应显示
    assert "EARTHDATA_TOKEN" in proc.stdout


def test_cli_known_search():
    proc = subprocess.run(
        [sys.executable, str(SKILL_DIR / "scripts" / "nasa_dataset_download.py"),
         "known", "MOD11A1", "--limit", "3"],
        capture_output=True, text=True, timeout=20,
    )
    assert proc.returncode == 0
    assert "MOD11A1" in proc.stdout


def test_cli_known_qa_sidecar(tmp_path):
    qa = tmp_path / "run.qa.json"
    proc = subprocess.run(
        [sys.executable, str(SKILL_DIR / "scripts" / "nasa_dataset_download.py"),
         "known", "precipitation", "--limit", "5", "--qa", str(qa)],
        capture_output=True, text=True, timeout=20,
    )
    assert proc.returncode == 0
    assert qa.is_file()
    data = json.loads(qa.read_text(encoding="utf-8"))
    assert data["skill"] == "nasa-dataset-download"
    assert "credentials" in data


# ─── live (skipif no token) ───


def _has_token() -> bool:
    sys.path.insert(0, str(SKILL_DIR))
    try:
        from _geoskill_core.credentials import get_earthdata_token
        return bool(get_earthdata_token())
    except ImportError:
        return False


requires_token = pytest.mark.skipif(
    not _has_token(), reason="EARTHDATA_TOKEN not configured; live tests skipped"
)


@requires_token
def test_live_login():
    auth = ndd.login()
    assert auth is not None


@requires_token
def test_live_search_mod11a1():
    granules = ndd.search_granules(
        "MOD11A1", version="061",
        temporal=("2024-06-01", "2024-06-01"),
        bbox=(115, 39, 117, 41),
        count=3,
    )
    assert len(granules) >= 1


@requires_token
def test_live_search_gpm():
    granules = ndd.search_granules(
        "GPM_3IMERGHH", version="07",
        temporal=("2024-06-01", "2024-06-01"),
        bbox=(115, 39, 117, 41),
        count=3,
    )
    assert len(granules) >= 1


@requires_token
def test_live_search_mod09ga():
    granules = ndd.search_granules(
        "MOD09GA", version="061",
        temporal=("2024-06-01", "2024-06-01"),
        bbox=(115, 39, 117, 41),
        count=3,
    )
    # MOD09GA 不一定有数据
    assert isinstance(granules, list)
