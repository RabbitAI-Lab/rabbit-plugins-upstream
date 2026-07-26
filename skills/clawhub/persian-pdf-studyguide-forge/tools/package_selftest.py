#!/usr/bin/env python3
from pathlib import Path
import sys
try:
    import yaml
except ImportError:
    yaml = None
root=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
p=root/'SKILL.md'
text=p.read_text(encoding='utf-8')
def fail(s): print('FAIL:',s); raise SystemExit(1)
if not text.startswith('---\n') or '\n---\n' not in text[4:]: fail('frontmatter missing')
if yaml is None: fail('PyYAML unavailable')
data=yaml.safe_load(text[4:text.find('\n---\n',4)])
if data.get('name')!='persian-pdf-studyguide-forge': fail('name mismatch')
for key in ('file_read','file_write','network','shell'):
    if key not in data.get('permissions',{}): fail('missing permission '+key)
for rel in ('templates/build_manifest.yaml','templates/source_unit.html'):
    if not (root/rel).is_file(): fail('missing '+rel)
print('PASS: Persian PDF StudyGuide Forge package self-test passed')
