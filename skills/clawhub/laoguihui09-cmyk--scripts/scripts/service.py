import sys
import json
import hashlib
import urllib.request
import urllib.error

from file_utils import load_order

GET_RESULT_URL = "https://web.kihb.shop/api/demo/getServiceResult"
SLUG = "clawtip-text-gen"


def compute_indicator(slug: str) -> str:
    return hashlib.md5(slug.encode("utf-8")).hexdigest()


def counseling(question: str, order_no: str, credential: str) -> str:
    if credential is None:
        return "请输入您的履约凭证"

    payload = json.dumps({
        "question": question,
        "orderNo": order_no,
        "credential": credential
    }).encode("utf-8")

    req = urllib.request.Request(
        GET_RESULT_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8")).get("resultData")
    except urllib.error.URLError as e:
        raise RuntimeError(f"履约请求失败: {e}") from e

    if body.get("responseCode") != "200":
        raise RuntimeError(
            f"履约失败: {body.get('responseMessage', 'unknown error')}"
        )

    pay_status = body.get("payStatus")
    print(f"PAY_STATUS: {pay_status}")

    answer = body.get("answer")
    if not answer and "ERROR" == pay_status:
        raise RuntimeError(f'获取信息失败：原因：{body.get("errorInfo", "未知错误")}')
    return answer


if __name__ == '__main__':
    parser = __import__('argparse').ArgumentParser(description="Get service result")
    parser.add_argument("order_no", help="Order number")
    args = parser.parse_args()

    indicator = compute_indicator(SLUG)

    try:
        order_data = load_order(indicator, args.order_no)
        question = order_data.get("question")
        if not question:
            raise RuntimeError("订单文件中缺少 question 字段")
        credential = order_data.get("payCredential")
        if not credential:
            raise RuntimeError("订单文件中缺少 payCredential 字段")
        result = counseling(question, args.order_no, credential)
        print(result)
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)
