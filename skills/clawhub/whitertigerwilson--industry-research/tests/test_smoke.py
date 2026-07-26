"""
tests/test_smoke.py - 端到端冒烟测试（v1.1.0 完整版）

跑：cd industry-research && python tests/test_smoke.py
"""

import sys
from pathlib import Path

# 让 ira 包可被导入
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from ira import stock_data, turnover, kline, financial, valuation, technical, anomaly, futures, archive, etf_chain


def test_filter_copper():
    df = stock_data.filter_stocks("铜")
    assert not df.empty, "铜 股票池空"
    assert "紫金矿业" in df["公司名称"].values
    print("✅ test_filter_copper")


def test_report_copper():
    from ira.report import generate_report
    p = generate_report("铜")
    assert p is not None, "铜 研报生成失败"
    assert p.stat().st_size > 2000, "报告太小"
    print(f"✅ test_report_copper ({p.stat().st_size} bytes)")


def test_etf_chain_copper():
    chain = etf_chain.get_chain("铜")
    assert len(chain["stocks"]) > 0, "铜 个股为空"
    assert len(chain["etfs"]) > 0, "铜 ETF 为空"
    print(f"✅ test_etf_chain_copper ({len(chain['stocks'])}只股, {len(chain['etfs'])}只ETF)")


def test_turnover_zijin():
    r = turnover.get_turnover("601899", 5)
    assert r["code"] == "601899"
    assert r["total"] > 0
    print(f"✅ test_turnover_zijin (5日累计 {r['total']}%)")


def test_kline_zijin():
    a = kline.analyze("601899", 20)
    assert a["klines_count"] > 0
    print(f"✅ test_kline_zijin (排列: {a['arrangement']}, 信号: {a['pattern_count']})")


def test_technical_zijin():
    t = technical.analyze("601899", 60)
    assert t["code"] == "601899"
    assert t["macd"].get("latest")
    assert t["rsi"].get("latest") is not None
    print(f"✅ test_technical_zijin (MACD 多空: {t['macd']['latest'][0]:.2f}, RSI: {t['rsi']['latest']})")


def test_financial_zijin():
    f = financial.get_financial("601899")
    assert f.get("price") is not None, "未取到价格"
    assert f.get("pe_ttm") is not None, "未取到 PE"
    assert f.get("market_cap_total_yi") is not None, "未取到市值"
    print(f"✅ test_financial_zijin (PE {f['pe_ttm']}, 市值 {f['market_cap_total_yi']}亿)")


def test_valuation_maotai():
    fin = financial.get_financial("600519")
    val = valuation.get_valuation("600519", "白酒")
    assert fin.get("price") is not None
    print(f"✅ test_valuation_maotai (PE {fin.get('pe_ttm')}, 历史分位 {val.get('price_history', {}).get('price_percentile')})")


def test_anomaly_zijin():
    r = anomaly.detect_volume_anomaly("601899", 60)
    assert r["code"] == "601899"
    print(f"✅ test_anomaly_zijin (异动信号: {r['anomaly_count']} 个)")


def test_futures_copper():
    r = futures.get_main_contract("铜", 30)
    if r.get("error"):
        print(f"⚠️ test_futures_copper SKIP ({r['error']})")
        return
    assert r["latest_close"] is not None
    print(f"✅ test_futures_copper (沪铜 {r['symbol']} {r['latest_close']} {r['latest_date']})")


def test_archive():
    results = archive.search_archive("铜")
    print(f"✅ test_archive (历史研究: {len(results)} 条)")


def main():
    print("=" * 55)
    print("  ira v1.1.0 端到端冒烟测试")
    print("=" * 55)
    tests = [
        test_filter_copper,
        test_etf_chain_copper,
        test_report_copper,
        test_turnover_zijin,
        test_kline_zijin,
        test_technical_zijin,
        test_financial_zijin,
        test_valuation_maotai,
        test_anomaly_zijin,
        test_futures_copper,
        test_archive,
    ]
    passed = 0
    for t in tests:
        try:
            t()
            passed += 1
        except AssertionError as e:
            print(f"❌ {t.__name__}: {e}")
        except Exception as e:
            print(f"⚠️ {t.__name__}: {type(e).__name__}: {e}")
    print("=" * 55)
    print(f"  {passed}/{len(tests)} 通过")
    print("=" * 55)
    return 0 if passed == len(tests) else 1


if __name__ == "__main__":
    sys.exit(main())
