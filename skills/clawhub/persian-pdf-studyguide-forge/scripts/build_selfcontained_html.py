#!/usr/bin/env python3
"""Build the established offline RTL shell with source units and enrichment.
Images are embedded as data URIs by default; --linked-images keeps local paths.
"""
from __future__ import annotations
import argparse,base64,html,json,re
from pathlib import Path
from common import strip_option_prefix
ROOT=Path(__file__).resolve().parents[1]
def esc(x):return html.escape(str(x),quote=True)
def norm(x):return re.sub(r'\W+','',str(x).lower())
def main():
 ap=argparse.ArgumentParser();ap.add_argument('corrected',type=Path);ap.add_argument('extraction_dir',type=Path);ap.add_argument('enrichment',type=Path);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--title',required=True);ap.add_argument('--lead',default='راهنمای مرور امتحانی تعاملی');ap.add_argument('--skin',default='scrub');ap.add_argument('--linked-images',action='store_true');a=ap.parse_args()
 d={int(k):v for k,v in json.loads(a.corrected.read_text()).items()};packs=json.loads(a.enrichment.read_text());packs=sorted(packs,key=lambda x:x['session']);n=len(d)
 css=(ROOT/'templates/guide.css').read_text();js=(ROOT/'templates/app.js').read_text();images=sorted((a.extraction_dir/'display').glob('page-*.jpg'))
 if len(images)!=n:raise SystemExit(f'image count {len(images)} != corrected pages {n}')
 def imgsrc(p):
  if a.linked_images:return p.resolve().as_uri()
  return 'data:image/jpeg;base64,'+base64.b64encode(p.read_bytes()).decode()
 toc=[];nav=[];units=[]
 for i in range(1,n+1):
  title=d[i].get('title') or f'صفحهٔ {i}';text=d[i]['text'];toc.append(f'<li><a href="#u-{i}"><b>سند {i}</b><span>{esc(title)}</span></a></li>');nav.append(f'<a href="#u-{i}">{i}</a>')
  prev=f'<a href="#u-{i-1}">قبلی ›</a>' if i>1 else '<span></span>';nxt=f'<a href="#u-{i+1}">‹ بعدی</a>' if i<n else '<span></span>'
  units.append(f'<article class="source-unit" id="u-{i}"><details class="unit-fold" {"open" if i<=2 else ""}><summary><span class="unit-title">سند {i} · {esc(title)}</span><span class="fold-arrow">▾</span></summary><div class="unit-cols"><div class="page-text" dir="rtl"><h3><a href="#u-{i}" class="unit-anchor">#{i}</a> 📚</h3><pre dir="rtl">{esc(text)}</pre></div><div class="inline-figures"><figure><img loading="lazy" src="{imgsrc(images[i-1])}" alt="تصویر صفحه {i}: {esc(title)}"><figcaption>تصویر وفادار صفحهٔ {i}</figcaption></figure></div></div><p class="unit-nav">{prev}<a href="#text-toc">فهرست ↑</a>{nxt}</p></details></article>')
 seen={k:set() for k in ('tables','flash','mnemonics','review','quiz','bank')};tables=[];flash=[];mnems=[];reviews=[];quizzes=[];banks=[];qnum=bnum=0
 def ref(x,s,e):
  try:return min(e,max(s,int(x)))
  except:return s
 for pack in packs:
  s,e=int(pack['start']),int(pack['end']);c=pack['content']
  for t in c['tables']:
   k=norm(t['caption']);
   if k in seen['tables']:continue
   seen['tables'].add(k);tables.append('<div class="table-scroll"><table><caption>'+esc(t['caption'])+'</caption><thead><tr>'+''.join('<th scope="col">'+esc(x)+'</th>' for x in t['headers'])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+esc(x)+'</td>' for x in row)+'</tr>' for row in t['rows'])+'</tbody></table></div>')
  for x in c['flash']:
   k=norm(x['q']);
   if k in seen['flash']:continue
   seen['flash'].add(k);r=ref(x['ref'],s,e);flash.append(f'<details class="flash"><summary><span class="emoji">🧠</span>{esc(x["q"])}</summary><p>{esc(x["a"])} <span class="ref">📎 <a href="#u-{r}">سند {r}</a></span></p></details>')
  for x in c['mnemonics']:
   k=norm(x['title']);
   if k in seen['mnemonics']:continue
   seen['mnemonics'].add(k);r=ref(x['ref'],s,e);mnems.append(f'<article><h3>🔑 {esc(x["title"])}</h3><p>{esc(x["text"])} <span class="ref">📎 <a href="#u-{r}">سند {r}</a></span></p></article>')
  for x in c['review']:
   k=norm(x['text']);
   if k in seen['review']:continue
   seen['review'].add(k);r=ref(x['ref'],s,e);reviews.append(f'<li>{esc(x["text"])} <span class="ref">(سند <a href="#u-{r}">{r}</a>)</span></li>')
  for key,out,klass in [('quiz',quizzes,''),('bank',banks,'bank-item')]:
   for x in c[key]:
    k=norm(x['q']);
    if k in seen[key]:continue
    seen[key].add(k);r=ref(x['ref'],s,e);opts=''.join(f'<li data-letter="{chr(65+j)}">{esc(strip_option_prefix(o))}</li>' for j,o in enumerate(x['options']))
    if key=='quiz':qnum+=1;head=f'{qnum}. '
    else:bnum+=1;head=f'سناریو {bnum} — '
    out.append(f'<article class="{klass}" data-answer="{x["answer"]}"><h3>{head}{esc(x["q"])}</h3><ol type="A">{opts}</ol><details><summary>پاسخ و منطق</summary><strong class="g">گزینهٔ {x["answer"]}</strong> — {esc(x["why"])}<span class="ref">📎 <a href="#u-{r}">سند {r}</a></span></details></article>')
 session_map=''.join(f'<a href="#u-{x["start"]}"><b>جلسهٔ {x["session"]}</b> · {esc(x["name"])}</a>' for x in packs)
 counts={'tables':len(tables),'flash':len(flash),'mnemonics':len(mnems),'review':len(reviews),'quiz':len(quizzes),'bank':len(banks)};total=sum(counts.values())
 doc=f'''<!DOCTYPE html><html lang="fa" dir="rtl" data-skin="{esc(a.skin)}" data-file="01"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(a.title)} | مرور امتحانی</title><style>{css}</style></head><body><a class="skip-link" href="#text">پرش به آموزش</a><button id="themeToggle">🌓</button><header class="hero"><div class="inner"><span class="eyebrow">مرور امتحانی جامع</span><h1>{esc(a.title)}</h1><p class="lead">{esc(a.lead)}</p><ul class="stats"><li>📄 {n} سند</li><li>📊 {counts['tables']} جدول</li><li>🧠 {counts['flash']} فلش‌کارت</li><li>✍️ {counts['quiz']+counts['bank']} پرسش</li></ul></div></header><nav class="site-nav"><ul><li><a href="#overview">🗺️ نقشه</a></li><li><a href="#text">📚 آموزش</a></li><li><a href="#comparisons">📊 جدول‌ها</a></li><li><a href="#flashcards">🧠 فلش‌کارت</a></li><li><a href="#mnemonics">🔑 رمزها</a></li><li><a href="#review">⭐ خلاصه</a></li><li><a href="#quiz">✍️ آزمون</a></li><li><a href="#bank">🏁 چالش</a></li><li><a href="#search">🔍 جست‌وجو</a></li></ul></nav><main><section id="search"><div class="section-head"><span>🔍 جست‌وجو</span></div><div class="search-panel"><input type="search" placeholder="جست‌وجو در همهٔ اسناد"><p class="search-hits"></p></div></section><section id="overview"><div class="section-head"><span>🗺️ نقشهٔ مرور</span></div><div class="roadmap">{session_map}</div><ol class="toc-cards">{''.join(toc)}</ol></section><section id="text"><div class="section-head"><span>📚 آموزش</span><small>متن ویراسته + تصویر منبع</small></div><div class="unit-toc" id="text-toc"><div class="toc-tools"><button data-act="openall">بازکردن همه</button><button data-act="closeall">بستن همه</button></div>{''.join(nav)}</div>{''.join(units)}</section><section id="comparisons"><div class="section-head"><span>📊 جدول‌ها</span><small>{counts['tables']} جدول</small></div>{''.join(tables)}</section><section id="flashcards"><div class="section-head"><span>🧠 فلش‌کارت</span><small>{counts['flash']} کارت</small></div><div class="flash-grid">{''.join(flash)}</div></section><section id="mnemonics"><div class="section-head"><span>🔑 رمزها</span><small>{counts['mnemonics']} کمک‌حافظه</small></div><div class="mnemonic-grid">{''.join(mnems)}</div></section><section id="review"><div class="section-head"><span>⭐ خلاصه</span><small>{counts['review']} نکته</small></div><ul>{''.join(reviews)}</ul></section><section id="quiz"><div class="section-head"><span>✍️ مینی‌آزمون</span><small>{counts['quiz']} پرسش</small></div><div class="qbar"><span class="score">—</span><button data-act="expand">پاسخ‌ها</button><button data-act="collapse">بستن</button><button data-act="reset">شروع دوباره</button></div><div class="qitems">{''.join(quizzes)}</div></section><section id="bank"><div class="section-head"><span>🏁 چالش</span><small>{counts['bank']} سناریو</small></div><div class="bank-items">{''.join(banks)}</div></section></main><footer class="site-footer"><p>{n} سند و {total} مؤلفهٔ مرور فعال؛ خودبسنده و آفلاین.</p></footer><button id="toTop">↑</button><script>{js}</script></body></html>'''
 a.output.write_text(doc,'utf8');print(json.dumps({'output':str(a.output),'pages':n,'counts':counts,'total':total,'bytes':a.output.stat().st_size},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
