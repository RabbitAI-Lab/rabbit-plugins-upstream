"""End-to-end integration test: download + convert + validate SHP.

Skipped if no network. Marks files for cleanup.
"""

from __future__ import annotations

import socket
import zipfile
from pathlib import Path

import geopandas as gpd
import pytest

from core import cache as cache_mod
from core import format as fmt_mod
from core import geoboundaries


def _has_network(timeout: float = 5.0) -> bool:
    try:
        socket.create_connection(("www.geoboundaries.org", 443), timeout=timeout).close()
        return True
    except OSError:
        return False


pytestmark = pytest.mark.skipif(
    not _has_network(), reason="no network"
)


@pytest.fixture(scope="module")
def chn_adm0_zip(tmp_path_factory) -> Path:
    cache = cache_mod.HttpCache(tmp_path_factory.mktemp("cache"))
    return geoboundaries.download_zip("CHN", "ADM0", cache=cache)


def test_read_input_from_zip(chn_adm0_zip):
    gdf = fmt_mod.read_input(chn_adm0_zip)
    assert isinstance(gdf, gpd.GeoDataFrame)
    assert len(gdf) == 1  # China ADM0 is a single polygon
    assert gdf.crs.to_epsg() == 4326


def test_convert_to_geojson(chn_adm0_zip, tmp_path: Path):
    out = fmt_mod.convert(chn_adm0_zip, tmp_path / "chn_adm0.geojson", "geojson")
    assert out.exists()
    gdf = gpd.read_file(out)
    assert len(gdf) == 1
    assert gdf.crs.to_epsg() == 4326


def test_convert_to_gpkg(chn_adm0_zip, tmp_path: Path):
    out = fmt_mod.convert(chn_adm0_zip, tmp_path / "chn_adm0.gpkg", "gpkg")
    assert out.exists()
    gdf = gpd.read_file(out)
    assert len(gdf) == 1


def test_convert_to_shp_passthrough(chn_adm0_zip, tmp_path: Path):
    out = fmt_mod.convert(chn_adm0_zip, tmp_path / "chn_adm0.zip", "shp")
    assert out.exists()
    # Should be a real zip containing .shp.
    assert zipfile.is_zipfile(out)
    with zipfile.ZipFile(out) as zf:
        names = zf.namelist()
        assert any(n.lower().endswith(".shp") for n in names)
        assert any(n.lower().endswith(".shx") for n in names)
        assert any(n.lower().endswith(".dbf") for n in names)


def test_convert_with_clip(chn_adm0_zip, tmp_path: Path):
    out = fmt_mod.convert(
        chn_adm0_zip,
        tmp_path / "chn_east.geojson",
        "geojson",
        clip_bbox=(100.0, 20.0, 130.0, 45.0),
    )
    assert out.exists()
    gdf = gpd.read_file(out)
    # China ADM0 is a single multipolygon; clipping should keep something.
    assert len(gdf) >= 1
