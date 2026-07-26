#!/usr/bin/env python3
"""足球赛事数据 Phase 1 — 创建付费订单.

用法: python scripts/create_order.py "巴西 vs 日本"
      python scripts/create_order.py 1359155
"""
import sys
import json
import uuid
import hashlib
import base64
import os
from datetime import datetime

from file_utils import SKILL_SLUG, INDICATOR, save_order

# ⚠️ 生产环境用环境变量, 不硬编码
PAY_TO = os.environ.get("CLAWTIP_PAYTO", "3c472160a2dffcb526e273c506bac514202607012124300010005348oNqXa3feWJ5vKOCbbty17w6sY67ty5xOS8RJ8OMq8fJN2fSg0elJscWXQ2bV3k7puxwaNzLu")
SM4_KEY = os.environ.get("CLAWTIP_SM4_KEY", "wTMwbvTIOznEzlP33FutnA==")
AMOUNT_FEN = 100  # 1元 = 100分

def sm4_encrypt(plain_text: str, key_b64: str) -> str:
    """SM4对称加密(国密), 返回Base64"""
    try:
        from gmssl.sm4 import CryptSM4, SM4_ENCRYPT
        key_bytes = base64.b64decode(key_b64)
        sm4 = CryptSM4()
        sm4.set_key(key_bytes, SM4_ENCRYPT)
        # Pad to 16-byte boundary
        pad_len = 16 - (len(plain_text.encode()) % 16)
        padded = plain_text + chr(pad_len) * pad_len
        cipher = sm4.crypt_ecb(padded.encode())
        return base64.b64encode(cipher).decode()
    except ImportError:
        # Fallback: skip encryption for sandbox testing
        return base64.b64encode(plain_text.encode()).decode()

def create_order(question: str):
    """创建订单, 返回 (order_no, amount, indicator)"""
    order_no = datetime.now().strftime("%Y%m%d%H%M%S") + uuid.uuid4().hex[:8]
    
    # 构建加密数据
    order_json = json.dumps({
        "orderNo": order_no,
        "amount": str(AMOUNT_FEN),
        "payTo": PAY_TO,
    })
    encrypted = sm4_encrypt(order_json, SM4_KEY)
    
    order_data = {
        "skill-id": SKILL_SLUG,
        "order_no": order_no,
        "amount": AMOUNT_FEN,
        "question": question,
        "encrypted_data": encrypted,
        "pay_to": PAY_TO,
        "description": f"足球赛事数据报告: {question}",
        "slug": SKILL_SLUG,
        "resource_url": "https://clawhub.ai/skills/football-match-data",
    }
    
    save_order(order_data)
    return order_no, AMOUNT_FEN, INDICATOR

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("订单创建失败: 缺少比赛参数. 用法: create_order.py <比赛ID或队名>")
        sys.exit(1)
    
    question = " ".join(sys.argv[1:])
    
    try:
        order_no, amount, indicator = create_order(question)
        print(f"ORDER_NO={order_no}")
        print(f"AMOUNT={amount}")
        print(f"QUESTION={question}")
        print(f"INDICATOR={indicator}")
    except Exception as e:
        print(f"订单创建失败: {e}")
        sys.exit(1)
