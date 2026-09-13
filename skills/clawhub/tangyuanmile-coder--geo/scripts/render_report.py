"""Render client-facing static HTML from measured evidence; no online dependencies."""
import argparse,collections,hashlib
from pathlib import Path
from common import *
from views import *

def render(m):
    c=m['config'];g=m['overall'];brand=c.get('brand');targets={p['key']:p['name'] for p in m['target_products']};target=g['target'];n=g['answers'];events=g['events'];ac=g['card_answers'];nt=len(c['questions']);np=len(m['platforms'])
    title=(brand+' · ' if brand else '')+c['name']+'｜'+('商品诊断报告' if targets else '商品竞争环境报告')
    sample='样例数据 · 非真实监测' if c.get('is_demo') else c['date']+' · 单日采样'
    status='本期采样完整' if m['sampling']['complete'] else '本期为已取得样本，部分采样数量与计划不一致'
    cover='<header class="cover" id="report-cover"><div class="brandline"><div class="logo"><span>✦</span> AIDSO <small>爱搜</small></div><div class="edition">商品诊断 · 客户报告<br><span>'+e(sample)+'</span></div></div><div class="hero"><p class="eyebrow">PRODUCT DIAGNOSTICS</p><h1>'+e(title)+'</h1><p class="subtitle">'+('正文提及、商品卡展示与竞争位置' if targets else '各搜索意图下的品牌与具体商品推荐')+'</p><div class="chips"><span>'+('品牌＋商品名' if brand else '商品名称')+f'</span><span>{np}个平台 · 按平台汇总</span><span>{nt}个问题 · {n}条回答</span></div></div><div class="executive"><div class="executive-label">本期数据</div><h2>'+ (f'正文品牌提及{target["body_brand"]}条 · ' if brand else '')+f'含商品卡回答{ac}条 · 商品卡{events:,}次</h2><div class="insights"><article><span>01 / 样本</span><strong>{n}条有效回答</strong><p>'+e(status)+f'</p></article><article><span>02 / 商品</span><strong>{len(g["products"])}个可区分商品</strong><p>明确系列按商品汇总；系列待确认条目独立保留。</p></article><article><span>03 / 范围</span><strong>'+ (str(target['events'])+'次目标商品卡' if targets else str(len(g['brands']['card']))+'个出卡品牌')+'</strong><p>统计对应题库实际出现的商品卡，所有比例使用所在表格的样本范围。</p></article></div></div><div class="cover-bottom"><span>诊断对象：'+e((brand+' · ' if brand else '')+c['name'])+'</span><span>统计层级：商品系列</span></div></header>'
    intro='<div class="brief-grid">'+''.join('<div><span>'+a+'</span><strong>'+e(b)+'</strong></div>' for a,b in [('监测品牌',brand or '未设置'),('名称与层级',c['name']+' · '+('类目' if c['name_type']=='category' else '具体商品')),('采样日期',c['date']),('实际样本',f'{nt}题 · {n}条回答')])+'</div>'
    intro+=table('input_methods',['输入方式','名称层级','统计范围'],[['商品名称','类目','题库中实际推荐的品牌及具体商品'],['商品名称','具体商品','已核验匹配的具体商品，按品牌分别列示'],['品牌＋商品名','类目','目标品牌在该类目范围内的商品集合'],['品牌＋商品名','具体商品','目标品牌的指定商品']], '支持两种输入及两个名称层级')
    scope_rows=[]
    for p in m['platforms']:
        sizes=[next(x['answers'] for x in q['platforms'] if x['provider']==p['provider']) for q in m['questions']]
        per=str(min(sizes)) if min(sizes)==max(sizes) else str(min(sizes))+'—'+str(max(sizes))
        scope_rows.append([p['provider'],str(nt),per,str(p['answers']),str(p['card_answers']),str(p['events'])])
    intro+=table('scope_matrix',['平台','问题数','每题实际回答数','实际回答数','含商品卡回答数','商品卡提及次数'],scope_rows,'按平台汇总的实际采样规模；每题数量不齐时列示最小至最大值')
    intro+=note('仅纳入已确认支持商品卡推荐的采样范围，客户报告按平台汇总。未出卡的有效回答仍进入覆盖率分母；同一问题的重复采样为独立回答，不按正文相同去重。'+status+'。')
    intro+=table('questions',['题号','监测问题（完整原文）','搜索意图','实际回答数'],[[e(q['id']),e(q['prompt']),e(q['intent']),str(q['answers'])] for q in m['questions']],'完整题库与搜索意图')
    intro+=note('每题只归入一个已确认搜索意图；不同意图先合并其实际回答，再计算指标。类目与材质不自动视作具体产品系列。品牌及系列归并依据随配套数据留存；店铺、规格与包装不单独构成商品层级。不同明确系列及跨系列组合分开；不能明确系列的条目不强行合并。')
    if targets:intro+=note('本次目标商品范围：'+'；'.join(targets.values())+'。'+('其中正文品牌只按品牌名称及已核验别名计数。' if brand else '未配置监测品牌，不计算以品牌为起点的承接率。'))
    intro+=note('商品卡展示不等同于点击、订单、销量或成交；本报告只展示采样数据，不作原因推断与优化建议。')
    measures=[]
    if targets:
        if brand:measures.append(('品牌提及次数',str(target['body_brand']),'正文提及目标品牌的回答数；每答最多计1次。'))
        measures += [('商品卡提及次数',str(target['events']),'目标范围的去重商品卡展示次数；不同卡片分别计次。'),('商品卡回答覆盖率',pct(target['coverage']),f'{target["card_answers"]} / {n}条有效回答')]
        if brand:measures.append(('商品卡承接率',pct(target['takeup']),f'{target["brand_card"]} / {target["body_brand"]}条正文目标品牌回答'))
        measures += [('商品卡SOV',pct(target['sov']),f'{target["events"]} / {events}次全部商品卡'),('首卡率',pct(target['first_rate']),f'{target["first"]} / {ac}条含任意商品卡回答'),('平均卡位',d(target['mean_position']),f'{target["position_sum"]}个卡位序号之和 / {target["events"]}次目标卡')]
        if brand:measures.append(('品牌→正文商品承接率',pct(target['brand_to_product']),f'{target["brand_product"]} / {target["body_brand"]}条正文目标品牌回答'))
        measures.append(('正文商品→商品卡转卡率',pct(target['product_to_card']),f'{target["product_card"]} / {target["body_product"]}条正文目标商品回答'))
    else:measures=[('商品卡提及次数',str(events),'全部有效商品卡展示次数'),('商品卡回答覆盖率',pct(ac/n),f'{ac} / {n}条有效回答'),('可区分商品数',str(len(g['products'])),'明确系列与未明确系列的独立条目'),('出卡品牌数',str(len(g['brands']['card'])),'不含品牌待确认归属组')]
    overall='<div class="metric-grid">'+''.join('<article class="metric"><span>'+a+'</span><strong>'+b+'</strong><p>'+e(t)+'</p></article>' for a,b,t in measures)+'</div>'
    defs=[['商品卡提及次数','同一回答内按卡源与商品ID去重；同一商品不同商品卡分别计次。'],['商品卡回答覆盖率','含所统计商品卡的回答数 ÷ 该范围全部有效回答数。'],['商品卡SOV','所统计商品的商品卡次数 ÷ 对应范围全部商品卡次数；未知品牌仍在分母中。'],['首卡率','所统计商品处于第1卡位的回答数 ÷ 对应范围含任意商品卡的回答数。'],['平均卡位','所统计商品所有卡片的展示序号之和 ÷ 其卡片次数；无卡不适用。']]
    if brand:defs += [['品牌提及次数','仅统计正文中出现监测品牌的回答数；每答最多1次，提及不限于正向推荐。'],['商品卡承接率','正文提及目标品牌且同答出现目标商品卡的回答数 ÷ 正文提及目标品牌回答数。'],['品牌→正文商品承接率','正文同时提及目标品牌与目标商品的回答数 ÷ 正文提及目标品牌回答数。']]
    if targets:defs.append(['正文商品→商品卡转卡率','正文提及目标商品且同答出现目标商品卡的回答数 ÷ 正文提及目标商品回答数。'])
    overall+=table('metric_definitions',['指标','计算口径'],defs,'指标与统计边界')+note('所有分母为0的比例均显示不适用；平台指标先合并样本重新计算，不对终端或模式百分比取平均。正文排除卡片、链接地址、引用摘要和思考内容；正文提及与商品卡归属独立识别。多目标集合的出卡回答数按回答并集计算。')
    if targets:
        if brand:
            s4=[('正文品牌与目标卡同时出现',target['brand_card']),('仅正文提及品牌',target['body_brand']-target['brand_card']),('仅出现目标商品卡',target['card_answers']-target['brand_card']),('两者均无',n-target['body_brand']-target['card_answers']+target['brand_card'])]
        else:s4=[('正文商品与目标卡同时出现',target['product_card']),('仅正文提及商品',target['body_product']-target['product_card']),('仅出现目标商品卡',target['card_answers']-target['product_card']),('两者均无',n-target['body_product']-target['card_answers']+target['product_card'])]
        colors=['purple','lavender','teal','gray']
        overall+='<h3>正文与目标商品卡的四状态分布</h3>'+note('每条回答只进入一种状态；没有目标卡并不表示没有其他商品卡。')+'<div class="state-stack">'+''.join(f'<span class="{col}" style="width:{v/n*100:.5f}%"></span>' for (label,v),col in zip(s4,colors))+'</div><div class="state-grid">'+''.join('<article class="state '+col+'"><span>'+label+'</span><strong>'+str(v)+'<small>'+pct(v/n)+'</small></strong></article>' for (label,v),col in zip(s4,colors))+'</div>'
        if brand:
            overall+='<h3>正文品牌 × 正文商品 × 目标商品卡：八种状态</h3>'+table('states8',['正文目标品牌','正文目标商品','目标商品卡','回答数','占全部回答'],[[('提及' if x['brand'] else '未提及'),('提及' if x['product'] else '未提及'),('有' if x['card'] else '无'),str(x['count']),pct(x['count']/n)] for x in g['states8']],f'每条回答只进入一种状态，共{n}条；零样本状态保留')
            overall+='<h3>目标商品承接表现 · 分平台</h3>'+note('目标品牌：'+brand+'；目标商品范围：'+'；'.join(targets.values())+'。本表的卡片分子只含目标范围商品，不含同品牌其他商品。')
            overall+=table('conversion_platforms',['平台','正文目标品牌回答','正文目标商品回答','目标品牌→正文目标商品','目标品牌→目标商品卡','正文目标商品→目标商品卡'],[[p['provider'],str(p['target']['body_brand']),str(p['target']['body_product']),fraction(p['target']['brand_product'],p['target']['body_brand']),fraction(p['target']['brand_card'],p['target']['body_brand']),fraction(p['target']['product_card'],p['target']['body_product'])] for p in m['platforms']],'各平台内独立计算，同答交集作为分子')
        overall+=note('正文商品识别名称：'+ ' / '.join(c.get('body_product',{}).get('aliases',[]))+('；按已核验的完整名称规则识别。' if c.get('body_product',{}).get('pattern') else '。')+'仅材质或泛类型表述不作为具体商品提及；类目模式的正文范围提及按已确认类目词识别。')
    overall+='<h3>产品展示结构</h3><div class="layer-title"><b>第一层</b><span>'+('目标商品在全部商品展示中的位置' if targets else '全部具体商品与品牌归属')+'</span></div>'
    structure={k:m['structure'].get(k,0) for k in (['目标商品','同品牌其他商品','其他品牌商品','品牌待确认商品'] if brand else ['目标商品','其他品牌商品','品牌待确认商品'])} if targets else {'明确品牌商品':events-m['structure'].get('品牌待确认商品',0),'品牌待确认商品':m['structure'].get('品牌待确认商品',0)}
    overall+=donut(structure,events)+note('各展示归属互斥，次数合计为全部商品卡次数；占比＝该归属卡片次数÷全部商品卡次数。')
    overall+='<div class="layer-title"><b>第二层</b><span>'+('目标商品' if targets else '全部商品')+'的采样价格、电商来源与店铺</span></div>'
    cards=[x for a in m['ledger'] for x in a['cards'] if not targets or x['product_key'] in targets];den=len(cards);pr=collections.Counter('未提供价格' if x['price'] is None else '¥'+d(x['price']) for x in cards);ss=collections.Counter(x['source']+' · '+x['shop'] for x in cards)
    def topcounter(counter):
        out=[{'name':k,'events':v} for k,v in counter.most_common(10)]
        if len(counter)>10:out.append({'name':'其余'+str(len(counter)-10)+'项','events':sum(counter.values())-sum(x['events'] for x in out)})
        return out
    overall+='<div class="chart-grid">'+bars('采样价格',topcounter(pr),'events',{},f'按采样报价计次，合计{den}次；金额未作规格折算。')+bars('店铺与商品来源',topcounter(ss),'events',{},f'按来源与店铺计次，合计{den}次；显示前10项及其余合计。')+'</div>'
    xs=target['commerce'] if targets else g['commerce']
    overall+=table('target_commerce',['电商来源','店铺','采样价格范围','商品卡提及次数','有报价次数'],[[e(x['source']),e(x['shop']),('未提供' if x['min'] is None else '¥'+d(x['min'])+'—¥'+d(x['max'])),str(x['events']),str(x['priced'])+' / '+str(x['events'])] for x in xs],('目标范围' if targets else '全部商品')+' · 电商信息')+commerce_note()
    overall+='<h3 id="brand-rankings">正文提及品牌榜与商品卡品牌榜</h3>'+note(f'同一{n}条回答，两张榜独立排名；正文提及品牌不由商品卡反向补记。')+'<div class="chart-grid">'
    for typ,caption in [('body','正文提及品牌Top10'),('card','商品卡品牌Top10')]:
        ps=g['brands'][typ][:10];outside=[x for x in g['brands'][typ][10:] if x['brand']==brand];ps=ps+outside
        overall+='<figure class="chart"><figcaption><h4>'+caption+'</h4></figcaption>'+table('body_brand_top' if typ=='body' else 'card_brand_top',['排名','品牌','正文提及回答数' if typ=='body' else '商品卡提及次数','正文提及率' if typ=='body' else '商品卡SOV'],[[str(x['body_rank'] if typ=='body' else x['card_rank']),e(x['brand']),str(x['body_answers'] if typ=='body' else x['events']),fraction(x['body_answers'],n) if typ=='body' else fraction(x['events'],events)] for x in ps],caption,focus=[x['brand']==brand for x in ps])+'</figure>'
    overall+='</div>'+note('正文提及率＝品牌正文提及回答数÷全部有效回答数；品牌商品卡SOV＝该品牌所有商品卡次数÷全部商品卡次数。品牌待确认卡片不参与品牌榜排名，仍保留在SOV分母。')
    union={x['brand'] for x in g['brands']['body'][:10]+g['brands']['card'][:10]}|{brand};bg={**g,'brands':{**g['brands'],'comparison':[x for x in g['brands']['comparison'] if x['brand'] in union]}}
    overall+=brand_comparison(bg,'brand_comparison',brand)
    platform=note('各榜按商品卡提及次数降序；同次数按出卡回答数降序，再按商品名称及归类标识排序。目标商品高亮；榜外补列实际名次，未出卡明确标为0。')+commerce_note()
    for i,p in enumerate(m['platforms'],1):platform+=ranking(p,f'platform-{i}',p['provider'],targets)
    platform+='<h3 id="search-intents">搜索意图 × 平台：推荐商品</h3>'+note('每个意图在每个平台独立选择商品Top榜；不同意图不共用固定竞品列。')
    platform+=table('intent_overview',['搜索意图']+[p['provider']+' Top3' for p in m['platforms']],[[e(it['name'])+f'<small>{len(it["questions"])}题 · {it["answers"]}条回答</small>']+[('<div>'+''.join('<p>'+str(p['rank'])+'. '+e(p['name'])+(badge() if p['key'] in targets else '')+f'<small>{p["events"]}次提及</small></p>' for p in gg['products'][:3])+'</div>') if gg['products'] else '未出现商品卡' for gg in it['platforms']] for it in m['intents']],'各搜索意图下不同平台推荐商品速览')
    for i,it in enumerate(m['intents'],1):
        platform+='<div class="layer-title"><b>意图 '+str(i)+'</b><span>'+e(it['name'])+'</span></div>'+note('所属问题：'+'；'.join(q['id']+' '+q['prompt'] for q in it['questions']))
        for j,p in enumerate(it['platforms'],1):platform+=ranking(p,f'intent-{i}-{j}',it['name']+' · '+p['provider'],targets)
    comp=m['target_products']+m['peers'] if targets else g['products'][:20]
    competition=note('展示竞品从同日同题库实际出现、品牌已确认的商品中按提及次数自动选择Top5；有品牌模式排除同品牌其他商品。该排名表示本次题库展示次数，不代表市场销量。')
    rows=[]
    for p in comp:
        cells=[name(p,targets),fraction(p['events'],events)]
        for gg in m['platforms']:
            x=next((x for x in gg['products'] if x['key']==p['key']),None);cells.append(fraction(x['events'] if x else 0,gg['events']))
        rows.append(cells)
    competition+=table('competitors',['商品／品牌及电商信息','整体商品卡SOV']+[p['provider']+'SOV' for p in m['platforms']],rows,'目标商品与Top5竞品 · 平台份额对照' if targets else '具体商品Top20 · 平台份额对照','competition',[p['key'] in targets for p in comp])+note('商品卡SOV＝该商品卡次数÷对应范围全部商品卡次数。整体和各平台分别给出分子／分母；整体不平均平台百分比。')
    if brand:
        ps=m['same_brand_products'];bn=sum(p['events'] for p in ps)
        competition+='<h3>目标品牌商品卡展示分布</h3>'+table('brand_product_distribution',['商品／品牌及电商信息','商品卡提及次数','品牌内商品卡占比']+[p['provider']+'提及次数' for p in m['platforms']],[[name(p,targets),str(p['events']),fraction(p['events'],bn)]+[str(next((x['events'] for x in gg['products'] if x['key']==p['key']),0)) for gg in m['platforms']] for p in ps],brand+'全部出卡商品 · 目标商品高亮','competition',[p['key'] in targets for p in ps])+note(f'品牌内占比＝该商品卡次数÷{bn}次目标品牌全部商品卡。此分母只含目标品牌，区别于全部品牌SOV；三平台次数相加等于整体次数。')
    position=comp if targets else [p for p in g['products'] if p['brand']!='未确认品牌'][:5]
    competition+='<h3>首卡率与平均卡位对比</h3><div class="chart-grid">'+bars('首卡率对比',position,'first_rate',targets,f'该商品第1卡位回答数÷{ac}条含任意商品卡回答。')+bars('平均卡位对比',position,'mean_position',targets,'各次卡位序号之和÷该商品卡次数；数值越小，展示越靠前。')+'</div>'
    appendix='<aside class="report-section" id="appendix"><div class="section-head"><span>附</span><div><h2>数据明细附录</h2><p>品牌明细、识别名称及逐题三平台商品榜</p></div></div><h3>完整品牌对照与平台品牌明细</h3>'+brand_comparison(g,'brand_comparison_full',brand)
    for i,gg in enumerate(m['platforms'],1):appendix+='<h3>'+gg['provider']+' · 品牌明细</h3>'+brand_comparison(gg,'brand-platform-'+str(i),brand)
    appendix+='<h3>品牌识别名称对照</h3>'+table('brand_aliases',['品牌／归属组','识别名称及别名'],[[e(x['name']),e(' / '.join(x.get('aliases',[])))] for x in m['brands']],'正文名称独立识别，同答最多计1次')+'<h3>逐题三平台推荐商品Top10</h3>'+commerce_note()
    for i,q in enumerate(m['questions'],1):
        appendix+='<h3>'+e(q['id']+' · '+q['prompt'])+'</h3>'+note('搜索意图：'+q['intent']+f'；实际{q["answers"]}条回答。')
        for j,p in enumerate(q['platforms'],1):appendix+=ranking(p,f'question-{i}-{j}',q['id']+' · '+p['provider'],targets)
    if brand:appendix+='<h3>逐题正文与目标商品卡状态</h3>'+table('question_states',['问题','正文品牌','正文商品','目标商品卡','回答数'],[[e(q['id']+' '+q['prompt']),('提及' if x['brand'] else '未提及'),('提及' if x['product'] else '未提及'),('有' if x['card'] else '无'),str(x['count'])] for q in m['questions'] for x in q['states8']],'每道问题的八种互斥状态，零样本状态保留')
    appendix+='<h3>竞品商品卡完整指标明细</h3>'+table('competitor_metrics_full',['商品／品牌及电商信息','商品卡提及次数','回答覆盖率','商品卡SOV','首卡率','平均卡位'],[[name(p,targets),str(p['events']),fraction(p['card_answers'],n),fraction(p['events'],events),fraction(p['first'],ac),d(p['mean_position'])] for p in comp],'与正文份额表相同商品范围','competition',[p['key'] in targets for p in comp])+note(f'整体分母：{n}条有效回答、{events}次商品卡、{ac}条含卡回答。指标按前述公式逐项计算。')+'</aside>'
    css=(Path(__file__).resolve().parents[1]/'assets/report.css').read_text();navcss=(Path(__file__).resolve().parents[1]/'assets/fixed-navigation.css').read_text()
    return '<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light dark"><title>'+e(title)+'</title><style>'+css+'</style><style id="fixed-navigation-style">'+navcss+'</style></head><body>'+navigation()+'<main>'+cover+section('01','诊断范围与样本概况','诊断对象、采样范围与完整题库',intro)+section('02','整体表现','正文提及、商品卡展示结构与品牌双榜',overall)+section('03','各平台商品Top榜单','三平台汇总及搜索意图下的具体推荐商品',platform)+section('04','竞品对比与竞争力','展示份额、品牌内商品分布与竞争位置',competition)+appendix+'<footer><div><b>AIDSO 爱搜</b><span>'+e(c['date'])+'</span></div><p>数据与口径以本报告列示的采样范围为准；完整复核记录随配套数据留存。</p></footer></main></body></html>'
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--model',required=True);p.add_argument('--out',required=True);a=p.parse_args()
    h=render(read_json(a.model));out=Path(a.out);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(h,encoding='utf-8');visible(out)
    print(json.dumps({'report':out.name,'bytes':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest()},ensure_ascii=False))
