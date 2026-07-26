"""
api_client.py - 统一 HTTP 客户端（带 retry + 限流保护）

数据源：
- 东方财富 push2his.eastmoney.com（K 线、财务）
- 腾讯 qt.gtimg.cn（实时行情）
- 新浪 hq.sinajs.cn（备用）
"""

import requests
import time
import random
from typing import Optional

# 公共请求头（避免触发明文限流）
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
    "Referer": "https://quote.eastmoney.com/",
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}

DEFAULT_TIMEOUT = 15
MAX_RETRY = 4  # 最多重试 4 次
RETRY_BACKOFF_BASE = 0.8  # 指数退避基数（秒）


def _backoff(attempt: int) -> float:
    """指数退避 + 抖动"""
    return RETRY_BACKOFF_BASE * (2 ** attempt) + random.uniform(0, 0.3)


def eastmoney_get(url: str, timeout: int = DEFAULT_TIMEOUT) -> Optional[dict]:
    """
    通用东方财富接口 GET。

    返回解析后的 JSON 字典；若失败返回 None。
    自动重试 4 次（指数退避），最终仍 rc!=0 / 解析失败时返回 None。
    """
    last_err: Optional[Exception] = None
    for attempt in range(MAX_RETRY):
        try:
            r = requests.get(url, headers=HEADERS, timeout=timeout)
            r.raise_for_status()
            j = r.json()
            rc = j.get("rc", 0)
            if rc == 0 and j.get("data"):
                return j
            # rc != 0：限流/无数据；按退避重试
            last_err = RuntimeError(f"eastmoney rc={rc} attempt={attempt}")
        except Exception as e:
            last_err = e
        time.sleep(_backoff(attempt))
    print(f"[api_client] eastmoney_get 最终失败: {last_err}")
    return None


def tencent_get(code: str) -> Optional[dict]:
    """
    腾讯行情接口。返回 v_sh<CODE>="..." 解析后的字段字典。
    备用数据源，主要用于实时价格。
    """
    market = "sh" if code.startswith("6") or code.startswith("5") else "sz"
    url = f"https://qt.gtimg.cn/q={market}{code}"
    last_err: Optional[Exception] = None
    for attempt in range(MAX_RETRY):
        try:
            r = requests.get(url, headers=HEADERS, timeout=DEFAULT_TIMEOUT)
            r.raise_for_status()
            text = r.text.strip()
            if '="' not in text:
                last_err = RuntimeError(f"tencent empty: {text[:80]}")
                time.sleep(_backoff(attempt))
                continue
            # 解析 v_sh601899="1~紫金矿业~..."
            payload = text.split('="', 1)[1].rstrip('";')
            fields = payload.split('~')
            if len(fields) < 40:
                last_err = RuntimeError(f"tencent short fields: {len(fields)}")
                time.sleep(_backoff(attempt))
                continue
            return {
                "name": fields[1],
                "code": fields[2],
                "price": float(fields[3]) if fields[3] else None,
                "yesterday": float(fields[4]) if fields[4] else None,
                "open": float(fields[5]) if fields[5] else None,
                "volume": fields[6],  # 成交手数
                "outer_buy": fields[7],
                "inner_buy": fields[8],
                "bid1": fields[9],
                "ask1": fields[19],
                "high": float(fields[33]) if len(fields) > 33 and fields[33] else None,
                "low": float(fields[34]) if len(fields) > 34 and fields[34] else None,
                "change_pct": float(fields[32]) if len(fields) > 32 and fields[32] else None,
                "turnover_pct": float(fields[38]) if len(fields) > 38 and fields[38] else None,
                "pe": float(fields[39]) if len(fields) > 39 and fields[39] else None,
                "amount_yi": fields[37],  # 成交额（亿）
                "timestamp": fields[30],
            }
        except Exception as e:
            last_err = e
            time.sleep(_backoff(attempt))
    print(f"[api_client] tencent_get 最终失败: {last_err}")
    return None


def market_prefix(code: str) -> str:
    """A 股代码前缀：6 开头 = 上交所 (1)，其他 = 深交所 (0)"""
    return "1" if code.startswith("6") or code.startswith("5") else "0"
