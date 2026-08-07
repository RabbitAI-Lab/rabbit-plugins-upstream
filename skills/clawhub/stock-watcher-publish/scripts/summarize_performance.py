#!/usr/bin/env python3
"""Summarize current performance for all watched stocks."""

import re
import sys
import time

import requests
from bs4 import BeautifulSoup

from config import WATCHLIST_FILE, ensure_watchlist


THS_SNAPSHOT_URL = "https://quota-h.10jqka.com.cn/fuyao/common_hq_aggr/quote/v1/multi_last_snapshot"
THS_HEADERS = {
    "accept": "*/*",
    "content-type": "application/json",
    "origin": "https://stockpage.10jqka.com.cn",
    "referer": "https://stockpage.10jqka.com.cn/",
    "platform": "hxkline",
    "source-id": "hxkline-NEWS_appNewsFlowHome_Page",
    "user-agent": "Mozilla/5.0",
    "x-auth-appname": "AINVEST",
    "x-auth-progid": "7047",
    "x-auth-type": "ths",
    "x-auth-version": "1.0",
    "x-fuyao-auth": (
        "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9."
        "eyJhdXRob3JpemVyX25hbWVzcGFjZSI6ImNvbW1vbi1ocS1hZ2dyIiwibGljZW5zZWVfdHlwZSI6IkZST05UX0FQUCIsImxpY2Vuc2VlX25hbWVzcGFjZSI6Imh4a2xpbmUtTkVXU19hcHBOZXdzRmxvd0hvbWVfUGFnZSJ9."
        "ldrvWTheNnGOa_rH_buA6OoUpLtW2bhcdr3fABrGHbk"
    ),
}
SNAPSHOT_FIELD_MAP = {
    "6": "base_price",
    "10": "latest_price",
    "19": "amount",
    "55": "name",
    "199112": "pct_change",
    "264648": "change",
}


def infer_market(stock_code: str) -> str | None:
    if stock_code.startswith("6"):
        return "17"
    if stock_code.startswith(("0", "3")):
        return "33"
    return None


def fetch_stock_snapshot_api(stock_code: str) -> dict | None:
    market = infer_market(stock_code)
    if not market:
        return None

    payload = {
        "code_list": [{"codes": [stock_code], "market": market}],
        "trade_class": "intraday",
        "data_fields": ["55", "10", "199112", "264648", "19", "6"],
        "lang": "zh_cn",
        "gpid": 0,
    }

    try:
        response = requests.post(THS_SNAPSHOT_URL, headers=THS_HEADERS, json=payload, timeout=10)
        response.raise_for_status()
        result = response.json()
        if result.get("status_code") != 0:
            return None

        quote_data = result.get("data", {}).get("quote_data") or []
        if not quote_data:
            return None

        item = quote_data[0]
        values = item.get("value") or []
        if not values:
            return None

        fields = [
            SNAPSHOT_FIELD_MAP.get(field, field)
            for field in item.get("data_fields", [])
        ]
        snapshot = dict(zip(fields, values[0]))
        snapshot.update({
            "code": stock_code,
            "market": market,
            "url": f"https://stockpage.10jqka.com.cn/{stock_code}/",
            "source": "api",
        })
        return snapshot
    except requests.RequestException as exc:
        print(f"API error fetching data for {stock_code}: {exc}", file=sys.stderr)
        return None


def fetch_stock_data_html(stock_code: str) -> dict | None:
    url = f"https://stockpage.10jqka.com.cn/{stock_code}/"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = "utf-8"
        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.find("title")
        stock_name = ""
        if title:
            title_text = title.get_text()
            if "(" in title_text and ")" in title_text:
                stock_name = title_text.split("(")[0].strip()

        text_content = soup.get_text()
        percentages = re.findall(r"[-+]?\d+\.?\d*%", text_content)
        performance = {}
        if percentages:
            performance["recent_changes"] = percentages[:3]

        return {
            "code": stock_code,
            "name": stock_name,
            "url": url,
            "performance": performance,
            "source": "html",
        }
    except requests.RequestException as exc:
        print(f"HTML error fetching data for {stock_code}: {exc}", file=sys.stderr)
        return None


def summarize_line(code: str, fallback_name: str) -> str:
    stock_data = fetch_stock_snapshot_api(code)
    if stock_data:
        latest_price = stock_data.get("latest_price")
        pct_change = stock_data.get("pct_change")
        change = stock_data.get("change")
        amount = stock_data.get("amount")
        stock_name = stock_data.get("name") or fallback_name
        return (
            f"{code} - {stock_name} - 最新价: {latest_price} "
            f"- 涨跌幅: {pct_change}% - 涨跌额: {change} "
            f"- 成交额: {amount} - 来源: API"
        )

    stock_data = fetch_stock_data_html(code)
    if stock_data and stock_data["performance"]:
        changes = ", ".join(stock_data["performance"].get("recent_changes", []))
        return f"{code} - {fallback_name} - 近期指标: {changes} - 来源: HTML"
    if stock_data:
        return f"{code} - {fallback_name} - 行情数据暂不可用 - 来源: HTML"
    return f"{code} - {fallback_name} - 获取数据失败"


def summarize_performance() -> None:
    ensure_watchlist()

    with WATCHLIST_FILE.open("r", encoding="utf-8") as file:
        lines = [line.strip() for line in file if line.strip()]

    if not lines:
        print("Watchlist is empty.")
        return

    for line in lines:
        parts = line.split("|", 1)
        if len(parts) != 2:
            print(f"Invalid watchlist entry: {line}")
            continue

        code, name = parts
        print(summarize_line(code, name))
        time.sleep(1)


if __name__ == "__main__":
    summarize_performance()
