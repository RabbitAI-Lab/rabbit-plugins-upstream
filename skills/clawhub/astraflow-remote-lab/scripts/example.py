#!/usr/bin/env python3
"""Run environment check for AstraFlow Desktop Sandbox."""

import os
import sys

def main():
    print("=== AstraFlow Desktop Sandbox Environment Check ===")
    try:
        import ucloud_sandbox
        ver = getattr(ucloud_sandbox, "__version__", "installed")
        print(f"[OK] Python SDK 'ucloud-sandbox' is installed (v{ver}).")
    except ImportError:
        print("[FAIL] Missing Python SDK 'ucloud-sandbox'. Run: pip install ucloud-sandbox")

    key = os.environ.get("UCLOUD_SANDBOX_API_KEY")
    reg = os.environ.get("UCLOUD_SANDBOX_REGION", "us-ca (default)")
    if not key:
        print("[WARN] UCLOUD_SANDBOX_API_KEY is not set.")
        print("       Obtain key from AstraFlow Console and set via:")
        print("       export UCLOUD_SANDBOX_API_KEY=\"<your_key>\"")
    else:
        # Do not print key length or contents to avoid leaking credential metadata
        print(f"[OK] UCLOUD_SANDBOX_API_KEY is configured (Target region: {reg}).")

if __name__ == "__main__":
    main()
