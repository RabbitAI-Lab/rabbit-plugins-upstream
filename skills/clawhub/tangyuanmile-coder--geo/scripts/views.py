"""Escaped static report components using the approved visual stylesheet."""
import html
from decimal import Decimal,ROUND_HALF_UP

def e(x):return html.escape(str(x))
def d(x):return format(Decimal(str(x)).quantize(Decimal('0.01'),rounding=ROUND_HALF_UP),'.2f') if x is not None else '不适用'
def pct(x):return d(x*100)+'%' if x is not None else '不适用'
def fraction(n,den):return pct(n/den if den else None)+f'<small>{n:,} / {den:,}</small>'
def note(x):return '<p class="note">'+e(x)+'</p>'
def badge():return '<span class="tag">目标商品</span>'
def table(ident,heads,rows,caption='',classes='',focus=None):
    content=[]
    for i,row in enumerate(rows):
        content.append('<tr'+(' class="target-row"' if focus and focus[i] else '')+'>'+''.join(f'<td data-label="{e(h)}">{v}</td>' for h,v in zip(heads,row))+'</tr>')
    return f'<table id="{e(ident)}" class="{e(classes)}"><caption>{e(caption)}</caption><thead><tr>'+''.join('<th scope="col">'+e(h)+'</th>' for h in heads)+'</tr></thead><tbody>'+''.join(content)+'</tbody></table>'
def commerce(xs):
    return ''.join('<small>'+e(x['source'])+' · '+e(x['shop'])+'<br>采样价格：'+('未提供' if x['min'] is None else '¥'+d(x['min'])+('—¥'+d(x['max']) if x['max']!=x['min'] else ''))+f'（{x["priced"]}/{x["events"]}次有报价）</small>' for x in xs)
def name(p,targets):return '<strong>'+e(p['name'])+'</strong>'+ (badge() if p['key'] in targets else '')+'<small>品牌：'+e(p['brand'])+'</small>'+('' if p.get('resolved') else '<small>系列待确认，单独统计</small>')+commerce(p.get('commerce',[]))
def selected(g,targets):
    shown=g['products'][:10]
    return shown+[p for p in g['products'][10:] if p['key'] in targets]

def ranking(g,ident,title,targets):
    ps=selected(g,targets)
    out=f'<div class="platform-block" id="{ident}"><div class="platform-head"><div><span class="platform-icon icon-{e(g["provider"])}">{e(g["provider"][0])}</span><h3>{e(title)}</h3></div><span>商品Top10</span></div><p class="platform-base">{g["answers"]}条监测回答 · {g["card_answers"]}条含商品卡回答 · {g["events"]:,}次商品卡提及</p>'
    rows=[[str(p['rank']),name(p,targets),str(p['events']),fraction(p['card_answers'],g['answers']),fraction(p['events'],g['events']),fraction(p['first'],g['card_answers']),d(p['mean_position'])] for p in ps]
    out+=table(ident+'_top',['排名','商品／品牌及电商信息','商品卡提及次数','回答覆盖率','商品卡SOV','首卡率','平均卡位'],rows,title+' · 商品卡提及Top10','ranking',[p['key'] in targets for p in ps])
    out+=note(f'本榜计算口径：同一回答同一商品卡去重，不同卡片分别计次；覆盖率＝该商品出卡回答数÷{g["answers"]}条回答；SOV＝该商品卡次数÷{g["events"]}次全部商品卡；首卡率＝该商品处于第1卡位的回答数÷{g["card_answers"]}条含卡回答；平均卡位＝各次卡位序号之和÷该商品卡次数。分母为0时不适用。')
    if len(g['products'])<10:out+=note('本范围实际出现'+str(len(g['products']))+'个可区分商品，已全部列出。' if ps else '本范围未出现有效商品卡；没有可列示商品。')
    for key in targets:
        p=next((p for p in g['products'] if p['key']==key),None)
        if p is None:out+=note('目标商品「'+targets[key]+'」未出卡：提及0次，覆盖率'+('0.00%' if g['answers'] else '不适用')+'；无商品排名，平均卡位不适用。')
        elif p['rank']>10:out+=note('目标商品「'+p['name']+'」位于Top10之外，已附列并保留实际名次。')
    return out+'</div>'
def commerce_note():return note('电商来源、店铺与价格均取自本榜实际商品卡，按来源／店铺列示采样最低至最高报价及有报价次数。缺失或不能确定为单一金额的报价不按0元计算；价格不折算为统一规格。店名不代表已核验授权；采样价格不代表当前售价。')
def bars(title,ps,field,targets,caption):
    xs=sorted(ps,key=lambda p:(p[field] is None, -(p[field] or 0) if field!='mean_position' else (p[field] or 0),p['name']))
    mx=max([p[field] or 0 for p in xs]+[0]) or 1;out='<figure class="chart"><figcaption><h4>'+e(title)+'</h4><p>'+e(caption)+'</p></figcaption>'
    for p in xs:
        v=p[field];label=pct(v) if field=='first_rate' else d(v) if field=='mean_position' else str(v)
        out+='<div class="bar-row"><div class="bar-label">'+e(p['name'])+(badge() if p.get('key') in targets else '')+'<strong>'+label+'</strong></div><div class="bar-track"><span class="'+('focus' if p.get('key') in targets else '')+f'" style="width:{(v or 0)/mx*100:.5f}%"></span></div></div>'
    if not xs:out+=note('本范围没有可比较的商品卡。')
    return out+'</figure>'
def section(number,title,sub,content):return f'<section class="report-section" id="section-{number}"><div class="section-head"><span>{number}</span><div><h2>{e(title)}</h2><p>{e(sub)}</p></div></div>{content}</section>'
NAV=[('report-cover','总览'),('section-01','诊断范围'),('section-02','整体表现'),('brand-rankings','品牌双榜'),('section-03','平台榜单'),('search-intents','搜索意图'),('section-04','竞品对比'),('appendix','数据附录')]
def navigation():return '<nav class="report-nav" aria-label="报告导航"><div class="report-nav-inner"><strong>AIDSO 爱搜</strong><div class="report-nav-links">'+''.join('<a href="#'+k+'">'+v+'</a>' for k,v in NAV)+'</div></div></nav>'
def brand_comparison(g,ident,brand=None):
    rs=g['brands']['comparison']
    return table(ident,['品牌','正文排名','卡片排名','正文提及回答','品牌出卡回答','品牌商品卡次数','正文与卡片同时出现','品牌商品卡承接率'],[[e(x['brand']),str(x['body_rank'] or '—'),str(x['card_rank'] or '—'),str(x['body_answers']),str(x['card_answers']),str(x['events']),str(x['joint']),fraction(x['joint'],x['body_answers'])] for x in rs],f'本范围{g["answers"]}条回答',focus=[x['brand']==brand for x in rs])+note('本表商品卡包含该品牌全部商品；品牌商品卡承接率＝正文提及该品牌且同答出现其商品卡的回答数÷正文提及该品牌回答数，区别于目标商品承接率。两榜分别排名，未出现不赋予名次。')


def donut(items,total):
    colors=['#7949ed','#ae8fed','#17a393','#d9dce8'];offset=0;circles='';legend=''
    for i,(label,n) in enumerate(items.items()):
        pc=n/total*100 if total else 0
        circles+=f'<circle cx="60" cy="60" r="46" pathLength="100" fill="none" stroke="{colors[i%4]}" stroke-width="16" stroke-dasharray="{pc} {100-pc}" stroke-dashoffset="{-offset}" transform="rotate(-90 60 60)"/>';offset+=pc
        legend+=f'<div><span class="dot dot-{i%4}"></span><span>{e(label)}</span><strong>{n}次</strong><em>{pct(n/total if total else None)}</em></div>'
    if not items:legend='<div>本范围未出现有效商品卡，占比不适用。</div>'
    return f'<div class="structure" id="product_structure"><svg class="donut" viewBox="0 0 120 120" role="img" aria-label="商品展示结构，共{total}次商品卡"><circle cx="60" cy="60" r="46" fill="none" stroke="#e9e5f0" stroke-width="16"/>{circles}<text x="60" y="58" text-anchor="middle" class="donut-num">{total:,}</text><text x="60" y="73" text-anchor="middle" class="donut-label">商品卡提及</text></svg><div class="legend">{legend}</div></div>'
