#!/usr/bin/env python3
"""
A股/港股公司数据采集脚本 — AKShare 主源 + 独立降级链（Codex 环境）。

用法:
  python3 scripts/collect_data.py <股票代码>            # 全量采集 → /tmp/{code}_data.json
  python3 scripts/collect_data.py --quotes <代码,代码>    # 批量行情 → stdout JSON
  python3 scripts/collect_data.py --finances <代码,代码>  # 批量财务比率 → stdout JSON

降级链（每项独立）：
  【A股】
    三表: AKShare stock_*_by_report_em → 新浪 HTTP → WebSearch
    财务指标: AKShare stock_financial_abstract → 东财 datacenter HTTP → WebSearch
    行情: 腾讯 qt.gtimg.cn → WebSearch
    F10/概况: 东财 emweb HTTP → WebSearch
    研报: AKShare stock_research_report_em → 东财 reportapi → WebSearch
    板块: 百度 API → WebSearch
    一致预期: 同花顺 HTTP → WebSearch

  【港股】
    三表: AKShare stock_financial_hk_report_em → yfinance(容错) → 东财 emweb HTTP → WebSearch
    财务指标: AKShare stock_financial_hk_analysis_indicator_em → yfinance(容错) → 东财 emweb HTTP → WebSearch
    行情: 腾讯 qt.gtimg.cn → yfinance(容错) → WebSearch
    概况/股东: 东财 emweb HTTP → WebSearch
    分红: 东财 emweb HTTP → WebSearch
    板块: WebSearch 兜底

  所有路径最终兜底: WebSearch（不在本脚本内，由 AI 在分析阶段按需触发）
"""
import sys, json, os, time, warnings
import pandas as pd
import requests
import urllib.request

warnings.filterwarnings("ignore")
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"

# ── 可选依赖探测 ──
try:
    import akshare as ak
    _AK = True
except ImportError:
    _AK = False

try:
    import yfinance as yf
    _YF = True
except ImportError:
    _YF = False

# ── 本地工具函数 ──

def _sh_pref(code):
    """A股 SH/SZ 前缀（AKShare 三表 API 需要）。"""
    if code.startswith(("6", "9")): return f"SH{code}"
    return f"SZ{code}"

def _prefix(code):
    """A股 sh/sz/bj 小写前缀（腾讯行情需要）。"""
    if code.startswith(("6", "9")): return "sh"
    if code.startswith(("8", "4")): return "bj"
    return "sz"

def _f(v):
    """安全转 float，百分比自动处理。"""
    if v in (None, "", "--", "-"): return None
    try:
        s = str(v).replace(",", "").strip()
    except:
        return None
    return float(s[:-1]) / 100 if s.endswith("%") else float(s)

def _round_or_none(v):
    if v is None: return None
    try: return float(v)
    except: return None

def http_get(url, params=None, headers=None, timeout=15, retries=2, want="json"):
    """通用 HTTP + 指数退避。"""
    h = {"User-Agent": UA}
    if headers: h.update(headers)
    for attempt in range(retries + 1):
        try:
            r = requests.get(url, params=params, headers=h, timeout=timeout)
            if want == "raw": return r
            return r.json()
        except Exception:
            if attempt == retries: raise
            time.sleep(1.0 * (2 ** attempt) + 0.3)

def _get_val_from(fa, label, period):
    m = fa[fa["指标"] == label]
    if m.empty or period not in fa.columns: return None
    return m.iloc[0][period]

# ── 参数解析 ──
if len(sys.argv) < 2:
    print("用法: python3 scripts/collect_data.py <5位港股或6位A股代码>")
    sys.exit(1)

QUOTES_MODE = sys.argv[1] == "--quotes"
FINANCES_MODE = sys.argv[1] == "--finances"
BATCH_MODE = QUOTES_MODE or FINANCES_MODE

if BATCH_MODE:
    if len(sys.argv) < 3:
        print(f"用法: python3 scripts/collect_data.py {'--quotes' if QUOTES_MODE else '--finances'} <代码,代码,...>")
        sys.exit(1)
    QUOTE_CODES = [c.strip() for c in sys.argv[2].split(",") if c.strip().isdigit()]
    CODE = QUOTE_CODES[0]
else:
    CODE = sys.argv[1]
    if not ((len(CODE) in (5, 6)) and CODE.isdigit()):
        print(f"错误：股票代码必须是 5 位港股或 6 位 A 股代码，当前输入：{CODE}")
        sys.exit(1)

IS_HK = len(CODE) == 5 and CODE.isdigit()
result = {}

# ════════════════════════════════════════════════════════════════
#  模块 1 — 三表
# ════════════════════════════════════════════════════════════════

# ── 1a. A股三表：AKShare ──
def triple_akshare_a(code):
    """AKShare A股三表（datacenter.eastmoney.com，实测可用）。"""
    if not _AK: raise RuntimeError("AKShare 不可用")
    sh = _sh_pref(code)
    out = {"lrb": [], "fzb": [], "llb": []}
    for fn, key, name in [
        (ak.stock_profit_sheet_by_report_em, "lrb", "利润表"),
        (ak.stock_balance_sheet_by_report_em, "fzb", "资产负债表"),
        (ak.stock_cash_flow_sheet_by_report_em, "llb", "现金流量表"),
    ]:
        try:
            df = fn(symbol=sh)
            if not df.empty:
                if "REPORT_TYPE" in df.columns:
                    df = df[df["REPORT_TYPE"] == "年报"]
                out[key] = df.head(8).to_dict(orient="records")
        except Exception:
            pass
    out["_数据源"] = "AKShare A股三表（东财 datacenter）"
    return out

# ── 1b. 港股三表：AKShare ──
def triple_akshare_hk(code):
    """AKShare 港股三表（emweb.securities.eastmoney.com，实测可用）。"""
    if not _AK: raise RuntimeError("AKShare 不可用")
    out = {"lrb": [], "fzb": [], "llb": []}
    mapping = [
        ("利润表", "lrb"),
        ("资产负债表", "fzb"),
        ("现金流量表", "llb"),
    ]
    for symbol, key in mapping:
        try:
            df = ak.stock_financial_hk_report_em(stock=code, symbol=symbol, indicator="年度")
            if df.empty:
                continue
            # Pivot: 长格式（STD_ITEM_NAME + AMOUNT × REPORT_DATE） → 宽格式（报告期 × 科目）
            pv = df.pivot_table(
                index="REPORT_DATE", columns="STD_ITEM_NAME",
                values="AMOUNT", aggfunc="first"
            ).sort_index(ascending=False)
            # 取前 8 期
            pv = pv.head(8)
            records = []
            for idx, row in pv.iterrows():
                rec = {"报告期": str(idx)[:10]}
                for col in pv.columns:
                    rec[col] = row[col] if pd.notna(row[col]) else None
                records.append(rec)
            out[key] = records
        except Exception:
            pass
    out["_数据源"] = "AKShare 港股三表（东财 emweb）"
    return out

# ── 1c. yfinance 三表（通用兜底，在此环境大概率被限速）──
def triple_yfinance(code):
    """yfinance 三表。Yahoo 在此环境可能被限速/封连接，只做容错尝试。"""
    if not _YF: raise RuntimeError("yfinance 不可用")
    ticker_str = f"{code}.HK" if IS_HK else code
    try:
        tk = yf.Ticker(ticker_str)
        # 短超时，快速失败
        inc = tk.income_stmt
        bs = tk.balance_sheet
        cf = tk.cashflow
    except Exception as e:
        raise RuntimeError(f"yfinance 连接失败: {str(e)[:60]}")
    out = {"lrb": [], "fzb": [], "llb": [], "_数据源": "yfinance"}
    if inc is not None and not inc.empty:
        out["lrb"] = [{"报告期": str(c)[:10], **{k: v for k, v in inc[c].to_dict().items() if pd.notna(v)}}
                      for c in inc.columns[:8]]
    if bs is not None and not bs.empty:
        out["fzb"] = [{"报告期": str(c)[:10], **{k: v for k, v in bs[c].to_dict().items() if pd.notna(v)}}
                      for c in bs.columns[:8]]
    if cf is not None and not cf.empty:
        out["llb"] = [{"报告期": str(c)[:10], **{k: v for k, v in cf[c].to_dict().items() if pd.notna(v)}}
                      for c in cf.columns[:8]]
    return out

# ── 1d. A股三表：新浪 HTTP 直连 ──
def triple_sina(code):
    """A股新浪直连（无需外部库）。"""
    out = {"lrb": [], "fzb": [], "llb": []}
    for rt, key in [("lrb", "lrb"), ("zcfz", "fzb"), ("xjll", "llb")]:
        try:
            r = requests.get(
                "https://quotes.sina.cn/cn/api/openapi.php/CompanyFinanceService.getFinanceReport2022",
                params={"paperCode": f"{_prefix(code)}{code}", "source": rt, "type": "0",
                        "page": "1", "num": "8"},
                headers={"User-Agent": UA}, timeout=15)
            d = r.json().get("result", {}).get("data", {}).get("report_list", {}) or {}
            rows = []
            for period in sorted(d.keys(), reverse=True)[:8]:
                obj = d[period]
                rec = {"报告期": f"{period[:4]}-{period[4:6]}-{period[6:8]}"}
                for it in (obj.get("data") or []):
                    if it.get("item_title") and it.get("item_value") is not None:
                        rec[it["item_title"]] = it["item_value"]
                rows.append(rec)
            out[key] = rows
        except Exception:
            pass
    out["_数据源"] = "新浪财经 HTTP"
    return out

# ── 1e. 港股三表：东财 emweb HTTP 直连 ──
def triple_em_hk(code):
    """港股三表东财 emweb HTTP 直连（无需 AKShare/yfinance）。"""
    out = {"lrb": [], "fzb": [], "llb": []}
    urls = {
        "fzb": f"https://emweb.securities.eastmoney.com/PC_HKF10/NewFinancialAnalysis/GetZCFZB?code={code}&startdate=&rtype=1",
        "lrb": f"https://emweb.securities.eastmoney.com/PC_HKF10/NewFinancialAnalysis/GetLRB?code={code}&startdate=&rtype=1",
        "llb": f"https://emweb.securities.eastmoney.com/PC_HKF10/NewFinancialAnalysis/GetXJLLB?code={code}&startdate=&rtype=1",
    }
    for key, url in urls.items():
        try:
            r = requests.get(url, headers={"User-Agent": UA, "Referer": "https://emweb.securities.eastmoney.com/"}, timeout=15)
            data = r.json().get("data", [])
            if not data:
                continue
            # Pivot: 长格式（截止日期 + 科目名称 + 本期金额）→ 宽格式
            df = pd.DataFrame(data)
            if "截止日期" not in df.columns:
                continue
            # 只取年报（TYPE=1 已经只给年报了）
            pv = df.pivot_table(
                index="截止日期", columns="科目名称",
                values="本期金额", aggfunc="first"
            ).sort_index(ascending=False).head(8)
            records = []
            for idx, row in pv.iterrows():
                rec = {"报告期": str(idx)[:10] if ":" not in str(idx) else str(idx)[:10]}
                for col in pv.columns:
                    rec[col] = row[col] if pd.notna(row[col]) else None
                records.append(rec)
            out[key] = records
        except Exception:
            pass
    out["_数据源"] = "东财 emweb HTTP（港股）"
    return out

def get_triple(code):
    """三表采集总入口，A股/港股不同降级链。"""
    if IS_HK:
        tiers = [
            ("AKShare(HK)", triple_akshare_hk),
            ("yfinance(HK)", triple_yfinance),
            ("emweb HTTP(HK)", triple_em_hk),
        ]
    else:
        tiers = [
            ("AKShare(A)", triple_akshare_a),
            ("新浪 HTTP", triple_sina),
        ]
    for tier, fn in tiers:
        try:
            t = fn(code)
            if t.get("lrb") or t.get("fzb"):
                print(f"  ✓ 三表 ({tier})", file=sys.stderr)
                return t
        except Exception:
            pass
    print("  ✗ 三表所有路径均失败", file=sys.stderr)
    return {"lrb": [], "fzb": [], "llb": [], "_数据源": "无"}

# ════════════════════════════════════════════════════════════════
#  模块 2 — 财务指标
# ════════════════════════════════════════════════════════════════

def finance_akshare_a(code):
    """A股: stock_financial_abstract（新浪源，80行指标×19年，实测可用）。"""
    if not _AK: raise RuntimeError("AKShare 不可用")
    fa = ak.stock_financial_abstract(symbol=code)
    if fa.empty: raise RuntimeError("为空")
    periods = [c for c in fa.columns if c not in ("选项", "指标")]
    annual = [p for p in periods if p.endswith("1231")]
    if not annual: annual = periods
    latest_p = annual[0]

    def _get(label):
        m = fa[fa["指标"] == label]
        return m.iloc[0][latest_p] if not m.empty else None

    rev = _round_or_none(_get("营业总收入"))
    np_ = _round_or_none(_get("归母净利润"))
    equity = _round_or_none(_get("股东权益合计(净资产)"))
    cost = _round_or_none(_get("营业成本"))
    total_assets = _round_or_none(_get("资产总计"))
    total_liab = _round_or_none(_get("负债合计"))

    snap = {
        "报告期": f"{latest_p[:4]}-{latest_p[4:6]}-{latest_p[6:8]}",
        "每股收益": str(_get("基本每股收益") or ""),
        "每股净资产": str(_get("每股净资产") or ""),
        "营业总收入": str(rev or ""),
        "归母净利润": str(np_ or ""),
        "_近8期报告期": annual[:8],
        "_数据源": "AKShare stock_financial_abstract（新浪）",
    }
    if rev and cost: snap["销售毛利率"] = f"{round((rev - cost) / rev * 100, 2)}%"
    if np_ and rev: snap["销售净利率"] = f"{round(np_ / rev * 100, 2)}%"
    if np_ and equity: snap["ROE加权"] = f"{round(np_ / equity * 100, 2)}%"
    if total_liab and total_assets: snap["资产负债率"] = f"{round(total_liab / total_assets * 100, 2)}%"

    prev_p = annual[1] if len(annual) > 1 else None
    if prev_p:
        prev_rev = _round_or_none(_get_val_from(fa, "营业总收入", prev_p))
        prev_np  = _round_or_none(_get_val_from(fa, "归母净利润", prev_p))
        if rev and prev_rev: snap["营收同比"] = f"{round((rev - prev_rev) / abs(prev_rev) * 100, 2)}%"
        if np_ and prev_np: snap["净利同比"] = f"{round((np_ - prev_np) / abs(prev_np) * 100, 2)}%"
    return snap

def finance_akshare_hk(code):
    """港股: stock_financial_hk_analysis_indicator_em（东财 emweb，9年数据，实测可用）。"""
    if not _AK: raise RuntimeError("AKShare 不可用")
    df = ak.stock_financial_hk_analysis_indicator_em(symbol=code)
    if df.empty: raise RuntimeError("为空")
    latest = df.iloc[0]
    snap = {
        "报告期": str(latest.get("REPORT_DATE", ""))[:10],
        "营业总收入": str(latest.get("OPERATE_INCOME", "")),
        "营收同比": str(latest.get("OPERATE_INCOME_YOY", "")),
        "归母净利润": str(latest.get("HOLDER_PROFIT", "")),
        "净利同比": str(latest.get("HOLDER_PROFIT_YOY", "")),
        "销售毛利率": str(latest.get("GROSS_PROFIT_RATIO", "")),
        "销售净利率": str(latest.get("NET_PROFIT_RATIO", "")),
        "ROE加权": str(latest.get("ROE_AVG", "")),
        "ROA": str(latest.get("ROA", "")),
        "资产负债率": str(latest.get("DEBT_ASSET_RATIO", "")),
        "流动比率": str(latest.get("CURRENT_RATIO", "")),
        "每股净资产": str(latest.get("BPS", "")),
        "基本每股收益": str(latest.get("BASIC_EPS", "")),
        "_数据源": "AKShare stock_financial_hk_analysis_indicator_em（东财 emweb）",
    }
    return snap

def finance_yfinance(code):
    """yfinance 财务指标（容错尝试）。"""
    if not _YF: raise RuntimeError("yfinance 不可用")
    ticker_str = f"{code}.HK" if IS_HK else code
    try:
        tk = yf.Ticker(ticker_str)
        info = tk.info
    except Exception as e:
        raise RuntimeError(f"yfinance 连接失败: {str(e)[:60]}")
    return {
        "报告期": str(info.get("lastFiscalYearEnd", ""))[:10],
        "营业总收入": str(info.get("totalRevenue", "")),
        "营收同比": str(info.get("revenueGrowth", "")),
        "归母净利润": str(info.get("netIncomeToCommon", "")),
        "销售毛利率": str(info.get("grossMargins", "")),
        "销售净利率": str(info.get("profitMargins", "")),
        "ROE加权": str(info.get("returnOnEquity", "")),
        "ROA": str(info.get("returnOnAssets", "")),
        "资产负债率": str(info.get("debtToEquity", "")),
        "每股收益": str(info.get("trailingEps", "")),
        "每股净资产": str(info.get("bookValue", "")),
        "PE": str(info.get("trailingPE", "")),
        "PB": str(info.get("priceToBook", "")),
        "_数据源": "yfinance",
    }

def finance_em(code):
    """东财 datacenter HTTP（A股/港股通用降级）。"""
    secucode = f"{code}.{'HK' if IS_HK else {'6':'SH','9':'SH'}.get(code[0],'SZ')}"
    try:
        d = http_get("https://datacenter.eastmoney.com/securities/api/data/v1/get",
                       params={"reportName": "RPT_F10_FINANCE_MAINFINADATA", "columns": "ALL",
                               "filter": f'(SECUCODE="{secucode}")', "pageSize": "8",
                               "sortColumns": "REPORT_DATE", "sortTypes": "-1",
                               "source": "HSF10", "client": "PC"}, timeout=15)
        rows = (d.get("result") or {}).get("data") or []
        if not rows: return {}
        latest = rows[0]
        pick = {"EPSJB": "每股收益", "BPS": "每股净资产", "ROEJQ": "ROE加权",
                "XSMLL": "销售毛利率", "XSJLL": "销售净利率", "ZCFZL": "资产负债率",
                "TOTALOPERATEREVE": "营业总收入", "PARENTNETPROFIT": "归母净利润",
                "TOTALOPERATEREVETZ": "营收同比", "PARENTNETPROFITTZ": "净利同比"}
        snap = {"报告期": str(latest.get("REPORT_DATE", ""))[:10]}
        for k, label in pick.items():
            v = latest.get(k); snap[label] = str(v) if v is not None else ""
        snap["_近8期报告期"] = [str(r.get("REPORT_DATE", ""))[:10] for r in rows]
        snap["_数据源"] = "东财 datacenter"
        return snap
    except Exception:
        return {}

def get_finance(code):
    """财务指标采集总入口。"""
    if IS_HK:
        tiers = [
            ("AKShare(HK)", finance_akshare_hk),
            ("yfinance", finance_yfinance),
            ("东财 datacenter", finance_em),
        ]
    else:
        tiers = [
            ("AKShare(A)", finance_akshare_a),
            ("东财 datacenter", finance_em),
        ]
    for tier, fn in tiers:
        try:
            snap = fn(code)
            if snap and len([v for v in snap.values() if v]) > 3:
                print(f"  ✓ finance ({tier})", file=sys.stderr)
                return snap
        except Exception:
            pass
    print("  ✗ finance 所有路径均失败", file=sys.stderr)
    return {"error": "finance 采集失败"}

# ════════════════════════════════════════════════════════════════
#  模块 3 — 行情
# ════════════════════════════════════════════════════════════════

def quote_tencent_a(codes):
    """A股腾讯行情（无需外部库，urllib 直连）。"""
    out = {}
    prefixed = [_prefix(c) + c for c in codes]
    try:
        req = urllib.request.Request(f"https://qt.gtimg.cn/q={','.join(prefixed)}")
        req.add_header("User-Agent", UA)
        data = urllib.request.urlopen(req, timeout=10).read().decode("gbk")
        for line in data.strip().split(";"):
            if "=" not in line or '"' not in line: continue
            key = line.split("=")[0].split("_")[-1]
            vals = line.split('"')[1].split("~")
            if len(vals) < 53: continue
            c = key[2:]
            out[c] = {
                "name": vals[1], "price": vals[3], "pe_ttm": vals[39],
                "pb": vals[46], "mcap_yi": vals[44], "float_mcap_yi": vals[45],
                "_数据源": "腾讯 qt.gtimg.cn",
            }
    except Exception:
        pass
    return out

def quote_tencent_hk(codes):
    """港股腾讯行情（urllib 直连，字段位置与 A 股不同）。"""
    out = {}
    prefixed = [f"hk{c}" for c in codes]
    try:
        req = urllib.request.Request(f"https://qt.gtimg.cn/q={','.join(prefixed)}")
        req.add_header("User-Agent", UA)
        data = urllib.request.urlopen(req, timeout=10).read().decode("gbk")
        for line in data.strip().split(";"):
            if "=" not in line or '"' not in line: continue
            key = line.split("=")[0].split("_")[-1]
            vals = line.split('"')[1].split("~")
            if len(vals) < 48: continue
            c = key[2:]  # hk00700 → 00700
            out[c] = {
                "name": vals[1], "price": vals[3],
                "pe_ttm": vals[39], "pb": vals[43],
                "mcap_yi": vals[44],
                "_数据源": "腾讯 qt.gtimg.cn（港股）",
            }
    except Exception:
        pass
    return out

def quote_yfinance(code):
    """yfinance 行情（容错尝试）。"""
    if not _YF: raise RuntimeError("yfinance 不可用")
    ticker_str = f"{code}.HK" if IS_HK else code
    try:
        tk = yf.Ticker(ticker_str)
        info = tk.info
    except Exception as e:
        raise RuntimeError(f"yfinance 连接失败: {str(e)[:60]}")
    return {
        code: {
            "name": info.get("shortName", ""),
            "price": str(info.get("currentPrice", "")),
            "pe_ttm": str(info.get("trailingPE", "")),
            "pb": str(info.get("priceToBook", "")),
            "mcap_yi": str(info.get("marketCap", "")),
            "_数据源": "yfinance",
        }
    }

def get_quotes(codes):
    """行情采集总入口。"""
    a_codes = [c for c in codes if len(c) == 6]
    hk_codes = [c for c in codes if len(c) == 5]
    out = {}
    if a_codes:
        out.update(quote_tencent_a(a_codes))
    if hk_codes:
        hk_quotes = quote_tencent_hk(hk_codes)
        out.update(hk_quotes)
        # 腾讯失败的走 yfinance
        for c in hk_codes:
            if c not in out or not out[c].get("name"):
                try:
                    yf_q = quote_yfinance(c)
                    out.update(yf_q)
                except Exception:
                    pass
    if out:
        print(f"  ✓ quote ({len(out)} 只)", file=sys.stderr)
        return out
    return {c: {"error": "行情获取失败"} for c in codes}

# ════════════════════════════════════════════════════════════════
#  模块 4 — 个股基本信息
# ════════════════════════════════════════════════════════════════

def get_em_info(code, quote_data=None):
    """个股信息：从行情 + F10 拼接。"""
    if quote_data is None:
        quote_data = {}
    q = quote_data.get(code, {}) if isinstance(quote_data, dict) else {}
    name = q.get("name", "")

    # 港股：走东财 emweb F10
    if IS_HK:
        try:
            d = http_get(f"https://emweb.securities.eastmoney.com/PC_HKF10/CompanySurvey/PageAjax?code={code}", timeout=15)
            jbzl = (d.get("jbzl") or [{}])[0] if isinstance(d, dict) else {}
            name = jbzl.get("ORG_NAME", name)
            return {
                "code": code, "name": name,
                "industry": jbzl.get("INDUSTRY_NAME", ""),
                "chairman": jbzl.get("CHAIRMAN", ""),
                "establish_date": str(jbzl.get("FOUND_DATE", ""))[:10],
                "total_shares": jbzl.get("TOTAL_CAPITAL", 0) or jbzl.get("TOTAL_SHARES", 0) or 0,
                "mcap_yi": q.get("mcap_yi", ""), "price": q.get("price", ""),
                "pe_ttm": q.get("pe_ttm", ""), "pb": q.get("pb", ""),
                "_数据源": "东财 emweb 港股 F10",
            }
        except Exception:
            return {"code": code, "name": name, "mcap_yi": q.get("mcap_yi", ""),
                    "price": q.get("price", ""), "_数据源": "行情拼接", "error": "港股 em_info 获取失败"}

    # A股：从行情 + F10 拼接
    try:
        d = http_get(f"https://emweb.securities.eastmoney.com/PC_HSF10/CompanySurvey/PageAjax?code=SH{code}", timeout=15)
        jbzl = (d.get("jbzl") or [{}])[0]
        name = jbzl.get("ORG_NAME", name)
        return {
            "code": code, "name": name,
            "industry": jbzl.get("EM2016", ""),
            "chairman": jbzl.get("CHAIRMAN", ""),
            "total_shares": jbzl.get("TOTAL_CAPITAL", 0) or 0,
            "mcap_yi": q.get("mcap_yi", ""), "price": q.get("price", ""),
            "pe_ttm": q.get("pe_ttm", ""), "pb": q.get("pb", ""),
            "_数据源": "东财 emweb F10 + 腾讯行情",
        }
    except Exception:
        return {"code": code, "name": name, "mcap_yi": q.get("mcap_yi", ""),
                "price": q.get("price", ""), "error": "A股 em_info 拼接失败", "_数据源": "行情拼接"}

# ════════════════════════════════════════════════════════════════
#  模块 5 — 研报（仅 A 股）
# ════════════════════════════════════════════════════════════════

def reports_akshare(code):
    if not _AK: raise RuntimeError("AKShare 不可用")
    try:
        df = ak.stock_research_report_em(symbol=code)
    except Exception:
        raise RuntimeError("AKShare 研报获取失败")
    if df.empty: return []
    records = []
    for _, r in df.head(30).iterrows():
        dt = next((str(r[c])[:10] for c in ["研究报告日期", "日期", "publishDate", "报告日期"] if c in r), "")
        org = next((str(r[c]) for c in ["研究机构简称", "机构", "orgSName"] if c in r), "")
        title = next((str(r[c])[:80] for c in ["研究报告标题", "标题", "title"] if c in r), "")
        records.append({"date": dt, "org": org, "title": title,
                        "_数据源": "AKShare stock_research_report_em"})
    return records

def reports_em(code):
    all_records = []
    for page in range(1, 3):
        try:
            d = http_get("https://reportapi.eastmoney.com/report/list",
                          params={"industryCode": "*", "pageSize": "100", "industry": "*",
                                  "beginTime": "2000-01-01", "endTime": "2030-01-01",
                                  "pageNo": str(page), "code": code, "fields": "", "qType": "0"},
                          headers={"Referer": "https://data.eastmoney.com/"}, timeout=30)
        except Exception:
            break
        rows = d.get("data") or []
        if not rows: break
        for r in rows:
            all_records.append({"date": str(r.get("publishDate", ""))[:10],
                                "org": r.get("orgSName", ""),
                                "title": str(r.get("title", ""))[:80],
                                "rating": r.get("emRatingName", ""),
                                "_数据源": "东财 reportapi"})
        if page >= min(d.get("TotalPage", 1) or 1, 3): break
        time.sleep(1.2)
    return all_records[:30]

def get_reports(code):
    if IS_HK: return [{"_说明": "港股研报需 WebSearch 补充"}]
    for tier, fn in [("AKShare", reports_akshare), ("东财", reports_em)]:
        try:
            recs = fn(code)
            if recs:
                print(f"  ✓ reports ({tier}, {len(recs)} 条)", file=sys.stderr)
                return recs
        except Exception:
            pass
    print("  ✗ reports 所有路径均失败", file=sys.stderr)
    return [{"error": "研报获取失败"}]

# ════════════════════════════════════════════════════════════════
#  模块 6 — 一致预期（仅 A 股，同花顺 HTTP）
# ════════════════════════════════════════════════════════════════

def get_forecast(code):
    if IS_HK: return [{"_说明": "港股一致预期需 WebSearch 补充"}]
    try:
        r = http_get(f"https://basic.10jqka.com.cn/new/{code}/worth.html",
                      headers={"Referer": "https://basic.10jqka.com.cn/"}, timeout=15, want="raw")
        r.encoding = "gbk"
        from io import StringIO
        try:
            dfs = pd.read_html(StringIO(r.text), flavor="lxml")
        except Exception:
            dfs = pd.read_html(StringIO(r.text), flavor="html5lib")
        for df in dfs:
            cols = [str(c) for c in df.columns]
            if any("每股收益" in c or "均值" in c for c in cols):
                print(f"  ✓ forecast (同花顺)", file=sys.stderr)
                return df.to_dict(orient="records")
    except Exception:
        pass
    print("  ✗ forecast 获取失败", file=sys.stderr)
    return [{"error": "一致预期获取失败"}]

# ════════════════════════════════════════════════════════════════
#  模块 7 — F10（公司概况 / 主营构成 / 股东研究）
# ════════════════════════════════════════════════════════════════

def get_f10(code):
    if IS_HK:
        return get_f10_hk(code)
    return get_f10_a(code)

def get_f10_hk(code):
    """港股 F10：东财 emweb HTTP 直连。"""
    out = {}
    # 公司概况
    try:
        d = http_get(f"https://emweb.securities.eastmoney.com/PC_HKF10/CompanySurvey/PageAjax?code={code}", timeout=15)
        jbzl = (d.get("jbzl") or [{}])[0]
        out["公司概况"] = {
            "公司简介": (jbzl.get("ORG_PROFILE") or "").strip()[:600],
            "所属行业": jbzl.get("INDUSTRY_NAME", ""),
            "董事长": jbzl.get("CHAIRMAN", ""),
            "成立日期": str(jbzl.get("FOUND_DATE", ""))[:10],
            "_数据源": "东财 emweb 港股 F10",
        }
    except Exception:
        out["公司概况"] = {"error": "港股 F10 CompanySurvey 失败"}

    # 港股无免费主营构成，用 WebSearch
    out["主营构成"] = [{"_说明": "港股主营构成需 WebSearch 补充"}]

    # 股东研究（尝试从 F10 获取）
    try:
        d = http_get(f"https://emweb.securities.eastmoney.com/PC_HKF10/ShareholderResearch/PageAjax?code={code}", timeout=15)
        sdgd = (d.get("sdgd") or []) if isinstance(d, dict) else []
        out["股东研究"] = {
            "十大股东": [
                {"名称": r.get("HOLDER_NAME", ""),
                 "持股比例": r.get("HOLD_RATIO", ""),
                 "持股数": r.get("HOLD_NUM", "")}
                for r in sdgd[:10]
            ],
            "_数据源": "东财 emweb 港股 F10",
        }
    except Exception:
        out["股东研究"] = {"error": "港股股东研究获取失败", "_说明": "需 WebSearch 补充"}

    out["财务分析"] = get_finance(code)
    out["行业分析"] = {"所属行业": out.get("公司概况", {}).get("所属行业", ""),
                       "说明": "行业竞争格局/排名以 WebSearch 为主"}
    return out

def get_f10_a(code):
    """A股 F10：东财 emweb HTTP。"""
    em = f"SH{code}" if code.startswith(("6", "9")) else f"SZ{code}"
    base = "https://emweb.securities.eastmoney.com/PC_HSF10"
    out = {}
    # 公司概况
    try:
        d = http_get(f"{base}/CompanySurvey/PageAjax?code={em}", timeout=15)
        jbzl = (d.get("jbzl") or [{}])[0]
        out["公司概况"] = {
            "公司简介": (jbzl.get("ORG_PROFILE") or "").strip()[:600],
            "所属东财行业": jbzl.get("EM2016", ""),
            "所属证监会行业": jbzl.get("INDUSTRYCSRC1", ""),
            "注册资本万元": jbzl.get("REG_CAPITAL", ""),
            "董事长": jbzl.get("CHAIRMAN", ""),
            "省份": jbzl.get("PROVINCE", ""),
            "_数据源": "东财 emweb F10",
        }
    except Exception:
        out["公司概况"] = {"error": "F10 CompanySurvey 失败"}
    time.sleep(0.3)
    # 主营构成
    try:
        d = http_get(f"{base}/BusinessAnalysis/PageAjax?code={em}", timeout=15)
        zygc = d.get("zygcfx") or []
        out["主营构成"] = [
            {"类型": r.get("MAINOP_TYPE", ""), "项目": r.get("ITEM_NAME", ""),
             "收入": r.get("MAIN_BUSINESS_INCOME", ""),
             "收入占比": r.get("MBI_RATIO", ""), "毛利率": r.get("GROSS_RPOFIT_RATIO", "")}
            for r in zygc[:20]]
    except Exception:
        out["主营构成"] = {"error": "主营构成获取失败"}
    time.sleep(0.3)
    # 股东研究
    try:
        d = http_get(f"{base}/ShareholderResearch/PageAjax?code={em}", timeout=15)
        sdgd = d.get("sdgd") or []
        out["股东研究"] = {
            "股东户数": d.get("gdrs", ""),
            "十大股东": [
                {"名称": r.get("HOLDER_NAME", ""), "持股比例": r.get("HOLD_RATIO", ""),
                 "持股数": r.get("HOLD_NUM", ""), "性质": r.get("HOLDER_TYPE", "")}
                for r in sdgd[:10]],
            "_数据源": "东财 emweb F10",
        }
    except Exception:
        out["股东研究"] = {"error": "股东研究获取失败"}
    out["财务分析"] = get_finance(code)
    out["行业分析"] = {
        "所属行业": out.get("公司概况", {}).get("所属东财行业", "") if isinstance(out.get("公司概况"), dict) else "",
        "说明": "行业竞争格局/排名以 WebSearch 为主",
    }
    return out

# ════════════════════════════════════════════════════════════════
#  模块 8 — 概念板块
# ════════════════════════════════════════════════════════════════

def get_blocks(code):
    if IS_HK:
        # 港股行业从 F10 公司概况中取
        f10 = result.get("f10", {})
        company = f10.get("公司概况", {}) if isinstance(f10, dict) else {}
        return {
            "industry": [{"name": company.get("所属行业", ""), "change_pct": "",
                          "_数据源": "东财 emweb 港股 F10"}],
            "concept": [],
            "region": [],
            "_说明": "港股概念板块需 WebSearch 补充",
        }
    try:
        d = http_get(
            f"https://finance.pae.baidu.com/api/getrelatedblock?code={code}&market=ab&typeCode=all&finClientType=pc",
            headers={"Accept": "application/vnd.finance-web.v1+json",
                     "Origin": "https://gushitong.baidu.com",
                     "Referer": "https://gushitong.baidu.com/"}, timeout=10)
    except Exception:
        return {"industry": [], "concept": [], "region": []}
    out = {"industry": [], "concept": [], "region": []}
    for block in d.get("Result", []):
        bt = block.get("type", "")
        for item in block.get("list", []):
            entry = {"name": item.get("name", ""), "change_pct": item.get("increase", "")}
            if "行业" in bt: out["industry"].append(entry)
            elif "概念" in bt: out["concept"].append(entry)
            elif "地域" in bt: out["region"].append(entry)
    return out

# ════════════════════════════════════════════════════════════════
#  模块 9 — 港股分红
# ════════════════════════════════════════════════════════════════

def get_hk_dividend(code):
    """港股分红：东财 emweb HTTP。"""
    try:
        d = http_get(
            f"https://emweb.securities.eastmoney.com/PC_HKF10/BonusFinancing/PageAjax?code={code}",
            timeout=15)
        rows = (d.get("fhpx") or []) if isinstance(d, dict) else []
        return [
            {
                "报告期": r.get("REPORT_DATE", ""),
                "方案": r.get("PLAN_EXPLAIN", ""),
                "除权日": r.get("EX_DIVIDEND_DATE", ""),
                "每股派息": r.get("DIVIDEND_PS", ""),
                "每股送转": r.get("BONUS_SHARE_RATIO", ""),
            }
            for r in rows[:20]
        ]
    except Exception:
        return [{"_说明": "港股分红数据需 WebSearch 补充"}]

# ════════════════════════════════════════════════════════════════
#  批量模式
# ════════════════════════════════════════════════════════════════

if QUOTES_MODE:
    try:
        q = get_quotes(QUOTE_CODES)
        print(json.dumps(q, ensure_ascii=False, indent=2))
    except Exception as e:
        print(json.dumps({"error": str(e)}, ensure_ascii=False))
        sys.exit(1)
    sys.exit(0)

if FINANCES_MODE:
    out = {"_meta": {"模式": "finances", "公司数": len(QUOTE_CODES),
                     "数据源": "A股: AKShare stock_financial_abstract | 港股: AKShare stock_financial_hk_analysis_indicator_em"}}
    for c in QUOTE_CODES:
        try:
            fin = get_finance(c)
            out[c] = fin
            print(f"  ✓ {c}", file=sys.stderr)
        except Exception as e:
            out[c] = {"error": str(e)[:80]}
        time.sleep(0.5)
    print(json.dumps(out, ensure_ascii=False, indent=2))
    sys.exit(0)

# ════════════════════════════════════════════════════════════════
#  全量采集
# ════════════════════════════════════════════════════════════════

print(f"开始采集 {CODE} 的数据...")

# 三表
triple = get_triple(CODE)
if triple.get("lrb") or triple.get("fzb"):
    for name in ("lrb", "fzb", "llb"):
        result[name] = triple.get(name, [])
    # EBITDA 拆解（仅 A 股，港股科目名不同且无现金流表标准字段）
    if result.get("lrb") and result.get("llb") and not IS_HK:
        try:
            lrb0 = result["lrb"][0] if result["lrb"] else {}
            llb0 = result["llb"][0] if result["llb"] else {}
            _get = lambda d, *keys: next((d.get(k) for k in keys if k in d and d[k] is not None), None)
            ebt = _get(lrb0, "利润总额", "TOTAL_PROFIT")
            interest = _get(lrb0, "财务费用", "FINANCIAL_EXPENSE") or 0
            ocf = _get(llb0, "经营活动产生的现金流量净额", "NETCASH_OPERATE", "NETCASH_OPER")
            np_ = _get(lrb0, "净利润", "NET_PROFIT",
                       "NETPROFIT_MARGIN") or _get(lrb0, "归属于母公司股东的净利润", "PARENT_NETPROFIT")
            if ebt:
                ebit = float(ebt) + (float(interest) if interest else 0)
                da = float(ocf) - float(np_) if ocf and np_ and float(ocf) > float(np_) else 0
                ebitda_v = ebit + da
                result["ebitda"] = {
                    "EBIT": round(ebit, 2), "EBITDA": round(ebitda_v, 2),
                    "税前利润": round(float(ebt), 2),
                    "财务费用": round(float(interest), 2) if interest else 0,
                    "折旧摊销": round(da, 2),
                    "报告期": lrb0.get("报告期", lrb0.get("REPORT_DATE_NAME", "")),
                    "数据来源": "AKShare 三表拆解",
                }
                print(f"  ✓ ebitda: {ebitda_v:.2f} 元 @ {result['ebitda']['报告期']}")
            else:
                result["ebitda"] = {"error": "利润总额字段缺失"}
        except Exception as e:
            result["ebitda"] = {"error": str(e)[:80]}
    else:
        result.setdefault("ebitda", {"error": "lrb/llb 缺失"})
else:
    for name in ("lrb", "fzb", "llb"):
        result[name] = []
    result["ebitda"] = {"error": "三表缺失"}

result["finance"] = get_finance(CODE)
result["f10"] = get_f10(CODE)

# 行情
try:
    result["quote"] = get_quotes([CODE])
except Exception as e:
    result["quote"] = {"error": str(e)}

# em_info 在行情之后获取（引用行情数据）
result["em_info"] = get_em_info(CODE, result.get("quote", {}))

result["reports"] = get_reports(CODE)
result["ths_forecast"] = get_forecast(CODE)

# 板块
try:
    result["blocks"] = get_blocks(CODE)
    print(f"  ✓ blocks", file=sys.stderr)
except Exception as e:
    result["blocks"] = {"error": str(e)}

# 港股分红
if IS_HK:
    result["dividend"] = get_hk_dividend(CODE)
    print(f"  ✓ dividend ({len(result['dividend'])} 条)", file=sys.stderr)

# ── 顶层拉平（保持与 valuation.py 兼容） ──
result["_market"] = "港股" if IS_HK else "A股"
try:
    em = result.get("em_info", {}) if isinstance(result.get("em_info"), dict) else {}
    q  = (result.get("quote") or {}).get(CODE, {}) if isinstance(result.get("quote"), dict) else {}
    fin = result.get("finance", {}) if isinstance(result.get("finance"), dict) else {}
    result["price"] = em.get("price") or q.get("price") or ""
    total_shares = em.get("total_shares", 0) or 0
    if total_shares: result["total_shares"] = float(total_shares)
    result["mcap_yi"] = em.get("mcap_yi", q.get("mcap_yi", 0))
    result["pe_ttm"] = em.get("pe_ttm", q.get("pe_ttm", 0))
    result["pb"] = em.get("pb", q.get("pb", 0))
    result["name"] = em.get("name", q.get("name", ""))
    result["code"] = CODE
    eps = fin.get("每股收益") or fin.get("基本每股收益", 0)
    bvps = fin.get("每股净资产") or fin.get("BPS", 0)
    result["eps_ttm"] = eps
    result["bvps"] = bvps
except Exception as e:
    print(f"  ⚠ 顶层拉平失败: {str(e)[:60]}", file=sys.stderr)

# ── 写入文件 ──
outfile = f"/tmp/{CODE}_data.json"
os.makedirs(os.path.dirname(outfile), exist_ok=True)
with open(outfile, "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2, default=str)

# 摘要
summary = {}
for k, v in result.items():
    if isinstance(v, dict) and "error" in v:
        summary[k] = f"FAIL: {str(v['error'])[:40]}"
    elif isinstance(v, list) and v and isinstance(v[0], dict) and "error" in v[0]:
        summary[k] = f"FAIL: {str(v[0]['error'])[:40]}"
    elif isinstance(v, list): summary[k] = f"OK: {len(v)} 条"
    elif isinstance(v, dict): summary[k] = f"OK: {len(v)} 项"
    else: summary[k] = str(v)[:30]
summary["output_file"] = outfile
print("\n" + "=" * 50)
print(json.dumps(summary, ensure_ascii=False, indent=2))
print("=" * 50)
print(f"\n数据已写入: {outfile}")
