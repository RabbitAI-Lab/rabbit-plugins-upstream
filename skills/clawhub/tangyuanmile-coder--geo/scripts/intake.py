"""Normalize local JSONL/ZIP exports or saved API/MCP responses; no network calls."""
import argparse, collections, hashlib, html, json, re, zipfile
from datetime import datetime
from zoneinfo import ZoneInfo
from html.parser import HTMLParser
from pathlib import Path
from common import *

MARKER=re.compile(r'render_ecom_card_widget_(\w+)_start:')
FIELDS={'product':('pid','text','seller_name','jump_url'),'jd':('sku','sku_name','shop_name','pc_url'),'taobao':('item_id','title','shop_name','jump_url')}
class TextOnly(HTMLParser):
    def __init__(self):super().__init__();self.parts=[];self.skip=0
    def handle_starttag(self,tag,attrs):
        if tag in ('script','style'):self.skip+=1
        elif tag in ('p','br','div','li'):self.parts.append('\n')
    def handle_endtag(self,tag):
        if tag in ('script','style') and self.skip:self.skip-=1
    def handle_data(self,s):
        if not self.skip:self.parts.append(s)

def clean_body(s):
    s=re.sub(r'!?\[([^\]]*)\]\(https?://[^)]*\)',r'\1',s)
    s=re.sub(r'\[\]\(@[^)]*\)','',s)
    s=re.sub(r'https?://[^\s<>]+','',s)
    p=TextOnly();p.feed(s);return html.unescape(''.join(p.parts)).replace('**','').replace('__','')

def price(v):
    if v is None or v=='':return None
    s=str(v).strip().replace(',','')
    m=re.fullmatch(r'(?:¥|￥)?\s*(\d+(?:\.\d+)?)\s*元?',s)
    return float(m[1]) if m else None

def extract(s):
    cards=[];spans=[];seen=set();ignored=collections.Counter();decoder=json.JSONDecoder()
    for m in MARKER.finditer(s):
        tail=s[m.end():];start=m.end()+len(tail)-len(tail.lstrip())
        try:items,used=decoder.raw_decode(s[start:])
        except json.JSONDecodeError as ex:raise ValueError('商品卡标记内JSON不完整，须修复或明确排除该回答') from ex
        endmark='render_ecom_card_widget_'+m[1]+'_end:';end=s.find(endmark,start+used)
        if end<0:raise ValueError('商品卡结束标记缺失')
        if s[start+used:end].strip():raise ValueError('商品卡标记存在未解析文本')
        spans.append((m.start(),end+len(endmark)))
        if not isinstance(items,list):raise ValueError('商品卡集合必须是数组')
        if m[1] not in FIELDS:ignored[m[1]]+=len(items);continue
        idf,tf,sf,lf=FIELDS[m[1]]
        for item in items:
            if not isinstance(item,dict) or not isinstance(item.get(tf),str) or not item[tf].strip():raise ValueError('有效商品卡缺少可核验商品名称')
            title=item[tf].strip();shop=str(item.get(sf) or '未提供店铺');url=str(item.get(lf) or item.get('auctionURL') or '')
            ident=m[1]+':'+str(item[idf]) if item.get(idf) not in (None,'') else m[1]+':fallback-'+digest([title,shop,url])[:24]
            if ident in seen:continue
            seen.add(ident)
            # Position is the first occurrence order among valid, deduplicated product cards.
            cards.append({'identity':ident,'kind':m[1],'title':title,'shop':shop,'source':{'jd':'京东商城','taobao':'淘宝商城','product':'电商来源未提供'}[m[1]],'price':price(item.get('price')),'price_raw':item.get('price'),'url':url,'position':len(cards)+1})
    for a,b in reversed(spans):s=s[:a]+s[b:]
    if 'render_ecom_card_widget_' in s:raise ValueError('存在未识别的商品卡标记，禁止当作正文统计')
    return clean_body(s),cards,dict(ignored)

def date_of(value):
    if isinstance(value,(int,float)):
        return datetime.fromtimestamp(value/1000 if value>1e12 else value,ZoneInfo('Asia/Shanghai')).date().isoformat()
    value=str(value or '')
    if len(value)>=10:
        d=datetime.fromisoformat(value.replace('Z','+00:00'))
        if d.tzinfo:d=d.astimezone(ZoneInfo('Asia/Shanghai'))
        return d.date().isoformat()
    raise ValueError('回答缺少可核验的采样日期')

def unpack(r,src):
    """Never infer platform or thinking mode from answer prose or the input filename."""
    code=r.get('name') or EXPORT_CODES.get(r.get('platform'),r.get('platform')) or src.get('name')
    mode=r.get('thinking_enabled',r.get('thinkingEnabled',src.get('thinking_enabled')))
    if mode in ('0','1'):mode=int(mode)
    if mode not in (0,1):raise ValueError('原始数据未带模式，请在来源配置中明确0/1')
    if src.get('thinking_enabled') is not None and mode!=src['thinking_enabled']:raise ValueError('来源配置与记录中的思考模式冲突')
    data=r.get('data',r)
    status=data.get('status',r.get('status','SUCCESS' if 'content' in r else None))
    prompt=r.get('prompt') or data.get('prompt')
    when=r.get('created_at',r.get('date',data.get('fetch_time')))
    if 'content' in r:body=r['content']
    else:
        result=data.get('result',[])
        if isinstance(result,str):result=json.loads(result)
        if not isinstance(result,list):raise ValueError('API result必须是数组')
        chunks=[x['context'] for x in result if isinstance(x,dict) and 'context' in x]
        if any(not isinstance(x,str) for x in chunks):raise ValueError('context必须是字符串')
        body='\n'.join(chunks)
    return code,mode,status,prompt,when,body

def source_records(src,base):
    p=relative(base,src['path']);raw=p.read_bytes();sha=hashlib.sha256(raw).hexdigest()
    if p.suffix.lower()=='.zip':
        with zipfile.ZipFile(p) as z:
            member=src.get('member')
            if not member or member not in z.namelist():raise ValueError('ZIP必须明确选择真实存在的成员文件')
            raw=z.read(member)
    else:member=''
    text=raw.decode('utf-8-sig')
    if p.suffix.lower()=='.json' and not member:
        o=json.loads(text);rs=list(enumerate(o if isinstance(o,list) else [o],1))
    else:rs=[(i,json.loads(x)) for i,x in enumerate(text.split('\n'),1) if x.strip()]
    for i,r in rs:yield r,sha,member,i

def normalize(c,base):
    validate_config(c);allowed={(x['name'],x['thinking_enabled']) for x in c['combinations']}
    qmap={q['prompt']:q for q in c['questions']};answers=[];excluded=collections.Counter();seen={};ignored=collections.Counter();sources=[]
    for src in c.get('sources',[]):
        p=relative(base,src['path']);sources.append({'file':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'member':src.get('member')})
        for r,sha,member,line in source_records(src,base):
            code,mode,status,prompt,when,body=unpack(r,src)
            if (code,mode) not in allowed:excluded['不在本次支持组合范围']+=1;continue
            if prompt not in qmap:excluded['不在已确认题库']+=1;continue
            if status!='SUCCESS':excluded['未成功完成']+=1;continue
            if date_of(when)!=c['date']:excluded['不在采样日']+=1;continue
            if not isinstance(body,str) or not body.strip():raise ValueError('成功回答缺少正文，须核验数据完整性')
            # Structured productVos requires a separately verified adapter; never silently count it as no-card.
            if r.get('productVos') and not MARKER.search(body):raise ValueError('本数据使用productVos；请按其真实schema编写并验证适配器后再统计')
            req_info=r.get('req_info')
            if isinstance(req_info,str):
                try:req_info=json.loads(req_info)
                except json.JSONDecodeError:req_info={}
            rid=r.get('reqId') or (req_info.get('req_id') if isinstance(req_info,dict) else None)
            uid=str(rid or (sha+':'+member+':'+str(line)))
            sig=digest([code,mode,prompt,when,body])
            if uid in seen:
                if seen[uid]!=sig:raise ValueError('同一回答ID出现冲突结果')
                excluded['重复导入同一回答']+=1;continue
            seen[uid]=sig;clean,cards,ig=extract(body);ignored.update(ig)
            answers.append({'uid':uid,'date':c['date'],'name':code,'thinking_enabled':mode,'provider':PLATFORMS[code],'question_id':qmap[prompt]['id'],'prompt':prompt,'intent':qmap[prompt]['intent'],'body':clean,'cards':cards,'source_sha256':sha,'source_member':member,'source_line':line})
    if not answers:raise ValueError('没有符合已确认范围的有效回答')
    actual=collections.Counter((a['question_id'],a['name'],a['thinking_enabled']) for a in answers)
    matrix=[{'question_id':q['id'],'name':code,'thinking_enabled':mode,'expected':c['repeats'],'actual':actual[(q['id'],code,mode)]} for q in c['questions'] for code,mode in [tuple((x['name'],x['thinking_enabled'])) for x in c['combinations']]]
    return {'config':c,'sources':sources,'answers':answers,'audit':{'excluded':dict(excluded),'non_product_cards':dict(ignored),'sampling_matrix':matrix,'complete':all(x['actual']==x['expected'] for x in matrix)}}

def inventory(data):
    inv={}
    for a in data['answers']:
        for c in a['cards']:
            x=inv.setdefault(c['identity'],{'titles':{},'events':0,'shops':[]})
            x['titles'][c['title']]=x['titles'].get(c['title'],0)+1;x['events']+=1
            if c['shop'] not in x['shops']:x['shops'].append(c['shop'])
    return inv
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--config',required=True);p.add_argument('--out',required=True);args=p.parse_args()
    data=normalize(read_json(args.config),args.config);out=Path(args.out);write_json(out/'normalized.json',data);write_json(out/'card_inventory.json',inventory(data))
    print(json.dumps({'answers':len(data['answers']),'card_events':sum(len(a['cards']) for a in data['answers']),'complete':data['audit']['complete']},ensure_ascii=False))
