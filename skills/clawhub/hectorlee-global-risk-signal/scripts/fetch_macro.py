#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fetch_macro.py — 模块 D 宏观数据采集（P2）

「盘前雷达」skill 的数据采集层之一。采集盘前判断所需的宏观底色指标：
  1. 中国 PMI / CPI / PPI（东方财富数据中心，月度，无 key）
  2. 全球底色（World Bank API，年度，无 key）
  3. 美国高频宏观（FRED，可选 key，读环境变量 FRED_API_KEY）

设计原则：
  1. 纯标准库（urllib），零第三方依赖，开箱即用。
  2. 多级降级：东财直连 -> World Bank -> FRED（可选）-> 标记缺失。
  3. 无 key 也能跑：FRED 缺失时用 World Bank 年度数据兜底美国宏观。
  4. 宏观数据是低频底色，用于情景推演背景，不做高频方向信号（方向信号在行情层）。

用法：
  python3 fetch_macro.py            # 打印 JSON 到 stdout
  python3 fetch_macro.py --pretty   # 美化打印
"""

import json
import os
import sys
import time
import urllib.request
import urllib.parse

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
TIMEOUT = 12
DC = "https://datacenter-web.eastmoney.com/api/data/v1/get"


def http_get_json(url, retries=2):
    """GET 请求，返回解析后的 JSON（dict/list）；失败返回 None。"""
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                raw = resp.read()
            return json.loads(raw.decode("utf-8", "ignore"))
        except Exception:
            if attempt < retries:
                time.sleep(0.5 * (attempt + 1))
    return None


def _f(x):
    """安全转 float。"""
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


# ---------------------------------------------------------------------------
# 1. 中国宏观（东方财富数据中心，月度，无 key）
# ---------------------------------------------------------------------------
def _fetch_em_macro(report_name, sort_col="REPORT_DATE"):
    """通用东财宏观接口，返回最新一条 data 行（dict）或 None。"""
    params = {
        "reportName": report_name,
        "columns": "ALL",
        "pageSize": "3",
        "pageNumber": "1",
        "sortColumns": sort_col,
        "sortTypes": "-1",
        "source": "WEB",
        "client": "WEB",
    }
    url = DC + "?" + urllib.parse.urlencode(params)
    js = http_get_json(url)
    if not js:
        return None
    data = (js.get("result") or {}).get("data") or []
    return data[0] if data else None


def fetch_china_macro():
    """中国 PMI / CPI / PPI 月度数据。返回 {pmi, cpi, ppi}。"""
    out = {}

    # 制造业/非制造业 PMI
    pmi_row = _fetch_em_macro("RPT_ECONOMY_PMI")
    if pmi_row:
        out["pmi"] = {
            "time": pmi_row.get("TIME", ""),
            "manufacturing": _f(pmi_row.get("MAKE_INDEX")),
            "non_manufacturing": _f(pmi_row.get("NMAKE_INDEX")),
            "make_same": _f(pmi_row.get("MAKE_SAME")),
            "source": "eastmoney",
        }

    # CPI（全国）
    cpi_row = _fetch_em_macro("RPT_ECONOMY_CPI")
    if cpi_row:
        out["cpi"] = {
            "time": cpi_row.get("TIME", ""),
            "yoy": _f(cpi_row.get("NATIONAL_SAME")),
            "mom": _f(cpi_row.get("NATIONAL_SEQUENTIAL")),
            "source": "eastmoney",
        }

    # PPI
    ppi_row = _fetch_em_macro("RPT_ECONOMY_PPI")
    if ppi_row:
        out["ppi"] = {
            "time": ppi_row.get("TIME", ""),
            "yoy": _f(ppi_row.get("BASE_SAME")),
            "source": "eastmoney",
        }

    return out


# ---------------------------------------------------------------------------
# 2. 全球底色（World Bank API，年度，无 key）
#   指标：GDP 增速 / CPI 年化 / 失业率，覆盖美国、中国、全球
# ---------------------------------------------------------------------------
WB = "https://api.worldbank.org/v2/country/{}/indicator/{}?format=json&per_page=3"

# (指标代码, 指标名, 单位后缀)
WB_INDICATORS = [
    ("NY.GDP.MKTP.KD.ZG", "gdp_growth", "%"),
    ("FP.CPI.TOTL.ZG", "cpi_yoy", "%"),
    ("SL.UEM.TOTL.ZS", "unemployment", "%"),
]
# (国家代码, 国家名)
WB_COUNTRIES = [
    ("USA", "美国"),
    ("CHN", "中国"),
    ("WLD", "全球"),
]


def _fetch_wb_indicator(country, indicator):
    """拉取某国某指标的最近若干年，返回 [(year, value), ...]，剔除 null。"""
    url = WB.format(country, indicator)
    js = http_get_json(url)
    if not js or not isinstance(js, list) or len(js) < 2:
        return []
    rows = js[1]
    out = []
    for r in rows:
        v = r.get("value")
        if v is None:
            continue
        out.append((r.get("date"), _f(v)))
    return out


def fetch_worldbank():
    """World Bank 全球底色。返回 {美国: {gdp_growth: {year, value}, ...}, ...}。"""
    out = {}
    for code, name in WB_COUNTRIES:
        entry = {}
        for indicator, key, unit in WB_INDICATORS:
            series = _fetch_wb_indicator(code, indicator)
            if series:
                # 取最新一年（series 已按年份降序）
                year, value = series[0]
                prev = series[1][1] if len(series) > 1 else None
                entry[key] = {
                    "year": year,
                    "value": value,
                    "prev": prev,
                    "unit": unit,
                }
        if entry:
            entry["name"] = name
            out[code] = entry
    return out


# ---------------------------------------------------------------------------
# 3. 美国高频宏观（FRED，可选 key）
#    读环境变量 FRED_API_KEY；无 key 时跳过，返回空 dict（由 World Bank 兜底）
# ---------------------------------------------------------------------------
FRED = "https://api.stlouisfed.org/fred/series/observations"

# (series_id, 说明)
FRED_SERIES = [
    ("CPIAUCSL", "美国CPI指数"),
    ("UNRATE", "美国失业率"),
    ("DFF", "联邦基金有效利率"),
    ("T10Y2Y", "美债10Y-2Y利差"),
]


def _fred_latest(series_id, api_key):
    """拉取 FRED 某序列最近观测值。返回 (date, value)；失败返回 None。"""
    params = {
        "series_id": series_id,
        "api_key": api_key,
        "file_type": "json",
        "sort_order": "desc",
        "limit": "3",
    }
    url = FRED + "?" + urllib.parse.urlencode(params)
    js = http_get_json(url)
    if not js:
        return None
    obs = js.get("observations") or []
    for o in obs:
        v = o.get("value")
        if v is None or v == ".":
            continue
        return o.get("date"), _f(v)
    return None


def fetch_fred():
    """美国高频宏观（可选）。无 FRED_API_KEY 时返回空 dict。"""
    api_key = os.environ.get("FRED_API_KEY", "").strip()
    if not api_key:
        return {}
    out = {}
    for sid, label in FRED_SERIES:
        got = _fred_latest(sid, api_key)
        if got:
            date, value = got
            out[sid] = {"label": label, "date": date, "value": value}
    return out


# ---------------------------------------------------------------------------
# 汇总
# ---------------------------------------------------------------------------
def collect():
    """采集全部宏观数据，返回结构化 dict。"""
    data = {
        "china": fetch_china_macro(),
        "worldbank": fetch_worldbank(),
        "fred": fetch_fred(),
    }
    return data


def main():
    pretty = "--pretty" in sys.argv
    data = collect()
    out = {
        "ts": time.strftime("%Y-%m-%d %H:%M:%S"),
        "items": data,
    }
    if pretty:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        print(json.dumps(out, ensure_ascii=False))


if __name__ == "__main__":
    main()
