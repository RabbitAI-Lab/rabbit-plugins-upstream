# -*- coding: utf-8 -*-
"""Reusable poster-style A4 briefing builder for 财富管理 innovation briefings.

USAGE (in a per-run build script, e.g. build_20260728.py):
    import sys, os
    sys.path.insert(0, os.path.dirname(__file__))
    import build_briefing_template as tpl
    from content_20260728 import DIRECTIONS, EXTRA
    tpl.today = "2026年7月28日"
    tpl.DIRECTIONS = DIRECTIONS
    tpl.EXTRA = EXTRA
    tpl.SUMMARY_LEAD = "三条主线摘要……"
    tpl.build()

Only override the four globals (today / DIRECTIONS / EXTRA / SUMMARY_LEAD).
Do NOT rewrite the CSS or the layout functions.
"""
from html import escape

# ---- overridable globals (set these from the per-run build script) ----
today = "2026年7月"
DIRECTIONS = []
EXTRA = {}
SUMMARY_LEAD = (
    "本月，私人银行与财富管理领域围绕“权益科技化、产品货架化、"
    "服务场景化、配置多元化”加速创新。银行借记卡/信用卡从餐饮出行积分转向AI算力Token；"
    "理财子公司以“固收+科技”与科创股权理财承接存款替代资金；"
    "个人养老金基金扩容，银行“研选/慧投/严选”品牌成为公募产品货架化主阵地；"
    "私募定投服务落地，多资产多策略成为高净值客户新共识；"
    "银保协同升级为养老社区场景与保单检视服务；"
    "信托从财富管理延伸至生命照护与家企隔离。"
)

def esc(s):
    return escape(str(s))

CSS = """
@page { size: A4; margin: 0; }
* { box-sizing: border-box; }
body { margin: 0; padding: 0; font-family: "Microsoft YaHei", "PingFang SC", sans-serif; color: #1a1a1a; font-size: 10.5pt; line-height: 1.6; }
.kai { font-family: "KaiTi", "STKaiti", serif; }
.page { width: 210mm; height: 297mm; position: relative; overflow: hidden; page-break-after: always; }
.page:last-child { page-break-after: auto; }

/* 封面 */
.cover { padding: 20mm 18mm; display: flex; flex-direction: column; justify-content: space-between; background: linear-gradient(155deg, #081426 0%, #0f2242 45%, #183866 100%); color: #fff; }
.cover-top { border-bottom: 1px solid rgba(255,255,255,0.22); padding-bottom: 6mm; }
.cover-label { font-size: 10.5pt; letter-spacing: 3px; color: rgba(255,255,255,0.72); }
.cover-mid { flex: 1; display: flex; flex-direction: column; justify-content: center; padding-left: 7mm; border-left: 5px solid #d95c28; margin: 16mm 0 18mm; }
.cover-title { font-size: 46pt; line-height: 1.1; margin-bottom: 7mm; }
.cover-sub { font-size: 15pt; color: rgba(255,255,255,0.9); line-height: 1.55; }
.cover-bottom { display: flex; justify-content: space-between; align-items: flex-end; font-size: 10.5pt; color: rgba(255,255,255,0.7); }
.cover-line { width: 55mm; height: 2px; background: #d95c28; margin-bottom: 4mm; }

/* 摘要页 */
.summary { padding: 13mm 15mm; background: #fff; }
.sum-head { display: flex; align-items: center; margin-bottom: 8mm; }
.sum-bar { width: 4px; height: 12mm; background: #d95c28; margin-right: 4mm; }
.sum-title { font-size: 24pt; color: #0a1a33; }
.sum-lead { font-size: 10.5pt; color: #444; line-height: 1.7; margin-bottom: 8mm; }
.sum-grid { display: flex; flex-wrap: wrap; gap: 4.5mm; }
.sum-card { width: calc(50% - 2.25mm); background: #f8f9fb; border: 1px solid #e4e6eb; border-radius: 3mm; padding: 4.5mm 5mm; }
.sum-card h3 { font-size: 12pt; color: #0a1a33; margin: 0 0 2.5mm 0; line-height: 1.3; }
.sum-card p { font-size: 9pt; color: #555; margin: 0; line-height: 1.5; }
.sum-tags { margin-top: 2.5mm; }
.sum-tags span { display: inline-block; font-size: 7.5pt; color: #d95c28; background: rgba(217,92,40,0.08); padding: 0.8mm 2mm; border-radius: 1.5mm; margin-right: 1.5mm; margin-bottom: 1.5mm; }
.sum-foot { margin-top: 7mm; padding: 4mm 5mm; background: #0a1a33; color: #fff; border-radius: 2.5mm; display: flex; justify-content: space-around; align-items: center; font-size: 9.5pt; }

/* 方向导读页 */
.dir-page { padding: 0; display: flex; flex-direction: column; background: #fff; }
.dir-head { background: #0a1a33; color: #fff; padding: 12mm 15mm 9mm; }
.dir-no { font-size: 10pt; color: #d95c28; letter-spacing: 2px; margin-bottom: 2mm; font-weight: bold; }
.dir-title { font-size: 24pt; line-height: 1.2; margin-bottom: 3mm; }
.dir-sub { font-size: 10.5pt; color: rgba(255,255,255,0.82); line-height: 1.5; }
.dir-body { flex: 1; padding: 8mm 15mm 11mm; display: flex; flex-direction: column; gap: 5mm; }
.dir-sec-title { font-size: 11pt; color: #0a1a33; font-weight: bold; border-left: 3px solid #d95c28; padding-left: 2.5mm; margin-bottom: 2mm; }
.dir-list { margin: 0; padding: 0; list-style: none; }
.dir-list li { display: flex; align-items: flex-start; font-size: 9.5pt; line-height: 1.55; padding: 2.2mm 0; border-bottom: 1px dashed #ddd; }
.dir-list li:last-child { border-bottom: none; }
.dir-list .num { min-width: 7mm; color: #d95c28; font-weight: bold; margin-right: 2.5mm; }
.dir-list .tit { color: #0a1a33; font-weight: bold; min-width: 58mm; margin-right: 2.5mm; }
.dir-list .desc { color: #555; flex: 1; }
.dir-bottom { display: flex; gap: 5mm; margin-top: auto; }
.dir-col { flex: 1; background: #f5f7fa; border-radius: 2.5mm; padding: 4mm 5mm; }
.dir-col .dir-sec-title { margin-bottom: 2.5mm; }
.dir-tags { display: flex; flex-wrap: wrap; gap: 1.5mm; }
.dir-tags span { background: #fff; border: 1px solid #d95c28; color: #d95c28; padding: 1mm 2.5mm; border-radius: 1.5mm; font-size: 8.5pt; }
.dir-learn { font-size: 9.5pt; color: #333; line-height: 1.6; }

/* 案例页 */
.item-page { padding: 9mm 13mm 10mm; background: #f5f7fa; }
.item-head { display: flex; justify-content: space-between; align-items: center; margin-bottom: 4mm; padding-bottom: 2mm; border-bottom: 1.5px solid #d95c28; }
.item-head .dir { font-size: 11pt; color: #0a1a33; font-weight: bold; }
.item-head .pg { font-size: 8.5pt; color: #777; }
.item-cards { display: flex; flex-direction: column; gap: 3.5mm; }
.card { background: #fff; border-radius: 2.5mm; border: 1px solid #e0e3e8; overflow: hidden; height: 90mm; display: flex; flex-direction: column; }
.card-hd { background: #0a1a33; color: #fff; padding: 1.8mm 3.5mm; display: flex; justify-content: space-between; align-items: center; font-size: 8.5pt; }
.card-hd .no { font-weight: bold; color: #d95c28; }
.card-inner { padding: 3.5mm 4.5mm; flex: 1; display: flex; flex-direction: column; }
.card-title { font-size: 12.5pt; color: #0a1a33; line-height: 1.25; margin-bottom: 1.2mm; }
.card-source { font-size: 7.5pt; color: #888; margin-bottom: 1.5mm; line-height: 1.35; }
.card-source a { color: #d95c28; text-decoration: none; word-break: break-all; }
.card-body { font-size: 9pt; color: #333; line-height: 1.5; margin-bottom: 2mm; flex: 1; overflow: hidden; }
.card-foot { display: flex; gap: 2.5mm; }
.box { flex: 1; background: #f8f9fb; border-radius: 1.5mm; padding: 2mm 2.5mm; font-size: 8pt; line-height: 1.4; border-left: 2px solid #d95c28; }
.box b { color: #0a1a33; display: block; margin-bottom: 0.6mm; }
.box.learn { border-left-color: #0a1a33; }
.card-sum { background: #0a1a33; color: #fff; border-radius: 2.5mm; padding: 4mm 5mm; height: 90mm; display: flex; flex-direction: column; }
.card-sum .sum-title { font-size: 13pt; color: #d95c28; margin-bottom: 3mm; }
.card-sum .sum-body { font-size: 9.5pt; line-height: 1.55; flex: 1; overflow: hidden; }
.card-sum .sum-foot2 { margin-top: 2mm; padding-top: 2mm; border-top: 1px solid rgba(255,255,255,0.2); font-size: 8.5pt; line-height: 1.45; color: rgba(255,255,255,0.85); }
"""

def cover_html():
    return f'''
<div class="page cover">
  <div class="cover-top"><span class="cover-label">FINANCIAL INNOVATION BRIEFING</span></div>
  <div class="cover-mid">
    <div class="cover-title kai">金融创新简报</div>
    <div class="cover-sub">财富管理 · 产品权益场景创新动态<br>私人银行 · 存款理财 · 公募私募 · 银保 · 信托</div>
  </div>
  <div class="cover-bottom">
    <div><div class="cover-line"></div>某股份制银行财富管理参考</div>
    <div>{esc(today)}</div>
  </div>
</div>
'''

def summary_html():
    cards = ""
    for idx, d in enumerate(DIRECTIONS, 1):
        extra = EXTRA.get(d['title'], {})
        tags = extra.get('tags', [])[:4]
        cards += f'''
<div class="sum-card">
  <h3 class="kai">方向 {idx:02d} · {esc(d['title'].split('：')[0])}</h3>
  <p>{esc(d['subtitle'])}</p>
  <div class="sum-tags">{''.join(f'<span>{esc(t)}</span>' for t in tags)}</div>
</div>
'''
    return f'''
<div class="page summary">
  <div class="sum-head"><div class="sum-bar"></div><div class="sum-title kai">本期摘要</div></div>
  <div class="sum-lead">{esc(SUMMARY_LEAD)}</div>
  <div class="sum-grid">{cards}</div>
  <div class="sum-foot">
    <div><b style="color:#d95c28;">6</b> 大方向</div>
    <div><b style="color:#d95c28;">30</b> 条案例</div>
    <div><b style="color:#d95c28;">4</b> 大品类</div>
    <div>来源：公开新闻 / 年报 / 监管公告</div>
  </div>
</div>
'''

def direction_page_html(idx, d):
    extra = EXTRA.get(d['title'], {})
    list_html = ""
    for i, it in enumerate(d['items'], 1):
        short = it['body'][:60] + "…" if len(it['body']) > 60 else it['body']
        list_html += f'<li><span class="num">{i:02d}</span><span class="tit">{esc(it["title"])}</span><span class="desc">{esc(short)}</span></li>'
    return f'''
<div class="page dir-page">
  <div class="dir-head">
    <div class="dir-no">方向 {idx:02d} / 06</div>
    <div class="dir-title kai">{esc(d['title'])}</div>
    <div class="dir-sub">{esc(d['subtitle'])}</div>
  </div>
  <div class="dir-body">
    <div>
      <div class="dir-sec-title">本方向 5 条创新动态</div>
      <ul class="dir-list">{list_html}</ul>
    </div>
    <div class="dir-bottom">
      <div class="dir-col">
        <div class="dir-sec-title">关键趋势</div>
        <div class="dir-tags">{''.join(f'<span>{esc(t)}</span>' for t in extra.get('tags', []))}</div>
      </div>
      <div class="dir-col">
        <div class="dir-sec-title">核心洞察</div>
        <div class="dir-learn">{esc(extra.get('insight', ''))}</div>
      </div>
    </div>
    <div class="dir-action" style="background:#d95c28;color:#fff;border-radius:2.5mm;padding:3mm 5mm;font-size:9.5pt;line-height:1.55;">
      <b>银行行动建议：</b>{esc(extra.get('action', ''))}
    </div>
  </div>
</div>
'''

def item_card_html(it, gi):
    return f'''
<div class="card">
  <div class="card-hd"><span class="no">NO.{gi:02d}</span><span>案例详情</span></div>
  <div class="card-inner">
    <div class="card-title kai">{esc(it['title'])}</div>
    <div class="card-source">来源：{esc(it['source'])}<br><a href="{esc(it['link'])}">{esc(it['link'])}</a></div>
    <div class="card-body">{esc(it['body'])}</div>
    <div class="card-foot">
      <div class="box inno"><b>创新点</b>{esc(it['innovation'])}</div>
      <div class="box learn"><b>银行学习点</b>{esc(it['learning'])}</div>
    </div>
  </div>
</div>
'''

def summary_card_html(d):
    extra = EXTRA.get(d['title'], {})
    summary = d['subtitle'] + "近期典型案例包括：" + "；".join([it['title'] for it in d['items']]) + "。"
    return f'''
<div class="card-sum">
  <div class="sum-title kai">方向小结 · {esc(d['title'].split('：')[0])}</div>
  <div class="sum-body">{esc(summary)}</div>
  <div class="sum-foot2"><b>银行学习要点：</b>{esc(extra.get('action', ''))}</div>
</div>
'''

def items_page_html(d, items, page_label):
    cards = ''.join(item_card_html(it, it['gi']) for it in items)
    return f'''
<div class="page item-page">
  <div class="item-head"><span class="dir">{esc(d['title'])}</span><span class="pg">{page_label}</span></div>
  <div class="item-cards">{cards}</div>
</div>
'''

def mixed_page_html(d, cards, page_label):
    html_cards = ""
    for c in cards:
        if c.get('is_summary'):
            html_cards += c['html']
        else:
            html_cards += item_card_html(c, c['gi'])
    return f'''
<div class="page item-page">
  <div class="item-head"><span class="dir">{esc(d['title'])}</span><span class="pg">{page_label}</span></div>
  <div class="item-cards">{html_cards}</div>
</div>
'''

def build():
    pages = [cover_html(), summary_html()]
    global_no = 1
    for idx, d in enumerate(DIRECTIONS, 1):
        pages.append(direction_page_html(idx, d))
        items = [{'gi': global_no + i, **it} for i, it in enumerate(d['items'])]
        pages.append(items_page_html(d, items[:3], f"NO.{items[0]['gi']:02d}–{items[2]['gi']:02d}"))
        page_cards = items[3:] + [{'is_summary': True, 'html': summary_card_html(d)}]
        pages.append(mixed_page_html(d, page_cards, f"NO.{items[3]['gi']:02d}–{items[4]['gi']:02d} + 小结"))
        global_no += 5

    html = f'''<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{''.join(pages)}</body></html>'''
    with open('briefing.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('generated briefing.html with', len(pages), 'pages')

if __name__ == '__main__':
    build()
