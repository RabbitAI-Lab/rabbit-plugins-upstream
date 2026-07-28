"""nasa-dataset-catalog tests — Phase 7.5 (2026-07-27).

Covers:
- catalog loading + normalize_record + search_catalog (offline, no network)
- cmr_search_granules (live CMR with mocked HTTP)
- download_granule (live with --max-bytes)
- end-to-end CLI smoke test (auth, stats, search, info, granules, download)
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path
from unittest import mock

import pytest

# Make the skill importable
SKILL_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SKILL_DIR / "scripts"))

import nasa_dataset_catalog as ndc  # noqa: E402

CATALOG = SKILL_DIR / "data" / "nasa_catalog.json"


# ─────────────────────────────────────────────────────────────────────
# Catalog (offline, no network)
# ─────────────────────────────────────────────────────────────────────


def test_catalog_exists():
    assert CATALOG.is_file(), f"offline catalog missing: {CATALOG}"
    assert CATALOG.stat().st_size > 1_000_000, "catalog should be > 1MB"


def test_load_catalog_returns_list():
    catalog = ndc.load_catalog()
    assert isinstance(catalog, list)
    assert len(catalog) > 1000, f"only {len(catalog)} records"


def test_normalize_record_strips_short_name():
    rec = {"ShortName": "\n  MOD11A1\n  ", "EntryTitle": "  Test  "}
    norm = ndc.normalize_record(rec)
    assert norm["short_name"] == "MOD11A1"
    assert norm["title"] == "Test"


def test_search_catalog_finds_mod11a1():
    catalog = ndc.load_catalog()
    results = ndc.search_catalog(catalog, "MOD11A1", limit=10)
    assert len(results) >= 1
    assert any(r["short_name"] == "MOD11A1" for r in results)


def test_search_catalog_keyword_in_title():
    catalog = ndc.load_catalog()
    results = ndc.search_catalog(catalog, "precipitation", limit=10)
    # 应该有匹配 GPM / IMERG / 3IMERG 之类的数据集
    assert len(results) >= 1


def test_search_catalog_empty_keyword():
    catalog = ndc.load_catalog()
    assert ndc.search_catalog(catalog, "") == []


def test_search_catalog_provider_filter():
    catalog = ndc.load_catalog()
    # LPDAAC 是 MODIS 主要 provider
    results = ndc.search_catalog(
        catalog, "MOD", provider="LPDAAC", limit=50
    )
    assert all(r["provider"] == "LPDAAC" for r in results)


def test_search_catalog_no_match():
    catalog = ndc.load_catalog()
    results = ndc.search_catalog(catalog, "ZZZZ_NOMATCH_ZZZZ", limit=10)
    assert results == []


# ─────────────────────────────────────────────────────────────────────
# Catalog stats
# ─────────────────────────────────────────────────────────────────────


def test_catalog_stats_keys():
    catalog = ndc.load_catalog()
    stats = ndc.catalog_stats(catalog)
    for k in ("total_records", "with_bbox", "with_doi",
              "top_providers", "year_distribution", "unique_short_names"):
        assert k in stats
    assert stats["total_records"] == len(catalog)
    assert stats["total_records"] > 10000


# ─────────────────────────────────────────────────────────────────────
# URL extraction
# ─────────────────────────────────────────────────────────────────────


def test_granule_download_url_with_data_rel():
    entry = {
        "links": [
            {"rel": "http://esipfed.org/ns/fedsearch/1.1/data#", "href": "https://x/y.HDF5"},
            {"rel": "http://esipfed.org/ns/fedsearch/1.1/metadata#", "href": "https://x/meta"},
        ]
    }
    assert ndc.granule_download_url(entry) == "https://x/y.HDF5"


def test_granule_download_url_with_enclosure():
    entry = {"links": [{"rel": "enclosure", "href": "https://x/file.hdf"}]}
    assert ndc.granule_download_url(entry) == "https://x/file.hdf"


def test_granule_download_url_none():
    assert ndc.granule_download_url({"links": []}) is None
    assert ndc.granule_download_url({}) is None


# ─────────────────────────────────────────────────────────────────────
# Live CMR (network — skip if no token)
# ─────────────────────────────────────────────────────────────────────


def _has_token() -> bool:
    sys.path.insert(0, str(SKILL_DIR))
    try:
        from _geoskill_core.credentials import get_earthdata_token
        return bool(get_earthdata_token())
    except ImportError:
        return False


requires_token = pytest.mark.skipif(
    not _has_token(), reason="EARTHDATA_TOKEN not configured; live CMR tests skipped"
)


@requires_token
def test_live_cmr_search_granules_mod11a1():
    entries = ndc.cmr_search_granules(
        "MOD11A1",
        version="061",
        temporal="2024-06-01,2024-06-02",
        bbox=[115, 39, 117, 41],
        limit=5,
    )
    assert len(entries) >= 1
    # 至少一个 granule 应该有 download URL
    urls = [ndc.granule_download_url(e) for e in entries]
    assert any(u for u in urls)


@requires_token
def test_live_cmr_search_collections():
    entries = ndc.cmr_search_collections("MOD11A1", limit=3)
    assert len(entries) >= 1


# ─────────────────────────────────────────────────────────────────────
# Download (network)
# ─────────────────────────────────────────────────────────────────────


@requires_token
def test_download_granule_max_bytes(tmp_path):
    """Download first 1 MB of a MOD11A1 HDF to verify flow."""
    entries = ndc.cmr_search_granules(
        "MOD11A1", version="061",
        temporal="2024-06-01,2024-06-01",
        bbox=[115, 39, 117, 41],
        limit=1,
    )
    assert entries, "no granule"
    url = ndc.granule_download_url(entries[0])
    assert url, "no url"
    out = tmp_path / "mod11a1_1mb.hdf"
    size = ndc.download_granule(url, out, max_bytes=1024 * 1024)
    assert 500_000 < size <= 1_100_000, f"size {size} out of range"
    assert out.is_file()
    assert out.stat().st_size == size


# ─────────────────────────────────────────────────────────────────────
# CLI (subprocess)
# ─────────────────────────────────────────────────────────────────────


def test_cli_auth_runs():
    """auth subcommand should always work (no network needed if cached)."""
    proc = subprocess.run(
        [sys.executable, str(SKILL_DIR / "scripts" / "nasa_dataset_catalog.py"), "auth"],
        capture_output=True, text=True, timeout=15,
    )
    assert proc.returncode == 0
    assert "EARTHDATA_TOKEN" in proc.stdout


def test_cli_stats_runs():
    proc = subprocess.run(
        [sys.executable, str(SKILL_DIR / "scripts" / "nasa_dataset_catalog.py"),
         "stats", "--format", "json"],
        capture_output=True, text=True, timeout=30,
    )
    assert proc.returncode == 0, f"stderr={proc.stderr!r}"
    data = json.loads(proc.stdout)
    assert data["total_records"] > 10000


def test_cli_search_runs():
    proc = subprocess.run(
        [sys.executable, str(SKILL_DIR / "scripts" / "nasa_dataset_catalog.py"),
         "search", "precipitation", "--format", "json", "--limit", "5"],
        capture_output=True, text=True, timeout=30,
    )
    assert proc.returncode == 0, f"stderr={proc.stderr!r}"
    data = json.loads(proc.stdout)
    # --format json 返回 {offline: [...], live_cmr: [...], cmr_error: ...}
    assert "offline" in data and "live_cmr" in data
    assert len(data["offline"]) >= 1


def test_cli_search_no_match():
    proc = subprocess.run(
        [sys.executable, str(SKILL_DIR / "scripts" / "nasa_dataset_catalog.py"),
         "search", "ZZZZZ_NOMATCH_ZZZZ", "--limit", "5"],
        capture_output=True, text=True, timeout=30,
    )
    assert proc.returncode == 0
    assert "0 match" in proc.stdout


def test_cli_info_no_match_exits_5():
    proc = subprocess.run(
        [sys.executable, str(SKILL_DIR / "scripts" / "nasa_dataset_catalog.py"),
         "info", "ZZZZ_NOMATCH"],
        capture_output=True, text=True, timeout=15,
    )
    assert proc.returncode == 5


def test_cli_qa_sidecar(tmp_path):
    qa = tmp_path / "run.qa.json"
    proc = subprocess.run(
        [sys.executable, str(SKILL_DIR / "scripts" / "nasa_dataset_catalog.py"),
         "stats", "--qa", str(qa)],
        capture_output=True, text=True, timeout=30,
    )
    assert proc.returncode == 0, f"stderr={proc.stderr!r}"
    assert qa.is_file()
    qa_data = json.loads(qa.read_text(encoding="utf-8"))
    assert qa_data["skill"] == "nasa-dataset-catalog"
    assert qa_data["command"] == "stats"
    assert "credentials" in qa_data
    # 必须不泄露密码
    raw = qa.read_text(encoding="utf-8")
    for forbidden in ("Ruiduobao123", "supersecret"):
        assert forbidden not in raw


def test_cli_help_exits_0():
    proc = subprocess.run(
        [sys.executable, str(SKILL_DIR / "scripts" / "nasa_dataset_catalog.py"),
         "--help"],
        capture_output=True, text=True, timeout=10,
    )
    assert proc.returncode == 0
    assert "nasa-dataset-catalog" in proc.stdout


def test_cli_version_exits_0():
    proc = subprocess.run(
        [sys.executable, str(SKILL_DIR / "scripts" / "nasa_dataset_catalog.py"),
         "--version"],
        capture_output=True, text=True, timeout=10,
    )
    assert proc.returncode == 0
    assert "0.1.0" in proc.stdout
