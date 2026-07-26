#!/usr/bin/env python3
"""
obsidian-memory-system - Create service order via clawtip (Phase 1: sends slug + question text to api.ideaidea.com.cn)
"""
import argparse
import hashlib
import json
import sys
import urllib.error
import urllib.request

from file_utils import save_order

DEFAULT_SERVER_URL = "https://api.ideaidea.com.cn"
CREATE_ORDER_PATH = "/api/skill/createOrder"

# NOTICE: this script creates a local order file and sends your question text to api.ideaidea.com.cn for order creation.
SLUG = "obsidian-memory-system"
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
        headers={"Content-Type": "application/json", "User-Agent": "ObsidianMemorySystem/3.0"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as e:
        raise RuntimeError(f"网络请求异常，请确认网络链接并稍后重试: {e}") from e
    if body.get("responseCode") != "200":
        raise RuntimeError(body.get("responseMessage", "未知错误"))
    order_no = body.get("orderNo")
    if not order_no:
        raise RuntimeError("服务器返回缺少订单号")
    return (
        order_no,
        body.get("amount"),
        body.get("encryptedData"),
        body.get("payTo"),
        body.get("description", SLUG),
        body.get("skillId", ""),
        body.get("resourceUrl", SERVER_URL),
    )


def save_order_info(order_no, amount, encrypted_data, pay_to, indicator, description, skill_id, resource_url) -> str:
    order_data = {
        "skill-id": skill_id,
        "order_no": order_no,
        "amount": amount,
        "encrypted_data": encrypted_data,
        "pay_to": pay_to,
        "description": description,
        "slug": SLUG,
        "resource_url": resource_url,
        "metadata_only": True,
    }
    return save_order(indicator, order_no, order_data)


def main() -> int:
    parser = argparse.ArgumentParser(description="Create service order for obsidian-memory-system")
    parser.add_argument("question", help="User question / consultation content")
    args = parser.parse_args()

    print("NOTICE: This step will create a local order file and send your question text")
    print("        to https://api.ideaidea.com.cn for order creation.")
    print("        No Obsidian vault content or source code is transmitted.")
    indicator = compute_indicator(SLUG)
    try:
        order_no, amount, encrypted_data, pay_to, description, skill_id, resource_url = create_order(args.question)
    except RuntimeError as e:
        print(f"订单创建失败: {e}")
        return 1

    save_order_info(order_no, amount, encrypted_data, pay_to, indicator, description, skill_id, resource_url)

    print(f"ORDER_NO={order_no}")
    print(f"AMOUNT={amount}")
    print(f"QUESTION={args.question}")
    print(f"INDICATOR={indicator}")
    _jr = json.dumps({
        "order_no": order_no,
        "amount": amount,
        "indicator": indicator,
        "slug": "obsidian-memory-system",
    }, ensure_ascii=False)
    print(f"JSON_RESULT={_jr}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
