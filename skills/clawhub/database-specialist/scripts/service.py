#!/usr/bin/env python3
"""
database-specialist - Service execution script.
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
SLUG = "database-specialist"
SERVER_URL = DEFAULT_SERVER_URL
GET_RESULT_URL = "{0}{1}".format(SERVER_URL, GET_RESULT_PATH)

def compute_indicator(slug):
    return hashlib.md5(slug.encode("utf-8")).hexdigest()

def verify_payment(order_no, credential):
    payload = json.dumps({"slug": SLUG, "orderNo": order_no, "credential": credential}).encode("utf-8")
    req = urllib.request.Request(GET_RESULT_URL, data=payload, headers={"Content-Type": "application/json", "User-Agent": "DatabaseSpecialist/1.0"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as e:
        raise RuntimeError("Authorization request failed: {0}".format(e))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Verify encrypted payment credential with api.ideaidea.com.cn for database-specialist")
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
        print("ERROR_INFO: {0}".format(e))
        sys.exit(1)

    if result is None:
        print("PAY_STATUS: ERROR")
        print("ERROR_INFO: No response from server")
        sys.exit(1)

    response_code = result.get("responseCode")
    pay_status = result.get("payStatus")
    already_fulfilled = result.get("alreadyFulfilled", False)

    print("PAY_STATUS: {0}".format(pay_status))
    print("ALREADY_FULFILLED: {0}".format(already_fulfilled))

    if response_code != "200" or pay_status != "SUCCESS":
        error_info = result.get("errorInfo", "Unknown error")
        print("PAY_STATUS: ERROR")
        print("ERROR_INFO: {0}".format(error_info))
        sys.exit(1)

    print("AUTHORIZATION_RESULT=verified")
    _jr = json.dumps({"pay_status": pay_status, "authorization": "verified", "order_no": args.order_no, "already_fulfilled": already_fulfilled})
    print("JSON_RESULT={0}".format(_jr))
