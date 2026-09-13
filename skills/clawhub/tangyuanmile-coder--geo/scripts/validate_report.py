"""Independent arithmetic, static-document and input-output binding checks."""
import argparse,collections,hashlib,json,math,re
from html.parser import HTMLParser
from pathlib import Path
from common import *
class Document(HTMLParser):
    def __init__(self):super().__init__();self.ids=[];self.hrefs=[];self.forbidden=[];self.styles=[];self.instyle=False;self.text=[];self.sections=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        if tag=='section' and 'report-section' in a.get('class',''):self.sections+=1
        if tag=='a':self.hrefs.append(a.get('href',''))
        if tag in ['script','iframe','button','input','select','details','img','link'] or 'hidden' in a:self.forbidden.append(tag)
        if any(k.startswith('on') for k in a):self.forbidden.append('event')
        if tag=='style':self.instyle=True;self.styles.append('')
    def handle_endtag(self,t):
        if t=='style':self.instyle=False
    def handle_data(self,s):
        if self.instyle:self.styles[-1]+=s
        else:self.text.append(s)

def validate(m,html_text):
    checks=[]
    def check(name,test):
        if not test:raise ValueError(name)
        checks.append(name)
    ledger=m['ledger'];N=len(ledger);cards=[x for a in ledger for x in a['cards']];uid={a['uid'] for a in ledger};target=set(m['config'].get('target_keys',[]));brand=m['config'].get('brand')
    check('回答去重与有效样本',N==len(uid)==m['overall']['answers'])
    check('每答同卡去重与连续顺序',all(len({x['identity'] for x in a['cards']})==len(a['cards']) and [x['position'] for x in a['cards']]==list(range(1,len(a['cards'])+1)) for a in ledger))
    def groupcheck(g,rs):
        cs=[x for a in rs for x in a['cards']];base=len(rs);anycard=sum(bool(a['cards']) for a in rs)
        check('局部基数',g['answers']==base and g['events']==len(cs) and g['card_answers']==anycard)
        check('商品事件守恒',sum(p['events'] for p in g['products'])==len(cs))
        for p in g['products']+[g['target']]:
            selected=[x for x in cs if x['product_key']==p['key']] if 'key' in p else [x for x in cs if x['product_key'] in target]
            seen={x['uid'] for x in selected};first={x['uid'] for x in selected if x['position']==1};ps=sum(x['position'] for x in selected)
            check('卡片次数回答覆盖与顺序',p['events']==len(selected) and p['card_answers']==len(seen) and p['first']==len(first) and p['position_sum']==ps)
            for field,num,den in [('coverage',len(seen),base),('sov',len(selected),len(cs)),('first_rate',len(first),anycard),('mean_position',ps,len(selected))]:check('独立计算'+field,p[field] is None if den==0 else p[field] is not None and math.isclose(p[field],num/den,abs_tol=1e-12))
        check('八状态回答数守恒',sum(x['count'] for x in g['states8'])==base)
        for b in g['brands']['comparison']:
            bs={a['uid'] for a in rs if b['brand'] in a['body_brands']};bc=[x for x in cs if x['brand']==b['brand']];bcuid={x['uid'] for x in bc}
            check('品牌独立正文及同答交集',b['body_answers']==len(bs) and b['card_answers']==len(bcuid) and b['events']==len(bc) and b['joint']==len(bs&bcuid))
    groupcheck(m['overall'],ledger)
    for p in m['platforms']:groupcheck(p,[a for a in ledger if a['provider']==p['provider']])
    intents={q['id']:q['intent'] for q in m['config']['questions']}
    for it in m['intents']:
        for p in it['platforms']:groupcheck(p,[a for a in ledger if a['provider']==p['provider'] and intents[a['question_id']]==it['name']])
    for q in m['questions']:
        rs=[a for a in ledger if a['question_id']==q['id']];groupcheck(q,rs)
        for p in q['platforms']:groupcheck(p,[a for a in rs if a['provider']==p['provider']])
    from render_report import render
    check('统计模型与最终HTML一致',html_text==render(m))
    doc=Document();doc.feed(html_text)
    check('四部分与附录',doc.sections==4 and all(x in doc.ids for x in ['section-01','section-02','section-03','section-04','appendix','brand-rankings','search-intents']))
    check('唯一锚点与固定导航',len(set(doc.ids))==len(doc.ids) and len(doc.hrefs)==8 and all(h.startswith('#') and h[1:] in doc.ids for h in doc.hrefs))
    check('纯静态报告',not doc.forbidden)
    check('批准的原始正文样式',doc.styles[0]==(Path(__file__).resolve().parents[1]/'assets/report.css').read_text())
    check('删除模块未恢复',not any(x in doc.ids for x in ['state_card_ownership','question_competition','same_brand_products']))
    text=' '.join(doc.text)
    check('正文无技术字段',not any(x in text for x in ['render_ecom_card_widget_','reqId','thinking_enabled','productVos','aidso-token']))
    check('不泄露当前用户目录',str(Path.home()) not in text)
    check('完整题库',all(q['prompt'] in text for q in m['config']['questions']))
    if not brand:check('无品牌不展示品牌起点指标','目标商品承接表现 · 分平台' not in text and 'states8' not in doc.ids)
    return {'status':'PASS','checks_passed':len(checks),'html_sha256':hashlib.sha256(html_text.encode()).hexdigest(),'model_digest':digest(m),'browser_qa':'尚需真实浏览器检查桌面、手机和深色视图'}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--model',required=True);p.add_argument('--html',required=True);p.add_argument('--out',required=True);p.add_argument('--normalized',required=True);p.add_argument('--taxonomy',required=True);a=p.parse_args();m=read_json(a.model)
    if m['input_digest']!=digest(read_json(a.normalized)) or m['taxonomy_digest']!=digest(read_json(a.taxonomy)):raise ValueError('模型与当前原始规范化数据或归属表不一致，请重新计算')
    out=validate(m,Path(a.html).read_text());out['input_binding']='PASS';write_json(a.out,out);print(json.dumps(out,ensure_ascii=False))
