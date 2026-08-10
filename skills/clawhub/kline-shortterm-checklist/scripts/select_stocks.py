#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全A 下午2:30 第1-4层客观初筛 (东方财富 push2delay 延迟行情 = 8-7收盘)。
pz 上限100/页, 故按 pn 翻页至 涨幅<3 为止。筛选: 涨幅3-5% & 量比>=1 & 换手5-10% & 流通50-200亿。"""
import json, urllib.request, urllib.parse, time

FS = "m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23"
FIELDS = "f12,f14,f2,f3,f9,f10,f8,f20"   # +f9 市盈率TTM(用于自动核查亏损/基本面)
HOST = "https://push2delay.eastmoney.com/api/qt/clist/get"

def fetch_page(pn, pz=100):
    url = f"{HOST}?pn={pn}&pz={pz}&po=1&np=1&fltt=2&invt=2&fid=f3&fs={FS}&fields={FIELDS}"
    req = urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0","Referer":"https://quote.eastmoney.com/"})
    for _ in range(6):
        try:
            return json.loads(urllib.request.urlopen(req, timeout=25).read().decode("utf-8"))
        except Exception:
            time.sleep(2)
    return None

def _norm(c):
    c = c.strip()
    if c[0] == "6": return "sh"+c
    if c[0] in ("0","3"): return "sz"+c
    if c[0] in ("4","8"): return "bj"+c
    return c

def tencent_float_mv(codes):
    """批量取腾讯权威流通市值(字段44, 单位亿)，修正东方财富 f20 实为总市值的偏差。"""
    out = {}
    for i in range(0, len(codes), 40):
        q = ",".join(_norm(c) for c in codes[i:i+40])
        url = "https://qt.gtimg.cn/q=" + urllib.parse.quote(q)
        req = urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0","Referer":"https://finance.qq.com/"})
        raw = None
        for _ in range(5):
            try:
                raw = urllib.request.urlopen(req, timeout=25).read().decode("gbk","ignore")
                break
            except Exception:
                time.sleep(1.5)
        if not raw: continue
        for blk in raw.split(";"):
            blk = blk.strip()
            if not blk.startswith("v_"): continue
            inner = blk.split('"',1)[1].rsplit('"',1)[0]
            fld = inner.split("~")
            try:
                code = fld[2]; fm = float(fld[44])
            except (IndexError, ValueError):
                continue
            out[code] = fm
    return out

def f(x):
    try: return float(x)
    except: return None

def main():
    cands=[]; pn=1; MAXP=60
    while pn<=MAXP:
        d=fetch_page(pn)
        if not d: break
        items=d.get("data",{}).get("diff",[])
        if not items: break
        stop=False
        for it in items:
            chg=f(it.get("f3"))
            if chg is None: continue
            if chg < 3.0:   # 涨幅降序, 之后均<3
                stop=True; break
            if not (3.0 <= chg <= 5.0): continue
            vr=f(it.get("f10")); to=f(it.get("f8")); fmraw=f(it.get("f20"))
            fm=(fmraw/1e8) if (fmraw and fmraw>1000) else fmraw
            pe=f(it.get("f9"))
            nm=it.get("f14") or ""
            st = ("ST" in nm) or ("退" in nm)
            if vr is None or vr < 1: continue
            if to is None or not (5.0 <= to <= 10.0): continue
            if fm is None or not (50 <= fm <= 200): continue
            cands.append({"code":it.get("f12"),"name":nm,
                          "price":f(it.get("f2")),"chg":chg,"vr":vr,"to":to,"fm":fm,"pe":pe,"st":st})
        if stop: break
        if len(items) < 100: break
        pn+=1
    # 流通市值口径修正：东方财富 f20 个别股票返回的是总市值，统一用腾讯权威流通市值(字段44)重筛
    if cands:
        fm_map = tencent_float_mv([c["code"] for c in cands])
        kept = []
        for c in cands:
            fm = fm_map.get(c["code"])
            if fm is None or not (50 <= fm <= 200):
                continue
            c["fm"] = fm
            kept.append(c)
        dropped = len(cands) - len(kept)
        if dropped:
            print(f"[口径修正] 腾讯流通市值重筛剔除 {dropped} 只(流通<50或>200亿)")
        cands = kept
    cands.sort(key=lambda x:(-x["vr"], -x["to"]))
    with open("candidates.json","w",encoding="utf-8") as fh:
        json.dump(cands, fh, ensure_ascii=False, indent=1)
    print(f"翻页数={pn}  通过四层(含流通市值修正)数量={len(cands)}")
    print(f"{'代码':<8}{'名称':<10}{'现价':>8}{'涨幅%':>8}{'量比':>8}{'换手%':>8}{'流通亿':>10}")
    for c in cands[:30]:
        print(f"{c['code']:<8}{c['name']:<10}{c['price']:>8.2f}{c['chg']:>8.2f}{c['vr']:>8.2f}{c['to']:>8.2f}{c['fm']:>10.1f}")

if __name__=="__main__":
    main()
