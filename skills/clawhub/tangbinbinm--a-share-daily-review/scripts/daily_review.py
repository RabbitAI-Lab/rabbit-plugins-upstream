#!/usr/bin/env python3
"""A股每日复盘数据采集脚本(免API Key,akshare公开数据)。

输出:单个 JSON 对象到 stdout。各数据段独立容错,失败段记入 errors,不中断整体。
用法:python3 daily_review.py [--date YYYYMMDD] [--format json|plain]
"""
import argparse
import concurrent.futures
import datetime as dt
import json
import signal
import sys
import threading

MAIN_INDICES = ["上证指数", "深证成指", "创业板指", "科创50", "北证50", "沪深300"]
# 港股: (代码, 显示名, Sina兜底匹配关键词)
HK_SPEC = [
    ("HSI",    "恒生指数",       "恒生指数"),
    ("HSCEI",  "国企指数",       "恒生中国企业指数"),
    ("HSCCI",  "红筹指数",       "恒生香港中资企业指数"),
    ("HSTECH", "恒生科技指数",    "恒生科技指数"),
]
US_INDICES = [".DJI", ".IXIC", ".INX"]       # 道琼斯 / 纳斯达克 / 标普500
TOP_N_BOARDS = 5
TOP_N_CONCEPTS = 5
TOP_N_ZT = 8
TOP_N_LHB = 5
YI = 100_000_000  # 1亿


def _f(value, ndigits=2):
    """安全转 float;失败返回 None。"""
    try:
        return round(float(value), ndigits)
    except (TypeError, ValueError):
        return None


def _with_timeout(fn, seconds=8):
    """执行 fn 并限制等待时间,避免外部行情接口卡住整个进程。"""
    if threading.current_thread() is threading.main_thread() and hasattr(signal, "setitimer"):
        def _raise_timeout(signum, frame):
            raise TimeoutError(f"operation timed out after {seconds}s")

        previous = signal.signal(signal.SIGALRM, _raise_timeout)
        signal.setitimer(signal.ITIMER_REAL, seconds)
        try:
            return fn()
        finally:
            signal.setitimer(signal.ITIMER_REAL, 0)
            signal.signal(signal.SIGALRM, previous)

    executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
    future = executor.submit(fn)
    try:
        return future.result(timeout=seconds)
    finally:
        executor.shutdown(wait=False, cancel_futures=True)


def latest_trade_date(ak, target=None):
    """返回 <= target 的最近交易日 (datetime.date)。失败则回退到今天/昨天。"""
    today = dt.date.today()
    target = target or today
    try:
        cal = _with_timeout(lambda: ak.tool_trade_date_hist_sina(), seconds=8)
        dates = [d if isinstance(d, dt.date) else dt.datetime.strptime(str(d), "%Y-%m-%d").date()
                 for d in cal["trade_date"]]
        past = [d for d in dates if d <= target]
        if past:
            return max(past)
    except Exception:
        pass
    # 回退:周末往前挪
    d = target
    while d.weekday() >= 5:
        d -= dt.timedelta(days=1)
    return d


def sec_indices(ak, out, errors):
    rows = None
    for call in (lambda: ak.stock_zh_index_spot_em(symbol="沪深重要指数"),
                 lambda: ak.stock_zh_index_spot_em(),
                 lambda: ak.stock_zh_index_spot_sina()):
        try:
            rows = _with_timeout(call, seconds=8)
            if rows is not None and len(rows):
                break
        except Exception:
            continue
    if rows is None or not len(rows):
        errors.append("indices: 指数行情接口不可用")
        return
    name_col = "名称" if "名称" in rows.columns else rows.columns[1]
    close_col = "最新价" if "最新价" in rows.columns else "最新价"
    pct_col = "涨跌幅" if "涨跌幅" in rows.columns else "涨跌幅"
    picked = []
    for want in MAIN_INDICES:
        hit = rows[rows[name_col] == want]
        if len(hit):
            r = hit.iloc[0]
            picked.append({"name": want, "close": _f(r.get(close_col)), "pct": _f(r.get(pct_col))})
    if picked:
        out["indices"] = picked
    else:
        errors.append("indices: 未匹配到主要指数")


def sec_market_activity(ak, out, errors):
    try:
        df = _with_timeout(lambda: ak.stock_market_activity_legu(), seconds=8)
        # 返回两列 item/value
        data = {}
        for _, r in df.iterrows():
            key = str(r.iloc[0]).strip()
            data[key] = _f(r.iloc[1]) if _f(r.iloc[1]) is not None else str(r.iloc[1])
        out["market_activity"] = data
    except Exception as e:
        errors.append(f"market_activity: {type(e).__name__}")


def sec_boards(ak, out, errors):
    # 主源:东财行业板块;兜底:同花顺行业一览
    try:
        df = _with_timeout(lambda: ak.stock_board_industry_name_em(), seconds=8)
        df = df.sort_values("涨跌幅", ascending=False)
        def rows(sub):
            return [{"name": str(r["板块名称"]), "pct": _f(r["涨跌幅"]),
                     "leader": str(r.get("领涨股票", ""))} for _, r in sub.iterrows()]
        out["boards_top"] = rows(df.head(TOP_N_BOARDS))
        out["boards_bottom"] = rows(df.tail(TOP_N_BOARDS).iloc[::-1])
        return
    except Exception as e:
        em_err = type(e).__name__
    try:
        df = _with_timeout(lambda: ak.stock_board_industry_summary_ths(), seconds=8)
        df = df.sort_values("涨跌幅", ascending=False)
        def rows_ths(sub):
            return [{"name": str(r["板块"]), "pct": _f(r["涨跌幅"]), "leader": ""}
                    for _, r in sub.iterrows()]
        out["boards_top"] = rows_ths(df.head(TOP_N_BOARDS))
        out["boards_bottom"] = rows_ths(df.tail(TOP_N_BOARDS).iloc[::-1])
    except Exception as e:
        errors.append(f"boards: EM={em_err}, THS={type(e).__name__}")


def sec_zt_pool(ak, out, errors, date_str):
    try:
        df = _with_timeout(lambda: ak.stock_zt_pool_em(date=date_str), seconds=8)
        if df is None or not len(df):
            out["zt_pool"] = {"count": 0, "max_streak": 0, "top": []}
            return
        streak_col = "连板数" if "连板数" in df.columns else None
        top = df.sort_values(streak_col, ascending=False).head(TOP_N_ZT) if streak_col else df.head(TOP_N_ZT)
        out["zt_pool"] = {
            "count": int(len(df)),
            "max_streak": int(df[streak_col].max()) if streak_col else None,
            "top": [{"name": str(r.get("名称")),
                     "streak": int(r.get("连板数", 0)) if streak_col else None,
                     "industry": str(r.get("所属行业", ""))} for _, r in top.iterrows()],
        }
    except Exception as e:
        errors.append(f"zt_pool: {type(e).__name__}")


def sec_lhb(ak, out, errors, date_str):
    try:
        df = _with_timeout(
            lambda: ak.stock_lhb_detail_em(start_date=date_str, end_date=date_str),
            seconds=8,
        )
        if df is None or not len(df):
            out["lhb"] = []
            return
        net_col = "龙虎榜净买额" if "龙虎榜净买额" in df.columns else None
        if net_col:
            df = df.sort_values(net_col, ascending=False)
        rows = []
        for _, r in df.head(TOP_N_LHB).iterrows():
            net = _f(r.get(net_col))
            rows.append({"name": str(r.get("名称")), "pct": _f(r.get("涨跌幅")),
                         "net_buy_yi": round(net / YI, 2) if net is not None else None})
        out["lhb"] = rows
    except Exception as e:
        errors.append(f"lhb: {type(e).__name__}")


def sec_global_indices(ak, out, errors):
    """全球主要指数 (优先东财 index_global_spot_em,8s超时;兜底新浪港股)。"""
    US_MAP = {"DJIA": "道琼斯工业", "NDX": "纳斯达克", "SPX": "标普500"}
    ASIA_MAP = {"N225": "日经225", "KOSPI": "韩国KOSPI", "TWII": "台湾加权"}
    EU_MAP = {"FTSE": "英国富时100", "GDAXI": "德国DAX", "FCHI": "法国CAC40"}

    def _pick(df, code_map):
        picked = []
        for code, name in code_map.items():
            hit = df[df["代码"] == code]
            if len(hit):
                r = hit.iloc[0]
                picked.append({"name": name, "close": _f(r["最新价"]), "pct": _f(r["涨跌幅"])})
        return picked

    # 主源:东财全球指数现货 (8s 超时,防止本机代理阻塞)
    try:
        df = _with_timeout(lambda: ak.index_global_spot_em(), seconds=8)
        us = _pick(df, US_MAP)
        hk = _pick(df, {code: name for code, name, _ in HK_SPEC})
        asia = _pick(df, ASIA_MAP)
        eu = _pick(df, EU_MAP)
        if us:
            out["us_indices"] = us
        if hk:
            out["hk_indices"] = hk
        if asia:
            out["asia_indices"] = asia
        if eu:
            out["eu_indices"] = eu
        if us or hk or asia or eu:
            return  # 主源成功
    except Exception as e:
        em_err = f"{type(e).__name__}: {e}" if str(e) else type(e).__name__
    else:
        em_err = "no_data"

    # 兜底:新浪港股
    try:
        df = _with_timeout(lambda: ak.stock_hk_index_spot_sina(), seconds=8)
        name_col = "名称" if "名称" in df.columns else df.columns[1]
        picked = []
        for code, display_name, sina_keyword in HK_SPEC:
            hit = df[df[name_col].str.contains(sina_keyword, na=False)]
            if len(hit):
                r = hit.iloc[0]
                picked.append({"name": display_name, "close": _f(r.get("最新价")), "pct": _f(r.get("涨跌幅"))})
        if picked:
            out["hk_indices"] = picked
        else:
            errors.append(f"hk_indices: 新浪源未匹配到港股指数")
    except Exception as e:
        errors.append(f"global_indices: EM={em_err}, SINA_HK={type(e).__name__}")


def sec_north_flow(ak, out, errors):
    """北向资金当日流向 (东财源,免费)。"""
    try:
        df = _with_timeout(lambda: ak.stock_hsgt_fund_flow_summary_em(), seconds=8)
        north = df[df["资金方向"] == "北向"]
        if len(north):
            rows = []
            for _, r in north.iterrows():
                rows.append({
                    "market": str(r.get("板块", "")),
                    "net_buy_yi": _f(r.get("成交净买额")),
                    "inflow_yi": _f(r.get("资金净流入")),
                })
            out["north_flow"] = rows
        else:
            errors.append("north_flow: 未解析到北向数据")
    except Exception as e:
        errors.append(f"north_flow: {type(e).__name__}")


def sec_concept_boards(ak, out, errors):
    """热门概念板块 TOP5 (东财源,免费;兜底同花顺)。"""
    try:
        df = _with_timeout(lambda: ak.stock_board_concept_spot_em(), seconds=8)
        df = df.sort_values("涨跌幅", ascending=False)
        out["concepts_top"] = [
            {"name": str(r["板块名称"]), "pct": _f(r["涨跌幅"])}
            for _, r in df.head(TOP_N_CONCEPTS).iterrows()
        ]
        out["concepts_bottom"] = [
            {"name": str(r["板块名称"]), "pct": _f(r["涨跌幅"])}
            for _, r in df.tail(TOP_N_CONCEPTS).iloc[::-1].iterrows()
        ]
        return
    except Exception as e:
        em_err = type(e).__name__
    # 兜底:同花顺概念
    try:
        df = _with_timeout(lambda: ak.stock_board_concept_summary_ths(), seconds=8)
        df = df.sort_values("涨跌幅", ascending=False)
        out["concepts_top"] = [
            {"name": str(r["概念"]), "pct": _f(r["涨跌幅"])}
            for _, r in df.head(TOP_N_CONCEPTS).iterrows()
        ]
        out["concepts_bottom"] = [
            {"name": str(r["概念"]), "pct": _f(r["涨跌幅"])}
            for _, r in df.tail(TOP_N_CONCEPTS).iloc[::-1].iterrows()
        ]
    except Exception as e:
        errors.append(f"concept_boards: EM={em_err}, THS={type(e).__name__}")


def _signed_pct(value):
    """格式化带正负号的百分比,缺失值返回 N/A。"""
    number = _f(value)
    if number is None:
        return "N/A"
    return f"{number:+.2f}%"


def build_insights(sections):
    """从已采集的 sections 生成确定性摘要、异动提醒和数据质量概览。"""
    available = [
        name for name, value in sections.items()
        if value not in (None, [], {})
    ]
    known_sections = [
        "indices", "market_activity", "boards_top", "boards_bottom",
        "concepts_top", "concepts_bottom", "zt_pool", "lhb",
        "hk_indices", "us_indices", "asia_indices", "eu_indices", "north_flow",
    ]
    missing = [name for name in known_sections if name not in sections]
    summary = []
    alerts = []

    for row in sections.get("indices", []):
        name = str(row.get("name", "指数"))
        pct = _f(row.get("pct"))
        if pct is not None:
            direction = "上涨" if pct > 0 else "下跌" if pct < 0 else "持平"
            summary.append(f"{name}{direction} {abs(pct):.2f}%")

    for section_name in ("boards_top", "boards_bottom", "concepts_top", "concepts_bottom"):
        for row in sections.get(section_name, []):
            pct = _f(row.get("pct"))
            if pct is not None and abs(pct) >= 5:
                alerts.append({
                    "type": "board_move",
                    "section": section_name,
                    "name": str(row.get("name", "未知板块")),
                    "pct": pct,
                    "direction": "up" if pct > 0 else "down",
                })

    zt_pool = sections.get("zt_pool") or {}
    max_streak = _f(zt_pool.get("max_streak"), 0)
    if max_streak is not None and max_streak >= 5:
        alerts.append({
            "type": "streak",
            "max_streak": int(max_streak),
            "count": int(_f(zt_pool.get("count"), 0) or 0),
        })

    activity = sections.get("market_activity") or {}
    for key, value in activity.items():
        if "上涨" in str(key) and "家" in str(key):
            summary.append(f"{key}: {value}")
            break

    if not summary:
        summary.append("主要数据段暂无可生成的摘要")

    return {
        "summary": summary[:8],
        "alerts": alerts[:20],
        "quality": {
            "available_sections": len(available),
            "missing_sections": missing,
            "error_count": 0,
        },
    }


def render_plain_text(result):
    """把 JSON 结果渲染为可复制的事实摘要文本。"""
    lines = [f"全球市场日报 · {result.get('date', '未知日期')}"]
    insights = result.get("insights") or {}
    for item in insights.get("summary", []):
        lines.append(f"- {item}")

    indices = (result.get("sections") or {}).get("indices", [])
    if indices:
        lines.append("\n指数:")
        for row in indices:
            lines.append(
                f"- {row.get('name', '未知指数')}: "
                f"{row.get('close', 'N/A')} ({_signed_pct(row.get('pct'))})"
            )

    alerts = insights.get("alerts", [])
    if alerts:
        lines.append("\n异动提醒:")
        for alert in alerts:
            if alert.get("type") == "streak":
                lines.append(f"- 涨停最高连板 {alert.get('max_streak')}，涨停 {alert.get('count')} 家")
            else:
                lines.append(f"- {alert.get('name')}: {_signed_pct(alert.get('pct'))}")

    errors = result.get("errors") or []
    if errors:
        lines.append("\n数据缺失:")
        lines.extend(f"- {error}" for error in errors)
    lines.append(f"\n{result.get('disclaimer', '')}")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="A股每日复盘数据采集")
    parser.add_argument("--date", help="指定交易日 YYYYMMDD,默认最近交易日")
    parser.add_argument("--format", choices=["json", "plain"], default="json",
                        help="输出格式,默认 json; plain 用于复制转发")
    args = parser.parse_args()

    try:
        import akshare as ak
    except ImportError:
        print(json.dumps({"fatal": "缺少依赖:请先执行 pip install akshare pandas"},
                         ensure_ascii=False))
        sys.exit(1)

    target = None
    if args.date:
        try:
            target = dt.datetime.strptime(args.date, "%Y%m%d").date()
        except ValueError:
            print(json.dumps({"fatal": "--date 格式应为 YYYYMMDD"}, ensure_ascii=False))
            sys.exit(1)

    trade_date = latest_trade_date(ak, target)
    date_str = trade_date.strftime("%Y%m%d")

    sections, errors = {}, []
    sec_indices(ak, sections, errors)
    sec_market_activity(ak, sections, errors)
    sec_boards(ak, sections, errors)
    sec_zt_pool(ak, sections, errors, date_str)
    sec_lhb(ak, sections, errors, date_str)
    sec_global_indices(ak, sections, errors)
    sec_north_flow(ak, sections, errors)
    sec_concept_boards(ak, sections, errors)

    result = {
        "date": trade_date.strftime("%Y-%m-%d"),
        "generated_at": dt.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "sections": sections,
        "errors": errors,
        "disclaimer": "本数据仅为公开市场信息整理,不构成投资建议。",
    }
    result["insights"] = build_insights(sections)
    result["insights"]["quality"]["error_count"] = len(errors)
    if args.format == "plain":
        print(render_plain_text(result))
    else:
        print(json.dumps(result, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
