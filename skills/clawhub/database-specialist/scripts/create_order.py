#!/usr/bin/env python3
"""database-specialist - Create service order via clawtip (Phase 1: sends slug + question text to api.ideaidea.com.cn)"""
import argparse
import hashlib
import json
import sys
import urllib.error
import urllib.request

from file_utils import save_order

DEFAULT_SERVER_URL = "https://api.ideaidea.com.cn"
CREATE_ORDER_PATH = "/api/skill/createOrder"

SLUG = "database-specialist"

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
        headers={"Content-Type": "application/json", "User-Agent": "DatabaseSpecialist/1.0"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as e:
        raise RuntimeError(f"网络请求异常，请确认网络链接并稍后重试: {e}") from e
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
    import re
    sanitized_question = re.sub(
        r'(password|passwd|pwd|secret|token|key|apikey|api_key)\s*[:=]\s*\S+',
        r'\1=[REDACTED]',
        question,
        flags=re.IGNORECASE
    )
    order_data = {
        "skill-id": skill_id,
        "order_no": order_no,
        "amount": amount,
        "question": sanitized_question,
        "encrypted_data": encrypted_data,
        "pay_to": pay_to,
        "description": description,
        "slug": SLUG,
        "resource_url": resource_url,
    }
    return save_order(indicator, order_no, order_data)


if __name__ == "__main__":
    print("正在通过 clawtip 第三方服务创建订单...")
    print(f"将要传输的信息：您的问题描述（用于生成服务内容）")
    print("以下信息不会被传输：数据库连接信息、密码、生产环境配置")
    print("通信协议：HTTPS + SM4 国密加密")
    print("NOTICE: This step sends your question text to")
    print("        https://api.ideaidea.com.cn for order creation.")
    print("        No database credentials or connection strings")
    print("        are transmitted.")
    parser = argparse.ArgumentParser(description="Create order")
    parser.add_argument("question", help="User question / consultation content")
    args = parser.parse_args()

    indicator = compute_indicator(SLUG)

    try:
        order_no, amount, encrypted_data, pay_to, description, skill_id, resource_url = create_order(args.question)
    except RuntimeError as e:
        print(f"订单创建失败: {e}")
        sys.exit(1)

    save_order_info(order_no, amount, args.question,
                    encrypted_data, pay_to, indicator, description, skill_id, resource_url)

    print(f"ORDER_NO={order_no}")
    print(f"AMOUNT={amount}")
    print(f"QUESTION={args.question}")
    print(f"INDICATOR={indicator}")
    _jr = json.dumps({
        "order_no": order_no,
        "amount": amount,
        "question": args.question,
        "indicator": indicator,
        "slug": SLUG,
    }, ensure_ascii=False)
    print(f"JSON_RESULT={_jr}")
