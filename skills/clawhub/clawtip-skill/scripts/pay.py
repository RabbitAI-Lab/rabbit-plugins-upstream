#!/usr/bin/env python3
"""
clawtip 支付处理脚本（Phase 2）
用法:
  python3 pay.py <order_no> <indicator>
  python3 pay.py <order_no> <indicator> --confirm <payment_reference>

第一段发起支付，只把订单切到待确认状态；第二段在用户完成真实支付后，
携带 payment_reference 再次调用确认接口，成功后才会写入支付凭证。
"""

import json
import os
import platform
import sys
import urllib.error
import urllib.request

SERVER_URL = "https://api.ideaidea.com.cn"
PAY_URL = f"{SERVER_URL}/api/skill/pay"
CONFIRM_PAYMENT_URL = f"{SERVER_URL}/api/skill/confirmPayment"


def get_orders_dir(indicator: str) -> str:
    system = platform.system()
    home = os.path.expanduser("~")
    if system == "Windows":
        base = os.path.join(home, "openclaw", "skills", "orders")
    else:
        base = os.path.join(home, ".openclaw", "skills", "orders")
    return os.path.join(base, indicator)


def get_order_file(indicator: str, order_no: str) -> str:
    return os.path.join(get_orders_dir(indicator), f"{order_no}.json")


def load_order(indicator: str, order_no: str):
    order_file = get_order_file(indicator, order_no)
    if not os.path.exists(order_file):
        return None, None, f"订单文件不存在: {order_file}"

    try:
        with open(order_file, "r", encoding="utf-8") as f:
            return json.load(f), order_file, None
    except (json.JSONDecodeError, IOError) as exc:
        return None, None, f"读取订单文件失败: {exc}"


def save_order(order_file: str, order_data: dict):
    try:
        with open(order_file, "w", encoding="utf-8") as f:
            json.dump(order_data, f, ensure_ascii=False, indent=2)
        return None
    except IOError as exc:
        return f"写入订单文件失败: {exc}"


def request_json(url: str, payload: dict):
    try:
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json", "User-Agent": "ClawtipSkill/1.0"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8")), None
    except urllib.error.HTTPError as exc:
        try:
            body = exc.read().decode("utf-8")
            return None, f"请求失败 (HTTP {exc.code}): {body}"
        except Exception:
            return None, f"请求失败 (HTTP {exc.code})"
    except urllib.error.URLError as exc:
        return None, f"请求失败: {exc.reason}"
    except Exception as exc:
        return None, f"请求异常: {exc}"


def initiate_payment(order_no: str, indicator: str) -> int:
    print("NOTICE: This step initiates payment and processes the order.")
    print("NOTICE: No vault content, project files, or user data are uploaded.")

    order_data, order_file, error = load_order(indicator, order_no)
    if error:
        print("PAY_RESULT: ERROR")
        print(f"ERROR_INFO: {error}")
        return 1

    slug = order_data.get("slug", "")
    if not slug:
        print("PAY_RESULT: ERROR")
        print("ERROR_INFO: 订单文件中缺少 slug 字段")
        return 1

    response_data, error = request_json(PAY_URL, {"slug": slug, "orderNo": order_no})
    if error:
        print("PAY_RESULT: ERROR")
        print(f"ERROR_INFO: {error}")
        return 1

    if response_data.get("responseCode") != "200":
        print("PAY_RESULT: ERROR")
        print(f"ERROR_INFO: {response_data.get('responseMessage', '支付发起失败')}")
        return 1

    pay_status = response_data.get("payStatus", "ERROR")

    # Server auto-completed the payment (wallet deduction, instant processing)
    if pay_status == "SUCCESS":
        pay_credential = response_data.get("payCredential")
        if pay_credential:
            order_data["payCredential"] = pay_credential
            save_error = save_order(order_file, order_data)
            if save_error:
                print("PAY_RESULT: ERROR")
                print(f"ERROR_INFO: {save_error}")
                return 1
        print("PAY_RESULT: SUCCESS")
        print(f"CREDENTIAL: {pay_credential}")
        print(f"ORDER_NO: {order_no}")
        print(f"AMOUNT: {response_data.get('amount', order_data.get('amount', ''))}")
        print("NEXT_STEP: Run the target skill's service.py to complete fulfillment.")
        return 0

    # Two-phase flow: user must pay externally, then confirm
    if pay_status == "PENDING":
        print("PAY_RESULT: PENDING")
        print(f"ORDER_NO: {order_no}")
        print(f"PAY_TO: {response_data.get('payTo', order_data.get('pay_to', ''))}")
        print(f"AMOUNT: {response_data.get('amount', order_data.get('amount', ''))}")
        print("NEXT_STEP: Complete the real payment, then run this script again with --confirm <payment_reference>.")
        return 0

    # Unexpected status
    print("PAY_RESULT: ERROR")
    print(f"ERROR_INFO: 服务端返回异常状态: {pay_status}")
    return 1


def confirm_payment(order_no: str, indicator: str, payment_reference: str) -> int:
    print("NOTICE: This step confirms that the external payment has completed.")
    print("NOTICE: amount and payTo from the local order file must match the confirmation request.")

    order_data, order_file, error = load_order(indicator, order_no)
    if error:
        print("PAY_RESULT: ERROR")
        print(f"ERROR_INFO: {error}")
        return 1

    slug = order_data.get("slug", "")
    if not slug:
        print("PAY_RESULT: ERROR")
        print("ERROR_INFO: 订单文件中缺少 slug 字段")
        return 1

    response_data, error = request_json(
        CONFIRM_PAYMENT_URL,
        {
            "slug": slug,
            "orderNo": order_no,
            "paymentReference": payment_reference,
            "amount": str(order_data.get("amount", "")),
            "payTo": order_data.get("pay_to") or order_data.get("payTo") or "",
        },
    )
    if error:
        print("PAY_RESULT: ERROR")
        print(f"ERROR_INFO: {error}")
        return 1

    resp_code = response_data.get("responseCode", "500")
    pay_status = response_data.get("payStatus", "ERROR")
    pay_credential = response_data.get("payCredential")
    if resp_code == "200" and pay_status == "SUCCESS" and pay_credential:
        order_data["payCredential"] = pay_credential
        order_data["paymentReference"] = payment_reference
        error = save_order(order_file, order_data)
        if error:
            print("PAY_RESULT: ERROR")
            print(f"ERROR_INFO: {error}")
            return 1
        print("PAY_RESULT: SUCCESS")
        print(f"CREDENTIAL: {pay_credential}")
        return 0

    print("PAY_RESULT: FAIL")
    print(f"ERROR_INFO: {response_data.get('responseMessage', '支付确认失败')}")
    return 1


def validate_inputs(order_no: str, indicator: str):
    if not indicator or len(indicator) != 32 or not all(c in "0123456789abcdefABCDEF" for c in indicator):
        return "indicator 格式无效，需要 32 位十六进制字符串"
    if not order_no or not (14 <= len(order_no) <= 32) or not order_no.isdigit():
        return "order_no 格式无效，需要 14-32 位数字"
    return None


if __name__ == "__main__":
    if len(sys.argv) not in (3, 5):
        print("PAY_RESULT: ERROR")
        print("ERROR_INFO: 用法: python3 pay.py <order_no> <indicator> 或 python3 pay.py <order_no> <indicator> --confirm <payment_reference>")
        sys.exit(1)

    order_no = sys.argv[1]
    indicator = sys.argv[2]
    error = validate_inputs(order_no, indicator)
    if error:
        print("PAY_RESULT: ERROR")
        print(f"ERROR_INFO: {error}")
        sys.exit(1)

    if len(sys.argv) == 3:
        sys.exit(initiate_payment(order_no, indicator))

    if sys.argv[3] != "--confirm" or not sys.argv[4].strip():
        print("PAY_RESULT: ERROR")
        print("ERROR_INFO: 确认支付时必须使用 --confirm <payment_reference>")
        sys.exit(1)

    sys.exit(confirm_payment(order_no, indicator, sys.argv[4].strip()))
