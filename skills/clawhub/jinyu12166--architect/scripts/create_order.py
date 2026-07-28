#!/usr/bin/env python3
"""ssq-analyzer - Order Creation Script (Phase 1)"""
import argparse
import hashlib
import json
import sys
import urllib.error
import urllib.request

from file_utils import save_order

DEFAULT_SERVER_URL = "https://api.ideaidea.com.cn"
CREATE_ORDER_PATH = "/api/skill/createOrder"

SLUG = "ssq-analyzer"

SERVER_URL = DEFAULT_SERVER_URL
CREATE_ORDER_URL = f"{SERVER_URL}{CREATE_ORDER_PATH}"


def compute_indicator(slug: str) -> str:
    return hashlib.md5(slug.encode("utf-8")).hexdigest()


def create_order(question: str) -> tuple:
    payload = json.dumps({
        "slug": SLUG,
        "question": question,
    }).encode("utf-8")
    req = urllib.request.Request(
        CREATE_ORDER_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as e:
        raise RuntimeError(f"\u7f51\u7edc\u8bf7\u6c42\u5f02\u5e38\uff0c\u8bf7\u786e\u8ba4\u7f51\u7edc\u94fe\u63a5\u5e76\u7a0d\u540e\u91cd\u8bd5: {e}") from e
    if body.get("responseCode") != "200":
        raise RuntimeError(body.get("responseMessage", "unknown error"))
    order_no = body.get("orderNo")
    if not order_no:
        raise RuntimeError("Order creation response missing orderNo")
    return (
        order_no,
        body.get("amount"),
        body.get("encryptedData"),
        body.get("payTo"),
        body.get("description", SLUG),
        body.get("skillId", ""),
        body.get("resourceUrl", SERVER_URL),
    )


def save_order_info(order_no, amount, question, encrypted_data, pay_to, indicator, description, skill_id, resource_url) -> str:
    order_data = {
        "skill-id": skill_id,
        "order_no": order_no,
        "amount": amount,
        "question": question,
        "encrypted_data": encrypted_data,
        "pay_to": pay_to,
        "description": description,
        "slug": SLUG,
        "resource_url": resource_url,
    }
    return save_order(indicator, order_no, order_data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create ssq-analyzer order")
    parser.add_argument("question", help="User question / consultation content")
    args = parser.parse_args()

    indicator = compute_indicator(SLUG)
    print("=" * 60)
    print("NOTICE: This step sends your question text to")
    print("        https://api.ideaidea.com.cn for order creation.")
    print("        Your question text is transmitted via HTTPS.")
    print("        No SSQ analysis data or purchase history")
    print("        is transmitted.")
    print("=" * 60)

    try:
        order_no, amount, encrypted_data, pay_to, description, skill_id, resource_url = create_order(args.question)
    except RuntimeError as e:
        print(f"\u8ba2\u5355\u521b\u5efa\u5931\u8d25: {e}")
        sys.exit(1)

    save_order_info(order_no, amount, args.question,
                    encrypted_data, pay_to, indicator, description, skill_id, resource_url)

    print(f"ORDER_NO={order_no}")
    print(f"AMOUNT={amount}")
    print(f"QUESTION={args.question}")
    print(f"INDICATOR={indicator}")
