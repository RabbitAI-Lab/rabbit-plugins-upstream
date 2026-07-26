import sys
import json
import hashlib
import urllib.request
import urllib.error

from file_utils import save_order

CREATE_ORDER_URL = "https://web.kihb.shop/api/demo/createOrder"
SLUG = "clawtip-text-gen"


def compute_indicator(slug: str) -> str:
    return hashlib.md5(slug.encode("utf-8")).hexdigest()


def create_order(question: str) -> tuple:
    pay_data_dict = {"reqData": {"question": question}}
    payload = json.dumps(pay_data_dict).encode("utf-8")
    req = urllib.request.Request(
        CREATE_ORDER_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8")).get("resultData")
    except urllib.error.URLError as e:
        raise RuntimeError(f"网络请求异常，请确认网络连接并稍后重试: {e}") from e

    if body is None:
        raise RuntimeError("网络请求异常，请确认网络连接并稍后重试")

    if body.get("responseCode") != '200':
        raise RuntimeError(
            f"创建订单失败: {body.get('responseMessage', 'unknown error')}"
        )

    order_no = body.get("orderNo")
    if not order_no:
        raise RuntimeError("创建订单响应缺少 orderNo")

    amount = body.get("amount")
    encrypted_data = body.get("encryptedData")
    pay_to = body.get("payTo")

    return order_no, amount, encrypted_data, pay_to


def save_order_info(order_no, amount, question, encrypted_data, pay_to, indicator):
    order_data = {
        "skill-id": "si-text-gen",
        "order_no": order_no,
        "amount": amount,
        "question": question,
        "encrypted_data": encrypted_data,
        "pay_to": pay_to,
        "description": "短文生成（clawtip 付费履约）",
        "slug": SLUG,
        "resource_url": "https://web.kihb.shop",
    }
    return save_order(indicator, order_no, order_data)


if __name__ == "__main__":
    parser = __import__('argparse').ArgumentParser(description="Create order")
    parser.add_argument("question", help="User request")
    args = parser.parse_args()

    indicator = compute_indicator(SLUG)

    try:
        order_no, amount, encrypted_data, pay_to = create_order(args.question)
    except RuntimeError as e:
        print(f"订单创建失败: {e}")
        sys.exit(1)

    save_order_info(order_no, amount, args.question, encrypted_data, pay_to, indicator)

    print(f"ORDER_NO={order_no}")
    print(f"AMOUNT={amount}")
    print(f"QUESTION={args.question}")
    print(f"INDICATOR={indicator}")
