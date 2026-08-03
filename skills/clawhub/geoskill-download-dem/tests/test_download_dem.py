"""Basic unit tests for download-dem skill (Phase 2 round 2).

These tests do NOT require network — they exercise pure utility functions
(bbox math, error class, source selection heuristics).  For real admin
resolution / DEM download, run integration tests separately.
"""
import importlib.util
import os
import sys
from unittest.mock import patch, MagicMock

import pytest

HERE = os.path.dirname(os.path.abspath(__file__))


def _load_module():
    name = "dem_download_test"
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, "..", "scripts", "dem_download.py"))
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m
    spec.loader.exec_module(m)
    return m


def test_bbox_area_zero():
    m = _load_module()
    with pytest.raises(Exception):  # DemError
        m.bbox_area_km2([0, 0, 0, 0])


def test_bbox_area_simple():
    m = _load_module()
    # 1° x 1° at equator ≈ 111 km x 111 km ≈ 12,321 km²
    area = m.bbox_area_km2([0, 0, 1, 1])
    assert 12_000 < area < 13_000


def test_bbox_overlap():
    m = _load_module()
    assert m.bbox_has_area_overlap([0, 0, 1, 1], [0.5, 0.5, 1.5, 1.5]) is True
    assert m.bbox_has_area_overlap([0, 0, 1, 1], [2, 2, 3, 3]) is False
    assert m.bbox_has_area_overlap([0, 0, 1, 1], [1, 1, 2, 2]) is False  # touch only


def test_expand_bbox_km():
    m = _load_module()
    # expand 10 km on each side at equator (1° lat ≈ 111 km → 10 km ≈ 0.09°)
    bbox = m.expand_bbox_km([100, 0, 101, 1], expand_km=10.0)
    assert bbox[0] < 100
    assert bbox[2] > 101
    assert bbox[1] < 0
    assert bbox[3] > 1


def test_normalize_admin_level():
    m = _load_module()
    assert m._normalize_admin_level("province") == "sheng"
    assert m._normalize_admin_level("shi") == "shi"
    assert m._normalize_admin_level("xian") == "xian"
    assert m._normalize_admin_level(None) == "xian"  # default
    with pytest.raises(Exception):  # DemError
        m._normalize_admin_level("unknown")


def test_normalize_bbox():
    m = _load_module()
    assert m.normalize_bbox((100.0, 0.0, 101.0, 1.0)) == (100.0, 0.0, 101.0, 1.0)
    # Out-of-order requires south < north — raises DemError, no auto-swap.
    with pytest.raises(Exception):  # DemError
        m.normalize_bbox((101.0, 1.0, 100.0, 0.0))


def test_select_source_aws_for_global():
    m = _load_module()
    # AWS source supports cop-dem-glo-30 (Copernicus 30m DEM, public)
    src, ds, _ = m.select_source("aws", "cop-dem-glo-30", 30.0, [100, 0, 101, 1])
    assert src == "aws"
    assert ds == "cop-dem-glo-30"


def test_select_source_mpc_for_cop30():
    m = _load_module()
    src, ds, _ = m.select_source("mpc", "cop-dem-glo-30", 30.0, [100, 0, 101, 1])
    assert src == "mpc"
    assert ds == "cop-dem-glo-30"


def test_resolve_admin_requires_name_or_code():
    m = _load_module()
    with pytest.raises(Exception):  # DemError
        m.resolve_admin(None, None)


def test_dem_error_message():
    m = _load_module()
    err = m.DemError("test error")
    assert "test error" in str(err)
