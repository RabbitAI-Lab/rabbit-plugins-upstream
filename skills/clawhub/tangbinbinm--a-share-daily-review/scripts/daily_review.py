#!/usr/bin/env python3
"""A股每日复盘数据采集脚本(免API Key,akshare公开数据)。

输出:单个 JSON 对象到 stdout。各数据段独立容错,失败段记入 errors,不中断整体。
用法:python3 daily_review.py [--date YYYYMMDD]
"""
import argparse
import datetime as dt
import json
import sys

MAIN_INDICES = ["上证指数", "深证成指", "创业板指", "科创50", "北证50", "沪深300"]
TOP_N_BOARDS = 5
TOP_N_ZT = 8
TOP_N_LHB = 5
YI = 100_000_000  # 1亿


def _f(value, ndigits=2):
    """安全转 float;失败返回 None。"""
    try:
        return round(float(value), ndigits)
    except (TypeError, ValueError):
        return None


def latest_trade_date(ak, target=None):
    """返回 <= target 的最近交易日 (datetime.date)。失败则回退到今天/昨天。"""
    today = dt.date.today()
    target = target or today
    try:
        cal = ak.tool_trade_date_hist_sina()
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
            rows = call()
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
        df = ak.stock_market_activity_legu()
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
        df = ak.stock_board_industry_name_em()
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
        df = ak.stock_board_industry_summary_ths()
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
        df = ak.stock_zt_pool_em(date=date_str)
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
        df = ak.stock_lhb_detail_em(start_date=date_str, end_date=date_str)
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


def main():
    parser = argparse.ArgumentParser(description="A股每日复盘数据采集")
    parser.add_argument("--date", help="指定交易日 YYYYMMDD,默认最近交易日")
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

    result = {
        "date": trade_date.strftime("%Y-%m-%d"),
        "generated_at": dt.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "sections": sections,
        "errors": errors,
        "disclaimer": "本数据仅为公开市场信息整理,不构成投资建议。",
    }
    print(json.dumps(result, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
