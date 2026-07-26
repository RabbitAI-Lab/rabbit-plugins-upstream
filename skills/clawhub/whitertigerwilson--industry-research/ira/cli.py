"""
cli.py - 命令行统一入口

用法：
  python -m ira turnover <code> [days]
  python -m ira kline <code> [days]
  python -m ira financial <code>
  python -m ira valuation <code> [industry]
  python -m ira futures <commodity>
  python -m ira filter <commodity>
  python -m ira realtime <code>
"""

from __future__ import annotations
import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description="ira - 行业研究助手 CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("version", help="显示版本").set_defaults(func=lambda args: print("ira v1.3.1"))

    p_src = sub.add_parser("sources", help="诊断 K 线数据源可用性")
    p_src.add_argument("code", nargs="?", default="601899", help="股票代码（默认 601899）")

    p_to = sub.add_parser("turnover", help="换手率分析")
    p_to.add_argument("code")
    p_to.add_argument("days", nargs="?", type=int, default=30)

    p_kl = sub.add_parser("kline", help="K 线形态 + 均线")
    p_kl.add_argument("code")
    p_kl.add_argument("days", nargs="?", type=int, default=20)

    p_ti = sub.add_parser("technical", help="高级技术指标 MACD/RSI/BOLL/KDJ")
    p_ti.add_argument("code")
    p_ti.add_argument("days", nargs="?", type=int, default=60)

    p_fi = sub.add_parser("financial", help="财务摘要（PE/PB/市值）")
    p_fi.add_argument("code")

    p_vl = sub.add_parser("valuation", help="历史分位 + 三档评估")
    p_vl.add_argument("code")
    p_vl.add_argument("industry", nargs="?", default="")

    p_ft = sub.add_parser("futures", help="期货合约元信息")
    p_ft.add_argument("commodity")

    p_ftk = sub.add_parser("futures-kline", help="期货主力连续 (akshare)")
    p_ftk.add_argument("commodity")
    p_ftk.add_argument("days", nargs="?", type=int, default=60)

    p_at = sub.add_parser("anomaly", help="量价异动检测")
    p_at.add_argument("code")
    p_at.add_argument("days", nargs="?", type=int, default=120)

    p_ft2 = sub.add_parser("filter", help="按商品筛选 A 股")
    p_ft2.add_argument("commodity")

    p_ar = sub.add_parser("archive", help="历史研究案例库")
    sub_ar = p_ar.add_subparsers(dest="ar_cmd", required=True)
    sub_ar.add_parser("list", help="列出全部")
    p_arsearch = sub_ar.add_parser("search", help="按商品检索")
    p_arsearch.add_argument("commodity")
    p_arsearch.add_argument("--limit", type=int, default=10)
    p_aradd = sub_ar.add_parser("add", help="归档当前研究")
    p_aradd.add_argument("commodity")
    p_aradd.add_argument("--summary", required=True)
    p_aradd.add_argument("--findings", default="{}")
    p_aradd.add_argument("--tags", default="")

    p_rt = sub.add_parser("realtime", help="实时价格")
    p_rt.add_argument("code")

    p_glob = sub.add_parser("global", help="港股/美股按代码查询")
    p_glob.add_argument("code", help="5位数字=港股，字母=美股")
    p_glob.add_argument("--search", action="store_true", help="关键词搜索股票列表")

    p_bb = sub.add_parser("billboard", help="龙虎榜")
    sub_bb = p_bb.add_subparsers(dest="bb_cmd", required=True)
    p_bbstock = sub_bb.add_parser("stock", help="个股上榜统计")
    p_bbstock.add_argument("--period", default="近一月", choices=["近一月", "近三月", "近六月", "近一年"])
    p_bborg = sub_bb.add_parser("org", help="机构席位追踪")
    p_bborg.add_argument("--days", default="30", choices=["5", "10", "30", "60"])
    p_bbdetail = sub_bb.add_parser("detail", help="龙虎榜详情（日期区间）")
    p_bbdetail.add_argument("--start", default="20260601")
    p_bbdetail.add_argument("--end", default="20260629")

    p_ch = sub.add_parser("chain", help="三级联动（商品→个股→ETF）")
    p_ch.add_argument("commodity", help="商品中文名，如 铜 / 半导体 / 白酒")

    p_etf = sub.add_parser("etf", help="ETF 实时查询（拉取/查询）")
    sub_etf = p_etf.add_subparsers(dest="etf_cmd", required=True)
    p_etfrefresh = sub_etf.add_parser("refresh", help="拉取全市场 ETF 实时")
    p_etfget = sub_etf.add_parser("get", help="按代码查 ETF")
    p_etfget.add_argument("code", help="ETF 代码")
    p_etflist = sub_etf.add_parser("commodities", help="支持联动的商品列表")

    p_rep = sub.add_parser("report", help="生成 HTML 研报")
    p_rep.add_argument("commodity", nargs="?", help="商品中文名（空 = 全部今日归档）")

    args = parser.parse_args()

    if args.cmd == "version":
        args.func(args)
        return

    if args.cmd == "sources":
        from .sources import diagnose_sources
        r = diagnose_sources(args.code)
        print(f"\n=== {r['code']} K 线数据源诊断 ===")
        for it in r["results"]:
            status = "OK" if it["ok"] else "FAIL"
            rows = it.get("rows", 0)
            err = it.get("error", "")
            print(f"  {it['source']:<12} {status:<4}  rows={rows}  {err}")
        print()
        return

    if args.cmd == "turnover":
        from .turnover import get_turnover, print_report
        print_report(get_turnover(args.code, args.days))
        return

    if args.cmd == "kline":
        from .kline import analyze, print_report
        print_report(analyze(args.code, args.days))
        return

    if args.cmd == "technical":
        from .technical import analyze, print_report
        print_report(analyze(args.code, args.days))
        return

    if args.cmd == "financial":
        from .financial import get_financial, print_report
        print_report(get_financial(args.code))
        return

    if args.cmd == "valuation":
        from .financial import get_financial
        from .valuation import get_valuation, print_report
        fin = get_financial(args.code)
        print_report(get_valuation(args.code, args.industry), fin)
        return

    if args.cmd == "futures":
        from .constants import FUTURES_MAP
        c = args.commodity
        if c in FUTURES_MAP:
            info = FUTURES_MAP[c]
            print(f"\n{c} → {info['symbol']}.{info['exchange']}")
            print(f"  合约单位: {info['unit']}")
            print(f"  每手规模: {info['contract_size']} 单位")
        else:
            print(f"\n未找到 {c} 的期货元信息。可用关键字:")
            for k in FUTURES_MAP:
                print(f"  {k}")
        return

    if args.cmd == "futures-kline":
        from .futures import get_main_contract, print_report
        print_report(get_main_contract(args.commodity, args.days))
        return

    if args.cmd == "anomaly":
        from .anomaly import detect_volume_anomaly, print_report
        print_report(detect_volume_anomaly(args.code, args.days))
        return

    if args.cmd == "filter":
        from .stock_data import filter_stocks
        import pandas as pd
        df = filter_stocks(args.commodity)
        if df.empty:
            print(f"未在预定义池中找到 '{args.commodity}'。可尝试用 web_search 查询具体商品。")
        else:
            print(df.to_string(index=False))
        return

    if args.cmd == "archive":
        from .archive import archive_research, search_archive, print_search_result, list_archive
        import json
        if args.ar_cmd == "list":
            items = list_archive()
            if not items:
                print("📁 历史研究库为空")
            else:
                print(f"📁 共 {len(items)} 条归档：")
                for it in items:
                    print(f"  {it['name']}")
            return
        if args.ar_cmd == "search":
            results = search_archive(args.commodity, args.limit)
            print_search_result(results, args.commodity)
            return
        if args.ar_cmd == "add":
            try:
                findings = json.loads(args.findings)
            except Exception:
                findings = {}
            tags = [t.strip() for t in args.tags.split(",") if t.strip()]
            archive_research(
                commodity=args.commodity,
                summary=args.summary,
                findings=findings,
                tags=tags,
            )
            return

    if args.cmd == "realtime":
        from .stock_data import get_realtime
        rt = get_realtime(args.code)
        if rt:
            for k, v in rt.items():
                print(f"  {k}: {v}")
        else:
            print("实时数据获取失败")
        return

    if args.cmd == "global":
        from .global_stocks import get_global_realtime, print_global, search_hk, search_us
        if args.search:
            kw = args.code
            hk_results = search_hk(kw)
            us_results = search_us(kw)
            print(f"\n=== 关键词 '{kw}' 搜索结果 ===")
            if hk_results:
                print("港股:")
                for s in hk_results:
                    print(f"  {s['code']} - {s['name']}")
            if us_results:
                print("美股:")
                for s in us_results:
                    print(f"  {s['code']} - {s['name']}")
            if not hk_results and not us_results:
                print("  未找到")
            print()
        else:
            r = get_global_realtime(args.code)
            print_global(r)
        return

    if args.cmd == "billboard":
        from .billboard import (
            get_stock_billboard_statistic,
            get_institution_tracking,
            get_billboard_details,
            print_billboard,
        )
        if args.bb_cmd == "stock":
            r = get_stock_billboard_statistic(args.period)
            print_billboard(r, top=15)
        elif args.bb_cmd == "org":
            r = get_institution_tracking(args.days)
            print_billboard(r, top=15)
        elif args.bb_cmd == "detail":
            r = get_billboard_details(args.start, args.end)
            print_billboard(r, top=15)
        return

    if args.cmd == "chain":
        from .etf_chain import get_chain, print_chain
        print_chain(get_chain(args.commodity))
        return

    if args.cmd == "etf":
        from .etf_chain import refresh_etf_spot, get_etf_realtime, list_supported_commodities
        if args.etf_cmd == "refresh":
            r = refresh_etf_spot()
            print(f"\n✅ 拉取完成: {r.get('row_count')} 只 ETF")
            print(f"   缓存: {r.get('cache_path')}\n")
        elif args.etf_cmd == "get":
            r = get_etf_realtime(args.code)
            for k, v in r.items():
                print(f"  {k}: {v}")
        elif args.etf_cmd == "commodities":
            print(f"支持联动的商品 ({len(list_supported_commodities())}):")
            for c in list_supported_commodities():
                print(f"  {c}")
        return

    if args.cmd == "report":
        from .report import generate_report, generate_all_reports
        if not args.commodity:
            paths = generate_all_reports()
            print(f"\n 生成 {len(paths)} 份 HTML 研报:")
            for p in paths:
                print(f"   {p}")
        else:
            p = generate_report(args.commodity)
            if p:
                print(f"\n 研报: {p}")
                print(f"   {p.stat().st_size} bytes")
            else:
                print(f"\n 未找到 {args.commodity} 的归档")
        return


if __name__ == "__main__":
    main()
