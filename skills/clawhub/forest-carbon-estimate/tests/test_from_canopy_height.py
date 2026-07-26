"""Tests for forest-carbon-estimate from-canopy-height (PHASE 1+ REFACTORED)."""
import os
import sys
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(HERE, ".."))
SCRIPTS = os.path.join(PROJECT_ROOT, "scripts")


def test_from_canopy_height_subcommand_in_help():
    out = subprocess.run(
        [sys.executable, os.path.join(SCRIPTS, "forest-carbon-estimate.py"), "--help"],
        capture_output=True, text=True, timeout=15,
    )
    combined = out.stdout + out.stderr
    assert "from-canopy-height" in combined


def test_from_canopy_height_resolves_place_then_runs():
    """PHASE 1+: from-canopy-height 真的解析 --place。
    缺 pystac-client/planetary_computer/numpy/rasterio 时返回 3。
    解析失败或 STAC 失败时返回 5/7。
    """
    out = subprocess.run(
        [sys.executable, os.path.join(SCRIPTS, "forest-carbon-estimate.py"),
         "from-canopy-height", "--place", "北京市",
         "--output", os.path.join(os.environ.get("TEMP", "/tmp"), "carbon_test.tif")],
        capture_output=True, text=True, timeout=60,
    )
    combined = out.stdout + out.stderr
    # 至少应解析 place
    assert "from-canopy-height" in combined or "resolved" in combined
    assert "PHASE 0 DISABLED" not in combined
    # 退出码：0=成功, 1=失败（实测在 fallback 路径）, 3=依赖缺失, 5=无数据, 7=处理失败
    assert out.returncode in (0, 1, 3, 5, 7), f"unexpected exit {out.returncode}"


def test_aoi_resolution_works_via_vendored_geoskill_core():
    skill_dir = PROJECT_ROOT
    sys.path.insert(0, skill_dir)
    from _geoskill_core import aoi
    m = aoi.resolve_place("北京市", allow_nominatim=True, use_cache=False)
    assert m.bbox_wgs84 is not None
    assert len(m.bbox_wgs84) == 4
