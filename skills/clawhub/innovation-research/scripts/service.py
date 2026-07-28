#!/usr/bin/env python3
"""
innovation-research - Service execution script.
Reads payCredential from order file and verifies payment with clawtip service.
"""
import argparse
import hashlib
import json
import sys
import urllib.error
import urllib.request

from file_utils import load_order

DEFAULT_SERVER_URL = "https://api.ideaidea.com.cn"
GET_RESULT_PATH = "/api/skill/getServiceResult"

SLUG = "innovation-research"

SERVER_URL = DEFAULT_SERVER_URL
GET_RESULT_URL = f"{SERVER_URL}{GET_RESULT_PATH}"


def compute_indicator(slug: str) -> str:
    return hashlib.md5(slug.encode("utf-8")).hexdigest()


def verify_payment(order_no: str, credential: str) -> dict | None:
    payload = json.dumps({
        "slug": SLUG,
        "orderNo": order_no,
        "credential": credential,
    }).encode("utf-8")
    req = urllib.request.Request(
        GET_RESULT_URL,
        data=payload,
        headers={"Content-Type": "application/json", "User-Agent": "InnovationResearch/1.0"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as e:
        raise RuntimeError(f"Authorization request failed: {e}") from e


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Verify encrypted payment credential with api.ideaidea.com.cn (clawtip verification) for innovation-research")
    parser.add_argument("order_no", help="Order number")
    args = parser.parse_args()

    indicator = compute_indicator(SLUG)

    try:
        order_data = load_order(indicator, args.order_no)
        credential = order_data.get("payCredential")
        if not credential:
            raise RuntimeError("Missing payCredential in local order file")
        result = verify_payment(args.order_no, credential)
    except Exception as e:
        print("PAY_STATUS: ERROR")
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
    print(f"ALREADY_FULFILLED: {already_fulfilled}")

    if response_code != "200" or pay_status != "SUCCESS":
        error_info = result.get("errorInfo", "Unknown error")
        print("PAY_STATUS: ERROR")
        print(f"ERROR_INFO: {error_info}")
        sys.exit(1)

    print("AUTHORIZATION_RESULT=verified")
    _jr = json.dumps({
        "pay_status": pay_status,
        "authorization": "verified",
        "order_no": args.order_no,
        "already_fulfilled": already_fulfilled,
    })
    print(f"JSON_RESULT={_jr}")
