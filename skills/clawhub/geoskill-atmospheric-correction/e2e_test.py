"""Standalone E2E test runner for atmospheric-correction — 5 real-world scenarios.

Run with: python e2e_test.py
"""
import subprocess
import sys
import os
import json
import shutil

SKILL_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(SKILL_DIR, "geoskill-atmospheric-correction.py")

PASS = 0
FAIL = 0


def run(args, expect_rc=0, label=""):
    global PASS, FAIL
    r = subprocess.run(
        [sys.executable, SCRIPT] + args,
        capture_output=True, text=True, timeout=120,
    )
    ok = r.returncode == expect_rc
    status = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{status}] {label}  rc={r.returncode}")
    if not ok:
        print(f"         stdout: {r.stdout[:300]}")
        print(f"         stderr: {r.stderr[:300]}")
    return r


def cleanup(*dirs):
    for d in dirs:
        p = os.path.join(SKILL_DIR, d)
        if os.path.isdir(p):
            shutil.rmtree(p, ignore_errors=True)


def main():
    global PASS, FAIL
    out1 = os.path.join(SKILL_DIR, "_e2e_out_01")
    out2 = os.path.join(SKILL_DIR, "_e2e_out_02")
    out3 = os.path.join(SKILL_DIR, "_e2e_out_03")
    out5 = os.path.join(SKILL_DIR, "_e2e_out_05")
    cleanup("_e2e_out_01", "_e2e_out_02", "_e2e_out_03", "_e2e_out_05")

    print("=" * 60)
    print("atmospheric-correction — E2E test (5 scenarios)")
    print("=" * 60)

    # 1. 基本功能：北京区域，合成数据，DOS 校正
    r = run(["--bbox", "116.0", "39.0", "117.0", "40.0",
             "--synthetic", "--output-dir", out1],
            label="01 北京 DOS 合成数据")
    assert os.path.exists(os.path.join(out1, "surface_reflectance.tif"))
    assert os.path.exists(os.path.join(out1, "output-manifest.json"))

    # 2. 不同区域：上海，Sentinel-2
    run(["--bbox", "121.0", "31.0", "122.0", "32.0",
         "--synthetic", "--sensor", "sentinel2", "--output-dir", out2, "--quiet"],
        label="02 上海 Sentinel-2")

    # 3. 极小区域（~1km）
    run(["--bbox", "116.39", "39.90", "116.40", "39.91",
         "--synthetic", "--output-dir", out3, "--quiet"],
        label="03 极小区域")

    # 4. 错误处理：无参数 → exit 2
    run([], expect_rc=2, label="04 无参数 exit 2")

    # 5. 6s-simplified 方法
    run(["--bbox", "116.0", "39.0", "117.0", "40.0",
         "--synthetic", "--method", "6s-simplified", "--output-dir", out5, "--quiet"],
        label="05 6s-simplified 方法")

    print("=" * 60)
    print(f"Results: {PASS} passed, {FAIL} failed")
    print("=" * 60)

    cleanup("_e2e_out_01", "_e2e_out_02", "_e2e_out_03", "_e2e_out_05")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
