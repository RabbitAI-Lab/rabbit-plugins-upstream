#!/usr/bin/env python3
"""
黄金追踪 - 摘要生成器
从最新日志和状态生成简报或完整摘要。
零第三方依赖。
"""

import json
import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TZ_BEIJING = timezone(timedelta(hours=8))

TERM_MAP = {
    "FOMC": "美联储公开市场委员会",
    "ECB": "欧洲央行",
    "DXY": "美元指数",
    "CPI": "消费者物价指数",
    "PCE": "个人消费支出价格指数",
    "GS": "高盛",
    "SEP": "经济预测摘要",
    "Warsh": "沃什",
    "Q3": "三季度",
    "Q2": "二季度",
    "Q1": "一季度",
    "Q4": "四季度",
    "鹰派": "鹰派",
    "点阵图": "点阵图",
    "布伦特": "布伦特原油",
    "胡塞": "胡塞武装",
    "沙特": "沙特",
    "油轮": "油轮",
    "加息": "加息",
    "降息": "降息",
    "议息": "议息会议",
    "通胀": "通货膨胀",
    "美联储": "美联储",
    "利率决议": "利率决议",
    "避险": "避险",
    "利多": "利多",
    "利空": "利空",
    "中性": "中性",
}


def translate_text(text: str) -> str:
    for en, zh in TERM_MAP.items():
        text = text.replace(en, zh)
    return text


def load_state() -> dict:
    f = ROOT / "state.json"
    if not f.exists():
        return {}
    try:
        return json.loads(f.read_text())
    except Exception:
        return {}


def load_latest_log() -> dict:
    logs_dir = ROOT / "logs"
    if not logs_dir.exists():
        return {"key_factors": [], "sources": [], "summary": {}}

    today = datetime.now(TZ_BEIJING).strftime("%Y-%m-%d")
    files = sorted(
        f for f in logs_dir.iterdir()
        if f.suffix in (".yaml", ".yml") and today in f.name
    )
    if not files:
        return {"key_factors": [], "sources": [], "summary": {}}

    text = files[-1].read_text(encoding="utf-8")
    return parse_log(text)


def parse_log(text: str) -> dict:
    result = {"key_factors": [], "sources": [], "summary": {}}

    m = re.search(r'focus:\s*"([^"]+)"', text)
    if m:
        result["summary"]["focus"] = m.group(1)

    blocks = re.findall(
        r'- factor:\s*"([^"]+)"\s+impact:\s*"?([^"\n]+)"?\s+reasoning:\s*"([^"]+)"',
        text
    )
    for factor, impact, reasoning in blocks:
        result["key_factors"].append({
            "factor": translate_text(factor),
            "impact": impact.strip(),
            "reasoning": translate_text(reasoning),
        })

    sources = re.findall(r'^  -\s*"?(https?://[^"\n]+)"?', text, re.MULTILINE)
    result["sources"] = sources

    return result


def impact_emoji(impact: str) -> str:
    return {
        "bullish": "🟢", "bearish": "🔴", "mixed": "🟡",
        "neutral": "⚪", "slightly_bullish": "🟢",
        "slightly_bearish": "🔴",
    }.get(impact, "⚪")


def impact_zh(impact: str) -> str:
    return {
        "bullish": "看多", "bearish": "看空", "mixed": "多空交织",
        "neutral": "中性", "slightly_bullish": "偏多",
        "slightly_bearish": "偏空",
    }.get(impact, impact)


def url_to_name(url: str) -> str:
    name = url.replace("https://", "").replace("http://", "").split("/")[0]
    if name == "goldpricez.com":
        return "黄金价格网"
    if name == "tradingeconomics.com":
        return "交易经济学"
    if name == "primerates.com":
        return "基准利率网"
    if name == "financecalendar.com" or name == "www.financecalendar.com":
        return "财经日历"
    if name == "ndtvprofit.com" or name == "www.ndtvprofit.com":
        return "NDTV财经"
    if name == "forecasts.org" or name == "www.forecasts.org":
        return "预测网"
    if name == "goldsilver.com":
        return "黄金白银网"
    if name == "kenmacro.com":
        return "KenMacro"
    if name == "open.er-api.com":
        return "汇率API"
    if name == "cambridgecurrencies.com":
        return "剑桥货币"
    return name


def generate_brief() -> str:
    state = load_state()
    log = load_latest_log()

    price = state.get("current_price")
    chg_abs = state.get("change_abs", 0)
    chg_pct = state.get("change_pct", 0)

    lines = [
        "🥇 **黄金追踪** · 简报",
        "",
        f"💰 **金价**: ${price} ({chg_abs:+.2f}, {chg_pct:+.2f}%)" if price else "💰 **金价**: 数据不可用",
        "",
    ]

    if log["summary"].get("focus"):
        lines.append("📌 **核心判断**:")
        lines.append("  " + translate_text(log["summary"]["focus"]))
        lines.append("")

    lines.append("🎯 **关键因素与逻辑**:")
    lines.append("")

    for f in log["key_factors"][:4]:
        lines.append(f"  {impact_emoji(f['impact'])} **{f['factor']}**")
        reasoning = f["reasoning"]
        lines.append(f"     → {reasoning}")
        lines.append("")

    src_names = list(dict.fromkeys(url_to_name(s) for s in log["sources"][:3]))
    lines.append(f"📰 来源: {', '.join(src_names)}")

    return "\n".join(lines)


def generate_full() -> str:
    state = load_state()
    log = load_latest_log()

    lines = [
        "# 黄金追踪 — 完整摘要",
        f"生成时间: {datetime.now(TZ_BEIJING).strftime('%Y年%m月%d日 %H:%M')}",
        "",
        "## 📊 核心数据",
    ]

    price = state.get("current_price")
    if price:
        lines.append(f"- 金价: ${price}")
        cny = state.get("price_cny_per_gram")
        if not cny and state.get("usd_cny"):
            cny = round(price * state["usd_cny"] / 31.1034768, 2)
        lines.append(f"- 人民币: ¥{cny or 'N/A'}/克")
        lines.append(f"- 汇率: {state.get('usd_cny', 'N/A')}")
        lines.append(f"- 变动: {state.get('change_abs', 0):+.2f} ({state.get('change_pct', 0):+.2f}%)")
    else:
        lines.append("- 数据不可用")

    if log["summary"].get("focus"):
        lines.append("")
        lines.append("## 📌 核心判断")
        lines.append(translate_text(log["summary"]["focus"]))

    lines.append("")
    lines.append("## 🎯 关键因素（含逻辑链）")
    lines.append("")

    for i, f in enumerate(log["key_factors"], 1):
        lines.append(f"{i}. **{f['factor']}**")
        lines.append(f"   - 方向: {impact_zh(f['impact'])} {impact_emoji(f['impact'])}")
        lines.append(f"   - 逻辑: {f['reasoning']}")
        lines.append("")

    lines.append("## 📰 信息来源")
    src_names = list(dict.fromkeys(url_to_name(s) for s in log["sources"]))
    for s in src_names:
        lines.append(f"- {s}")

    return "\n".join(lines)


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "brief"

    if mode == "brief":
        print(generate_brief())
    elif mode == "full":
        print(generate_full())
    else:
        print(f"用法: {sys.argv[0]} [brief|full]")
        sys.exit(1)


if __name__ == "__main__":
    main()
