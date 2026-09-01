#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fetch_calendar.py — 模块 C 财经日历 / 重磅事件采集（P1）

「盘前雷达」skill 的数据采集层之一。
基于华尔街见闻宏观日历接口（wallstreetcn.com），拉取当日 + 次日的宏观经济数据发布、
政策会议、央行讲话、交易所休市等事件，按重要性分级输出。

设计原则：
  1. 纯标准库（urllib），零第三方依赖。
  2. start/end 参数必须是 Unix 时间戳（东八区），public_date 同为时间戳，需转东八区显示。
  3. importance 取值 1~4，4 为最重磅（如官方 PMI、美联储主席讲话），默认只输出 >=2。
  4. 只取「标题 + 国家 + 时间 + 重要性」，不抓全文，规避时政转载红线。

用法：
  python3 fetch_calendar.py                 # 打印 JSON 到 stdout
  python3 fetch_calendar.py --pretty        # 美化打印
  python3 fetch_calendar.py --days 2        # 拉取今天 + 明天（默认）
  python3 fetch_calendar.py --min-importance 3   # 只输出重要(>=3)事件
"""

import json
import sys
import time
import urllib.request
from datetime import datetime, timedelta, timezone

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
TIMEOUT = 15
TZ = timezone(timedelta(hours=8))  # 东八区

API_URL = "https://api-one-wscn.awtmt.com/apiv1/finance/macrodatas"

# importance 数字 -> 中文语义
IMPORTANCE_LEVEL = {
    4: "重磅",
    3: "重要",
    2: "一般",
    1: "琐碎",
}


def _get(url):
    """HTTP GET，带 UA 与 Referer（华尔街见闻要求 Referer）。"""
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Referer": "https://wallstreetcn.com/",
    })
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return resp.read().decode("utf-8", "ignore")


def fetch_events(days=2):
    """拉取从今天 00:00 起 `days` 天内的事件，返回原始 items 列表。"""
    now = datetime.now(TZ)
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    start_ts = int(today_start.timestamp())
    end_ts = int((today_start + timedelta(days=days)).timestamp())

    url = f"{API_URL}?start={start_ts}&end={end_ts}"
    data = json.loads(_get(url))
    return data.get("data", {}).get("items", [])


def collect(days=2, min_importance=2):
    """采集并结构化财经日历事件。"""
    items = fetch_events(days=days)

    events = []
    for it in items:
        imp = it.get("importance") or 0
        if imp < min_importance:
            continue
        pd = it.get("public_date") or 0
        dt_str = ""
        if pd:
            dt = datetime.fromtimestamp(int(pd), tz=TZ)
            dt_str = dt.strftime("%m-%d %H:%M")
        events.append({
            "time": dt_str,
            "country": it.get("country") or "",
            "title": (it.get("title") or "").strip(),
            "importance": imp,
            "importance_label": IMPORTANCE_LEVEL.get(imp, "未知"),
            "actual": it.get("actual") or "",
            "forecast": it.get("forecast") or "",
            "previous": it.get("previous") or "",
        })

    # 按时间排序（无时间的排后面）
    events.sort(key=lambda e: e["time"])

    highlights = [e for e in events if e["importance"] >= 3]

    return {
        "ts": time.strftime("%Y-%m-%d %H:%M:%S"),
        "source": "华尔街见闻宏观日历 (wallstreetcn.com, free, no key)",
        "range_days": days,
        "total_events": len(events),
        "highlight_count": len(highlights),
        "highlights": highlights,
        "events": events,
    }


def main():
    args = sys.argv[1:]
    pretty = "--pretty" in args
    days = 2
    min_importance = 2
    if "--days" in args:
        days = int(args[args.index("--days") + 1])
    if "--min-importance" in args:
        min_importance = int(args[args.index("--min-importance") + 1])

    out = collect(days=days, min_importance=min_importance)
    if pretty:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        print(json.dumps(out, ensure_ascii=False))


if __name__ == "__main__":
    main()
