#!/usr/bin/env python3
"""Measured per-page fidelity signals: token coverage, order ratio, digit drift.
This is an audit aid, not proof of semantic identity; low pages require rendered-page adjudication.
"""
import argparse,collections,difflib,json,re
from pathlib import Path
from common import search_normalize
WORD=re.compile(r'[\w\u0600-\u06ff]+',re.UNICODE)
def toks(s):return WORD.findall(search_normalize(s))
ap=argparse.ArgumentParser();ap.add_argument('evidence',type=Path);ap.add_argument('corrected',type=Path);ap.add_argument('--out',type=Path,required=True);ap.add_argument('--coverage',type=float,default=.80);ap.add_argument('--order',type=float,default=.45);a=ap.parse_args()
ev=json.loads(a.evidence.read_text());co={int(k):v for k,v in json.loads(a.corrected.read_text()).items()};rows=[]
for x in ev:
 p=int(x['page']);src=toks((x.get('logical_normalized') or '')+' '+(x.get('ocr_normalized') or ''));dst=toks(co[p]['text']);cs,cd=collections.Counter(src),collections.Counter(dst);matched=sum(min(n,cd[w]) for w,n in cs.items());cov=matched/max(1,sum(cs.values()));ratio=difflib.SequenceMatcher(None,src,dst,autojunk=False).ratio() if src and dst else 0;sd=re.findall(r'\d+',search_normalize(' '.join(src)));dd=re.findall(r'\d+',search_normalize(' '.join(dst)));rows.append({'page':p,'coverage':round(cov,4),'order_ratio':round(ratio,4),'source_tokens':len(src),'corrected_tokens':len(dst),'source_digits':sd,'corrected_digits':dd,'needs_review':cov<a.coverage or ratio<a.order})
report={'pages':len(rows),'thresholds':{'coverage':a.coverage,'order':a.order},'needs_review':[x['page'] for x in rows if x['needs_review']],'rows':rows};a.out.write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps({'pages':len(rows),'needs_review':len(report['needs_review']),'output':str(a.out)},ensure_ascii=False))
