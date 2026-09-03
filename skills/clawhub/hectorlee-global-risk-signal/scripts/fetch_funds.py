#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fetch_funds.py — 模块 E 中国资金面采集（P1）

「盘前雷达」skill 的数据采集层之一。
采集 A 股特有的资金面信号：两融余额（融资融券杠杆）、龙虎榜（游资/机构动向）、
沪深港通成交（北向资金口径）、在岸人民币（替代每日中间价）。

设计原则：
  1. 纯标准库（urllib），零第三方依赖。
  2. 数据源均为东方财富数据中心 / 新浪财经公开接口，免费、无 key。
  3. 北向资金实时「净买入」自 2024-08 起已停披，仅成交额 / 额度状态可用（脚本已适配）。
  4. 金额统一换算为「亿元」，涨跌幅为百分比。

用法：
  python3 fetch_funds.py            # 打印 JSON 到 stdout
  python3 fetch_funds.py --pretty   # 美化打印
"""

import json
import sys
import time
import urllib.request
import urllib.parse

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
TIMEOUT = 15

# 东方财富数据中心通用接口
DC = "https://datacenter-web.eastmoney.com/api/data/v1/get"

# 新浪外汇报价
SINA_FX = "https://hq.sinajs.cn/list=fx_susdcny"

# 沪深港通 MUTUAL_TYPE 含义（东财接口）
MUTUAL_TYPE_MAP = {
    "001": "沪股通(北向)",
    "002": "港股通沪(南向)",
    "003": "深股通(北向)",
    "004": "港股通深(南向)",
    "005": "北向资金汇总",
    "006": "南向资金汇总",
}


def _get(url, gbk=False, referer=None):
    headers = {"User-Agent": UA}
    if referer:
        headers["Referer"] = referer
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        raw = resp.read()
    return raw.decode("gbk" if gbk else "utf-8", "ignore")


def _dc_get(report_name, columns="ALL", page_size=20, sort_columns="", sort_types="-1", extra=""):
    """调用东方财富 datacenter-web 通用数据接口，返回 data 列表。"""
    params = {
        "reportName": report_name,
        "columns": columns,
        "pageSize": str(page_size),
        "pageNumber": "1",
        "source": "WEB",
        "client": "WEB",
    }
    if sort_columns:
        params["sortColumns"] = sort_columns
        params["sortTypes"] = sort_types
    url = DC + "?" + urllib.parse.urlencode(params) + extra
    data = json.loads(_get(url))
    if not data.get("result"):
        return []
    return data["result"].get("data") or []


def _yi(x):
    """元 -> 亿元，保留 2 位小数；非法返回 None。"""
    try:
        if x is None:
            return None
        return round(float(x) / 1e8, 2)
    except (TypeError, ValueError):
        return None


def fetch_margin():
    """两融余额（最新交易日）。"""
    rows = _dc_get("RPTA_RZRQ_LSHJ", page_size=1, sort_columns="DIM_DATE", sort_types="-1")
    if not rows:
        return {"error": "no_data"}
    r = rows[0]
    return {
        "date": (r.get("DIM_DATE") or "")[:10],
        "rz_balance_yi": _yi(r.get("RZYE")),          # 融资余额
        "rq_balance_yi": _yi(r.get("RQYE")),          # 融券余额
        "rzrq_balance_yi": _yi(r.get("RZRQYE")),      # 两融余额合计
        "rz_net_buy_yi": _yi(r.get("RZJME")),         # 融资净买入
        "balance_change_pct": r.get("ZDF"),           # 两融余额较前日涨跌幅%
    }


def fetch_dragon_tiger(limit=15):
    """龙虎榜（最新交易日，按净买入额排序取前 N）。"""
    rows = _dc_get("RPT_DAILYBILLBOARD_DETAILSNEW", page_size=200,
                   sort_columns="TRADE_DATE", sort_types="-1")
    if not rows:
        return {"error": "no_data"}
    date = (rows[0].get("TRADE_DATE") or "")[:10]
    # 只保留最新交易日，按净买入额降序
    rows = [r for r in rows if (r.get("TRADE_DATE") or "").startswith(date)]
    rows.sort(key=lambda r: -(r.get("BILLBOARD_NET_AMT") or 0))
    # 按股票代码去重（同一股票可因多个上榜原因重复出现，保留净买入最大那条）
    dedup = {}
    for r in rows:
        code = r.get("SECURITY_CODE")
        if code not in dedup:
            dedup[code] = r
    top = list(dedup.values())[:limit]
    return {
        "date": date,
        "list": [
            {
                "code": r.get("SECURITY_CODE"),
                "name": r.get("SECURITY_NAME_ABBR"),
                "close": r.get("CLOSE_PRICE"),
                "change_pct": r.get("CHANGE_RATE"),
                "reason": r.get("EXPLANATION"),
                "net_buy_yi": _yi(r.get("BILLBOARD_NET_AMT")),
                "buy_yi": _yi(r.get("BILLBOARD_BUY_AMT")),
                "sell_yi": _yi(r.get("BILLBOARD_SELL_AMT")),
            }
            for r in top
        ],
    }


def fetch_northbound():
    """沪深港通成交（北向口径，最新交易日）。"""
    rows = _dc_get("RPT_MUTUAL_DEAL_HISTORY", page_size=10,
                   sort_columns="TRADE_DATE", sort_types="-1")
    if not rows:
        return {"error": "no_data"}
    date = (rows[0].get("TRADE_DATE") or "")[:10]
    rows = [r for r in rows if (r.get("TRADE_DATE") or "").startswith(date)]
    return {
        "date": date,
        "note": "北向实时净买入自2024-08起停披，仅成交额/额度可用",
        "list": [
            {
                "type": r.get("MUTUAL_TYPE"),
                "type_name": MUTUAL_TYPE_MAP.get(r.get("MUTUAL_TYPE"), r.get("MUTUAL_TYPE")),
                # DEAL_AMT 原始单位百万元，÷100 得亿元
                "deal_amt_yi": round((r.get("DEAL_AMT") or 0) / 100, 2),
                "quota": r.get("QUOTA_BALANCE_TEXT"),
                "lead_stock": r.get("LEAD_STOCKS_NAME"),
            }
            for r in rows
        ],
    }


def fetch_cny_onshore():
    """在岸人民币（新浪，替代每日中间价）。"""
    try:
        raw = _get(SINA_FX, gbk=True, referer="https://finance.sina.com.cn")
        f = raw.split('"')[1].split(",")
        price = float(f[1]) if len(f) > 1 else None
        prev = float(f[2]) if len(f) > 2 else None
        change = round(price - prev, 4) if (price is not None and prev) else None
        pct = round((price - prev) / prev * 100, 4) if (price is not None and prev) else None
        return {
            "name": f[9] if len(f) > 9 else "在岸人民币",
            "price": price,
            "prev_close": prev,
            "change": change,
            "change_pct": pct,
            "time": f[0] if f else "",
            "date": f[17] if len(f) > 17 else "",
        }
    except Exception:
        return {"error": "fetch_failed"}


def collect():
    return {
        "ts": time.strftime("%Y-%m-%d %H:%M:%S"),
        "source": "东方财富数据中心 + 新浪财经 (free, no key)",
        "margin_trading": fetch_margin(),
        "dragon_tiger": fetch_dragon_tiger(),
        "northbound": fetch_northbound(),
        "cny_onshore": fetch_cny_onshore(),
    }


def main():
    pretty = "--pretty" in sys.argv
    out = collect()
    if pretty:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        print(json.dumps(out, ensure_ascii=False))


if __name__ == "__main__":
    main()
