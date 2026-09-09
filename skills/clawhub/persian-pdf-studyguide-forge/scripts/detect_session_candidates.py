#!/usr/bin/env python3
"""Suggest session boundaries from corrected titles/text; never guesses silently.
Review and copy accepted boundaries into sessions.json before enrichment.
"""
import argparse,json,re
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('corrected',type=Path);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
d={int(k):v for k,v in json.loads(a.corrected.read_text()).items()}
c=[]
for p,x in sorted(d.items()):
 hay=(x.get('title','')+'\n'+x.get('text','')[:500])
 score=sum(bool(re.search(k,hay,re.I)) for k in [r'جلسه\s*(?:اول|دوم|سوم|چهار|پنج|شش|هفت|هشت|نه|ده|یازده|دوازده|سیزده|چهارده|پانزده|شانزده|هفده|هجده|نوزده|بیست|\d+)',r'ترم\s+',r'استاد\s*:',r'نویسنده\s*:'])
 if score>=2:c.append({'page':p,'score':score,'suggested_name':x.get('title','')})
a.out.write_text(json.dumps({'review_required':True,'candidates':c},ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'candidates':len(c),'output':str(a.out)},ensure_ascii=False))
