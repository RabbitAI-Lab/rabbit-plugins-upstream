import argparse
import hashlib
import json
import sys
import urllib.error
import urllib.request

from file_utils import load_order

DEFAULT_SERVER_URL = "https://api.ideaidea.com.cn"
GET_RESULT_PATH = "/api/skill/getServiceResult"

SKILL_NAME = "soft-ip-full-lifecycle-zijian"

SERVER_URL = DEFAULT_SERVER_URL
GET_RESULT_URL = f"{SERVER_URL}{GET_RESULT_PATH}"


def compute_indicator(skill_name: str) -> str:
    return hashlib.md5(skill_name.encode("utf-8")).hexdigest()


def request_service_authorization(order_no: str, credential: str) -> dict:
    payload = json.dumps({
        "slug": SKILL_NAME,
        "orderNo": order_no,
        "credential": credential,
    }).encode("utf-8")
    req = urllib.request.Request(
        GET_RESULT_URL,
        data=payload,
        headers={"Content-Type": "application/json", "User-Agent": "SoftIP-Skill/3.1"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as e:
        raise RuntimeError(f"Authorization request failed: {e}") from e


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify encrypted payment credential with clawtip authorization service for soft-ip-full-lifecycle-zijian"
    )
    parser.add_argument("order_no", help="Order number")
    args = parser.parse_args()
    print(60*"=")
    print("NOTICE: This step sends the encrypted payment credential")
    print("        to https://api.ideaidea.com.cn for verification.")
    print("        No source code or legal documents are transmitted.")
    print(60*"=")

    try:
        order_data = load_order(compute_indicator(SKILL_NAME), args.order_no)
        credential = order_data.get("payCredential")
        if not credential:
            raise RuntimeError("Missing payCredential in local order file")
        result = request_service_authorization(args.order_no, credential)
    except Exception as e:
        print("PAY_STATUS: ERROR")
        print(f"ERROR_INFO: {e}")
        return 1

    if result is None:
        print("PAY_STATUS: ERROR")
        print("ERROR_INFO: No response from server")
        return 1

    response_code = result.get("responseCode")
    pay_status = result.get("payStatus")
    already_fulfilled = result.get("alreadyFulfilled", False)

    print(f"PAY_STATUS: {pay_status}")
    print(f"ALREADY_FULFILLED: {already_fulfilled}")

    if response_code != "200" or pay_status != "SUCCESS":
        error_info = result.get("errorInfo", "Unknown error")
        print("PAY_STATUS: ERROR")
        print(f"ERROR_INFO: {error_info}")
        return 1

    print("AUTHORIZATION_RESULT=verified")
    _jr = json.dumps({
        "pay_status": pay_status,
        "authorization": "verified",
        "order_no": args.order_no,
        "already_fulfilled": already_fulfilled,
    })
    print(f"JSON_RESULT={_jr}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
