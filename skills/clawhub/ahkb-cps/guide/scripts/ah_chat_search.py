#!/usr/bin/env python3
"""ahkb-cps 知识库检索引擎 v2 — 预建索引 + chunk检索 + 追问上下文"""
import sys, json, re, time, argparse, os
if hasattr(sys.stdout, 'reconfigure'): sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path
try: import jieba, jieba.analyse
except ImportError: jieba = None

INDEX_FILE = '临时工作文件/ah_chat_index.json'

def parse_frontmatter(content):
    m = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if not m: return {}, content.strip()
    fm_text, body = m.group(1), m.group(2).strip()
    fm = {'tags': []}
    tags_m = re.search(r'tags:\s*\[(.*?)\]', fm_text)
    if tags_m: fm['tags'] = [t.strip() for t in tags_m.group(1).split(',') if t.strip()]
    for field in ['summary','source','unit_id','created','updated','kb_name']:
        m2 = re.search(rf'^{field}:\s*(.*?)$', fm_text, re.MULTILINE)
        fm[field] = m2.group(1).strip() if m2 else ''
    return fm, body

def extract_keywords(text, topK=15):
    if not text.strip(): return []
    if jieba: return jieba.analyse.extract_tags(text, topK=topK)
    words = re.findall(r'[一-鿿]{2,}', text)
    return list(dict.fromkeys(words))[:topK]

def rebuild_index(kb_dir):
    kb = Path(kb_dir); units = []; errors = []
    kdir = kb / '知识元'
    if kdir.is_dir():
        for f in sorted(kdir.glob('*.md')):
            try:
                c = f.read_text(encoding='utf-8')
                fm, body = parse_frontmatter(c)
                title_m = re.match(r'^#\s+(.*?)$', body, re.MULTILINE)
                title = title_m.group(1).strip() if title_m else f.stem
                preview = re.sub(r'[#*`\[\]]+', '', body)[:300].strip()
                kw = extract_keywords(f"{title} {' '.join(fm.get('tags',[]))} {fm.get('summary','')} {preview[:200]}", 25)
                units.append({'type':'knowledge_unit','filename':f.stem,'title':title,'tags':fm.get('tags',[]),
                    'summary':fm.get('summary',''),'source':fm.get('source',''),'unit_id':fm.get('unit_id',''),
                    'kb_name':fm.get('kb_name',''),'body_preview':preview,'body_length':len(body),'keywords':kw})
            except Exception as e: errors.append(f"知识元解析失败 {f.name}: {e}")
    cdir = kb / 'chunks'
    if cdir.is_dir():
        for f in sorted(cdir.glob('*.json')):
            try:
                data = json.loads(f.read_text('utf-8'))
                for c in data.get('chunks', []):
                    text = (c.get('text','') or '')[:300]
                    preview = re.sub(r'[#*`\[\]]+', '', text).strip()
                    kw = extract_keywords(f"{c.get('heading','')} {preview[:150]}", 15)
                    units.append({'type':'chunk','filename':c.get('chunk_id',f.stem),'title':c.get('heading',f.stem),
                        'tags':c.get('tags',[]),'summary':c.get('heading',''),'source':data.get('source_file',''),
                        'unit_id':'','kb_name':'','body_preview':preview[:200],'body_length':c.get('word_count',len(text)),'keywords':kw})
            except: pass
    inverted = {}
    for idx, u in enumerate(units):
        for kw in u.get('keywords',[]):
            inverted.setdefault(kw, []).append(idx)
    index_data = {'version':2,'built_at':time.strftime('%Y-%m-%dT%H:%M:%S'),'kb_dir':str(kb.resolve()),
        'unit_count':len(units),'units':units,'inverted_index':inverted}
    index_path = kb / INDEX_FILE
    index_path.parent.mkdir(parents=True, exist_ok=True)
    index_path.write_text(json.dumps(index_data, ensure_ascii=False, indent=2), encoding='utf-8')
    return {'status':'ok','units_built':len([u for u in units if u['type']=='knowledge_unit']),
        'chunks_built':len([u for u in units if u['type']=='chunk']),'keywords_indexed':len(inverted),
        'errors':errors[:5] if errors else [],'index_path':str(index_path)}, units

def index_is_fresh(kb_dir):
    """简化版：索引存在即视为有效（用户通过 --rebuild-index 手动刷新）"""
    ip = Path(kb_dir) / INDEX_FILE
    return ip.is_file()

def ensure_loaded(kb_dir):
    """加载数据：索引存在就用索引（快），否则动态加载"""
    ip = Path(kb_dir) / INDEX_FILE
    if ip.is_file():
        try:
            data = json.loads(ip.read_text('utf-8'))
            return data.get('units',[]), data, []
        except: pass
    units, errors = [], []
    kdir = Path(kb_dir) / '知识元'
    if kdir.is_dir():
        for f in sorted(kdir.glob('*.md')):
            try:
                c = f.read_text('utf-8'); fm, body = parse_frontmatter(c)
                title_m = re.match(r'^#\s+(.*?)$', body, re.MULTILINE)
                title = title_m.group(1).strip() if title_m else f.stem
                preview = re.sub(r'[#*`\[\]]+','',body)[:300].strip()
                kw = extract_keywords(f"{title} {' '.join(fm.get('tags',[]))} {fm.get('summary','')} {preview[:200]}", 25)
                units.append({'type':'knowledge_unit','filename':f.stem,'title':title,'tags':fm.get('tags',[]),
                    'summary':fm.get('summary',''),'source':fm.get('source',''),'unit_id':fm.get('unit_id',''),
                    'kb_name':fm.get('kb_name',''),'body_preview':preview,'body_length':len(body),'keywords':kw})
            except: pass
    cdir = Path(kb_dir) / 'chunks'
    if cdir.is_dir():
        for f in sorted(cdir.glob('*.json')):
            try:
                data = json.loads(f.read_text('utf-8'))
                for c in data.get('chunks',[]):
                    text = (c.get('text','') or '')[:300]; preview = re.sub(r'[#*`\[\]]+','',text).strip()
                    units.append({'type':'chunk','filename':c.get('chunk_id',f.stem),'title':c.get('heading',f.stem),
                        'tags':c.get('tags',[]),'summary':c.get('heading',''),'source':data.get('source_file',''),
                        'unit_id':'','kb_name':'','body_preview':preview[:200],'body_length':c.get('word_count',len(text)),
                        'keywords':extract_keywords(f"{c.get('heading','')} {preview[:150]}",15)})
            except: pass
    if not units: errors.append("知识库尚未构建，请先用知识库构建模块入库")
    return units, None, errors

def score_item(item, keywords, query_text, narrow_set=None):
    nb = 1.0
    if narrow_set is not None:
        nb = 1.5 if (item['filename'] in narrow_set or item['title'] in narrow_set) else 0.3
    t = f"{item['title']} {item['filename']}".lower()
    tg = ' '.join(item['tags']).lower()
    s = item['summary'].lower()
    b = item.get('body_preview','').lower()
    def hit(kws, txt):
        if not kws: return 0
        return min(sum(1 for kw in kws if kw.lower() in txt)/len(kws),1.0)
    return round((hit(keywords,t)*0.30+hit(keywords,tg)*0.25+hit(keywords,s)*0.25+hit(keywords,b)*0.20)*nb,4)

def search(kb_dir, query, top_k=8, min_score=0.02, narrow=None):
    start = time.time()
    units, idx_data, errors = ensure_loaded(kb_dir)
    if not units: return {'status':'empty','message':errors[0] if errors else '知识库为空','results':[],'errors':errors}
    keywords = extract_keywords(query)
    if len(keywords) < 3:
        for w in re.findall(r'[一-鿿]{2,}', query):
            if w not in keywords: keywords.append(w)
    narrow_set = set(n.strip() for n in narrow.split(',')) if narrow else None
    scored = [(s,u) for u in units if (s:=score_item(u,keywords,query,narrow_set)) >= (min_score*0.8 if narrow_set else min_score)]
    scored.sort(key=lambda x:(-x[0],-x[1].get('body_length',0)))
    top = scored[:top_k]
    uc = sum(1 for u in units if u['type']=='knowledge_unit')
    cc = sum(1 for u in units if u['type']=='chunk')
    return {'status':'ok','query':query,'keywords':keywords[:15],'total_items':len(units),
        'knowledge_units':uc,'chunks':cc,'matched_items':len(scored),'narrow':bool(narrow_set),
        'narrow_items':len(narrow_set) if narrow_set else 0,
        'top_results':[{'rank':i+1,'score':s,'type':u['type'],'title':u['title'],'filename':u['filename'],
            'tags':u.get('tags',[]),'summary':u.get('summary',''),'source':u.get('source',''),
            'body_preview':u.get('body_preview','')} for i,(s,u) in enumerate(top)],
        'search_time_ms':int((time.time()-start)*1000),
        'warnings':errors[:3] if errors else []}

def cmd_status(kb_dir):
    ip = Path(kb_dir) / INDEX_FILE; ie = ip.is_file(); fr = index_is_fresh(kb_dir) if ie else False
    kdir = Path(kb_dir) / '知识元'; uf = len(list(kdir.glob('*.md'))) if kdir.is_dir() else 0
    cdir = Path(kb_dir) / 'chunks'; cf = len(list(cdir.glob('*.json'))) if cdir.is_dir() else 0
    return {'status':'ready' if uf>0 or cf>0 else 'empty','kb_dir':str(Path(kb_dir).resolve()),
        'knowledge_units':uf,'chunk_files':cf,'index':{'exists':ie,'fresh':fr,'needs_rebuild':ie and not fr},
        'message':'知识库就绪' if uf>0 else '知识库为空，请先用知识库构建模块入库'}

def main():
    p = argparse.ArgumentParser(description='AH-Chat 知识库检索 v2')
    p.add_argument('query', nargs='?', default='')
    p.add_argument('--workspace','-w', default=None)
    p.add_argument('--top-k','-k', type=int, default=8)
    p.add_argument('--min-score','-m', type=float, default=0.02)
    p.add_argument('--status', action='store_true')
    p.add_argument('--rebuild-index', action='store_true')
    p.add_argument('--narrow', default=None)
    args = p.parse_args()
    kb_dir = args.workspace or str(Path.cwd())
    if args.rebuild_index: print(json.dumps(rebuild_index(kb_dir)[0], ensure_ascii=False)); return
    if args.status or not args.query: print(json.dumps(cmd_status(kb_dir), ensure_ascii=False)); return
    print(json.dumps(search(kb_dir,args.query,top_k=args.top_k,min_score=args.min_score,narrow=args.narrow), ensure_ascii=False))

if __name__ == '__main__': main()
