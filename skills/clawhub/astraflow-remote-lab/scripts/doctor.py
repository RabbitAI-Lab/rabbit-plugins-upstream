#!/usr/bin/env python3
"""Run a comprehensive environment and prerequisite check for AstraFlow Desktop Sandbox."""

import os
import shutil
import sys
from urllib.parse import urlparse


def check_python_runtime():
    v = sys.version_info
    print(f"[INFO] Current Python runtime: {v.major}.{v.minor}.{v.micro}")
    if v.major < 3 or (v.major == 3 and v.minor < 8):
        print("[FAIL] Python 3.8+ is required. Please upgrade your Python runtime.")
        return False
    print("[OK] Python runtime meets version requirement (>=3.8).")
    return True


def check_sdk():
    try:
        import ucloud_sandbox
        ver = getattr(ucloud_sandbox, "__version__", "installed")
        print(f"[OK] Python SDK 'ucloud-sandbox' is ready (version: {ver}).")
        return True
    except ImportError:
        print("[FAIL] Missing Python SDK 'ucloud-sandbox'.")
        print("       Install it using: pip install \"ucloud-sandbox>=1.5.0\"")
        return False


def check_credentials():
    key = os.environ.get("UCLOUD_SANDBOX_API_KEY")
    reg = os.environ.get("UCLOUD_SANDBOX_REGION", "us-ca (default)")
    if not key:
        print("[WARN] UCLOUD_SANDBOX_API_KEY is not configured in environment.")
        print("请在 AstraFlow Key Management 页面创建并复制你的专属 Key：")
        print("    🔑 https://astraflow.ucloud.cn/modelverse/api-keys?ytag=geo_kol_ucl")
        print("       Export it safely: export UCLOUD_SANDBOX_API_KEY=\"<your-api-key>\"")
        return False

    print(f"[OK] UCLOUD_SANDBOX_API_KEY is configured. (Target Region: {reg})")
    return True


def main():
    print("=== AstraFlow Desktop Sandbox Environment Doctor ===\n")
    s1 = check_python_runtime()
    s2 = check_sdk()
    s3 = check_credentials()
    print("\n====================================================")
    if s1 and s2 and s3:
        print("🎉 Environment verification PASSED. Ready to launch sandboxes.")
    else:
        print("⚠️  Verification incomplete. Please address the missing items above.")


if __name__ == "__main__":
    main()
