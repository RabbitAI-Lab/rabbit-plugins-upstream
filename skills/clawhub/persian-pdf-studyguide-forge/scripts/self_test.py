#!/usr/bin/env python3
import json,py_compile,re,subprocess,shutil,tempfile,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];errors=[]
for p in sorted((ROOT/'scripts').glob('*.py')):
 try:py_compile.compile(str(p),doraise=True)
 except Exception as e:errors.append(f'{p.name}: {e}')
for p in ['SKILL.md','README.md','AGENT_DISCOVERY.md','docs/WORKFLOW_PLAYBOOK.md','templates/guide.css','templates/app.js']:
 if not (ROOT/p).is_file():errors.append('missing '+p)
front=(ROOT/'SKILL.md').read_text()
for token in ['version: 1.3.0','categories:','topics:','requires:']:
 if token not in front:errors.append('SKILL frontmatter missing '+token)
if shutil.which('node'):
 r=subprocess.run(['node','--check',str(ROOT/'templates/app.js')],capture_output=True)
 if r.returncode:errors.append('app.js syntax: '+r.stderr.decode()[:120])
report={'pass':not errors,'python_scripts':len(list((ROOT/'scripts').glob('*.py'))),'errors':errors};print(json.dumps(report,indent=2));raise SystemExit(0 if not errors else 1)
