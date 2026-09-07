#!/usr/bin/env python3
"""Classify candidate figures without deleting them. Requires Pillow.
Flags tiny (<5% reference page area), extreme aspect, exact duplicates, and
high-frequency repeated template assets. Human review decides final use.
"""
import argparse,hashlib,json
from collections import Counter
from pathlib import Path
try:from PIL import Image
except ImportError:raise SystemExit('install Pillow: python -m pip install pillow')
ap=argparse.ArgumentParser();ap.add_argument('directory',type=Path);ap.add_argument('--page-width',type=int,required=True);ap.add_argument('--page-height',type=int,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();rows=[]
for p in sorted(x for x in a.directory.rglob('*') if x.suffix.lower() in ('.png','.jpg','.jpeg','.webp')):
 try:
  with Image.open(p) as im:w,h=im.size
 except Exception:continue
 digest=hashlib.sha256(p.read_bytes()).hexdigest();frac=w*h/(a.page_width*a.page_height);reasons=[]
 if frac<.05:reasons.append('tiny-under-5-percent')
 if max(w/h,h/w)>8:reasons.append('extreme-aspect-logo-or-rule')
 rows.append({'file':str(p),'width':w,'height':h,'area_fraction':round(frac,4),'sha256':digest,'reasons':reasons})
freq=Counter(x['sha256'] for x in rows)
for x in rows:
 if freq[x['sha256']]>2:x['reasons'].append('repeated-template-or-logo')
 x['classification']='review-decoration' if x['reasons'] else 'candidate-educational'
a.out.write_text(json.dumps({'files':rows},indent=2));print(json.dumps(Counter(x['classification'] for x in rows)))
