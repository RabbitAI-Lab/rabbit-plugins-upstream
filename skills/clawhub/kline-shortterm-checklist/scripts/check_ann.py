#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""自动核查个股公告，覆盖 96 原则 #5(大股东减持) 与 #6(基本面问题) 的可文本判定部分。

⚠️ 重要：本脚本对「数据源是否真的按股票过滤」做了校验。若接口返回的是全市场通用流
（不绑定该股票，本沙箱环境的 np-anotice / 新浪公告页即如此），脚本会显式告警
「数据源未过滤→结果不可信」，而**不会**输出虚假的「✅ 未见」，避免对交易产生误导。

数据源（实测本环境可达但多数不按股票过滤）：
  - 东方财富 公告中心 np-anotice：返回 200，但忽略 stock_list/code，回吐全市场通用公告流
    → 脚本通过校验每条公告的关联股票代码来识别这种情况
  - 新浪个股公告页：返回 200，但 symbol 被忽略，回吐通用页
  - 巨潮 cninfo / 东财 datacenter：本环境 500 / 报表配置不存在

用法：python check_ann.py <代码> [代码 ...]
输出：JSON>>>-prefixed 行 + 人类可读结论。每个代码带 scoped 字段表示数据是否真按该股票过滤。
"""
import urllib.request
import json
import ssl
import sys

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

KEYWORDS = {
    "减持(#5)": ["减持"],
    "业绩预减/亏损(#6)": ["业绩预减", "预亏", "亏损", "同比下降", "业绩下滑", "营收下降"],
    "违规/处罚(#6)": ["违规", "处罚", "警示函", "立案", "被罚", "通报批评", "监管函"],
    "退市/风险警示(#6)": ["退市", "风险警示", "终止上市", "*ST", "ST"],
}


def _get(url, ref, timeout=10):
    h = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)", "Referer": ref}
    req = urllib.request.Request(url, headers=h)
    with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
        return r.read().decode("utf-8", "ignore")


def _norm(code):
    return code.replace("sh", "").replace("sz", "").replace("bj", "").strip()


def fetch_notices_em(code, pages=2):
    """返回公告列表，每条带 related_codes（关联股票代码），用于过滤校验。"""
    out = []
    for p in range(pages):
        url = (
            "https://np-anotice-stock.eastmoney.com/api/security/ann"
            f"?sr=-1&page_size=30&page_index={p}&client_source=web&stock_list={code}"
        )
        try:
            txt = _get(url, "https://quote.eastmoney.com/")
            j = json.loads(txt)
        except Exception as e:
            print(f"  [warn] np-anotice 页{p} 失败: {e}", file=sys.stderr)
            break
        lst = (j.get("data") or {}).get("list") or []
        if not lst:
            break
        for it in lst:
            codes = it.get("codes") or []
            related = [str(c.get("stock_code", "")) for c in codes]
            out.append(
                {
                    "date": (it.get("notice_date") or it.get("eitime") or "")[:10],
                    "title": (it.get("title") or it.get("notice_title") or "").strip(),
                    "type": it.get("column") or it.get("ann_type") or "",
                    "related_codes": related,
                }
            )
    return out


def is_scoped(notices, code6):
    """若没有任何一条公告关联到目标股票代码，说明接口未按股票过滤（回吐通用流）。"""
    for n in notices:
        for rc in n.get("related_codes", []):
            if rc and rc == code6:
                return True
    return False


def scan(notices):
    result = {k: [] for k in KEYWORDS}
    for n in notices:
        t = n.get("title", "")
        for cat, kws in KEYWORDS.items():
            for kw in kws:
                if kw in t:
                    result[cat].append(f"{n.get('date','')} {t}")
                    break
    return result


def main():
    if len(sys.argv) < 2:
        print("用法: python check_ann.py <代码> [代码 ...]  例如 603045 600158")
        sys.exit(1)
    summary = {}
    for raw in sys.argv[1:]:
        code6 = _norm(raw)
        print(f"\n=== {raw} 公告核查 ===")
        notices = fetch_notices_em(code6)
        if not notices:
            print("  np-anotice 未返回数据（接口异常）。")
            summary[raw] = {"scoped": None, "notice_count": 0, "verdict": "无数据/需人工"}
            continue
        scoped = is_scoped(notices, code6)
        if not scoped:
            print(f"  ⚠️ 数据源未按股票过滤（返回全市场通用公告流，{len(notices)} 条均不关联本股）")
            print(f"  → 结果不可信，#5/#6 仍需人工核查（东财公告页 / 巨潮 cninfo）。")
            summary[raw] = {
                "scoped": False,
                "notice_count": len(notices),
                "verdict": "数据源未过滤/不可信→需人工",
            }
            continue
        print(f"  数据已确认按本股过滤，拉取 {len(notices)} 条（最新 {notices[0].get('date','')}）")
        hits = scan(notices)
        for cat, items in hits.items():
            flag = "⚠️ 命中" if items else "✅ 未见"
            print(f"  {cat}: {flag}" + ("" if not items else " -> " + "; ".join(items[:3])))
        summary[raw] = {"scoped": True, "notice_count": len(notices), "hits": hits}
    print("\nJSON>>> " + json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
