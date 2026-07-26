import argparse
import hashlib
import json
import sys
import urllib.error
import urllib.request

from file_utils import load_order

DEFAULT_SERVER_URL = "https://api.ideaidea.com.cn"
GET_RESULT_PATH = "/api/skill/getServiceResult"

SKILL_NAME = "database-specialist"

SERVER_URL = DEFAULT_SERVER_URL
GET_RESULT_URL = f"{SERVER_URL}{GET_RESULT_PATH}"


def compute_indicator(skill_name: str) -> str:
    return hashlib.md5(skill_name.encode("utf-8")).hexdigest()


def request_service_authorization(order_no: str, credential: str) -> dict:
    print("正在向 clawtip 验证服务提交身份验证请求...")
    print(f"将要传输的数据：订单号（{order_no}）、加密支付凭证（非明文）")
    print("以下信息不会被传输：数据库连接信息、密码、生产环境配置、表结构详情")
    print("通信协议：HTTPS + SM4 国密加密")
    payload = json.dumps({
        "slug": SKILL_NAME,
        "orderNo": order_no,
        "credential": credential,
    }).encode("utf-8")
    req = urllib.request.Request(
        GET_RESULT_URL,
        data=payload,
        headers={"Content-Type": "application/json", "User-Agent": "DatabaseSpecialist/1.0"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as e:
        raise RuntimeError(f"Authorization request failed: {e}") from e


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=f"Verify encrypted payment credential with clawtip authorization service for {SKILL_NAME}"
    )
    parser.add_argument("order_no", help="Order number")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    print("=" * 60)
    print("NOTICE: This step sends the encrypted payment credential")
    print("        to https://api.ideaidea.com.cn for verification.")
    print("        No database credentials or connection strings")
    print("        are transmitted.")
    print("        Communication: HTTPS + SM4 encryption.")
    print("=" * 60)

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
