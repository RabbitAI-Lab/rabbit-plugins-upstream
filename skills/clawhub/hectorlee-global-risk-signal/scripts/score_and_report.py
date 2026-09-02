#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
score_and_report.py — 打分 + 多空情景推演 + 风险分级（「盘前雷达」决策层）

「盘前雷达」skill 的核心决策脚本。汇总五个采集脚本的数据，做经验驱动的
多空方向判断 + 风险分级 + 多空情景推演，输出结构化报告（也是信号卡渲染的输入）。

设计原则：
  1. 经验驱动、可解释——每个信号都有明确的「利多/利空方向 + 阈值 + 权重」，
     不搞黑箱机器学习打分。
  2. 多空情景推演，而非单一机械结论（贴合用户「多空情景推演」偏好）。
  3. 纯标准库，零第三方依赖。
  4. 所有方向判断遵循 A 股习惯：红 = 利多、绿 = 利空。

方向信号约定：
  - 权益类（A50 / 纳指期货 / 标普期货）：涨 = 利多，跌 = 利空。
  - 离岸人民币（USD/CNH）：跌 = 人民币升值 = 利多 A 股。
  - 美元指数：跌 = 美元走弱 = 利多 A 股。
  - VIX：跌 = 恐慌缓解 = 利多。
  - 美债 10Y 收益率：跌 = 利多（尤其成长股）。

用法：
  python3 score_and_report.py            # 打印报告 JSON
  python3 score_and_report.py --pretty   # 美化打印
"""

import json
import sys
import time
from datetime import datetime, timedelta, timezone

import fetch_market
import fetch_geopolitics
import fetch_calendar
import fetch_funds
import fetch_news_cn
import fetch_macro

TZ = timezone(timedelta(hours=8))
WEEKDAY_MAP = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]

# ---------------------------------------------------------------------------
# 方向信号配置：(数据key, 利多方向, 阈值%, 权重, 标签)
#   利多方向 +1 = 涨利多；-1 = 跌利多
# ---------------------------------------------------------------------------
SIGNALS = [
    ("hf_CHA50CFD", +1, 0.2, 2.0, "A50期货"),
    ("fx_susdcnh",  -1, 0.05, 1.5, "离岸人民币"),
    ("hf_NQ",       +1, 0.3, 1.5, "纳指期货"),
    ("hf_ES",       +1, 0.3, 1.0, "标普期货"),
    ("DINIW",       -1, 0.2, 1.0, "美元指数"),
    ("hf_VX",       -1, 2.0, 1.0, "VIX恐慌指数"),
]
UST10Y_THRESHOLD = 0.03   # 美债10Y 收益率变化阈值（百分点，3bp）
UST10Y_WEIGHT = 0.5

# 地缘 / 黑天鹅关键词
BLACK_SWAN_EN = ["attack", "strike", "missile", "invasion", "war", "blockade",
                 "hijack", "tanker", "strait", "sanctions", "nuclear", "crash",
                 "escalat", "strike"]
BLACK_SWAN_CN = ["遇袭", "袭击", "攻击", "导弹", "空袭", "封锁", "断航", "油轮",
                 "海峡", "制裁", "危机", "崩盘", "暴跌", "熔断", "宣战", "入侵",
                 "冲突升级", "战争"]


def _f(x):
    """安全转 float。"""
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def _fmt_pct(pct):
    """格式化涨跌幅为带符号字符串，如 '+0.32%' / '-0.65%' / '0.00%'。"""
    if pct is None:
        return ""
    return f"{pct:+.2f}%"


def _fmt_price(price, pct, is_yield=False, precision=2):
    """格式化展示字符串。is_yield 时变化为百分点（不带 %）。"""
    if price is None:
        return "--"
    if is_yield:
        # 收益率：'4.73%'，变化 '+0.06'
        change = "" if pct is None else f"{pct:+.2f}"
        return f"{price:.2f}%{(' ' + change) if change else ''}"
    pct_s = _fmt_pct(pct)
    return f"{price:.{precision}f}{(' ' + pct_s) if pct_s else ''}"


def _classify(direction, change_pct, threshold):
    """按「利多方向调整后的涨跌」判定 rk-up / rk-dn / rk-nt。"""
    if change_pct is None:
        return "rk-nt"
    adj = direction * change_pct
    if adj >= threshold:
        return "rk-up"
    if adj <= -threshold:
        return "rk-dn"
    return "rk-nt"


# ---------------------------------------------------------------------------
# 方向打分
# ---------------------------------------------------------------------------
def _score_direction(market):
    """返回 (bull, bear, bull_list, bear_list)，权重分 + 明细。"""
    bull = 0.0
    bear = 0.0
    bull_list = []
    bear_list = []
    for key, direction, threshold, weight, label in SIGNALS:
        item = market.get(key) or {}
        pct = item.get("change_pct")
        adj = direction * pct if pct is not None else None
        if adj is None:
            continue
        if adj >= threshold:
            bull += weight
            bull_list.append(f"{label} {_fmt_pct(pct)}")
        elif adj <= -threshold:
            bear += weight
            bear_list.append(f"{label} {_fmt_pct(pct)}")
    # 美债 10Y（收益率变化，单位百分点，跌=利多）
    uy = market.get("ust_yield") or {}
    us10 = uy.get("us10y")
    us10_change = uy.get("change")
    if us10_change is not None:
        adj = -us10_change  # 收益率跌=利多
        if adj >= UST10Y_THRESHOLD:
            bull += UST10Y_WEIGHT
            bull_list.append(f"美债10Y {_fmt_price(us10, us10_change, True)}")
        elif adj <= -UST10Y_THRESHOLD:
            bear += UST10Y_WEIGHT
            bear_list.append(f"美债10Y {_fmt_price(us10, us10_change, True)}")
    return bull, bear, bull_list, bear_list


def _verdict(bull, bear):
    """由加权分判定方向。"""
    if bull >= bear + 2 and bull >= 3:
        return "偏多"
    if bear >= bull + 2 and bear >= 3:
        return "偏空"
    return "中性"


# ---------------------------------------------------------------------------
# 地缘风险检测
# ---------------------------------------------------------------------------
def _detect_geo(geo, news):
    """返回 (风险等级文字, 命中标题列表)。"""
    hits = []
    for theme_key in ("conflict", "mideast", "trade"):
        theme = geo.get(theme_key) or {}
        for a in theme.get("articles", []):
            title = (a.get("title") or "").lower()
            if any(w in title for w in BLACK_SWAN_EN):
                hits.append(a.get("title", ""))
    for x in (news.get("eastmoney_flash") or []):
        title = x.get("title") or ""
        if any(w in title for w in BLACK_SWAN_CN):
            hits.append(title)
    for x in (news.get("sina_roll") or []):
        title = x.get("title") or ""
        if any(w in title for w in BLACK_SWAN_CN):
            hits.append(title)
    # 去重
    hits = list(dict.fromkeys(hits))
    if len(hits) >= 3:
        level = "高"
    elif len(hits) >= 1:
        level = "中"
    else:
        level = "低"
    return level, hits


# ---------------------------------------------------------------------------
# 风险分级（1-5）
# ---------------------------------------------------------------------------
def _score_risk(market, geo_level, calendar, geo_hits):
    """基础 1 分，叠加风险因子，封顶 5。"""
    risk = 1
    factors = []

    vix_item = market.get("hf_VX") or {}
    vix = _f(vix_item.get("price"))
    vix_pct = vix_item.get("change_pct")
    if vix is not None:
        if vix >= 25:
            risk += 2
            factors.append(f"VIX {vix:.1f} 处于恐慌区间")
        elif vix >= 20:
            risk += 1
            factors.append(f"VIX {vix:.1f} 偏高")
        if vix_pct is not None and vix_pct >= 8:
            risk += 1
            factors.append(f"VIX 单日急升 {_fmt_pct(vix_pct)}")

    # 美股期货大跌传导
    for key, label in (("hf_NQ", "纳指期货"), ("hf_ES", "标普期货"), ("hf_CHA50CFD", "A50期货")):
        item = market.get(key) or {}
        pct = item.get("change_pct")
        if pct is not None and pct <= -1.0:
            risk += 1
            factors.append(f"{label} 跌超 1%（{_fmt_pct(pct)}）")

    # 离岸人民币急贬
    cny = market.get("fx_susdcnh") or {}
    cny_pct = cny.get("change_pct")
    if cny_pct is not None and cny_pct >= 0.3:
        risk += 1
        factors.append(f"离岸人民币急贬 {_fmt_pct(cny_pct)}")

    # 地缘黑天鹅
    if geo_level == "高":
        risk += 2
        factors.append(f"地缘事件密集（{len(geo_hits)} 条信号）")
    elif geo_level == "中":
        risk += 1
        factors.append("地缘出现异动信号")

    # 今日重磅财经事件
    today = datetime.now(TZ).strftime("%m-%d")
    for e in (calendar.get("highlights") or []):
        if (e.get("time") or "").startswith(today) and e.get("importance", 0) >= 4:
            risk += 1
            factors.append(f"今日重磅：{e.get('title', '')[:20]}")
            break

    return min(5, risk), factors


# ---------------------------------------------------------------------------
# 汇总
# ---------------------------------------------------------------------------
RISK_TEXT = {1: "低", 2: "较低", 3: "中等", 4: "较高", 5: "高"}
VERDICT_STYLE = {
    "偏多": {"color": "#e64340", "box_bg": "#fdf0ef", "box_border": "#f6d2cf"},
    "偏空": {"color": "#1e9e6b", "box_bg": "#eef7f1", "box_border": "#cfe6d8"},
    "中性": {"color": "#8a8a86", "box_bg": "#f5f5f3", "box_border": "#e5e5e1"},
}


def collect():
    """拉数据 + 打分，返回完整报告 dict。"""
    market = fetch_market.collect()
    geo = fetch_geopolitics.collect()
    calendar = fetch_calendar.collect()
    funds = fetch_funds.collect()
    news = fetch_news_cn.collect(limit=10)
    macro = fetch_macro.collect()

    bull, bear, bull_list, bear_list = _score_direction(market)
    verdict = _verdict(bull, bear)
    geo_level, geo_hits = _detect_geo(geo, news)
    risk_level, risk_factors = _score_risk(market, geo_level, calendar, geo_hits)

    # 多空概率（clamp 25~75，避免极端）
    total = bull + bear
    if total <= 0:
        bull_pct, bear_pct = 50, 50
    else:
        bull_pct = round(max(25, min(75, bull / total * 100)))
        bear_pct = 100 - bull_pct

    # 一句话理由
    reason = _build_reason(verdict, bull_list, bear_list)

    # 今日重磅（供地缘/日历区展示）
    today = datetime.now(TZ).strftime("%m-%d")
    today_highlights = [e for e in (calendar.get("highlights") or [])
                        if (e.get("time") or "").startswith(today)][:2]

    # 卡片渲染所需的 7 个外围指标
    card_market = _build_card_market(market)

    now = datetime.now(TZ)
    return {
        "ts": time.strftime("%Y-%m-%d %H:%M:%S"),
        "date": now.strftime("%Y-%m-%d"),
        "weekday": WEEKDAY_MAP[now.weekday()],
        "verdict": verdict,
        "verdict_style": VERDICT_STYLE[verdict],
        "reason": reason,
        "bull_score": round(bull, 1),
        "bear_score": round(bear, 1),
        "bull_signals": bull_list,
        "bear_signals": bear_list,
        "risk_level": risk_level,
        "risk_text": RISK_TEXT[risk_level],
        "risk_factors": risk_factors,
        "geo_level": geo_level,
        "geo_hits": geo_hits[:3],
        "geo_note": _build_geo_note(geo_level, geo_hits),
        "scenario": {
            "bull_pct": bull_pct,
            "bear_pct": bear_pct,
            "bull_text": "、".join(bull_list) if bull_list else "无明显利多信号",
            "bear_text": "、".join(bear_list) if bear_list else "无明显利空信号",
        },
        "card_market": card_market,
        "today_highlights": today_highlights,
        "funds_summary": _funds_summary(funds),
        "macro": _macro_brief(macro, market),
        "raw": {
            "market_count": len(market),
            "geo_themes": {k: (v or {}).get("count", 0) for k, v in geo.items()},
            "calendar_events": calendar.get("total_events", 0),
        },
    }


def _build_reason(verdict, bull_list, bear_list):
    """生成一句话理由。"""
    if verdict == "偏空":
        core = "、".join(bear_list[:3]) if bear_list else "外围承压"
        return f"{core}，外围偏空"
    if verdict == "偏多":
        core = "、".join(bull_list[:3]) if bull_list else "外围走强"
        return f"{core}，外围偏多"
    return "外围涨跌互现、方向信号背离，等待开盘确认"


def _build_geo_note(geo_level, geo_hits):
    if geo_level == "高" and geo_hits:
        return f"多条地缘异动：{geo_hits[0][:28]}"
    if geo_level == "中" and geo_hits:
        return f"出现异动信号：{geo_hits[0][:28]}"
    return "地缘事件平静，无重大冲突信号"


def _build_card_market(market):
    """生成卡片 7 个外围指标的展示字符串 + 方向 class。"""
    def item(key, direction, threshold, is_yield=False, precision=2):
        d = market.get(key) or {}
        if is_yield:
            price = d.get("us10y")
            change = d.get("change")
            cls = _classify(direction, change, threshold)
            return {"text": _fmt_price(price, change, True), "cls": cls}
        price = d.get("price")
        pct = d.get("change_pct")
        cls = _classify(direction, pct, threshold)
        return {"text": _fmt_price(price, pct, precision=precision), "cls": cls}

    return {
        "a50": item("hf_CHA50CFD", +1, 0.2),
        "cny": item("fx_susdcnh", -1, 0.05, precision=4),
        "nasdaq_fut": item("hf_NQ", +1, 0.3),
        "spx_fut": item("hf_ES", +1, 0.3),
        "dxy": item("DINIW", -1, 0.2),
        "vix": item("hf_VX", -1, 2.0),
        "ust10y": item("ust_yield", -1, UST10Y_THRESHOLD, is_yield=True),
    }


def _funds_summary(funds):
    """资金面摘要（供报告展示，不进卡片主体）。"""
    out = {}
    mt = funds.get("margin_trading") or {}
    if "error" not in mt and mt.get("rzrq_balance_yi") is not None:
        out["两融余额"] = f"{mt['rzrq_balance_yi']:.0f}亿"
        if mt.get("rz_net_buy_yi") is not None:
            out["融资净买入"] = f"{mt['rz_net_buy_yi']:+.0f}亿"
    return out


def _macro_brief(macro, market):
    """宏观底色摘要（P2）：一句话 + 关键指标列表。不进方向打分，仅作情景背景。"""
    china = macro.get("china") or {}
    brief_parts = []
    metrics = []

    pmi = china.get("pmi") or {}
    if pmi.get("manufacturing") is not None:
        m = pmi["manufacturing"]
        zone = "扩张" if m >= 50 else "收缩"
        brief_parts.append(f"中国制造业PMI {m:.1f}（{zone}）")
        metrics.append(("中国制造业PMI", f"{m:.1f}（{zone}）"))

    cpi = china.get("cpi") or {}
    if cpi.get("yoy") is not None:
        brief_parts.append(f"CPI同比 {cpi['yoy']:+.1f}%")
        metrics.append(("中国CPI同比", f"{cpi['yoy']:+.1f}%"))

    ppi = china.get("ppi") or {}
    if ppi.get("yoy") is not None:
        brief_parts.append(f"PPI同比 {ppi['yoy']:+.1f}%")
        metrics.append(("中国PPI同比", f"{ppi['yoy']:+.1f}%"))

    # 中美利差（10Y 美债 - 10Y 中债，来自行情层 ust_yield）
    uy = market.get("ust_yield") or {}
    us10, cn10 = uy.get("us10y"), uy.get("cn10y")
    if us10 is not None and cn10 is not None:
        spread_bp = round((us10 - cn10) * 100, 1)
        brief_parts.append(f"中美10Y利差 {spread_bp:+.0f}bp")
        metrics.append(("中美10Y利差", f"{spread_bp:+.0f}bp"))

    # 美国宏观底色：FRED 月度优先，缺 key 时用 World Bank 年度兜底
    fred = macro.get("fred") or {}
    wb = (macro.get("worldbank") or {}).get("USA") or {}
    if fred:
        if fred.get("UNRATE", {}).get("value") is not None:
            metrics.append(("美国失业率", f"{fred['UNRATE']['value']:.1f}%"))
        if fred.get("DFF", {}).get("value") is not None:
            metrics.append(("联邦基金利率", f"{fred['DFF']['value']:.2f}%"))
        if fred.get("T10Y2Y", {}).get("value") is not None:
            metrics.append(("美债10Y-2Y利差", f"{fred['T10Y2Y']['value']:+.2f}%"))
    elif wb:
        cpi_us = wb.get("cpi_yoy") or {}
        unemp = wb.get("unemployment") or {}
        if cpi_us.get("value") is not None:
            metrics.append(("美国CPI(年)", f"{cpi_us['value']:.1f}%"))
        if unemp.get("value") is not None:
            metrics.append(("美国失业率", f"{unemp['value']:.1f}%"))

    brief = "；".join(brief_parts) if brief_parts else "宏观数据暂缺"
    return {"brief": brief, "metrics": metrics}


def main():
    pretty = "--pretty" in sys.argv
    report = collect()
    if pretty:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()
