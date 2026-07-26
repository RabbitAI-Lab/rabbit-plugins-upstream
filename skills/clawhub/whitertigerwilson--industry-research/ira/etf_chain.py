"""
etf_chain.py - 三级联动（商品 → 个股 → ETF）

策略：
1. 维护手配 commodity → etf 映射表（覆盖核心商品）
2. 个股复用 COMMODITY_STOCKS 常量
3. ETF 实时数据用 akshare.fund_etf_spot_em 拉，缓存到 JSON
4. CLI:
   - chain <commodity>: 商品 → 个股 → ETF 完整链路
   - etf <industry>: 列出某行业 ETF 实时
   - etf-refresh: 拉取最新 ETF 全量数据
"""

from __future__ import annotations
import json
from pathlib import Path
from typing import Optional
from datetime import datetime

try:
    import akshare as ak
    HAS_AKSHARE = True
except ImportError:
    HAS_AKSHARE = False


# 三级映射：商品 → 代表 ETF（手配高匹配度）
# 注：以下代码为常见 ETF 标的，可根据实际持仓调整
COMMODITY_TO_ETFS = {
    "铜": [
        {"code": "512400", "name": "有色金属 ETF", "logic": "覆盖铜/铝/铅锌"},
        {"code": "159697", "name": "矿业 ETF", "logic": "覆盖铜/黄金/铁矿"},
    ],
    "黄金": [
        {"code": "518880", "name": "黄金 ETF", "logic": "直接跟踪金价"},
        {"code": "518600", "name": "上海金 ETF", "logic": "黄金现货合约"},
    ],
    "铝": [
        {"code": "512400", "name": "有色金属 ETF", "logic": "覆盖铜/铝/铅锌"},
    ],
    "白银": [
        {"code": "518880", "name": "黄金 ETF", "logic": "白银弹性高于黄金"},
    ],
    "螺纹钢": [
        {"code": "510410", "name": "资源 ETF", "logic": "覆盖钢铁/有色/煤炭"},
    ],
    "铁矿石": [
        {"code": "510410", "name": "资源 ETF", "logic": "覆盖钢铁产业链"},
    ],
    "煤炭": [
        {"code": "515220", "name": "煤炭 ETF", "logic": "直接跟踪煤炭行业"},
    ],
    "焦煤": [
        {"code": "515220", "name": "煤炭 ETF", "logic": "焦煤与动力煤联动"},
    ],
    "原油": [
        {"code": "160723", "name": "嘉实原油", "logic": "QDII 原油基金"},
        {"code": "501018", "name": "南方原油", "logic": "QDII 原油基金"},
    ],
    "豆粕": [
        {"code": "159985", "name": "豆粕 ETF", "logic": "直接跟踪大商所豆粕期货"},
    ],
    "玉米": [
        {"code": "159825", "name": "农业 ETF", "logic": "覆盖粮食/畜牧"},
    ],
    "棉花": [
        {"code": "159825", "name": "农业 ETF", "logic": "覆盖农产品"},
    ],
    "半导体": [
        {"code": "512480", "name": "国联安半导体 ETF", "logic": "直接跟踪半导体指数"},
        {"code": "159995", "name": "华夏国证半导体芯片 ETF", "logic": "覆盖芯片设计/制造/封测"},
    ],
    "军工": [
        {"code": "512660", "name": "军工 ETF", "logic": "直接跟踪中证军工指数"},
    ],
    "新能源车": [
        {"code": "515030", "name": "新能源车 ETF", "logic": "覆盖整车/电池/电机电控"},
    ],
    "光伏": [
        {"code": "515790", "name": "光伏 ETF", "logic": "覆盖硅料/电池/组件"},
    ],
    "储能": [
        {"code": "159885", "name": "储能电池 ETF", "logic": "覆盖储能产业链"},
    ],
    "白酒": [
        {"code": "512690", "name": "酒 ETF", "logic": "覆盖白酒/啤酒/葡萄酒"},
    ],
    "医药": [
        {"code": "512010", "name": "医药 ETF", "logic": "覆盖医药/医疗器械"},
    ],
    "银行": [
        {"code": "512800", "name": "银行 ETF", "logic": "覆盖国有大行+股份行"},
    ],
    "券商": [
        {"code": "512000", "name": "券商 ETF", "logic": "覆盖证券行业"},
    ],
    "地产": [
        {"code": "512200", "name": "房地产 ETF", "logic": "覆盖房地产开发/物业"},
    ],
    "家电": [
        {"code": "159996", "name": "家电 ETF", "logic": "覆盖白电/小家电"},
    ],
    "钢铁": [
        {"code": "510410", "name": "资源 ETF", "logic": "覆盖钢铁产业链"},
    ],
}


# ETF 实时数据缓存
ETF_CACHE = Path.home() / ".openclaw" / "workspace" / "ira-new" / "industry-research" / "data" / "etf_spot.json"


def _ensure_data_dir():
    ETF_CACHE.parent.mkdir(parents=True, exist_ok=True)


def refresh_etf_spot() -> dict:
    """拉取全市场 ETF 实时数据，缓存到 JSON"""
    if not HAS_AKSHARE:
        return {"error": "akshare 未安装"}
    _ensure_data_dir()

    try:
        df = ak.fund_etf_spot_em()
        if df is None or df.empty:
            return {"error": "ETF 实时数据为空"}
        # 选择关键字段
        cols_to_keep = ["代码", "名称", "最新价", "涨跌幅", "涨跌额", "成交量", "成交额"]
        available = [c for c in cols_to_keep if c in df.columns]
        df_simple = df[available].copy()
        # 缓存
        ETF_CACHE.write_text(
            df_simple.to_json(orient="records", force_ascii=False),
            encoding="utf-8",
        )
        return {
            "row_count": len(df_simple),
            "fields": available,
            "cache_path": str(ETF_CACHE),
            "source": "eastmoney-fund",
            "fetched_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        }
    except Exception as e:
        return {"error": f"ETF 实时拉取失败: {e}"}


def _load_cache() -> list[dict]:
    if not ETF_CACHE.exists():
        return []
    try:
        return json.loads(ETF_CACHE.read_text(encoding="utf-8"))
    except Exception:
        return []


def get_etf_realtime(code: str) -> dict:
    """按代码查 ETF 实时（从缓存或实时拉取）"""
    cache = _load_cache()
    if not cache:
        # 缓存为空，先拉一次
        refresh_etf_spot()
        cache = _load_cache()
    for etf in cache:
        if str(etf.get("代码", "")) == str(code):
            return etf
    return {"error": f"未找到 ETF {code}"}


def get_chain(commodity: str) -> dict:
    """
    商品 → 个股 → ETF 完整链路。
    """
    from .constants import find_commodity

    # 个股层
    stocks = find_commodity(commodity) or []
    # ETF 层
    etfs = COMMODITY_TO_ETFS.get(commodity, [])

    # 拉取 ETF 实时
    etf_realtime = []
    for etf in etfs:
        rt = get_etf_realtime(etf["code"])
        if rt and not rt.get("error"):
            etf_realtime.append({**etf, **rt})
        else:
            etf_realtime.append({**etf, "latest_price": "—", "change_pct": "—"})

    return {
        "commodity": commodity,
        "stocks": [
            {
                "code": s[1] if isinstance(s, tuple) else s.get("code", "?"),
                "name": s[0] if isinstance(s, tuple) else s.get("name", "?"),
                "weight": (s[2] if isinstance(s, tuple) and len(s) > 2 else "—"),
            }
            for s in stocks[:5]
        ],
        "etfs": etf_realtime,
        "source": "akshare-constants-manual",
    }


def print_chain(result: dict):
    print(f"\n{'=' * 60}")
    print(f"  {result.get('commodity')} 完整链路")
    print(f"{'=' * 60}")

    # 个股
    stocks = result.get("stocks", [])
    if stocks:
        print(f"\n  --- 个股（{len(stocks)} 只）---")
        for s in stocks:
            print(f"  {s['code']} {s['name']} 主营: {s['weight']}")
    else:
        print("\n  --- 个股：无 ---")

    # ETF
    etfs = result.get("etfs", [])
    if etfs:
        print(f"\n  --- ETF（{len(etfs)} 只）---")
        for e in etfs:
            lp = e.get("最新价") or e.get("latest_price") or "—"
            ch = e.get("涨跌幅") or e.get("change_pct") or "—"
            print(f"  {e['code']} {e['name']} 最新 {lp} 涨跌 {ch}%")
            print(f"      匹配逻辑: {e.get('logic', '—')}")
    else:
        print("\n  --- ETF：无 ---")

    print(f"{'=' * 60}\n")


def list_supported_commodities() -> list[str]:
    return list(COMMODITY_TO_ETFS.keys())