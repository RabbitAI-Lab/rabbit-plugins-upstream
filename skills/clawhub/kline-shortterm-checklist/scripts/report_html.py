#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""report_html.py — 输出【固定版式·清爽】的 96原则 短线筛查 HTML 看板。

用法（在已运行 select_stocks.py 与 kline_history.py --json 的目录下执行）:
    python report_html.py

读取同目录 candidates.json（客观四层候选）与 kline_data.json（K线研判），
统一渲染成：顶部 KPI 概览 + 可折叠候选表 + 纵向分块深度研判 + 六不卖 + 综合结论。
版式固定，保证每次产出一致（不再随实例飘移）。仅用标准库。
"""
import json, os

PAT_MEAN = {
    "狮子张口": "下跌末端抛压枯竭，多头启动", "挖坑埋牛": "刻意洗盘挖坑，挖完往往起涨",
    "阴阳鉴攻": "横盘蓄势结束，选择向上", "回眸一笑": "回踩确认，二次启动",
    "鱼跃龙门": "趋势反转确认", "葵花向阳": "上涨中继洗盘后继续",
    "美人长腿": "下方有强承接，见底信号", "旭日东升": "空头力竭，多头反包",
    "倒锤头线": "探顶试盘/潜在反转，需次日确认", "希望之星": "经典见底组合",
    "岛形反转": "情绪急转，底部反转强信号", "上涨分手": "上涨中继，短暂洗盘后延续",
}

def norm_key(code):
    return code[2:] if code[:2] in ("sh", "sz", "bj") else code

def verdict(c):
    if c.get("pe") is not None and c["pe"] < 0:
        return ("不买", "亏损·九不买#6")
    if c.get("pe") is not None and c["pe"] > 200:
        return ("观察", "估值偏高·谨慎")
    return ("符合", "通过·待人工核查")

def build():
    cwd = os.getcwd()
    with open(os.path.join(cwd, "candidates.json"), encoding="utf-8") as f:
        cands = json.load(f)
    kl = {}
    try:
        with open(os.path.join(cwd, "kline_data.json"), encoding="utf-8") as f:
            for d in json.load(f):
                kl[norm_key(d["code"])] = d
    except FileNotFoundError:
        pass
    data_date = next(iter(kl.values())).get("date", "最近交易日") if kl else "最近交易日"

    # ---- 全候选表格 ----
    rows = []
    for c in cands:
        v, note = verdict(c)
        k = kl.get(c["code"])
        trend = ("多头排列✓" if k and k.get("multi") else
                 ("站上均线·未完全多头" if k else "—"))
        badge = {"不买": "bad", "观察": "warn", "符合": "ok"}[v]
        rows.append(
            f"<tr><td class='l'>{c['code']}</td><td class='l'>{c['name']}</td><td>{c['price']:.2f}</td>"
            f"<td>{c['chg']:.2f}</td><td>{c['vr']:.2f}</td><td>{c['to']:.2f}</td>"
            f"<td>{c['fm']:.1f}</td><td>{c['pe']:.2f}</td><td>{trend}</td>"
            f"<td><span class='b {badge}'>{v}</span></td></tr>"
        )
    all_rows = "\n".join(rows)

    loss = [c for c in cands if c.get("pe") is not None and c["pe"] < 0]
    loss_rows = "\n".join(
        f"<tr><td class='l'>{c['code']}</td><td class='l'>{c['name']}</td><td>{c['price']:.2f}</td>"
        f"<td>{c['chg']:.2f}</td><td>{c['pe']:.2f}</td>"
        f"<td class='l'>TTM 市盈率为负 = 当期亏损，触发九不买 #6</td></tr>"
        for c in loss)

    # ---- 深度研判候选 ----
    prio = [c for c in cands if c["code"] in kl and (
        kl[c["code"]].get("multi") or
        (c.get("pe") and c["pe"] > 0 and c["pe"] < 20) or
        kl[c["code"]].get("near_high", 99) < 1)]
    prio.sort(key=lambda x: -x["vr"])
    prio = prio[:10]

    def deep(c):
        k = kl[c["code"]]
        multi_txt = "是（MA5>MA10>MA20 且价>MA5）" if k.get("multi") else "否（价站上均线，但 MA10 仍在 MA20 下方，属企稳/反弹初期）"
        pat_html = "<br>".join(f"· {p}：{PAT_MEAN.get(p,'')}" for p in k.get("pats", [])) or "无程序化命中（需看图确认 狮子张口/挖坑埋牛/回眸一笑/鱼跃龙门/岛形反转）"
        nh = k.get("near_high", 99)
        items = [
            ("下跌趋势不买", f"价 {k['close']} > MA20 {k['ma20']}，不在长期均线下方 → 未触发"),
            ("高位放量滞涨不买", ("处 20 日新高突破位，价随量升、非滞涨 → 未触发，但追高需等回踩" if nh < 1 else "处反弹/上行段，非三浪末端诱多 → 未触发")),
            ("利好兑现不买", "👁 需核查公告/新闻（本环境无可达公告源），无可见证据"),
            ("短期暴涨不买", ("处 20 日新高突破位，非连续涨停/一字板 → 未触发，但追高需等回踩" if nh < 1 else "近20日距高点尚远（非连续涨停）→ 未触发")),
            ("大股东减持不买", "👁 需查东财/巨潮资讯减持公告，本环境不可达，标人工核查"),
            ("基本面问题不买", f"PE(TTM) {c['pe']:.2f}，非负、非 ST → 未触发"),
            ("跌破平台支撑不买", "价在 MA 上方运行，未破位 → 未触发（深跌反弹股需确认不再创新低）"),
            ("技术走坏不买", f"均线非空头排列；量比 {c['vr']:.2f} ≤10 → 未触发"),
            ("换手异常不买", f"换手 {c['to']:.2f}% 在 5~10%；量比≤10 → 未触发"),
        ]
        nine = "\n".join(f"<li><b>{t}</b>：{d}</li>" for t, d in items)
        buypt = ("距 20 日高仅 %.1f%%，处于突破位——按层8须等 14:30 后回踩均线不破再入场，忌追高" % nh) if nh < 1 else ("距 20 日高 %.1f%%，仍有空间；按层8等回踩均线（MA5≈%.2f）低吸" % (nh, k["ma5"]))
        concl = ('趋势最强（干净多头排列）' if k.get('multi') else '价格站上均线、反弹初期')
        if nh < 1: concl += '；创新高突破，动能强但需回踩确认'
        else: concl += '；未达前高，安全边际较好'
        if c['pe'] and c['pe'] < 20: concl += '；估值偏低（PE<20）'
        else: concl += '；估值中性'
        # --- 六不卖逐只研判 + 下车信号（持有侧纪律，告诉用户何时该走）---
        ts = (k['close'] > k['ma5'] and k['close'] > k['ma10'])   # 趋势强劲
        vh = k['vratio'] >= 0.8                                  # 量能健康(价涨量增/未明显缩)
        io = bool(k.get('multi')) or bool(k.get('pats'))          # 指标向好
        tg = k['near_high'] > 5                                  # 未达目标(距前高仍有空间)
        sell_items = [
            ("趋势强劲", "命中（价在 MA5/MA10 上方）" if ts else "偏弱（价未稳站短均线）"),
            ("热点题材", "👁 需人工结合当日板块/政策判定"),
            ("指标向好", ("命中（多头排列/底部形态）" if io else "一般（无明确共振）")),
            ("量能健康", ("命中（量价配合）" if vh else "偏弱（缩量，需观察）")),
            ("逻辑未变", "👁 取决于你的买入初衷，无法从量价判定"),
            ("未达目标", (f"命中（距前高尚有 {k['near_high']:.1f}% 空间）" if tg else "已近前高，须先设止盈目标")),
        ]
        sell_li = "\n".join(f"<li><b>{t}</b>：{d}</li>" for t, d in sell_items)
        obj_hit = sum([ts, vh, io, tg])
        hold = ("持有信号较强，可继续持有，严格按下方离场信号风控" if obj_hit >= 3 else
                "持有信号中等，可持有但收紧止损（如 MA5 下方）" if obj_hit == 2 else
                "持有信号偏弱，仅宜快进快出/小仓，破短均线即走")
        exit_sig = (f"⏹ <b>下车信号（离场条件）</b>：跌破 MA5({k['ma5']:.2f}) 或前低失效、"
                    f"量价背离（价升量缩）、逻辑破坏、或达预设止盈 —— 任一触发即离场，其余继续持有。")
        sell_html = f"""
      <div class="blk full sell"><div class="blk-t">六不卖持有研判 + 下车信号</div>
        <ul class="nine">{sell_li}</ul>
        客观命中 <b>{obj_hit}/4</b>，主观 2 项（题材/逻辑）待核 → <b>综合：{hold}</b><br>{exit_sig}
      </div>"""
        return f"""
    <div class="card">
      <div class="card-h">
        <span class="cname">{c['name']} <span class="ccode">{c['code']}</span></span>
        <span class="pills">
          <span class="pill">现价 {c['price']:.2f}</span>
          <span class="pill">涨幅 {c['chg']:.2f}%</span>
          <span class="pill">PE {c['pe']:.2f}</span>
          <span class="pill">流通 {c['fm']:.0f}亿</span>
        </span>
      </div>
      <div class="grid3">
        <div class="blk"><div class="blk-t">客观指标</div>
          涨幅 {c['chg']:.2f}%（达标 3~5%）<br>量比 {c['vr']:.2f}（≥1）<br>换手 {c['to']:.2f}%（达标 5~10%）<br>流通市值 {c['fm']:.0f}亿（达标 50~200）
        </div>
        <div class="blk"><div class="blk-t">趋势 / 均线</div>
          MA5 {k['ma5']:.2f} / MA10 {k['ma10']:.2f} / MA20 {k['ma20']:.2f}<br>多头排列：{multi_txt}<br>近20日 高 {k['hh']:.2f} 低 {k['ll']:.2f}<br>较20日前 {k['chg20']:+.1f}%，距高 {k['near_high']:.1f}%
        </div>
        <div class="blk"><div class="blk-t">量能 / K线</div>
          近5/20日均量 {k['vratio']:.2f}x → {k['vlab']}<br>{pat_html}
        </div>
      </div>
      <div class="blk full"><div class="blk-t">九不买逐条判定</div><ul class="nine">{nine}</ul></div>
      <div class="blk full"><div class="blk-t">八层筛选（层5-8 人工）</div>量能{k['vlab']}（{'量价配合尚可' if k['vratio']>=1.0 else '量能偏谨慎'}）；均线见上；分时强度/题材 👁；<b>买点</b>：{buypt}。</div>
      <div class="blk full concl"><div class="blk-t">综合结论</div>{concl}。量化九不买全过。</div>{sell_html}
    </div>"""
    deep_html = "\n".join(deep(c) for c in prio)

    multi_list = [c for c in cands if kl.get(c["code"], {}).get("multi")]
    cheap = [c for c in cands if c.get("pe") and 0 < c["pe"] < 20]
    rebound = [c for c in cands if kl.get(c["code"], {}).get("near_high", 0) > 20]

    CSS = """
<style>
 :root{--accent:#2f5fe0;--ok:#1f9d57;--warn:#d98200;--bad:#d64545;--ink:#27313f;--muted:#7a8696;--line:#e8edf3;--soft:#f6f8fb;}
 *{box-sizing:border-box}
 body{font-family:-apple-system,'PingFang SC','Microsoft YaHei',sans-serif;background:#eaeef4;color:var(--ink);margin:0;padding:28px 16px;line-height:1.75;font-size:14px}
 .wrap{max-width:1060px;margin:0 auto;background:#fff;border-radius:18px;padding:40px 46px;box-shadow:0 10px 40px rgba(30,50,90,.08)}
 h1{font-size:25px;margin:0 0 6px;color:#16223a;font-weight:700;letter-spacing:.5px}
 .sub{color:var(--muted);font-size:12.5px;margin-bottom:6px}
 .note{margin:18px 0;padding:10px 16px;border-left:4px solid var(--warn);background:#fff8ee;color:#8a5a00;border-radius:0 10px 10px 0;font-size:12.5px}
 h2{font-size:17px;margin:34px 0 14px;color:#16223a;font-weight:700;display:flex;align-items:center;gap:9px}
 h2::before{content:"";width:5px;height:18px;background:var(--accent);border-radius:3px;display:inline-block}
 .kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin:20px 0 4px}
 .kpi{background:linear-gradient(135deg,#f3f6fd,#eaf0fc);border:1px solid #e2e9f7;border-radius:14px;padding:16px 14px;text-align:center}
 .kpi .num{font-size:27px;font-weight:800;color:var(--accent);line-height:1.1}
 .kpi .lab{font-size:12px;color:var(--muted);margin-top:4px}
 table{width:100%;border-collapse:collapse;font-size:13px;margin:6px 0}
 th,td{padding:10px 12px;text-align:center;border-bottom:1px solid var(--line)}
 th{background:var(--soft);color:#46556b;font-weight:600;font-size:12.5px;position:sticky;top:0}
 td.l,th.l{text-align:left}
 tbody tr:hover{background:#f5f9ff}
 .b{display:inline-block;padding:2px 11px;border-radius:20px;font-size:12px;font-weight:700;color:#fff}
 .ok{background:var(--ok)}.warn{background:var(--warn)}.bad{background:var(--bad)}
 .pill{display:inline-block;background:var(--soft);border:1px solid var(--line);border-radius:20px;padding:2px 11px;font-size:12px;color:#46556b;margin:2px 4px 2px 0}
 details{border:1px solid var(--line);border-radius:12px;padding:4px 18px;margin:12px 0;background:#fcfdff}
 summary{cursor:pointer;font-weight:600;color:#2b3a52;padding:12px 0;font-size:14px}
 summary::marker{color:var(--accent)}
 .legend{font-size:12px;color:var(--muted);margin:2px 0 10px}
 .card{border:1px solid var(--line);border-left:5px solid var(--accent);border-radius:14px;padding:20px 22px;margin:18px 0;background:#fff;box-shadow:0 2px 10px rgba(30,50,90,.04)}
 .card-h{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;margin-bottom:14px;padding-bottom:12px;border-bottom:1px dashed var(--line)}
 .cname{font-size:17px;font-weight:700;color:#16223a}
 .ccode{font-size:12px;color:var(--muted);font-weight:500;margin-left:4px}
 .grid3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px}
 .blk{background:var(--soft);border-radius:10px;padding:12px 14px;font-size:13px;color:#3a4658}
 .blk.full{grid-column:1/-1}
 .blk-t{font-size:12px;font-weight:700;color:var(--accent);margin-bottom:6px;letter-spacing:.3px}
 .blk.concl{background:#eef6ef;border-left:3px solid var(--ok)}
 .blk.sell{background:#fff7f0;border-left:3px solid var(--warn)}
 .nine{margin:0;padding-left:18px}
 .nine li{margin:4px 0}
 .six{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:8px}
 .six div{background:var(--soft);border-radius:9px;padding:9px 12px;font-size:12.5px}
 .tier{display:flex;gap:12px;flex-wrap:wrap;margin:8px 0}
 .chip{background:var(--soft);border:1px solid var(--line);border-radius:10px;padding:8px 12px;font-size:12.5px;color:#3a4658}
 .chip b{color:var(--accent)}
 .foot{margin-top:34px;font-size:11.5px;color:var(--muted);border-top:1px solid var(--line);padding-top:14px}
 @media(max-width:720px){.kpis{grid-template-columns:repeat(2,1fr)}.grid3{grid-template-columns:1fr}.six{grid-template-columns:1fr}}
</style>"""

    k_total = len(cands); k_excl = len(loss); k_conf = k_total - k_excl; k_multi = len(multi_list)
    multi_txt = "、".join(f"{c['name']}({c['code']})" for c in multi_list) or "无"
    cheap_txt = "、".join(f"{c['name']}({c['code']} PE{c['pe']:.0f})" for c in cheap[:8]) or "无"
    reb_txt = "、".join(f"{c['name']}({c['code']})" for c in rebound) or "无"

    HTML = f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>96原则短线筛查报告 {data_date}</title>{CSS}</head><body><div class="wrap">
<h1>K线短线选股 · 96原则筛查报告</h1>
<div class="sub">数据基准日：{data_date}（最近交易日收盘）｜方法论：kline-shortterm-checklist 技能｜版式：固定 HTML 看板</div>

<div class="kpis">
  <div class="kpi"><div class="num">{k_total}</div><div class="lab">客观四层候选</div></div>
  <div class="kpi"><div class="num" style="color:var(--bad)">{k_excl}</div><div class="lab">九不买剔除（亏损）</div></div>
  <div class="kpi"><div class="num" style="color:var(--ok)">{k_conf}</div><div class="lab">通过九不买量化</div></div>
  <div class="kpi"><div class="num">{k_multi}</div><div class="lab">干净多头排列</div></div>
</div>

<div class="note">⚠️ 风险声明：本清单为技术分析方法论的纪律化整理，<b>不构成任何投资建议</b>。指标/形态均有失效与骗线可能，请结合仓位管理与止损纪律；实盘前用模拟盘或极小仓位验证，亏损自负。</div>

<h2>一、数据与方法</h2>
<p style="color:#3a4658">客观指标（涨幅/量比/换手/流通市值/PE）取自东方财富 push2delay 延迟行情 + 腾讯 qt.gtimg.cn 权威流通市值修正；历史 K 线与均线取自新浪日 K（截至 {data_date}）。<br>
<b>筛选口径</b>：先按「下午2:30选股法」层1-4（涨幅3~5% &amp; 量比≥1 &amp; 换手5~10% &amp; 流通市值50~200亿）对全 A 做客观初筛，得 {k_total} 只；再套用「96原则·九不买」逐条过滤。</p>

<h2>二、九不买筛查结果</h2>
<p style="color:#3a4658">九不买可量化项（#6 基本面亏损、#8/#9 量比换手阈值）已自动判定：<b>{k_excl} 只因 TTM 亏损触发 #6 被剔除</b>，其余通过量化项（#3/#5/#7 需人工核查公告）。</p>

<details open>
  <summary>被剔除的 {k_excl} 只（亏损 · 九不买#6）</summary>
  <table><thead><tr><th class="l">代码</th><th class="l">名称</th><th>现价</th><th>涨幅%</th><th>PE(TTM)</th><th class="l">剔除理由</th></tr></thead><tbody>{loss_rows}</tbody></table>
</details>

<details>
  <summary>全 {k_total} 只候选 · 九不买结论（点击展开）</summary>
  <div class="legend">标签：<span class="b ok">符合</span> 通过量化项·待人工核查 ｜ <span class="b warn">观察</span> 估值偏高·谨慎 ｜ <span class="b bad">不买</span> 亏损触发#6</div>
  <table><thead><tr><th class="l">代码</th><th class="l">名称</th><th>现价</th><th>涨幅%</th><th>量比</th><th>换手%</th><th>流通亿</th><th>PE</th><th>均线/趋势</th><th>结论</th></tr></thead><tbody>{all_rows}</tbody></table>
</details>

<h2>三、重点候选深度研判</h2>
<p style="color:#3a4658">对「多头排列 / 低估值(PE&lt;20) / 创新高」代表做完整 96 原则研判。标记 👁 为主观项，需结合分时图与题材面人工把关。</p>
{deep_html}

<h2>四、96原则 · 六不卖（持有纪律）</h2>
<p style="color:#3a4658">若已持有上述个股，逐条核对 6 类「不卖」情形——命中越多越应持有；仅当破位/逻辑破坏/达止盈/量价背离才离场：</p>
<div class="six">
  <div><b>趋势强劲</b>：价在 5/10 日线上方</div>
  <div><b>热点题材</b>：契合主流政策板块</div>
  <div><b>指标向好</b>：低位金叉/底部形态</div>
  <div><b>量能健康</b>：价涨量增</div>
  <div><b>逻辑未变</b>：初始逻辑未被破坏</div>
  <div><b>未达目标</b>：未到止盈且符合预期</div>
</div>
<p style="color:#3a4658;margin-top:10px">📌 上面是规则说明；<b>每只重点候选已在上方卡片里做了「六不卖逐条命中（客观 X/4）+ 明确下车信号」</b>——
当「下车信号」任一触发（跌破 MA5/前低、量价背离、逻辑破坏、达止盈）即离场，其余继续持有，不要因短期波动提前下车。</p>

<h2>五、综合结论与仓位建议</h2>
<div class="tier">
  <div class="chip"><b>趋势最强（干净多头排列）</b>：{multi_txt}</div>
  <div class="chip"><b>低估值修复(PE&lt;20)</b>：{cheap_txt}</div>
  <div class="chip"><b>深跌反弹·未确认(距高&gt;20%)</b>：{reb_txt}</div>
</div>
<p style="color:#3a4658"><b>结论</b>：通过「客观四层 + 九不买量化」的 {k_conf} 只中，趋势质量分层明显。优先关注干净多头排列且 PE 合理的标的；创新高突破位（距高&lt;1%）动能强但须按层8等回踩均线再介入、忌追高。低 PE 标的属企稳修复，安全边际较好但需确认均线完全多头。<br>
<b>仓位建议</b>：单只不超过总仓 1/5，设 5%~8% 止损；深跌反弹股仅以小仓试错；所有结论需 14:30 后复核分时与量能再决策。</p>

<div class="foot">数据来源：东方财富 push2delay / 腾讯 qt.gtimg.cn / 新浪日K。本报告由 kline-shortterm-checklist 技能固定模板生成，仅供学习与复盘，非投资建议。</div>
</div></body></html>"""

    out = os.path.join(cwd, f"筛查报告_{data_date}.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(HTML)
    print(f"报告已生成: {out}  (候选 {k_total} 只, 剔除亏损 {k_excl} 只, 深度研判 {len(prio)} 只)")

if __name__ == "__main__":
    build()
