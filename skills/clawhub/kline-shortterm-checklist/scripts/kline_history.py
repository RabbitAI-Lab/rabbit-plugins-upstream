#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""kline_history.py — 日K历史研判(趋势/均线/量能/当日K线形态)

用法:
    python kline_history.py <代码> [<代码2> ...]
    代码支持: 603045 / sh603045 / 600158 / sz000001

数据源: 新浪日K (money.finance.sina.com.cn, 实际价, 未前复权)。
  说明: 腾讯 web.ifzq.gtimg.cn K线接口在本环境返回 "bad params",
        东方财富 push2his 在本环境断连, 故历史K线统一走新浪。
  客观快照(涨跌幅/量比/换手/流通市值)仍由 fetch_quote.py 走腾讯 qt.gtimg.cn。

输出: MA5/10/20、多头排列、近20日高低与涨跌、量能比、当日K线要素,
      以及可程序化判定的12形态子集(其余需副图/缺口人工确认)。
"""
import sys, json, urllib.request

API = "https://money.finance.sina.com.cn/quotes_service/api/json_v2.php/CN_MarketData.getKLineData"

def normalize(code):
    code = code.strip().lower()
    if code.startswith(("sh","sz","bj")):
        return code
    if len(code)==6 and code.isdigit():
        if code[0]=="6": return "sh"+code
        if code[0] in ("0","3"): return "sz"+code
        if code[0] in ("4","8"): return "bj"+code
    return code

def fetch(sym, datalen=45):
    url = f"{API}?symbol={sym}&scale=240&ma=20&datalen={datalen}"
    req = urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0","Referer":"https://finance.sina.com.cn/"})
    raw = urllib.request.urlopen(req, timeout=15).read().decode("gbk","ignore")
    return json.loads(raw)

def ma(closes, n, i):
    if i < n-1: return None
    return sum(closes[i-n+1:i+1]) / n

def analyze(sym, name):
    k = fetch(sym)
    k = [r for r in k if r["day"] <= "2026-08-07"][-45:]
    n=len(k); i=n-1
    dates=[r["day"] for r in k]
    o=[float(r["open"]) for r in k]; c=[float(r["close"]) for r in k]
    h=[float(r["high"]) for r in k]; l=[float(r["low"]) for r in k]
    v=[int(r["volume"]) for r in k]
    ma5,ma10,ma20 = ma(c,5,i), ma(c,10,i), ma(c,20,i)
    multi = (ma5 and ma10 and ma20 and ma5>ma10>ma20 and c[i]>ma5)
    hh=max(h[max(0,i-19):i+1]); ll=min(l[max(0,i-19):i+1])
    chg20=(c[i]/c[i-19]-1)*100 if i>=19 else None
    near_high=(hh-c[i])/hh*100
    v5=sum(v[max(0,i-4):i+1])/5; v20=sum(v[max(0,i-19):i+1])/20
    vratio=v5/v20
    body=abs(c[i]-o[i]); rng=h[i]-l[i]
    upper=h[i]-max(o[i],c[i]); lower=min(o[i],c[i])-l[i]
    yang=c[i]>o[i]
    def big(idx): return abs(c[idx]-o[idx]) > (h[idx]-l[idx])*0.5
    pats=[]
    if i>=2 and c[i-2]<o[i-2] and abs(c[i-1]-o[i-1])<(h[i-1]-l[i-1])*0.3 and yang and c[i]>o[i-2] and (h[i]-l[i])>body*1.5:
        pats.append("希望之星(阴→十字星→大阳)")
    if i>=1:
        if c[i-1]<o[i-1] and big(i-1) and yang and c[i]>o[i-1]:
            pats.append("旭日东升(大阴后阳线反包)")
        if c[i-1]<o[i-1] and o[i]>=o[i-1] and yang and (c[i]-o[i])>body*1.0:
            pats.append("上涨分手(中阴后跳空高开大阳)")
        if c[i-1]<o[i-1] and v[i]>v[i-1]*1.2 and yang and c[i]>o[i-1]:
            pats.append("葵花向阳(缩量阴后放量大阳)")
    if yang and lower>=2*body and lower>upper and lower>rng*0.45:
        pats.append("美人长腿(长下影阳线/单针探底)")
    if upper>=2*body and lower<upper*0.4 and not yang:
        pats.append("倒锤头线(长上影、下影极短)")
    if i>=3:
        pre=[abs(c[j]-o[j]) for j in range(i-3,i)]; pre_v=sum(v[i-3:i])/3
        if max(pre)<rng*0.6 and v[i]>pre_v*1.3 and yang and c[i]>max(c[i-3:i]):
            pats.append("阴阳鉴攻(缩量横盘后放量突破)")
    print(f"=== {name}({sym}) 截至 {dates[-1]} ===")
    print(f"  收盘={c[i]:.2f} 开={o[i]:.2f} 高={h[i]:.2f} 低={l[i]:.2f} 量={v[i]/100/10000:.1f}万手")
    print(f"  MA5={ma5:.2f} MA10={ma10:.2f} MA20={ma20:.2f}")
    print(f"  多头排列(MA5>MA10>MA20且价>MA5): {'是' if multi else '否'}")
    print(f"  近20日: 高={hh:.2f} 低={ll:.2f} 收盘较20日前={chg20:+.1f}% 距20日高={near_high:.1f}%")
    print(f"  量能: 近5/20日均量={vratio:.2f}x -> {('放量' if vratio>1.2 else '缩量' if vratio<0.8 else '平量')}")
    print(f"  8-7K线: {'阳线' if yang else '阴线'} 实体={body:.2f} 上影={upper:.2f} 下影={lower:.2f} 振幅={rng:.2f}")
    print(f"  可程序化命中形态: {pats if pats else '无'}")
    print(f"  需副图/缺口人工项: 狮子张口·挖坑埋牛(KDJ J<0/CCI<-200)·回眸一笑(30日线)·鱼跃龙门(5/10/30金叉)·岛形反转")
    print()

def main():
    if len(sys.argv)<2:
        print("用法: python kline_history.py <代码> [<代码2> ...]"); sys.exit(1)
    names = {"sh603045":"福达合金","sh600158":"中体产业"}
    for cd in sys.argv[1:]:
        s = normalize(cd)
        analyze(s, names.get(s, s))

if __name__ == "__main__":
    main()
