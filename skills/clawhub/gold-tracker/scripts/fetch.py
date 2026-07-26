#!/usr/bin/env python3
"""
黄金追踪 - 数据获取器
获取金价和汇率，带验证、缓存和状态更新。
零第三方依赖。
"""

import json
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE_DIR = ROOT / ".cache"
STATE_FILE = ROOT / "state.json"
CONFIG_FILE = ROOT / "config.yaml"

CACHE_DIR.mkdir(exist_ok=True)

OZ_TO_GRAM = 31.1034768
TZ_BEIJING = timezone(timedelta(hours=8))


def load_config() -> dict:
    """无需 PyYAML 的简单配置加载（只读取关键值）。"""
    cfg = {
        "gold_url": "https://goldpricez.com",
        "gold_timeout": 15,
        "gold_min": 1000.0,
        "gold_max": 10000.0,
        "fx_url": "https://open.er-api.com/v6/latest/USD",
        "fx_timeout": 10,
        "fx_min": 6.0,
        "fx_max": 8.0,
        "cache_ttl": 300,
    }
    if CONFIG_FILE.exists():
        text = CONFIG_FILE.read_text(encoding="utf-8")
        m = re.search(r'url:\s*"([^"]+goldpricez[^"]+)"', text)
        if m: cfg["gold_url"] = m.group(1)
        m = re.search(r'timeout:\s*(\d+)', text)
        if m: cfg["gold_timeout"] = int(m.group(1))
        m = re.search(r'min_price_usd:\s*([\d.]+)', text)
        if m: cfg["gold_min"] = float(m.group(1))
        m = re.search(r'max_price_usd:\s*([\d.]+)', text)
        if m: cfg["gold_max"] = float(m.group(1))
        m = re.search(r'ttl_seconds:\s*(\d+)', text)
        if m: cfg["cache_ttl"] = int(m.group(1))
    return cfg


def fetch_url(url: str, timeout: int) -> str:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "GoldTracker/1.0"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")


def get_cache(key: str, ttl: int) -> dict:
    f = CACHE_DIR / f"{key}.json"
    if not f.exists():
        return {}
    try:
        data = json.loads(f.read_text())
        if time.time() - data.get("_t", 0) < ttl:
            return data
    except Exception:
        pass
    return {}


def set_cache(key: str, data: dict):
    f = CACHE_DIR / f"{key}.json"
    data["_t"] = time.time()
    f.write_text(json.dumps(data))


def parse_gold_price(html: str) -> float:
    """从 HTML 提取金价（美元/盎司）。失败返回 0。"""
    patterns = [
        r'class="gold-price"[^>]*>\$?([\d,]+\.?\d*)',
        r'Gold Price.*?\$([\d,]+\.?\d*)',
        r'"price":\s*"?([\d,]+\.?\d*)"?',
        r'\$([\d,]{4,}\.\d{2})',
    ]
    for pat in patterns:
        m = re.search(pat, html, re.IGNORECASE)
        if m:
            try:
                return float(m.group(1).replace(",", ""))
            except ValueError:
                continue
    return 0.0


def parse_cny_rate(text: str) -> float:
    """从 JSON API 响应提取美元兑人民币汇率。失败返回 0。"""
    try:
        data = json.loads(text)
        return float(data["rates"]["CNY"])
    except Exception:
        m = re.search(r'"CNY":\s*([\d.]+)', text)
        if m:
            try:
                return float(m.group(1))
            except ValueError:
                pass
    return 0.0


def fetch_all() -> dict:
    cfg = load_config()
    now = datetime.now(TZ_BEIJING)
    result = {
        "timestamp": now.isoformat(),
        "price_usd": 0.0,
        "price_cny_per_gram": 0.0,
        "usd_cny": 0.0,
        "sources": {},
        "errors": [],
    }

    # 金价
    cache = get_cache("gold", cfg["cache_ttl"])
    if cache.get("price"):
        result["price_usd"] = cache["price"]
        result["sources"]["gold"] = "cache"
    else:
        try:
            html = fetch_url(cfg["gold_url"], cfg["gold_timeout"])
            price = parse_gold_price(html)
            if cfg["gold_min"] <= price <= cfg["gold_max"]:
                result["price_usd"] = price
                result["sources"]["gold"] = cfg["gold_url"]
                set_cache("gold", {"price": price})
            else:
                result["errors"].append(f"金价异常: {price}")
        except Exception as e:
            result["errors"].append(f"金价获取失败: {e}")

    # 汇率
    cache = get_cache("fx", cfg["cache_ttl"])
    if cache.get("rate"):
        result["usd_cny"] = cache["rate"]
        result["sources"]["fx"] = "cache"
    else:
        try:
            text = fetch_url(cfg["fx_url"], cfg["fx_timeout"])
            rate = parse_cny_rate(text)
            if cfg["fx_min"] <= rate <= cfg["fx_max"]:
                result["usd_cny"] = rate
                result["sources"]["fx"] = cfg["fx_url"]
                set_cache("fx", {"rate": rate})
            else:
                result["errors"].append(f"汇率异常: {rate}")
        except Exception as e:
            result["errors"].append(f"汇率获取失败: {e}")

    # 计算人民币金价（元/克）
    if result["price_usd"] and result["usd_cny"]:
        result["price_cny_per_gram"] = round(
            result["price_usd"] * result["usd_cny"] / OZ_TO_GRAM, 2
        )

    return result


def update_state(data: dict):
    state = {}
    if STATE_FILE.exists():
        try:
            state = json.loads(STATE_FILE.read_text())
        except Exception:
            state = {}

    last_price = state.get("current_price", 0.0)
    current = data["price_usd"]

    state.update({
        "date": datetime.now(TZ_BEIJING).strftime("%Y-%m-%d"),
        "last_update": data["timestamp"],
        "current_price": current,
        "price_cny_per_gram": data["price_cny_per_gram"],
        "usd_cny": data["usd_cny"],
        "sources": data["sources"],
    })

    if last_price and current:
        change = current - last_price
        state["last_price"] = last_price
        state["change_pct"] = round((change / last_price) * 100, 2)
        state["change_abs"] = round(change, 2)
    else:
        state["last_price"] = current
        state["change_pct"] = 0.0
        state["change_abs"] = 0.0

    STATE_FILE.write_text(json.dumps(state, indent=2))


def main():
    data = fetch_all()
    print(json.dumps(data, indent=2))

    if data["price_usd"]:
        update_state(data)
        print(f"[成功] state.json 更新: ${data['price_usd']}", file=sys.stderr)

    if data["errors"]:
        for e in data["errors"]:
            print(f"[警告] {e}", file=sys.stderr)
        sys.exit(1 if not data["price_usd"] else 0)


if __name__ == "__main__":
    main()
