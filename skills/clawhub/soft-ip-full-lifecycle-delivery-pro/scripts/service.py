#!/usr/bin/env python3
"""
soft-ip-full-lifecycle-delivery-pro - Service execution script.
Reads payCredential from order file, verifies payment, and runs SoftIP Delivery Pro analysis.
"""
import argparse
import hashlib
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
from file_utils import load_order
DEFAULT_SERVER_URL = "https://api.ideaidea.com.cn"
GET_RESULT_PATH = "/api/skill/getServiceResult"
SLUG = "soft-ip-full-lifecycle-delivery-pro"
SERVER_URL = DEFAULT_SERVER_URL
GET_RESULT_URL = f"{SERVER_URL}{GET_RESULT_PATH}"
SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FETCH_SCRIPT = os.path.join(SKILL_DIR, "scripts", "fetch_ssq.py")
ANALYZE_SCRIPT = os.path.join(SKILL_DIR, "scripts", "analyze_ssq.py")

def compute_indicator(slug: str) -> str:
    return hashlib.md5(slug.encode("utf-8")).hexdigest()

def verify_payment(order_no: str, credential: str) -> dict | None:
    """Send credential to service backend for verification."""
    payload = json.dumps({
        "slug": SLUG,
        "orderNo": order_no,
        "credential": credential,
    }).encode("utf-8")
    req = urllib.request.Request(
        GET_RESULT_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as e:
        raise RuntimeError(f"Authorization request failed: {e}") from e


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Execute SoftIP Delivery Pro analysis service")
    parser.add_argument("order_no", help="Order number")
    args = parser.parse_args()
    indicator = compute_indicator(SLUG)
    try:
        order_data = load_order(indicator, args.order_no)
        question = order_data.get("question")
        if not question:
            raise RuntimeError("Missing question field in order file")
        credential = order_data.get("payCredential")
        if not credential:
            raise RuntimeError("Missing payCredential in order file")
        result = verify_payment(args.order_no, credential)
    except Exception as e:
        print(f"PAY_STATUS: ERROR")
        print(f"ERROR_INFO: {e}")
        sys.exit(1)
    if result is None:
        print("PAY_STATUS: ERROR")
        print("ERROR_INFO: No response from server")
        sys.exit(1)
    response_code = result.get("responseCode")
    pay_status = result.get("payStatus")
    already_fulfilled = result.get("alreadyFulfilled", False)
    print(f"PAY_STATUS: {pay_status}")
    if response_code != "200" or pay_status != "SUCCESS":
        error_info = result.get("errorInfo", "Unknown error")
        print(f"ERROR_INFO: {error_info}")
        sys.exit(1)
    if already_fulfilled:
        print("Service already fulfilled for this order.")
        sys.exit(0)
    try:
        report = "PAYMENT_VERIFIED=ready`nNEXT_STEP=AI will now draft all 8 copyright registration documents."
        print(report)
    except (RuntimeError, Exception) as e:
        print("PAY_STATUS: ERROR")
        print(f"ERROR_INFO: Analysis execution failed: {e}")
        sys.exit(1)
