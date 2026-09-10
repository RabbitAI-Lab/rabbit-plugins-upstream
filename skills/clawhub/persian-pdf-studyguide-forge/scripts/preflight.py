#!/usr/bin/env python3
import importlib.util,json,shutil,subprocess
bins=['pdfinfo','pdftotext','pdftoppm','tesseract','node'];mods=['fitz','bs4','PIL']
report={'binaries':{x:shutil.which(x) for x in bins},'python':{x:bool(importlib.util.find_spec(x)) for x in mods}}
if report['binaries']['tesseract']:
 r=subprocess.run(['tesseract','--list-langs'],capture_output=True,text=True);report['tesseract_languages']=[x.strip() for x in r.stdout.splitlines()[1:] if x.strip()]
report['ready_required']=all(report['binaries'][x] for x in ['pdfinfo','pdftotext','pdftoppm','tesseract']) and {'fas','eng'}.issubset(set(report.get('tesseract_languages',[])))
report['install_hints']={'debian':'sudo apt-get install poppler-utils tesseract-ocr tesseract-ocr-fas tesseract-ocr-eng','python':'python -m pip install pymupdf beautifulsoup4 pillow'}
print(json.dumps(report,indent=2));raise SystemExit(0 if report['ready_required'] else 1)
