"""E2E tests for atmospheric-correction — 5 real-world scenarios."""
import subprocess
import sys
import os
import json

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(SKILL_DIR, "geoskill-atmospheric-correction.py")


def run(args, expect_rc=0, timeout=120):
    r = subprocess.run(
        [sys.executable, SCRIPT] + args,
        capture_output=True, text=True, timeout=timeout,
    )
    assert r.returncode == expect_rc, (
        f"rc={r.returncode} (expected {expect_rc})\n"
        f"stdout={r.stdout[:500]}\nstderr={r.stderr[:500]}"
    )
    return r


def test_01_basic_synthetic():
    """基本功能：仅给 bbox（无 --input）→ 自动合成，产出反射率 GeoTIFF + manifest"""
    out = os.path.join(SKILL_DIR, "_test_out_01")
    r = run(["--bbox", "116.0", "39.0", "117.0", "40.0", "--output-dir", out])
    assert os.path.isdir(out)
    assert os.path.exists(os.path.join(out, "surface_reflectance.tif"))
    assert os.path.exists(os.path.join(out, "output-manifest.json"))
    # manifest should be valid JSON with exit_code 0
    with open(os.path.join(out, "output-manifest.json"), encoding="utf-8") as f:
        man = json.load(f)
    assert man["exit_code"] == 0
    assert man["skill"] == "geoskill-atmospheric-correction"


def test_02_different_region_shanghai():
    """不同区域：上海，Sentinel-2 sensor"""
    out = os.path.join(SKILL_DIR, "_test_out_02")
    r = run([
        "--bbox", "121.0", "31.0", "122.0", "32.0",
        "--synthetic", "--sensor", "sentinel2", "--output-dir", out, "--quiet",
    ])
    assert os.path.exists(os.path.join(out, "surface_reflectance.tif"))
    with open(os.path.join(out, "correction_params.json"), encoding="utf-8") as f:
        params = json.load(f)
    assert params["sensor"] == "sentinel2"


def test_03_edge_tiny_bbox():
    """边界情况：极小区域（约 1km × 1km）"""
    out = os.path.join(SKILL_DIR, "_test_out_03")
    r = run([
        "--bbox", "116.39", "39.90", "116.40", "39.91",
        "--synthetic", "--output-dir", out, "--quiet",
    ])
    assert os.path.exists(os.path.join(out, "surface_reflectance.tif"))


def test_04_error_no_args():
    """错误处理：缺少必要参数 → exit 2"""
    r = run([], expect_rc=2)


def test_05_6s_method():
    """6s-simplified 方法：追加瑞利散射改正"""
    out = os.path.join(SKILL_DIR, "_test_out_05")
    r = run([
        "--bbox", "116.0", "39.0", "117.0", "40.0",
        "--synthetic", "--sensor", "landsat8",
        "--method", "6s-simplified", "--output-dir", out, "--quiet",
    ])
    assert os.path.exists(os.path.join(out, "surface_reflectance.tif"))
    with open(os.path.join(out, "correction_params.json"), encoding="utf-8") as f:
        params = json.load(f)
    assert params["method"] == "6s-simplified"
    # 6s should have tau_rayleigh in band params
    assert "tau_rayleigh" in params["bands"][0]
