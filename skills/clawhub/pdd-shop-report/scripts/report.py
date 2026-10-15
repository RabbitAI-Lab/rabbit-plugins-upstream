#!/usr/bin/env python3
"""
pdd-shop-report v2：店铺经营报表（商务版）。

v2（创始人 2026-10-10 验收意见落地）：
  1. 后台联动：商品名/缩略图 → mms 后台单品过滤页；"需处理事项" KPI → 后台商品列表
  2. 数据质量：近30天成交额/订单数 = 平台数据中心**真实日历史**（sydney queryType=2）；
     库存为点时态快照序列（平台无库存历史），口径经 ⓘ 说明
  3. dashboard 基本功：指标 ⓘ hover 说明（健康度算法/可售天数/成交口径）；折线 hover 十字线+tooltip
  4. AI 引导：页尾给可直接对 WorkBuddy 说的一句话定制 prompt
数据色经 dataviz 验证器（#2E7D52/#A87F2E on #FBF8F2 全检通过）；品牌色仅用于标题/强调。

用法: python3 report.py [--mall <id>] [--theme clawschool|boardroom|slate] [--out report.html]
"""
import sys, os, json, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import store  # noqa: E402

MMS = "https://mms.pinduoduo.com"

THEMES = {
    "clawschool": dict(bg="#FBF8F2", card="#FFFFFF", line="#EDE6D8", text="#211810",
                       muted="#9A8A78", head="#1E3D2F", accent="#C99A3C",
                       dgreen="#2E7D52", dgold="#A87F2E",  # 数据色（验证器全检通过）
                       display='"Noto Serif SC","Songti SC",serif'),
    "boardroom": dict(bg="#FFFFFF", card="#FFFFFF", line="#E5E5E5", text="#111111",
                      muted="#737373", head="#111111", accent="#444444",
                      dgreen="#3B6E8F", dgold="#8F6A3B",
                      display='"Helvetica Neue",Arial,sans-serif'),
    "slate": dict(bg="#101418", card="#171C22", line="#262D36", text="#E8EAED",
                  muted="#8A94A0", head="#E8EAED", accent="#D4A94F",
                  dgreen="#5BA67E", dgold="#C9A35B",
                  display='"Noto Serif SC","Songti SC",serif'),
}

INFO = {
    "trade": "数据来源：拼多多后台·数据中心（交易概况）的按日官方数据，口径与后台一致。",
    "stock": "库存为同步时点的快照记录（平台不提供库存历史），每日运行 pdd-sync-shop 可积累趋势。",
    "health": ("库存健康判定规则：断货 = 库存0且近30天有销量；即将断货 = 可售天数&lt;7；"
               "积压 = 可售天数&gt;90；滞销 = 近30天销量为0；其余为健康。可售天数 = 库存 ÷ 日均销量（近30天销量÷30）。"),
    "gmv": "近30天成交额来自平台数据中心按日成交金额合计，与后台交易概况一致。",
    "dos": "可售天数 = 当前库存 ÷ 日均销量（近30天销量 ÷ 30）；近30天无销量时不计算。",
}

HEALTH_ORDER = ["断货", "即将断货", "滞销", "积压", "健康"]
NEED_ACTION = {"断货", "即将断货", "滞销", "积压"}


def info_icon(key, T):
    return (f'<span class="info" tabindex="0"><svg width="13" height="13" viewBox="0 0 16 16" fill="none" '
            f'stroke="{T["muted"]}" stroke-width="1.3"><circle cx="8" cy="8" r="6.6"/>'
            f'<path d="M8 7.2v4" stroke-linecap="round"/><circle cx="8" cy="4.9" r="0.7" fill="{T["muted"]}" stroke="none"/></svg>'
            f'<span class="tip">{INFO[key]}</span></span>')


def goods_link(goods_id):
    return f"{MMS}/goods/goods_list?goods_id={goods_id}"


def line_chart(points, color, T, unit="", cid="c0", h=150):
    """日粒度折线：网格、首末直标、hover 十字线 + tooltip（自包含内联 JS）。"""
    if len(points) < 2:
        return f'<div class="empty">数据积累中，次日即可显示趋势</div>'
    w = 560
    pad_l, pad_r, pad_t, pad_b = 16, 16, 20, 22
    vals = [p[1] for p in points]
    lo, hi = min(vals), max(vals)
    rng = (hi - lo) or 1
    xs = [pad_l + i * (w - pad_l - pad_r) / (len(vals) - 1) for i in range(len(vals))]
    ys = [pad_t + (h - pad_t - pad_b) * (1 - (v - lo) / rng) for v in vals]
    pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in zip(xs, ys))
    grid = "".join(
        f'<line x1="{pad_l}" y1="{pad_t + (h-pad_t-pad_b)*i/2:.1f}" x2="{w-pad_r}" '
        f'y2="{pad_t + (h-pad_t-pad_b)*i/2:.1f}" stroke="{T["line"]}" stroke-width="1"/>'
        for i in range(3))
    # x 轴首末日期
    d0, d1 = points[0][0][5:], points[-1][0][5:]
    data_js = json.dumps([[p[0][5:], p[1]] for p in points])
    return f"""<div class="chart" id="{cid}">
<svg viewBox="0 0 {w} {h}" width="100%" height="{h}">{grid}
<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="2" stroke-linejoin="round"/>
<circle cx="{xs[-1]:.1f}" cy="{ys[-1]:.1f}" r="3.5" fill="{color}"/>
<text x="{pad_l}" y="13" font-size="11" fill="{T['muted']}">{vals[0]:g}{unit}</text>
<text x="{w-pad_r}" y="13" font-size="11" fill="{T['muted']}" text-anchor="end">{vals[-1]:g}{unit}</text>
<text x="{pad_l}" y="{h-6}" font-size="10.5" fill="{T['muted']}">{d0}</text>
<text x="{w-pad_r}" y="{h-6}" font-size="10.5" fill="{T['muted']}" text-anchor="end">{d1}</text>
<line class="xh" x1="0" y1="{pad_t}" x2="0" y2="{h-pad_b}" stroke="{T['muted']}" stroke-width="1" stroke-dasharray="3,3" opacity="0"/>
</svg><div class="tt"></div>
<script>(function(){{var D={data_js},el=document.getElementById("{cid}"),sv=el.querySelector("svg"),
xh=el.querySelector(".xh"),tt=el.querySelector(".tt"),PL={pad_l},PR={pad_r},W={w};
sv.addEventListener("mousemove",function(e){{var r=sv.getBoundingClientRect(),
x=(e.clientX-r.left)*W/r.width,i=Math.round((x-PL)/((W-PL-PR)/(D.length-1)));
if(i<0)i=0;if(i>=D.length)i=D.length-1;var cx=PL+i*(W-PL-PR)/(D.length-1);
xh.setAttribute("x1",cx);xh.setAttribute("x2",cx);xh.setAttribute("opacity","1");
tt.textContent=D[i][0]+"　"+D[i][1].toLocaleString()+"{unit}";tt.style.opacity=1;
tt.style.left=Math.min(Math.max(cx*r.width/W-40,0),r.width-96)+"px";}});
sv.addEventListener("mouseleave",function(){{xh.setAttribute("opacity","0");tt.style.opacity=0;}});}})();</script></div>"""


def main():
    a = sys.argv
    def arg(k, d=None): return a[a.index(k) + 1] if k in a else d
    mall = arg("--mall")
    theme_name = arg("--theme", "clawschool")
    out = arg("--out", os.path.join(HERE, "..", "report.html"))
    T = THEMES.get(theme_name, THEMES["clawschool"])

    store.ensure_schema()
    goods = [g for g in store.latest_goods(mall) if g.get("is_onsale")]
    if not goods:
        print(json.dumps({"ok": False, "reason": "no_data",
                          "action": {"type": "notify_user",
                                     "message": "暂无数据：请先运行一次 pdd-sync-shop"}}, ensure_ascii=False))
        sys.exit(2)
    goods.sort(key=lambda g: -g["sold_quantity_30d"])
    mall_id = goods[0]["mall_id"]
    daily = store.shop_daily_series(mall)          # 平台真实日历史
    snaps = store.snapshot_series(mall)            # 快照序列（库存）
    as_of = max(g["collected_at"] for g in goods)

    n = len(goods)
    stock = sum(g["quantity"] for g in goods)
    if daily:
        amt30 = sum(d["pay_amt"] for d in daily)
        cnt30 = sum(d["pay_cnt"] for d in daily)
    else:
        amt30, cnt30 = 0, sum(g["sold_quantity_30d"] for g in goods)
    health = {}
    for g in goods:
        health[g["stock_health"]] = health.get(g["stock_health"], 0) + 1
    actions = [g for g in goods if g["stock_health"] in NEED_ACTION]

    kpis = [
        ("在售商品", f"{n}", None, None),
        ("总库存", f"{stock:,}", None, None),
        ("近30天订单", f"{cnt30:,}", "trade", None),
        ("近30天成交额", f"¥{amt30:,.0f}", "gmv", None),
        ("需处理事项", f"{len(actions)}", None, f"{MMS}/goods/goods_list"),
    ]
    kpi_html = ""
    for k, v, ikey, href in kpis:
        inner = (f'<div class="v">{v}</div><div class="l">{k}'
                 + (info_icon(ikey, T) if ikey else "") + "</div>")
        kpi_html += (f'<a class="kpi klink" href="{href}" target="_blank" rel="noopener">{inner}'
                     f'<div class="go">去后台处理 ↗</div></a>') if href else f'<div class="kpi">{inner}</div>'

    trade_amt = line_chart([(d["state_date"], round(d["pay_amt"])) for d in daily],
                           T["dgold"], T, unit="元", cid="c-amt") if daily else \
        '<div class="empty">平台日交易数据将在下次同步时拉取</div>'
    trade_cnt = line_chart([(d["state_date"], d["pay_cnt"]) for d in daily],
                           T["dgreen"], T, unit="单", cid="c-cnt") if daily else \
        '<div class="empty">平台日交易数据将在下次同步时拉取</div>'
    stock_tr = line_chart([(r["t"], r["q"]) for r in snaps], T["dgreen"], T,
                          unit="件", cid="c-stk", h=120)

    seg = "".join(
        f'<div class="seg" style="flex:{health.get(h,0)};'
        f'background:{T["dgold"] if h in NEED_ACTION else T["dgreen"]};'
        f'opacity:{0.95 if h in NEED_ACTION else 0.3}" title="{h} {health.get(h,0)} 款"></div>'
        for h in HEALTH_ORDER if health.get(h, 0))
    legend = "　".join(f"{h} {health.get(h,0)}" for h in HEALTH_ORDER if health.get(h, 0))

    def gcell(g):
        return (f'<a class="glink" href="{goods_link(g["goods_id"])}" target="_blank" rel="noopener">'
                f'<img src="{g["thumb_url"]}" loading="lazy" alt="">'
                f'<span>{g["goods_name"][:24]}</span></a>')

    act_rows = "".join(
        f'<tr><td class="tag">{g["stock_health"]}</td><td class="name">{gcell(g)}</td>'
        f'<td class="num">¥{g["group_price_min_yuan"]}</td><td class="num">{g["quantity"]}</td>'
        f'<td class="num">{g["sold_quantity_30d"]}</td><td class="advice">{_advice(g)}</td></tr>'
        for g in actions) or '<tr><td colspan="6" class="advice">当前库存与动销状态正常，无需处理。</td></tr>'

    import time as _t
    ev_by_goods = {}
    for e in store.commit_events(mall_id=mall_id, days=30):
        ev_by_goods.setdefault(e["goods_id"], []).append(e["submit_time"])
    detail_rows = ""
    for g in goods:
        tr = store.goods_trend(g["goods_id"], 30)
        evs = ev_by_goods.get(g["goods_id"], [])
        spark = _spark(tr, evs, T["dgreen"], T["accent"])
        last_edit = ""
        if evs:
            dd = int((_t.time() - max(evs)) / 86400)
            last_edit = (f'<div class="edit">改动 {dd}天前'
                         + (f' · {len(evs)}次' if len(evs) > 1 else '') + '</div>')
        dos = "—" if g["days_of_stock"] is None else f'{g["days_of_stock"]:g}'
        detail_rows += (f'<tr><td class="name">{gcell(g)}</td>'
                        f'<td class="num">¥{g["group_price_min_yuan"]}</td><td>{spark}{last_edit}</td>'
                        f'<td class="num">{g["quantity"]}</td><td class="num">{g["sold_quantity_30d"]}</td>'
                        f'<td class="num">{g["daily_sales_30d"]:g}</td><td class="num">{dos}</td>'
                        f'<td class="tag">{g["stock_health"]}</td></tr>')

    prompts = ["把报表换成深色主题再生成一次", "只看滞销商品，给我清仓方案",
               "把近7天和近30天成交放在一起对比", "每天早上 9 点自动生成这份报表发给我"]
    prompt_html = "".join(f'<span class="p">“{p}”</span>' for p in prompts)

    gen_at = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    preview_tag = "" if theme_name == "clawschool" else f'<span class="preview">主题 {theme_name} · 内部预览</span>'

    html = f"""<!doctype html><html lang="zh"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>店铺经营报表 · {as_of[:10]}</title>
<style>
body{{margin:0;background:{T['bg']};color:{T['text']};font:14px/1.6 "Noto Sans SC","PingFang SC",-apple-system,sans-serif}}
.wrap{{max-width:1060px;margin:0 auto;padding:40px 28px}}
a{{color:inherit;text-decoration:none}}
.hd{{border-bottom:2px solid {T['head']};padding-bottom:18px;margin-bottom:26px;display:flex;justify-content:space-between;align-items:flex-end}}
h1{{font-family:{T['display']};font-size:26px;font-weight:700;color:{T['head']};margin:0}}
.hd .meta{{font-size:12.5px;color:{T['muted']};text-align:right}}
.hd .meta a{{border-bottom:1px dotted {T['muted']}}}
.preview{{display:inline-block;font-size:11px;color:{T['accent']};border:1px solid {T['accent']};border-radius:3px;padding:1px 6px;margin-left:8px}}
.kpis{{display:grid;grid-template-columns:repeat(5,1fr);gap:1px;background:{T['line']};border:1px solid {T['line']};margin-bottom:26px}}
.kpi{{background:{T['card']};padding:16px 18px;position:relative}}
.kpi .v{{font-size:25px;font-weight:700;color:{T['head']};font-variant-numeric:tabular-nums}}
.kpi .l{{font-size:12px;color:{T['muted']};margin-top:4px;letter-spacing:.05em}}
.klink .go{{font-size:11px;color:{T['accent']};margin-top:6px;opacity:0;transition:opacity .15s}}
.klink:hover .go{{opacity:1}}
.klink:hover{{outline:1px solid {T['accent']}}}
h2{{font-family:{T['display']};font-size:16px;color:{T['head']};margin:32px 0 12px;padding-left:10px;border-left:3px solid {T['accent']};display:flex;align-items:center;gap:6px}}
.grid2{{display:grid;grid-template-columns:1fr 1fr;gap:22px}}
.panel{{background:{T['card']};border:1px solid {T['line']};padding:14px 18px}}
.panel .t{{font-size:12.5px;color:{T['muted']};margin-bottom:4px;display:flex;align-items:center;gap:5px}}
.chart{{position:relative}}
.tt{{position:absolute;top:2px;background:{T['head']};color:#fff;font-size:11.5px;padding:3px 8px;border-radius:3px;opacity:0;pointer-events:none;white-space:nowrap;transition:opacity .1s}}
.empty{{color:{T['muted']};font-size:12.5px;padding:28px 0;text-align:center}}
.info{{position:relative;display:inline-flex;margin-left:3px;cursor:help;vertical-align:-2px}}
.info .tip{{position:absolute;bottom:130%;left:-8px;z-index:9;width:300px;background:{T['head']};color:#fff;font-size:12px;line-height:1.55;font-weight:400;padding:9px 11px;border-radius:4px;opacity:0;visibility:hidden;transition:opacity .12s;pointer-events:none}}
.info:hover .tip,.info:focus .tip{{opacity:1;visibility:visible}}
.healthbar{{display:flex;height:14px;border:1px solid {T['line']};overflow:hidden}}
.seg{{border-right:1px solid {T['bg']}}}
.legend{{font-size:12.5px;color:{T['muted']};margin-top:8px}}
table{{width:100%;border-collapse:collapse;background:{T['card']};border:1px solid {T['line']};font-size:13px}}
th{{text-align:left;font-weight:500;font-size:12px;color:{T['muted']};border-bottom:1px solid {T['line']};padding:10px 12px;letter-spacing:.04em}}
td{{padding:8px 12px;border-bottom:1px solid {T['line']};vertical-align:middle}}
tr:last-child td{{border-bottom:none}}
.num{{text-align:right;font-variant-numeric:tabular-nums}}
.name{{max-width:280px}}
.glink{{display:flex;align-items:center;gap:9px}}
.glink img{{width:34px;height:34px;border-radius:5px;object-fit:cover;border:1px solid {T['line']};flex:none}}
.glink span{{border-bottom:1px dotted transparent;line-height:1.4}}
.glink:hover span{{border-bottom-color:{T['accent']};color:{T['head']}}}
.tag{{color:{T['accent']};font-size:12.5px;white-space:nowrap}}
.advice{{color:{T['muted']};font-size:12.5px}}
.edit{{font-size:10.5px;color:{T['accent']};margin-top:2px}}
.ai{{margin-top:34px;border:1px dashed {T['accent']};background:{T['card']};padding:14px 18px}}
.ai .t{{font-size:12.5px;color:{T['head']};font-weight:600;margin-bottom:8px}}
.ai .p{{display:inline-block;font-size:12.5px;color:{T['muted']};border:1px solid {T['line']};border-radius:999px;padding:4px 12px;margin:0 8px 6px 0}}
.ft{{margin-top:26px;padding-top:14px;border-top:1px solid {T['line']};font-size:12px;color:{T['muted']};display:flex;justify-content:space-between}}
@media(max-width:760px){{.kpis{{grid-template-columns:repeat(2,1fr)}}.grid2{{grid-template-columns:1fr}}}}
</style></head><body><div class="wrap">
<div class="hd"><h1>店铺经营报表{preview_tag}</h1>
<div class="meta"><a href="{MMS}/home" target="_blank" rel="noopener">店铺 {mall_id} ↗</a><br>数据截至 {as_of} UTC</div></div>
<div class="kpis">{kpi_html}</div>
<div class="grid2">
  <div class="panel"><div class="t">近30天成交额（元）{info_icon("trade", T)}</div>{trade_amt}</div>
  <div class="panel"><div class="t">近30天订单量（单）{info_icon("trade", T)}</div>{trade_cnt}</div>
</div>
<div class="grid2" style="margin-top:22px">
  <div class="panel"><div class="t">总库存走势{info_icon("stock", T)}</div>{stock_tr}</div>
  <div class="panel"><div class="t">库存健康{info_icon("health", T)}</div>
    <div class="healthbar" style="margin-top:14px">{seg}</div><div class="legend">{legend}</div></div>
</div>
<h2>待处理事项</h2>
<table><thead><tr><th>状态</th><th>商品（点击直达后台）</th><th style="text-align:right">拼单价</th>
<th style="text-align:right">库存</th><th style="text-align:right">30天销</th><th>建议</th></tr></thead>
<tbody>{act_rows}</tbody></table>
<h2>商品明细</h2>
<table><thead><tr><th>商品（点击直达后台）</th><th style="text-align:right">拼单价</th><th>价格走势</th>
<th style="text-align:right">库存</th><th style="text-align:right">30天销</th>
<th style="text-align:right">日均</th><th style="text-align:right">可售天数{info_icon("dos", T)}</th><th>状态</th></tr></thead>
<tbody>{detail_rows}</tbody></table>
<div class="ai"><div class="t">这份报表可以继续定制 — 直接对 WorkBuddy 说：</div>{prompt_html}</div>
<div class="ft"><span>数据来源：拼多多后台数据中心（日交易）+ 同步快照（pdd-sync-shop）</span>
<span>生成于 {gen_at} · <a href="https://claw-school.com?utm_source=skill&utm_medium=report" style="color:inherit;text-decoration:underline;text-underline-offset:2px" target="_blank" rel="noopener">Claw School 龙虾学院</a> 商家自动化</span></div>
</div></body></html>"""

    out = os.path.abspath(out)
    open(out, "w").write(html)
    print(json.dumps({"ok": True, "report": out, "theme": theme_name, "as_of": as_of,
                      "goods": n, "daily_days": len(daily), "actions_needed": len(actions)},
                     ensure_ascii=False))


def _epoch(ts):
    try:
        return datetime.datetime.strptime(ts[:19], "%Y-%m-%d %H:%M:%S").replace(
            tzinfo=datetime.timezone.utc).timestamp()
    except Exception:
        return None


def _spark(tr, events, color, mark_color, w=110, h=22):
    """价格火花线 + 改动事件竖线标记。tr=[{t, price_yuan}]，events=[epoch,...]"""
    vals = [t["price_yuan"] for t in tr]
    if len(vals) < 2:
        return (f'<svg width="{w}" height="{h}"><line x1="2" y1="{h/2}" x2="{w-2}" y2="{h/2}" '
                f'stroke="{color}" stroke-width="1.5" opacity="0.5"/></svg>')
    times = [_epoch(t["t"]) for t in tr]
    t0, t1 = times[0], times[-1]
    lo, hi = min(vals), max(vals)
    span = (hi - lo) or 1
    xs = [2 + i * (w - 4) / (len(vals) - 1) for i in range(len(vals))]
    ys = [h - 3 - (v - lo) / span * (h - 6) for v in vals]
    pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in zip(xs, ys))
    ticks = ""
    if t0 and t1 and t1 > t0:
        seen = set()
        for e in events:
            if e < t0 or e > t1:
                continue
            x = 2 + (e - t0) / (t1 - t0) * (w - 4)
            xr = round(x)
            if xr in seen:
                continue
            seen.add(xr)
            ticks += (f'<line x1="{x:.1f}" y1="1" x2="{x:.1f}" y2="{h-1}" '
                      f'stroke="{mark_color}" stroke-width="1" opacity="0.7"/>')
    title = f"¥{lo:g} – ¥{hi:g}" + ("　竖线=改动" if ticks else "")
    return (f'<svg width="{w}" height="{h}"><title>{title}</title>{ticks}'
            f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="1.5"/></svg>')


def _advice(g):
    h = g["stock_health"]
    if h == "断货":
        return f"尽快补货，建议 {max(1, round(g['daily_sales_30d']*44))} 件"
    if h == "即将断货":
        need = max(1, round(g["daily_sales_30d"] * 44 - g["quantity"]))
        return f"剩约 {g['days_of_stock']:g} 天可售，建议补 {need} 件"
    if h == "积压":
        return f"可售约 {g['days_of_stock']:g} 天，建议促销或暂停补货"
    return "近30天无销量，建议调价或参加活动"


# ---------------- 店群驾驶舱（多店合并） ----------------

def _shop_labels():
    """注册表 ~/.pdd-data/shops.yaml 的 mall_id → 显示名（自包含解析，无跨技能依赖）。"""
    import re as _re
    path = os.path.expanduser(os.environ.get("PDD_DATA_DIR", "~/.pdd-data") + "/shops.yaml")
    labels = {}
    try:
        cur = None
        for ln in open(path, encoding="utf-8"):
            m = _re.match(r"\s*- name:\s*(\S+)", ln)
            if m:
                cur = {"name": m.group(1)}
                continue
            m = _re.match(r"\s*(label|mall_id):\s*(.+)", ln)
            if m and cur is not None:
                cur[m.group(1)] = m.group(2).strip()
                if m.group(1) == "mall_id":
                    try:
                        labels[int(cur[m.group(1)])] = cur.get("label") or cur["name"]
                    except ValueError:
                        pass
    except Exception:
        pass
    return labels


def cockpit(theme_name="clawschool", out=None):
    """店群驾驶舱：N 家店铺一屏对比 + 全店待办汇总。数据来自本地库（先跑 pdd-sync-shop --all）。"""
    T = THEMES.get(theme_name, THEMES["clawschool"])
    out = out or os.path.join(HERE, "..", "cockpit.html")
    labels = _shop_labels()
    malls = store.known_malls()
    if not malls:
        print(json.dumps({"ok": False, "reason": "no_data",
                          "action": {"type": "notify_user",
                                     "message": "暂无数据：请先运行 pdd-sync-shop 采集（多店：--all）"}},
                         ensure_ascii=False))
        sys.exit(2)

    shops = []
    for mid in malls:
        goods = [g for g in store.latest_goods(mid) if g.get("is_onsale")]
        daily = store.shop_daily_series(mid)
        amt30 = sum(d["pay_amt"] for d in daily)
        cnt30 = sum(d["pay_cnt"] for d in daily)
        health = {}
        for g in goods:
            health[g["stock_health"]] = health.get(g["stock_health"], 0) + 1
        acts = [g for g in goods if g["stock_health"] in NEED_ACTION]
        as_of = max((g["collected_at"] for g in goods), default="")
        shops.append({"mall_id": mid, "label": labels.get(mid, f"店铺 {mid}"), "goods": goods,
                      "amt30": amt30, "cnt30": cnt30, "health": health, "acts": acts,
                      "stock": sum(g["quantity"] for g in goods), "as_of": as_of})
    shops.sort(key=lambda s: -s["amt30"])

    n_shops = len(shops)
    tot_amt = sum(s["amt30"] for s in shops)
    tot_cnt = sum(s["cnt30"] for s in shops)
    tot_goods = sum(len(s["goods"]) for s in shops)
    tot_acts = sum(len(s["acts"]) for s in shops)

    kpis = [("店铺数", f"{n_shops}", None),
            ("全店GMV·30天", f"¥{tot_amt:,.0f}", "gmv"),
            ("全店订单·30天", f"{tot_cnt:,}", "trade"),
            ("在售商品", f"{tot_goods}", None),
            ("需处理事项", f"{tot_acts}", "health")]
    kpi_html = "".join(f'<div class="kpi"><div class="v">{v}</div>'
                       f'<div class="l">{k}' + (info_icon(i, T) if i else "") + "</div></div>"
                       for k, v, i in kpis)

    def hbar(health):
        return ('<div class="healthbar" style="height:10px">'
                + "".join(f'<div class="seg" style="flex:{health.get(h,0)};'
                          f'background:{T["dgold"] if h in NEED_ACTION else T["dgreen"]};'
                          f'opacity:{0.95 if h in NEED_ACTION else 0.3}"></div>'
                          for h in HEALTH_ORDER if health.get(h, 0)) + "</div>")

    shop_rows = "".join(
        f'<tr><td class="name"><b>{s["label"]}</b><div class="edit">{s["mall_id"]} · 同步于 {s["as_of"][:16] if s["as_of"] else "—"}</div></td>'
        f'<td class="num">¥{s["amt30"]:,.0f}</td><td class="num">{s["cnt30"]:,}</td>'
        f'<td class="num">{len(s["goods"])}</td><td class="num">{s["stock"]:,}</td>'
        f'<td class="num" style="color:{T["accent"] if s["acts"] else T["muted"]}">{len(s["acts"])}</td>'
        f'<td>{hbar(s["health"])}</td></tr>'
        for s in shops)

    act_rows = ""
    for s in shops:
        for g in sorted(s["acts"], key=lambda g: -g["sold_quantity_30d"])[:6]:
            act_rows += (f'<tr><td class="tag">{s["label"]}</td><td class="tag">{g["stock_health"]}</td>'
                         f'<td class="name">{g["goods_name"][:30]}</td>'
                         f'<td class="num">¥{g["group_price_min_yuan"]}</td><td class="num">{g["quantity"]}</td>'
                         f'<td class="advice">{_advice(g)}</td></tr>')
    act_rows = act_rows or '<tr><td colspan="6" class="advice">全部店铺库存与动销正常，无需处理。</td></tr>'

    prompts = ["店铺按 GMV 排序生成每家店的完整报表", "哪家的需处理事项最多，先给我它的滞销清单",
               "把全店近30天 GMV 画成一张趋势图", "每天早上 9 点同步全部店铺并出驾驶舱"]
    prompt_html = "".join(f'<span class="p">“{p}”</span>' for p in prompts)

    gen_at = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    html = f"""<!doctype html><html lang="zh"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>店群驾驶舱 · {n_shops} 家店铺</title>
<style>
body{{margin:0;background:{T['bg']};color:{T['text']};font:14px/1.6 "Noto Sans SC","PingFang SC",-apple-system,sans-serif}}
.wrap{{max-width:1060px;margin:0 auto;padding:40px 28px}}
a{{color:inherit;text-decoration:none}}
.hd{{border-bottom:2px solid {T['head']};padding-bottom:18px;margin-bottom:26px;display:flex;justify-content:space-between;align-items:flex-end}}
h1{{font-family:{T['display']};font-size:26px;font-weight:700;color:{T['head']};margin:0}}
.hd .meta{{font-size:12.5px;color:{T['muted']};text-align:right}}
.kpis{{display:grid;grid-template-columns:repeat(5,1fr);gap:1px;background:{T['line']};border:1px solid {T['line']};margin-bottom:26px}}
.kpi{{background:{T['card']};padding:16px 18px}}
.kpi .v{{font-size:25px;font-weight:700;color:{T['head']};font-variant-numeric:tabular-nums}}
.kpi .l{{font-size:12px;color:{T['muted']};margin-top:4px;letter-spacing:.05em}}
h2{{font-family:{T['display']};font-size:16px;color:{T['head']};margin:32px 0 12px;padding-left:10px;border-left:3px solid {T['accent']};display:flex;align-items:center;gap:6px}}
table{{width:100%;border-collapse:collapse;background:{T['card']};border:1px solid {T['line']};font-size:13px}}
th{{text-align:left;font-weight:500;font-size:12px;color:{T['muted']};border-bottom:1px solid {T['line']};padding:10px 12px;letter-spacing:.04em}}
th.num{{text-align:right}}
td{{padding:9px 12px;border-bottom:1px solid {T['line']};vertical-align:middle}}
tr:last-child td{{border-bottom:none}}
.num{{text-align:right;font-variant-numeric:tabular-nums}}
.name{{max-width:300px}}
.tag{{color:{T['accent']};font-size:12.5px;white-space:nowrap}}
.advice{{color:{T['muted']};font-size:12.5px}}
.edit{{font-size:10.5px;color:{T['muted']};margin-top:2px}}
.healthbar{{display:flex;height:14px;border:1px solid {T['line']};overflow:hidden;min-width:120px}}
.seg{{border-right:1px solid {T['bg']}}}
.info{{position:relative;display:inline-flex;margin-left:3px;cursor:help;vertical-align:-2px}}
.info .tip{{position:absolute;bottom:130%;left:-8px;z-index:9;width:300px;background:{T['head']};color:#fff;font-size:12px;line-height:1.55;font-weight:400;padding:9px 11px;border-radius:4px;opacity:0;visibility:hidden;transition:opacity .12s;pointer-events:none}}
.info:hover .tip,.info:focus .tip{{opacity:1;visibility:visible}}
.ai{{margin-top:34px;border:1px dashed {T['accent']};background:{T['card']};padding:14px 18px}}
.ai .t{{font-size:12.5px;color:{T['head']};font-weight:600;margin-bottom:8px}}
.ai .p{{display:inline-block;font-size:12.5px;color:{T['muted']};border:1px solid {T['line']};border-radius:999px;padding:4px 12px;margin:0 8px 6px 0}}
.ft{{margin-top:26px;padding-top:14px;border-top:1px solid {T['line']};font-size:12px;color:{T['muted']};display:flex;justify-content:space-between}}
@media(max-width:760px){{.kpis{{grid-template-columns:repeat(2,1fr)}}}}
</style></head><body><div class="wrap">
<div class="hd"><h1>店群驾驶舱</h1>
<div class="meta">{n_shops} 家店铺 · 数据截至 {max(s["as_of"] for s in shops if s["as_of"])[:16] if any(s["as_of"] for s in shops) else "—"} UTC</div></div>
<div class="kpis">{kpi_html}</div>
<h2>各店对比（按 GMV·30天排序）</h2>
<table><thead><tr><th>店铺</th><th class="num">GMV·30天</th><th class="num">订单·30天</th>
<th class="num">在售</th><th class="num">库存</th><th class="num">需处理</th><th>库存健康分布</th></tr></thead>
<tbody>{shop_rows}</tbody></table>
<h2>全店待处理事项（每店 Top 6）</h2>
<table><thead><tr><th>店铺</th><th>状态</th><th>商品</th>
<th class="num">拼单价</th><th class="num">库存</th><th>建议</th></tr></thead>
<tbody>{act_rows}</tbody></table>
<div class="ai"><div class="t">这份驾驶舱可以继续定制 — 直接对 WorkBuddy 说：</div>{prompt_html}</div>
<div class="ft"><span>数据来源：各店同步快照 + 平台日交易（pdd-sync-shop --all 采集）</span>
<span>生成于 {gen_at} · <a href="https://claw-school.com?utm_source=skill&utm_medium=report" style="color:inherit;text-decoration:underline;text-underline-offset:2px" target="_blank" rel="noopener">Claw School 龙虾学院</a> 商家自动化</span></div>
</div></body></html>"""

    out = os.path.abspath(out)
    open(out, "w").write(html)
    print(json.dumps({"ok": True, "report": out, "mode": "cockpit", "shops": n_shops,
                      "total_gmv30": round(tot_amt), "actions_needed": tot_acts},
                     ensure_ascii=False))


if __name__ == "__main__":
    if "--cockpit" in sys.argv or "--all" in sys.argv:
        a = sys.argv
        cockpit(theme_name=a[a.index("--theme") + 1] if "--theme" in a else "clawschool",
                out=a[a.index("--out") + 1] if "--out" in a else None)
    else:
        main()
