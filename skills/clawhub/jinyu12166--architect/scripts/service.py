#!/usr/bin/env python3
"""ssq-analyzer - Service execution script (Phase 3)

Free tier: runs data fetch and statistical analysis without payment.
Paid tier: reads payCredential from order file; if valid, adds
5 recommended number sets to the analysis report.
"""
import argparse
import hashlib
import json
import os
import subprocess
import sys
import time

from file_utils import load_order

SLUG = "ssq-analyzer"
SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FETCH_SCRIPT = os.path.join(SKILL_DIR, "scripts", "fetch_ssq.py")
ANALYZE_SCRIPT = os.path.join(SKILL_DIR, "scripts", "analyze_ssq.py")
RECOMMEND_SCRIPT = os.path.join(SKILL_DIR, "scripts", "recommend_ssq.py")
REPORT_PATH = os.path.join(SKILL_DIR, "scripts", "\u6700\u65b0\u5206\u6790\u7ed3\u679c.md")
CREDENTIAL_TTL = 86400  # 24 hours


def compute_indicator(slug: str) -> str:
    return hashlib.md5(slug.encode("utf-8")).hexdigest()


def is_credential_valid(order_data: dict) -> bool:
    credential = order_data.get("payCredential")
    if not credential:
        return False
    credential_ts = order_data.get("credentialTimestamp")
    if credential_ts and time.time() - credential_ts > CREDENTIAL_TTL:
        return False
    return True


def run_free_analysis() -> str:
    """Run data fetch + free analysis. Always available."""
    print("[STEP 1/3] Fetching latest SSQ data from cwl.gov.cn...")
    result = subprocess.run(
        [sys.executable, FETCH_SCRIPT],
        capture_output=True, text=True, timeout=120
    )
    print(result.stdout.strip())
    if result.returncode != 0:
        if result.stderr:
            print(result.stderr)
        raise RuntimeError("Data fetch failed")

    print("\n[STEP 2/3] Generating free analysis report...")
    result = subprocess.run(
        [sys.executable, ANALYZE_SCRIPT],
        capture_output=True, text=True, timeout=120
    )
    print(result.stdout.strip())
    if result.returncode != 0:
        if result.stderr:
            print(result.stderr)
        raise RuntimeError("Free analysis failed")

    if os.path.exists(REPORT_PATH):
        with open(REPORT_PATH, "r", encoding="utf-8") as f:
            return f.read()
    return result.stdout


def run_paid_recommendation() -> str:
    """Run recommendation generation (only after payment verification)."""
    print("\n[STEP 3/3] Generating paid recommendation numbers...")
    result = subprocess.run(
        [sys.executable, RECOMMEND_SCRIPT],
        capture_output=True, text=True, timeout=120
    )
    print(result.stdout.strip())
    if result.returncode != 0:
        if result.stderr:
            print(result.stderr)
        raise RuntimeError("Recommendation generation failed")
    return result.stdout


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Execute SSQ analysis service")
    parser.add_argument("order_no", nargs="?", default="", help="Order number from Phase 1 (optional for free tier)")
    args = parser.parse_args()

    try:
        print("=" * 60)
        print("  SSQ Analyzer - Free Tier Analysis")
        print("=" * 60)
        report = run_free_analysis()
        print("\n" + "=" * 50)
        print("  Free Analysis Complete")
        print("=" * 50)
        print(report)

        # Check for paid recommendations
        if args.order_no:
            indicator = compute_indicator(SLUG)
            try:
                order_data = load_order(indicator, args.order_no)
                if is_credential_valid(order_data):
                    pay_status = order_data.get("payStatus", "SUCCESS")
                    if pay_status == "SUCCESS" or pay_status == "TEST_SUCCESS":
                        print("\n" + "=" * 60)
                        print("  Payment Verified - Adding Recommendation Numbers")
                        print("=" * 60)
                        recommendation = run_paid_recommendation()
                        print(recommendation)
                    else:
                        print(f"\nℹ️  Payment status is '{pay_status}'. Skipping paid recommendations.")
                else:
                    print("\nℹ️  No valid payment credential found. Skipping paid recommendations.")
                    print("   To get recommended numbers, complete payment via clawtip first.")
            except Exception as e:
                print(f"\nℹ️  No order file or payment credential found. Free report only.")
        else:
            print("\nℹ️  Free report generated. To unlock 5 recommended number sets,")
            print("   create an order and complete payment via clawtip.")

        print("\n" + "=" * 60)
        print("  PAY_STATUS: SUCCESS")
        print("=" * 60)

    except (RuntimeError, subprocess.TimeoutExpired) as e:
        print("PAY_STATUS: ERROR")
        print(f"ERROR_INFO: {e}")
        sys.exit(1)
