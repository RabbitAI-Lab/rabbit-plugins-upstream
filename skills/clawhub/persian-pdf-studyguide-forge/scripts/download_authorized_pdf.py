#!/usr/bin/env python3
"""Download an operator-authorized PDF without exposing credentials.
Follows redirects, enforces HTTPS by default, caps size, verifies %PDF magic,
and records source URL + SHA-256. It never scrapes or guesses credentials.
"""
import argparse, hashlib, json, urllib.parse, urllib.request
from pathlib import Path

def main():
    ap=argparse.ArgumentParser();ap.add_argument('url');ap.add_argument('output',type=Path)
    ap.add_argument('--max-mb',type=int,default=256);ap.add_argument('--allow-http',action='store_true')
    a=ap.parse_args();u=urllib.parse.urlparse(a.url)
    if u.scheme!='https' and not a.allow_http:raise SystemExit('HTTPS required (or explicit --allow-http)')
    req=urllib.request.Request(a.url,headers={'User-Agent':'PersianPDFStudyGuideForge/1.2'})
    h=hashlib.sha256();size=0;a.output.parent.mkdir(parents=True,exist_ok=True)
    with urllib.request.urlopen(req,timeout=180) as r,open(a.output,'wb') as f:
        final=r.geturl()
        while True:
            b=r.read(1024*1024)
            if not b:break
            size+=len(b)
            if size>a.max_mb*1024*1024:raise SystemExit('download exceeds --max-mb')
            h.update(b);f.write(b)
    if a.output.read_bytes()[:5]!=b'%PDF-':a.output.unlink(missing_ok=True);raise SystemExit('download is not a PDF')
    meta={'requested_url':a.url,'final_url':final,'bytes':size,'sha256':h.hexdigest()}
    (a.output.parent/(a.output.name+'.download.json')).write_text(json.dumps(meta,indent=2),'utf8')
    print(json.dumps(meta,indent=2))
if __name__=='__main__':main()
