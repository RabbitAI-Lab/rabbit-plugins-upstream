#!/usr/bin/env python3
"""Measured QA gates for a generated guide. Exit 0 only when every gate passes."""
import argparse,json,re,shutil,subprocess,tempfile
from pathlib import Path
try:from bs4 import BeautifulSoup
except ImportError:raise SystemExit('install beautifulsoup4 for QA: python -m pip install beautifulsoup4')
ap=argparse.ArgumentParser();ap.add_argument('html',type=Path);ap.add_argument('--expected-pages',type=int);a=ap.parse_args();s=BeautifulSoup(a.html.read_text('utf8'),'html.parser');results=[]
def gate(name,ok,detail=''):results.append({'gate':name,'pass':bool(ok),'detail':detail})
units=s.select('.source-unit');ids=[x.get('id') for x in s.select('[id]')]
gate('source-unit-count',not a.expected_pages or len(units)==a.expected_pages,f'{len(units)}')
gate('unique-ids',len(ids)==len(set(ids)),f'{len(ids)-len(set(ids))} duplicates')
missing=[]
for x in s.select('a[href^="#"]'):
 h=x.get('href');
 if h!='#' and not s.select_one(h):missing.append(h)
gate('fragment-links',not missing,f'{len(missing)} missing')
q=s.select('#quiz article,#bank article');bad=[]
for i,x in enumerate(q,1):
 refs=[r for r in x.select('.ref a[href^="#u-"]')]
 if len(x.select('ol[type="A"] li'))!=4 or x.get('data-answer') not in 'ABCD' or not refs:bad.append(i)
gate('question-contract',not bad,f'{len(q)} questions; {len(bad)} bad')
imgs=s.select('.source-unit img');badimg=[x.get('src','') for x in imgs if not (x.get('src','').startswith('data:image/') or x.get('src','').startswith('file:') or Path(x.get('src','')).exists())]
gate('images',len(imgs)==len(units) and not badimg,f'{len(imgs)} images')
text=s.get_text();gate('no-bidi-or-replacement',not re.search(r'�|[\u202a-\u202e\u200e\u200f]',text))
external=[x for x in s.select('[src]') if re.match(r'https?://',x.get('src',''))]
gate('offline-no-external-src',not external,f'{len(external)} external')
for t in s.select('table'):
 n=len(t.select('thead th'))
 if n<2 or any(len(r.select('td'))!=n for r in t.select('tbody tr')):bad.append('table')
gate('table-contract','table' not in bad,f'{len(s.select("table"))} tables')
# Exact duplicate authored items after removing references.
for name,sel in [('table','#comparisons caption'),('flash','#flashcards summary'),('mnemonic','#mnemonics h3'),('quiz','#quiz article h3'),('bank','#bank article h3')]:
 vals=[re.sub(r'\W+','',x.get_text(' ',strip=True).lower()) for x in s.select(sel)];gate('dedup-'+name,len(vals)==len(set(vals)),f'{len(vals)-len(set(vals))} duplicates')
# JS syntax when Node is available.
if shutil.which('node') and s.find_all('script'):
 with tempfile.NamedTemporaryFile('w',suffix='.js',delete=False) as f:f.write(s.find_all('script')[-1].string or '');fn=f.name
 r=subprocess.run(['node','--check',fn],capture_output=True);Path(fn).unlink(missing_ok=True);gate('javascript-syntax',r.returncode==0,r.stderr.decode(errors='replace')[:100])
# Declared section counters must contain measured numbers.
for sid,sel in [('comparisons','table'),('flashcards','details.flash'),('mnemonics','article'),('review','li'),('quiz','article'),('bank','article')]:
 n=len(s.select(f'#{sid} {sel}'));label=s.select_one(f'#{sid} .section-head').get_text(' ',strip=True);gate('counter-'+sid,str(n) in label,f'measured {n}')
# Flashcards must carry a real answer — never a bare letter like 'A' (v1.3.0).
bare_flash=[]
for x in s.select('#flashcards details.flash'):
    p=x.select_one('p');txt=''
    if p:
        ref=p.select_one('.ref')
        if ref: ref.decompose()
        txt=re.sub(r'\s+','',p.get_text(' ',strip=True))
    if not txt or re.fullmatch(r'[A-Da-d]',txt) or (len(txt)<=2 and not re.search(r'\d',txt)):
        bare_flash.append(x.select_one('summary').get_text(' ',strip=True)[:40] if x.select_one('summary') else '?')
gate('flash-no-bare-answer',not bare_flash,f'{len(bare_flash)} bare')
# Quiz/bank options must not repeat the shell's A-D label as their own prefix.
prefixed=[]
for x in s.select('#quiz article ol li,#bank article ol li'):
    t=x.get_text(' ',strip=True)
    if re.match(r'^(?:الف|[بجدا]|[پتث]|[۱-۴1-4]|[A-Da-d])\s*[).\-:]',t):
        prefixed.append(t[:40])
gate('quiz-options-no-letter-prefix',not prefixed,f'{len(prefixed)} prefixed')
report={'html':str(a.html),'passed':sum(x['pass'] for x in results),'total':len(results),'gates':results};print(json.dumps(report,ensure_ascii=False,indent=2));raise SystemExit(0 if report['passed']==report['total'] else 1)
