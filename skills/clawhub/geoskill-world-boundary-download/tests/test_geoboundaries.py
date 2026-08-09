"""Integration tests for the geoBoundaries source.

These tests make live HTTP calls. They are skipped when no network is
available or the geoBoundaries API is unreachable.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from core import cache as cache_mod
from core import geoboundaries


pytestmark = pytest.mark.network


@pytest.fixture
def cache(tmp_path: Path) -> cache_mod.HttpCache:
    return cache_mod.HttpCache(tmp_path)


def _has_network(timeout: float = 5.0) -> bool:
    """Quick reachability check; skip integration tests if no internet."""

    import socket
    try:
        socket.create_connection(("www.geoboundaries.org", 443), timeout=timeout).close()
        return True
    except OSError:
        return False


pytestmark_skip = pytest.mark.skipif(
    not _has_network(), reason="no network or geoboundaries.org unreachable"
)


@pytest.mark.skipif(not _has_network(), reason="no network")
def test_fetch_metadata_chn_adm1(cache):
    meta = geoboundaries.fetch_metadata("CHN", "ADM1", cache=cache)
    assert meta is not None
    assert meta.get("boundaryISO") == "CHN"
    assert meta.get("boundaryType") == "ADM1"
    assert "staticDownloadLink" in meta


@pytest.mark.skipif(not _has_network(), reason="no network")
def test_fetch_metadata_404_returns_none(cache):
    # Random ISO that likely does not exist; API returns 404 -> None.
    meta = geoboundaries.fetch_metadata("XYZ", "ADM0", cache=cache)
    assert meta is None


@pytest.mark.skipif(not _has_network(), reason="no network")
def test_flatten_meta(cache):
    meta = geoboundaries.fetch_metadata("CHN", "ADM0", cache=cache)
    flat = geoboundaries.flatten_meta(meta)
    assert flat["iso3"] == "CHN"
    assert flat["name"] == "China"
    assert flat["level"] == "ADM0"


@pytest.mark.skipif(not _has_network(), reason="no network")
def test_list_available_levels_chn(cache):
    levels = geoboundaries.list_available_levels("CHN", cache=cache)
    assert "ADM0" in levels
    assert "ADM1" in levels


@pytest.mark.skipif(not _has_network(), reason="no network")
def test_download_zip_chn_adm0(cache):
    path = geoboundaries.download_zip("CHN", "ADM0", cache=cache)
    assert path.exists()
    assert path.stat().st_size > 0
    # The zip should be a real zip.
    import zipfile
    assert zipfile.is_zipfile(path)
    with zipfile.ZipFile(path) as zf:
        names = zf.namelist()
        assert any(n.lower().endswith(".shp") for n in names)
        assert any(n.lower().endswith(".geojson") for n in names)


@pytest.mark.skipif(not _has_network(), reason="no network")
def test_download_simplified_geojson(cache):
    path = geoboundaries.download_zip("CHN", "ADM0", cache=cache, simplified=True)
    assert path.exists()
    # .geojson starts with "{" not "PK".
    with open(path, "rb") as f:
        sig = f.read(2)
    assert sig != b"PK"
