"""Product-level measures from independent answer and card evidence."""
import argparse, collections, copy, re
from pathlib import Path
from common import *
from intake import inventory
UNKNOWN='未确认品牌'
def ratio(n,d):return n/d if d else None

def matches(text,rule):
    if rule.get('pattern'):
        if not rule.get('basis'):raise ValueError('正则匹配规则须说明核验依据')
        return bool(re.search(rule['pattern'],text,re.I))
    for alias in rule.get('aliases',[]):
        if not alias:raise ValueError('别名不可为空')
        pattern=re.escape(alias)
        if re.fullmatch(r'[\w .-]+',alias,re.ASCII):pattern=r'(?<![A-Za-z0-9])'+pattern+r'(?![A-Za-z0-9])'
        if re.search(pattern,text,re.I):return True
    return False

def commerce(cards):
    buckets={}
    for c in cards:
        k=(c['source'],c['shop']);x=buckets.setdefault(k,{'source':k[0],'shop':k[1],'events':0,'priced':0,'min':None,'max':None})
        x['events']+=1
        if c['price'] is not None:
            x['priced']+=1;x['min']=min(x['min'],c['price']) if x['min'] is not None else c['price'];x['max']=max(x['max'],c['price']) if x['max'] is not None else c['price']
    return sorted(buckets.values(),key=lambda x:(-x['events'],x['source'],x['shop']))

def measure(rows,cards,brand=None,body_set=None):
    n=len(rows);all_cards=[x for a in rows for x in a['cards']];ac={a['uid'] for a in rows if a['cards']};cu={x['uid'] for x in cards}
    bu={a['uid'] for a in rows if brand and brand in a['body_brands']}
    pu={a['uid'] for a in rows if a['body_target']};fi={x['uid'] for x in cards if x['position']==1}
    return {'answers':n,'all_card_events':len(all_cards),'all_card_answers':len(ac),'events':len(cards),'card_answers':len(cu),'coverage':ratio(len(cu),n),'sov':ratio(len(cards),len(all_cards)),'first':len(fi),'first_rate':ratio(len(fi),len(ac)),'position_sum':sum(x['position'] for x in cards),'mean_position':ratio(sum(x['position'] for x in cards),len(cards)),'body_brand':len(bu),'body_product':len(pu),'brand_product':len(bu&pu),'brand_card':len(bu&cu),'product_card':len(pu&cu),'takeup':ratio(len(bu&cu),len(bu)) if brand else None,'brand_to_product':ratio(len(bu&pu),len(bu)) if brand else None,'product_to_card':ratio(len(pu&cu),len(pu)),'commerce':commerce(cards)}

def group(rows,catalog,brands,c):
    cards=[x for a in rows for x in a['cards']];by=collections.defaultdict(list)
    for x in cards:by[x['product_key']].append(x)
    products=[{**catalog[k],**measure(rows,xs,c.get('brand'))} for k,xs in by.items()]
    products.sort(key=lambda p:(-p['events'],-p['card_answers'],p['name'],p['key']))
    for i,p in enumerate(products,1):p['rank']=i
    target_cards=[x for x in cards if x['product_key'] in c.get('target_keys',[])]
    target=measure(rows,target_cards,c.get('brand'))
    brand_rows=[]
    for b in brands:
        bb={a['uid'] for a in rows if b['name'] in a['body_brands']};bc=[x for x in cards if x['brand']==b['name']];cu={x['uid'] for x in bc};joint=len(bb&cu)
        if bb or bc:brand_rows.append({'brand':b['name'],'body_answers':len(bb),'body_rate':ratio(len(bb),len(rows)),'card_answers':len(cu),'events':len(bc),'sov':ratio(len(bc),len(cards)),'joint':joint,'takeup':ratio(joint,len(bb)),'body_rank':None,'card_rank':None})
    bs=sorted([x for x in brand_rows if x['body_answers']],key=lambda x:(-x['body_answers'],x['brand']));cs=sorted([x for x in brand_rows if x['events']],key=lambda x:(-x['events'],x['brand']))
    for i,x in enumerate(bs,1):x['body_rank']=i
    for i,x in enumerate(cs,1):x['card_rank']=i
    states=[]
    for b in (True,False):
        for p in (True,False):
            for card in (True,False):
                n=sum((bool(c.get('brand') and c['brand'] in a['body_brands']),a['body_target'],any(x['product_key'] in c.get('target_keys',[]) for x in a['cards']))==(b,p,card) for a in rows)
                states.append({'brand':b,'product':p,'card':card,'count':n})
    return {'answers':len(rows),'card_answers':sum(bool(a['cards']) for a in rows),'events':len(cards),'products':products,'target':target,'brands':{'body':bs,'card':cs,'comparison':sorted(brand_rows,key=lambda x:(-x['events'],-x['body_answers'],x['brand']))},'states8':states,'commerce':commerce(cards)}

def build(data,tax):
    c=validate_config(data['config'],require_targets=True);rows=copy.deepcopy(data['answers']);inv=inventory(data)
    brands=tax.get('brands',[]);catalog={p['key']:p for p in tax.get('products',[])}
    if len(catalog)!=len(tax.get('products',[])):raise ValueError('商品key重复')
    bnames={b['name'] for b in brands}
    if len(bnames)!=len(brands):raise ValueError('品牌归属组重复')
    if c.get('brand') and c['brand'] not in bnames:raise ValueError('请提供监测品牌的已核验正文识别名称')
    for b in brands:
        if not b.get('aliases') and not b.get('pattern'):raise ValueError('品牌必须有正文识别名称')
    mapping=tax.get('cards',{})
    for ident,mp in mapping.items():
        if mp['product_key'] not in catalog:raise ValueError('卡片归并映射指向不存在的商品')
        if ident in inv and (not mp.get('basis') or mp.get('evidence_title') not in inv[ident]['titles']):raise ValueError('商品归并依据须包含该原始卡片ID实际出现过的标题')
    for k,p in catalog.items():
        if p.get('brand') not in bnames|{UNKNOWN}:raise ValueError('商品品牌未在已核验品牌表中登记')
        if not p.get('name'):raise ValueError('商品缺少名称')
    targets=set(c.get('target_keys',[]))
    if not targets<=set(catalog):raise ValueError('目标商品集合尚未完成核验')
    if c.get('brand') and any(catalog[k]['brand']!=c['brand'] for k in targets):raise ValueError('目标品牌范围混入其他品牌商品')
    body_rule=c.get('body_product',{})
    if targets and not body_rule.get('aliases') and not body_rule.get('pattern'):raise ValueError('目标正文识别规则不可缺失，且不能由商品卡推定')
    overrides={x['uid']:x for x in c.get('body_overrides',[])}
    for a in rows:
        a['body_brands']=[b['name'] for b in brands if matches(a['body'],b)]
        a['body_target']=matches(a['body'],body_rule) if targets else False
        if a['uid'] in overrides:
            o=overrides[a['uid']]
            if not o.get('evidence') or o['evidence'] not in a['body'] or type(o.get('value')) is not bool:raise ValueError('正文判断修正缺少原文证据')
            a['body_target']=o['value']
        for x in a['cards']:
            ident=x['identity'];mp=mapping.get(ident)
            if mp:k=mp['product_key']
            else:
                k='unresolved:'+ident
                candidates=[b['name'] for b in brands if matches(x['title'],b)]
                if k not in catalog:catalog[k]={'key':k,'name':x['title'],'brand':candidates[0] if len(candidates)==1 else UNKNOWN,'resolved':False}
            x.update(product_key=k,brand=catalog[k]['brand'],uid=a['uid'])
    overall=group(rows,catalog,brands,c)
    providers=[p for p in ['豆包','元宝','千问'] if any(PLATFORMS[x['name']]==p for x in c['combinations'])]
    def sub(rs):return group(rs,catalog,brands,c)
    platforms=[{'provider':p,**sub([a for a in rows if a['provider']==p])} for p in providers]
    intents=[]
    for intent in dict.fromkeys(q['intent'] for q in c['questions']):
        qs=[q for q in c['questions'] if q['intent']==intent];rs=[a for a in rows if a['intent']==intent]
        intents.append({'name':intent,'questions':qs,'answers':len(rs),'platforms':[{'provider':p,**sub([a for a in rs if a['provider']==p])} for p in providers]})
    questions=[]
    for q in c['questions']:
        rs=[a for a in rows if a['question_id']==q['id']]
        questions.append({**q,**sub(rs),'platforms':[{'provider':p,**sub([a for a in rs if a['provider']==p])} for p in providers]})
    allp=overall['products']
    if c.get('brand'):peers=[p for p in allp if p['brand'] not in (c['brand'],UNKNOWN)][:5]
    else:peers=[p for p in allp if p['key'] not in targets and p['brand']!=UNKNOWN][:5]
    target_products=[]
    for k in c.get('target_keys',[]):target_products.append(next((p for p in allp if p['key']==k),{**catalog[k],**measure(rows,[],c.get('brand')),'rank':None}))
    structure=collections.Counter()
    for a in rows:
        for x in a['cards']:
            key='目标商品' if x['product_key'] in targets else '同品牌其他商品' if c.get('brand') and x['brand']==c['brand'] else '品牌待确认商品' if x['brand']==UNKNOWN else '其他品牌商品'
            structure[key]+=1
    ledger=[{'uid':a['uid'],'provider':a['provider'],'question_id':a['question_id'],'body_brands':a['body_brands'],'body_target':a['body_target'],'cards':a['cards']} for a in rows]
    return {'config':c,'input_digest':digest(data),'taxonomy_digest':digest(tax),'sampling':data['audit'],'sources':data['sources'],'overall':overall,'platforms':platforms,'intents':intents,'questions':questions,'brands':brands,'target_products':target_products,'peers':peers,'same_brand_products':[p for p in allp if p['brand']==c.get('brand')],'structure':dict(structure),'ledger':ledger}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--data',required=True);p.add_argument('--taxonomy',required=True);p.add_argument('--out',required=True);a=p.parse_args()
    model=build(read_json(a.data),read_json(a.taxonomy));write_json(a.out,model)
    print(json.dumps({'answers':model['overall']['answers'],'card_events':model['overall']['events'],'products':len(model['overall']['products']),'target_events':model['overall']['target']['events']},ensure_ascii=False))
