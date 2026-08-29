#!/usr/bin/env python3
"""Create and verify a fresh ZIP; PDFs excluded unless --include-pdf."""
import argparse,hashlib,json,os,zipfile
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('directory',type=Path);ap.add_argument('zipfile',type=Path);ap.add_argument('--include-pdf',action='store_true');a=ap.parse_args();root=a.directory.resolve();files=[]
for p in sorted(x for x in root.rglob('*') if x.is_file()):
 if p.resolve()==a.zipfile.resolve():continue
 if not a.include_pdf and p.suffix.lower()=='.pdf':continue
 if any(part.startswith('.') for part in p.relative_to(root).parts):continue
 files.append(p)
a.zipfile.parent.mkdir(parents=True,exist_ok=True)
with zipfile.ZipFile(a.zipfile,'w',zipfile.ZIP_DEFLATED,allowZip64=True) as z:
 for p in files:z.write(p,p.relative_to(root))
with zipfile.ZipFile(a.zipfile) as z:
 bad=z.testzip();names=set(z.namelist())
expected={str(p.relative_to(root)) for p in files};missing=expected-names;extra=names-expected
if bad or missing or extra:raise SystemExit(f'ZIP verification failed: bad={bad} missing={missing} extra={extra}')
h=hashlib.sha256(a.zipfile.read_bytes()).hexdigest();Path(str(a.zipfile)+'.sha256').write_text(f'{h}  {a.zipfile.name}\n');print(json.dumps({'zip':str(a.zipfile),'files':len(files),'bytes':a.zipfile.stat().st_size,'sha256':h},indent=2))
